# 07 — Adapter
### Build inside the user's design system, not on top of ours

This skill has no palette and no typeface. It has **rules**. The values belong to the project.

That split is the whole point: a design system is a set of decisions a team already made. Arriving with your own
decisions and overriding theirs is not design work, it is vandalism with good intentions. The adapter is the handoff.

---

## 0. The one rule

> **Never invent a brand colour or a typeface.**

If the project has values, use them. If it does not, **describe a direction in words**, get agreement, then derive
values that satisfy the contract's obligations. The skill may propose *"cool neutrals with one saturated accent and a
neo-grotesque"*. It may not propose `#2563eb` and `Inter` as if they were the answer.

Two corollaries:

- **Their token wins over our default.** If their spacing scale is 6-based, use 6 — then enforce the ratio, not the base.
- **If their system breaks a law, say so.** Report the specific failure, propose the smallest fix, and let them decide.
  Silently "correcting" their brand is the same crime in the other direction.

---

## 1. Detect what you were given

| Input | How to read it | What you get |
|---|---|---|
| **Design tokens** (CSS vars, JSON, Tailwind config, Figma variables) | Read the file. It is the source of truth. | Exact values, exact names |
| **Component library / DS docs** (Storybook, a docs site) | Read the components, not the marketing page | Values *and* conventions: radii, states, density |
| **Live site or app** | DevTools → computed styles on 5–6 representative elements | Real values, including the ones they forgot to document |
| **Screenshot / image** | Sample the dominant surface, text, accent, border; measure type | Approximate values — always label them as estimates |
| **A written brief only** | Nothing yet | Propose a direction (§5) |

**Before extracting, ask one question:** *"Do you have a design system or brand tokens I should build inside?"*
If the answer is yes and they hand you a link, stop designing and start reading.

---

## 2. Extract — the short list

Do not inventory everything. You need eleven values to build a screen:

| What | Where to look | Why it matters |
|---|---|---|
| Page background | `body` background | The base the whole contrast chain hangs on |
| Primary text | `body` colour | Sets the contrast floor |
| Secondary / muted text | labels, hints, captions | The most-abused role in most systems |
| Border / divider | card, input, table | Without it, groups have no edges |
| Primary action | the main button | The single accent |
| Action hover / active | button states | Without these, the button feels dead |
| Semantic set | success / warning / danger / info | States are not optional |
| Type family + fallback | `font-family` on body | One family, one mono |
| Sizes actually used | headings, body, caption | Their scale, not yours |
| Radius | buttons, cards, inputs | Their geometry |
| Density | row height, control height, padding | Comfortable / compact / dense |

If a value is missing (most systems have no `--text-tertiary`), **derive it from their nearest neighbour** — same hue,
one step toward the background — and tell them what you derived.

---

## 3. Map to roles

The contract in `assets/design-contract.css` names 21 roles. Map their tokens onto those names; never rename their
tokens to match ours.

| Role | Typical source in their system |
|---|---|
| `--surface` | `--color-bg`, `--background`, `canvas` |
| `--surface-raised` | `--color-surface`, `--card`, `elevation-1` |
| `--surface-sunken` | `--color-bg-subtle`, `--muted`, `well` |
| `--text-primary` | `--color-fg`, `--foreground`, `text` |
| `--text-secondary` | `--color-fg-muted`, `text-secondary` |
| `--text-tertiary` | `--color-fg-subtle`, `placeholder`, `disabled` |
| `--border` | `--color-border`, `divider` |
| `--border-strong` | `--color-border-strong`, `input-border` |
| `--accent` | `--color-primary`, `brand`, `action` |
| `--accent-hover` | `primary-hover`, `brand-600` |
| `--accent-active` | `primary-active`, `brand-700` |
| `--on-accent` | `on-primary`, `text-on-brand` |
| `--focus-ring` | `focus`, `ring` — often the accent |
| `--success` / `--success-surface` | `green-600` / `green-50` equivalents |
| `--warning` / `--warning-surface` | `amber-*` equivalents |
| `--danger` / `--danger-surface` | `red-*` equivalents |
| `--info` / `--info-surface` | `blue-*` / `cyan-*` equivalents |

