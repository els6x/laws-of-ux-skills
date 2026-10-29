# 03 — Motivation & Journey
### Eight laws about effort, momentum, endings, and first impressions

Files 01–02 make a screen *readable*. This file makes it *completable*. These laws govern the shape of a task over
time: how hard it feels, whether the user keeps going, what they remember afterwards, and what they do in the first
five seconds when nobody has explained anything.

Two of these laws (Goal-Gradient, Zeigarnik) are the most commonly weaponised in dark patterns. Read §9 of `SKILL.md`
before applying them.

---

## 3.1 Flow

> The mental state in which a person is fully immersed in an activity — energized focus, full involvement, enjoyment.

### Mechanism
Csíkszentmihályi (1975) described flow as the "optimal experience": complete absorption, merging of action and
awareness, loss of self-consciousness, a sense of control, altered time perception, and intrinsic reward. The
antecedents are specific and designable:

1. **Clear goals** — the user knows what "done" looks like at every moment.
2. **Immediate feedback** — every action produces a visible consequence.
3. **Challenge–skill balance** — perceived difficulty matches perceived ability, with confidence of success.

The **eight-channel model** (Massimini, Csíkszentmihályi & Carli, 1987) maps experience against perceived challenge
and perceived skill: **flow** sits where both are above average; **anxiety** where challenge exceeds skill;
**boredom** where skill exceeds challenge; **apathy** where both are low.

Design consequence: a task that is too hard produces abandonment, a task that is too easy produces disengagement —
and *both* feel like "the product is bad". Flow is a difficulty curve, not a feature.

### Numbers
| Decision | Value |
|---|---|
| First meaningful success | within the first session, ideally <2 minutes |
| Feedback latency per action | <400 ms (see Doherty, 4.4) |
| Difficulty step between levels | one increment the user can perceive but not struggle with |
| Interruptions during a focused task | 0 (no modals, no chat popups, no toasts that require dismissal) |
| Progress visibility during a multi-step task | always |

### Do
- **State the goal at the start of every task.** A one-line "you'll set up your workspace in 3 steps" converts
  uncertainty into a challenge.
- **Give the first win early.** Pre-fill, demo data, a template, a sample project — anything that produces a real
  result before the user has invested.
- **Match difficulty to skill, visibly.** Beginner mode with fewer options; expert mode with density and shortcuts.
  Let the user choose, and let them move up.
- **Remove friction, not features.** Flow's own takeaway: optimise for efficiency and responsiveness; make features
  *discoverable* rather than forcing them.
- **Protect the focus window.** Suppress non-critical interruptions while a task is in progress.

### Don't
- Don't front-load a tutorial for a task the user could simply start. Flow requires starting.
- Don't make the first step the hardest one (usually: account creation before value).
- Don't add gamification without a real skill curve — points on a flat task produce boredom, not flow.

### Audit question
> At each step: does the user know the goal, see the result of their last action, and believe they can do the next one?

### Source
[lawsofux.com/flow](https://lawsofux.com/flow/) · [Flow, Wikipedia](https://en.wikipedia.org/wiki/Flow_(psychology)) ·
Csíkszentmihályi (1975); Massimini et al. (1987); Nakamura & Csíkszentmihályi.

---

## 3.2 Goal-Gradient Effect

> The tendency to approach a goal increases with proximity to the goal.

### Mechanism
Clark Hull (1932) observed that rats ran faster as they neared the food. The human version was demonstrated in loyalty
programs by Kivetz, Urminsky & Zheng (2006): customers bought coffee more frequently as they approached a free-drink
reward, and — the famous finding — a **12-stamp card with 2 stamps already given** (10 purchases required) produced
higher completion than a plain **10-stamp card**, despite identical effort. That is *endowed progress*: the feeling of
having started accelerates behaviour.

The mechanism is motivational, not rational: effort is a function of perceived distance remaining, not total distance.

### Numbers
| Decision | Value |
|---|---|
| Progress indicator | required for any task >1 step |
| Endowed progress | start the bar at 10–30% when there is a legitimate starting state |
| Milestones | every 20–25% of a long process |
| Remaining-effort display | show *remaining*, not just *completed* ("2 steps left" beats "3 of 5 done" for urgency) |
| Reward visibility | always — the goal must be on screen |

### Do
- **Show a progress bar with a defined end.** A bar with no endpoint is decoration.
- **Make the last mile feel short**: name the remaining steps, pre-fill the final step, offer a one-click finish.
- **Use endowed progress honestly** — if the account already exists, or the first step is genuinely complete, show it
  as complete. Do not invent progress.
- **Put the reward where it can be seen** during the task (the free item, the unlocked feature, the certificate).
- **Accelerate at the end**: reduce required input, auto-advance, remember choices.

### Don't
- **Don't fake progress.** Pre-ticked steps, artificial "1 of 2" on a 5-step flow, and progress that resets are dark
  patterns and destroy trust the moment they are noticed.
- Don't show a bar that jumps backwards. Progress must be monotonic within a session.
- Don't use goal-gradient to stretch a task (Parkinson's Law cuts the other way — see 3.5).

