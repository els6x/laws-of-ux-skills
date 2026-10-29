---
law: Miller's Law
slug: millers-law
index: 18
category: memory
lever: working memory capacity
audit_weight: high
source: https://en.wikipedia.org/wiki/Working_memory
---

# 18 · Miller's Law

> The average person can only keep 7 (plus or minus 2) items in their working memory.

**Category** Memory · **Lever** Working memory capacity · **Audit weight** High

## What the site says

### Takeaways

1. Don’t use the “magical number seven” to justify unnecessary design limitations.
2. Organize content into smaller chunks to help users process, understand, and memorize easily.
3. Remember that short-term memory capacity will vary per individual, based on their prior knowledge and situational context.

### Origins

In 1956, George Miller asserted that the span of immediate memory and absolute judgment were both limited to around 7 pieces of information. The main unit of information is the bit, the amount of data necessary to make a choice between two equally likely alternatives. Likewise, 4 bits of information is a decision between 16 binary alternatives (4 successive binary decisions). The point where confusion creates an incorrect judgment is the channel capacity. In other words, the quantity of bits which can be transmitted reliably through a channel, within a certain amount of time.

*Primary source cited on the site: [khanacademy.org](https://www.khanacademy.org/test-prep/mcat/social-sciences-practice/social-science-practice-tut/e/miller-s-law--chunking--and-the-capacity-of-working-memory)*

## Mechanism — why this happens

Miller's 1956 paper is one of the most cited and most misapplied findings in design. What he actually showed is that
the **span of absolute judgment and the span of immediate memory are both limited to about seven categories**, and that
the limit is on **chunks**, not on raw information. The number is not a design constraint on menus; it is a description
of a bottleneck.

The bottleneck matters because working memory is where the user holds *the current task*: the value they just read, the
choice they made two screens ago, the reason they are on this page. When that store overflows, the user does not
experience "too many items" — they experience **losing the thread**, and the recovery cost is a re-read of everything.

Two corrections that every designer should carry:

1. **The modern estimate is closer to 4** (Cowan, 2001), not 7. Seven was an upper bound measured under favourable
   conditions; four is what holds under normal cognitive load.
2. **A chunk is whatever the user treats as one thing.** "2026-10-29" is one chunk to someone who reads dates daily and
   three to someone who does not. Chunking (see `03-chunking.md`) is how you raise density without raising count.

## Numbers that matter

| Quantity | Value | Consequence for the interface |
|---|---|---|
| Miller (1956) | 7 ± 2 chunks | Historical ceiling — not a target to fill |
| Cowan (2001) | **~4 chunks** | The number to design against |
| Duration without rehearsal | ~20–30 s | Anything off-screen must be re-derivable |
| Items per visual group | 3–5 | Keeps a group inside one chunk-slot budget |
| Digits in a formatted number | 3–4 per group | The reason phone numbers are dashed |

## Apply it

### Do

- **Design for four, not seven.** Four items per group is safe under load; seven is only safe when the user is rested,
  focused, and familiar.
- **Offload memory onto the screen.** Show the selected plan, the cart total, the entered email. The interface should
  never require the user to remember what it already knows.
- **Chunk long content** into named groups with headings. The heading is the "close this group" instruction.
- **Reduce simultaneous decisions** — one question per screen where the question is hard.
- **Let users review before committing.** A summary screen converts working-memory load into recognition, which is
  nearly free.
- **Persist state across steps** so a back button does not require reconstruction.

### Don't

- Don't use 7 as a quota ("we can fit one more"). It is a ceiling measured under ideal conditions.
- Don't put the instructions on one screen and the fields on another. That is a memory tax with no benefit.
- Don't require the user to compare values they can no longer see. Put them side by side.
- Don't split a single decision across two screens with a back button; that converts load into re-work.
- Don't confuse *visual* density with *cognitive* density. A dense table can be low-load if it is scannable.

## Pattern

```html
<!-- Offload memory: the summary carries what the user would otherwise hold -->
<section class="review" aria-labelledby="review-title">
  <h2 id="review-title">Review your order</h2>
  <dl class="review__list">
    <div><dt>Plan</dt><dd>Pro — $24/mo</dd></div>
    <div><dt>Seats</dt><dd>5</dd></div>
    <div><dt>Billing</dt><dd>Yearly — $19/mo</dd></div>
    <div><dt>Total today</dt><dd>$228</dd></div>
  </dl>
  <a href="/checkout/payment" class="link">Edit payment</a>
</section>
```

```css
.review__list { display: grid; gap: var(--space-3); margin: 0; }
.review__list > div { display: flex; justify-content: space-between; gap: var(--space-4); }
.review__list dt { color: var(--text-secondary); }
.review__list dd { margin: 0; font-weight: 600; }
```

```html
<!-- Four per group, named — the heading is the chunk boundary -->
<fieldset>
  <legend>Notification preferences</legend>
  <label><input type="checkbox" checked> Product updates</label>
  <label><input type="checkbox" checked> Security alerts</label>
  <label><input type="checkbox"> Weekly digest</label>
  <label><input type="checkbox"> Partner offers</label>
</fieldset>
```

## Audit question

> At the hardest step of the flow, how many separate things must the user hold in mind at once? If more than four, put
> something back on the screen.

## Further reading

| Reading | Author / Publisher |
|---|---|
| [Miller’s Law, Chunking, and the Capacity of Working Memory](https://www.khanacademy.org/test-prep/mcat/social-sciences-practice/social-science-practice-tut/e/miller-s-law--chunking--and-the-capacity-of-working-memory) | Khan Academy |
| [Design Principles for Reducing Cognitive Load](https://blog.prototypr.io/design-principles-for-reducing-cognitive-load-84e82ca61abd) | Jon Yablonski \| Medium.com |
| [The Magical Mystery Four: How is Working Memory Capacity Limited, and Why?](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2864034/) | Nelson Cowan \| NCBI |
| [Miller’s Law on Wikipedia](https://en.wikipedia.org/wiki/Miller%27s_law) | Wikipedia |
| [The Magical Number Seven, Plus or Minus Two: Some Limits on Our Capacity for Processing Information](http://www2.psych.utoronto.ca/users/peterson/psy430s2001/Miller%20GA%20Magical%20Seven%20Psych%20Review%201955.pdf) | George A. Miller |

---

**Site page** · [lawsofux.com/millers-law](https://lawsofux.com/millers-law/)
