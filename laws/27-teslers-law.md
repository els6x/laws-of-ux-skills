---
law: Tesler's Law
slug: teslers-law
index: 27
category: complexity
lever: who carries the complexity
audit_weight: critical
source: https://en.wikipedia.org/wiki/Law_of_conservation_of_complexity
---

# 27 · Tesler's Law

> Tesler’s Law, also known as The Law of Conservation of Complexity, states that for any system there is a certain amount of complexity which cannot be reduced.

**Category** Complexity · **Lever** Who carries the complexity · **Audit weight** Critical

## What the site says

### Takeaways

1. All processes have a core of complexity that cannot be designed away and therefore must be assumed by either the system or the user.
2. Ensure as much as possible of the burden is lifted from users by dealing with inherent complexity during design and development.
3. Remember to not build products and services for an idealized, rational user, because people don’t always behave rationally in real life.
4. Make guidance accessible and fit within the context of use so that it can help these active new users, no matter what path they choose to take (e.g., tooltips with helpful information).

### Origins

While working for Xerox PARC in the mid-1980s, Larry Tesler realized that the way users interact with applications was just as important as the application itself. The book Designing for Interaction by Dan Saffer, includes an interview with Larry Tesler that describes the law of conservation of complexity. The interview is popular among user experience and interaction designers. Larry Tesler argues that, in most cases, an engineer should spend an extra week reducing the complexity of an application versus making millions of users spend an extra minute using the program because of the extra complexity. However, Bruce Tognazzini proposes that people resist reductions to the amount of complexity in their lives. Thus, when an application is simplified, users begin attempting more complex tasks.

*Primary source cited on the site: [en.wikipedia.org](https://en.wikipedia.org/wiki/Law_of_conservation_of_complexity)*

## Mechanism — why this happens

Complexity is conserved. Every process has an irreducible amount of it, and the only real decision is **who absorbs it**:
the user, the designer, or the system. It cannot be deleted, only relocated — and relocating it is the entire job of
design.

Three carriers, and the trade-off between them:

| Carrier | What it costs | When it is right |
|---|---|---|
| **User** | Time, errors, learning, frustration | Only when the complexity is the product (professional tools, creative software) |
| **Designer** | Upfront work: defaults, detection, sensible constraints | Almost always — this is the default choice |
| **System** | Compute, storage, background jobs, automation | When the machine can genuinely infer or precompute |

The failure mode is **complexity transfer disguised as simplification**. Moving a setting from the main screen into a
nested menu does not remove complexity; it moves it into discovery. Hiding an advanced option behind a "More" link is
only a simplification if the user did not need it.

Tesler's own framing was about the engineer/user boundary at Xerox PARC: the engineer's time is expensive once, the
user's time is expensive every time. That asymmetry is the argument for absorbing complexity in design — a week of
engineering can save a second per user per day, forever.

## Numbers that matter

| Quantity | Value | Consequence for the interface |
|---|---|---|
| Settings exposed on the main screen | as few as possible | Every exposed setting is complexity transferred to the user |
| Defaults that must be right | 100% of the common case | A wrong default is complexity with interest |
| Steps the system can absorb | all that can be inferred | Detect, prefill, remember |
| Advanced options | 1 click away | Reachable, not prominent |
| Cost asymmetry | engineer once vs user every time | Absorb it in design |

## Apply it

### Do

- **Absorb complexity into defaults.** Detect locale, timezone, currency, and file type. Prefill from the user's data.
- **Absorb it into constraints.** A date picker is less complex than a free-text date field, because the system carries
  the format.
- **Absorb it into automation.** Background sync, auto-save, auto-formatting. The user should not manage what the system
  can manage.
- **Expose complexity only where it is the value.** A photo editor should expose layer blending; a to-do app should not.
- **Ask "who pays for this?" for every setting.** If the answer is "the user, every time", find another carrier.
- **Make the advanced path real, not decorative.** If you hide it, it must still be findable and complete.

### Don't

- Don't call hiding a feature "simplifying". That is relocation, and it has a discovery cost.
- Don't expose a setting because the backend has a parameter. The database schema is not the interface.
- Don't put complexity on the user to keep engineering simple. That trade is almost always wrong at scale.
- Don't remove the escape hatch entirely. Power users need the advanced path, or they leave.
- Don't confuse *fewer controls* with *less complexity*. A single control that requires a manual is worse than five
  obvious ones.

## Pattern

```html
<!-- Bad: complexity transferred to the user as a raw setting -->
<label for="tz">Timezone (IANA)</label>
<input id="tz" placeholder="Asia/Jakarta">

<!-- Better: the system absorbs it, the user confirms -->
<label for="tz">Timezone</label>
<select id="tz" autocomplete="off">
  <option selected>Asia/Jakarta (GMT+7) — detected</option>
  <!-- ... -->
</select>
```

```js
// Absorb complexity: detect instead of ask
const tz = Intl.DateTimeFormat().resolvedOptions().timeZone;
const currency = new Intl.NumberFormat(undefined, { style: "currency", currency: "IDR" });
```

```html
<!-- Advanced complexity stays reachable, one click away -->
<details class="advanced">
  <summary>Advanced</summary>
  <div class="advanced__body">
    <label><input type="checkbox"> Use custom SMTP</label>
    <label><input type="checkbox"> Disable automatic retries</label>
  </div>
</details>
```

```css
.advanced { border-block-start: 1px solid var(--border); padding-block-start: var(--space-4); }
.advanced summary { cursor: pointer; color: var(--text-secondary); font-size: var(--text-sm); }
.advanced__body { display: grid; gap: var(--space-3); padding-block-start: var(--space-4); }
```

## Audit question

> For every control on the screen: who is carrying this complexity — the user, the design, or the system? If the answer
> is "the user" and the setting is not the product's core value, it belongs somewhere else.

## Further reading

| Reading | Author / Publisher |
|---|---|
| [Tesler’s Law [article]](https://lawsofux.com/articles/2024/teslers-law/) | Jon Yablonski \| Laws of UX |
| [Tesler’s Law: Shift Complexity to Simplify UX [video]](https://www.nngroup.com/videos/teslers-law/) | Lola Famulegun \| Nielsen Norman Group |
| [Why Life Can’t Be Simpler](https://fs.blog/2020/10/why-life-cant-be-simpler/) | Farnam Street |
| [8 Design Guidelines for Complex Applications](https://www.nngroup.com/articles/complex-application-design/) | Kate Kaplan \| Nielsen Norman Group |
| [Explaining the Law of Conservation of Complexity](http://humanist.co/blog/law-of-conservation-of-complexity/) | Michael Calleia \| Humanist.co |
| [Controls are Choices](https://medium.com/@odannyboy/controls-are-choices-7de90363d0dd) | Dan Saffer \| Medium.com |
| [Simplicity is Overrated](https://blog.marvelapp.com/simplicity-is-overrated/) | Gabriel Colombo \| Marvel |
| [Nobody Wants To Use Your Product](https://www.smashingmagazine.com/2016/01/nobody-wants-use-your-product/) | Goran Peuc \| Smashing Magazine |
| [Law of Conservation of Complexity on Wikipedia](https://en.wikipedia.org/wiki/Law_of_conservation_of_complexity) | Wikipedia |

---

**Site page** · [lawsofux.com/teslers-law](https://lawsofux.com/teslers-law/)
