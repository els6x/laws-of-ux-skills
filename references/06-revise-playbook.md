# 06 — The Revise Playbook
### Diagnosing a UI that "looks bad", and fixing it in the order that actually works

Most bad interfaces are not ugly. They are **undifferentiated**: every gap is the same, every element has the same
weight, every section has the same shape. The eye has nothing to build a tree from, so it gives up and the user
describes the result as "unprofessional" without being able to say why.

This file is the diagnosis-and-repair procedure. Follow the order. Fixing colour before structure is the most common
reason a "redesign" ships and still feels wrong.

---

## 1. Diagnosis — the 12 failure signatures

Score each 0–3 (0 = absent, 3 = severe). One pass, no edits.

### S1 — Flat spacing (no grouping)
**Looks like:** every gap is 16 px; sections run together; labels float between fields; nothing feels attached to anything.
**Cause:** a single spacing value applied universally; no separation hierarchy.
**Fix:** impose the three-value rule and the 1:2 ratio (`05` §2.2–2.3). This one fix usually produces the largest
visible improvement of any change.

### S2 — Collapsed hierarchy
**Looks like:** everything is 16 px, or everything is bold, or there are four things shouting at once.
**Cause:** emphasis applied per-element instead of per-page; no ranked content inventory.
**Fix:** rank content 1 primary / 2–3 secondary / rest tertiary. Then allow exactly one focal point (Von Restorff) and
build the rest with size and space (`05` §3.3).

### S3 — Type soup
**Looks like:** five sizes, three families, six weights, inconsistent tracking; headings that don't relate to body.
**Cause:** type chosen per component instead of per system.
**Fix:** one family, three weights, three sizes per view, one scale (`05` §3.1). Delete the rest.

### S4 — Measure sprawl
**Looks like:** paragraphs running 120+ characters across a wide container; the eye loses the line return.
**Cause:** text filling the container instead of a measure.
**Fix:** `max-width: 65ch` on all prose. Break long paragraphs into 4–5 line blocks.

### S5 — Alignment drift
**Looks like:** three left edges in one region; centred headings over left-aligned body; buttons at inconsistent x.
**Cause:** no shared axis; centring used as a default.
**Fix:** one alignment axis per region; left-align body; centre only ≤3 lines or a single CTA. Align every element to a
column edge, not to "visually about there".

### S6 — Label–field divorce
**Looks like:** placeholder-as-label, labels above but equidistant from two fields, help text closer to the next field
than its own.
**Cause:** spacing not expressing ownership.
**Fix:** label 8 px above its field, 20 px to the next field, helper 4 px below the input (`05` §7 Input).

### S7 — Card fog
**Looks like:** every block is a bordered card with a shadow; twelve equal rectangles; nothing is more important.
**Cause:** regions used as the default container instead of as meaning.
**Fix:** remove borders/backgrounds from everything that doesn't need to survive distance. Group by gap first. Keep
cards only for genuine objects (`01` §1.2).

### S8 — Contrast & colour-only meaning
**Looks like:** grey-on-grey text; 3:1 body copy; error state signalled only by red; disabled-looking buttons that work.
**Cause:** colour chosen aesthetically, meaning encoded in hue.
**Fix:** 4.5:1 body / 3:1 large / 3:1 UI boundaries. Add icon, label, or weight to every colour-coded meaning. Test in
grayscale.

### S9 — Decision dump
**Looks like:** 12 nav items, a 14-field form, six equal CTAs, a pricing page with five tiers.
**Cause:** completeness prioritised over decision cost.
**Fix:** Hick + Choice Overload + Miller (`02` §2.1–2.4): ≤7 nav, ≤5 fields per group, 3 tiers with one recommended,
stage the rest.

### S10 — Missing states
**Looks like:** no loading state, empty state is blank, error is a generic banner, success is a silent re-render.
**Cause:** only the happy path was designed.
**Fix:** design all eight states (`SKILL.md` Gate 6). Empty state = onboarding. Error = cause + fix + preserved input.
Success = what happened + what's next (Peak-End).

### S11 — Target poverty
**Looks like:** 20 px icon buttons, 4 px gaps between adjacent actions, a small "×" beside "Delete", hover-only affordances on touch.
**Cause:** density prioritised over motor accuracy.
**Fix:** 44×44 minimum, 8 px separation, primary actions in the thumb zone, whole-row click targets (`04` §4.5).

