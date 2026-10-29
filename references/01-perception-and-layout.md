# 01 — Perception & Layout
### The five Gestalt laws: how the eye groups, and how to make spacing do the work

These five laws answer one question: **what belongs to what?** Every layout decision — gaps, borders, backgrounds,
alignment — is a grouping decision. Get grouping right and the page reads itself. Get it wrong and no amount of
color, shadow, or animation will fix the sense that "something is off".

All five come from the Gestalt school (Wertheimer, 1910; Koffka, Köhler). They describe *perception*, not taste —
which is why they translate directly into numbers.

**Relative strength when principles conflict** (from Smashing Magazine's Gestalt series and Palmer's vision science):

```
Uniform connectedness  ▸ strongest relatedness cue
Common region          ▸ strong, but visually heavier
Proximity              ▸ cheap, reliable, weakest of the three grouping cues
Similarity             ▸ can override proximity
Symmetry               ▸ can override proximity
Past experience        ▸ weakest principle — dominated by any other when they conflict
```

---

## 1.1 Law of Proximity

> Objects that are near, or proximate to each other, tend to be grouped together.

### Mechanism
The visual system computes grouping before it identifies objects (emergence). Distance is the cheapest grouping
signal available: it requires no color, no border, no component — only whitespace. This is why proximity is the
first tool to reach for and the last thing amateurs control.

### Numbers
| Decision | Value |
|---|---|
| Base gap inside a group | 1 step (8 or 12 px) |
| Gap between groups | 2 steps (16 or 24 px) |
| Gap between sections | 3–4 steps (48, 64, 96 px) |
| Minimum ratio, inside : outside | **1 : 2** — below this, groups dissolve |
| Target ratio for section breaks | 1 : 3 or more |
| Label → its own field | 8 px (must be *closer* than to the next field) |
| Field → next field | 20–24 px |

### Do
- Express grouping as a **ratio, not a value**. Two groups separated by 24 px, with 12 px inside each, read as two
  groups. The same 24 px with 24 px inside reads as one list.
- Make the *innermost* gap the smallest number on the screen region. Hierarchy of gaps = hierarchy of meaning.
- Use proximity **before** borders. A border is a heavier commitment; whitespace is reversible.
- Keep label-to-field distance smaller than field-to-field distance. This one ratio fixes most form ugliness.
- On mobile, halve the gaps but preserve the ratio (8 inside / 16 between, not 8 / 8).

### Don't
- Don't use one universal gap (16 px everywhere). It is the most common cause of "flat, unprofessional" layouts:
  everything is equally related, therefore nothing is.
- Don't let a section heading sit equidistant between the section above and the block below — it will attach to
  the wrong one. Headings belong to what follows (gap above ≈ 2× gap below).
- Don't compensate for weak grouping with borders, dividers, and boxes. That is proximity debt paid at a higher
  visual cost.
- Don't rely on proximity alone when items are visually similar but semantically different (see 1.4).

### Audit question
> Cover the borders and backgrounds. Can you still tell where each group starts and ends?
> If not, the spacing is wrong — not the styling.

