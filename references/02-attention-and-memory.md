# 02 — Attention & Memory
### Nine laws that govern how many decisions, how much memory, and where the eye goes

This is the working core of the skill. Perception (file 01) decides *what groups with what*. These nine decide
*how much* you may put in front of a person, *how long* they can hold it, and *what they will actually see*.

The three questions this file answers:

1. **How many?** → Hick, Choice Overload, Miller, Chunking
2. **How much can they hold?** → Working Memory, Cognitive Load
3. **Where will they look?** → Selective Attention, Serial Position, Von Restorff

---

## 2.1 Hick's Law

> The time it takes to make a decision increases with the number and complexity of choices.

### Mechanism
Hick & Hyman (1952) measured reaction time across sets of stimuli and found it grows with the **base-2 logarithm** of
the number of equally likely choices:

```
RT = a + b · log₂(n)
```

`a` is the cost of perceiving and responding at all; `b` is the per-bit decision cost. Because the relationship is
logarithmic, doubling options adds a *constant* increment rather than doubling time — but the increment never
disappears. Two consequences follow:

- **Reducing 12 options to 6 saves the same time as reducing 6 to 3.** Cuts get cheaper as the set shrinks, so cut early.
- **Familiarity and pre-formed decisions bypass the law.** If the user already knows what they want, or the options are
  strongly associated with a response, reaction time falls below the log prediction (Gross, *Redefining Hick's Law*,
  2012). This is why expert tools can be dense while onboarding cannot.

### Numbers
| Decision | Value |
|---|---|
| Top-level nav items | **≤7**, target 5 |
| Primary actions per screen | 1 |
| Visible actions per row/toolbar | ≤5 before overflow |
| Options in a single decision | ≤7; beyond that, stage or filter |
| Steps in a linear flow | ≤5 visible steps; use progress + branch for more |
| Menu depth | ≤2 levels for a primary task |

### Do
- **Highlight a recommended option.** A visible default converts a 7-way decision into a 2-way one ("this or something else").
- **Stage the choice.** Wizard, tabs, progressive disclosure, filters. Each screen asks one narrow question.
- **Categorise before listing.** Grouping 20 items into 4 labelled groups of 5 reduces perceived n without hiding anything.
- **Put the most-chosen option first.** Order is a form of recommendation and costs nothing.
- **Use search and filters for large sets** instead of paginating everything. A filter converts n choices into one
  choice about the filter.

### Don't
- Don't hide required options to "reduce choices". Hiding a mandatory decision relocates the cost to error recovery.
- Don't simplify past meaning. The site's own warning: *"Be careful not to simplify to the point of abstraction."*
- Don't apply Hick to a *skilled* repeated task — expert users benefit from density and keyboard shortcuts.
- Don't count visual elements as "choices". A paragraph is not a decision; a button is.

### Audit question
> On this screen, how many things can the user click that lead to *different* outcomes? If >7, what can be grouped, staged, or defaulted?

