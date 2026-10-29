---
law: Selective Attention
slug: selective-attention
index: 25
category: attention
lever: salience
audit_weight: critical
source: https://en.wikipedia.org/wiki/Attention
---

# 25 · Selective Attention

> The process of focusing our attention only to a subset of stimuli in an environment — usually those related to our goals.

**Category** Attention · **Lever** Salience · **Audit weight** Critical

## What the site says

### Takeaways

1. People often filter out information that isn’t relevant. This happens in order to maintain focus on information that is important or relevant to the task at hand. Designers must guide users’ attention, prevent them from being overwhelmed or distracted, and help them find relevant information or action.
2. Banner Blindness is an example phenomenon of selection attention where visitors to a website consciously or unconsciously ignore banner-like information. Users have learned to ignore content that resembles ads, is close to ads, or appears in locations traditionally dedicated to ads. Avoid confusion by not styling content to look like ads or placing content and ads in the same visual section.
3. Change blindness is another example phenomenon of selection attention that occurs when significant changes in an interface go unnoticed because due to the limitations of human attention and the lack of strong cues. Avoid this by analyzing your design for any competing changes that may happen at the same time and that may divert attention from each other.

### Origins

Selective Attention Theory originated in the mid-20th century as researchers sought to understand how humans process information from their environment. The theory developed through several key contributions:Donald Broadbent’s Filter Theory (1958): Broadbent proposed the first comprehensive model of selective attention, known as the Filter Theory. He suggested that there is an attentional “bottleneck” that allows only limited information to be processed at a time. According to this model, information is initially filtered based on physical characteristics before semantic processing occurs.Cherry’s Cocktail Party Effect (1953): E. Colin Cherry conducted seminal work on the “cocktail party phenomenon,” using dichotic listening tasks to study how people selectively attend to one auditory stream while ignoring others.Anne Treisman’s Attenuation Model (1960): Treisman refined Broadbent’s theory, proposing that unattended information is not completely blocked but rather attenuated. This allowed for the explanation of how some unattended information could still be processed.Deutsch and Deutsch’s Late Selection Theory (1963): This theory proposed that all sensory information is fully processed for meaning before selection occurs, contrasting with Broadbent’s early selection model.The development of these theories was driven by both practical concerns and theoretical interests. For instance, Mackworth’s research on vigilance in 1950 was motivated by concerns about radar operators’ performance during World War II. Throughout the 1950s to 1970s, research on attention shifted from primarily auditory tasks to visual tasks. This period also saw the emergence of capacity theories, such as Kahneman’s (1973) model, which viewed attention as a limited resource that could be divided among different tasks. These early theories and experiments laid the foundation for our current understanding of selective attention and continue to influence research in cognitive psychology and neuroscience today.

