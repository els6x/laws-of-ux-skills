---
name: laws-of-ux
description: Use this skill whenever you design, build, or repair a user interface — websites, web apps, mobile apps, dashboards, landing pages, forms, onboarding, or design systems. It turns the 30 Laws of UX (lawsofux.com) and their primary research sources into working rules: a spacing/type/grid contract, law-by-law thresholds, and a severity-ordered audit playbook. It carries no palette and no typeface — it adapts to the project's existing design system or UI reference, and when there is none it proposes a direction in words instead of imposing one. Trigger on: build or redesign a website/app UI, improve layout, spacing, hierarchy or typography, fix a UI that looks bad or unprofessional, review or critique a design, audit accessibility and visual structure, apply our design system or tokens to a page, match a reference UI, or any mention of UX laws, Gestalt, Hick, Fitts, Miller, cognitive load, visual hierarchy, or design principles. Indonesian triggers: buat website, buat aplikasi, desain UI, rapikan tampilan, spacing berantakan, UI kurang rapi, revisi desain, perbaiki layout, sesuaikan dengan design system, ikuti brand kami.
---

# Laws of UX — Rules, not a theme

Thirty laws, one job: make interfaces that are legible, calm, structured, and memorable — not decorated.
This skill converts each law into a **decision** (a number, an order, a constraint), and converts the decisions
into a build sequence and an audit sequence.

