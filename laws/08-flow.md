---
law: Flow
slug: flow
index: 8
category: motivation
lever: challenge–skill balance
audit_weight: medium
source: https://en.wikipedia.org/wiki/Flow_(psychology)
---

# 08 · Flow

> The mental state in which a person performing some activity is fully immersed in a feeling of energized focus, full involvement, and enjoyment in the process of the activity.

**Category** Motivation · **Lever** Challenge–skill balance · **Audit weight** Medium

## What the site says

### Takeaways

1. Flow occurs when there is a balance between the difficulty of a task with the level of skill at the given task. It’s characterized by intense and focused concentration on the present, combined with a sense of total control.
2. A task that’s too difficult leads to heighten frustration while a task that’s too easy can lead to boredom. Finding the right balance requires matching the challenge with skill of the user.
3. Design for flow by providing the necessary feedback so that the user know what action has been done and what has been accomplished.
4. Optimize for efficiency and system responsiveness by removing any unnecessary friction, and making content and features available for discovery to avoid disengagement with the interface.

### Origins

Flow was coined by psychologist Mihály Csíkszentmihályi in 1975 and has been widely referred to across a variety of fields (and is particularly well recognized in occupational therapy), though the concept has been claimed to have existed for thousands of years under other names.

*Primary source cited on the site: [en.wikipedia.org](https://en.wikipedia.org/wiki/Flow_%28psychology%29)*

## Mechanism — why this happens

Flow is the state where attention is fully invested, self-consciousness drops, and time distorts. Csikszentmihalyi
identified the conditions that produce it, and every one of them is something an interface can either supply or destroy:

| Condition | What it means in software | What breaks it |
|---|---|---|
| Clear goals at each moment | The user always knows what "done" looks like next | Vague labels, multi-purpose screens |
| Immediate feedback | Every action visibly lands | Silent saves, unexplained delays |
| Challenge ≈ skill | Difficulty tracks the user's ability | Onboarding that is too hard *or* too easy |
| Sense of control | The user can undo, cancel, go back | Destructive actions with no recovery |
| Concentration on the task | No interruptions, no competing chrome | Modals, banners, notifications, upsells |
| Loss of self-consciousness | No fear of looking foolish | Error messages that blame the user |
| Time distortion | The task absorbs attention | Frequent context switches |
| Autotelic experience | The activity is worth doing for itself | Gamification that replaces the task with points |

The challenge–skill model is the actionable core. Plot challenge against skill and you get three regions:

```
        high │  ANXIETY        │        FLOW
   challenge │  (too hard)     │   (matched, stretching)
             ├─────────────────┼─────────────────
             │  APATHY         │        BOREDOM
        low  │  (neither)      │   (too easy)
             └─────────────────┴─────────────────
               low        skill        high
```

Both failure modes are design bugs. Anxiety shows up as abandonment and support tickets; boredom shows up as
"it's fine, I guess" and churn.

## Numbers that matter

| Quantity | Value | Consequence for the interface |
|---|---|---|
| Feedback latency for flow | <1 s (see `06-doherty-threshold.md`) | Beyond this, the loop breaks |
| Onboarding steps before first value | 1–3 | Longer, and the user is in the anxiety region |
| Interruptions during a primary task | **0** | Every modal is a flow reset |
| Difficulty ramp | +1 capability per session, roughly | Too steep → anxiety; flat → boredom |

## Apply it

### Do

- **Get to first value fast.** The first session should end with the user having *done* the thing, not watched a tour.
- **Match difficulty to experience.** Show the simple path first, then reveal power features (progressive disclosure).
  The expertise reversal effect is the same idea from cognitive load theory.
- **Give immediate, local feedback** on every action: inline validation, optimistic updates, visible state changes.
- **Protect the task.** No modals, no newsletter prompts, no cookie banners mid-flow, no chat bubble over the submit button.
- **Make undo the default safety net** instead of confirmation dialogs. Undo preserves flow; a confirm dialog interrupts it.
- **Show progress within a long task** so the user knows the goal is still there.
- **Let experts skip.** A "skip guide" link is a flow feature for the high-skill user.

### Don't

- Don't front-load tutorials. A 6-step modal tour before the first action is anxiety by design.
- Don't gamify the task itself. Points and badges that replace the real goal produce engagement with the *badge*.
- Don't interrupt with upsells during the primary flow. Move monetisation to natural boundaries.
- Don't punish errors. A red banner that says "Invalid input" resets flow and adds shame; an inline hint does not.
- Don't make the same screen serve beginners and experts without a mode switch.

## Pattern

```html
<!-- Flow-preserving validation: inline, immediate, non-blaming -->
<div class="field">
  <label for="email">Email</label>
  <input id="email" type="email" aria-describedby="email-err" aria-invalid="true">
  <p id="email-err" class="field__error">That address is missing an @. Try name@company.com.</p>
</div>
```

```css
.field__error { color: var(--danger); font-size: var(--text-sm); margin-block-start: var(--space-1); }
.field input[aria-invalid="true"] { border-color: var(--danger); }
```

```js
// Undo instead of confirm — keeps the user in the task
function deleteItem(id) {
  const snapshot = removeFromUI(id);
  toast("Deleted", { action: "Undo", onAction: () => restore(snapshot) });
}
```

## Audit question

> Walk the first-run experience. At which step does the user first *do* the thing the product is for? If it is after
> step three, the flow starts too late.

## Further reading

| Reading | Author / Publisher |
|---|---|
| [The 3 design principles for creating flow](https://blog.superhuman.com/how-to-design-for-flow/) | Rahul Vohra \| Superhuman |
| [Designing For Flow](https://alistapart.com/article/designingforflow/) | Jim Ramsey \| A List Apart |
| [7 Steps to Achieving Flow in UX Design](https://uxdesign.cc/7-steps-to-achieving-flow-in-ux-design-7ef28adb0de2) | Elaine Tran \| UX Collective |
| [Beyond Task Completion: Flow in Design](https://uxmag.com/articles/beyond-task-completion-flow-in-design) | Dana Chisnell \| UX Magazine |

---

**Site page** · [lawsofux.com/flow](https://lawsofux.com/flow/)
