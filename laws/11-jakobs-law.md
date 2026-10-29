---
law: Jakob's Law
slug: jakobs-law
index: 11
category: convention
lever: familiarity
audit_weight: high
source: https://www.nngroup.com/articles/jakobs-law/
---

# 11 · Jakob's Law

> Users spend most of their time on other sites. This means that users prefer your site to work the same way as all the other sites they already know.

**Category** Convention · **Lever** Borrowed familiarity · **Audit weight** High

## What the site says

### Takeaways

1. Users will transfer expectations they have built around one familiar product to another that appears similar.
2. By leveraging existing mental models, we can create superior user experiences in which the users can focus on their tasks rather than on learning new models.
3. When making changes, minimize discord by empowering users to continue using a familiar version for a limited time.

### Origins

Jakob’s Law was coined by Jakob Nielsen, a User Advocate and principal of the Nielsen Norman Group which he co-founded with Dr. Donald A. Norman (former VP of research at Apple Computer). Dr. Nielsen established the ‘discount usability engineering’ movement for fast and cheap improvements of user interfaces and has invented several usability methods, including heuristic evaluation.

*Primary source cited on the site: [nngroup.com](https://www.nngroup.com/people/jakob-nielsen/)*

## Mechanism — why this happens

Every interface is learned, and learning is expensive. Users arrive with a large, mostly implicit library of patterns
built from every other product they use: the cart is top-right, the logo goes home, the search field has a magnifier,
swiping back goes back. That library is a **mental model of software in general**, and it is the cheapest thing you can
borrow.

Jakob's law is therefore not "be boring". It is an economic statement: **familiarity is a discount on learning cost**,
and you should spend your novelty budget where it produces value, not on re-teaching the location of the close button.

The useful refinement is the *convention–innovation trade-off*:

| Situation | Follow convention | Deviate |
|---|---|---|
| The pattern is universal (back, close, cart, search) | Always | Never |
| The pattern is common in your category | Yes, by default | Only with a clear, demonstrable gain |
| The pattern is contested or new | Either | If your version is measurably better |
| The pattern is the product's differentiator | No | Yes — but teach it explicitly |

The test for a deviation is not "is it nicer?" but **"can a new user succeed without being taught?"** If the answer is
no and the task is not the differentiator, you have bought novelty with someone else's time.

## Numbers that matter

| Quantity | Value | Consequence for the interface |
|---|---|---|
| Time on other sites | the majority of users' web time | Their model is formed elsewhere, not on yours |
| Learning cost of a new pattern | one failed attempt, typically | Failures are cheap once, expensive at scale |
| Safe-to-innovate surface | the differentiator only | Spend novelty there, nowhere else |
| Convention violations per flow | 0–1 | Two is a usability problem, three is a maze |

## Apply it

### Do

- **Keep the universal furniture where it is**: logo → home, top-right account, cart icon, magnifier for search,
  back arrow top-left on mobile, `Esc` closes a modal.
- **Copy the interaction, not the pixels.** What matters is that a click on the row opens the item, not that your row
  looks like someone else's.
- **Match category conventions even when you dislike them.** A booking flow that works like every other booking flow
  is a feature.
- **Innovate in one place at a time**, and make that place obviously better. One novel interaction per product is a
  statement; five is a maze.
- **Teach deviations explicitly** when you must make them: a short inline hint at the point of first use.
- **Reuse platform patterns** (native pickers, native share sheets, OS back gesture). Users' models are strongest at the OS level.

### Don't

- Don't redesign standard controls for brand reasons. A custom scrollbar or a custom checkbox is a cost with no upside.
- Don't move primary navigation to a novel location without strong evidence.
- Don't assume your users only use your product. They use ten others with the same patterns.
- Don't confuse "our old version" with "convention". Your legacy layout is not a mental model; the web's is.
- Don't innovate on the checkout. Ever. The conversion cost is measurable and the upside is not.

## Pattern

```html
<!-- Conventional shell: the parts users do not want to learn -->
<header class="app-header">
  <a href="/" class="app-header__brand" aria-label="Acme home">Acme</a>
  <nav aria-label="Main"><!-- ≤7 items --></nav>
  <form role="search" class="app-header__search">
    <input type="search" placeholder="Search" aria-label="Search">
  </form>
  <a href="/cart" class="app-header__cart" aria-label="Cart, 2 items">Cart (2)</a>
  <a href="/account" class="app-header__account" aria-label="Account">Account</a>
</header>
```

```css
/* Conventional layout, unconventional only where it earns its keep */
.app-header {
  display: flex; align-items: center; gap: var(--space-6);
  padding-block: var(--space-3);
  border-block-end: 1px solid var(--border);
}
.app-header__search { margin-inline-start: auto; }
```

```html
<!-- If you deviate, label it. This is the cost of innovation, paid once. -->
<button class="btn" aria-describedby="tip-publish">
  Publish
</button>
<p id="tip-publish" class="hint">
  Publishing sends a live link to your team. You can unpublish any time.
</p>
```

## Audit question

> Take every interactive element on the primary path and ask: would a user who has never seen this product know what it
> does without a tooltip? Every "no" is a place where you are charging the user for your novelty.

## Further reading

| Reading | Author / Publisher |
|---|---|
| [Jakob’s Law of Internet User Experience](https://www.nngroup.com/videos/jakobs-law-internet-ux/) | Nielsen Norman Group |
| [The Power Law of Learning: Consistency vs. Innovation in User Interfaces](https://www.nngroup.com/articles/power-law-learning/) | Nielsen Norman Group |
| [Familiar vs Novel](https://lawsofux.com/articles/2024/familiar-vs-novel/) | Jon Yablonski \| Laws of UX |
| [Top 10 Mistakes in Web Design](https://www.nngroup.com/articles/top-10-mistakes-web-design/) | Nielsen Norman Group |
| [End of Web Design](https://www.nngroup.com/articles/end-of-web-design/) | Nielsen Norman Group |

---

**Site page** · [lawsofux.com/jakobs-law](https://lawsofux.com/jakobs-law/)
