---
law: Zeigarnik Effect
slug: zeigarnik-effect
index: 30
category: motivation
lever: unfinished state
audit_weight: medium
source: https://en.wikipedia.org/wiki/Zeigarnik_effect
---

# 30 · Zeigarnik Effect

> People remember uncompleted or interrupted tasks better than completed tasks.

**Category** Motivation · **Lever** Unfinished state · **Audit weight** Medium

## What the site says

### Takeaways

1. Invite content discovery by providing clear signifiers of additional content.
2. Providing artificial progress towards a goal will help to ensure users are more likely to have the motivation to complete that task.
3. Provide a clear indication of progress in order to motivate users to complete tasks.

### Origins

Bluma Wulfovna Zeigarnik (1900 – 1988) was a Soviet psychologist and psychiatrist, a member of the Berlin School of experimental psychology and Vygotsky Circle. She discovered the Zeigarnik effect and contributed to the establishment of experimental psychopathology as a separate discipline in the Soviet Union in the post-World War II period. In the 1920s she conducted a study on memory, in which she compared memory in relation to incomplete and complete tasks. She had found that incomplete tasks are easier to remember than successful ones. This is now known as the Zeigarnik effect. She later began working at the Institute of Higher Nervous Activity which is where she would meet her next big influence Vygowsky, and become a part of his circle of scientists. It was also there that Zeigarnik founded the Department of Psychology. During that time, Zeigarnik received the Lewin Memorial Award in 1983 for her psychological research.

*Primary source cited on the site: [en.wikipedia.org](https://en.wikipedia.org/wiki/Bluma_Zeigarnik)*

## Mechanism — why this happens

Unfinished tasks stay active in memory; completed ones are released. Bluma Zeigarnik's observation (from Kurt Lewin's
group) was that waiters remembered unpaid orders and forgot paid ones. The mechanism is a kind of **open loop**: an
incomplete goal keeps a representation active, and that activation creates a mild tension that motivates return.

For design, the effect is the basis of every progress pattern that works:

- A partially filled profile ("3 of 5 steps complete") pulls the user back.
- A checklist with two items left is harder to abandon than one with no structure.
- A saved draft with a visible "continue where you left off" is more likely to be resumed.

But the effect has a sharp ethical edge, and it is worth stating plainly: **open loops can be manufactured**. Streak
counters, "your profile is 80% complete" nudges that never reach 100%, and badge progress that requires spending are all
Zeigarnik exploits. The test is the same as for cognitive bias (see `04-cognitive-bias.md`): does the loop correspond to
something the user actually wants to finish?

## Numbers that matter

| Quantity | Value | Consequence for the interface |
|---|---|---|
| Items left visible | 1–3 | More becomes overwhelming, fewer loses the pull |
| Checklist completion threshold | start with 1–2 done | A 0% checklist has no open-loop pull |
| Resume prompt window | next session | The loop decays; prompt while it is still warm |
| Artificial loops | 0 | Manufactured incompleteness is a dark pattern |

## Apply it

### Do

- **Make progress visible and specific.** "2 of 5 done" creates a loop; "setup incomplete" does not.
- **Start the user with one item already done.** A checklist at 20% is more compelling than one at 0% (this is also the
  goal-gradient head start — see `09-goal-gradient-effect.md`).
- **Offer resume, not restart.** "Continue where you left off" respects the open loop; a blank form closes it by force.
- **Auto-save drafts** and surface them. An unsaved draft is an open loop the user cannot see, which produces anxiety
  rather than motivation.
- **Close loops explicitly.** When the task is done, show completion and stop prompting. A loop that never closes
  becomes noise.
- **Use it for the user's own goals**, not for engagement metrics.

### Don't

- Don't invent incompleteness. A profile that can never reach 100% is a manipulation.
- Don't use streak loss as a threat. "You'll lose your 47-day streak" is coercion, not motivation.
- Don't leave loops open by accident — a form that silently fails to save is the worst version of this effect.
- Don't stack loops. Five simultaneous "incomplete" indicators cancel each other and read as nagging.
- Don't prompt about the same unfinished task forever. After two prompts, let it go.

## Pattern

```html
<!-- A real open loop: countable, closeable, tied to the user's goal -->
<section class="setup" aria-labelledby="setup-title">
  <h2 id="setup-title">Finish setting up Acme</h2>
  <p class="setup__meta">2 of 4 done</p>
  <ul class="checklist">
    <li class="checklist__item is-done">Create workspace</li>
    <li class="checklist__item is-done">Connect your domain</li>
    <li class="checklist__item">Invite a teammate <a class="link" href="/invite">Invite</a></li>
    <li class="checklist__item">Add a payment method <a class="link" href="/billing">Add</a></li>
  </ul>
</section>
```

```css
.setup { display: grid; gap: var(--space-3); padding: var(--space-6);
         border: 1px solid var(--border); border-radius: var(--radius-lg); }
.setup__meta { margin: 0; font-size: var(--text-sm); color: var(--text-secondary); }
.checklist { display: grid; gap: var(--space-2); margin: 0; padding: 0; list-style: none; }
.checklist__item { display: flex; align-items: center; justify-content: space-between; gap: var(--space-4);
                   padding-block: var(--space-2); }
.checklist__item.is-done { color: var(--text-secondary); text-decoration: line-through; }
```

```html
<!-- Resume, don't restart -->
<div class="resume" role="status">
  <p>You have an unsaved draft from yesterday.</p>
  <a class="btn btn--primary" href="/draft/42">Continue draft</a>
  <button class="btn btn--ghost">Start over</button>
</div>
```

```js
// Auto-save: an invisible open loop is anxiety, a visible one is motivation
let t;
editor.addEventListener("input", () => {
  clearTimeout(t);
  t = setTimeout(async () => {
    await fetch(`/api/draft/${id}`, { method: "PUT", body: editor.value });
    setStatus("Saved");
  }, 800);   // debounce, well inside the working-memory window
});
```

## Audit question

> Does every "incomplete" indicator on this screen correspond to something the user actually wants to finish, and can it
> be closed? If it cannot be closed, it is a manufactured loop.

## Further reading

| Reading | Author / Publisher |
|---|---|
| [How to Use the Zeigarnik Effect in UX](https://www.nngroup.com/videos/zeigarnik-effect/) | Feifei Liu \| Nielsen Norman Group |
| [Endowed progress effect: Give your users a head start](https://uxdesign.cc/endowed-progress-effect-give-your-users-a-head-start-97d52d8b0396) | Canvs Editorial \| UX Collective |
| [Moving the Finish Line: The Goal Gradient Hypothesis](https://fs.blog/2016/10/goal-gradient-hypothesis/) | Farnam Street |
| [The Zeigarnik Effect: Why it is so hard to leave things incomplete](https://medium.com/coffee-and-junk/design-psychology-zeigarnik-effect-a53688b7f6d1) | Abhishek Chakraborty \| Medium.com |
| [Zeigarnik Effect](http://coglode.com/gem/zeigarnik-effect) | Coglode |
| [Zeigarnik Effect on Wikipedia](https://en.wikipedia.org/wiki/Bluma_Zeigarnik) | Wikipedia |

---

**Site page** · [lawsofux.com/zeigarnik-effect](https://lawsofux.com/zeigarnik-effect/)
