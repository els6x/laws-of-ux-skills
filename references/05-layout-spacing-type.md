# 05 — The Structure
### Grid, spacing, type sizes, colour roles, motion, components — the numbers that make a UI look organised

The laws explain *why*. This file is *what*. Every value here is derived from them and is meant to be copied, not
reinterpreted. If you change a number, change it once, in the contract layer, and change it everywhere.

**This file contains no palette and no typeface.** Colour is defined as roles with obligations (§4); the values come
from the project's design system, or from a direction they agreed to — see `07-design-system-adapter.md`.

**The organising idea:** a layout looks "rapi" when three things are true —
(1) every gap comes from a small closed set, (2) the gap between groups is at least twice the gap inside groups,
(3) every visual difference corresponds to a difference in meaning. Everything below serves those three.

---

## 1. Grid

```
Columns     12 (desktop) · 8 (tablet) · 4 (mobile)
Gutter      24 desktop · 16 tablet/mobile
Margin      80 (≥1440) · 48 (1024–1439) · 24 (768–1023) · 16 (<768)
Max width   1280 content · 1440 shell · 640 prose
Prose width 65ch regardless of container
```

| Breakpoint | Width | Columns | Gutter | Margin |
|---|---|---|---|---|
| xs | <480 | 4 | 16 | 16 |
| sm | 480–767 | 4 | 16 | 24 |
| md | 768–1023 | 8 | 24 | 24 |
| lg | 1024–1279 | 12 | 24 | 48 |
| xl | 1280–1439 | 12 | 24 | 48 |
| 2xl | ≥1440 | 12 | 32 | 80 |

**Rules**
- Build mobile-first. Every layout must survive at 320 px with no horizontal scroll.
- Content column is capped by `ch`, not by the container. A 1280 px container does not mean 1280 px of text.
- One alignment axis per region. Left-align body text always; never justify; centre only blocks ≤3 lines or a single CTA.
- Full-bleed sections break the container; their *content* still respects the grid.
- Never centre a long paragraph, a form, or a list. Centred text has no stable left edge, so the eye cannot return to
  the start of the next line — it is a reading cost with no benefit.

---

## 2. Spacing — the part that actually decides whether it looks professional

### 2.1 The scale (closed set)

```
4   8   12   16   24   32   48   64   96   128
```

Base unit **4 px**; primary rhythm **8 px**. After 16 the ratio is roughly 1.5–1.33, which keeps adjacent steps
visibly different (a 1.15 ratio produces gaps that look like mistakes).

| Token | px | Use |
|---|---|---|
| `--space-1` | 4 | icon↔label, badge inset, hairline offsets |
| `--space-2` | 8 | inside a control; label↔input; chip gap |
| `--space-3` | 12 | compact padding; list item gap |
| `--space-4` | 16 | default padding; paragraph gap; card inner gap |
| `--space-6` | 24 | card padding; block gap; gutter |
| `--space-8` | 32 | group gap; heading↔content |
| `--space-12` | 48 | section padding (mobile/tablet) |
| `--space-16` | 64 | section padding (desktop) |
| `--space-24` | 96 | hero padding, major section break |
| `--space-32` | 128 | page-level separation |

### 2.2 The separation hierarchy — the single most important rule

Four levels. Each level must be **at least 2×** the level inside it.

```
L1  inline     4–8     between icon and its label, words in a chip
L2  element    12–16   between fields, list rows, card contents
L3  group      24–32   between a group and the next group
L4  section    48–96   between page sections
```

| Relationship | Gap | Ratio check |
|---|---|---|
| Label ↔ its input | 8 | vs. 20 to next field → 1:2.5 ✓ |
| Input ↔ helper text | 4 | must be < gap to next field |
| Field ↔ next field | 20 | |
| Group ↔ next group | 32–40 | vs. 20 inside → 1:2 ✓ |
| Section ↔ section | 64–96 | vs. 32 → 1:2–1:3 ✓ |
| Heading ↔ its content | 16 | vs. 64 above → heading belongs to what follows ✓ |

