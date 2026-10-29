# Laws of UX — a rules engine for interface design

A skill that turns the [30 Laws of UX](https://lawsofux.com/) into **decisions an agent can execute**: a spacing and
type contract, law-by-law rules with real thresholds, and a severity-ordered audit for fixing interfaces that look
messy, cramped, unstructured, or generic.

**It ships no palette and no typeface.** A design system is a set of decisions a team already made; arriving with your
own and overriding theirs is not design work. So the skill defines *structure and obligations* — spacing, type sizes,
grid, contrast floors, 21 colour roles — and takes the **values** from the project: its design system, its tokens, or a
UI reference it points at. When there is none, it proposes a direction in words rather than imposing one.

This is not a summary of the website. Each law has its own file containing the site's own takeaways and origin text,
a mechanism section grounded in the primary research, a numbers table, Do/Don't rules, a code pattern, an audit
question, and the site's **complete Further Reading list** — 142 links across the 30 laws.

---

## What it does

The skill runs in five modes, selected by what the user asks for:

| Mode | Trigger | What the agent does |
|---|---|---|
| **BUILD** | "make a site / app / dashboard / landing page" | Six gates: intent → content inventory → design contract → skeleton → assemble with a law pass → states + self-audit |
| **ADAPT** | "here are our tokens / build inside our design system / match this reference UI" | Reads their system, maps 21 roles, validates contrast, then builds inside it |
| **REVISE** | "my UI looks bad / fix this / rapikan tampilan" | Six passes in fixed order: diagnose → structure → rhythm → type → colour → states → re-audit |
| **REVIEW** | "what do you think of this design" | Diagnosis only, no rewrite |
| **EXPLAIN** | "why does this rule exist" | Opens the single law file and answers from it |

Two rules do most of the work in practice:

1. **The Design Contract** — six lines written before any markup (grid, spacing, type scale, colour source, radius,
   motion). Two of the six are slots filled by the project; values outside the contract are a bug.
2. **The three-value rule** — a screen may use at most three spacing values, with an inside : outside ratio of at
   least 1 : 2. This single constraint is the difference between "tidy" and "assembled by eye".

---

## Install

The skill is a plain folder with `SKILL.md` at its root. No build step, no dependencies. Copy it wherever your agent
looks for skills.

### WorkBuddy

```bash
# macOS / Linux
cp -r laws-of-ux ~/.workbuddy-ai/skills/

# Windows (PowerShell)
Copy-Item -Recurse laws-of-ux "$env:USERPROFILE\.workbuddy-ai\skills\"
```

Restart the session — the skill list is read at session start.

### Claude Code

```bash
cp -r laws-of-ux ~/.claude/skills/
```

### Any agent that reads `~/.agents/skills`

```bash
cp -r laws-of-ux ~/.agents/skills/
```

### Project-local (one repo only)

```bash
mkdir -p .claude/skills && cp -r laws-of-ux .claude/skills/
# or
mkdir -p .workbuddy-ai/skills && cp -r laws-of-ux .workbuddy-ai/skills/
```

### Via the `skills` CLI

If the repo is published on GitHub:

```bash
npx -y skills@latest add <owner>/laws-of-ux -g
```

### Verify the install

The skill ships a checker with no dependencies beyond Python 3.8+:

```bash
cd laws-of-ux
python scripts/ux_check.py contrast "#475569" "#ffffff"   # → 7.58:1, AAA for normal text
python scripts/ux_check.py roles path/to/adapter.css      # → the 21 roles + contrast obligations
python scripts/ux_check.py scale                          # → the spacing and type scales
python scripts/ux_check.py css path/to/your.css           # → off-grid spacing, type sizes, radii
python scripts/ux_check.py html path/to/page.html         # → a11y lint + scale audit
python scripts/ux_check.py all path/to/project            # → everything
```

Add `--strict` to exit non-zero on warnings, for CI.

---

## What's inside

```
laws-of-ux/
├── SKILL.md                     the operating manual: modes, gates, passes, self-check
├── laws/                        30 files, one per law — the deep layer
│   ├── 01-aesthetic-usability-effect.md
│   ├── 02-choice-overload.md
│   ├── ...
│   └── 30-zeigarnik-effect.md
├── references/
│   ├── 01-perception-and-layout.md       Gestalt synthesis → grouping, spacing ratios, borders
│   ├── 02-attention-and-memory.md        attention, choice, chunking, memory offload
│   ├── 03-motivation-and-journey.md      flow, progress, endings, first run
│   ├── 04-system-and-interaction.md      convention, targets, latency, complexity, bias
│   ├── 05-layout-spacing-type.md         THE STRUCTURE: grid, scales, colour roles, motion, components
│   ├── 06-revise-playbook.md             12 failure signatures, severity model, 40-point audit
│   ├── 07-design-system-adapter.md       ADAPT: read their system, map 21 roles, validate, or propose a direction
│   └── law-index.md                      symptom → law → file lookup
├── assets/
│   └── design-contract.css               structural tokens + the 21 role obligations (no colours, no typefaces)
└── scripts/
    └── ux_check.py                       contrast, role contract, spacing grid, type scale, a11y lint
```

### Two layers of law, three layers of value

The law layer comes in two depths:

- **`laws/`** — depth on one law. Open it when the task hinges on a specific principle. Every file has the same shape:
  one-liner · site takeaways · site origins · mechanism · numbers · Do/Don't · code pattern · audit question ·
  Further Reading · source.
- **`references/01`–`04`** — synthesis across laws. Use when several laws must agree on one decision (e.g. "how much
  space between these groups?" needs proximity + common region + Prägnanz together).

The value layer comes in three, and only the bottom two belong to this skill:

| Layer | Owner | Contents |
|---|---|---|
| **Values** | the project | colours, typeface, radius, density — from their design system, or a direction they agreed to |
| **Roles** | this skill | 21 named slots with contrast obligations (`--surface`, `--text-primary`, `--accent`…) |
| **Structure** | this skill | spacing scale, type sizes, grid, motion, states |

`references/05` is the structural system. `references/07` is the handoff to the project's values. `references/06` is
the repair playbook.

---

## The 30 laws

| # | Law | The lever | Key number | File |
|---|---|---|---|---|
| 01 | Aesthetic-Usability Effect | polish buys tolerance for *minor* issues | — | [open](laws/01-aesthetic-usability-effect.md) |
| 02 | Choice Overload | cut, stage, or default the option set | 3 preconditions | [open](laws/02-choice-overload.md) |
| 03 | Chunking | group content into meaningful wholes | 3–5 per group | [open](laws/03-chunking.md) |
| 04 | Cognitive Bias | design *with* heuristics, never exploit them | 0 exploitative defaults | [open](laws/04-cognitive-bias.md) |
| 05 | Cognitive Load | remove extraneous load, sequence intrinsic load | 1 source per decision | [open](laws/05-cognitive-load.md) |
| 06 | Doherty Threshold | feedback inside the attention gap | **< 400 ms** | [open](laws/06-doherty-threshold.md) |
| 07 | Fitts's Law | bigger and closer targets | **44 × 44 px**, 8 px gap | [open](laws/07-fittss-law.md) |
| 08 | Flow | match challenge to skill, keep feedback tight | first win < 2 min | [open](laws/08-flow.md) |
| 09 | Goal-Gradient Effect | show progress, accelerate the end | visible remaining steps | [open](laws/09-goal-gradient-effect.md) |
| 10 | Hick's Law | decision time grows with log₂(choices) | ≤ 7 nav items | [open](laws/10-hicks-law.md) |
| 11 | Jakob's Law | borrow conventions users already know | ≤ 1 novel pattern | [open](laws/11-jakobs-law.md) |
| 12 | Law of Common Region | a shared boundary makes a group | padding ≥ sibling gap | [open](laws/12-law-of-common-region.md) |
| 13 | Law of Proximity | distance is the strongest cheap grouping tool | ratio ≥ 1 : 2 | [open](laws/13-law-of-proximity.md) |
| 14 | Law of Prägnanz | simplest readable form wins | ≤ 5 type sizes | [open](laws/14-law-of-pragnanz.md) |
| 15 | Law of Similarity | same look = same meaning | 3 button roles | [open](laws/15-law-of-similarity.md) |
| 16 | Law of Uniform Connectedness | visible connection beats similarity | 1 connector system | [open](laws/16-law-of-uniform-connectedness.md) |
| 17 | Mental Model | match the model in the user's head | ≤ 3 core concepts | [open](laws/17-mental-model.md) |
| 18 | Miller's Law | ~7 ± 2 chunks — a warning, not a quota | **~4** (Cowan) | [open](laws/18-millers-law.md) |
| 19 | Occam's Razor | fewest assumptions, fewest elements | 0 unexplained elements | [open](laws/19-occams-razor.md) |
| 20 | Paradox of the Active User | nobody reads the manual | first action < 10 s | [open](laws/20-paradox-of-the-active-user.md) |
| 21 | Pareto Principle | 20% of elements carry 80% of the task | 80 / 20 | [open](laws/21-pareto-principle.md) |
| 22 | Parkinson's Law | work fills the time given | bound the task | [open](laws/22-parkinsons-law.md) |
| 23 | Peak-End Rule | the peak and the ending are the memory | 1–2 designed peaks | [open](laws/23-peak-end-rule.md) |
| 24 | Postel's Law | liberal input, strict output | 1 output format | [open](laws/24-postels-law.md) |
| 25 | Selective Attention | users filter out what looks irrelevant | 1 focal point | [open](laws/25-selective-attention.md) |
| 26 | Serial Position Effect | first and last are remembered | first + last slots | [open](laws/26-serial-position-effect.md) |
| 27 | Tesler's Law | complexity is conserved — choose who carries it | system absorbs it | [open](laws/27-teslers-law.md) |
| 28 | Von Restorff Effect | one different thing gets remembered | **exactly 1** per view | [open](laws/28-von-restorff-effect.md) |
| 29 | Working Memory | 4–7 chunks, 20–30 s decay | **~4 chunks** | [open](laws/29-working-memory.md) |
| 30 | Zeigarnik Effect | unfinished tasks stay in mind | ≤ 2 open loops | [open](laws/30-zeigarnik-effect.md) |

---

## Using it

You do not invoke the skill by name. Describe the task; the trigger conditions in `SKILL.md` pick it up.

**Build**

> Build a pricing page for a B2B analytics tool. Three plans, annual/monthly toggle, enterprise contact sales.

**Adapt**

> Build that pricing page inside our design system — tokens are in `tokens.css`, brand typeface is already loaded.

**Revise**

> Here is my dashboard. It looks cramped and I can't tell where to look. Fix it.

**Explain**

> Why shouldn't I put more than seven items in the nav?

**Audit**

> Review this checkout flow and tell me what is broken, in priority order.

When the agent cites a law, it should cite the **prescription**, not the name — "proximity ratio ≥ 1 : 2", not "the law
of proximity". A named law is an appeal to authority; a number is a decision.

---

## Bring your own design system

Point the agent at your tokens and the skill builds **inside** them instead of around them.

> Here's our design system (`tokens.css`). Build a settings page that follows it.

What happens:

1. **Read** — extract eleven values: surface, primary text, muted text, border, the primary action and its hover/active
   states, the semantic set, the type family, the sizes actually in use, the radius, and the density.
2. **Map** — those values go onto 21 fixed role names in one adapter block. Your token names are never renamed.
3. **Validate** — `ux_check.py roles` checks the contrast obligations before a single screen is written. If your
   `--text-muted` is 2.6:1 on white, you hear about it now, not at review.
4. **Build** — structure comes from the laws; every colour and every typeface comes from you.
5. **Report** — what was used, what had to be derived, and what failed.

### When you have no design system

The skill will not invent a palette. It proposes at most three **directions in words** — *"cool neutrals with one
saturated accent and a neo-grotesque"* — you pick one, and only then are values derived. `references/07` carries the
vocabulary: eight colour directions and eight type categories, described by what they signal rather than by hex codes,
plus the obligations every derived value has to satisfy.

### What it will not do

- Invent a brand colour or a typeface and present it as the answer.
- Silently override your radius, spacing base, or density.
- Mix two design systems into one screen.
- Copy a reference site's pixels — tokens and conventions, yes; its bugs, no.

---

## Design principles behind the skill

1. **Every law becomes a decision.** If a law cannot produce a number, an order, or a constraint, it is not in the
   build path.
2. **Numbers over adjectives.** "Rapi" is not a specification; `gap: 8px` inside a group and `24px` between groups is.
3. **Fixed order of repair.** Structure → rhythm → type → colour → states → motion → polish. Painting before
   restructuring is why redesigns stay ugly.
4. **Ethics is not optional.** Cognitive bias, scarcity, defaults, and open loops all have manipulative uses. The skill
   carries an explicit guardrail: if the user would not choose it knowing the mechanic, it is a dark pattern.
5. **Depth is per-law, synthesis is thematic.** Two layers, because "explain this law" and "decide this gap" are
   different questions.
6. **Values belong to the project.** A skill that ships a palette is a theme pretending to be a method. This one ships
   obligations and takes values.

---

## The checker

`scripts/ux_check.py` is the part that keeps the agent honest, because eyeballing spacing does not scale.

| Command | What it catches |
|---|---|
| `contrast <fg> <bg>` | WCAG ratio, AA/AAA verdict, and the minimum passing shade |
| `roles <adapter.css>` | the 21 required roles, which are missing, and whether each contrast obligation passes |
| `scale` | prints the spacing and type scales, and states that colour has no values |
| `css <file>` | off-grid spacing, off-scale type sizes, unusual radii, missing 1.5 line-height |
| `html <file>` | the above plus missing `alt`, unlabeled inputs, missing `lang`, heading order |
| `all <dir>` | walks a project |

Example output:

```
$ python scripts/ux_check.py css app.css

  file: app.css

  [FAIL] off-scale spacing: 4 declaration(s)
             18px  x1
              7px  x1
             22px  x1
             13px  x1
         allowed: 4 8 12 16 24 32 48 64 96 128

  type sizes in use: 1 -> 15px
  [WARN] off-scale sizes: 15px

  radii in use: 1 -> 10px
  [WARN] unusual radii: 10px

  4 problem(s) reported across 1 file(s)
  Fix order: structure -> rhythm -> type -> color -> states -> motion -> polish
```

---

## Sources and attribution

Law names, one-line definitions, takeaways, origin text and Further Reading lists come from
**[lawsofux.com](https://lawsofux.com/) by Jon Yablonski** (*Laws of UX*, O'Reilly, 2020), and are quoted here for
reference. The mechanism sections, numbers tables, Do/Don't rules, code patterns and audit questions are original to
this skill and grounded in the primary research those pages cite — Nielsen Norman Group, Interaction Design
Foundation, Smashing Magazine, and the original papers (Miller 1956; Cowan 2001; Hick 1952; Hyman 1953; Fitts 1954;
Sweller 1988; Baddeley & Hitch 1974; von Restorff 1933; Zeigarnik 1927; Csíkszentmihályi 1975; Kahneman et al. 1993;
Kivetz, Urminsky & Zheng 2006; Kurosu & Kashimura 1995; Tversky & Kahneman 1974; Doherty & Thadani 1982;
Rosson & Carroll 1987; Postel, RFC 761).

Standards referenced: WCAG 2.2 (1.4.3, 1.4.11, 1.4.12, 2.5.8), ISO 9241-9, Apple HIG (44 pt), Material Design (48 dp).

If you redistribute this skill, keep this attribution. The lawsofux.com text is the author's work; the analysis around
it is not a substitute for the book.

---

## License

The skill's original content (SKILL.md, references, laws analysis, scripts) is released under the MIT license.
Quoted material remains © Jon Yablonski and the respective publishers listed in each law's Further Reading.