Write the mapping **in one place** — an adapter block at the top of their stylesheet, or a single `adapter.css`. If the
mapping is scattered across components, the next person cannot change the brand without a hunt.

```css
/* adapter.css — the only file that knows both vocabularies */
:root {
  --surface:         var(--ds-bg);
  --text-primary:    var(--ds-fg);
  --accent:          var(--ds-primary);
  /* …the rest of the 21 roles */
}
```

---

## 4. Validate before building

Run the contract's obligations against their values **before** you write a screen. Finding out at the end that their
muted grey is 3.1:1 means re-doing every label.

```bash
python scripts/ux_check.py roles path/to/adapter.css
python scripts/ux_check.py contrast "#767676" "#ffffff"
```

| Check | Requirement | If it fails |
|---|---|---|
| Text on surface | ≥ 4.5:1 | Darken or lighten one step; report the change |
| Accent as link text | ≥ 4.5:1 | Use a darker step of the same hue for text, keep the base for fills |
| `--on-accent` on `--accent` | ≥ 4.5:1 | Flip to white/black — this is a real bug in many systems |
| Borders and focus ring | ≥ 3:1 | Strengthen one step |
| Semantic on its surface | ≥ 4.5:1 | Adjust the text step, not the surface |
| Targets | ≥ 44 × 44 px | Their control height may be 32 — add hit-area padding, do not grow the visual |
| Spacing | ratio ≥ 1 : 2 between groups | Keep their base, fix the ratio |

Report failures as a short list with the fix you applied — not as a lecture, and never as a silent override.

---

## 5. When there is no design system: propose a direction

Do not open a colour picker. **Describe, ask, then derive.**

Propose at most **three** directions, one line each, and ask which fits. Ten options is choice overload
(`laws/02-choice-overload.md`).

### 5.1 Colour directions — described, not specified

| Direction | Reads as | Fits | Pair with | Watch |
|---|---|---|---|---|
| Cool neutral + one saturated accent | precise, technical, trustworthy | SaaS, dashboards, dev tools | accent only on the primary action | accent creeping into body text |
| Warm neutral + muted accent | approachable, human, editorial | consumer, health, education | generous line-height | low-contrast secondary text |
| Near-black + single signal | premium, confident | portfolio, luxury, fintech | lots of empty space | pure black text on pure white (harsh, halates) |
| Off-white + ink + one earth tone | calm, considered, print-like | publishing, docs, long reading | a serif for prose | too many tints |
| Duotone (two hues, one dominant) | bold, branded, memorable | launch pages, campaigns | large type | product UI — it will fight every state |
| Low-chroma monochrome | quiet, dense, tool-like | admin, expert tools | weight and spacing for hierarchy | hierarchy collapsing at low contrast |
| High-key pastel + dark text | friendly, light, modern | onboarding, consumer mobile | a strong accent for actions | 12 px text on pastel |
| Dark-first + luminous accent | focused, technical | media, dashboards, night work | raised surfaces instead of shadows | glare, and pure black everywhere |

Each row is a *decision about relationships* — how much contrast between surface and text, how loud the accent is,
whether the palette is warm or cool. Those relationships are what the laws constrain. The hexes are downstream.

### 5.2 Type directions — categories, not families

| Category | Reads as | Fits | Watch |
|---|---|---|---|
| Neo-grotesque | neutral, institutional, reliable | UI, corporate, product | bland without a strong scale |
| Humanist sans | warm, legible, approachable | public services, health, education | can read as dated |
| Geometric sans | modern, optimistic, precise | startups, marketing, product | weak at 12–14 px for body |
| Grotesque | editorial, confident, cultural | media, culture, brand | needs deliberate tracking |
| Transitional / old-style serif | trustworthy, literary, editorial | publishing, finance, long-form | poor for dense UI |
| Slab serif | sturdy, technical, distinctive | engineering, logistics, headlines | too heavy for body |
| Condensed | efficient, urgent, data-dense | tables, labels, news | never for body |
| Mono-led | technical, honest, developer-facing | dev tools, docs, terminals | slow to read in paragraphs |