**The failure this prevents.** Setting every gap to 16 px makes every relationship equal, so the eye cannot build a
tree. The page is not "cramped" or "spacious" — it is *undifferentiated*, which is what people mean when they say it
looks amateur.

### 2.3 The three-value rule

For any single screen, use **three** spacing values, no more. Example: `8 / 24 / 64`.

```
8   inside things
24  between things
64  between sections
```

Everything else is a mistake or a component default. This one constraint produces more visible tidiness than any other
single decision, because it makes the rhythm legible at a glance.

### 2.4 Spacing do / don't

| Do | Don't |
|---|---|
| Use tokens only | `padding: 18px` — off-scale, and it will drift |
| Make inner gaps the smallest | Equal gaps everywhere |
| Group with space before boxes | Draw a card to fix a gap problem |
| Scale gaps with viewport, preserving ratio | Halve all gaps on mobile (destroys hierarchy) |
| Let one region breathe more than the rest | Distribute whitespace evenly |
| Align to the 8 px rhythm | Mix 5/10/15 px values from a template |

**Optical exceptions** (the only permitted off-scale values): 1 px borders and hairlines; ±1–2 px to optically centre a
glyph, icon, or play triangle; letter-spacing on display type; `-1px` margin to collapse doubled borders.

---

## 3. Typography

### 3.1 Scale

One family (two if one is monospace for code/data). **The family itself is the project's** — it is never chosen in this
file (`07`). Sizes snap to a 2 px grid; the ratio between steps is 1.2–1.33.

| Token | px | Line-height | Use |
|---|---|---|---|
| `--text-xs` | 12 | 1.5 | metadata, badges, table headers (uppercase +0.04em) |
| `--text-sm` | 14 | 1.5 | secondary text, helper, labels |
| `--text-base` | 16 | **1.5** | body, inputs, buttons |
| `--text-lg` | 20 | 1.45 | lead paragraph, card title |
| `--text-xl` | 24 | 1.35 | section title |
| `--text-2xl` | 32 | 1.25 | page title |
| `--text-3xl` | 40 | 1.15 | display |
| `--text-4xl` | 48 | 1.1 | hero |
| `--text-5xl` | 64 | 1.05 | hero (desktop only) |

**Rules**
- Body never below 16 px on mobile, never below 14 px anywhere. 12 px is for metadata only, and only at ≥4.5:1 contrast.
- Line-height is inversely proportional to size. Large type needs *less* leading; small type needs more.
- Max **3 sizes per view** plus one display size. If you need a fourth, the hierarchy is wrong.
- Max **3 weights**: 400, 500/600, 700. Never fake bold, never use 300 for body (it disappears on low-DPI).
- Fluid type with `clamp()` on display sizes only; body stays fixed for readability.

### 3.2 Measure and rhythm

| Property | Value |
|---|---|
| Line length | 45–75 characters, target **60–70** (`max-width: 65ch`) |
| Paragraph spacing | ≥ `0.75em`, target `1em` (WCAG 1.4.12 asks 2× font size) |
| Paragraph max length | 4–5 lines before a break, list, or subhead |
| Heading ↔ following text | 16 px (must be visibly closer to what follows than to what precedes) |
| Heading ↔ preceding section | 48–64 px |
| Letter-spacing | 0 body · −0.01 to −0.02em at ≥32 px · +0.02 to +0.04em for uppercase small text |
| Text alignment | left (LTR) · never justified · numbers right-aligned with `font-variant-numeric: tabular-nums` |

### 3.3 Hierarchy

Build hierarchy with, in order of strength:

1. **Size** (strongest, most reliable)
2. **Weight**
3. **Space** (isolation creates emphasis)
4. **Color / opacity**
5. **Case and tracking**
6. Decoration (weakest — avoid)