### Source
[lawsofux.com/law-of-proximity](https://lawsofux.com/law-of-proximity/) · Gestalt principles of grouping
([Wikipedia](https://en.wikipedia.org/wiki/Principles_of_grouping)) · Bradley, *Design Principles: Visual Perception
and the Principles of Gestalt*, Smashing Magazine, 2014.

---

## 1.2 Law of Common Region

> Elements tend to be perceived into groups if they are sharing an area with a clearly defined boundary.

### Mechanism
A boundary — border, background fill, or both — creates an enclosed region. Everything inside is read as one object;
everything outside is read as separate. This is a *stronger* grouping signal than proximity because it survives
distance: items at opposite corners of a card still belong together.

### Numbers
| Decision | Value |
|---|---|
| Card padding | 16 (compact) · 24 (default) · 32 (spacious) |
| Gap between sibling cards | 16 or 24 — must be **≤** card padding |
| Nested radius | inner radius = outer radius − padding (12 outer + 24 pad → 0; use 16 outer + 16 pad → 0, or 16 + 8 → 8) |
| Border | 1 px, neutral-200 equivalent, never 2 px "for emphasis" |
| Max nesting depth | 2 (card inside card is the limit; card inside card inside card is noise) |

### Do
- Prefer **background fill** over border for large regions; prefer **border** over fill for small, repeated items
  (rows, chips). Fill on everything turns the page into a patchwork.
- Keep padding **≥** the gap between siblings. If the gap is larger than the padding, the card stops reading as a
  container and its contents float toward the edges.
- Use one region per idea. A card that contains two unrelated ideas forces the eye to re-group inside a group.
- Reserve cards for things that are genuinely *objects* (a product, a person, a task). A card around a paragraph
  is a box around a sentence.

### Don't
- **Don't card everything.** When every block is a card, all blocks become equal in weight — the page loses
  hierarchy and gains visual noise. This is the most common "dashboard made by a template" failure.
- Don't mix border + strong shadow + fill on the same element. Pick one elevation language.
- Don't use a region to fix a proximity problem. If items belong together, first try removing 8 px; only then draw a box.
- Don't nest regions to create hierarchy. Use type scale and spacing for hierarchy; regions are for *separation*.

### Audit question
> Remove every border and background. Does the page still group correctly?
> If yes, the regions are decoration. If no, keep only the regions that carry meaning.

### Source
[lawsofux.com/law-of-common-region](https://lawsofux.com/law-of-common-region/) · Gestalt principles of grouping.

---

## 1.3 Law of Uniform Connectedness

> Elements that are visually connected are perceived as more related than elements with no connection.

### Mechanism
The strongest of the grouping principles. A line, a shared shape, an arrow, or a continuous background connects
elements even when they are far apart and dissimilar — and it works **without touching** the elements. This makes it
the right tool for relationships that must survive distance: steps, timelines, parent/child, cause/effect.

### Numbers
| Decision | Value |
|---|---|
| Connector stroke | 1–2 px; 2 px only for the active path |
| Connector color | neutral-300 default, accent for the active segment |
| Dot/node size on a stepper | 8–12 px idle, 24–32 px active |
| Connector gap around a node | ≥8 px (line must not touch the node — it still reads as connected) |
| Max connectors per view | 1 system (a stepper OR a timeline OR a tree — not all three) |

### Do
- Use connectedness for **sequence**: onboarding steps, checkout progress, timeline, org chart, dependency graph.
- Use it for **attribution**: a quote with a left rule, a comment thread with a spine, a reply indented under a line.
- Let one continuous surface connect items instead of many small ones (a single panel with rows beats five separate
  chips when the rows are steps of one thing).
- Make the *active* segment the only accented one. A fully colored path communicates "done", not "here".

### Don't
- Don't connect things that are merely adjacent. Connectedness asserts causality or membership; a decorative line
  between unrelated blocks is a false claim.
- Don't use connectors when proximity already works — two elements 8 px apart do not need an arrow.
- Don't combine a connector with a common region around the same items unless the region is the *container* of the
  whole sequence; otherwise you get competing grouping cues.

### Audit question
> For each line, arrow, or shared spine: what relationship does it assert, and is that relationship true?

### Source
[lawsofux.com/law-of-uniform-connectedness](https://lawsofux.com/law-of-uniform-connectedness/) · Gestalt principles
of grouping (connectedness is the strongest of the five categories).

---

## 1.4 Law of Similarity

> The human eye tends to perceive similar elements as a complete picture, shape, or group, even if those elements are separated.

### Mechanism
Shared visual attributes — color, shape, size, orientation, weight, motion — are read as shared *meaning*. Similarity
is therefore a **semantic contract**: once two things look the same, users assume they behave the same. Breaking that
contract is the most expensive kind of inconsistency, because it produces confident wrong clicks.

### Numbers
| Decision | Value |
|---|---|
| Type families | 1 (2 max: one text, one mono/display) |
| Font weights in use | 3 max (regular, medium, semibold/bold) |
| Type sizes per view | 3 max (plus one display size if there is a hero) |
| Button styles | 3 (primary, secondary, tertiary/ghost) + 1 destructive |
| Icon stroke weight | 1 consistent value (1.5 or 2 px) across the whole set |
| Link styling | must differ from body text in ≥2 dimensions (color + underline, or color + weight) |

### Do
- Define **semantic styles**, not visual ones: `primary-action`, `secondary-action`, `destructive`, `metadata`,
  `link`. Then every instance of that meaning uses the same style, everywhere.
- Differentiate links from text in at least two ways. Color alone fails for color-blind users and for anyone reading
  on a bad screen — this is both Von Restorff's warning and a WCAG requirement.
- Keep interactive and non-interactive elements visually distinct. A chip that looks tappable but isn't is a
  similarity defect.
- Reuse the *same* component for the same job. Two implementations of "date picker" will drift within a month.

### Don't
- Don't style two different actions identically (e.g. "Save" and "Delete" as the same grey button).
- Don't let decoration create false similarity: two unrelated blocks with the same card style and the same icon
  treatment will read as the same kind of thing.
- Don't introduce a second accent hue for variety. Variety in hue is read as variety in meaning.
- Don't use similarity to compensate for poor grouping — if items must group, fix the gaps first (1.1).

### Audit question
> Point at any two elements that look alike. Do they do the same thing?
> Point at two elements that do the same thing. Do they look alike?

### Source
[lawsofux.com/law-of-similarity](https://lawsofux.com/law-of-similarity/) · Gestalt principles of grouping
(similarity can dominate proximity).

---

## 1.5 Law of Prägnanz

> People will perceive and interpret ambiguous or complex images as the simplest form possible, because it is the
> interpretation that requires the least cognitive effort.

### Mechanism
Perception is compression. The eye resolves ambiguous input into the simplest stable interpretation available, and
that resolution happens before conscious attention. Consequences: complex shapes get simplified (so detail is lost
anyway), and ambiguous shapes cost processing time (so they feel "wrong" without the user knowing why). Prägnanz is
the theoretical root of the other four — and the reason "clean" design is not a style preference.

### Numbers
| Decision | Value |
|---|---|
| Distinct shapes in one icon set | ≤3 geometric families (e.g. rounded square, circle, line) |
| Icon detail at 16–20 px | ≤2 strokes per concept; no fine detail below 24 px |
| Decorative elements competing with content | 0 |
| Gradients / effects per view | ≤1 system |
| Visual "noise budget" | one accent, one texture, one shadow language — not three |

### Do
- Reduce to **one idea per shape**. A logo, icon, or illustration that needs a second look is failing at 24 px.
- Use simple geometry for containers: rectangles, rounded rectangles, circles. Novel shapes cost comprehension.
- Cut decorative elements until removal starts to hurt, then stop (this is Occam's Razor applied to visuals).
- Make the simplest interpretation the *correct* one. If a card could be read as clickable or not, it is ambiguous —
  resolve it with affordance, not with explanation.
- Prefer one strong idea over three weak ones. A single 64 px headline beats a headline, a subhead, a badge, and an icon.

### Don't
- Don't add ornament to signal quality. Ornament raises the cost of finding the simplest interpretation and reads as
  noise at a glance.
- Don't use low-contrast decorative type, thin hairline dividers at 10% opacity, or blurred background shapes behind
  text — all three are ambiguity generators.
- Don't stack effects (gradient + shadow + border + texture + glow). Each one multiplies the interpretations available.

### Audit question
> Look for 1 second, then look away. What did you see? If the answer is "a lot of stuff", Prägnanz is failing.

### Source
[lawsofux.com/law-of-prägnanz](https://lawsofux.com/law-of-pr%C3%A4gnanz/) · Wertheimer's 1910 observation of the
railway-crossing lights · Bradley, Smashing Magazine, 2014.

---

## Companion principles (same Gestalt family, not separate Laws of UX entries)

These appear inside the same research tradition and are worth applying, but they are **not** among the 30 entries on
lawsofux.com. Use them as supporting tools, and do not present them as laws from that site.

| Principle | What it does | Practical rule |
|---|---|---|
| **Closure** | The eye completes incomplete shapes | You may omit part of an outline; provide *just enough* for the pattern to resolve. Too little → parts; too much → no closure needed. |
| **Continuity (good continuation)** | Elements on a line or curve read as one path | Align related items along a single axis. Eyes follow the line — use it to lead to the primary action. |
| **Figure / ground** | Smaller, convex, enclosed regions read as figure | Keep the figure/ground relationship stable. Never put text over a busy photo without a scrim. |
| **Common fate** | Elements moving together read as related | Animate a group as one unit. Real movement > arrows/gaze, which only imply it. |
| **Symmetry & order** | Symmetry is found fast; it can override proximity | Use symmetry for calm, speed of reading, and stable compositions — not for every block. |
| **Focal point** | Contrast draws attention; requires similarity to exist | A focal point cannot exist without a consistent baseline. One per view. |

---

## Layout synthesis — the five laws as a build sequence

```
1. GROUP BY GAP       → set 3 gap values (8 / 24 / 64). Assign every gap to one of them.
2. ADD REGION ONLY IF → the group must survive distance or scrolling. Else: no box.
3. CONNECT ONLY IF    → the relationship is sequence, hierarchy, or attribution. One connector system.
4. UNIFY SIMILARITY   → one style per meaning; max 3 sizes, 3 weights, 1 accent.
5. REDUCE TO PRÄGNANZ → delete decoration until removal hurts. Resolve every ambiguity.
```

**The 60-second layout test.** Screenshot the page, apply a 12 px blur, and look at the grey blocks. You should see:
one dominant block, two or three supporting blocks, and clear channels of whitespace between groups. If the blurred
image is a uniform field of grey rectangles, the layout has no hierarchy — the problem is grouping and spacing, not color.