### Source
[lawsofux.com/hicks-law](https://lawsofux.com/hicks-law/) · IxDF, *Hick's Law: Making the Choice Easier for Users* ·
Hick (1952), Hyman (1953) · Gross, *Redefining Hick's Law*, Smashing Magazine, 2012.

---

## 2.2 Choice Overload

> The tendency for people to get overwhelmed when presented with a large number of options; often used interchangeably
> with the paradox of choice.

### Mechanism
Overchoice was named by Alvin Toffler in *Future Shock* (1970): the advantages of diversity are cancelled by the
complexity of deciding. The canonical demonstration is Iyengar & Lepper's 2000 jam study — a tasting table with **24**
varieties drew more stops than one with **6**, but only about **3%** of the 24-jam stoppers bought, versus roughly
**30%** of the 6-jam stoppers.

But choice overload is **conditional**, not universal. Scheibehenne, Greifeneder & Todd (2010) showed it appears mainly
when three preconditions hold:

1. **No clear prior preference** — the user doesn't already know what they want.
2. **No dominant option** — all options look roughly equivalent in quality.
3. **Low familiarity / expertise** — the user can't quickly sort the set.

Remove any one of those and a large set is fine. This is why experts love dense catalogues and novices freeze.

### Numbers
| Decision | Value |
|---|---|
| Comparable options shown at once | 3–5 (pricing tiers: 3, with 1 recommended) |
| Variants of one product | show 1, offer ≤6 |
| Filters before results | ≤5 primary filters visible, rest behind "more" |
| Time pressure + large set | never — tight time + many options maximises regret |
| Default | always provide one |

### Do
- **Give the user a prior preference** before showing the set: a quiz, a use-case split ("for home / for studio"), a
  recommended pick. Forming a preference is what defuses overload.
- **Create a dominant option.** A clearly best-value tier restores satisfaction even in a large set.
- **Separate *variety* from *complexity*.** Variety helps when choosing an assortment; complexity hurts when choosing
  *within* it (Townsend & Kahn, 2014). So: rich category page, narrow product page.
- **Use images for breadth, text for depth.** Visual sets raise *perceived* variety; verbal detail lowers *perceived*
  complexity. Match the medium to the stage.
- **Enable side-by-side comparison** when the decision is inherently comparative (pricing, specs, plans).

### Don't
- Don't use "choice overload" as a licence to remove options users need. Segment, don't amputate.
- Don't add a countdown to a large set. Time pressure converts a manageable set into a regretted one.
- Don't confuse a long page with a large choice set. Scrolling is cheap; deciding is not.

### Audit question
> Does this screen ask the user to compare more than 5 things at once, with no default and no prior preference formed?
> If yes, add a recommendation, a filter, or a stage.

### Source
[lawsofux.com/choice-overload](https://lawsofux.com/choice-overload/) ·
[Overchoice, Wikipedia](https://en.wikipedia.org/wiki/Overchoice) · Iyengar & Lepper (2000), *JPSP* 79(6) ·
Scheibehenne, Greifeneder & Todd (2010) · Chernev, Böckenholt & Goodman (2015), meta-analysis, *JCP* 25(2).

---

## 2.3 Miller's Law

> The average person can only keep 7 (plus or minus 2) items in their working memory.

### Mechanism
Miller's 1956 paper, *The Magical Number Seven, Plus or Minus Two*, described a roughly constant channel capacity for
immediate memory and absolute judgement. Crucially, **the unit is a chunk, not an item** — and chunk size is learned.
Later work revised the estimate downward: Cowan (2001) puts the focus of attention at about **4 chunks** in young
adults, fewer in children and older adults.

The single most important line in the law's own entry on lawsofux.com is its first takeaway:

> *"Don't use the 'magical number seven' to justify unnecessary design limitations."*

Miller describes a limit on *recall*, not a quota for *design*. The correct response to the limit is chunking (2.5),
not deleting information.

### Numbers
| Domain | Realistic span |
|---|---|
| Digits | ~7 |
| Letters | ~6 |
| Words | ~5 |
| Cowan's revised focus of attention | **~4 chunks** |
| Design rule of thumb per decision point | **3–5** |
| Trained digit span (extreme, via chunking) | up to 80 — proves chunking, not capacity, is the lever |

### Do
- **Design to 4, not 7.** If a decision point must hold items in mind simultaneously (comparing, matching, recalling),
  keep it at 3–5.
- **Chunk aggressively**: phone numbers as `0812-3456-7890`, card numbers in groups of 4, IDs in 4-char blocks.
- **Externalise memory**: show the selected filters, the cart count, the current step, the entered values.
- **Assume individual variation.** Prior knowledge, stress, age, and disability all reduce span. Never design at the
  ceiling of the average.

### Don't
- Don't cite "7±2" to cap a menu at 7 and call it science. Menus are scanned, not recalled — Hick governs menus, Miller governs memory.
- Don't split a single meaningful unit into arbitrary chunks (a 9-digit reference number split 3-3-3 is harder than 4-5).
- Don't rely on the user remembering anything from a previous screen.

### Audit question
> What must the user hold in their head to complete this step? If the answer is more than 4 things, where can the
> interface hold them instead?

### Source
[lawsofux.com/millers-law](https://lawsofux.com/millers-law/) · Miller (1956), *Psychological Review* 63(2) ·
Cowan (2001) · [Working memory, Wikipedia](https://en.wikipedia.org/wiki/Working_memory).

---

## 2.4 Working Memory

> A cognitive system that temporarily holds and manipulates information needed to complete tasks.

### Mechanism
Baddeley & Hitch's multicomponent model (1974, extended 2000) describes a **central executive** coordinating a
**phonological loop** (verbal), a **visuospatial sketchpad** (visual/spatial), and an **episodic buffer** that binds
them and links to long-term memory. Two properties matter for UI:

- **Capacity is ~4 chunks**, and the components are partly independent — so a visual task and a verbal task can run in
  parallel, but two verbal tasks cannot.
- **Contents decay within seconds** without rehearsal. Interference, not just time, causes loss: similar material
  overwrites similar material.

Working memory *manipulates*; short-term memory only *stores*. Every multi-step flow taxes the manipulation capacity.

### Numbers
| Decision | Value |
|---|---|
| Simultaneous chunks | 4–7 (design to 4) |
| Decay without rehearsal | ~20–30 seconds |
| Values carried between steps | 0 — persist them in the UI |
| Comparison items visible at once | ≤4 without a comparison table |
| Fields per step | ≤5 |

### Do
- **Offload to the system.** Carry entered values forward: order summary, "you selected", persistent filters,
  breadcrumbs, visited-link styling.
- **Prefer recognition over recall.** Show options instead of asking the user to type from memory; show the chosen
  value next to the control; show recent items.
- **Keep context on screen** while the task needs it: the item being edited, the total, the step number, the rules.
- **Use a comparison table** for multi-item decisions. It converts n memory slots into one visual scan.
- **Split verbal and visual load** across channels where possible (spoken/visual pairing beats two blocks of text).

### Don't
- Don't require the user to remember a code, price, or selection from a previous screen.
- Don't animate away information the user still needs.
- Don't stack two verbal tasks (e.g. read instructions while listening to a voice prompt that repeats them).

### Audit question
> Walk the flow screen by screen. At each step, what is the user forced to remember? Move it onto the screen.

### Source
[lawsofux.com/working-memory](https://lawsofux.com/working-memory/) ·
[Working memory, Wikipedia](https://en.wikipedia.org/wiki/Working_memory) · Baddeley & Hitch (1974); Baddeley (2000).

---

## 2.5 Cognitive Load

> The amount of mental resources needed to understand and interact with an interface.

### Mechanism
Sweller's cognitive load theory (late 1980s) splits load into three types:

| Type | What it is | Who controls it |
|---|---|---|
| **Intrinsic** | Inherent difficulty of the material (2+2 vs. a differential equation) | Nobody — but it can be *sequenced* into sub-schemas |
| **Extraneous** | Load created by how the material is presented | **The designer** — this is the only lever that matters |
| **Germane** | Effort spent building a mental model (schema construction) | Emerges when extraneous load is low |

The practical law: **extraneous load steals directly from germane load.** Every decorative animation, redundant label,
and split-attention layout is paid for out of the user's capacity to understand the thing they came for.

Named effects worth knowing:

- **Split-attention effect** — forcing the eye to alternate between two sources (chart in one place, legend in another;
  error message at the top, field at the bottom). Fix: integrate spatially.
- **Redundancy effect** — presenting the same information twice in different forms (a paragraph *and* a voice-over
  reading it verbatim) adds load rather than reinforcing.
- **Expertise reversal effect** — guidance that helps novices (tooltips, worked examples, step-by-step) becomes friction
  for experts. Fix: let advanced users dismiss or skip.
- **Worked-example effect** — showing a completed example beats asking someone to figure it out from scratch.

### Numbers
| Decision | Value |
|---|---|
| Competing information sources for one decision | 1 |
| Labels + placeholder + helper + tooltip on one field | max 2 of these |
| Simultaneous animations | 1 |
| Nested navigation depth before breadcrumbs | 2 |
| Reading level for instructional copy | plain language; short sentences |

### Do
- **Integrate, don't separate.** Put the error message under the field, the unit inside the input, the legend next to
  the mark, the price next to the plan.
- **Sequence intrinsic load.** Teach the model in sub-schemas: one concept per step, then combine.
- **Show a worked example** for any non-obvious task (a filled sample, a template, a demo row).
- **Fade guidance with expertise.** Dismissible tips, "don't show again", advanced mode.
- **Remove one thing per screen** until removal hurts. That is the whole method.

### Don't
- Don't decorate a complex task. High intrinsic load + high extraneous load = abandonment.
- Don't repeat the same content in two formats "for accessibility" — provide one clear format plus an alternative
  *on request*.
- Don't put help in a place that requires leaving the task (a separate docs page) when the task is hard.

### Audit question
> For each element on screen: does it help the user do the thing, or does it help the designer feel something?
> Delete the second category.

### Source
[lawsofux.com/cognitive-load](https://lawsofux.com/cognitive-load/) ·
[Cognitive load, Wikipedia](https://en.wikipedia.org/wiki/Cognitive_load) · Sweller (1988); Chandler & Sweller (1992);
Kalyuga et al. (2003).

---

## 2.6 Chunking

> A process by which individual pieces of an information set are broken down and then grouped together in a meaningful whole.

### Mechanism
Chunking is the *constructive* answer to Miller and Working Memory. Capacity is fixed in chunks; a chunk can contain
arbitrarily much if the grouping is meaningful. Miller's own example: 1-9-6-2-1-9-4-5 is eight items, but
"1962 — 1945" is two. Expertise is largely the acquisition of larger chunks.

The design consequence: **meaningful grouping raises effective capacity; arbitrary grouping does not.** Splitting a
10-digit number 3-3-4 helps because phone numbers are learned in that shape. Splitting a name into 3-3-4 does not.

### Numbers
| Decision | Value |
|---|---|
| Items per visual group | **3–5** |
| Groups per section | 3–5 |
| Card grid columns | 2–4 (3 is the safe default) |
| Form fields per group | 3–5, with a group label |
| Nav groups | ≤5 groups × ≤7 items |
| Chunk boundary | must follow a *semantic* boundary, not a count |

### Do
- **Group by meaning first, then by count.** "Contact / Shipping / Payment" is chunking; "fields 1–3 / 4–6" is not.
- **Give each chunk a label** — a heading converts an implicit group into an explicit one and reduces scanning cost.
- **Use progressive disclosure** for chunk depth: summary chunk → detail chunk.
- **Format data in learned chunks**: currency (`Rp 1.250.000`), dates (`23 Oct 2026`), phone, card, IBAN, tracking numbers.
- **Cap card grids at 3–4 columns.** Beyond 4, each card loses enough width that its content chunks break.

### Don't
- Don't chunk visually without chunking semantically (a divider every 5 rows is noise).
- Don't create more than 5 chunks per view; that just relocates the overload one level up.
- Don't break a single unit across chunks to make the counts even.

### Audit question
> Can each group on this screen be named in 1–3 words? If a group needs a sentence to explain, it is not a chunk.

### Source
[lawsofux.com/chunking](https://lawsofux.com/chunking/) · Miller (1956) · IxDF glossary, *Chunking*.

---

## 2.7 Selective Attention

> The process of focusing our attention only to a subset of stimuli in an environment — usually those related to our goals.

### Mechanism
Attention is a bottleneck, not a spotlight with unlimited width. Broadbent's filter theory (1958) proposed early
selection based on physical characteristics; Treisman's attenuation model (1960) softened it (unattended channels are
damped, not blocked); Deutsch & Deutsch (1963) argued selection happens late, after meaning is extracted. The practical
synthesis: **users filter by goal and by learned visual patterns, and they do it before reading.**

Two failure modes you will meet constantly:

- **Banner blindness** — anything that *looks like an ad* (or sits where ads usually sit: right rail, top strip,
  between content blocks) is skipped, including your important content.
- **Change blindness** — a significant change goes unnoticed because nothing marked it. Toasts that appear far from the
  point of action, silent list updates, and state changes without motion all fail here.

### Numbers
| Decision | Value |
|---|---|
| Competing emphases per view | 1 primary, ≤3 secondary |
| Elements that resemble ads (bordered, right-rail, animated, "sponsored" styling) | 0 for real content |
| Noticeable state change | must include ≥1 of: position change, motion, color shift + text |
| Toast duration | 4–6 s for info, persistent for errors |
| Attention resets per screen | ≤1 |

### Do
- **Design for the goal, not the page.** Put the thing the user came for where the eye already goes (top-left of the
  content column, first row, above the fold on mobile).
- **Mark changes explicitly.** Inline highlight that fades, a count badge, a moved element — not a silent re-render.
- **Keep one visual language for "content"** and a clearly different one for "chrome". If content is styled like chrome,
  it disappears.
- **Use motion sparingly and locally** — motion is the strongest attention cue and the fastest way to lose trust when overused.

### Don't
- Don't put critical information in ad-shaped slots. It will be filtered out and you will blame the copy.
- Don't animate more than one thing at a time; competing changes cancel each other (change blindness).
- Don't rely on a color change alone to signal state (also: accessibility, also: Von Restorff's warning).

### Audit question
> Squint. What are the three most visually salient things? Are they the three most important things?
> If not, salience and priority are inverted.

### Source
[lawsofux.com/selective-attention](https://lawsofux.com/selective-attention/) · Broadbent (1958); Cherry (1953);
Treisman (1960); Deutsch & Deutsch (1963); Kahneman (1973).

---

## 2.8 Serial Position Effect

> Users have a propensity to best remember the first and last items in a series.

### Mechanism
Ebbinghaus's U-shaped recall curve, split into two mechanisms:

- **Primacy** — early items get more rehearsal and are transferred to long-term memory. Glenberg et al. (1980): when
  items were presented rapidly, primacy disappeared; when slowly, recall improved.
- **Recency** — late items are still in working memory. Glanzer & Cunitz (1966): a 30-second interference task wiped out
  recency but left primacy intact.

Implication: **the middle of any list is the cheapest real estate and the most expensive place to put something important.**
Short-term capacity in that study: ~3–4 chunks.

### Numbers
| Decision | Value |
|---|---|
| Nav items: most important | first and last |
| Primary CTA position | end of the reading flow (or fixed, but visually last) |
| List length before the middle becomes a dead zone | ~5 |
| Items a user will recall from a 10-item list | ~4 (first 2, last 2) |
| Pagination | keep the current page near an edge; don't bury it mid-row |

### Do
- **Front-load the reason to care**, back-load the action. Landing page: value proposition first, CTA last.
- **Put the two most important nav items at the extremes** — first and last positions in a top nav or tab bar.
- **Bury the least important items in the middle** — legal links, tertiary settings, "about".
- **Repeat the key takeaway at the end** of a long page or flow (this is also Peak-End).
- **Keep lists short enough that the middle is still visible** — or add structure (chunking) so the middle becomes an edge.

### Don't
- Don't put your primary action in the middle of a toolbar or a long menu.
- Don't assume the user read the middle of the page. If it mattered, it belongs at an edge or in its own section.
- Don't confuse "last" with "bottom of a very long scroll" — recency applies to the *sequence attended to*, so a
  persistent CTA can occupy the recency slot.

### Audit question
> List the elements in order. Are positions 1 and n occupied by the two things that matter most?

### Source
[lawsofux.com/serial-position-effect](https://lawsofux.com/serial-position-effect/) · IxDF, *Serial Position Effect* ·
Glenberg et al. (1980); Glanzer & Cunitz (1966).

---

## 2.9 Von Restorff Effect

> When multiple similar objects are present, the one that differs from the rest is most likely to be remembered.

### Mechanism
Hedwig von Restorff (1933) showed that an item which differs from a homogeneous set — by size, color, shape, spacing,
or meaning — is recalled better than its neighbours, regardless of its position. Modern accounts attribute this to
**contextual incongruity**: the isolate violates the established pattern, which recruits extra attention at encoding
(larger P300 amplitude predicts later recall). The critical detail: **the effect requires a consistent baseline.** If
everything is distinctive, nothing is.

This is the law most often abused. It is a budget of exactly one.

### Numbers
| Decision | Value |
|---|---|
| Distinctive elements per view | **1** (2 in a dense dashboard, never more) |
| Ways the isolate differs | 1–2 dimensions (color + weight, or size + position) — not five |
| Accent color usage | ≤10% of the visible surface |
| Similar baseline required | ≥3 similar siblings before an isolate reads as intentional |

### Do
- **Make one thing different per view**: the primary CTA, the recommended plan, the row that needs action.
- **Differentiate on two dimensions**, so the emphasis survives grayscale and color-blindness: fill + weight, or size + position.
- **Keep the baseline boring.** The isolate works because the rest is quiet.
- **Use it for the thing you want remembered tomorrow** — not for the thing you want clicked today. Those are often different.

### Don't
- Don't make every button a different color. That is not emphasis, it is noise with a color palette.
- Don't rely on color alone — von Restorff's own takeaway warns about color-vision deficiency and low vision.
- Don't use motion as the only differentiator for users with motion sensitivity (`prefers-reduced-motion`).
- Don't style important content to look like an ad — salience + ad shape = banner blindness (2.7).

### Audit question
> Screenshot in grayscale. Is exactly one element still dominant? If three are, you have no focal point.

### Source
[lawsofux.com/von-restorff-effect](https://lawsofux.com/von-restorff-effect/) ·
[Von Restorff effect, Wikipedia](https://en.wikipedia.org/wiki/Von_Restorff_effect) · von Restorff (1933),
*Psychologische Forschung* 18(1), 299–342.

---

## Synthesis — the attention budget

A screen has a fixed budget. Spend it once.

```
DECISIONS      ≤7 visible, 1 recommended default            (Hick, Choice Overload)
MEMORY         0 items carried between screens               (Working Memory, Miller)
CHUNKS         3–5 per group, 3–5 groups per section         (Chunking)
EMPHASIS       1 focal point, 2 dimensions of difference      (Von Restorff)
SALIENCE       top 3 salient = top 3 important                (Selective Attention)
POSITIONS      first and last hold the two most important     (Serial Position)
LOAD           one source per decision, nothing decorative    (Cognitive Load)
```

**The reduction ritual.** Before shipping any screen, delete one element. Then ask whether anything was lost.
If nothing was lost, delete another. Stop when removal costs the user something — that is the minimum viable screen,
and it is almost always better than the first draft.
