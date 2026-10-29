---
law: Postel's Law
slug: postels-law
index: 24
category: robustness
lever: input tolerance
audit_weight: high
source: https://en.wikipedia.org/wiki/Robustness_principle
---

# 24 · Postel's Law

> Be liberal in what you accept, and conservative in what you send.

**Category** Robustness · **Lever** Input tolerance · **Audit weight** High

## What the site says

### Takeaways

1. Be empathetic to, flexible about, and tolerant of any of the various actions the user could take or any input they might provide.
2. Anticipate virtually anything in terms of input, access, and capability while providing a reliable and accessible interface.
3. The more we can anticipate and plan for in design, the more resilient the design will be.
4. Accept variable input from users, translating that input to meet your requirements, defining boundaries for input, and providing clear feedback to the user.

### Origins

Postel’s Law (also known as the Robustness Principle) was formulated by Jon Postel, an early pioneer of the Internet. The Law is a design guideline for software, specifically in regards to TCP and networks, and states “TCP implementations should follow a general principle of robustness: be conservative in what you do, be liberal in what you accept from others”. In other words, programs that send messages to other machines (or to other programs on the same machine) should conform completely to the specifications, but programs that receive messages should accept non-conformant input as long as the meaning is clear.

*Primary source cited on the site: [en.wikipedia.org](https://en.wikipedia.org/wiki/Robustness_principle)*

## Mechanism — why this happens

The robustness principle comes from protocol design (RFC 761, 1980; restated in RFC 1122): be **conservative in what you
send** and **liberal in what you accept**. The reasoning is about interoperability under partial failure — if every
implementation is strict about input, any small deviation breaks the whole network; if every implementation is tolerant
about input, the network keeps working.

For interfaces the translation is direct and very practical:

- **Liberal input.** Users type phone numbers with spaces, dashes, parentheses, or `+62`. They paste card numbers with
  trailing whitespace. They type `1 November 2026`, `01/11/2026`, or `2026-11-01`. A tolerant field accepts all of
  these and normalises them; a strict field rejects and blames the user.
- **Conservative output.** What you *display* and *send* should be canonical: one date format per locale, one phone
  format, one currency format, one casing convention. Inconsistency in output is what makes a product feel unreliable.

The interface version of the rule: **the machine adapts to the human on the way in; the human gets consistency on the
way out.**

**Important caveat.** Postel's law has a well-documented dark side, and it applies to UI too: being too liberal in
parsing creates ambiguity, and ambiguity is where security bugs live. If two different inputs normalise to the same
value, you have created a collision. Be liberal about *formatting*, strict about *validity*.

## Numbers that matter

| Quantity | Value | Consequence for the interface |
|---|---|---|
| Accepted phone formats | all common ones | Normalise on blur, not on keystroke |
| Accepted date inputs | ≥3 common formats | Parse then reformat to the canonical display |
| Paste support | required | Pasting is the fastest input method; blocking it is hostile |
| Output formats per field type | exactly 1 | One date format, one phone format, one currency format |
| Validation timing | on blur / on submit | Validating per keystroke punishes mid-typing states |

## Apply it

### Do

- **Accept formatted input and normalise it.** Strip spaces, dashes, and parentheses from phone and card numbers before
  validating; reformat for display.
- **Support paste everywhere**, including one-time codes (`autocomplete="one-time-code"` and no `maxlength` that cuts
  a pasted value).
- **Parse dates liberally, display them canonically.** Accept what the user types; show one format consistently.
- **Accept leading/trailing whitespace** and trim it silently. Rejecting `"  name"` is a bug, not validation.
- **Be strict about validity, liberal about format.** `"abc"` in an email field is invalid; `"Name@Example.com "` is valid
  and should be trimmed and lowercased.
- **Send canonical output**: consistent casing, consistent number and currency formatting, consistent date format.

### Don't

- Don't reject a valid value because of formatting. That is the single most common form failure.
- Don't validate on every keystroke; a half-typed email is not an error, it is a work in progress.
- Don't be liberal about *semantics*. Accept `+62 812-3456-7890`, but do not guess whether a 10-digit number is a phone
  or a postal code.
- Don't silently coerce ambiguous input. If two readings exist, ask.
- Don't let tolerant parsing create duplicate records — normalise to a canonical key before storing.

## Pattern

```html
<!-- Tolerant input, canonical output -->
<div class="field">
  <label for="phone">Phone</label>
  <input id="phone" type="tel" inputmode="tel" autocomplete="tel"
         placeholder="+62 812 3456 7890">
  <p class="hint">Any format is fine — we'll tidy it up.</p>
</div>
```

```js
// Liberal in: strip formatting, validate the digits
function normalisePhone(raw) {
  const digits = raw.replace(/[^\d+]/g, "");
  return digits.startsWith("+") ? digits : `+${digits}`;
}

// Conservative out: one canonical display format
function formatPhone(e164) {
  const m = e164.match(/^\+(\d{2})(\d{3})(\d{4})(\d+)$/);
  return m ? `+${m[1]} ${m[2]}-${m[3]}-${m[4]}` : e164;
}
```

```js
// Card: accept pasted, spaced, dashed — normalise once
const cardDigits = value.replace(/\D/g, "").slice(0, 19);
input.value = cardDigits.replace(/(.{4})/g, "$1 ").trim();
```

```html
<!-- One-time code: paste must work -->
<input inputmode="numeric" autocomplete="one-time-code" aria-label="6-digit code">
```

## Audit question

> Try to enter a valid value in the ugliest realistic format — spaces, dashes, parentheses, uppercase. Does the field
> accept it? Then check the display: is the same value shown in exactly one format everywhere?

## Further reading

| Reading | Author / Publisher |
|---|---|
| [Design Systems and Postel’s Law](https://markboulton.co.uk/journal/2016-05-17.design-systems-and-postels-law/) | Mark Boulton |
| [Robustness and Least Power](https://adactio.com/journal/14327) | Adactio |
| [Your Website has Two Faces](https://alistapart.com/article/your-website-has-two-faces) | A List Apart |
| [Design with Difficult Data](https://alistapart.com/article/design-with-difficult-data/) | Steven Garrity |
| [Robustness Principle](https://en.wikipedia.org/wiki/Robustness_principle) | Wikipedia |

---

**Site page** · [lawsofux.com/postels-law](https://lawsofux.com/postels-law/)
