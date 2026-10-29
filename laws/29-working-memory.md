---
law: Working Memory
slug: working-memory
index: 29
category: memory
lever: holding capacity over time
audit_weight: critical
source: https://en.wikipedia.org/wiki/Working_memory
---

# 29 · Working Memory

> A cognitive system that temporarily holds and manipulates information needed to complete tasks.

**Category** Memory · **Lever** Holding capacity over time · **Audit weight** Critical

## What the site says

### Takeaways

1. Working memory is limited to 4-7 chunks of information at any given moment with each chunk fades after 20-30 seconds. We use it to keep track of information in order to achieve tasks but we often have trouble remembering what information we’ve already seen. Designers must be mindful of this limit when displaying information to users and ensure it’s both necessary and relevant.
2. Our brains are good at recognizing something we’ve seen before but not at keeping new information ready to be used. We can support recognition over recall by making it clear what information has already been viewed (e.g. visually differentiating visited links and providing breadcrumbs links).
3. Place burden of memory on the system, not the user. We can lessen the burden of memorizing critical information by carrying it over from screen to screen when necessary (e.g. comparison tables that make comparing multiple items easy).

### Origins

The term “working memory” was coined by George A. Miller, Eugene Galanter, and Karl H. Pribram, and was used in the 1960s in the context of theories that likened the mind to a computer. In 1968, Richard C. Atkinson and Richard M. Shiffrin used the term to describe their “short-term store”. The term short-term store was the name previously used for working memory. Other suggested names were short-term memory, primary memory, immediate memory, operant memory, and provisional memory. Short-term memory is the ability to remember information over a brief period (in the order of seconds). Most theorists today use the concept of working memory to replace or include the older concept of short-term memory, marking a stronger emphasis on the notion of manipulating information rather than mere maintenance.The earliest mention of experiments on the neural basis of working memory can be traced back to more than 100 years ago, when Eduard Hitzig and Sir David Ferrier described ablation experiments of the prefrontal cortex (PFC); they concluded that the frontal cortex was important for cognitive rather than sensory processes. In 1935 and 1936, Carlyle Jacobsen and colleagues were the first to show the deleterious effect of prefrontal ablation on delayed response.

*Primary source cited on the site: [en.wikipedia.org](https://en.wikipedia.org/wiki/Working_memory)*

## Mechanism — why this happens

Working memory is the workspace where the current task lives: the number you just read, the choice you made last screen,
the reason you are on this page. Baddeley and Hitch's multicomponent model splits it into:

| Component | What it holds | Design relevance |
|---|---|---|
| **Phonological loop** | Verbal/acoustic information, ~2 s of speech | Why labels read aloud must be short; why "repeat after me" fails |
| **Visuospatial sketchpad** | Visual and spatial information | Why layout position is remembered better than text |
| **Central executive** | Attention allocation, task switching | Why interruptions are so expensive |
| **Episodic buffer** | Binding across modalities and time | Why a consistent visual context helps recall |

Two properties drive every design rule here:

1. **Capacity is small.** Miller's 7 ± 2 was the historical figure; Cowan's estimate of **~4 chunks** is what holds
   under realistic load. Four is the number to design against.
2. **Contents decay without rehearsal.** Without rehearsal, items fade in roughly **20–30 seconds**, and any
   interruption accelerates the loss. This is why a modal in the middle of a form is expensive: it evicts the contents.

The design implication is blunt: **the interface should not require the user to hold anything it can show.** Every
requirement to remember is a bet against a 4-slot, 30-second store.

## Numbers that matter

| Quantity | Value | Consequence for the interface |
|---|---|---|
| Capacity (Cowan) | **~4 chunks** | The budget for any single step |
| Capacity (Miller) | 7 ± 2 | Historical ceiling, not a target |
| Decay without rehearsal | **20–30 s** | Anything off-screen must be re-derivable |
| Interruption cost | full re-read of the step | Modals mid-flow are expensive |
| Chunk size in a group | 3–5 | Keeps a group inside the budget |
| Labels read aloud | ≤5 words | Longer labels exceed the phonological loop's comfort |

## Apply it

### Do

- **Show, don't require recall.** Selected plan, cart total, entered email, previous answers — all visible on the
  current screen.
- **Persist state across steps.** A back button should restore the screen exactly, not ask the user to reconstruct it.
- **Keep labels short and concrete.** The phonological loop holds about two seconds of speech; a 12-word label is gone
  before it is used.
- **Avoid interruptions in the middle of a task.** Move modals, upsells, and notifications to natural boundaries.
- **Use recognition over recall.** Pickers, recent items, and suggestions beat blank fields.
- **Give a review step** before irreversible actions. Recognition is nearly free; recall is not.

### Don't

- Don't put instructions on one screen and the fields on another.
- Don't require the user to compare values they can no longer see; put them side by side.
- Don't use a code the user must memorise across screens. Show it, or copy it for them.
- Don't interrupt a form with a modal, even a "helpful" one.
- Don't assume a returning user remembers the previous session. Show state, not a blank slate.

## Pattern

```html
<!-- Persistent context: the user never has to remember what they chose -->
<aside class="context" aria-label="Order summary">
  <h2 class="context__title">Your order</h2>
  <dl class="context__list">
    <div><dt>Plan</dt><dd>Pro</dd></div>
    <div><dt>Billing</dt><dd>Yearly</dd></div>
    <div><dt>Seats</dt><dd>5</dd></div>
    <div><dt>Due today</dt><dd>$228</dd></div>
  </dl>
</aside>
```

```css
.context { position: sticky; inset-block-start: var(--space-6); padding: var(--space-6);
           background: var(--surface-raised); border-radius: var(--radius-md); }
.context__list { display: grid; gap: var(--space-2); margin: 0; }
.context__list > div { display: flex; justify-content: space-between; gap: var(--space-4); }
.context__list dd { margin: 0; font-weight: 600; }
```

```html
<!-- Recognition over recall: recent values, one click -->
<label for="project">Project</label>
<input id="project" list="recent-projects" autocomplete="off">
<datalist id="recent-projects">
  <option value="Website redesign"></option>
  <option value="Q4 campaign"></option>
  <option value="Mobile onboarding"></option>
</datalist>
```

```js
// Persist across steps so back does not require reconstruction
const draft = JSON.parse(sessionStorage.getItem("checkout") || "{}");
for (const [name, value] of Object.entries(draft)) {
  const el = document.querySelector(`[name="${name}"]`);
  if (el) el.value = value;
}
```

## Audit question

> Walk the flow and note every moment the user must remember something that is not on screen. Each one is a bet against
> a four-slot, thirty-second store.

## Further reading

| Reading | Author / Publisher |
|---|---|
| [Working Memory and External Memory](https://www.nngroup.com/articles/working-memory-external-memory/) | Raluca Budiu \| Nielsen Norman Group |
| [Working Memory and External Memory [Video]](https://www.youtube.com/watch?v=qV5gSyfi4p8) | Raluca Budiu \| Nielsen Norman Group |
| [Reducing Cognitive Overload For A Better User Experience](https://www.smashingmagazine.com/2016/09/reducing-cognitive-overload-for-a-better-user-experience/) | Danny Halarewich \| Smashing Magazine |

---

**Site page** · [lawsofux.com/working-memory](https://lawsofux.com/working-memory/)
