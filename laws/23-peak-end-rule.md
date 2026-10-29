---
law: Peak-End Rule
slug: peak-end-rule
index: 23
category: memory
lever: endings and peaks
audit_weight: critical
source: https://en.wikipedia.org/wiki/Peak%E2%80%93end_rule
---

# 23 · Peak-End Rule

> People judge an experience largely based on how they felt at its peak and at its end, rather than the total sum or average of every moment of the experience.

**Category** Memory · **Lever** Endings and peaks · **Audit weight** Critical

## What the site says

### Takeaways

1. Pay close attention to the most intense points and the final moments (the “end”) of the user journey.
2. Identify the moments when your product is most helpful, valuable, or entertaining and design to delight the end user.
3. Remember that people recall negative experiences more vividly than positive ones.

### Origins

A 1993 study titled “When More Pain Is Preferred to Less: Adding a Better End” by Kahneman, Fredrickson, Charles Schreiber, and Donald Redelmeier provided groundbreaking evidence for the peak–end rule. Participants were subjected to two different versions of a single unpleasant experience. The first trial had subjects submerge a hand in 14°C water for 60 seconds. The second trial had subjects submerge the other hand in 14°C water for 60 seconds, but then keep their hand submerged for an additional 30 seconds, during which the temperature was raised to 15 °C. Subjects were then offered the option of which trial to repeat. Against the law of temporal monotonicity, subjects were more willing to repeat the second trial, despite a prolonged exposure to uncomfortable temperatures. Kahneman et al. concluded that “subjects chose the long trial simply because they liked the memory of it better than the alternative (or disliked it less)”.

