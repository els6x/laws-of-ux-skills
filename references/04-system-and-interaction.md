# 04 — System & Interaction
### Eight laws about convention, targets, latency, complexity, and judgement

Files 01–03 are about a screen. This file is about the *system* behind it: what the user already expects, how far their
finger has to travel, how long they will wait, who carries the complexity, and which of their judgement errors you are
designing with or against.

---

## 4.1 Jakob's Law

> Users spend most of their time on other sites. This means that users prefer your site to work the same way as all the
> other sites they already know.

### Mechanism
Jakob Nielsen's observation is really a statement about **transfer**: users arrive with a mental model built from every
other product they use, and they apply it without checking. Familiar patterns cost nothing to learn; novel patterns cost
attention that the user wanted to spend on their task. This is why "creative" navigation is expensive and why
"boring" forms convert.

The law does not say *never innovate*. It says the burden of proof is on the deviation: you must be meaningfully better,
not merely different.

### Numbers
| Decision | Value |
|---|---|
| Novel interaction patterns per product | ≤1, and only where it creates real advantage |
| Convention coverage of core flows | logo → home, cart top-right, avatar menu top-right, search top, back = previous |
| Redesign migration | keep the old version reachable for a transition period |
| Icon-only controls without labels | 0 for anything not universally understood (search, close, menu) |

### Do
- **Follow the conventions that carry meaning**: form layout, navigation position, checkout sequence, error placement,
  focus behaviour, keyboard shortcuts.
- **Match platform, not brand.** iOS back-swipe, Android back button, desktop hover states, mobile tap states.
- **Migrate gently.** YouTube's 2017 redesign let users preview the new UI, give feedback, and revert. Do that.
- **Spend your novelty budget on one thing** — the thing users came for — and be conventional everywhere else.

### Don't
- Don't redesign a convention to look original. Users will pay for it in errors, and you will pay for it in support.
- Don't assume your users are new to the category. They have used six competitors before you.
- Don't break a convention without a visible affordance explaining the new one.

### Audit question
> For each core interaction: where else has the user done this before, and does ours behave the same way?

