---
law: Hick's Law
slug: hicks-law
index: 10
category: decision
lever: number of choices
audit_weight: critical
source: https://www.interaction-design.org/literature/article/hick-s-law-making-the-choice-easier-for-users
---

# 10 · Hick's Law

> The time it takes to make a decision increases with the number and complexity of choices.

**Category** Decision · **Lever** Number of choices · **Audit weight** Critical

## What the site says

### Takeaways

1. Minimize choices when response times are critical to decrease decision time.
2. Break complex tasks into smaller steps in order to decrease cognitive load.
3. Avoid overwhelming users by highlighting recommended options.
4. Use progressive onboarding to minimize cognitive load for new users.
5. Be careful not to simplify to the point of abstraction.

### Origins

Hick’s Law (or the Hick-Hyman Law) is named after a British and an American psychologist team of William Edmund Hick and Ray Hyman. In 1952, this pair set out to examine the relationship between the number of stimuli present and an individual’s reaction time to any given stimulus. As you would expect, the more stimuli to choose from, the longer it takes the user to make a decision on which one to interact with. Users bombarded with choices have to take time to interpret and decide, giving them work they don’t want.

*Primary source cited on the site: [interaction-design.org](https://www.interaction-design.org/literature/article/hick-s-law-making-the-choice-easier-for-users)*

## Mechanism — why this happens

Decision time grows **logarithmically** with the number of equally likely choices:

```
RT = a + b · log₂(n + 1)
```

`RT` is reaction time, `n` is the number of choices, `a` accounts for sensory and motor time (constant), and `b` is the
slope — the cost of one additional **bit** of decision. The `+1` accounts for the decision not to respond at all.

The log is the important part, and it is routinely misread in two directions:

- **"So more options are nearly free."** No. Log still grows, and `b` is not small. Going from 4 to 8 options costs
  about one bit — measurable, and multiplied across every screen in a flow.
- **"So I should cap everything at 7."** Also no. The formula assumes options are **equally likely and equally
  distinguishable**. Grouping, labelling, and recommendation change the effective `n` without changing the visible count.

The practical translation: **the cost is not the number of items, it is the number of *undifferentiated* items the user
must compare.** A 12-item menu with clear groups is cheaper than 12 flat items; a 12-item menu with one recommended
item is cheaper still, because most users do not evaluate the other eleven.

Hick's law and choice overload (`02-choice-overload.md`) are related but distinct: Hick is about **reaction time** under
a known set; choice overload is about **motivation and satisfaction** when the set is hard to evaluate. Fixing one does
not automatically fix the other.

## Numbers that matter

| Choices (n) | Bits (log₂(n+1)) | Relative decision cost |
|---|---|---|
| 1 | 1.0 | Baseline |
| 2 | 1.6 | +0.6 |
| 4 | 2.3 | +1.3 |
| 8 | 3.2 | +2.2 |
| 16 | 4.1 | +3.1 |
| 32 | 5.0 | +4.0 |

| Rule of thumb | Value |
|---|---|
| Navigation items per level | **≤7** |
| Options in a picker before search is needed | ~10 |
| Primary actions on a screen | **1** |
| Grouped items before a sub-heading is needed | 3–5 |

## Apply it

### Do

- **Cut to what the decision actually is.** Most menus contain three intents and nine variants of each.
- **Group before you cut.** A 12-item menu in 3 labelled groups of 4 reads as 3 decisions, not 12.
- **Recommend one.** Highlighting a default collapses `n` for the majority who have no strong preference.
- **Use progressive disclosure** — 5 visible, the rest behind "More". The user who needs the long tail can still reach it.
- **Add search once the list exceeds ~10.** At that size, recall beats scanning.
- **Keep primary actions to one per screen.** Two equal-weight buttons is a Hick's-law tax on every visit.
- **Order by frequency**, not alphabetically. The first item is read fastest; put the common case there.

### Don't

- Don't add options to appear comprehensive. Comprehensiveness is a feature of the *catalogue*, not the *interface*.
- Don't hide options behind hover menus on touch — that trades Hick's cost for discovery cost.
- Don't use a dropdown for 2 options. Two radio buttons are faster and visible.
- Don't flatten a hierarchy to "simplify". Removing group labels raises effective `n` even when the item count drops.
- Don't optimise the count and ignore the labels. Unclear labels make every item expensive.

## Pattern

```html
<!-- Bad: 9 flat, equal-weight choices -->
<nav>
  <a>Home</a><a>Product</a><a>Solutions</a><a>Pricing</a><a>Docs</a>
  <a>Blog</a><a>Careers</a><a>Support</a><a>Login</a>
</nav>

<!-- Better: 5 primary, grouped intent, one obvious action -->
<nav class="nav" aria-label="Main">
  <a href="/" class="nav__brand">Acme</a>
  <ul class="nav__list">
    <li><a href="/product">Product</a></li>
    <li><a href="/pricing">Pricing</a></li>
    <li><a href="/docs">Docs</a></li>
  </ul>
  <div class="nav__actions">
    <a href="/login" class="btn btn--ghost">Log in</a>
    <a href="/signup" class="btn btn--primary">Start free</a>
  </div>
</nav>
```

```css
.nav { display: flex; align-items: center; gap: var(--space-6); }
.nav__list { display: flex; gap: var(--space-6); list-style: none; margin: 0; padding: 0; }
.nav__actions { margin-inline-start: auto; display: flex; gap: var(--space-3); }
```

```html
<!-- Two options: radios, not a select -->
<fieldset>
  <legend>Billing</legend>
  <label><input type="radio" name="billing" value="monthly" checked> Monthly — $24</label>
  <label><input type="radio" name="billing" value="yearly"> Yearly — $19/mo, billed annually</label>
</fieldset>
```

## Audit question

> Count the items a user must compare on this screen to make the primary decision. If that number is above seven and
> none is recommended, the screen is asking for a search, not a choice.

## Further reading

| Reading | Author / Publisher |
|---|---|
| [UX Psychology: Google Search](https://lawsofux.com/articles/2020/ux-psychology-google-search/) | Jon Yablonski |
| [The Choice Overload Effect: Why simplicity is the key to perfecting your experience](https://medium.com/choice-hacking/choice-overload-why-simplicity-is-the-key-to-winning-customers-2f8e239eaba6) | Jennifer Clinehens \| Medium |
| [Hick’s Law: Making the choice easier for users](https://www.interaction-design.org/literature/article/hick-s-law-making-the-choice-easier-for-users) | Mads Soegaard \| Interaction Design Foundation |
| [Hick’s Law — Quick Decision Making](https://uxplanet.org/design-principles-hicks-law-quick-decision-making-3dcc1b1a0632) | Anton Nikolov \| Medium.com |
| [The Psychology Principles Every UI/UX Designer Needs to Know](https://blog.marvelapp.com/psychology-principles-every-uiux-designer-needs-know/) | Thanasis Rigopoulos \| Marvel |
| [Hick’s Law on Wikipedia](https://en.wikipedia.org/wiki/Hick%27s_law) | Wikipedia |

---

**Site page** · [lawsofux.com/hicks-law](https://lawsofux.com/hicks-law/)
