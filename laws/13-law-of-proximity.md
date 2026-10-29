---
law: Law of Proximity
slug: law-of-proximity
index: 13
category: gestalt
lever: distance
audit_weight: critical
source: https://en.wikipedia.org/wiki/Principles_of_grouping
---

# 13 · Law of Proximity

> Objects that are near, or proximate to each other, tend to be grouped together.

**Category** Gestalt · **Lever** Distance · **Audit weight** Critical

## What the site says

### Takeaways

1. Proximity helps to establish a relationship with nearby objects.
2. Elements in close proximity are perceived to share similar functionality or traits.
3. Proximity helps users understand and organize information faster and more efficiently.

### Origins

The principles of grouping (or Gestalt laws of grouping) are a set of principles in psychology, first proposed by Gestalt psychologists to account for the observation that humans naturally perceive objects as organized patterns and objects, a principle known as Prägnanz. Gestalt psychologists argued that these principles exist because the mind has an innate disposition to perceive patterns in the stimulus based on certain rules. These principles are organized into five categories: Proximity, Similarity, Continuity, Closure, and Connectedness.

*Primary source cited on the site: [en.wikipedia.org](https://en.wikipedia.org/wiki/Principles_of_grouping)*

## Mechanism — why this happens

Distance is the cheapest grouping signal available, and the eye reads it before it reads anything else — before color,
before weight, before labels. Two elements close together are assumed to be related; two elements far apart are assumed
to be separate. This happens pre-attentively, which is why proximity errors are so damaging: the user has formed the
wrong grouping before they have read a single word.

The practical rule that follows is the most useful single number in layout design:

> **The space between groups must be at least twice the space within a group.**

If within-group spacing is 8 px, between-group spacing must be ≥16 px. Below that ratio, the groupings blur and the
page reads as an undifferentiated list — the single most common cause of "it looks messy but I can't say why".

The reason uniform 16 px spacing looks amateur is now precise: when every gap is equal, **every element is equally
related to every other**, so the layout communicates no structure at all. Structure is *difference* in spacing, not the
presence of spacing.

## Numbers that matter

| Quantity | Value | Consequence for the interface |
|---|---|---|
| Within-group : between-group ratio | **≥ 1 : 2** | The core rule; below it, groups merge |
| Comfortable ratio | 1 : 3 | Clearer hierarchy without looking sparse |
| Base unit | 4 or 8 px | All spacing should be a multiple |
| Spacing scale | 4, 8, 12, 16, 24, 32, 48, 64 | Pick from the scale; never invent 13 or 22 |
| Distinct spacing values per screen | **≤3** | More than three reads as noise |
| Label-to-field gap | 4–8 px | Must be smaller than field-to-field gap (16–24 px) |

## Apply it

### Do

- **Group first, then space.** Decide the groups, then assign two values: tight inside, loose outside.
- **Use a scale, not arbitrary numbers.** 4 / 8 / 12 / 16 / 24 / 32 / 48 / 64. Off-scale values (13, 18, 22) are the
  signature of a layout assembled by eye.
- **Limit yourself to three spacing values per screen** — small, medium, large. This single constraint produces most of
  the "clean" look people attribute to talent.
- **Put labels closer to their field than to the previous field.** The most common form error is a label equidistant
  between two inputs.
- **Use proximity instead of dividers** where you can. Removing a border and tightening the group is usually cleaner.
- **Keep related actions near their object.** "Edit" belongs next to the thing it edits, not in a toolbar at the top.

### Don't

- Don't use equal spacing everywhere. Equal spacing = no grouping = messy.
- Don't add a divider to fix a spacing problem. A line is a heavier signal than space; fix the space first.
- Don't put a section heading equidistant from the section above and below — it will attach to the wrong one.
- Don't let margins collapse unpredictably. Pick one spacing mechanism (gap, or margin, not both).
- Don't space by eye at one zoom level; check at 100% and on a small screen.

## Pattern

```css
/* One scale, three roles. This is the whole system. */
:root {
  --space-1: 4px;  --space-2: 8px;  --space-3: 12px; --space-4: 16px;
  --space-6: 24px; --space-8: 32px; --space-12: 48px; --space-16: 64px;

  --space-in:  var(--space-2);   /* within a group  — 8px  */
  --space-out: var(--space-6);   /* between groups  — 24px */
}
```

```html
<!-- The label sits closer to its field than the fields sit to each other -->
<form class="form">
  <div class="field">
    <label for="name">Full name</label>
    <input id="name" autocomplete="name">
  </div>
  <div class="field">
    <label for="email">Email</label>
    <input id="email" type="email" autocomplete="email">
  </div>
</form>
```

```css
.form  { display: grid; gap: var(--space-out); }        /* 24px between fields  */
.field { display: grid; gap: var(--space-in); }         /* 8px  label → input   */
```

```html
<!-- Bad: equal gaps, so the heading belongs to nothing -->
<h2>Shipping</h2>
<p>Address</p>
<p>City</p>

<!-- Better: heading tight to its group, loose from the previous section -->
<section class="section">
  <h2 class="section__title">Shipping</h2>
  <div class="section__body">
    <p>Address</p><p>City</p>
  </div>
</section>
```

```css
.section + .section { margin-block-start: var(--space-12); }
.section__title { margin-block-end: var(--space-3); }
.section__body > * + * { margin-block-start: var(--space-1); }
```

## Audit question

> Pick any two adjacent groups. Is the gap between them at least twice the gap inside them? If not, the page is telling
> the user those elements are equally related, and it is wrong.

## Further reading

| Reading | Author / Publisher |
|---|---|
| [Gestalt Principles of Design — Proximity](https://www.chrbutler.com/gestalt-principles-of-design-proximity) | Chris Butler |
| [Proximity Principle in Visual Design](https://www.nngroup.com/articles/gestalt-proximity/) | Aurora Harley \| Nielsen Norman Group |
| [Laws of Proximity, Uniform Connectedness, and Continuation](https://www.interaction-design.org/literature/article/laws-of-proximity-uniform-connectedness-and-continuation-gestalt-principles-2) | Mads Soegaard \| Interation Design Foundation |
| [The Psychology Principles Every UI/UX Designer Needs to Know](https://blog.marvelapp.com/psychology-principles-every-uiux-designer-needs-know/) | Thanasis Rigopoulos \| Marvel |
| [Design Principles: Visual Perception And The Principles Of Gestalt](https://www.smashingmagazine.com/2014/03/design-principles-visual-perception-and-the-principles-of-gestalt/) | Steven Bradley \| Smashing Magazine |

---

**Site page** · [lawsofux.com/law-of-proximity](https://lawsofux.com/law-of-proximity/)
