---
law: Goal-Gradient Effect
slug: goal-gradient-effect
index: 9
category: motivation
lever: visible progress
audit_weight: medium
source: http://home.uchicago.edu/ourminsky/Goal-Gradient_Illusionary_Goal_Progress.pdf
---

# 09 · Goal-Gradient Effect

> The tendency to approach a goal increases with proximity to the goal.

**Category** Motivation · **Lever** Visible progress · **Audit weight** Medium

## What the site says

### Takeaways

1. The closer users are to completing a task, the faster they work towards reaching it.
2. Providing artificial progress towards a goal will help to ensure users are more likely to have the motivation to complete that task.
3. Provide a clear indication of progress in order to motivate users to complete tasks.

### Origins

The goal-gradient hypothesis, originally proposed by the behaviorist Clark Hull in 1932, states that the tendency to approach a goal increases with proximity to the goal. In a classic experiment that tests this hypothesis, Hull (1934) found that rats in a straight alley ran progressively faster as they proceeded from the starting box to the food. Although the goal-gradient hypothesis has been investigated exten-sively with animals (e.g., Anderson 1933; Brown 1948; for a review, see Heilizer 1977), its implications for human behavior and decision making are understudied. Further-more, this issue has important theoretical and practical implications for intertemporal consumer behavior in reward programs (hereinafter RPs) and other types of motivational systems (e.g., Deighton 2000; Hsee, Yu, and Zhang 2003; Kivetz 2003; Lal and Bell 2003).

*Primary source cited on the site: [home.uchicago.edu](http://home.uchicago.edu/ourminsky/Goal-Gradient_Illusionary_Goal_Progress.pdf)*

## Mechanism — why this happens

Effort is not constant across a task; it **accelerates as the goal gets closer**. Hull proposed this in 1932 as a
behavioural gradient, and Kivetz, Urminsky & Zheng revived it in 2006 with field data from a real reward programme.
Two findings matter for design:

1. **Purchase acceleration.** The time between purchases shrinks as the reward approaches. The user is not more
   motivated at the start — they are more motivated near the end.
2. **Illusionary progress.** A card with a head start — 12 stamps where 2 are already filled, so 10 remain — is
   completed more often than a 10-stamp card where 10 remain. The *effort required is identical*. What differs is the
   **perceived position**, and perceived position drives effort.

The second finding is the design lever, and it is subtle: what matters is not how much is left, but **how far along the
user believes they are**. A progress indicator that starts at zero throws away free motivation.

## Numbers that matter

| Quantity | Value | Consequence for the interface |
|---|---|---|
| Original hypothesis | Hull, 1932 | The gradient is old and well replicated |
| Field evidence | Kivetz, Urminsky & Zheng, 2006 | Real purchase data, not lab ratings |
| Head-start condition | 12-stamp card, 2 pre-filled | Same 10 purchases required as the 10-stamp card |
| Effect direction | pre-filled card completed **more often** | Perceived progress beats actual progress |
| Inter-purchase interval | decreases toward the reward | The last 20% moves fastest |

## Apply it

### Do

- **Show progress, always.** "Step 3 of 5", "2 of 4 connected", a filled bar. Invisible progress is unmotivated progress.
- **Give a head start where it is honest.** Pre-fill the first step from data you already have (imported contacts,
  detected location, suggested name). The user starts at 20%, not 0%.
- **Show remaining work in the unit the user cares about** ("2 more to unlock free shipping") rather than a percentage.
- **Make the last stretch visible and close.** A bar at 80% is a stronger motivator than the same bar at 10%.
- **Put the reward at the end of the visible path.** Show the unlocked state as a target, greyed but present.
- **Use milestones** for long tasks so there are several "near-goal" moments, not one distant one.

### Don't

- Don't fake progress. A bar that jumps to 90% and stalls destroys trust in every future bar.
- Don't pre-fill progress the user did not earn in a way that misrepresents the offer (see `04-cognitive-bias.md`).
- Don't show progress that never advances (a static "1 of 3" for a week).
- Don't use a percentage when the unit is countable — "3 of 5" is more motivating than "60%".
- Don't reset progress on a trivial error. Losing a nearly-complete bar is the strongest churn trigger in onboarding.

## Pattern

```html
<!-- Progress with a head start and a countable remainder -->
<div class="progress" role="progressbar" aria-valuenow="3" aria-valuemin="1" aria-valuemax="5"
     aria-valuetext="Step 3 of 5: payment">
  <div class="progress__bar" style="--p: 60%"></div>
</div>
<p class="progress__label">Step 3 of 5 — 2 more to finish</p>
```

```css
.progress { block-size: 8px; background: var(--surface-sunken); border-radius: 999px; overflow: hidden; }
.progress__bar {
  block-size: 100%;
  inline-size: var(--p);
  background: var(--accent);
  transition: inline-size .3s ease;
}
@media (prefers-reduced-motion: reduce) { .progress__bar { transition: none } }
```

```html
<!-- Head start: the first step is already done because you know the data -->
<ol class="steps">
  <li class="steps__item is-done">Account created</li>
  <li class="steps__item is-current">Add your first project</li>
  <li class="steps__item">Invite a teammate</li>
</ol>
```

## Audit question

> Does the user always know how far along they are and how much is left, in countable units? At the start of the flow,
> is any progress already credited from data you have?

## Further reading

| Reading | Author / Publisher |
|---|---|
| [How Uber uses psychology to perfect their customer experience](https://medium.com/choice-hacking/how-uber-uses-psychology-to-perfect-their-customer-experience-d6c440285029) | Jennifer Clinehens \| Choice Hacking |
| [Moving the Finish Line: The Goal Gradient Hypothesis](https://fs.blog/2016/10/goal-gradient-hypothesis/) | Farnam Street |
| [Designing for motivation with the goal-gradient effect](https://uxdesign.cc/designing-for-motivation-with-the-goal-gradient-effect-c873cdf58beb) | Ian Batterbee \| UX Collective |
| [The Goal-Gradient Hypothesis Resurrected: Purchase Acceleration, Illusionary Goal Progress, and Customer Retention](http://home.uchicago.edu/ourminsky/Goal-Gradient_Illusionary_Goal_Progress.pdf) | Ran Kivetz, Oleg Urminsky, Yuhuang Zheng \| uchicago.edu |
| [The importance of percent-done progress indicators for computer-human interfaces](https://www.researchgate.net/publication/234791131_The_importance_of_percent-done_progress_indicators_for_computer-human_interfaces) | Brad A. Myers \| Carnegie Mellon University |

---

**Site page** · [lawsofux.com/goal-gradient-effect](https://lawsofux.com/goal-gradient-effect/)