One emphasis per region. A heading that is large *and* bold *and* colored *and* uppercase *and* spaced is four
attempts at the same job, and it reads as shouting.

### 3.4 Type do / don't

| Do | Don't |
|---|---|
| One family, 3 weights, 3 sizes | 4 sizes + 2 families + 5 weights |
| `65ch` for prose | Full-width paragraphs at 1440 px |
| Line-height 1.5 for body | 1.2 body text (cramped) or 2.0 (disconnected) |
| Tabular numbers in tables | Proportional digits in a column of figures |
| Real hierarchy via size/weight | Fake hierarchy via colour alone |

---

## 4. Colour — roles and obligations, not values

This file does not contain a palette. A palette is a brand decision; the laws constrain *relationships*, not hues.
The values come from the project — their design system, or a direction they agreed to (`07`).

### 4.1 The roles

Twenty-one slots, declared in `assets/design-contract.css` §R and filled by the adapter:

```
surfaces     surface · surface-raised · surface-sunken
text         text-primary · text-secondary · text-tertiary
edges        border · border-strong
accent       accent · accent-hover · accent-active · on-accent · focus-ring
semantic     success · success-surface · warning · warning-surface
             danger · danger-surface · info · info-surface
```

A role is a promise about *use*, not a colour. `--text-secondary` means "this is still text and must clear 4.5:1",
whatever hue the project chose for it.

### 4.2 Contrast floors (non-negotiable)

| Content | Ratio |
|---|---|
| Body text | **4.5:1** |
| Large text (≥24 px, or ≥18.66 px bold) | **3:1** |
| UI component boundaries, icons, focus rings | **3:1** |
| Disabled text | exempt, but still aim for 3:1 |
| Placeholder | 4.5:1 — placeholders are text, not decoration |
| Text on accent (`--on-accent`) | **4.5:1** — the most commonly broken pair in real systems |

### 4.3 Structural rules (true for any hue)