*Primary source cited on the site: [simplypsychology.org](https://www.simplypsychology.org/attention-models.html)*

## Mechanism — why this happens

Attention is a filter, not a spotlight. At any moment the visual system receives far more information than it can
process, so it selects a subset based on goals, expectations, and low-level salience (contrast, motion, color, size).
Everything else is not merely ignored — it is often **not perceived at all**.

The classic demonstrations:

- **The cocktail party effect** (Cherry, 1953): people can follow one conversation in a noisy room and can report almost
  nothing about the others, though they still notice their own name.
- **Inattentional blindness** (Simons & Chabris, 1999): a person counting basketball passes fails to see a person in a
  gorilla suit walk through the scene.
- **Banner blindness** (Nielsen, 2007): users' eyes skip anything that looks like an advertisement, regardless of
  whether it is one.

The design consequence is a hard constraint: **you cannot make something seen by making it important. You make it seen
by making it different from its surroundings, in a channel the user is already monitoring.**

And the corollary, which is where most interfaces fail: **everything that competes for attention reduces the attention
available for the thing that matters.** A page with five equally loud elements has no focal point, and the user's filter
resolves the ambiguity by ignoring all five.

## Numbers that matter

| Quantity | Value | Consequence for the interface |
|---|---|---|
| Focal points per screen | **1** | Two means the user chooses at random |
| Competing accent colors | 1 | Each additional accent divides attention |
| Banner-like elements noticed | very low | Banner blindness is real; do not put critical info in one |
| Motion in peripheral vision | captures attention involuntarily | Use sparingly; it overrides everything else |
| Time to notice a change | 200–500 ms with motion | Animation is the strongest attention cue you have |

## Apply it

### Do

- **Establish one focal point per screen** and make everything else clearly subordinate. Size, weight, and contrast are
  the hierarchy; use them in that order.
- **Make the important thing different, not louder.** A single accent color on one action beats five colored buttons.
- **Respect banner blindness.** Do not put critical information in anything shaped like an ad, and do not expect users
  to read promotional strips.
- **Use motion only for meaning** — a state change, a transition, a newly arrived item. Decorative motion steals
  attention permanently.
- **Place information where the eye already goes**: top-left for scanning, near the action for decisions, in the field
  for validation.
- **Reduce competition.** Remove secondary links, badges, and promos from the primary task screen.

### Don't

- Don't rely on a red banner to convey an error the user must act on. Put the error next to the field.
- Don't use five accent colors to mean five things; use one accent and a second channel (icon, label, position).
- Don't animate backgrounds, carousels, or decorative gradients near text.
- Don't assume a prominent element is a noticed element. Test with eye-tracking or a 5-second recall test.
- Don't compete with your own primary action. A second equally-weighted button splits attention and slows every visit.

## Pattern

```html
<!-- One focal point: the primary action is the only accent on the screen -->
<section class="hero">
  <h1 class="hero__title">Ship your first project today</h1>
  <p class="hero__lead">Everything you need to plan, build, and share — in one workspace.</p>
  <a class="btn btn--primary" href="/signup">Start free</a>
</section>
```

```css
.hero { display: grid; gap: var(--space-4); max-inline-size: 60ch; }
.hero__title { font-size: clamp(2rem, 5vw, 3rem); line-height: 1.15; color: var(--text-primary); }
.hero__lead  { font-size: var(--text-lg); color: var(--text-secondary); }
/* Only .btn--primary uses the accent. Nothing else on this screen does. */
```

```css
/* Motion reserved for state, and disabled for users who ask */
.toast { animation: slide-in .18s ease-out; }
@keyframes slide-in { from { opacity: 0; transform: translateY(4px) } to { opacity: 1; transform: none } }
@media (prefers-reduced-motion: reduce) { .toast { animation: none } }
```

```html
<!-- Error where the eye already is: at the field, not in a banner -->
<div class="field">
  <label for="email">Email</label>
  <input id="email" aria-invalid="true" aria-describedby="email-err">
  <p id="email-err" class="field__error" role="alert">Enter a complete address, like name@company.com.</p>
</div>
```

## Audit question

> Squint at the screen until the text is illegible. What is the one thing that stands out? If the answer is not the
> primary action, the salience is pointed at the wrong element.

## Further reading

| Reading | Author / Publisher |
|---|---|
| [Change Blindness in UX: Definition](https://www.nngroup.com/articles/change-blindness-definition/) | Raluca Budiu \| Nielsen Norman Group |
| [Banner Blindness Revisited: Users Dodge Ads on Mobile and Desktop](https://www.nngroup.com/articles/banner-blindness-old-and-new-findings/) | Kara Pernice \| Nielsen Norman Group |
| [How We Use Selective Attention to Filter Information and Focus](https://www.verywellmind.com/what-is-selective-attention-2795022) | Kendra Cherry, MSEd \| VerywellMind |
| [Tunnel Vision and Selective Attention](https://www.nngroup.com/articles/tunnel-vision-and-selective-attention/) | Jakob Nielsen \| Nielsen Norman Group |

---

**Site page** · [lawsofux.com/selective-attention](https://lawsofux.com/selective-attention/)
