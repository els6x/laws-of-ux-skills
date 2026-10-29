---
law: Law of Uniform Connectedness
slug: law-of-uniform-connectedness
index: 16
category: gestalt
lever: visible connection
audit_weight: medium
source: https://en.wikipedia.org/wiki/Principles_of_grouping
---

# 16 · Law of Uniform Connectedness

> Elements that are visually connected are perceived as more related than elements with no connection.

**Category** Gestalt · **Lever** Visible connection · **Audit weight** Medium

## What the site says

### Takeaways

1. Group functions of a similar nature so they are visually connected via colors, lines, frames, or other shapes.
2. Alternately, you can use a tangible connecting reference (line, arrow, etc) from one element to the next to also create a visual connection.
3. Use uniform connectedness to show context or to emphasize the relationship between similar items.

### Origins

The principles of grouping (or Gestalt laws of grouping) are a set of principles in psychology, first proposed by Gestalt psychologists to account for the observation that humans naturally perceive objects as organized patterns and objects, a principle known as Prägnanz. Gestalt psychologists argued that these principles exist because the mind has an innate disposition to perceive patterns in the stimulus based on certain rules. These principles are organized into five categories: Proximity, Similarity, Continuity, Closure, and Connectedness.

*Primary source cited on the site: [en.wikipedia.org](https://en.wikipedia.org/wiki/Principles_of_grouping)*

## Mechanism — why this happens

Uniform connectedness is the strongest of the grouping principles: elements that are **physically joined** — by a line,
a shared container, a continuous background — are perceived as a single unit even when they are far apart and even when
they look different. In the classic ordering of Gestalt strength, connectedness beats common region, which beats
proximity, which beats similarity.

That hierarchy is the practical value of this law. When you need a group to survive **distance and dissimilarity** —
a multi-step flow where steps are far apart, an org chart, a timeline, a table with related columns — connection is the
only signal strong enough to hold it together.

The two everyday forms:

1. **A connecting line or path** — steppers, timelines, flow diagrams, tree structures.
2. **A shared continuous surface** — a table row with alternating background, a list where every item shares the same
   container and separators.

Because it is so strong, it is also the easiest to misuse: connect two things and users will assume a causal or
sequential relationship. A decorative line between unrelated cards will be read as "step 1 → step 2".

## Numbers that matter

| Quantity | Value | Consequence for the interface |
|---|---|---|
| Strength order | connectedness > region > proximity > similarity | Use the weakest signal that holds the group |
| Connector stroke | 1–2 px, muted | A heavy connector competes with content |
| Stepper connector length | ≥24 px | Shorter reads as one blob, not a sequence |
| Table row separators | 1 px, low contrast | Needed only when rows exceed ~5 |
| Nesting of connected groups | ≤2 | Nested trees deeper than 2 are unreadable on mobile |

## Apply it

### Do

- **Use a connector for sequence**: steppers, timelines, wizards, dependency graphs. The line *is* the "then".
- **Use a shared surface for membership**: a table row, a list item with a divider, a card. The surface *is* the "these".
- **Keep connectors visually subordinate** to the nodes they connect. 1 px at low contrast, not a bold arrow.
- **Connect only what is genuinely related.** A connector is a claim about causality or sequence.
- **Use it when proximity cannot work** — e.g. steps that must be spread across a wide screen, or grouped columns in a
  data table.

### Don't

- Don't draw decorative lines between unrelated blocks; users will read them as flow.
- Don't use a connector when a heading and spacing would do. Stronger signal = stronger false claim when wrong.
- Don't connect more than ~7 nodes in one path on mobile. Split into stages.
- Don't mix connection styles (solid + dashed + dotted) without a documented meaning for each.

## Pattern

```html
<!-- Stepper: the line carries the sequence, the nodes carry the state -->
<ol class="stepper">
  <li class="stepper__step is-done">
    <span class="stepper__dot" aria-hidden="true"></span>
    <span class="stepper__label">Account</span>
  </li>
  <li class="stepper__step is-current" aria-current="step">
    <span class="stepper__dot" aria-hidden="true"></span>
    <span class="stepper__label">Payment</span>
  </li>
  <li class="stepper__step">
    <span class="stepper__dot" aria-hidden="true"></span>
    <span class="stepper__label">Confirm</span>
  </li>
</ol>
```

```css
.stepper { display: flex; gap: var(--space-6); list-style: none; margin: 0; padding: 0; }
.stepper__step { position: relative; display: grid; gap: var(--space-2); justify-items: center; flex: 1; }
.stepper__step + .stepper__step::before {          /* the connector */
  content: "";
  position: absolute; inset-block-start: 6px; inset-inline-start: -50%;
  inline-size: 100%; block-size: 1px;
  background: var(--border);
}
.stepper__dot {
  inline-size: 12px; block-size: 12px; border-radius: 50%;
  background: var(--surface-sunken); outline: 2px solid var(--surface);
}
.stepper__step.is-done .stepper__dot    { background: var(--accent); }
.stepper__step.is-current .stepper__dot { background: var(--accent); box-shadow: 0 0 0 4px color-mix(in srgb, var(--accent) 20%, transparent); }
```

```html
<!-- Table: the row surface is the connection -->
<table class="table">
  <thead><tr><th>Plan</th><th>Price</th><th>Seats</th></tr></thead>
  <tbody>
    <tr><td>Free</td><td>$0</td><td>1</td></tr>
    <tr><td>Pro</td><td>$24</td><td>5</td></tr>
    <tr><td>Team</td><td>$79</td><td>20</td></tr>
  </tbody>
</table>
```

```css
.table { border-collapse: collapse; inline-size: 100%; }
.table th, .table td { text-align: start; padding: var(--space-3) var(--space-4); }
.table tbody tr + tr { border-block-start: 1px solid var(--border); }
.table tbody tr:hover { background: var(--surface-raised); }
```

## Audit question

> For every connector and shared surface on the screen: is the relationship it implies actually true? Would a user who
> saw only the line, not the labels, draw the same conclusion?

## Further reading

| Reading | Author / Publisher |
|---|---|
| [Gestalt Principles of Perception](http://www.andyrutledge.com/gestalt-principles-3.html) | Andy Rutledge |
| [Laws of Proximity, Uniform Connectedness, and Continuation](https://www.interaction-design.org/literature/article/laws-of-proximity-uniform-connectedness-and-continuation-gestalt-principles-2) | Interaction Design Foundation \| Mads Soegaard |
| [Design Principles: Visual Perception And The Principles Of Gestalt](https://www.smashingmagazine.com/2014/03/design-principles-visual-perception-and-the-principles-of-gestalt/) | Steven Bradley \| Smashing Magazine |

---

**Site page** · [lawsofux.com/law-of-uniform-connectedness](https://lawsofux.com/law-of-uniform-connectedness/)