- **One accent hue**, three steps: base, hover, active. A second accent halves the meaning of the first.
- **One neutral family** for surfaces and text. Mixing a warm grey and a cool grey reads as a mistake.
- **Four semantic families**, each with a surface tint (10–15%) — not a single text colour.
- **Accent covers ≤10% of the visible surface**, and appears on the primary action only.
- **Never encode meaning in hue alone**: pair with icon, label, weight, or position (Von Restorff's own takeaway).
- **Dark mode is a remap, not an inversion.** Raise surfaces by going *lighter*; desaturate the accent; avoid pure
  black and pure white as large fields.
- **Test in grayscale.** If the hierarchy disappears, colour is carrying structural weight it should not.

### 4.4 When the project's values fail a floor

Say so, propose the nearest passing step of the *same* hue, and let them decide. Silently overriding a brand colour is
the same error as inventing one.

```
FAIL  --text-secondary on --surface = 3.1:1  (needs 4.5)
FIX   darken one step of the same hue → 4.9:1
```

---

## 5. Radius, border, elevation

```
Radius   4 (badge/input-sm) · 8 (buttons, inputs) · 12 (cards) · 16 (modals, sheets) · 999 (pills)
Border   1 px, var(--border). Never 2 px "for emphasis" — use weight or fill instead.
```

**Nested radius rule:** `inner radius = outer radius − padding`. A 16 px card with 24 px padding has no visible inner
corner; a 16 px card with 8 px padding needs an 8 px inner radius. Mismatched nesting is the most common "almost right"
detail in modern UI.

**Elevation — flat plus three shadow levels, no more:**

| Level | Shadow | Use |
|---|---|---|
| 0 | none + 1 px border | cards, sections, table rows |
| 1 | `0 1px 2px rgba(0,0,0,.06), 0 1px 3px rgba(0,0,0,.10)` | dropdowns, popovers, sticky headers |
| 2 | `0 8px 24px rgba(0,0,0,.12), 0 2px 6px rgba(0,0,0,.08)` | modals, sheets |
| 3 | `0 24px 48px rgba(0,0,0,.18)` | full-screen overlays only |

Never combine a heavy shadow with a strong border. Pick one elevation language and keep it.

---

## 6. Motion

| Token | ms | Use |
|---|---|---|
| `--motion-instant` | 120 | hover, focus, toggle, checkbox |
| `--motion-fast` | 200 | dropdown, tooltip, tab switch |
| `--motion-base` | 320 | modal, sheet, drawer, accordion |
| `--motion-slow` | 480 | page/route transition, large layout shift |

| Curve | Value | Use |
|---|---|---|
| enter | `cubic-bezier(.16,1,.3,1)` | things appearing (fast out, settle) |
| exit | `cubic-bezier(.4,0,1,1)` | things leaving (accelerate away) |
| move | `cubic-bezier(.4,0,.2,1)` | position/colour changes |

**Rules**
- Motion budget: **one** noticeable moment per view (Peak-End). Everything else is 120–200 ms and should be felt, not watched.
- Never animate `width`, `height`, `top`, `left`. Animate `transform` and `opacity`.
- Feedback must start within 100 ms even if the animation finishes later (Doherty).
- `@media (prefers-reduced-motion: reduce)`: remove transforms, keep opacity, cap duration at 0.01 ms for non-essential motion.
- Never animate content the user is currently reading.

---

## 7. Component specs

### Button
```
height      32 (sm) · 40 (md) · 48 (lg)     padding-x  12 · 16 · 24
radius      8                                gap        8
font        14/500 (sm) · 16/500 (md/lg)     icon       16 (sm) · 20 (md)
states      default · hover(+1 step) · active(+2) · focus-visible(2px ring, 2px offset) · disabled(40% + no pointer) · loading
rules       1 primary per view · destructive never adjacent to primary · min target 44×44 including padding
```

### Input
```
height      40 · 48                          radius 8
padding     12 x · 10 y (40h) / 12 y (48h)    border 1px var(--border)
label       above, 14/500, gap 8
helper      below, 12–14, gap 4, var(--text-secondary)
error       replaces helper, var(--danger), + icon (not colour alone)
gap         field→field 20 · group→group 32
rules       one column · ≤5 fields per group · validate on blur · never clear input on error
```

### Card
```
padding     24 (default) · 16 (compact) · 32 (spacious)
radius      12        gap between cards 24 (must be ≤ padding)
inner gap   16 between content blocks, 8 inside a block
elevation   border OR shadow, not both
rules       one idea per card · never nest more than 2 deep · don't card everything
```

### Navigation
```
height      64 desktop · 56 mobile            padding-x 24 · 48
items       ≤7 top-level · gap 24 · 16 font/500
primary     rightmost item or a single CTA button
mobile      ≤5 items in bottom bar; primary action in thumb zone
rules       current state always visible · logo returns home · back = previous, always
```

### Table
```
row height  44 (comfortable) · 36 (compact) · 32 (dense)
cell        12–16 padding · 14 font · tabular numbers · right-align numerics
header      12 uppercase +0.04em, var(--text-secondary), sticky
rules       zebra optional, borders horizontal only · no vertical grid lines unless comparing cells
```

### Modal
```
width       480 (sm) · 640 (md) · 800 (lg)     radius 16    padding 24–32
gap         24 between header / body / footer
rules       title + close · focus trapped · Esc closes · overlay 40–60% · never stack modals
```

### Empty state
```
max-width   360, centred      icon 48, var(--text-tertiary)
title       20/600            body 14–16, var(--text-secondary), ≤2 lines
action      one primary button that creates the first item
rules       the empty state IS the onboarding (Paradox of the Active User)
```

### Form layout
```
max-width   480 single column · label above field
groups      ≤5 fields, group label 16/600, gap 32 between groups
submit      full-width or left-aligned, 48 high, primary
rules       no multi-column forms · no placeholder-as-label · no required asterisks without a legend
```

---

## 8. Density

| Mode | Row height | Padding | Font | Use |
|---|---|---|---|---|
| Comfortable | 48 | 16–24 | 16 | marketing, onboarding, consumer |
| Compact | 36 | 12–16 | 14 | dashboards, admin |
| Dense | 32 | 8–12 | 13–14 | data tables, expert tools |

Density is a *mode*, not a per-component decision. Pick one per surface and apply it to every component on that
surface. Mixing densities inside one view is read as sloppiness, not as hierarchy.

---

## 9. CSS implementation

The structural layer is `assets/design-contract.css`: spacing, type sizes, radius, elevation, motion, layout, plus the
21 role obligations. It contains **no colours and no typefaces**. Minimum viable version:

```css
:root {
  /* space */
  --space-1: .25rem; --space-2: .5rem;  --space-3: .75rem; --space-4: 1rem;
  --space-6: 1.5rem; --space-8: 2rem;   --space-12: 3rem;  --space-16: 4rem;
  --space-24: 6rem;  --space-32: 8rem;

  /* type — sizes only; the family is set once on body, by the project */
  --text-xs: .75rem; --text-sm: .875rem; --text-base: 1rem; --text-lg: 1.25rem;
  --text-xl: 1.5rem; --text-2xl: 2rem;   --text-3xl: 2.5rem; --text-4xl: 3rem; --text-5xl: 4rem;
  --leading-tight: 1.15; --leading-snug: 1.35; --leading-normal: 1.5;
  --measure: 65ch;

  /* radius / elevation / motion */
  --radius-sm: 4px; --radius-md: 8px; --radius-lg: 12px; --radius-xl: 16px;
  --shadow-1: 0 1px 2px rgb(0 0 0 / .06), 0 1px 3px rgb(0 0 0 / .10);
  --shadow-2: 0 8px 24px rgb(0 0 0 / .12), 0 2px 6px rgb(0 0 0 / .08);
  --motion-instant: 120ms; --motion-fast: 200ms; --motion-base: 320ms;
  --ease-enter: cubic-bezier(.16, 1, .3, 1);
  --ease-exit:  cubic-bezier(.4, 0, 1, 1);

  /* layout */
  --container: 80rem; --container-prose: 40rem; --gutter: 1.5rem;
}
```

Then **the adapter** — one block, one file, the only place that knows both vocabularies:

```css
:root {
  --surface:      var(--ds-bg);
  --text-primary: var(--ds-fg);
  --accent:       var(--ds-primary);
  /* …the other 18 roles, then validate with `ux_check.py roles` */
}
```

Use logical properties (`padding-inline`, `margin-block`) so RTL and vertical writing modes work without a second
stylesheet. Use `gap` for spacing inside flex/grid instead of margins — margins collapse, gaps don't, and gaps express
the relationship directly.

---

## 10. The one-page summary

```
GRID      12 col · gutter 24 · margin 16/24/48/80 · content 65ch
SPACE     4 8 12 16 24 32 48 64 96 128 · 3 values per screen · inside:outside ≥ 1:2
TYPE      12 14 16 20 24 32 40 48 64 · lh 1.5 body · 3 sizes per view · 3 weights · family from the project
COLOUR    21 roles from the adapter · 1 accent ≤10% · contrast 4.5 / 3 / 3 · never hue alone
RADIUS    8 controls · 12 cards · 16 modals · inner = outer − padding
ELEVATION 3 levels · border OR shadow, never both
MOTION    120 / 200 / 320 · one noticeable moment · reduced-motion respected
TARGETS   44×44 · 8 px apart · thumb zone on mobile
STATES    default hover focus active disabled loading empty error
```

If a screen satisfies all ten lines, it will read as organised. If it satisfies nine and violates the spacing line, it
will still read as amateur — because spacing is the line users feel before they can name anything.
