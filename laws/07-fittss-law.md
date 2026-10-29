---
law: Fitts's Law
slug: fittss-law
index: 7
category: motor
lever: target size and distance
audit_weight: critical
source: https://www.interaction-design.org/literature/topics/fitts-law
---

# 07 · Fitts's Law

> The time to acquire a target is a function of the distance to and size of the target.

**Category** Motor control · **Lever** Target size × distance · **Audit weight** Critical

## What the site says

### Takeaways

1. Touch targets should be large enough for users to accurately select them.
2. Touch targets should have ample spacing between them.
3. Touch targets should be placed in areas of an interface that allow them to be easily acquired.

### Origins

In 1954, psychologist Paul Fitts, examining the human motor system, showed that the time required to move to a target depends on the distance to it, yet relates inversely to its size. By his law, fast movements and small targets result in greater error rates, due to the speed-accuracy trade-off. Although multiple variants of Fitts’ law exist, all encompass this idea. Fitts’ law is widely applied in user experience (UX) and user interface (UI) design. For example, this law influenced the convention of making interactive buttons large (especially on finger-operated mobile devices)—smaller buttons are more difficult (and time-consuming) to click. Likewise, the distance between a user’s task/attention area and the task-related button should be kept as short as possible.

*Primary source cited on the site: [interaction-design.org](https://www.interaction-design.org/literature/topics/fitts-law)*

## Mechanism — why this happens

Pointing is a closed-loop motor task with noise. The hand moves fast toward the target, then slows to correct. The
smaller and farther the target, the more correction cycles are needed, and the time cost is **logarithmic in the ratio
of distance to width** — not linear in either one.

The Shannon formulation, which is what modern HCI uses:

```
MT = a + b · log₂( D / W + 1 )
```

where `MT` is movement time, `D` is distance to the target centre, `W` is target width along the axis of movement, and
`a`, `b` are empirically fitted constants. The term `log₂(D/W + 1)` is the **index of difficulty (ID)**, measured in
bits. Throughput (`ID / MT`, in bits per second) is roughly stable for a given device and posture — which is the useful
part: **you cannot make a person faster by asking, only by changing D and W.**

Two consequences that are easy to miss:

1. **Halving distance and doubling width are equivalent.** Both reduce ID by about one bit.
2. **Targets at screen edges and corners have effectively infinite width** on desktop, because the pointer cannot
   overshoot. That is why menu bars live at the top edge and why "Fitts's law targets" are a real design technique.

## Numbers that matter

| Quantity | Value | Consequence for the interface |
|---|---|---|
| Minimum touch target (Apple HIG) | **44 × 44 pt** | Below this, error rate climbs on mobile |
| Minimum touch target (Material) | **48 × 48 dp** | Android equivalent |
| Minimum WCAG 2.2 target (AA) | **24 × 24 CSS px** | The accessibility floor, not the comfort floor |
| Spacing between adjacent targets | **≥8 px** | Prevents mis-taps between neighbours |
| Primary button height | 44–48 px | Comfortable on both pointer and touch |
| Desktop edge targets | infinite width | Use screen edges for frequent actions |
| Icon-only button | 44 × 44 px hit area | The glyph may be 20 px; the *hit area* is 44 |

## Apply it

### Do

- **Make the whole row clickable**, not just the text link. The hit area is free real estate.
- **Keep destructive and primary actions far apart.** Adjacent "Delete" and "Save" is a Fitts's-law trap.
- **Use edge and corner positions** for high-frequency desktop actions (menu bar, dock, floating action at bottom).
- **Size by importance and frequency**, not by visual symmetry. The most-used control should be the largest.
- **Give icon buttons a 44 × 44 hit area** even when the icon is 20 px, with `padding` or a pseudo-element.
- **Place form actions at the end of the reading flow**, close to where the user's attention already is.
- **On mobile, put primary actions in the thumb zone** (bottom third), not at the top of the screen.

### Don't

- Don't use text links as the only target for a primary action on touch. Minimum 44 px.
- Don't place small icon buttons in a row with 4 px gaps — mis-taps become routine.
- Don't put the close button of a modal in a corner *and* make it 16 px. That is the most common accessibility failure in dialogs.
- Don't make targets large but ambiguous (a big button labelled "Continue" that does two different things).
- Don't rely on hover to reveal the real target size; touch has no hover.

## Pattern

```css
/* Icon button: 20px glyph, 44px hit area — the glyph is not the target */
.icon-btn {
  display: inline-grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  padding: 0;
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  background: var(--surface);
}
.icon-btn > svg { inline-size: 20px; block-size: 20px; }

/* Adjacent targets need breathing room */
.action-row { display: flex; gap: var(--space-3); }   /* ≥12px, above the 8px floor */

/* Primary action sized for touch, placed at the end of the flow */
.btn-primary { min-block-size: 44px; padding-inline: var(--space-6); }
```

```html
<!-- Whole card is the target; the link inside is a label, not the hit area -->
<a class="card" href="/project/42">
  <h3>Website redesign</h3>
  <p>Updated 2 hours ago</p>
</a>
```

```css
.card { display: block; padding: var(--space-4); border-radius: var(--radius-md); }
.card:hover { background: var(--surface-raised); }
```

## Audit question

> Measure the smallest interactive element on the primary path. Is it at least 44 × 44 px on touch, and at least 8 px
> away from its nearest neighbour?

## Further reading

| Reading | Author / Publisher |
|---|---|
| [Fitts's Law and Its Applications in UX](https://www.nngroup.com/articles/fitts-law/) | Nielsen Norman Group |
| [Fitts’ Law In The Touch Era](https://www.smashingmagazine.com/2022/02/fitts-law-touch-era/) | Smashing Magazine |
| [Fitts’s Law: The Importance of Size and Distance in UI Design](https://www.interaction-design.org/literature/article/fitts-s-law-the-importance-of-size-and-distance-in-ui-design) | Interaction Design Foundation |
| [Fitts’s Law on Wikipedia](https://en.wikipedia.org/wiki/Fitts%27s_law) | Wikipedia |
| [Design for Fingers, Touch, and People, Part 1](https://www.uxmatters.com/mt/archives/2017/03/design-for-fingers-touch-and-people-part-1.php) | Steven Hoober \| UX Matters |
| [The information capacity of the human motor system in controlling the amplitude of movement](https://pdfs.semanticscholar.org/634c/9fde5f1c411e4487658ac738dcf18d98ea8d.pdf) | Semantic Scholar |

---

**Site page** · [lawsofux.com/fittss-law](https://lawsofux.com/fittss-law/)
