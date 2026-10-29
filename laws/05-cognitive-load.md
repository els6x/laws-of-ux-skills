---
law: Cognitive Load
slug: cognitive-load
index: 5
category: cognition
lever: mental effort
audit_weight: critical
source: https://en.wikipedia.org/wiki/Cognitive_load
---

# 05 · Cognitive Load

> The amount of mental resources needed to understand and interact with an interface.

**Category** Cognition · **Lever** Mental effort per step · **Audit weight** Critical

## What the site says

### Takeaways

1. When the amount of information coming in exceeds the space we have available, we struggle mentally to keep up — tasks become more difficult, details are missed, and we begin to feel overwhelmed.
2. Intrinsic cognitive load refers to the effort required by users to carry around information relevant to their goal, absorb new information and keep track of their goals.
3. Extraneous cognitive load refers to the mental processing that takes up resources but doesn't help users understand the content of an interface (e.g. distracting or unnecessary design elements).

### Origins

Cognitive load theory was developed in the late 1980s by John Sweller out of a study of problem solving and was in many ways an expansion on the information processing theories of George Miller. Sweller argued that instructional design can be used to reduce cognitive load in learners, culminating in his 1988 publication of “Cognitive Load Theory, Learning Difficulty, and Instructional Design”. Researchers later on developed a way to measure perceived mental effort which is indicative of cognitive load.

*Primary source cited on the site: [en.wikipedia.org](https://en.wikipedia.org/wiki/Cognitive_load)*

## Mechanism — why this happens

Sweller's cognitive load theory splits load into three kinds, and the split is what makes it usable:

| Type | What it is | What design can do |
|---|---|---|
| **Intrinsic** | Inherent difficulty of the material (tax law is harder than a name field) | Sequence it, split it, scaffold it — cannot remove it |
| **Extraneous** | Load caused by *how* the material is presented (bad layout, unclear labels, duplication) | Remove it entirely — this is the designer's job |
| **Germane** | Effort that builds understanding (schema construction) | Protect it; do not optimise it away |

The rule that follows: **you may not be able to make the task easy, but you can always stop making it harder.**
Extraneous load is pure waste, and it is almost always the largest term in a bad interface.

Three well-documented effects tell you where it comes from:

- **Split-attention effect** — when related information is in two places (a label far from its field, a legend far from
  the chart), the user must hold one while looking at the other. Load comes from the *distance*.
- **Redundancy effect** — repeating the same information in two formats (a paragraph and an identical bullet list) adds
  load instead of reinforcing. Duplication is not clarity.
- **Worked-example effect** — novices learn faster from a completed example than from a problem to solve. Show the
  filled-in state before asking for input.

## Numbers that matter

| Quantity | Value | Consequence for the interface |
|---|---|---|
| Working memory capacity | ~4 chunks (Cowan) | The hard ceiling every step is competing for |
| Decay without rehearsal | ~20–30 seconds | Anything not on screen must be re-derivable, not remembered |
| Fields per step (practical) | 3–7 | Beyond this, completion drops and errors rise |
| Primary actions per screen | 1 | Two primaries means the user must choose under uncertainty |

## Apply it

### Do

- **Put labels next to fields, not in a legend above the form.** Split-attention is the most common extraneous load in
  forms, and the cheapest to fix.
- **Remove duplicate explanation.** If the helper text says the same thing as the placeholder, delete one.
- **One primary action per screen.** Secondary actions get lower visual weight or move to a menu.
- **Externalise memory.** Show the selected plan, the cart total, the entered email — never make the user remember what
  they chose two steps ago.
- **Sequence intrinsic load.** Teach the concept before asking the user to act on it; three easy screens beat one hard one.
- **Use a worked example for anything novel.** A filled-in sample row is worth a paragraph of instructions.
- **Respect the expertise reversal effect**: hide beginner scaffolding from expert users (advanced mode, "skip guide").

### Don't

- Don't add "helpful" tooltips for every field. Ten tooltips is more load than zero.
- Don't decorate the task with choices that are not the task (theme pickers during checkout).
- Don't split a single decision across two screens with a back button — that converts load into re-work.
- Don't use jargon the user must decode ("provisioning", "entitlement", "SSO assertion"). Use the user's word.
- Don't confuse *simple-looking* with *low-load*: hidden options the user must discover also cost.

## Pattern

```html
<!-- Bad: split attention — legend far from the fields -->
<p class="hint">Enter your card number, expiry, and CVC.</p>
<div class="form">
  <input placeholder="Card"><input placeholder="MM/YY"><input placeholder="CVC">
</div>

<!-- Better: label adjacent, no legend to hold in memory -->
<div class="field">
  <label for="cc">Card number</label>
  <input id="cc" inputmode="numeric" autocomplete="cc-number" placeholder="4242 4242 4242 4242">
</div>
<div class="row">
  <div class="field">
    <label for="exp">Expiry</label>
    <input id="exp" autocomplete="cc-exp" placeholder="MM/YY">
  </div>
  <div class="field">
    <label for="cvc">CVC</label>
    <input id="cvc" inputmode="numeric" autocomplete="cc-csc" placeholder="123">
  </div>
</div>
```

```css
.field { display: grid; gap: var(--space-2); }
.field label { font-size: var(--text-sm); font-weight: 500; }
.row { display: grid; grid-template-columns: 1fr 1fr; gap: var(--space-4); }
```

## Audit question

> How many things must the user hold in their head at the same time to finish this step? If more than one, remove
> something or show it on screen.

## Further reading

| Reading | Author / Publisher |
|---|---|
| [What Is Cognitive Load? [Video]](https://www.nngroup.com/videos/cognitive-load/) | Maddie Brown \| Nielsen Norman Group |
| [Ease Cognitive Overload in UX Design](https://mailchimp.com/resources/cognitive-overload/) | Mailchimp |
| [Minimize Cognitive Load to Maximize Usability](https://www.nngroup.com/articles/minimize-cognitive-load/) | Kathryn Whitenton \| Nielsen Norman Group |
| [Design Principles for Reducing Cognitive Load](https://lawsofux.com/articles/2015/design-principles-for-reducing-cognitive-load/) | Jon Yablonski \| Laws of UX |
| [Reducing Cognitive Overload For A Better User Experience](https://www.smashingmagazine.com/2016/09/reducing-cognitive-overload-for-a-better-user-experience/) | Danny Halarewich \| Smashing Magazine |

---

**Site page** · [lawsofux.com/cognitive-load](https://lawsofux.com/cognitive-load/)
