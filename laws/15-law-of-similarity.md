---
law: Law of Similarity
slug: law-of-similarity
index: 15
category: gestalt
lever: visual sameness
audit_weight: high
source: https://en.wikipedia.org/wiki/Principles_of_grouping
---

# 15 · Law of Similarity

> The human eye tends to perceive similar elements as a complete picture, shape, or group, even if those elements are separated.

**Category** Gestalt · **Lever** Visual sameness · **Audit weight** High

## What the site says

### Takeaways

1. Elements that are visually similar will be perceived as related.
2. Color, shape, and size, orientation and movement can signal that elements belong to the same group and likely share a common meaning or functionality.
3. Ensure that links and navigation systems are visually differentiated from normal text elements.

### Origins

The principles of grouping (or Gestalt laws of grouping) are a set of principles in psychology, first proposed by Gestalt psychologists to account for the observation that humans naturally perceive objects as organized patterns and objects, a principle known as Prägnanz. Gestalt psychologists argued that these principles exist because the mind has an innate disposition to perceive patterns in the stimulus based on certain rules. These principles are organized into five categories: Proximity, Similarity, Continuity, Closure, and Connectedness.

*Primary source cited on the site: [en.wikipedia.org](https://en.wikipedia.org/wiki/Principles_of_grouping)*

## Mechanism — why this happens

The visual system groups by shared attributes: same color, same shape, same size, same orientation, same type
treatment. Similarity is how the eye builds **categories** before the mind reads labels — which means it is also how
the interface teaches "these things are the same kind of thing".

That gives the law two directions, and most interfaces only apply one:

- **Same function → same appearance.** All primary actions look identical; all destructive actions look identical.
  This is what makes a design system feel coherent.
- **Different function → different appearance.** If a link and a button look the same, users will click the wrong one.
  If "save" and "delete" share a style, the style has stopped carrying meaning.

Similarity is weaker than common region and uniform connectedness when they conflict, but it is stronger than proximity
in one specific case: **a repeated color or shape will group items across a large distance**, which is why color-coding
works in dense tables and calendars.

## Numbers that matter

| Quantity | Value | Consequence for the interface |
|---|---|---|
| Distinct button styles | **≤3** (primary, secondary, danger) | A fourth means the system has lost its vocabulary |
| Distinct link treatments | 1 | Underline or color, not both inconsistently |
| Color-coded categories | ≤5–6 | Beyond that, colors are no longer distinguishable |
| Icon style per set | 1 (outline *or* filled) | Mixing is two languages |
| Repeated element spacing | identical | Inconsistency reads as a different type |

## Apply it

### Do

- **Define a small component vocabulary** and use it everywhere: primary, secondary, ghost, danger. If a new button
  does not fit, question the button, not the system.
- **Make links look like links** (accent color, underline on hover, cursor) and buttons look like buttons (surface,
  padding, border). Never style a link as a button unless it performs an action.
- **Use similarity to encode state**, not to decorate: all "completed" steps share one treatment, all "pending" another.
- **Keep repeated components pixel-identical.** A card that is 1 px different from its siblings reads as a different
  component and costs the user a re-read.
- **Color-code with restraint and pair it with a second channel** (icon or label) for accessibility.

### Don't

- Don't use the same visual style for different meanings. Red text that sometimes means error and sometimes means
  "featured" destroys the signal.
- Don't use accent color for non-interactive text. It teaches users that accent = clickable, then punishes them.
- Don't let "special case" components accumulate. Each one dilutes the vocabulary.
- Don't rely on color alone to distinguish categories; ~8% of men have a color vision deficiency.
- Don't make disabled states look like enabled states with lower opacity only — pair with cursor and `aria-disabled`.

## Pattern

```css
/* One vocabulary: three button roles, one link role */
.btn            { display: inline-flex; align-items: center; gap: var(--space-2);
                  min-block-size: 44px; padding-inline: var(--space-6);
                  border-radius: var(--radius-md); font-weight: 600;
                  border: 1px solid transparent; }
.btn--primary   { background: var(--accent); color: var(--on-accent); }
.btn--secondary { background: transparent; color: var(--text-primary); border-color: var(--border); }
.btn--danger    { background: var(--danger); color: var(--on-accent); }

.link { color: var(--accent); text-decoration: none; }
.link:hover { text-decoration: underline; }
.link:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
```

```html
<!-- Same function, same appearance — across the whole product -->
<div class="actions">
  <button class="btn btn--primary">Save changes</button>
  <button class="btn btn--secondary">Cancel</button>
  <button class="btn btn--danger">Delete project</button>
</div>
```

```html
<!-- Bad: link styled as a button, button styled as a link -->
<a class="btn btn--primary" href="/docs">Read the docs</a>
<button class="link">Submit</button>

<!-- Better: navigate vs act is visually distinct -->
<a class="link" href="/docs">Read the docs</a>
<button class="btn btn--primary">Submit</button>
```

## Audit question

> Do all elements that do the same thing look identical, and do all elements that look identical do the same thing? If
> either answer is no, the visual language is lying.

## Further reading

| Reading | Author / Publisher |
|---|---|
| [Gestalt Principles of Design — Similarity](https://www.chrbutler.com/gestalt-principles-of-design-similarity) | Chris Butler |
| [Similarity Principle in Visual Design](https://www.nngroup.com/articles/gestalt-similarity/) | Aurora Harley \| Nielson Norman Group |
| [The Law of Similarity - Gestalt Principles](https://www.interaction-design.org/literature/article/the-law-of-similarity-gestalt-principles-1) | Interaction Deisgn Foundation \| Mads Soegaard |
| [Design Principles: Visual Perception And The Principles Of Gestalt](https://www.smashingmagazine.com/2014/03/design-principles-visual-perception-and-the-principles-of-gestalt/) | Steven Bradley \| Smashing Magazine |
| [Use Gestalt Laws to Improve Your UX](http://blog.usabilla.com/gestalt-laws-start-with-thinking-basic/) | Sabina Idler \| Usabilla Blog |

---

**Site page** · [lawsofux.com/law-of-similarity](https://lawsofux.com/law-of-similarity/)
