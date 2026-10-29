# Law Index
### Two lookup tables: symptom → law, and law → prescription

Use the first table when you have a problem. Use the second when you have a law and need its number.

**Reading the § column.** `01`–`04` refer to `references/01`–`references/04` (thematic synthesis). The **Detail** column
in Part 2 links to `laws/NN-<slug>.md`, which holds the full treatment of that single law — site takeaways and origin
text, mechanism, numbers, Do/Don't, code, audit question, and its Further Reading list.

---

## Part 1 — Symptom → law

| What the user says | What it usually is | Laws | Thematic § (`references/`) |
|---|---|---|---|
| "It looks messy / unprofessional" | flat spacing, no separation hierarchy | Proximity, Common Region | 01 §1.1–1.2 · 05 §2 |
| "It's cramped" | no difference between gap levels, not lack of padding | Proximity | 01 §1.1 · 05 §2.2 |
| "I don't know where to look" | no focal point / too many emphases | Von Restorff, Selective Attention | 02 §2.7, §2.9 |
| "Nothing stands out" | everything equally weighted | Von Restorff, Prägnanz | 02 §2.9 · 01 §1.5 |
| "It's overwhelming" | too many decisions or chunks per view | Hick, Choice Overload, Miller, Chunking | 02 §2.1–2.6 |
| "The form is too long" | ungrouped fields, no staging, no autofill | Hick, Chunking, Parkinson, Cognitive Load | 02 §2.5–2.6 · 03 §3.5 |
| "I got lost in the flow" | memory tax, no progress, no context | Working Memory, Goal-Gradient, Zeigarnik | 02 §2.4 · 03 §3.2–3.3 |
| "It's slow" | latency without feedback | Doherty | 04 §4.4 |
| "It feels sluggish even though it's fast" | perceived performance, wrong feedback type | Doherty, Parkinson | 04 §4.4 · 03 §3.5 |
| "I can't tap the right thing" | small targets, no separation, wrong zone | Fitts | 04 §4.5 |
| "It feels unfamiliar / confusing" | broken convention | Jakob, Mental Model | 04 §4.1–4.2 |
| "I don't understand what happened" | invisible state, no feedback, no model | Mental Model, Doherty, Postel | 04 §4.2, §4.4, §4.6 |
| "It looks like every other site" | Prägnanz without a signature | Von Restorff, Aesthetic-Usability | SKILL §10 · 02 §2.9 |
| "It's pretty but useless" | aesthetics masking structural failure | Aesthetic-Usability, Occam | 03 §3.7 · 04 §4.7 |
| "There's too much on the page" | decoration and redundancy | Cognitive Load, Occam, Prägnanz | 02 §2.5 · 04 §4.7 · 01 §1.5 |
| "The text is hard to read" | measure, contrast, line-height, size | (05 §3, §4) + Von Restorff | 05 §3–4 |
| "The error messages are useless" | no cause/fix, wrong location, cleared input | Postel, Cognitive Load, Peak-End | 04 §4.6 · 02 §2.5 · 03 §3.4 |
| "The ending feels abrupt" | no designed ending | Peak-End, Goal-Gradient | 03 §3.2, §3.4 |
| "Users abandon onboarding" | manual-first, no early win, too much setup | Paradox of the Active User, Flow, Parkinson | 03 §3.1, §3.5, §3.6 |
| "Users don't find the feature" | salience inverted, feature below the fold, no signifier | Selective Attention, Serial Position, Zeigarnik | 02 §2.7–2.8 · 03 §3.3 |
| "Users keep making the same mistake" | false similarity, ambiguous affordance, no guardrail | Similarity, Prägnanz, Postel | 01 §1.4–1.5 · 04 §4.6 |
| "Everything looks equally important" | no ranking, card fog | Von Restorff, Common Region, Occam | 02 §2.9 · 01 §1.2 · 04 §4.7 |
| "It doesn't feel trustworthy" | inconsistency, no defaults, no state visibility | Similarity, Cognitive Bias, Mental Model | 01 §1.4 · 04 §4.8, §4.2 |
| "Too many options at checkout" | choice overload without a default | Choice Overload, Hick | 02 §2.1–2.2 |

---

## Part 2 — Law → prescription

### Perception & layout (`01`)

| Law | Detail | Use it when | Key number |
|---|---|---|---|
| **Proximity** | [13](../laws/13-law-of-proximity.md) | deciding any gap | inside : outside ≥ 1 : 2 |
| **Common Region** | [12](../laws/12-law-of-common-region.md) | a group must survive distance/scrolling | padding ≥ gap between siblings |
| **Uniform Connectedness** | [16](../laws/16-law-of-uniform-connectedness.md) | sequence, hierarchy, attribution | 1 connector system per view |
| **Similarity** | [15](../laws/15-law-of-similarity.md) | defining component semantics | 3 sizes · 3 weights · 1 accent |
| **Prägnanz** | [14](../laws/14-law-of-pragnanz.md) | reducing visual noise | 0 decorative elements competing with content |

### Attention & memory (`02`)

