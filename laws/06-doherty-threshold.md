---
law: Doherty Threshold
slug: doherty-threshold
index: 6
category: performance
lever: latency and feedback
audit_weight: critical
source: https://www.nngroup.com/articles/response-times-3-important-limits/
---

# 06 · Doherty Threshold

> Productivity soars when a computer and its users interact at a pace (<400ms) that ensures that neither has to wait on the other.

**Category** Performance · **Lever** Latency and feedback · **Audit weight** Critical

## What the site says

### Takeaways

1. Provide system feedback within 400 ms in order to keep users’ attention and increase productivity.
2. Use perceived performance to improve response time and reduce the perception of waiting.
3. Animation is one way to visually engage people while loading or processing is happening in the background.
4. Progress bars help make wait times tolerable, regardless of their accuracy.
5. Purposefully adding a delay to a process can actually increase its perceived value and instill a sense of trust, even when the process itself actually takes much less time.

### Origins

In 1982 Walter J. Doherty and Ahrvind J. Thadani published, in the IBM Systems Journal, a research paper that set the requirement for computer response time to be 400 milliseconds, not 2,000 (2 seconds) which had been the previous standard. When a human being’s command was executed and returned an answer in under 400 milliseconds, it was deemed to exceed the Doherty threshold, and use of such applications were deemed to be “addicting” to users.

## Mechanism — why this happens

Attention is a shared resource between the user and the machine. When the system responds inside the window where the
user is still holding the task in mind, the two work as one loop and the user stays in flow. When the response arrives
after that window, the user's attention drifts to something else, and the cost is not the wait itself — it is the
**re-entry**: re-reading the screen, re-establishing where they were, re-deciding.

That is why 400 ms is not an arbitrary performance budget. It is the point past which the loop breaks and the user
starts doing unpaid context-switching work.

Nielsen's three limits give the full picture and should be read together with this law:

| Limit | What the user perceives | What you must do |
|---|---|---|
| **0.1 s** | Instant — "the system did it" | No feedback needed beyond the state change |
| **1 s** | Noticeable but uninterrupted — flow preserved | Feedback can be subtle; do not block the UI |
| **10 s** | Attention limit — user will switch tasks | Show progress, allow cancel, never a blank screen |

The design rule: **every interaction under 400 ms should feel like a direct manipulation; every interaction over 1 s
needs a visible promise that something is happening; nothing should exceed 10 s without a progress indicator and an
escape hatch.**

## Numbers that matter

| Quantity | Value | Consequence for the interface |
|---|---|---|
| Doherty threshold | **<400 ms** | Target for every direct interaction |
| Previous standard | 2,000 ms | What the 1982 paper replaced |
| Instant threshold | 0.1 s | No spinner — a spinner here makes it feel *slower* |
| Flow threshold | 1 s | Above this, show state, keep the UI responsive |
| Attention limit | 10 s | Above this, progress + cancel are mandatory |
| Perceived speed trick | skeleton screens | Perceived load drops versus a blank spinner |

## Apply it

### Do

- **Respond optimistically.** Update the UI immediately, reconcile with the server after. A like button that fills
  instantly and rolls back on failure feels faster than an honest 600 ms round-trip.
- **Use skeletons shaped like the content** instead of a centered spinner. The shape primes layout and hides the wait.
- **Disable-and-label on submit** ("Saving…") so the user cannot double-submit and knows the click landed.
- **Stream long results.** First paragraph in 300 ms beats a complete page in 4 s.
- **Prefetch on intent.** Hover or focus on a link is a 200–400 ms head start you can spend on the next screen.
- **Move work off the critical path.** Optimistic writes, background sync, local cache.
- **Keep the 0.1 s tier clean.** Hover, focus, toggle, and tab switches must not animate for 300 ms; that reads as lag.

### Don't

- Don't show a spinner for a 120 ms operation — it converts "instant" into "loading".
- Don't block the whole page for one slow widget. Isolate the slow part.
- Don't use a fake progress bar that jumps to 90% and stalls; users notice, and it reads as dishonesty.
- Don't let a slow request freeze input. If the user can type during the wait, the wait is nearly free.
- Don't optimise the average and ignore the tail. The 95th percentile is what users remember (see `23-peak-end-rule.md`).

## Pattern

```js
// Optimistic update: the UI answers in <16ms, the network catches up later
async function toggleLike(btn, id) {
  const liked = btn.getAttribute("aria-pressed") === "true";
  btn.setAttribute("aria-pressed", String(!liked));   // immediate
  try {
    await fetch(`/api/like/${id}`, { method: liked ? "DELETE" : "POST" });
  } catch {
    btn.setAttribute("aria-pressed", String(liked));   // rollback on failure
    announce("Could not save. Try again.");
  }
}
```

```css
/* Skeleton shaped like the real content, not a generic spinner */
.skeleton {
  background: linear-gradient(90deg, var(--surface-raised) 25%, var(--surface-sunken) 37%, var(--surface-raised) 63%);
  background-size: 400% 100%;
  animation: shimmer 1.2s ease-in-out infinite;
  border-radius: var(--radius-sm);
}
@keyframes shimmer { from { background-position: 100% 0 } to { background-position: 0 0 } }
@media (prefers-reduced-motion: reduce) { .skeleton { animation: none } }
```

## Audit question

> Walk the primary task with the network throttled. Is there any moment where the user waits more than 400 ms with no
> visible change, or more than 1 s with no explanation?

## Further reading

| Reading | Author / Publisher |
|---|---|
| [The Economic Value of Rapid Response Time](https://jlelliotton.blogspot.ca/p/the-economic-value-of-rapid-response.html) | Jim Elliott |
| [This 70s UX gem still applies today](https://medium.com/@Gugel/the-doherty-threshold-5471ca990de6) | Michael Gugel \| Medium |
| [The Economic Value of Rapid Response Time](https://daverupert.com/2015/06/doherty-threshold/) | Dave Rupert |
| [The importance of percent-done progress indicators for computer-human interfaces](https://www.researchgate.net/publication/234791131_The_importance_of_percent-done_progress_indicators_for_computer-human_interfaces) | Brad A. Myers |
| [Response time in man-computer conversational transactions](http://yusufarslan.net/sites/yusufarslan.net/files/upload/content/Miller1968.pdf) | Robert B. Miller |

---

**Site page** · [lawsofux.com/doherty-threshold](https://lawsofux.com/doherty-threshold/)
