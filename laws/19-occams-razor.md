---
law: Occam's Razor
slug: occams-razor
index: 19
category: simplicity
lever: element count
audit_weight: high
source: https://en.wikipedia.org/wiki/Occam%27s_razor
---

# 19 · Occam's Razor

> Among competing hypotheses that predict equally well, the one with the fewest assumptions should be selected.

**Category** Simplicity · **Lever** Element count · **Audit weight** High

## What the site says

### Takeaways

1. The best method for reducing complexity is to avoid it in the first place.
2. Analyze each element and remove as many as possible, without compromising the overall function.
3. Consider completion only when no additional items can be removed.

### Origins

Occam’s razor (also Ockham’s razor; Latin: lex parsimoniae "law of parsimony") is a problem-solving principle that, when presented with competing hypothetical answers to a problem, one should select the one that makes the fewest assumptions. The idea is attributed to William of Ockham (c. 1287–1347), who was an English Franciscan friar, scholastic philosopher, and theologian.

*Primary source cited on the site: [en.wikipedia.org](https://en.wikipedia.org/wiki/Occam%27s_razor)*

## Mechanism — why this happens

Occam's razor is an **epistemic** principle, not an aesthetic one: among competing explanations that account for the
same observations equally well, prefer the one that posits fewer entities. Its design translation is precise, and it is
not "make it minimal":

> Among competing designs that let the user accomplish the same task equally well, prefer the one with fewer
> **assumptions the user must make**.

That last word is what separates Occam's razor from minimalism as a style. An extra element that removes an assumption
is a *simplification*. A missing element that forces the user to guess is *not* simple — it is under-specified. The
razor cuts assumptions, not pixels.

What counts as an assumption in an interface:

- "I have to know what this icon means."
- "I have to remember what I typed two steps ago."
- "I have to infer whether this action is reversible."
- "I have to understand why this field is required."

Each of those is an entity. A design with fewer of them is simpler, even if it has more elements.

## Numbers that matter

| Quantity | Value | Consequence for the interface |
|---|---|---|
| Assumptions per primary action | **0** | Every one is a place the user can fail |
| Elements per screen serving no task | **0** | Decoration competes for the same attention |
| Steps in the shortest successful path | measured, then matched | The razor applies to steps too |
| Explanations needed for a first-time user | 0–1 | More means the design is carrying complexity it should absorb |

## Apply it

### Do

- **Remove before you add.** When a screen feels heavy, delete an element and check whether the task still succeeds.
  Repeat until deleting one more would break the task. That point is the design.
- **Cut steps, not just pixels.** A two-step flow that could be one step is a razor failure even if both screens are clean.
- **Absorb complexity into defaults** instead of asking. Detect the locale, pre-fill the country, remember the last choice.
- **Remove duplicate information** — the same fact stated twice is two entities for one observation.
- **Prefer one strong signal to three weak ones.** One heading beats a heading plus a divider plus a background tint.
- **Justify every element with a task.** If you cannot name the user task it serves, it is decoration.

### Don't

- Don't cut information the user needs and call it simplicity. That is under-specification; it increases assumptions.
- Don't use "clean" as an argument. Clean is a result of fewer assumptions, not a goal in itself.
- Don't hide essential controls to reduce visual count. Discovery cost is an assumption too.
- Don't simplify the *task* — simplify the *path to the task*. Removing a required field is only valid if it is truly
  not required.
- Don't apply the razor to accessibility features (labels, focus rings, skip links). Those remove assumptions.

## Pattern

```html
<!-- Before: four entities for one observation -->
<div class="card card--shadow">
  <div class="divider"></div>
  <h3 class="title">Billing</h3>
  <p class="subtitle">Billing</p>
  <p class="hint">Your billing information</p>
</div>

<!-- After: one entity — the heading — and the rest of the space does the grouping -->
<section class="panel">
  <h3>Billing</h3>
  <p>Visa ending 4242 · renews Nov 12</p>
</section>
```

```css
/* One signal does the work of three */
.panel { padding-block: var(--space-6); border-block-start: 1px solid var(--border); }
.panel h3 { margin-block-end: var(--space-2); }
```

```html
<!-- Absorb an assumption into a default: the country is known -->
<label for="country">Country</label>
<select id="country" autocomplete="country">
  <option selected>Indonesia</option>
  <!-- ... -->
</select>
```

```js
// Absorb a step: derive it instead of asking
const tz = Intl.DateTimeFormat().resolvedOptions().timeZone;  // no "choose your timezone" screen
const locale = navigator.language;                            // no "choose your language" screen
```

## Audit question

> For each element on the screen, name the user task it serves. For each step in the flow, name the assumption it
> removes. Elements with no task and steps that remove nothing are candidates for deletion.

## Further reading

| Reading | Author / Publisher |
|---|---|
| [How to Use Occam’s Razor Without Getting Cut](https://fs.blog/occams-razor/) | Farnam Street |
| [Designing with Occam’s Razor](https://medium.com/@jonyablonski/designing-with-occams-razor-3692df2f3c7f) | Jon Yablonski \| Medium |
| [Occam’s Razor: The Simplest Solution is Always the Best](https://www.interaction-design.org/literature/article/occam-s-razor-the-simplest-solution-is-always-the-best) | Mads Soegaard \| Interaction Design Foundation |
| [Complexity Bias: Why We Prefer Complicated to Simple](https://fs.blog/complexity-bias/) | Farnam Street |
| [Occam’s Razor: A Great Principle for Designers](https://www.webdesignerdepot.com/2010/07/occams-razor-a-great-principle-for-designers/) | Web Designer Depot |

---

**Site page** · [lawsofux.com/occams-razor](https://lawsofux.com/occams-razor/)
