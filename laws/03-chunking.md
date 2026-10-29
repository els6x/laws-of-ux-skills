---
law: Chunking
slug: chunking
index: 3
category: memory
lever: grouping
audit_weight: high
source: https://en.wikipedia.org/wiki/Chunking_(psychology)
---

# 03 · Chunking

> A process by which individual pieces of an information set are broken down and then grouped together in a meaningful whole.

**Category** Memory · **Lever** Grouping content into meaningful wholes · **Audit weight** High

## What the site says

### Takeaways

1. Chunking enables users to easily scan content. It allows them to easily identify the information that aligns with their goals and process that information to achieve their goals more quickly.
2. Structuring content into visually distinct groups with a clear hierarchy enables designers to align information with how people evaluate and process digital content.
3. Chunking can be used to help users understand underlying relationships by grouping content into distinctive modules, applying rules to separate content, and providing hierarchy.

### Origins

The word chunking comes from a famous 1956 paper by George A. Miller, “The Magical Number Seven, Plus or Minus Two: Some Limits on Our Capacity for Processing Information”. At a time when information theory was beginning to be applied in psychology, Miller observed that some human cognitive tasks fit the model of a “channel capacity” characterized by a roughly constant capacity in bits, but short-term memory did not.

*Primary source cited on the site: [interaction-design.org](https://www.interaction-design.org/literature/book/the-glossary-of-human-computer-interaction/chunking)*

## Mechanism — why this happens

Working memory holds **chunks**, not items. A chunk is a unit that is already meaningful to the person holding it —
"555-0134" is seven digits but roughly two chunks, because the dash lets the mind store "555" and "0134" as units.
This is why chunking works: it does not increase capacity, it increases **density per slot**.

The design implication is a shift in what you are counting. When you ask "is this form too long?", the wrong unit is
fields. The right unit is *groups the user can hold as one idea* — "shipping address", "payment", "confirm".

There is a second, more useful implication: chunk boundaries are **semantic**, so a good chunk has a name. If you cannot
label a group, it is not a chunk; it is just a pile.

## Numbers that matter

| Quantity | Value | Consequence for the interface |
|---|---|---|
| Miller (1956) | 7 ± 2 chunks | Historical upper bound — a ceiling, not a target |
| Cowan (2001) | ~4 chunks | Modern estimate for pure storage; assume 4 |
| Practical group size | **3–5 items** | What a group can hold before it needs a sub-label |
| Phone number format | 3-4 split (`555-0134`) | The canonical chunking example |
| Card number format | 4-4-4-4 | 16 digits become 4 chunks |

## Apply it

### Do

- **Group form fields by meaning, then label the group.** "Contact", "Shipping", "Payment" with 3–5 fields each beats
  one list of 14 fields, even at identical total length.
- **Format long numbers as users type.** Card `4242 4242 4242 4242`, phone `(555) 013-4000`, IBAN in groups of four.
  The formatting is not cosmetic; it is the chunk delimiter.
- **Break multi-step tasks into named steps** with a visible count ("Step 2 of 4"). The step is the chunk.
- **Use headings as chunk boundaries.** A section heading tells working memory "you may close the previous group".
- **Keep each navigation level to ≤7 items**, and each group within it to 3–5.
- **Chunk by task, not by database schema.** Users chunk by intent ("where does it go"), not by table.

### Don't

- Don't use 7 as a quota to fill. Miller's number is a limit, and the modern working figure is closer to 4.
- Don't split a coherent idea across two visual groups just to balance column heights — that destroys the chunk.
- Don't chunk visually without chunking semantically (a divider between unrelated items is worse than no divider).
- Don't put more than ~5 actions in one button row. Group secondary actions under a menu instead.

## Pattern

```html
<!-- Bad: 12 ungrouped fields -->
<input name="first"><input name="last"><input name="email">
<input name="street"><input name="city"><input name="zip">
<input name="card"><input name="exp"><input name="cvc">
<input name="coupon"><input name="notes"><input name="phone">

<!-- Better: 3 named chunks, each ≤4 fields -->
<fieldset>
  <legend>Contact</legend>
  <input name="first" autocomplete="given-name">
  <input name="last" autocomplete="family-name">
  <input name="email" type="email" autocomplete="email">
</fieldset>
<fieldset>
  <legend>Shipping address</legend>
  <input name="street" autocomplete="street-address">
  <input name="city" autocomplete="address-level2">
  <input name="zip" inputmode="numeric" autocomplete="postal-code">
</fieldset>
<fieldset>
  <legend>Payment</legend>
  <input name="card" inputmode="numeric" autocomplete="cc-number" placeholder="4242 4242 4242 4242">
  <input name="exp" autocomplete="cc-exp">
  <input name="cvc" inputmode="numeric" autocomplete="cc-csc">
</fieldset>
```

```css
fieldset { border: 0; padding: 0; margin-block-end: var(--space-6); }
fieldset > * + * { margin-block-start: var(--space-3); }
legend { font-weight: 600; margin-block-end: var(--space-3); }
```

## Audit question

> Does every group on this screen have a name, and does it hold five items or fewer? If a group has no name, it is
> not a chunk.

## Further reading

| Reading | Author / Publisher |
|---|---|
| [How Chunking Helps Content Processing](https://www.nngroup.com/articles/chunking/) | Kate Moran \| Nielsen Norman Group |
| [Chunking](https://www.interaction-design.org/literature/book/the-glossary-of-human-computer-interaction/chunking) | Interaction Design Foundation |
| [Why Chunking Content is Important [Video]](https://www.nngroup.com/videos/chunking/) | Kate Moran \| Nielsen Norman Group |

---

**Site page** · [lawsofux.com/chunking](https://lawsofux.com/chunking/)
