---
law: Parkinson's Law
slug: parkinsons-law
index: 22
category: behaviour
lever: time and constraint
audit_weight: medium
source: https://en.wikipedia.org/wiki/Parkinson%27s_law
---

# 22 · Parkinson's Law

> Any task will inflate until all of the available time is spent.

**Category** Behaviour · **Lever** Time and constraint · **Audit weight** Medium

## What the site says

### Takeaways

1. Limit the time it takes to complete a task to what users expect it’ll take.
2. Reducing the actual duration to complete a task from the expected duration will improve the overall user experience.
3. Leverage features such as autofill to save the user time when providing critical information within forms. This allows for quick completion of purchases, bookings and other such functions while preventing task inflation.

### Origins

Articulated by Cyril Northcote Parkinson as part of the first sentence of a humorous essay published in The Economist in 1955 and since republished online, it was reprinted with other essays in the book Parkinson’s Law: The Pursuit of Progress (London, John Murray, 1958). He derived the dictum from his extensive experience in the British Civil Service.

*Primary source cited on the site: [en.wikipedia.org](https://en.wikipedia.org/wiki/Parkinson%27s_law)*

## Mechanism — why this happens

Parkinson's observation was about bureaucracy, but the mechanism generalises: **work expands to fill the resources
allocated to it**, because effort is elastic and there is no natural stopping point. Given more time, people refine;
given more space, people fill it; given more options, people deliberate longer.

In interfaces the law shows up in three concrete places:

1. **Time.** A task with no visible end takes as long as the user is willing to give it. A task with a visible end —
   "3 steps, about 2 minutes" — is finished faster and abandoned less.
2. **Space.** A text field sized for a paragraph invites a paragraph. A field sized for a sentence gets a sentence.
3. **Choice.** A form with 20 optional fields will be filled slowly, partially, and often abandoned, even though only
   4 fields matter.

The design lever is therefore **constraint as a service**: the interface decides how much time, space, and attention the
task deserves, and communicates that decision to the user.

## Numbers that matter

| Quantity | Value | Consequence for the interface |
|---|---|---|
| Visible time estimate | shown up front | Cuts abandonment; users budget attention |
| Required fields | as few as possible | Every optional field is time the user must decide about |
| Textarea rows | match expected input | Oversized inputs invite oversized answers |
| Steps in a first-run flow | 1–3 | Longer flows expand to fill the patience available |
| Autofill / paste support | yes | The fastest way to shrink a task is to not ask |

## Apply it

### Do

- **State the cost up front**: "3 steps · about 2 minutes". A bounded task is a finishable task.
- **Make optional fields visually optional** and hide the truly optional ones behind "Add more". A visible optional
  field still costs a decision.
- **Size inputs to expected content.** A 1-row input for a name, a 3-row textarea for a comment, a 1-line field for a
  URL. Size is a prompt.
- **Autofill what you can** — address, card, email — and support paste everywhere, including one-time codes.
- **Set a default and let the user move on.** A pre-selected option converts an open question into a confirm.
- **Give the task a finish line** and celebrate it briefly. Without an end, effort keeps expanding.

### Don't

- Don't leave a task open-ended ("customise your workspace") with no completion state.
- Don't pad flows with optional steps to seem thorough. Thoroughness is the enemy of completion.
- Don't make a textarea huge "to be safe"; it reads as "write an essay".
- Don't put a timer on the user unless the deadline is real. Fake urgency is a bias exploit (see `04-cognitive-bias.md`).
- Don't assume a shorter flow is always better — a flow that is short but ambiguous takes longer.

## Pattern

```html
<!-- Bound the task: the user knows the cost before starting -->
<header class="flow-head">
  <h1>Create your workspace</h1>
  <p class="flow-head__meta">3 steps · about 2 minutes</p>
</header>
```

```css
.flow-head__meta { color: var(--text-secondary); font-size: var(--text-sm); }
```

```html
<!-- Size the input to the content it expects -->
<label for="name">Workspace name</label>
<input id="name" maxlength="40" placeholder="Acme">

<label for="note">What is this workspace for? <span class="optional">(optional)</span></label>
<textarea id="note" rows="2" maxlength="200"></textarea>
```

```css
.optional { color: var(--text-secondary); font-weight: 400; }
```

```html
<!-- Hide the optional tail instead of showing it as a decision -->
<details class="advanced">
  <summary>Add advanced settings</summary>
  <!-- region, retention, SSO ... -->
</details>
```

## Audit question

> Does the user know how long this will take before starting, and is every visible field something they must decide
> about? If a field is optional and visible, it is costing time.

## Further reading

| Reading | Author / Publisher |
|---|---|
| [Parkinson’s Law on Wikipedia](https://en.wikipedia.org/wiki/Parkinson%27s_law) | Wikipedia |
| [Parkinson’s Law: Why Constraints Are The Best Thing You Can Work With](https://medium.com/the-mission/parkinsons-law-why-constraints-are-the-best-thing-you-can-work-with-4fad6e0e91cf) | Louis Chew \| Medium.com |

---

**Site page** · [lawsofux.com/parkinsons-law](https://lawsofux.com/parkinsons-law/)