### S12 — Generic slop
**Looks like:** centred hero + three equal feature cards with emoji icons + purple gradient + every section the same
height + "Lorem ipsum" energy. Technically tidy, entirely forgettable.
**Cause:** Prägnanz with no Von Restorff — simplification without a point of view.
**Fix:** one signature move (`SKILL.md` §10), one grid break, contrast of scale, one deliberate emptiness, type as image.

### Bonus — S13: Memory tax
**Looks like:** a multi-step flow where step 3 requires remembering something from step 1; filters that vanish when
results load; a code shown once and never again.
**Cause:** no offloading; each screen designed in isolation.
**Fix:** persist context on screen (`02` §2.4): selected filters, cart count, step number, summary panel, breadcrumbs.

---

## 2. Severity model

Do not fix by visual annoyance. Fix by cost.

| Level | Definition | Examples | Rule |
|---|---|---|---|
| **P0** | Blocks the task | broken submit, unreadable text, unreachable control, contrast <3:1 on body | fix before anything else, regardless of count |
| **P1** | Slows the task materially | wrong grouping, buried primary action, 14-field form, missing error state | fix in this pass |
| **P2** | Adds friction | inconsistent radius, flat spacing, misaligned edges | fix if time allows |
| **P3** | Polish | shadow depth, micro-copy, easing curve | fix last, never first |

**Priority formula:** `severity × frequency`. A P1 on the checkout screen outranks a P0 on a settings page nobody visits.
Count the traffic before ranking.

---

## 3. Fix order — never reverse

```
1  STRUCTURE   what is on the screen, in what order, grouped how      → S2, S7, S9, S13
2  RHYTHM      gaps, ratios, alignment, measure                      → S1, S4, S5, S6
3  TYPE        scale, weights, hierarchy, tracking                   → S3
4  COLOR       contrast, semantic roles, accent discipline           → S8
5  STATES      loading, empty, error, success, focus, disabled       → S10, S11
6  MOTION      transitions, feedback latency, reduced-motion         → (see 05 §6)
7  POLISH      radius, shadow, icons, micro-copy                     → S12
```

Why this order: each layer constrains the next. Changing colour before structure means repainting elements that will be
deleted. Changing type before rhythm means sizing text into gaps that are about to change. Changing motion before states
means animating transitions between screens that don't exist yet.

**The 60% rule.** Structure and rhythm typically account for ~60% of the perceived improvement. If a revision doesn't
touch them, it is a reskin, not a fix.

---

## 4. The 40-point audit

Run after the fix pass. Any "no" is a defect with a law attached.

### Grouping & layout (01)
1. Every gap comes from the scale — no `18px`, `22px`, `35px`.
2. Only three spacing values per screen.
3. Gap between groups ≥2× gap inside groups.
4. Gap above a heading ≥2× gap below it.
5. Card padding ≥ gap between cards.
6. Nested radius = outer − padding.
7. No more than 2 levels of nesting.
8. One alignment axis per region.
9. Body text left-aligned; centring only for ≤3 lines or a single CTA.
10. Borders and backgrounds removed where proximity already groups.

### Hierarchy & attention (02)
11. Exactly one primary action per screen.
12. Squint test: the 3 most salient elements are the 3 most important.
13. Grayscale test: one element still dominant.
14. Max 3 type sizes per view (plus one display).
15. Max 3 font weights in use.
16. No element emphasised on more than 2 dimensions.
17. First and last positions hold the two most important items.
18. Accent colour ≤10% of visible surface.

### Decisions & memory (02)
19. ≤7 top-level nav items.
20. ≤5 fields per form group; ≤7 choices per decision.
21. A recommended default exists wherever a choice exists.
22. Nothing must be remembered from a previous screen.
23. Selected filters/values remain visible.
24. Comparison of >4 items uses a table, not memory.
25. Every multi-step flow shows progress.

### Typography (05)
26. Body ≥16 px mobile, ≥14 px desktop.
27. Line-height 1.5 for body.
28. Measure 45–75ch on all prose.
29. Paragraph spacing ≥0.75em.
30. Numbers in tables are tabular and right-aligned.

### Color & accessibility (04, 05)
31. Body contrast ≥4.5:1; large text ≥3:1; UI boundaries ≥3:1.
32. No meaning carried by hue alone.
33. Focus-visible ring present on every interactive element.
34. Dark mode uses elevation, not inversion.

