---
law: Cognitive Bias
slug: cognitive-bias
index: 4
category: cognition
lever: heuristics
audit_weight: critical
source: https://en.wikipedia.org/wiki/Cognitive_bias
---

# 04 · Cognitive Bias

> A systematic error of thinking or rationality in judgment that influence our perception of the world and our decision-making ability.

**Category** Cognition · **Lever** Working with (never against) heuristics · **Audit weight** Critical

## What the site says

### Takeaways

1. Rather than thinking through every situation, we conserve mental energy by developing rules of thumb to make decisions which are based on past experiences. These mental shortcuts increase our efficiency by enabling us to make quick decisions without the need to thoroughly analyze a situation but can also influence our decision-making processes and judgement without our awareness.
2. Understanding of our own intrinsic biases may not eliminate them completely from our decision-making but it increases the chance that we can identify them in ourselves and others and serve as a safeguard against fallacious reasoning, unintentional discrimination or costly mistakes our decisions.
3. Take for example our tendency to seek out, interpret, and recall information in a way that confirms their preconceived notions and ideas. This is known as confirmation bias, and it can make having a logical discussion about a polarizing hot-button issue with someone incredibly difficult.

### Origins

Amos Tversky and Daniel Kahneman introduced the notion of cognitive biases in 1972 after they observed people’s inability to reason intuitively with greater orders of magnitude. In a series of replicable experiments, Tversky, Kahneman, and their colleagues demonstrated that human judgment and decision-making differ from rational choice theory. They explained human differences in judgment and decision-making in terms of heuristics, which are mental shortcuts that provide quick estimates about the probabilities of uncertain events. but can introduce severe and systematic errors.

*Primary source cited on the site: [en.wikipedia.org](https://en.wikipedia.org/wiki/Cognitive_bias)*

## Mechanism — why this happens

Judgment runs on shortcuts. Tversky and Kahneman's programme (from 1974 onward) showed that people answer hard
questions by substituting easier ones: *how likely is this?* becomes *how easily does an example come to mind?*
(availability), *how representative does this look?* (representativeness), *what number was I just shown?* (anchoring).
These substitutions are usually adaptive — they are fast and mostly right — which is exactly why they cannot be
designed away. They can only be designed **for**.

The design question is therefore never "how do we remove bias?" but **"which direction does this bias push the user,
and is that direction in their interest?"** Every bias below has an honest use and a manipulative one, and the
difference is usually one sentence: *would the user still choose this if they understood the mechanic?*

| Bias | Honest use | Manipulative use |
|---|---|---|
| Anchoring | Show the full price before the discount, so the discount is real | Show a fake "was" price that never existed |
| Default effect | Pre-select the safest, most reversible option | Pre-select the expensive plan or the marketing consent |
| Loss aversion | Warn clearly before destructive actions | "Only 2 left!" when stock is unlimited |
| Framing | State outcomes positively when both framings are true | Frame a fee as "no extra charge" when it is built in |
| Sunk cost | Show progress so effort feels worthwhile | Make cancellation hard because "you've come so far" |
| Social proof | Show real review counts and real usage | Fabricate "1,204 people bought this today" |
| Confirmation | Let users filter to what they already believe | Hide contradicting information in fine print |
| Halo | Keep visual quality consistent so trust is earned | Use polish to disguise a harmful flow (see `01`) |

## Numbers that matter

| Quantity | Value | Consequence for the interface |
|---|---|---|
| Anchoring (Tversky & Kahneman, 1974) | Estimates shift toward any prior number, even a random one | Order matters: first price seen sets the frame |
| Loss aversion (Kahneman & Tversky, 1979) | Losses weigh roughly **2×** gains | "Keep your data" beats "delete your data" for the same outcome |
| Default effect | Opt-in vs opt-out changes participation by large margins | Defaults are the strongest single control you have |
| Framing | Same fact, different choice, reliably | Never assume a neutral presentation exists |

## Apply it

### Do

- **Choose defaults as if you were choosing for the user.** The default is your recommendation; make it the
  reversible, low-risk, privacy-preserving option.
- **Order information honestly.** Put the real price first, then the discount. Put the recommended plan where the eye
  lands, but label *why* it is recommended.
- **Frame truthfully and usefully.** "92% of teams finish setup in one day" is framing *and* true; both must hold.
- **Make the destructive action the one that requires effort**, and the safe action the easy one.
- **Expose the mechanic on request.** A tooltip like "why am I seeing this?" converts a nudge into a choice.
- **Use social proof only when it is real, current, and representative.**

### Don't

- Don't manufacture urgency, scarcity, or social proof. It is a one-time gain against permanent trust.
- Don't pre-check marketing consent, add-ons, or insurance. That is the default effect used against the user.
- Don't use confirmshaming ("No thanks, I don't want to save money").
- Don't hide costs until the final step. Drip pricing is a bias exploit, not a design pattern.
- Don't assume your own interface is neutral. It is already framing something; decide what.

## Pattern

```html
<!-- Bad: default opts the user into the paid add-on -->
<label><input type="checkbox" checked> Add priority support (+$9/mo)</label>

<!-- Better: default is off, benefit is stated, no shame in declining -->
<label>
  <input type="checkbox">
  Priority support — replies within 4 hours (+$9/mo)
</label>

<!-- Bad: fake scarcity -->
<p class="urgent">Only 2 left!</p>

<!-- Better: real, verifiable scarcity, or nothing -->
<p class="stock">3 left in this size</p>
```

```html
<!-- Honest anchoring: real price first -->
<p class="price">
  <span class="price__now">$24</span>
  <span class="price__was">$30</span>
  <span class="price__note">Launch price until Nov 1</span>
</p>
```

## Audit question

> For each nudge on this screen: would the user still choose it if they understood exactly how it works? If the answer
> is no, it is a dark pattern.

## Further reading

| Reading | Author / Publisher |
|---|---|
| [Thinking, Fast and Slow [Book]](https://us.macmillan.com/books/9780374533557/thinkingfastandslow) | Daniel Kahneman \| Farrar, Straus and Giroux |
| [Design for Cognitive Bias [Book]](https://abookapart.com/products/design-for-cognitive-bias.html) | David Dylan Thomas \| A Book Apart |
| [Cognitive Bias Index [Website]](https://cognitivebiasindex.com/) | Jon Yablonski |
| [Decision Frames: How Cognitive Biases Affect UX Practitioners](https://www.nngroup.com/articles/decision-framing-cognitive-bias-ux-pros/) | Kathryn Whitenton \| Nielsen Norman Group |
| [Daniel Kahneman Explains The Machinery of Thought](https://fs.blog/daniel-kahneman-the-two-systems/) | Farnam Street |
| [Cognitive Biases](https://www.interaction-design.org/literature/topics/cognitive-biases) | Interaction Design Foundation |
| [How Cognitive Biases Influence the Way You Think and Act](https://www.verywellmind.com/what-is-a-cognitive-bias-2794963) | Kendra Cherry, MSEd \| verywell mind |

---

**Site page** · [lawsofux.com/cognitive-bias](https://lawsofux.com/cognitive-bias/)