### Audit question
> Where is the goal on screen, and how far away does it feel? If the user can't answer "how much is left", add the bar.

### Source
[lawsofux.com/goal-gradient-effect](https://lawsofux.com/goal-gradient-effect/) · Hull (1932, 1934) · Kivetz, Urminsky
& Zheng (2006), *The Goal-Gradient Hypothesis Resurrected*, *Journal of Marketing Research*.

---

## 3.3 Zeigarnik Effect

> People remember uncompleted or interrupted tasks better than completed tasks.

### Mechanism
Bluma Zeigarnik (1920s, Berlin School) found that interrupted tasks are recalled more readily than finished ones —
an unfinished task stays active in memory and creates a mild tension that motivates return. The design uses are
legitimate (resume where you left off, signifiers of more content) and illegitimate (manufactured incompleteness).

The law's own takeaways point at the honest version: *provide clear signifiers of additional content* and *provide a
clear indication of progress*.

### Numbers
| Decision | Value |
|---|---|
| Resume affordance | on every return visit, for any flow >2 steps |
| "More content" signifier | visible partial next item (peek), not a hidden count |
| Open loops per view | 1–2 (a checklist, a draft, a next step) |
| Completion state | must be reachable and clearly marked |

### Do
- **Persist drafts and show them.** "Continue where you left off" is the highest-value use of this law.
- **Leave a visible edge of the next thing** — a partially visible card, a "3 more lessons", a next-step preview.
- **Use checklists for multi-part setup**, with completed items visibly struck through.
- **Close loops you open.** If you show a task list, let every item reach a done state.

### Don't
- Don't manufacture incompleteness: fake "almost done" states, un-dismissable badges, streak counters that punish rest.
- Don't leave the user in an unresolvable open loop (a notification with no action, a checklist that can never be completed).
- Don't stack open loops — three unfinished flows is anxiety, not motivation.

### Audit question
> What open loop is this screen creating, and can the user close it from here?

### Source
[lawsofux.com/zeigarnik-effect](https://lawsofux.com/zeigarnik-effect/) · Zeigarnik (1927) · Lewin's tension systems.

---

## 3.4 Peak-End Rule

> People judge an experience largely by how they felt at its peak and at its end, not the sum or average of every moment.

### Mechanism
Kahneman, Fredrickson, Schreiber & Redelmeier (1993) had participants submerge a hand in **14 °C** water for **60
seconds**, and the other hand for **60 seconds at 14 °C plus 30 seconds at 15 °C** — objectively longer and more
unpleasant. Asked which trial to repeat, participants preferred the **longer** one. They remembered the ending, not
the duration.

Two mechanisms: **duration neglect** (length barely affects retrospective evaluation) and **snapshot memory** (the
remembered value is roughly the average of the most intense moment and the end). Related finding from the same
literature: **negative peaks are weighted more heavily than positive ones** — one bad moment costs more than one good
moment earns.

Later replications: colonoscopy patients rated the procedure by peak and end pain; adding three minutes of *less*
painful ending improved both ratings and return rates.

### Numbers
| Decision | Value |
|---|---|
| Peak moments per journey | 1–2, deliberately designed |
| Endings | always designed — success screen, confirmation, summary, next step |
| Error recovery | treat as a peak: it will be remembered disproportionately |
| Post-task summary | required for any flow >3 steps |
| Waiting at the end | eliminate — an unresolved spinner is a negative peak |

### Do
- **Design the ending.** A confirmation that states what happened, what to expect, and what to do next. Not a bare
  "Success."
- **Put the delight at a real moment of value** — first result, first publish, first share — not on a loading screen.
- **Make error states feel resolved.** A clear cause, a clear fix, and a preserved state turns the worst peak into a
  neutral one.
- **Compress the last 10%.** The final step should be the fastest.
- **Add a summary** (receipt, recap, "you just did X") — it converts the end into a positive anchor.

### Don't
- Don't end on a spinner, an empty state, or a dead end ("we'll email you").
- Don't put the only delightful moment before the value is delivered.
- Don't use confetti to cover a failure. Users remember the failure and the insult.

### Audit question
> Walk the journey and mark the highest and lowest emotional points, and the last screen.
> Are those three moments designed, or did they happen by accident?

### Source
[lawsofux.com/peak-end-rule](https://lawsofux.com/peak-end-rule/) ·
[Peak–end rule, Wikipedia](https://en.wikipedia.org/wiki/Peak%E2%80%93end_rule) · Kahneman et al. (1993);
Redelmeier & Kahneman (1996); Redelmeier, Katz & Kahneman (2003).

---

## 3.5 Parkinson's Law

> Any task will inflate until all of the available time is spent.

### Mechanism
C. Northcote Parkinson's 1955 *Economist* essay observed that work expands to fill the time available, and that
administrative headcount grows regardless of workload (British Admiralty ships falling, staff rising; the Colonial
Office peaking in staff exactly as it was absorbed). For interfaces the useful reading is narrower and practical:
**if a task has no time signal, the user will spend whatever attention is available on it — and the task will feel as
long as it takes.**

The design translation is not "rush the user". It is: **set an expectation, then beat it.** A task that takes less time
than expected feels good; the same task that takes longer than expected feels broken, even at identical duration.

### Numbers
| Decision | Value |
|---|---|
| Time estimate shown before a multi-step task | yes, in human units ("about 2 minutes") |
| Fields the system can fill | all of them (autofill, saved data, defaults) |
| Checkout / signup steps | ≤3 before value |
| Perceived wait | always shorter than actual: skeleton or optimistic UI |
| Task time vs. expectation | deliver under, never over |

### Do
- **Set the expectation explicitly**, then finish early. "3 steps, about a minute" changes the experience of the same flow.
- **Autofill everything you already know** — address, card, company, previous answers. Every field the system could
  fill but doesn't is a tax the user pays for the system's convenience.
- **Default the common case.** Pre-selected shipping, remembered preferences, sensible units.
- **Cut steps, not just fields.** Merging two screens beats shrinking both.

### Don't
- Don't pad a process to seem thorough. Artificial delays to "build trust" are a lie with a progress bar.
- Don't show an estimate you can't beat.
- Don't make the user re-enter information the system already has.

### Audit question
> What did we promise this task would take, and what does it actually take? Where is the gap coming from?

### Source
[lawsofux.com/parkinsons-law](https://lawsofux.com/parkinsons-law/) ·
[Parkinson's law, Wikipedia](https://en.wikipedia.org/wiki/Parkinson%27s_law) · Parkinson, *The Economist*, 19 Nov 1955.

---

## 3.6 Paradox of the Active User

> Users never read manuals but start using the software immediately.

### Mechanism
Rosson & Carroll (1987) found that new users skip documentation and begin acting, even at the cost of errors and
dead ends. The paradox: reading first would save time overall, but users optimise for the immediate task. They are
not lazy — they are **goal-directed under time pressure**, and they assume the interface will teach them.

Design consequence: **guidance must live inside the task**, at the moment of need, in the shape of the thing being done.
Documentation is a fallback, not a strategy.

### Numbers
| Decision | Value |
|---|---|
| Time to first action without instruction | <10 seconds |
| Onboarding screens before first use | 0–1 |
| Guidance placement | in-context, at the point of need |
| Tooltip length | ≤1 sentence |
| Empty state | must teach the first action |

### Do
- **Design the empty state as the tutorial.** The first screen a new user sees should contain the action, not a description of it.
- **Put help where the confusion is** — inline hints, example values, a sample row, a "what's this?" next to the field.
- **Make the safe path the default path.** If a mistake is recoverable, users will learn by doing. Undo beats a warning.
- **Progressive onboarding** (Slack's model): hide everything except the one feature being learned, then reveal.
- **Keep docs one click away** from the exact context, not in a separate help centre.

### Don't
- Don't gate the product behind a multi-screen tour. Users will skip it and then blame the product.
- Don't write help text that describes the UI ("this field is for your name") — say what to do and why.
- Don't rely on a manual for a recoverable action. Make it undoable instead.

### Audit question
> If the user ignores every piece of instruction on this screen, can they still succeed?

### Source
[lawsofux.com/paradox-of-the-active-user](https://lawsofux.com/paradox-of-the-active-user/) · Rosson & Carroll (1987),
*Interfacing Thought*.

---

## 3.7 Aesthetic-Usability Effect

> Users often perceive aesthetically pleasing design as design that's more usable.

### Mechanism
Kurosu & Kashimura (1995, Hitachi Design Center) tested **26 variations** of an ATM interface with **252 participants**,
rating each on ease of use and aesthetic appeal. The correlation between *aesthetics* and *perceived* ease of use was
stronger than between aesthetics and *actual* ease of use. People judge the book by the cover, even when told to judge
the contents.

Two limits matter more than the effect itself:

- **It only buys tolerance for minor problems.** When a task genuinely fails, aesthetics stop helping — NN/g's example:
  a participant loved a site's full-bleed photography until he couldn't find what he needed, then called it "annoying".
- **It contaminates usability testing.** Participants rate attractive interfaces highly while failing tasks. Watch what
  they *do*, not what they *say*.

Related and worth knowing: visual appeal is judged extremely fast — Lindgaard et al. (2006) found judgements of
attractiveness formed at **50 ms** exposure correlated with judgements at longer exposure. The first impression is
pre-verbal and it sets the frame for everything after.

### Numbers
| Decision | Value |
|---|---|
| First-impression budget | ~50 ms — the layout must read at a glance |
| Polish effort vs. structural effort | structure first, always |
| Visual consistency (radius, shadow, spacing) | one system, no exceptions |
| Typography | the highest-leverage aesthetic investment |
| Aesthetic "tricks" replacing usability fixes | 0 |

### Do
- **Invest in typography, spacing, and alignment before illustration.** Those three carry most of the perceived quality.
- **Make the system consistent** — same radius, same shadow language, same spacing scale. Inconsistency reads as
  carelessness even when each element is fine.
- **Use aesthetics to buy patience for the *learning* phase**, not for broken flows. First-run, empty states, and
  waiting moments are where polish pays.
- **Watch behaviour in tests.** If a participant praises the visuals after failing a task, you have found the effect,
  not a success.

### Don't
- Don't ship a beautiful interface with a broken core task and call it "delightful". The effect expires at the first
  real failure.
- Don't use aesthetics to skip accessibility. Contrast, focus, and target size are not aesthetic choices.
- Don't let visual polish delay structural fixes — it hides problems from the team as well as from users.

### Audit question
> If I removed all styling, would the task still work? If not, aesthetics are covering a structural failure.

### Source
[lawsofux.com/aesthetic-usability-effect](https://lawsofux.com/aesthetic-usability-effect/) ·
[NN/g, *The Aesthetic-Usability Effect*](https://www.nngroup.com/articles/aesthetic-usability-effect/), Kate Moran,
2024 · Kurosu & Kashimura (1995), CHI '95 · Norman, *Emotional Design* (2004) · Lindgaard et al. (2006).

---

## 3.8 Pareto Principle

> Roughly 80% of the effects come from 20% of the causes.

### Mechanism
Vilfredo Pareto observed that 80% of Italy's land was owned by 20% of the population. The ratio is not a law of nature;
it is a **diagnostic habit**: in most systems, inputs and outputs are lopsided, and a small subset carries most of the
value. For interface work this is an effort-allocation rule, not a feature-cutting rule.

### Numbers
| Decision | Value |
|---|---|
| Screens/flows that carry the core task | typically 20% — find them first |
| Design effort distribution | majority on that 20% |
| Long-tail screens | consistent, conventional, cheap |
| Features used by most users | usually a small minority of the feature set |

### Do
- **Find the 20% before designing.** Which three screens does the user touch every day? Those get the craft; the rest
  gets the system.
- **Apply the system to the long tail.** Templates, tokens, and components make the 80% cheap and consistent.
- **Cut features that serve nobody** and invest the saved effort in the flows that serve everybody.
- **Measure before assuming.** The 20% is empirical — analytics, support tickets, session recordings — not intuition.

### Don't
- Don't treat 80/20 as a precise law. It is a prompt to check for lopsidedness, not a quota.
- Don't neglect the long tail into inconsistency. Cheap is fine; broken is not.
- Don't use it to justify ignoring accessibility or edge cases — those are small in count and large in consequence.

### Audit question
> Which 20% of these screens carry 80% of the user's task? Is that where the design effort actually went?

### Source
[lawsofux.com/pareto-principle](https://lawsofux.com/pareto-principle/) · Pareto (1906) · IBM Design, *The 80/20 Rule
in User Experience*.

---

## Synthesis — the journey curve

Design the journey as a curve, not a set of screens.

```
START     → reduce time-to-first-action to <10 s           (Paradox of the Active User)
          → deliver one real success early                  (Flow)
MIDDLE    → show progress, keep the goal visible            (Goal-Gradient)
          → protect focus, one open loop at a time          (Flow, Zeigarnik)
          → make difficulty climb in visible steps          (Flow)
END       → compress the last step                          (Parkinson)
          → design the ending explicitly                    (Peak-End)
          → surface what was accomplished                   (Peak-End, Goal-Gradient)
ALWAYS    → beat the time you promised                      (Parkinson)
          → let aesthetics carry the learning phase only    (Aesthetic-Usability)
```

**The memory test.** Ask a user one day later: "what was it like?" If they describe the middle of the flow, the
journey has no peak. If they describe the last screen, the ending is doing its job. If they describe an error, that
error is your product's memory — fix the error before adding delight.