| Law | Detail | Use it when | Key number |
|---|---|---|---|
| **Hick** | [10](../laws/10-hicks-law.md) | menus, toolbars, option sets | ≤7 choices; RT = a + b·log₂(n) |
| **Choice Overload** | [02](../laws/02-choice-overload.md) | catalogues, pricing, filters | 3–5 comparable options; 3 preconditions |
| **Miller** | [18](../laws/18-millers-law.md) | anything requiring recall | 7±2 items, **~4 chunks** (Cowan) |
| **Working Memory** | [29](../laws/29-working-memory.md) | multi-step flows, comparisons | 4–7 chunks, 20–30 s decay |
| **Cognitive Load** | [05](../laws/05-cognitive-load.md) | any complex task | 1 source per decision |
| **Chunking** | [03](../laws/03-chunking.md) | long forms, dense content | 3–5 per group |
| **Selective Attention** | [25](../laws/25-selective-attention.md) | salience, state changes | 1 primary, ≤3 secondary |
| **Serial Position** | [26](../laws/26-serial-position-effect.md) | ordering, nav, CTA placement | first + last carry the weight |
| **Von Restorff** | [28](../laws/28-von-restorff-effect.md) | emphasis, primary action | exactly 1 per view |

### Motivation & journey (`03`)

| Law | Detail | Use it when | Key number |
|---|---|---|---|
| **Flow** | [08](../laws/08-flow.md) | difficulty curve, focus | first win < 2 min |
| **Goal-Gradient** | [09](../laws/09-goal-gradient-effect.md) | progress, completion | bar + remaining steps visible |
| **Zeigarnik** | [30](../laws/30-zeigarnik-effect.md) | resume, discoverability | ≤2 open loops |
| **Peak-End** | [23](../laws/23-peak-end-rule.md) | endings, error recovery | 1–2 designed peaks |
| **Parkinson** | [22](../laws/22-parkinsons-law.md) | form length, perceived duration | beat the promised time |
| **Paradox of the Active User** | [20](../laws/20-paradox-of-the-active-user.md) | onboarding, empty states, help | first action < 10 s |
| **Aesthetic-Usability** | [01](../laws/01-aesthetic-usability-effect.md) | polish investment | first impression ~50 ms |
| **Pareto** | [21](../laws/21-pareto-principle.md) | effort allocation | 20% of screens |

### System & interaction (`04`)

| Law | Detail | Use it when | Key number |
|---|---|---|---|
| **Jakob** | [11](../laws/11-jakobs-law.md) | navigation, forms, any convention | ≤1 novel pattern |
| **Mental Model** | [17](../laws/17-mental-model.md) | naming, structure, state visibility | ≤3 core concepts |
| **Tesler** | [27](../laws/27-teslers-law.md) | settings, defaults, complexity | system absorbs it |
| **Doherty** | [06](../laws/06-doherty-threshold.md) | latency, feedback | **<400 ms** |
| **Fitts** | [07](../laws/07-fittss-law.md) | target size and placement | **44×44 px**, 8 px gap |
| **Postel** | [24](../laws/24-postels-law.md) | input handling, validation | liberal format, strict meaning |
| **Occam** | [19](../laws/19-occams-razor.md) | element count | minimum that preserves the task |
| **Cognitive Bias** | [04](../laws/04-cognitive-bias.md) | defaults, pricing, consent | 0 exploitative defaults |

---

## Part 3 — Numbers worth memorising

```
400 ms      Doherty threshold — feedback or the user notices
100 ms      direct manipulation
1 s         flow preserved
10 s        attention limit — progress bar + interrupt
44 × 44 px  minimum touch target
8 px        minimum gap between targets
7 ± 2       Miller's original span (do not use as a quota)
4           Cowan's revised working-memory focus
3–5         items per chunk / fields per group
65ch        measure
1.5         body line-height
4.5 : 1     body contrast
3 : 1       large text and UI boundaries
1 : 2       minimum inside : outside spacing ratio
1           focal point per view
```

---

## Part 4 — Sources

All 30 entries and their primary references originate from [lawsofux.com](https://lawsofux.com/) by Jon Yablonski
(*Laws of UX*, O'Reilly, 2020). The deeper material in each reference file is drawn from the sources those entries link
to, plus the standards they imply:

- **Nielsen Norman Group** — aesthetic-usability effect (Moran, 2024); response time limits (Nielsen, 1993)
- **Interaction Design Foundation** — Fitts's law; Hick's law; serial position effect; chunking
- **Smashing Magazine** — Gestalt principles of visual perception (Bradley, 2014)
- **Wikipedia** — overchoice; cognitive bias; cognitive load; working memory; flow; peak–end rule; von Restorff effect;
  principles of grouping; Occam's razor; Parkinson's law; robustness principle; law of conservation of complexity
- **Primary research** — Miller (1956); Cowan (2001); Hick (1952); Hyman (1953); Fitts (1954); Sweller (1988);
  Chandler & Sweller (1992); Kalyuga et al. (2003); Baddeley & Hitch (1974); Glanzer & Cunitz (1966); Glenberg et al.
  (1980); von Restorff (1933); Zeigarnik (1927); Csíkszentmihályi (1975); Massimini et al. (1987); Kahneman et al.
  (1993); Redelmeier & Kahneman (1996); Kivetz, Urminsky & Zheng (2006); Kurosu & Kashimura (1995); Tversky &
  Kahneman (1974); Hull (1932); Rosson & Carroll (1987); Postel, RFC 761 (1980); Thomson & Schinazi, RFC 9413 (2023)
- **Standards** — WCAG 2.2 (contrast 1.4.3/1.4.11, text spacing 1.4.12, target size 2.5.8); ISO 9241-9 (Fitts);
  Apple HIG (44 pt); Material Design (48 dp)

Two caveats that the sources themselves insist on, and that this skill repeats deliberately:

1. **Miller's 7 is not a design quota.** lawsofux.com lists "don't use the magical number seven to justify unnecessary
   design limitations" as its first takeaway.
2. **Choice overload is conditional**, not universal — it needs no prior preference, no dominant option, and low
   familiarity (Scheibehenne et al., 2010).