### Interaction (04)
35. Every target ≥44×44 px with ≥8 px separation.
36. Feedback <400 ms; spinner >1 s; progress >10 s.
37. Labels above fields; validation on blur; input preserved on error.
38. All eight states designed (default + hover, focus, active, disabled, loading, empty, error).

### Craft (03, 05)
39. One signature element per page — nameable in one sentence.
40. `prefers-reduced-motion` respected; no more than one noticeable motion moment.

---

## 5. Scoring

Ten dimensions, 0–3 each (0 absent/broken, 1 weak, 2 adequate, 3 strong):

```
grouping · hierarchy · decisions · memory · typography
colour · accessibility · states · interaction · craft
```

| Score | Band | Meaning |
|---|---|---|
| 0–9 | Broken | task likely fails; rebuild structure |
| 10–17 | Amateur | works, but reads as unprofessional; rhythm and type are the leverage |
| 18–23 | Competent | solid; polish and signature missing |
| 24–27 | Good | ship-ready; refine edge cases |
| 28–30 | Excellent | distinctive and defensible |

Report before/after per dimension. **If a dimension didn't move, say so** — an honest flat line is more useful than a
fabricated improvement, and it tells the user where the remaining debt is.

---

## 6. Before / after recipes

The eight transformations that cover most real cases.

### R1 — "Everything looks cramped"
```css
/* before */
.card { padding: 12px; } .field { margin-bottom: 12px; } section { margin: 12px 0; }

/* after — three values, 1:2:5 ratio */
:root { --s1: 8px; --s2: 24px; --s3: 64px; }
.card  { padding: var(--s2); }
.field { margin-bottom: 20px; }        /* element level */
.group { margin-bottom: var(--s2); }   /* group level */
section{ padding-block: var(--s3); }   /* section level */
```
Cramped is almost never "not enough padding" — it is "no difference between levels".

### R2 — "It looks flat / nothing stands out"
```css
/* after */
h1 { font-size: var(--text-3xl); font-weight: 700; letter-spacing: -.02em; }
.lead { font-size: var(--text-lg); color: var(--text-secondary); max-width: 60ch; }
.cta  { /* the only filled accent element on the page */ }
/* everything else: neutral, 1px border, no shadow */
```
Flatness is fixed by removing emphasis from nine things, not adding it to the tenth.

### R3 — "The form is exhausting"
Split into ≤5-field groups with labels; one column; label above; helper below; validate on blur; primary action
full-width at the end; optional fields behind "Add more". Autofill everything the system already knows (Parkinson).

### R4 — "The page is a wall of cards"
Remove the card from anything that isn't an object. Keep cards for products, people, tasks. Group the rest with
`--s2` gaps and a section heading. Result: one level of containment instead of four.

### R5 — "The dashboard is unreadable"
Rank: 1 headline metric (largest), 3–5 supporting metrics (equal, smaller), everything else in a table. Kill 30% of the
widgets. Use one chart type per question. Tabular numbers. Remove gridlines; keep the baseline.

### R6 — "It feels cheap"
Four fixes, in order: (1) consistent radius everywhere, (2) one shadow language, (3) 1.5 line-height on body + 65ch
measure, (4) 8 px icon grid with one stroke weight. Cheapness is inconsistency, not lack of effects.

### R7 — "The flow feels endless"
Add a progress indicator, name the remaining steps, compress the last step, and end with a summary screen. Goal-Gradient
+ Parkinson + Peak-End, applied in that order.

### R8 — "It looks like every other AI-generated site"
Delete the centred hero, the three equal feature cards, and the gradient. Choose one: an asymmetric editorial grid, a
type-led hero, or a single full-bleed image with text on a scrim. Break the grid once. Add one motion moment. See
`SKILL.md` §10.

---

## 7. What not to do

- **Don't restyle before restructuring.** Repainting a broken layout produces a prettier broken layout.
- **Don't add a component to solve a spacing problem.** The box is usually the problem.
- **Don't fix contrast by lightening the background** until you've checked the text colour — you'll often make it worse.
- **Don't "clean up" by deleting information.** Chunk, disclose, or move it. Deleting a required field is not simplification.
- **Don't chase a reference site's look.** Copy its system (scale, ratios, rhythm), not its pixels.
- **Don't declare victory on a dimension you didn't test.** Re-run the audit; report the flat lines.
