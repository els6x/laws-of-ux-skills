#!/usr/bin/env python3
"""
ux_check.py — mechanical checks for the Laws of UX skill.

Checks the things a human eye is bad at: contrast ratios, whether spacing values
actually belong to a scale, how many type sizes and radii are in use, and a
handful of structural/accessibility facts in HTML.

It does NOT judge design. It reports facts so the design judgement can be made
against them. Exit code is 0 unless --strict is passed and problems were found.

Usage:
    python ux_check.py contrast "#475569" "#ffffff"
    python ux_check.py roles path/to/adapter.css     # validate the 21-role contract
    python ux_check.py css path/to/styles.css
    python ux_check.py html path/to/index.html
    python ux_check.py all path/to/project
    python ux_check.py scale            # print the reference scales

Options:
    --strict    exit 1 when any problem is reported
    --json      machine-readable output
"""

import json
import re
import sys
from pathlib import Path

# ----------------------------------------------------------------------------
# Reference scales (references/05-layout-spacing-type.md)
# ----------------------------------------------------------------------------
SPACE_SCALE = {4, 8, 12, 16, 24, 32, 48, 64, 96, 128}
TYPE_SCALE = {12, 14, 16, 20, 24, 32, 40, 48, 64}
LINE_HEIGHTS = {1.0, 1.05, 1.1, 1.15, 1.25, 1.35, 1.4, 1.45, 1.5, 1.6}
RADIUS_OK = {0, 2, 4, 6, 8, 12, 16, 999, 9999}

SPACING_PROPS = (
    "padding", "margin", "gap", "row-gap", "column-gap", "inset",
    "top", "right", "bottom", "left",
    "padding-inline", "padding-block", "margin-inline", "margin-block",
)

NAMED_COLORS = {
    "white": (255, 255, 255), "black": (0, 0, 0), "red": (255, 0, 0),
    "green": (0, 128, 0), "blue": (0, 0, 255), "gray": (128, 128, 128),
    "grey": (128, 128, 128), "transparent": (0, 0, 0),
}


# ----------------------------------------------------------------------------
# Colour
# ----------------------------------------------------------------------------
def parse_color(value):
    """Return (r, g, b) 0-255 or None."""
    v = value.strip().lower()
    if v in NAMED_COLORS:
        return NAMED_COLORS[v]
    if v.startswith("#"):
        h = v[1:]
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h[:3])
        if len(h) not in (6, 8):
            return None
        try:
            return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))
        except ValueError:
            return None
    m = re.match(r"rgba?\(([^)]+)\)", v)
    if m:
        parts = [p.strip() for p in re.split(r"[,\s/]+", m.group(1)) if p.strip()]
        try:
            nums = []
            for p in parts[:3]:
                nums.append(float(p[:-1]) * 2.55 if p.endswith("%") else float(p))
            if len(nums) == 3:
                return tuple(max(0, min(255, int(round(n)))) for n in nums)
        except ValueError:
            return None
    return None


