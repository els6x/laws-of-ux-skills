---
law: Law of Common Region
slug: law-of-common-region
index: 12
category: gestalt
lever: shared boundary
audit_weight: high
source: https://en.wikipedia.org/wiki/Principles_of_grouping
---

# 12 · Law of Common Region

> Elements tend to be perceived into groups if they are sharing an area with a clearly defined boundary.

**Category** Gestalt · **Lever** Shared boundary · **Audit weight** High

## What the site says

### Takeaways

1. Common region creates a clear structure and helps users quickly and effectively understand the relationship between elements and sections.
2. Adding a border around an element or group of elements is an easy way to create common region.
3. Common region can also be created by defining a background behind an element or group of elements.

### Origins

The principles of grouping (or Gestalt laws of grouping) are a set of principles in psychology, first proposed by Gestalt psychologists to account for the observation that humans naturally perceive objects as organized patterns and objects, a principle known as Prägnanz. Gestalt psychologists argued that these principles exist because the mind has an innate disposition to perceive patterns in the stimulus based on certain rules. These principles are organized into five categories: Proximity, Similarity, Continuity, Closure, and Connectedness.

*Primary source cited on the site: [en.wikipedia.org](https://en.wikipedia.org/wiki/Principles_of_grouping)*

## Mechanism — why this happens

A closed boundary creates a figure — an object — and everything inside that object is read as belonging to it. This is
the same figure–ground mechanism that lets you see a face rather than a collection of features. The boundary does not
have to be a line: a background tint, a shadow, a card surface, or even a strong change in value all produce the same
effect.

Common region is **stronger than proximity** when the two conflict. Two items 8 px apart inside the same card will read
as one group; two items 4 px apart but separated by a card boundary will read as two. That strength is why it is the
go-to tool for grouping things that are semantically together but physically spread out (a row of stats, a form
section, a pricing tier).

The cost is visual weight. Every boundary you draw is an edge the eye must process, and a screen full of cards reads as
a grid of boxes rather than a page. The discipline is: **use the weakest boundary that works** — space first, then tint,
then border, then shadow.

## Numbers that matter

| Quantity | Value | Consequence for the interface |
|---|---|---|
| Nesting depth | **≤2 levels** | Card inside card inside card is visual noise |
| Card padding | 16–24 px | Below 16, content touches the boundary and reads cramped |
| Gap between sibling cards | ≥ card padding | Otherwise cards read as one broken card |
| Border vs tint | tint is lighter | Prefer a 4–6% surface tint to a 1 px border |
| Corner radius consistency | one value per system | Mixed radii read as different component types |

## Apply it

### Do

- **Use a container for a coherent unit**: a form section, a pricing tier, a stat, a list item with actions.
- **Prefer a subtle surface tint over a border.** `background: color-mix(in srgb, var(--surface) 96%, var(--text-primary))`
  groups without drawing a line.
- **Keep the padding consistent on all four sides.** Asymmetric padding breaks the "object" reading.
- **Let the container carry the group label.** A card with a heading is self-describing; a card without one is a box.
- **Separate the group from its neighbours more than its contents from each other.** A card's outer margin must exceed
  its inner padding, or the grouping inverts.

### Don't

- Don't wrap every element in a card. When everything is a card, nothing is a group.
- Don't nest more than two levels of boundary. Use a heading or a divider instead of a third box.
- Don't use a border *and* a shadow *and* a tint on the same element. Pick one signal.
- Don't put unrelated actions inside the same container — the boundary will claim they belong together.
- Don't let a card's hover state change its geometry (scale, border width). It makes the group boundary jitter.

## Pattern

```css
/* Weakest → strongest boundary. Use the first one that works. */
.group--space   { /* just spacing: margin-block-end: var(--space-8) */ }
.group--tint    { background: var(--surface-raised); padding: var(--space-6); border-radius: var(--radius-md); }
.group--border  { border: 1px solid var(--border); padding: var(--space-6); border-radius: var(--radius-md); }
.group--shadow  { box-shadow: 0 1px 2px rgb(0 0 0 / .06), 0 8px 24px rgb(0 0 0 / .06); }
```

```html
<!-- The outer gap must exceed the inner padding, or the grouping inverts -->
<section class="cards">
  <article class="card">
    <h3 class="card__title">Billing</h3>
    <p class="card__body">Visa ending 4242 · renews Nov 12</p>
    <a href="/billing" class="card__action">Manage</a>
  </article>
  <article class="card">
    <h3 class="card__title">Team</h3>
    <p class="card__body">4 members · 2 pending invites</p>
    <a href="/team" class="card__action">Manage</a>
  </article>
</section>
```

```css
.cards { display: grid; gap: var(--space-6); }        /* 24px between groups */
.card  { padding: var(--space-6); border-radius: var(--radius-md);
         background: var(--surface-raised); }               /* 20px inside the group */
```

## Audit question

> Does every container hold exactly one idea, and is the gap between containers larger than the padding inside them? If
> the outer gap is smaller, the boundaries are lying about the grouping.

## Further reading

| Reading | Author / Publisher |
|---|---|
| [The Principle of Common Region: Containers Create Groupings](https://www.nngroup.com/articles/common-region/) | Aurora Harley \| Nielsen Norman Group |
| [Design Principles: Visual Perception And The Principles Of Gestalt](https://www.smashingmagazine.com/2014/03/design-principles-visual-perception-and-the-principles-of-gestalt/) | Steven Bradley \| Smashing Magazine |
| [Gestalt principles](http://www.scholarpedia.org/article/Gestalt_principles) | Scholarpedia |

---

**Site page** · [lawsofux.com/law-of-common-region](https://lawsofux.com/law-of-common-region/)
