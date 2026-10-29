---
law: Serial Position Effect
slug: serial-position-effect
index: 26
category: memory
lever: position in a sequence
audit_weight: high
source: https://en.wikipedia.org/wiki/Serial-position_effect
---

# 26 · Serial Position Effect

> Users have a propensity to best remember the first and last items in a series.

**Category** Memory · **Lever** Position in a sequence · **Audit weight** High

## What the site says

### Takeaways

1. Placing the least important items in the middle of lists can be helpful because these items tend to be stored less frequently in long-term and working memory.
2. Positioning key actions on the far left and right within elements such as navigation can increase memorization.

### Origins

The serial position effect, a term coined by Herman Ebbinghaus, describes how the position of an item in a sequence affects recall accuracy. The two concepts involved, the primacy effect and the recency effect, explains how items presented at the beginning of a sequence and the end of a sequence are recalled with greater accuracy than items in the middle of a list. Manipulation of the serial position effect to create better user experiences is reflected in many popular designs by successful companies like Apple, Electronic Arts, and Nike.

*Primary source cited on the site: [interaction-design.org](https://www.interaction-design.org/literature/topics/serial-position-effect)*

## Mechanism — why this happens

When people recall a sequence, recall is not uniform. The first items are rehearsed most and enter long-term memory
(**primacy**); the last items are still in working memory when recall begins (**recency**). Items in the middle are
neither, and they are the ones that disappear.

The classic curve looks like this:

```
recall
  │ ●                                    ●
  │ ●  ●                              ●  ●
  │ ●  ●  ●                        ●  ●  ●
  │ ●  ●  ●  ●  ●  ●  ●  ●  ●  ●  ●  ●  ●  ●
  └──────────────────────────────────────────
    first        middle          last
    (primacy)                    (recency)
```

The middle is a valley, and it is where interfaces put their least-remembered content. Two design consequences:

1. **Position is a memory modifier.** Moving an item from the middle to an end changes how well it is remembered, without
   changing the item.
2. **The recency effect is fragile.** It depends on the last items still being in working memory; if the user is
   interrupted or the list is long, recency collapses and only primacy survives.

## Numbers that matter

| Quantity | Value | Consequence for the interface |
|---|---|---|
| Primacy span | first ~3–4 items | Put the most important items first |
| Recency span | last ~2–3 items | Put the second-most important items last |
| Middle valley | everything between | Do not put critical items here |
| List length before the valley dominates | ~7+ | Long lists need grouping or search |
| Navigation emphasis | first and last slots | Home first, account/action last |

## Apply it

### Do

- **Put the most important item first** and the second-most important last. That is the whole technique.
- **Use the ends of navigation** for the highest-value destinations: brand/home first, primary action last.
- **Group long lists** so each group has its own primacy and recency, instead of one long valley.
- **Repeat critical information at the end** of a long form or article — the summary is remembered, the middle is not.
- **Order onboarding steps deliberately**: the first step sets the frame, the last step is what they remember doing.
- **Put "what happens next" at the end** of any multi-step flow.

### Don't

- Don't bury pricing, terms, or the primary CTA in the middle of a long page and expect it to be remembered.
- Don't rely on a middle item being seen because it is visually styled; position beats styling in recall.
- Don't assume a user who scrolled the whole page remembers the middle.
- Don't put two equally important items at the two ends — that is a tie the user resolves arbitrarily.
- Don't use position alone; pair it with visual hierarchy so the eye and the memory agree.

## Pattern

```html
<!-- Navigation: highest-value first and last -->
<nav class="nav" aria-label="Main">
  <a href="/" class="nav__brand">Acme</a>
  <ul class="nav__list">
    <li><a href="/product">Product</a></li>
    <li><a href="/pricing">Pricing</a></li>
    <li><a href="/docs">Docs</a></li>
  </ul>
  <a href="/signup" class="btn btn--primary">Start free</a>  <!-- last = remembered -->
</nav>
```

```html
<!-- Long form: summarise at the end, where recency works for you -->
<form class="checkout">
  <!-- ... fields ... -->
  <section class="summary" aria-labelledby="sum-title">
    <h2 id="sum-title">Before you pay</h2>
    <ul>
      <li>Pro plan, yearly — $228 today</li>
      <li>5 seats, billed annually</li>
      <li>Cancel any time from Settings</li>
    </ul>
  </section>
  <button class="btn btn--primary">Pay $228</button>
</form>
```

```html
<!-- Onboarding: first step sets the frame, last step states the outcome -->
<ol class="steps">
  <li class="steps__item is-done">Connect your data</li>
  <li class="steps__item">Choose a template</li>
  <li class="steps__item is-current">Invite your team</li>
</ol>
```

## Audit question

> Rank the items on this screen by importance. Do the top two sit at the beginning and the end of the sequence? If the
> most important item is in the middle, position is fighting the content.

## Further reading

| Reading | Author / Publisher |
|---|---|
| [Serial Position Effect: How to Create Better User Interfaces](https://www.interaction-design.org/literature/article/serial-position-effect-how-to-create-better-user-interfaces) | Euphemia Wong \| Interaction Design Foundation |
| [The Serial Position Effect: Why ABC and XYZ Stand Out the Most Among All the Alphabets](https://medium.com/coffee-and-junk/design-psychology-serial-position-effect-ca0e4cf299cb) | Abhishek Chakraborty \| Medium.com |
| [Psychology in Design (Part 1)](https://blog.prototypr.io/psychology-in-design-part-1-cdc63229cbe4) | Andri Budzinskiy \| Medium.com |
| [Serial Position Effect on Wikipedia](https://en.wikipedia.org/wiki/Serial-position_effect) | Wikipedia |

---

**Site page** · [lawsofux.com/serial-position-effect](https://lawsofux.com/serial-position-effect/)