### Source
[lawsofux.com/jakobs-law](https://lawsofux.com/jakobs-law/) · Jakob Nielsen, NN/g · *Mental model* (4.2).

---

## 4.2 Mental Model

> A compressed model based on what we think we know about a system and how it works.

### Mechanism
Kenneth Craik (1943, *The Nature of Explanation*) proposed that people carry a small-scale model of how the world works,
used to anticipate events and form explanations. Donald Norman later split this into the **design model** (what the
designer intended), the **system image** (what the product actually shows), and the **user's model** (what they believe).
Every usability problem is a gap between those three.

Mental models are *compressed and lossy*. Users do not hold your data structure; they hold a story about it. If the
story is wrong, the interface will be used wrongly — confidently.

### Numbers
| Decision | Value |
|---|---|
| Concepts the user must learn to use the product | ≤3 |
| Names for the same concept across the UI | 1 (never "workspace / project / board" for one thing) |
| Visible state changes per action | must be explainable in one sentence |
| Research inputs before a structural redesign | ≥5 user interviews or equivalent |

### Do
- **Name things the way users name them**, not the way the database names them.
- **Make the system's state visible.** Users cannot build a model of something they cannot see: show what is saved,
  what is syncing, what is shared, what is deleted.
- **Be consistent about cause and effect.** One action → one visible result, every time.
- **Research the model before changing it.** Interviews, support tickets, search queries, and observed sessions reveal
  the story users already believe.
- **Use the model as the navigation structure.** If users think in projects, navigate by projects — even if the data is
  stored as tasks.

### Don't
- Don't expose implementation concepts (IDs, sync states, retries) as primary UI vocabulary.
- Don't rename established concepts for branding. "Spaces" instead of "folders" costs every user a translation.
- Don't change the model silently. If the underlying behaviour changes, the interface must show it.

### Audit question
> Ask a user to explain how this feature works. Where does their explanation diverge from the actual behaviour?
> That divergence is the design work.

### Source
[lawsofux.com/mental-model](https://lawsofux.com/mental-model/) · Craik (1943) · Norman, *The Design of Everyday Things*.

---

## 4.3 Tesler's Law (Law of Conservation of Complexity)

> For any system there is a certain amount of complexity which cannot be reduced.

### Mechanism
Larry Tesler, at Xerox PARC in the mid-1980s, argued that interaction design matters as much as function, and that
complexity is conserved: it can be moved, but not deleted. Someone must absorb it — the engineer, the interface, or the
user.

His formulation of the trade-off:

> *"If a million users each waste a minute a day dealing with complexity that an engineer could have eliminated in a
> week by making the software a little more complex, you are penalizing the user to make the engineer's job easier."*

Bruce Tognazzini's counterpoint: people resist reductions in complexity — simplify an application and users attempt more
complex tasks, so the complexity reappears at a higher level. Both are right: **complexity is conserved, but its
location and its shape are design decisions.**

### Numbers
| Decision | Value |
|---|---|
| Complexity accepted by the system | as much as possible |
| Complexity exposed to the user | only where it changes their outcome |
| Settings exposed by default | the 20% that most users change; rest behind "advanced" |
| Defaults | must produce a good result with zero configuration |

### Do
- **Absorb complexity in code, not in the interface.** Sensible defaults, automatic formatting, validation, retries,
  state recovery.
- **Expose complexity only where it changes the result** (advanced filters, expert settings, raw mode) and label it as such.
- **Design for a real user, not an idealised rational one.** Tesler's own takeaway: people don't behave rationally.
- **Make the default excellent.** Most users will never change a setting; the default *is* the product.

### Don't
- Don't pass complexity to the user to keep the code simple. That trade is almost always a bad one at scale.
- Don't hide complexity so completely that power users cannot reach it. Provide an escape hatch.
- Don't confuse "simple" with "few features". Simple is about the path, not the feature count.

### Audit question
> For each hard decision in this flow: who is carrying it — the system, or the user? Can the system carry more?

### Source
[lawsofux.com/teslers-law](https://lawsofux.com/teslers-law/) ·
[Law of conservation of complexity, Wikipedia](https://en.wikipedia.org/wiki/Law_of_conservation_of_complexity) ·
Saffer, *Designing for Interaction* (2010) · Tognazzini, *The Complexity Paradox*.

---

## 4.4 Doherty Threshold

> Productivity soars when a computer and its users interact at a pace (<400 ms) that ensures neither has to wait on the other.

### Mechanism
Walter J. Doherty and Ahrvind J. Thadani (IBM Systems Journal, 1982) found that response times under **400 ms** produced
a step change in productivity and engagement — applications at that speed were described as "addicting". The previous
standard had been 2 seconds.

This aligns with Nielsen's three perceptual limits (1993), which are still the most useful numbers in interface performance:

| Limit | What it protects | What to do |
|---|---|---|
| **0.1 s** | feeling of direct manipulation | no feedback needed; just show the result |
| **1.0 s** | continuity of thought / flow | no special feedback needed, but the user notices; keep it under 1 s |
| **10 s** | attention on the task | show percent-done progress and a way to interrupt |

Below 0.1 s the interface feels like an object. Between 0.1 and 1 s it feels like a fast tool. Between 1 and 10 s it
feels like a request. Above 10 s the user leaves the task mentally, and you must give them a reason to come back.

### Numbers
| Decision | Value |
|---|---|
| Target response | **<400 ms** (Doherty) |
| Direct manipulation | <100 ms |
| Flow preserved | <1 s |
| Spinner threshold | >1 s |
| Skeleton | show immediately for content likely to exceed ~300 ms |
| Progress bar | >10 s, with an interrupt |
| Optimistic UI | allowed, but must reconcile and surface failure |

### Do
- **Make the common action instant.** Local state update first, network second.
- **Use skeletons, not spinners**, for content with a known shape — they reduce perceived duration and prevent layout shift.
- **Use optimistic UI** for reversible actions (like, follow, reorder, send) and reconcile in the background.
- **Make waits legible**: name what is happening ("uploading 3 of 12"), not just that something is.
- **Never block the whole screen for a local action.** Scope the loading state to the thing that is loading.

### Don't
- Don't show a spinner for a 120 ms operation — it makes the wait *feel* longer by drawing attention to it.
- Don't fake speed. An optimistic update that silently fails is worse than a spinner.
- Don't put a progress bar on an operation you cannot measure; use indeterminate feedback instead.
- Don't animate the transition longer than the wait itself.

### Audit question
> Time every interaction. Which ones exceed 400 ms, and what does the user see during the gap?

### Source
[lawsofux.com/doherty-threshold](https://lawsofux.com/doherty-threshold/) · Doherty & Thadani (1982), *IBM Systems
Journal* · [NN/g, *Response Times: The 3 Important Limits*](https://www.nngroup.com/articles/response-times-3-important-limits/),
Nielsen, 1993.

---

## 4.5 Fitts's Law

> The time to acquire a target is a function of the distance to and size of the target.

### Mechanism
Paul Fitts (1954) showed that movement time depends on distance and inversely on target width, with a speed–accuracy
trade-off: fast movements and small targets produce more errors. The common formulation:

```
T = a + b · log₂(2D / W)        D = distance, W = target width
```

(Shannon form, used in ISO 9241-9: `ID = log₂(D/W + 1)`, measured in bits.) Two practical corollaries that the formula
hides:

- **Height matters as much as width.** A 500 px wide, 2 px tall target is still hard to hit.
- **Edges and corners are infinite targets.** The cursor cannot go past the screen edge, so a corner has effectively
  unbounded width. This is why menu bars, dock edges, and corner buttons are fast.

### Numbers
| Decision | Value |
|---|---|
| Touch target (minimum) | **44 × 44 CSS px** (Apple HIG 44 pt, Material 48 dp) |
| WCAG 2.2 SC 2.5.8 floor | 24 × 24 CSS px, or 24 px spacing |
| Gap between adjacent targets | ≥8 px |
| Primary CTA height | 40–48 px (desktop), 48–56 px (mobile) |
| Thumb-zone placement (mobile) | primary actions in the bottom third |
| Distance, trigger → result | 0 — the result appears where the action was |
| Icon-only button hit area | ≥44 px even if the glyph is 20 px |

### Do
- **Size by consequence.** Destructive or frequent actions get the largest targets; rare, safe actions can be smaller.
- **Place primary actions where the hand already is** (mobile: bottom; desktop: near the working area, not the far corner).
- **Keep related controls adjacent.** Distance is a cost, and moving the mouse across a 1440 px screen is a real cost.
- **Make the whole row/card clickable** when the row is the target, rather than a small link inside it.
- **Use edge and corner positions** for persistent, high-frequency controls.

### Don't
- Don't put a small "×" next to a large "Save" — mis-taps on destructive controls are a Fitts problem, not a user problem.
- Don't rely on hover-only affordances on touch devices.
- Don't spread a single task's controls across the screen (label far from field, error far from input).
- Don't shrink targets to fit more in. Add a second row, an overflow menu, or a scroll — never smaller targets.

### Audit question
> Measure the smallest tappable thing on the screen. Is it ≥44 px, ≥8 px from its neighbour, and reachable one-handed?

### Source
[lawsofux.com/fittss-law](https://lawsofux.com/fittss-law/) · IxDF, *Fitts's Law* · Fitts (1954) · ISO 9241-9 ·
WCAG 2.2 SC 2.5.8.

---

## 4.6 Postel's Law (Robustness Principle)

> Be liberal in what you accept, and conservative in what you send.

### Mechanism
Jon Postel wrote the principle into the IPv4 and TCP specifications (1979/1980): send only conformant output, but accept
non-conformant input as long as the meaning is clear. For interfaces this becomes: **tolerate human input, be strict
about what you emit.**

The modern caveat is important. Thomson & Schinazi (RFC 9413, 2023) argue that unbounded leniency creates its own
fragility: a tolerated deviation becomes a de facto standard, and every implementation must then replicate the bug.
Applied to UI: be liberal about **format**, strict about **meaning** — especially for destructive or ambiguous actions.

### Numbers
| Decision | Value |
|---|---|
| Input formats accepted per field (phone, date, currency) | ≥3 common variants |
| Silent corrections | only when unambiguous and reversible |
| Destructive/ambiguous input accepted silently | 0 |
| Validation timing | on blur, not on every keystroke |
| Error message specificity | names the field, the problem, and the fix |

### Do
- **Normalise, don't reject.** Accept `+62 812-3456-7890`, `0812 3456 7890`, `081234567890`; store one canonical form.
- **Trim, collapse whitespace, accept pasted formatting** (currency symbols, thousands separators, trailing spaces).
- **Preserve user input on failure.** Never clear a form because one field was invalid.
- **Validate late, forgive early.** Let the user type, then check.
- **Be strict on output**: consistent date formats, canonical URLs, one number format, one casing convention.

### Don't
- Don't silently guess destructive intent (delete vs. archive, send vs. save draft).
- Don't accept invalid input and fail later with a generic error. The failure belongs at the field.
- Don't be so lenient that typos become data (`gmial.com` should be *suggested*, not silently accepted).
- Don't use leniency as an excuse to skip validation on the server.

### Audit question
> Paste something real into every field — a formatted phone number, a currency with a symbol, a date written the way a
> human writes it. Does the interface accept it, or punish the user for formatting?

### Source
[lawsofux.com/postels-law](https://lawsofux.com/postels-law/) ·
[Robustness principle, Wikipedia](https://en.wikipedia.org/wiki/Robustness_principle) · RFC 761 (1980) · RFC 1122 (1989) ·
RFC 9413 (2023).

---

## 4.7 Occam's Razor

> Among competing hypotheses that predict equally well, the one with the fewest assumptions should be selected.

### Mechanism
William of Ockham's principle (*Numquam ponenda est pluralitas sine necessitate* — "plurality must never be posited
without necessity") is a heuristic for choosing between explanations of equal power. In design it becomes: **among
solutions that work equally well, choose the one with the fewest elements.**

Two cautions from the philosophical literature, both directly applicable:

- It is **not** a licence to oversimplify. Einstein's formulation: *"as simple as possible, but not simpler."*
- It applies **only between options that already work**. Removing an element that carried meaning is not parsimony,
  it is loss.

### Numbers
| Decision | Value |
|---|---|
| Elements per screen | minimum that preserves the task |
| Clicks to complete the primary task | the fewest that keep the user oriented |
| Visual treatments per element | 1 (a border OR a shadow OR a fill) |
| Concepts introduced per screen | ≤1 new idea |

### Do
- **Remove, then check.** Delete an element; if the task is unaffected, it was decoration.
- **Prefer the solution that needs no explanation.** If it needs a tooltip to be understood, it is too complex.
- **Collapse redundant states.** Two ways to do the same thing is one too many — unless one is a shortcut for experts.
- **Simplify the path, not the meaning.** Fewer steps is good; fewer *options that matter* is not.

### Don't
- Don't remove the label to look minimal. Unlabelled icons are not simpler; they are ambiguous.
- Don't hide essential controls behind a "more" menu to reduce visual count. That moves cost from vision to memory.
- Don't mistake emptiness for simplicity. Whitespace is not the same as fewer decisions.

### Audit question
> Name every element on this screen and what it does. Which ones cannot answer in one sentence? Remove those.

### Source
[lawsofux.com/occams-razor](https://lawsofux.com/occams-razor/) ·
[Occam's razor, Wikipedia](https://en.wikipedia.org/wiki/Occam%27s_razor) · William of Ockham (c. 1287–1347).

---

## 4.8 Cognitive Bias

> A systematic error of thinking or rationality in judgement that influences perception and decision-making.

### Mechanism
Tversky & Kahneman (1972; *Judgment under Uncertainty*, 1974) showed that people use heuristics — representativeness,
availability, anchoring — which are fast and usually good, but produce **predictable, systematic** errors. Because the
errors are systematic, they can be designed for. Because they are systematic, they can also be exploited. The line
between the two is §9 of `SKILL.md`.

The biases that matter most in interface work:

| Bias | What it does | Legitimate design use | Exploitative use (forbidden) |
|---|---|---|---|
| **Default effect / status quo** | People keep what is pre-selected | Sensible, privacy-preserving defaults | Pre-checked marketing consent |
| **Anchoring** | First number pulls later judgements | Show the reference price honestly | Fake "was" prices |
| **Framing** | Same fact, different response by wording | Frame positively without distortion ("90% success") | "95% fat free" on a bad product |
| **Loss aversion** | Losses weigh ~2× gains | Warn before destructive actions | Fake urgency, expiring carts |
| **Confirmation bias** | Seek confirming information | Show disconfirming evidence in comparisons | Filter bubbles, one-sided reviews |
| **Availability** | Vivid examples feel frequent | Use realistic examples and testimonials | Manufactured scary statistics |
| **Sunk cost** | Past investment drives continuation | Save progress, show accumulated value | "You'll lose your 40% discount" |
| **Halo effect** | One good attribute colours the rest | Consistent quality across the product | Pretty UI on a broken product |
| **Social proof** | Others' behaviour guides choice | Real, relevant usage data | Invented "12 people are viewing" |

### Numbers
| Decision | Value |
|---|---|
| Defaults that benefit the business at the user's expense | 0 |
| Pricing tiers shown | 3 (anchoring works; decoys are manipulation) |
| Consent pre-ticked | never |
| Countdown timers on non-scarce things | 0 |
| Reviews shown | representative sample, including negative |

### Do
- **Design defaults as if the user will never change them** — because most won't. Make the default the one you would
  recommend to a friend.
- **Anchor honestly.** Show the real comparison (market price, previous price, competitor range) — anchoring is
  legitimate when the anchor is true.
- **Frame both ways where the decision is consequential**: "90% survive" and "10% die" are both true; show both.
- **Make the reversible choice easy** and the irreversible choice explicit.

### Don't
- Don't use cognitive bias as a growth lever. Every dark pattern is a bias with a revenue model attached.
- Don't assume bias makes users stupid. It makes them *fast*, and fast is usually correct. Design for the fast path.
- Don't confuse a bias with a preference. If users choose the cheap plan, that may be a preference, not anchoring.

### Audit question
> For every default, pre-selection, and piece of urgency copy: if the user understood exactly why it is there, would
> they still choose it?

### Source
[lawsofux.com/cognitive-bias](https://lawsofux.com/cognitive-bias/) ·
[Cognitive bias, Wikipedia](https://en.wikipedia.org/wiki/Cognitive_bias) · Tversky & Kahneman (1972, 1974) ·
Thaler & Sunstein, *Nudge*.

---

## Synthesis — the system layer

```
CONVENTION   follow it everywhere except the one thing you are actually innovating   (Jakob)
MODEL        use the user's vocabulary, show the system's state                      (Mental Model)
COMPLEXITY   the system absorbs it; the user sees only what changes the outcome      (Tesler, Occam)
TIME         <400 ms, or tell the truth about the wait                               (Doherty)
TARGETS      44 px, 8 px apart, where the hand already is                            (Fitts)
INPUT        liberal on format, strict on meaning                                    (Postel)
JUDGEMENT    design for heuristics, never against the user                           (Cognitive Bias)
```

**The interaction floor.** A screen passes this layer when a user who has never seen it can: find the primary action in
under 3 seconds, hit it first try on a phone, see a response within 400 ms, recover from a wrong input without losing
their work, and explain what happened afterwards in one sentence. Everything above that is craft.
