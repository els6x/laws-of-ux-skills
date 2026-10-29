---
law: Mental Model
slug: mental-model
index: 17
category: cognition
lever: expectation match
audit_weight: critical
source: https://en.wikipedia.org/wiki/Mental_model
---

# 17 · Mental Model

> A compressed model based on what we think we know about a system and how it works.

**Category** Cognition · **Lever** Expectation match · **Audit weight** Critical

## What the site says

### Takeaways

1. We form a working model in our minds around what we think we know about a system, especially about how it works, and then we apply that model to new situations where the system is similar.
2. Match designs to the users’ mental models to improve their experience. This enables them to easily transfer their knowledge from one product or experience to another, without the need to first take the time to understand how the new system works.
3. Good user experiences are made possible when the design of a product or service is in alignment with the user’s mental model. Take for example e-commerce websites, which use consistent patterns and conventions such product cards, virtual carts and checkout flows in order to conform to users’ expectations.
4. The task of shrinking the gap between our own mental models and those of the users is one of the biggest challenges we face, and to achieve this goal we use a variety of user research methods (e.g. user interviews, personas, journey maps, empathy maps).

### Origins

The notion of a mental model was originally postulated by the psychologist Kenneth Craik in the 1943 book The Nature of Explanation (1943). He proposed that people carry in their minds a small-scale model of how the world works. These models are used to anticipate events, reason, and form explanations.

*Primary source cited on the site: [jstor.org](https://www.jstor.org/stable/26268859)*

## Mechanism — why this happens

A mental model is a **compressed, incomplete, often wrong theory** of how a system works. Users do not read your
architecture; they run their model against it and notice only when the two disagree. The disagreement is the bug report
— "it didn't save", "where did my file go", "why did it charge me twice" — even when the system behaved exactly as
specified.

The useful frame is the gap between three models:

| Model | Whose | What it contains |
|---|---|---|
| **User's model** | the person | What they believe happens, built from other products and prior sessions |
| **System model** | yours | What actually happens, including edge cases |
| **Design model** | the interface | What the interface *communicates* about how it works |

Usability problems are almost always a gap between the first and the third. The system model is rarely the problem; the
*communication* is. That is why "the user is wrong" is never a fix.

Two practical consequences:

1. **You cannot change the user's model by explaining it in documentation.** You change it by making the interface
   behave the way they expect, or by showing the difference at the moment it matters.
2. **The strongest mental models are spatial and physical** — files in folders, items in a cart, pages in a book, layers
   in a stack. Borrowing one is free; inventing one is expensive.

## Numbers that matter

| Quantity | Value | Consequence for the interface |
|---|---|---|
| Models a user holds per product | 1 (plus fragments) | You get one metaphor, not five |
| Tolerance for a model mismatch | 1 occurrence | After that, trust in the whole system drops |
| Onboarding needed for a novel model | explicit teaching | Every unexplained novelty becomes support load |
| Steps to recover from a broken model | ≤1 | If recovery takes more, the user leaves |

## Apply it

### Do

- **Find the model before you design.** Ask five users "what do you think happens when you click this?" Their answers
  are the spec.
- **Borrow existing metaphors** — inbox, cart, folder, board, calendar, timeline. They come pre-loaded.
- **Make system state visible.** Show what is saved, what is syncing, what failed. Invisible state forces the user to
  guess, and guesses drift.
- **Confirm the model at the moment of action.** "This will email all 240 subscribers" is a model correction that
  costs one line.
- **Keep the model consistent across surfaces.** If "archive" hides items in the app but deletes them in the API, the
  model breaks.
- **Design the recovery path** for when the model is wrong: undo, version history, restore.

### Don't

- Don't invent a novel interaction model for a solved problem. See `11-jakobs-law.md` — novelty has a price and the
  user pays it.
- Don't use internal vocabulary in the interface ("workspace entity", "provisioning state"). It teaches your model,
  not theirs.
- Don't hide destructive behaviour behind a benign label. "Clean up" that deletes is a model violation, not a
  simplification.
- Don't assume the model transfers from desktop to mobile. It often does not.
- Don't explain the model in a help centre article and call it designed.

## Pattern

```html
<!-- Make state visible: the user's model says "saved" means saved -->
<div class="doc-status" role="status" aria-live="polite">
  <span class="doc-status__dot doc-status__dot--saved" aria-hidden="true"></span>
  Saved 2 minutes ago
</div>
```

```css
.doc-status { display: inline-flex; align-items: center; gap: var(--space-2);
              font-size: var(--text-sm); color: var(--text-secondary); }
.doc-status__dot { inline-size: 8px; block-size: 8px; border-radius: 50%; }
.doc-status__dot--saved   { background: var(--success); }
.doc-status__dot--saving  { background: var(--warning); }
.doc-status__dot--failed  { background: var(--danger); }
```

```html
<!-- Correct the model at the moment of action, not in docs -->
<button class="btn btn--danger" aria-describedby="archive-note">Archive project</button>
<p id="archive-note" class="hint">
  Archived projects are hidden from everyone but not deleted. Restore any time from Settings → Archived.
</p>
```

```html
<!-- A familiar metaphor does the teaching for free -->
<nav class="tabs" role="tablist" aria-label="Project sections">
  <button role="tab" aria-selected="true">Overview</button>
  <button role="tab" aria-selected="false">Files</button>
  <button role="tab" aria-selected="false">Activity</button>
</nav>
```

## Audit question

> Ask a user who has never seen this screen: "what do you think happens if you click this?" If their answer differs
> from the system model, the interface is the thing that is wrong.

## Further reading

| Reading | Author / Publisher |
|---|---|
| [Mental Models: An Interdisciplinary Synthesis of Theory and Methods](https://www.jstor.org/stable/26268859) | Natalie A. Jones, Helen Ross, Timothy Lynam, Pascal Perez, Anne Leitch \| JSTOR |
| [Mental Models in User Experience Design](https://www.nngroup.com/articles/mental-models/) | Megan Chan and Jakob Nielsen \| Nielsen Norman Group |
| [Familiar vs Novel](https://lawsofux.com/articles/2024/familiar-vs-novel/) | Jon Yablonski \| Laws of UX |
| [Mental Models](https://thedecisionlab.com/reference-guide/design/mental-models) | Dr. Lauren Braithwaite \| The Decision Lab |

---

**Site page** · [lawsofux.com/mental-model](https://lawsofux.com/mental-model/)
