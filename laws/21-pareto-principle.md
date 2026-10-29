---
law: Pareto Principle
slug: pareto-principle
index: 21
category: prioritisation
lever: effort allocation
audit_weight: high
source: https://en.wikipedia.org/wiki/Pareto_principle
---

# 21 · Pareto Principle

> The Pareto principle states that, for many events, roughly 80% of the effects come from 20% of the causes.

**Category** Prioritisation · **Lever** Effort allocation · **Audit weight** High

## What the site says

### Takeaways

1. Inputs and outputs are often not evenly distributed.
2. A large group may contain only a few meaningful contributors to the desired outcome.
3. Focus the majority of effort on the areas that will bring the largest benefits to the most users.

### Origins

Its origins stem back to Vilfredo Pareto, an economist who noticed 80% of Italy’s land was owned by 20% of the population. Though it might seem vague, the 80/20 way of thinking can provide insightful and endlessly applicable analysis of lopsided systems, including user experience strategy.

*Primary source cited on the site: [medium.com](https://medium.com/design-ibm/the-80-20-rule-in-user-experience-1695de32aaae)*

## Mechanism — why this happens

The 80/20 rule is an observation about **skew**, not a law of nature: in many systems a small number of inputs produce
a large share of the output. In interfaces the skew is usually even sharper than 80/20, because usage concentrates on
the shortest path to the core value.

For design, the principle does two jobs:

1. **Allocation.** Spend the design budget — spacing, states, polish, performance, testing — proportionally to usage,
   not proportionally to feature count.
2. **Simplification.** The long tail is real but rare. It belongs behind progressive disclosure, not on the main screen.

The trap is treating 80/20 as a licence to delete the tail. The tail is where power users live, and power users are
often the ones who renew. The correct move is **not removal but relocation**: the 20% gets the prime real estate, the
80% gets a reachable, well-organised secondary path.

## Numbers that matter

| Quantity | Value | Consequence for the interface |
|---|---|---|
| Core actions | ~20% of features | Deserve the primary surface, the polish, the tests |
| Usage share | ~80% of interactions | The justification for prioritisation |
| Primary navigation | 5–7 items | The core 20% made explicit |
| Long-tail access | 1 click away | Reachable, not prominent |
| Design/QA effort split | 80% on core paths | The rest gets consistency, not investment |

## Apply it

### Do

- **Instrument first.** You cannot apply Pareto without usage data. Find the top 5 actions and the top 5 screens.
- **Give the core path the best real estate**: above the fold, larger targets, fewer steps, more polish.
- **Make the long tail reachable but quiet** — a "More" menu, an advanced tab, a secondary settings page.
- **Allocate performance work by frequency.** Optimising a screen 2% of users see is a rounding error.
- **Apply it to content too.** 20% of help articles answer 80% of questions; surface those in the empty states.
- **Re-check quarterly.** Usage skew moves; last year's core path may be this year's tail.

### Don't

- Don't delete features because they are rare. Relocate them.
- Don't use Pareto to justify ignoring accessibility, error states, or edge cases — those are not "the tail", they are
  the floor.
- Don't guess the 80/20 split. Without data it is a story, not a prioritisation.
- Don't let the core path become the only path; power users hit the ceiling and leave.
- Don't apply it to visual design as "polish 20% of the screen". Polish is a property of the whole surface.

## Pattern

```html
<!-- Core 20% on the surface, tail one click away -->
<div class="toolbar" role="toolbar" aria-label="Editor actions">
  <button class="btn btn--primary">Publish</button>
  <button class="btn btn--secondary">Preview</button>
  <button class="btn btn--ghost" aria-label="Bold"><b>B</b></button>
  <button class="btn btn--ghost" aria-label="Italic"><i>I</i></button>
  <details class="menu">
    <summary class="btn btn--ghost">More</summary>
    <ul>
      <li><button>Insert table</button></li>
      <li><button>Insert code block</button></li>
      <li><button>Export as PDF</button></li>
    </ul>
  </details>
</div>
```

```css
.toolbar { display: flex; align-items: center; gap: var(--space-2); flex-wrap: wrap; }
.toolbar .btn--primary { margin-inline-end: var(--space-3); }
.menu { position: relative; }
.menu > ul { position: absolute; inset-block-start: calc(100% + var(--space-2)); inset-inline-end: 0;
             min-inline-size: 200px; padding: var(--space-2); margin: 0; list-style: none;
             background: var(--surface); border: 1px solid var(--border);
             border-radius: var(--radius-md); box-shadow: 0 8px 24px rgb(0 0 0 / .12); }
```

```js
// Measure before you prioritise: the top actions are the design budget
const top = events
  .reduce((m, e) => (m[e.action] = (m[e.action] || 0) + 1, m), {});
const ranked = Object.entries(top).sort((a, b) => b[1] - a[1]).slice(0, 5);
console.table(ranked);   // these five get the polish
```

## Audit question

> List the five most frequent user actions. Do they have the largest targets, the fewest steps, and the most polish on
> the screen? If not, the design budget is being spent on the wrong 80%.

## Further reading

| Reading | Author / Publisher |
|---|---|
| [Good UX is not just about minimizing clicks](https://uxdesign.cc/good-ux-is-not-just-about-minimizing-clicks-5504fa2ff430) | Avi Siegel \| UX Collective |
| [Prioritize Quantitative Data with the Pareto Principle](https://www.nngroup.com/articles/pareto-principle/) | Evan Sunwall \| Nielsen Norman Group |
| [The 80/20 Rule in User Experience](https://medium.com/design-ibm/the-80-20-rule-in-user-experience-1695de32aaae) | Arin Bhowmick \| Medium |
| [Applying the Pareto Principle to the User Experience](https://measuringu.com/pareto-ux/) | Jeff Sauro \| Measuring U |
| [The Pareto Principle and Your User Experience Work](https://www.interaction-design.org/literature/article/the-pareto-principle-and-your-user-experience-work) | Interaction Design Foundation |
| [Pareto Principle on Wikipedia](https://en.wikipedia.org/wiki/Pareto_principle) | Wikipedia |

---

**Site page** · [lawsofux.com/pareto-principle](https://lawsofux.com/pareto-principle/)