def _linear(channel):
    c = channel / 255.0
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def luminance(rgb):
    r, g, b = (_linear(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast_ratio(fg, bg):
    l1, l2 = luminance(fg), luminance(bg)
    if l1 < l2:
        l1, l2 = l2, l1
    return (l1 + 0.05) / (l2 + 0.05)


def report_contrast(fg_raw, bg_raw):
    fg, bg = parse_color(fg_raw), parse_color(bg_raw)
    if not fg or not bg:
        print(f"  ! could not parse colours: {fg_raw!r} / {bg_raw!r}")
        return {"ok": False, "error": "unparsable colour"}

    ratio = contrast_ratio(fg, bg)
    checks = [
        ("body text   (>=4.5:1)", 4.5),
        ("large text  (>=3.0:1)", 3.0),
        ("UI boundary (>=3.0:1)", 3.0),
    ]
    print(f"\n  foreground {fg_raw}  on  background {bg_raw}")
    print(f"  contrast ratio: {ratio:.2f}:1\n")
    for label, threshold in checks:
        mark = "PASS" if ratio >= threshold else "FAIL"
        print(f"    [{mark}] {label}")
    if ratio >= 7.0:
        print("\n  -> AAA for normal text.")
    elif ratio >= 4.5:
        print("\n  -> AA for normal text. Not AAA (needs 7:1).")
    elif ratio >= 3.0:
        print("\n  -> Only valid for large text (>=24px, or >=18.66px bold).")
    else:
        print("\n  -> Below every floor. Not usable for text or for a control boundary.")
    return {"ok": True, "ratio": round(ratio, 2)}


# ----------------------------------------------------------------------------
# CSS
# ----------------------------------------------------------------------------
def _to_px(num, unit):
    if unit == "px":
        return num
    if unit == "rem":
        return num * 16
    if unit == "em":
        return num * 16  # approximation, flagged separately
    return None


def scan_css(text):
    """Return findings dict for a CSS string."""
    text = re.sub(r"/\*.*?\*/", "", text, flags=re.S)
    findings = {"spacing": [], "type": [], "radius": [], "line_height": [], "notes": [],
                "token_type": False, "token_lh": False}

    # spacing declarations
    prop_re = "|".join(p.replace("-", r"\-") for p in SPACING_PROPS)
    for m in re.finditer(rf"(?:^|[{{;\s])((?:{prop_re})(?:-(?:top|right|bottom|left|inline|block))?)"
                         rf"\s*:\s*([^;}}]+)", text):
        value = m.group(2)
        for num_s, unit in re.findall(r"(-?\d*\.?\d+)(px|rem|em)\b", value):
            px = _to_px(abs(float(num_s)), unit)
            if px is None:
                continue
            if unit == "em":
                findings["notes"].append(
                    f"em spacing ({m.group(1)}: {value.strip()}) — relative to font size, verify intent")
                continue
            if px not in SPACE_SCALE:
                findings["spacing"].append(
                    {"prop": m.group(1), "value": f"{num_s}{unit}", "px": px})

    # font-size
    for m in re.finditer(r"font-size\s*:\s*([^;}}]+)", text):
        raw = m.group(1).strip()
        if "var(" in raw:
            findings["token_type"] = True
            continue
        if "clamp(" in raw or "calc(" in raw or "vw" in raw:
            findings["notes"].append(f"fluid font-size: {raw}")
            continue
        for num_s, unit in re.findall(r"(\d*\.?\d+)(px|rem)\b", raw):
            px = _to_px(float(num_s), unit)
            if px is not None:
                findings["type"].append({"value": f"{num_s}{unit}", "px": px})

    # line-height
    for m in re.finditer(r"line-height\s*:\s*([^;}}]+)", text):
        raw = m.group(1).strip()
        if "var(" in raw:
            findings["token_lh"] = True
            continue
        try:
            val = float(raw)
            findings["line_height"].append(val)
        except ValueError:
            pass

    # radius
    for m in re.finditer(r"border-radius\s*:\s*([^;}}]+)", text):
        raw = m.group(1).strip()
        if "%" in raw:
            continue
        for num_s, unit in re.findall(r"(\d*\.?\d+)(px|rem)\b", raw):
            px = _to_px(float(num_s), unit)
            if px is not None:
                findings["radius"].append({"value": f"{num_s}{unit}", "px": px})

    return findings


def report_css(path):
    text = Path(path).read_text(encoding="utf-8", errors="replace")
    f = scan_css(text)
    problems = 0

    print(f"\n  file: {path}")

    # spacing
    off = f["spacing"]
    if off:
        problems += len(off)
        counts = {}
        for item in off:
            counts[item["value"]] = counts.get(item["value"], 0) + 1
        ranked = sorted(counts.items(), key=lambda kv: -kv[1])
        print(f"\n  [FAIL] off-scale spacing: {len(off)} declaration(s)")
        for value, n in ranked[:12]:
            print(f"         {value:>8}  x{n}")
        print("         allowed: " + " ".join(str(v) for v in sorted(SPACE_SCALE)))
    else:
        print("\n  [PASS] all spacing values are on the scale")

    # type
    if f["type"]:
        unique = sorted({t["px"] for t in f["type"]})
        print(f"\n  type sizes in use: {len(unique)} -> {', '.join(f'{u:g}' for u in unique)}px")
        if len(unique) > 6:
            problems += 1
            print("  [FAIL] more than 6 sizes — a scale, not a pile")
        elif len(unique) > 3:
            print("  [WARN] more than 3 sizes per view is likely; check each screen")
        off_type = [u for u in unique if u not in TYPE_SCALE]
        if off_type:
            print(f"  [WARN] off-scale sizes: {', '.join(f'{u:g}' for u in off_type)}px")
    else:
        if f["token_type"]:
            print("\n  type sizes: token-based (var) — check the token file for the scale")
        else:
            print("\n  type sizes: none declared (inherited)")

    # line-height
    if f["line_height"]:
        bad = [v for v in set(f["line_height"]) if v not in LINE_HEIGHTS]
        body_ok = any(abs(v - 1.5) < 0.01 for v in f["line_height"])
        if bad:
            print(f"\n  [WARN] unusual line-heights: {', '.join(f'{b:g}' for b in sorted(bad))}")
        if not body_ok and not f["token_lh"]:
            print("  [WARN] no 1.5 line-height found — body text may be cramped")
    elif f["token_lh"]:
        print("\n  [PASS] line-height uses tokens")

    # radius
    if f["radius"]:
        unique = sorted({r["px"] for r in f["radius"]})
        print(f"\n  radii in use: {len(unique)} -> {', '.join(f'{u:g}' for u in unique)}px")
        if len(unique) > 4:
            problems += 1
            print("  [FAIL] more than 4 radii — one of them is a mistake")
        nested_note = [r for r in unique if r not in RADIUS_OK]
        if nested_note:
            print(f"  [WARN] unusual radii: {', '.join(f'{u:g}' for u in nested_note)}px")

    for note in f["notes"][:6]:
        print(f"  [note] {note}")

    return problems, f


# ----------------------------------------------------------------------------
# HTML
# ----------------------------------------------------------------------------
def report_html(path):
    text = Path(path).read_text(encoding="utf-8", errors="replace")
    problems = 0
    print(f"\n  file: {path}")

    def flag(ok, message):
        nonlocal problems
        print(f"  [{'PASS' if ok else 'FAIL'}] {message}")
        if not ok:
            problems += 1

    flag(bool(re.search(r"<html[^>]+lang=", text, re.I)), "html has a lang attribute")
    flag(bool(re.search(r'name=["\']viewport["\']', text, re.I)), "viewport meta present")

    h1s = len(re.findall(r"<h1[\s>]", text, re.I))
    flag(h1s == 1, f"exactly one h1 (found {h1s})")

    headings = [int(m) for m in re.findall(r"<h([1-6])[\s>]", text, re.I)]
    skipped = [(a, b) for a, b in zip(headings, headings[1:]) if b - a > 1]
    flag(not skipped, f"heading levels not skipped (found {len(skipped)} jump(s))")

    imgs = re.findall(r"<img\b[^>]*>", text, re.I)
    no_alt = [i for i in imgs if not re.search(r"\balt\s*=", i, re.I)]
    flag(not no_alt, f"every img has alt (found {len(no_alt)} without)")

    ids_with_for = set(re.findall(r"<label[^>]*\bfor=[\"']([^\"']+)", text, re.I))
    inputs = re.findall(r"<input\b[^>]*>", text, re.I)
    unlabelled = 0
    for tag in inputs:
        if re.search(r'type=["\'](hidden|submit|button|reset|image)["\']', tag, re.I):
            continue
        if re.search(r"aria-label|aria-labelledby", tag, re.I):
            continue
        m = re.search(r'\bid=["\']([^"\']+)', tag, re.I)
        if not (m and m.group(1) in ids_with_for):
            unlabelled += 1
    flag(unlabelled == 0, f"every input has a label (found {unlabelled} unlabelled)")

    outline_off = len(re.findall(r"outline\s*:\s*(?:none|0)\b", text, re.I))
    flag(outline_off == 0, f"outline not removed without replacement (found {outline_off})")

    # inline styles off the spacing grid
    inline = re.findall(r'style=["\']([^"\']+)["\']', text, re.I)
    off_grid = []
    for decl in inline:
        for num_s, unit in re.findall(r"(-?\d*\.?\d+)(px)\b", decl):
            px = abs(float(num_s))
            if px not in SPACE_SCALE and px not in {0, 1, 2}:
                off_grid.append(f"{num_s}px")
    flag(not off_grid, f"inline styles on the 4px grid (found {len(off_grid)} off-scale)")

    button_tags = re.findall(r"<button\b([^>]*)>(.*?)</button>", text, re.I | re.S)
    unnamed = []
    for attrs, inner in button_tags:
        has_text = bool(re.sub(r"<[^>]+>|\s", "", inner))
        has_label = (
            re.search(r'aria-label\s*=\s*["\'][^"\']+["\']', attrs, re.I)
            or re.search(r"aria-labelledby\s*=", attrs, re.I)
            or re.search(r'\btitle\s*=\s*["\'][^"\']+["\']', attrs, re.I)
        )
        if not has_text and not has_label:
            unnamed.append(re.sub(r"\s+", " ", inner).strip()[:40])
    flag(not unnamed, f"every button has an accessible name (found {len(unnamed)} without)")

    links = re.findall(r"<a\b([^>]*)>(.*?)</a>", text, re.I | re.S)
    empty_links = [l for l in links
                   if not re.sub(r"<[^>]+>|\s", "", l[1]) and "aria-label" not in l[0].lower()]
    flag(not empty_links, f"every link has an accessible name (found {len(empty_links)} empty)")

    reduced = len(re.findall(r"prefers-reduced-motion", text, re.I))
    if reduced == 0:
        print("  [note] no prefers-reduced-motion rule found in this file")

    return problems


# ----------------------------------------------------------------------------
# Entry
# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------
# Role contract (assets/design-contract.css §R)
# ----------------------------------------------------------------------------
REQUIRED_ROLES = [
    "--surface", "--surface-raised", "--surface-sunken",
    "--text-primary", "--text-secondary", "--text-tertiary",
    "--border", "--border-strong",
    "--accent", "--accent-hover", "--accent-active", "--on-accent", "--focus-ring",
    "--success", "--success-surface", "--warning", "--warning-surface",
    "--danger", "--danger-surface", "--info", "--info-surface",
]

ROLE_OBLIGATIONS = [
    ("--text-primary", "--surface", 4.5),
    ("--text-secondary", "--surface", 4.5),
    ("--text-tertiary", "--surface", 4.5),
    ("--accent", "--surface", 4.5),
    ("--on-accent", "--accent", 4.5),
    ("--border-strong", "--surface", 3.0),
    ("--focus-ring", "--surface", 3.0),
    ("--success", "--success-surface", 4.5),
    ("--warning", "--warning-surface", 4.5),
    ("--danger", "--danger-surface", 4.5),
    ("--info", "--info-surface", 4.5),
]


def _read_decls(path):
    text = Path(path).read_text(encoding="utf-8", errors="ignore")
    return {m.group(1): m.group(2).strip()
            for m in re.finditer(r"(--[\w-]+)\s*:\s*([^;{}]+);", text)}


def _resolve_role(name, decls, depth=0):
    """Follow var() chains inside one file. Returns (r,g,b) or None."""
    if depth > 8:
        return None
    raw = decls.get(name)
    if raw is None:
        return None
    m = re.fullmatch(r"var\(\s*(--[\w-]+)\s*(?:,\s*[^)]*)?\)", raw)
    if m:
        return _resolve_role(m.group(1), decls, depth + 1)
    return parse_color(raw)


def report_roles(path):
    """Validate an adapter against the 21-role contract."""
    decls = _read_decls(path)
    problems = 0
    print(f"\n  file: {path}")

    missing = [r for r in REQUIRED_ROLES if r not in decls]
    if missing:
        problems += len(missing)
        print(f"\n  [FAIL] {len(missing)} required role(s) not defined:")
        for r in missing:
            print(f"             {r}")
    else:
        print(f"\n  [PASS] all {len(REQUIRED_ROLES)} roles defined")

    print("\n  obligations:")
    for fg, bg, minimum in ROLE_OBLIGATIONS:
        fg_rgb, bg_rgb = _resolve_role(fg, decls), _resolve_role(bg, decls)
        if fg_rgb is None or bg_rgb is None:
            print(f"    [SKIP] {fg} on {bg} — not resolvable offline (external var or system colour)")
            continue
        ratio = contrast_ratio(fg_rgb, bg_rgb)
        ok = ratio >= minimum
        if not ok:
            problems += 1
        print(f"    [{'PASS' if ok else 'FAIL'}] {fg} on {bg}: {ratio:.2f}:1  (needs {minimum}:1)")

    extra = sorted(set(decls) - set(REQUIRED_ROLES))
    if extra:
        print(f"\n  note: {len(extra)} additional custom propert(ies) in this file (not part of the contract)")

    print(f"\n  {problems} problem(s) reported")
    return problems


def print_scale():
    space = " ".join(str(v) for v in sorted(SPACE_SCALE))
    type_ = " ".join(str(v) for v in sorted(TYPE_SCALE))
    print(f"\n  SPACING  {space}   (base 4, rhythm 8)")
    print(f"  TYPE     {type_}           (lh 1.5 body)")
    print("  RADIUS   4 8 12 16 999                        (inner = outer - padding)")
    print("  MEASURE  65ch    CONTRAST  4.5 / 3 / 3    TARGET 44x44")
    print("  COLOUR   no values — 21 roles from the project's adapter\n")


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 0

    strict = "--strict" in argv
    as_json = "--json" in argv
    args = [a for a in argv[1:] if not a.startswith("--")]
    if not args:
        print(__doc__)
        return 0

    cmd = args[0]
    problems = 0
    payload = {}

    if cmd == "scale":
        print_scale()
        return 0

    if cmd == "roles":
        if len(args) < 2:
            print("  usage: ux_check.py roles <adapter.css>")
            return 1
        problems = report_roles(args[1])
        return 1 if (strict and problems) else 0

    if cmd == "contrast":
        if len(args) < 3:
            print("  usage: ux_check.py contrast <fg> <bg>")
            return 1
        payload = report_contrast(args[1], args[2])
        if as_json:
            print(json.dumps(payload, indent=2))
        return 0

    if cmd in ("css", "html", "all"):
        targets = [Path(a) for a in args[1:]]
        if cmd == "all" and len(targets) == 1 and targets[0].is_dir():
            root = targets[0]
            targets = sorted(list(root.rglob("*.css")) + list(root.rglob("*.html")))
        if not targets:
            print("  nothing to check")
            return 1
        for target in targets:
            if not target.exists():
                print(f"  ! not found: {target}")
                problems += 1
                continue
            if target.suffix.lower() == ".css":
                p, _ = report_css(target)
            elif target.suffix.lower() in (".html", ".htm"):
                p = report_html(target)
            else:
                continue
            problems += p
        print(f"\n  {problems} problem(s) reported across {len(targets)} file(s)")
        if problems:
            print("  Fix order: structure -> rhythm -> type -> color -> states -> motion -> polish")
    else:
        print(__doc__)
        return 1

    return 1 if (strict and problems) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
