---
law: Von Restorff Effect
slug: von-restorff-effect
index: 28
category: attention
lever: distinctiveness
audit_weight: high
source: https://en.wikipedia.org/wiki/Von_Restorff_effect
---

# 28 · Von Restorff Effect

> The Von Restorff effect, also known as The Isolation Effect, predicts that when multiple similar objects are present, the one that differs from the rest is most likely to be remembered.

**Category** Attention · **Lever** Distinctiveness · **Audit weight** High

## What the site says

### Takeaways

1. Make important information or key actions visually distinctive.
2. Use restraint when placing emphasis on visual elements to avoid them competing with one another and to ensure salient items don’t get mistakenly identified as ads.
3. Don’t exclude those with a color vision deficiency or low vision by relying exclusively on color to communicate contrast.
4. Carefully consider users with motion sensitivity when using motion to communicate contrast.

### Origins

The theory was coined by German psychiatrist and pediatrician Hedwig von Restorff (1906–1962), who, in her 1933 study, found that when participants were presented with a list of categorically similar items with one distinctive, isolated item on the list, memory for the item was improved.

*Primary source cited on the site: [en.wikipedia.org](https://en.wikipedia.org/wiki/Von_Restorff_effect)*

## Mechanism — why this happens

Hedwig von Restorff's 1933 experiments showed that an item which differs from its neighbours is recalled better than
items which do not. The mechanism is **distinctiveness**: isolation makes an item easier to encode, because it has fewer
competitors for the same memory trace.

For interfaces, the effect is the basis of every "highlight the recommended plan" pattern — and also the basis of its
most common failure. The effect depends on **contrast with the surrounding set**. If two items are highlighted, neither
is isolated; if five are highlighted, the set has simply changed and nothing stands out. Distinctiveness is a
zero-sum resource: **every additional highlight reduces the value of the others**.

There is a second failure mode worth naming: **highlighting the wrong thing**. Von Restorff predicts the isolated item
will be remembered, not that it will be *chosen*. A red "Delete" button is remembered; that is not a reason to make it
the most prominent element on the screen.

## Numbers that matter

| Quantity | Value | Consequence for the interface |
|---|---|---|
| Distinct items per view | **1** | Two is a tie; the effect cancels |
| Highlight techniques | 1 per element | Color + size + border + badge is noise, not emphasis |
| Contrast ratio of the highlight vs the set | clearly higher | If it blends at a squint, it is not distinct |
| Recommended-plan highlights | exactly 1 | "Most popular" on three plans means nothing |
| Reuse of the accent for emphasis | ≤2 per screen | Beyond that, the accent stops meaning "special" |

## Apply it

### Do

- **Highlight exactly one thing per view** — the recommended plan, the primary action, the new item.
- **Use one technique.** A filled accent button among ghost buttons is enough; do not also add a badge, a glow, and a
  larger size.
- **Make the distinction survive a squint test.** If the highlighted element disappears when you blur your eyes, the
  contrast is insufficient.
- **Use it to guide, not to decorate.** The isolated element should be the one you want chosen or noticed.
- **Reset the baseline.** If everything has been highlighted over time, remove the highlights and start again.

### Don't

- Don't highlight multiple items in the same set. The effect requires a minority of one.
- Don't use the accent color for non-emphasised elements; it spends the distinctiveness budget.
- Don't rely on color alone — add a label ("Recommended") so the distinction survives color blindness.
- Don't make destructive actions the most visually distinct thing on the screen.
- Don't animate the highlight continuously. Motion competes with the isolation and reads as an ad.

## Pattern

```html
<!-- Exactly one highlighted plan, with a non-color cue -->
<ul class="plans">
  <li class="plan">
    <h3>Free</h3><p class="plan__price">$0</p>
    <button class="btn btn--secondary">Choose Free</button>
  </li>
  <li class="plan plan--featured">
    <p class="plan__badge">Recommended</p>
    <h3>Pro</h3><p class="plan__price">$24<span>/mo</span></p>
    <button class="btn btn--primary">Choose Pro</button>
  </li>
  <li class="plan">
    <h3>Team</h3><p class="plan__price">$79</p>
    <button class="btn btn--secondary">Choose Team</button>
  </li>
</ul>
```

```css
.plans { display: grid; gap: var(--space-4); grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); }
.plan { display: grid; gap: var(--space-3); padding: var(--space-6);
        border: 1px solid var(--border); border-radius: var(--radius-lg); background: var(--surface); }
.plan--featured { border-color: var(--accent); box-shadow: 0 0 0 1px var(--accent); }
.plan__badge { margin: 0; font-size: var(--text-sm); font-weight: 600; color: var(--accent); }
.plan__price { font-size: var(--text-2xl); font-weight: 700; }
.plan__price span { font-size: var(--text-sm); color: var(--text-secondary); font-weight: 400; }
```

```html
<!-- A new item in a list: isolated by one cue, not five -->
<li class="row row--new">
  <span class="row__title">Q4 report</span>
  <span class="row__tag">New</span>
</li>
```

```css
.row--new { background: color-mix(in srgb, var(--accent) 6%, transparent); }
.row__tag { font-size: var(--text-sm); color: var(--accent); font-weight: 600; }
```

## Audit question

> Squint at the screen. How many elements still stand out? If more than one, none of them is isolated and the effect is
> being spent for nothing.

## Further reading

| Reading | Author / Publisher |
|---|---|
| [Psychology in Design (Part 1)](https://blog.prototypr.io/psychology-in-design-part-1-cdc63229cbe4) | Andri Budzinskiy \| Medium.com |
| [The Psychology Principles Every UI/UX Designer Needs to Know](https://blog.marvelapp.com/psychology-principles-every-uiux-designer-needs-know/) | Thanasis Rigopoulos \| Marvel |
| [Von Restorff Effect on Wikipedia](https://en.wikipedia.org/wiki/Von_Restorff_effect) | Wikipedia |
| [Superior pattern processing is the essence of the evolved human brain](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4141622/) | Mark P. Mattson |
| [Working Memory and Attention – A Conceptual Analysis and Review](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6688548/) | Klaus Oberauer |

---

**Site page** · [lawsofux.com/von-restorff-effect](https://lawsofux.com/von-restorff-effect/)