Source: [lawsofux.com](https://lawsofux.com/) by Jon Yablonski, plus the primary research each law links to
(Nielsen Norman Group, Interaction Design Foundation, Smashing Magazine, Wikipedia, Sweller, Kahneman, Hick,
Fitts, Miller, Cowan, Zeigarnik, von Restorff, Csikszentmihalyi, Krug, Norman). Per-law citations live in
`references/`. Do not invent statistics — every number in this skill is sourced.

---

## 0. Four rules that override everything below

1. **Laws are constraints, not decoration.** Never cite a law to justify a choice you already made.
   If a law does not change a number, an order, or a removal — it is not being used.
2. **Structure before surface.** Content → grid → spacing → type → color → states → motion → polish.
   Fixing color before hierarchy is wasted work, and it is the #1 reason "revised" UIs still look bad.
3. **One signature, many conventions.** Familiar structure (Jakob's Law) carrying exactly one distinctive
   idea (Von Restorff). Two signatures is noise; zero is generic.
4. **Values come from the project.** This skill has no palette and no typeface, and that is deliberate.
   Read the user's design system or UI reference (`references/07`). If there is none, propose a **direction in
   words**, get agreement, then derive values that satisfy the contrast obligations. Never invent a brand colour
   or a typeface and present it as the answer.

---

## 1. Mode router — read this first

| User intent | Mode | Load |
|---|---|---|
| "Build / make / design a site, app, page, dashboard" | **BUILD** | `references/05` → then 1–2 of `01`–`04` |
| "Here is our design system / tokens / brand — build inside it" | **ADAPT** | `references/07` → `05` |
| "Match this reference UI / make it look like this" | **ADAPT** | `references/07` → `05` |
| "My UI looks bad / messy / fix it / revise this" | **REVISE** | `references/06` → `05` → targeted law files |
| "What do you think of this design / review it" | **REVIEW** | `references/06` (diagnosis only, no rewrite) |
| "Why does this rule exist / explain X law" | **EXPLAIN** | `references/law-index.md` → `laws/NN-*.md` for that law |

Load **at most two** law reference files at a time. They are deep, not scannable; loading all four dilutes attention.

**Three layers, and only one of them is ours.**

| Layer | Who owns it | What it contains |
|---|---|---|
| Values | the project | colours, typeface, radius, density — from their design system or a direction they agreed to |
| Roles | this skill | 21 named slots (`--surface`, `--text-primary`, `--accent`…) with contrast obligations |
| Structure | this skill | spacing scale, type sizes, grid, motion, states |

If a task needs a colour and no value has been supplied, the answer is never "pick a nice one". It is
`references/07`: read their system, or propose a direction in words and get agreement.

**Two depths of law.**

- `laws/` — one complete file per law, 30 files, numbered in the site's alphabetical order. Each holds the site's own
  takeaways and origin text verbatim, a mechanism section grounded in the primary research, a numbers table, Do/Don't,
  a code pattern, an audit question, and the site's **entire Further Reading list**. Open one of these when the task
  hinges on a single law.
- `references/01`–`04` — thematic synthesis *across* laws (grouping, attention, motivation, system behaviour). Use these
  when you need several laws to agree on one decision.

Never cite a law from memory when `laws/` has the file. The file carries the numbers.

---

## 2. BUILD mode — six gates

Do not skip a gate. Each gate has a pass condition.

### Gate 1 — Intent (no pixels yet)
Answer in ≤5 lines: who the user is, the one task the screen exists for, the primary action, what "done" looks like,
and the single most important number/text on the page.
- **Pass:** you can name the primary action in 4 words. If you can't, the screen has no hierarchy yet.

### Gate 2 — Content inventory (Occam + Pareto)
List every element. Then delete: anything that does not serve the Gate-1 task, anything duplicated, anything
that exists "because other sites have it". Rank what remains: 1 primary, 2–3 secondary, rest tertiary.
- **Pass:** ≤1 primary, ≤3 secondary, and you removed at least one thing.
- 80/20 (Pareto): spend design effort on the 20% of elements that carry the task.

### Gate 3 — Design Contract (write this before markup)
Emit exactly these six lines. Every later value must come from them. Two slots are filled by the project, not by you.

```
GRID      : 12 col / gutter 24 / margin 24·48·80 / max 1280 · content 65ch
SPACING   : 4 8 12 16 24 32 48 64 96 128   (base 4, rhythm 8) — or their base, same ratios
TYPE      : 12 14 16 20 24 32 40 48 64 · lh 1.5 body · 1 family (2 with mono)
            family: <their typeface, or the category you agreed on>
COLOUR    : 21 roles via the adapter · 1 accent ≤10% · contrast 4.5 / 3 / 3
            values: <their tokens, or the direction they agreed to>
RADIUS    : 8 (controls) · 12 (cards) · 16 (modals) · full (pills) — or their geometry
MOTION    : 120 / 200 / 320 ms · ease-out in, ease-in out · reduced-motion respected
```

- **Pass:** the six lines exist, no later value contradicts them, and both `<...>` slots name a real source — a token
  file, a reference UI, or a direction the user agreed to. "Looks good" is not a source.
- If you need a 7th spacing value, you have a broken scale — reuse or fix the scale, don't add `padding: 18px`.
- If the project has a design system, the adapter comes **before** the skeleton (`references/07`).

### Gate 4 — Skeleton (structure, no styling)
Semantic landmarks, one `<h1>`, heading levels in order, a 12-col grid, and every region placed by importance.
Test at 320px width first (mobile-first), then 768, 1280.
- **Pass:** with CSS disabled, the reading order still matches the importance ranking from Gate 2.

### Gate 5 — Assemble with the law pass
Apply, in this order — each layer depends on the previous:
1. **Group** — Proximity, Common Region, Uniform Connectedness, Similarity (file `01`)
2. **Rank** — Von Restorff, Selective Attention, Serial Position (`02`)
3. **Bound** — Hick, Choice Overload, Miller, Chunking, Working Memory, Cognitive Load (`02`)
4. **Place & time** — Fitts, Doherty, Parkinson, Flow (`04`, `03`)
5. **Mean** — Jakob, Mental Model, Postel, Tesler (`04`)
6. **Feel** — Aesthetic-Usability, Peak-End, Goal-Gradient, Zeigarnik (`03`)
- **Pass:** every spacing gap is a token; every emphasis is unique on the screen.

### Gate 6 — States and self-audit
Build all eight states before calling it done: default, hover, focus-visible, active, disabled, loading, empty, error.
Then run §6 self-check. If a state is missing, the UI is not finished — it is a mockup.

If you are writing files, start from `assets/design-contract.css`, then write the adapter from the project's values
(`references/07`). Build the markup yourself — the contract and the laws are the reference, not a template.
Run `python scripts/ux_check.py all <project-dir>` and fix every `[FAIL]`. Report the numbers, don't claim they pass.

---

## 3. REVISE mode — six passes, fixed order

Never jump to pass 3. Most "ugly" UIs are structurally broken, and restyling them makes the breakage prettier.

**Pass 1 — Diagnose (no edits).** Score the UI against the 12 failure signatures in `references/06`.
Name the top 3 by severity (P0 blocks a task, P1 slows it, P2 friction, P3 polish).

**Pass 2 — Structure.** Fix reading order, grouping, and what is on the screen at all. Delete before adding.
This is where 60% of the visible improvement comes from.

**Pass 3 — Rhythm.** Replace every ad-hoc gap with the spacing scale. Enforce the separation ratio:
intra-group = 1 step, inter-group = 2 steps, inter-section = 3–4 steps, each level ≥2× the one inside it.
Flattening all gaps to 16px is the single most common cause of "looks unprofessional".

**Pass 4 — Type & hierarchy.** One scale, max 3 sizes per view, one emphasis per region, measure 45–75ch,
line-height 1.5 for body.

**Pass 5 — Color, states, motion.** Contrast floor, non-color redundancy, eight states, motion budget.

**Pass 6 — Re-audit.** Re-score. Report before/after per dimension. If a dimension did not move, say so.

---

## 4. Law → lever map

Use this to pick the right tool. Full detail in the numbered reference files.

| Design decision | Governing laws | Load |
|---|---|---|
| Grouping, spacing, layout structure | Proximity · Common Region · Uniform Connectedness · Similarity · Prägnanz | `01` |
| How many choices, menu size, form length | Hick · Choice Overload · Miller · Chunking | `02` |
| Memory burden, multi-step flows, tables | Working Memory · Cognitive Load · Serial Position · Paradox of the Active User | `02`,`03` |
| What draws the eye first | Von Restorff · Selective Attention · Serial Position | `02` |
| Target size, placement, thumb zones | Fitts | `04` |
| Speed, feedback, perceived performance | Doherty · Parkinson · Flow | `04`,`03` |
| Convention vs. novelty | Jakob · Mental Model · Postel | `04` |
| Who carries the complexity | Tesler · Occam · Pareto | `04`,`03` |
| Momentum, progress, completion | Goal-Gradient · Zeigarnik · Flow | `03` |
| Emotional memory of the journey | Peak-End · Aesthetic-Usability | `03` |
| Judgment errors, defaults, pricing | Cognitive Bias · Choice Overload · Aesthetic-Usability | `04`,`02` |

---

## 5. The 30 laws, compressed

Numbers are the thresholds that matter. `—` means the law is qualitative; use its Do/Don't list instead.

| # | Law | Lever | Number |
|---|---|---|---|
| 01 | Aesthetic-Usability | polish buys tolerance — of *minor* issues only | — |
| 02 | Choice Overload | cut, stage, or default the option set | 3 preconditions (§02) |
| 03 | Chunking | group content into meaningful wholes | 3–5 per group |
| 04 | Cognitive Bias | design *with* heuristics, never exploit them | — |
| 05 | Cognitive Load | remove extraneous load, sequence intrinsic load | — |
| 06 | Doherty Threshold | feedback under the attention gap | **<400 ms** |
| 07 | Fitts's Law | bigger + closer targets | **≥44×44 px**, gap ≥8 |
| 08 | Flow | match challenge to skill, keep feedback tight | — |
| 09 | Goal-Gradient | show progress, accelerate the end | — |
| 10 | Hick's Law | decision time grows with log₂(choices) | ≤7 nav items |
| 11 | Jakob's Law | borrow conventions users already know | — |
| 12 | Law of Common Region | a shared boundary makes a group | — |
| 13 | Law of Proximity | distance is the strongest cheap grouping tool | ratio ≥2× |
| 14 | Law of Prägnanz | simplest readable form wins | — |
| 15 | Law of Similarity | same look = same meaning | — |
| 16 | Law of Uniform Connectedness | visible connection beats similarity | strongest grouping |
| 17 | Mental Model | match the model in the user's head | — |
| 18 | Miller's Law | ~7±2 chunks — a warning, not a quota | 7±2 / **4** |
| 19 | Occam's Razor | fewest assumptions, fewest elements | — |
| 20 | Paradox of the Active User | nobody reads the manual | — |
| 21 | Pareto Principle | 20% of elements carry 80% of the task | 80/20 |
| 22 | Parkinson's Law | work fills the time given | — |
| 23 | Peak-End Rule | the peak and the ending are the memory | — |
| 24 | Postel's Law | liberal input, strict output | — |
| 25 | Selective Attention | users filter out what looks irrelevant | — |
| 26 | Serial Position Effect | first and last are remembered | — |
| 27 | Tesler's Law | complexity is conserved — you choose who carries it | — |
| 28 | Von Restorff Effect | one different thing gets remembered | **1** per view |
| 29 | Working Memory | 4–7 chunks, ~20–30 s decay | 4–7 |
| 30 | Zeigarnik Effect | unfinished tasks stay in mind | — |

The `#` column is the file in `laws/` — `laws/01-aesthetic-usability-effect.md` through `laws/30-zeigarnik-effect.md`.
Open the file when you need the full treatment; this table is only the routing layer.

---

## 6. Self-check before delivering (11 gates)

Fail any → fix before showing the result.

1. **Squint test** — blur the UI. Can you still see exactly one primary action? (Von Restorff, Prägnanz)
2. **Gap test** — are all gaps from the scale, and does the gap between groups exceed the gap inside groups by ≥2×? (Proximity)
3. **Order test** — with CSS off, does reading order equal importance order? (Serial Position, Cognitive Load)
4. **Count test** — nav items ≤7, fields per step ≤5, choices per decision ≤7 (or staged). (Hick, Miller, Choice Overload)
5. **Memory test** — can the task be done without remembering anything from a previous screen? (Working Memory)
6. **Target test** — every interactive element ≥44×44 px with ≥8 px separation, reachable one-handed on mobile. (Fitts)
7. **Time test** — every action has feedback <400 ms; anything >1 s shows progress; anything >10 s is interruptible. (Doherty)
8. **Contrast test** — body ≥4.5:1, large text ≥3:1, UI boundaries ≥3:1; no meaning carried by color alone. (Von Restorff + WCAG)
9. **State test** — hover, focus-visible, active, disabled, loading, empty, error all exist. (Doherty, Postel)
10. **Signature test** — name the one thing a user would remember about this screen. If you can't, it is generic. (Von Restorff, Aesthetic-Usability)
11. **Source test** — point at every colour and every typeface in the output and name where it came from: their token
    file, their reference UI, or a direction they agreed to. Anything you cannot trace, you invented.

---

## 7. When laws conflict

Resolve top-down. Higher layers veto lower ones.

1. **Accessibility & legibility** — contrast, target size, focus, reduced motion. Never traded.
2. **Comprehension** — can the user tell what this is, where they are, and what to do next?
3. **Efficiency** — time and steps to complete the task.
4. **Delight** — aesthetics, motion, personality.

Common conflicts and the ruling:

| Conflict | Ruling |
|---|---|
| Hick (fewer options) vs. Jakob (conventional full nav) | Keep the conventional *pattern*, reduce the *items*. Convention governs shape, Hick governs count. |
| Von Restorff (make it pop) vs. Prägnanz (simplify) | One focal point per view. Emphasis is a scarce resource, not a style. |
| Aesthetic-Usability (pretty) vs. Cognitive Load (dense) | Aesthetics may mask only *minor* friction; real task cost always wins. |
| Miller (7±2) vs. completeness (show everything) | Miller is not a quota. Chunk and disclose; never delete information the task needs. |
| Tesler (system absorbs complexity) vs. Occam (remove elements) | Absorb complexity in the system, remove it from the screen. Never the reverse. |
| Flow (remove friction) vs. Postel (accept anything) | Be liberal in *input format*, strict in *meaning*; never silently guess destructive intent. |

---

## 8. Anti-patterns: law theater

Reject these moves in your own output:

- **"Miller's 7" as a design limit.** Miller himself is cited on lawsofux.com warning against this. Chunk; don't count.
- **"Hick's Law" to hide necessary options.** Progressive disclosure is fine; hiding a required choice is not.
- **"Gestalt" as a vibe word.** Name the principle and the gap value it produced.
- **"Aesthetic-Usability" to skip usability testing.** It masks minor issues and *contaminates* research.
- **"Zeigarnik" to fake incompleteness.** Manufactured progress is a dark pattern (§9).
- **Generic AI-slop layout**: centered hero + three equal icon cards + purple gradient + emoji + every section
  the same height. It is Prägnanz with no Von Restorff — legible and forgettable. Fix with §10.

---

## 9. Ethics guardrail (non-negotiable)

These laws describe how attention works; using them against the user is a defect, not a growth tactic.

- **No fake progress.** Goal-Gradient and Zeigarnik require *real* progress. No pre-ticked steps, no artificial
  near-completion, no "1 of 2" when there are five.
- **No dark defaults.** Cognitive Bias + Choice Overload: no opt-out buried, no confirmshaming, no roach motel,
  no scarcity timers that reset.
- **No dishonest speed.** Optimistic UI must reconcile with the server and surface failure. Never show "Saved"
  before it is saved.
- **No delight as cover.** Peak-End cannot rescue a broken core task; a confetti ending on a failed flow is contempt.
- **Test:** would the user thank you if they could see the mechanism? If not, remove it.

---

## 10. Making it creative (not just tidy)

Tidiness is the floor. Distinctiveness comes from **one deliberate deviation inside a strict system** — which is
exactly Von Restorff applied at page scale.

- **Fix three variables, vary one.** Lock grid, type family, and the surface ramp — *theirs*, not yours; then take one
  bold position on scale, accent intensity, or composition.
- **Contrast of scale, not contrast of hue.** 64px against 14px reads as designed; 24px against 18px reads as an accident.
- **One grid break per page.** Break on one axis only; keep the other locked. Break it where the argument is.
- **Negative space as content.** Reserve one region of deliberate emptiness — it buys Prägnanz for everything near it.
- **One motion moment.** A single transition worth noticing (Peak-End). Everything else is 120–200 ms and invisible.
- **Type as the image.** Before adding illustration, try weight, scale, and tracking. Cheapest, most distinctive move.
- **Signature test** (§6.10) is the acceptance criterion for "creative", not "has gradients".

---

## 11. Worked example (REVISE mode)

Input: *"rapikan UI dashboard saya, spacing-nya berantakan dan semuanya kelihatan sama penting."*

Wrong response: change colours, add shadows, round the corners.

Right response — trace:

```
1  DIAGNOSE   Screenshot. Signatures found: S1 flat spacing (3), S2 collapsed hierarchy (3),
              S7 card fog (2), S9 decision dump (2). Top: S1 + S2, both P1, both high-frequency.
2  STRUCTURE  Rank: 1 headline metric, 4 supporting, rest into a table. Delete 3 of 11 widgets.
              Remove cards from the 6 blocks that are not objects. (60% of the win, here.)
3  RHYTHM     Adopt 8 / 24 / 64. Inside cards 24, between cards 24 → raise to 32. Section 64.
              Every 12/18/20px gap collapses into the scale.
4  TYPE       5 sizes → 3 (14 / 16 / 32). Drop the 700-weight on body copy.
5  COLOR      Accent only on the primary action and the one positive delta. Grayscale check passes.
6  STATES     Add loading skeleton per widget, empty state with a create action, inline error per widget.
7  RE-AUDIT    grouping 1→3 · hierarchy 0→3 · typography 1→3 · states 0→2 · craft 1→2
              Flat lines reported: colour was already adequate (2→2).
```

Output shape: what changed, why (law + number), what did not change, and the remaining debt.

---

## 12. Reference map

```
laws/01..30-<slug>.md                   ONE FILE PER LAW — site takeaways + origins verbatim, mechanism, numbers,
                                        Do/Don't, code pattern, audit question, full Further Reading list
references/01-perception-and-layout.md   5 Gestalt laws → grouping, spacing ratios, borders, alignment
references/02-attention-and-memory.md    9 laws → choice count, chunking, memory offload, emphasis
references/03-motivation-and-journey.md  8 laws → flow, progress, endings, first-run, effort allocation
references/04-system-and-interaction.md  8 laws → convention, targets, latency, complexity, bias
references/05-layout-spacing-type.md     THE STRUCTURE: grid, spacing scale, type scale, roles, motion, components
references/06-revise-playbook.md         12 failure signatures, severity model, fix order, 40-point audit
references/07-design-system-adapter.md   ADAPT: read the project's system, map 21 roles, validate, or propose a direction
references/law-index.md                  symptom → law → file:section lookup
assets/design-contract.css               structural tokens + the 21 role obligations (no colours, no typefaces)
scripts/ux_check.py                      contrast + role contract + spacing-grid + type-scale checker
```

Each law file uses the same schema: **one-liner · site takeaways · site origins · mechanism · numbers · Do/Don't ·
code pattern · audit question · Further Reading · source.**
When you cite a law in a deliverable, cite the specific prescription ("proximity ratio ≥2:1"), not the name.