**Pairing rules**

- One family for everything, plus a mono for code and tabular numbers. That is the default; two is the maximum.
- If you pair, pair by **contrast of category** (serif + grotesque), never two similar sans — that reads as a mistake,
  not a choice.
- A display face belongs at ≥ 32 px only. Never body, never labels, never buttons.
- Two or three weights, no more. Fake bold is a defect.
- The system stack is a *fallback*, not a design decision. If the answer to "what typeface?" is "whatever the OS has",
  the product has no typographic voice — say so, then pick a category.

### 5.3 How to derive values from a direction

1. Pick the surface and text first. Set the contrast you want (4.5:1 is the floor, 7:1 is comfortable for long reading).
2. Pick **one** accent hue. Derive three steps: base, hover (slightly darker or lighter), active (one further).
3. Derive the semantic four from the accent's neighbours in hue, not from a random palette: success leans green,
   danger leans red, warning leans amber, info leans toward the accent.
4. Check every pair with `ux_check.py contrast`. Adjust the *step*, never the requirement.
5. Write the result into an adapter block, and keep the direction's name in a comment so the next person knows why.

---

## 6. Build order with an adapter

```
1  CONTRACT    structural tokens only (assets/design-contract.css)
2  ADAPTER     map the 21 roles → the project's tokens; validate contrast
3  SKELETON    structure and reading order — landmarks, one h1, importance order
4  LAW PASS    grouping → ranking → bounding → placement → meaning → feel
5  AUDIT       scripts/ux_check.py all <dir>, then the 10 self-checks
```

Steps 1–2 happen **before** any screen. If you find yourself choosing a colour while placing a card, you skipped the
adapter and you are about to build a second design system by accident.

---

## 7. Anti-patterns

| Anti-pattern | Why it is wrong | Do instead |
|---|---|---|
| Inventing a palette "because it looks better" | You replaced their brand with your taste | Ask for their tokens, or propose a direction in words |
| Mixing two design systems | Two radii, two greys, two button heights — reads as sloppy | Pick one; map the other's values onto roles |
| Overriding their radius silently | Geometry is part of brand recognition | Keep it, or flag the change and why |
| Using the accent for everything | Destroys Von Restorff — nothing stands out | Accent on the primary action only |
| Copying a reference site's pixels | You inherit its bugs and its licences | Copy the *tokens and conventions*, rebuild the layout |
| Treating their failing contrast as "their choice" | Accessibility is not a brand preference | Report, propose the nearest passing step |
| Adding a display face to a UI | Slows reading, breaks at small sizes | Display for display only |
| Presenting 8 palettes | Choice overload | Three directions, one line each |

---

## 8. Worked example

> *"Here's our design system — build a settings page. Tokens are in `tokens.css`."*

```
1  READ      tokens.css: bg #fbfbfd, fg #16181d, muted #6b7280, border #e5e7eb,
             primary #4f46e5 (hover #4338ca), radius 10px, control height 36px.
             No semantic set. No tertiary text.
2  MAP       18 roles mapped. Derived --text-tertiary from --muted, one step toward
             the background (#9ca3af). Derived success/warning/danger/info from
             their hue family, flagged as derived.
3  VALIDATE  --muted on --surface = 4.9:1 ✓   --primary on --surface = 5.2:1 ✓
             --on-accent (white) on --primary = 4.6:1 ✓
             control height 36px < 44px → keep 36px visual, add 4px invisible
             hit area to reach 44. Flagged.
4  BUILD     structure from the laws: one column, groups of ≤5 fields, label above,
             one primary action. Their radius 10px, their density (compact).
5  REPORT    "Used your tokens. Three things you should know: no tertiary text
             (derived #9ca3af), no semantic colours (derived four), controls are
             36px so I added hit-area padding rather than growing them."
```

That report is the deliverable as much as the page is. It tells them what was decided **about their system**, which is
the only part they cannot see in the output.
