---
law: Paradox of the Active User
slug: paradox-of-the-active-user
index: 20
category: behaviour
lever: onboarding in context
audit_weight: critical
source: https://en.wikipedia.org/wiki/Paradox_of_the_active_user
---

# 20 · Paradox of the Active User

> Users never read manuals but start using the software immediately.

**Category** Behaviour · **Lever** Onboarding in context · **Audit weight** Critical

## What the site says

### Takeaways

1. Users are often motivated to complete their immediate tasks and therefore they don't want to spend time up front reading documentation.
2. This paradox exist because users will save time in the long term if they take the time to optimize the system and learn more about it.
3. Make guidance accessible throughout the product experience and design it to fit within the context of use so that it can help these active new users no matter what path they choose to take (e.g. tooltips with helpful information).

### Origins

This concept was first defined by Mary Beth Rosson and John Carroll in 1987 as part of their larger work on interaction design, Interfacing thought: cognitive aspects of human-computer interaction. Rosson and Carroll found that new users were not reading the manuals supplied with computers and instead would just get started using them, even if it meant getting into errors and running into roadblocks.

*Primary source cited on the site: [researchgate.net](https://www.researchgate.net/publication/262322669_Paradox_of_the_active_user)*

## Mechanism — why this happens

The paradox, described by Carroll and Rosson, is that users **start using software immediately and never read the
manual**, even though reading first would be more efficient. They do not behave irrationally — they behave optimally
under uncertainty. Reading costs time now for a benefit that may not materialise; clicking costs almost nothing and
produces information immediately. Given an unknown payoff, trying is the rational strategy.

The design consequence is severe and often ignored: **any knowledge required before the first action will not be
acquired.** Tutorials, tooltips shown before the task, help-centre links, and "read this first" panels are all
documentation delivered at the moment of lowest motivation.

What works instead is information delivered **at the point of need**, in the context of an action the user has already
decided to take:

| Moment | What the user will read |
|---|---|
| Before any action | Nothing |
| At the field they are stuck on | The hint, briefly |
| After an error | The error message, carefully |
| At the moment of a consequential action | The confirmation, if it is short |
| After success | The next step |

That is the whole strategy: **move the manual into the interface, one sentence at a time, at the moment it is needed.**

## Numbers that matter

| Quantity | Value | Consequence for the interface |
|---|---|---|
| Users who read onboarding before acting | very few | Do not design for them |
| Time tolerated before first value | a few seconds | Any longer and the user starts clicking randomly |
| Hint length that gets read | one short sentence | Paragraphs are skipped |
| Steps before the first real action | 0–1 | Beyond that, the manual is being enforced |

## Apply it

### Do

- **Let the user act immediately.** The first screen should contain the product's core action, not a tour.
- **Put guidance where the decision is.** Inline hints under the field, a short note next to the toggle, a one-line
  explanation in the confirm dialog.
- **Use empty states as onboarding.** The empty state is the only moment the user is guaranteed to look at the screen
  with nothing else to do. Make it explain the first action, with a button that does it.
- **Design for the "stuck" moment.** When the user hesitates, the interface should offer the answer — a tooltip on
  focus, an example value in the placeholder.
- **Make errors instructive.** Cause, fix, preserved input. This is the one message that will definitely be read.
- **Provide a "show me" instead of a "tell me"** — a sample document, a demo project, a prefilled example.

### Don't

- Don't gate the product behind a tutorial. A 6-step modal tour is a manual with worse UX.
- Don't put essential instructions in a help centre and link to it from step one.
- Don't show all hints at once. Twelve tooltips is a manual again, just scattered.
- Don't rely on placeholder text as the only label — it disappears exactly when the user needs it.
- Don't assume a returning user wants the tour again. Persist dismissal.

## Pattern

```html
<!-- Empty state is the onboarding: it explains and acts in one place -->
<section class="empty">
  <h2>No projects yet</h2>
  <p>Projects hold your files, notes, and teammates. Start with a template or a blank one.</p>
  <div class="empty__actions">
    <button class="btn btn--primary">Create project</button>
    <a class="link" href="/templates">Browse templates</a>
  </div>
</section>
```

```css
.empty { display: grid; gap: var(--space-3); justify-items: start;
         padding: var(--space-12) var(--space-6); text-align: start;
         border: 1px dashed var(--border); border-radius: var(--radius-lg); }
.empty__actions { display: flex; align-items: center; gap: var(--space-4); }
```

```html
<!-- Hint at the point of need, not before the task -->
<div class="field">
  <label for="slug">Project URL</label>
  <input id="slug" aria-describedby="slug-hint" placeholder="my-project">
  <p id="slug-hint" class="hint">Lowercase letters, numbers, and dashes. You can change it later.</p>
</div>
```

```html
<!-- Error that teaches: cause, fix, preserved input -->
<div class="field">
  <label for="card">Card number</label>
  <input id="card" aria-invalid="true" aria-describedby="card-err" value="4242 4242 4242 424">
  <p id="card-err" class="field__error">That number is one digit short. It should be 16 digits.</p>
</div>
```

## Audit question

> What can a user accomplish on their first screen without reading anything? If the answer is "nothing", the manual is
> in the wrong place.

## Further reading

| Reading | Author / Publisher |
|---|---|
| [Onboarding for Active Users](https://lawsofux.com/articles/2024/onboarding-for-active-users/) | Jon Yablonski \| Laws of UX |
| [Paradox of the Active User](https://www.nngroup.com/articles/paradox-of-the-active-user/) | Nielsen Norman Group |
| [Paradox of the Active User [PDF]](https://www.researchgate.net/publication/262322669_Paradox_of_the_active_user) | ResearchGate |
| [The Paradox of Active Users [PDF]](https://www.researchgate.net/publication/285543245_The_paradox_of_active_users) | ResearchGate |

---

**Site page** · [lawsofux.com/paradox-of-the-active-user](https://lawsofux.com/paradox-of-the-active-user/)