*Primary source cited on the site: [en.wikipedia.org](https://en.wikipedia.org/wiki/Peak%E2%80%93end_rule)*

## Mechanism — why this happens

Memory of an experience is not an average of its moments. It is constructed from a few salient points — the most intense
moment (the **peak**) and the final moment (the **end**) — plus a rough sense of duration that barely registers at all.
This is **duration neglect**: a longer experience with the same peak and end is remembered as no worse than a shorter one.

Kahneman's cold-water studies are the canonical demonstration. Participants immersed a hand in 14 °C water for 60
seconds, and in a second condition for 60 seconds plus an additional 30 seconds during which the temperature was raised
very slightly (still unpleasant, but marginally less so). Objectively, the second trial was **longer and included all of
the first trial's discomfort**. Yet participants rated it as less unpleasant and were more willing to repeat it. The end
dominated the memory.

For interfaces, three implications follow:

1. **The last screen is disproportionately remembered.** A checkout that ends on a blank confirmation page undoes a
   good flow.
2. **One peak can carry the whole experience** — a delightful moment, a fast first result, a well-timed animation.
3. **A bad ending is expensive.** Errors at the end, a confusing success state, or an unexpected upsell after payment
   dominate the memory of everything before.

## Numbers that matter

| Quantity | Value | Consequence for the interface |
|---|---|---|
| Cold-water study | 14 °C, 60 s vs 60 s + 30 s | Longer but gentler ending rated better |
| Duration weight in memory | near zero | Optimising average speed is not the same as optimising memory |
| Peaks worth designing | 1–2 per journey | More than two dilutes; none means the flow is forgettable |
| End-screen attention | highest of the flow | The most-read screen you own |

## Apply it

### Do

- **Design the ending deliberately.** A confirmation that states what happened, what happens next, and what the user can
  do now. Never a blank page or a redirect to a dashboard.
- **Engineer one peak.** A fast first result, a satisfying completion animation, a genuinely useful summary. One is
  enough; it does not need to be loud.
- **Put the best moment late.** Users remember the end; a great first step and a dull finish produces a dull memory.
- **Handle late errors with extra care.** An error at the last step is the peak *and* the end — it will define the
  experience. Preserve input, explain the cause, offer a fix.
- **Make success states specific.** "Order #4821 confirmed — arriving Thursday" beats "Success!".
- **Close loops.** Show the completed state of what the user started (see `30-zeigarnik-effect.md`).

### Don't

- Don't end a flow with an upsell. You are attaching the peak to a sales pitch.
- Don't let the confirmation be a toast that disappears in 3 seconds. The end deserves a screen.
- Don't assume a fast flow is a good memory. A fast flow with a confusing ending is remembered as confusing.
- Don't put the only friction at the end (a surprise fee, a mandatory survey).
- Don't celebrate before the outcome is certain. Confetti on a pending payment is a false peak.

## Pattern

```html
<!-- The end screen: what happened, what's next, what now -->
<section class="done" aria-labelledby="done-title">
  <div class="done__mark" aria-hidden="true">✓</div>
  <h1 id="done-title">You're all set</h1>
  <p class="done__lead">Workspace <strong>Acme</strong> is ready. We sent an invite link to your team.</p>
  <dl class="done__facts">
    <div><dt>Plan</dt><dd>Pro — $24/mo</dd></div>
    <div><dt>Next invoice</dt><dd>Nov 29</dd></div>
  </dl>
  <div class="done__actions">
    <a class="btn btn--primary" href="/app">Open workspace</a>
    <a class="link" href="/invite">Invite more people</a>
  </div>
</section>
```

```css
.done { display: grid; gap: var(--space-4); justify-items: start; max-inline-size: 52ch; }
.done__mark { inline-size: 40px; block-size: 40px; display: grid; place-items: center;
              border-radius: 50%; background: color-mix(in srgb, var(--success) 16%, transparent);
              color: var(--success); font-weight: 700; }
.done__facts { display: grid; gap: var(--space-2); margin: 0; inline-size: 100%; }
.done__facts > div { display: flex; justify-content: space-between; gap: var(--space-4); }
.done__facts dd { margin: 0; font-weight: 600; }
.done__actions { display: flex; align-items: center; gap: var(--space-4); margin-block-start: var(--space-2); }
```

```html
<!-- A late error is both peak and end: treat it as the most important screen -->
<div class="pay-error" role="alert">
  <h2>Your card was declined</h2>
  <p>Your bank declined the charge. Your details are saved — nothing was lost.</p>
  <p class="pay-error__hint">Try another card, or contact your bank and mention code <code>do_not_honor</code>.</p>
  <button class="btn btn--primary">Try another card</button>
</div>
```

## Audit question

> Look at the last screen of the primary flow. Is it the best-designed screen in the product? If not, the memory of the
> whole flow is being decided by an afterthought.

## Further reading

| Reading | Author / Publisher |
|---|---|
| [Peak–End Rule](https://lawsofux.com/articles/2020/peak-end-rule/) | Jon Yablonski |
| [How Uber uses psychology to perfect their customer experience](https://medium.com/choice-hacking/how-uber-uses-psychology-to-perfect-their-customer-experience-d6c440285029) | Jennifer Clinehens \| Medium |
| [The Peak–End Rule: How Impressions Become Memories](https://www.nngroup.com/articles/peak-end-rule) | Lexie Kane \| Nielsen Norman Group |
| [What is Peak-End Theory? A Psychologist Explains How Our Memory Fools Us](https://positivepsychology.com/what-is-peak-end-theory/) | Positive Psychology |
| [How do our memories differ from our experiences?](https://thedecisionlab.com/biases/peak-end-rule/) | The Decision Lab |
| [Peak–End Rule](https://en.wikipedia.org/wiki/Peak%E2%80%93end_rule) | Wikipedia |
| [When More Pain Is Preferred to Less: Adding a Better End](https://www.jstor.org/stable/40062570) | Daniel Kahneman, Barbara L. Fredrickson, Charles A. Schreiber and Donald A. Redelmeier |
| [Evaluations of pleasurable experiences: The peak-end rule](https://link.springer.com/article/10.3758/PBR.15.1.96) | Amy M. Do, Alexander V. Rupert & George Wolford |

---

**Site page** · [lawsofux.com/peak-end-rule](https://lawsofux.com/peak-end-rule/)
