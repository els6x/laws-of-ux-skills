---
law: Law of Prägnanz
slug: law-of-pr%C3%A4gnanz
index: 14
category: gestalt
lever: simplicity of form
audit_weight: high
source: https://en.wikipedia.org/wiki/Principles_of_grouping
---

# 14 · Law of Prägnanz

> People will perceive and interpret ambiguous or complex images as the simplest form possible, because it is the interpretation that requires the least cognitive effort of us.

**Category** Gestalt · **Lever** Simplicity of form · **Audit weight** High

## What the site says

### Takeaways

1. The human eye likes to find simplicity and order in complex shapes because it prevents us from becoming overwhelmed with information.
2. Research confirms that people are better able to visually process and remember simple figures than complex figures.
3. The human eye simplifies complex shapes by transforming them into a single, unified shape.

### Origins

In 1910, psychologist Max Wertheimer had an insight when he observed a series of lights flashing on and off at a railroad crossing. It was similar to how the lights encircling a movie theater marquee flash on and off. To the observer, it appears as if a single light moves around the marquee, traveling from bulb to bulb, when in reality it’s a series of bulbs turning on and off and the lights don’t move it all. This observation led to a set of descriptive principles about how we visually perceive objects. These principles sit at the heart of nearly everything we do graphically as designers.

*Primary source cited on the site: [smashingmagazine.com](https://www.smashingmagazine.com/2014/03/design-principles-visual-perception-and-the-principles-of-gestalt/)*

## Mechanism — why this happens

Perception is an act of compression. Faced with ambiguity, the visual system resolves it toward the simplest
interpretation available — the one requiring the fewest assumptions, the fewest distinct shapes, the most regular
geometry. Prägnanz (from the German for "conciseness" or "good form") is the claim that this is not a preference but a
constraint on how perception works.

This is the parent principle behind the other Gestalt laws: proximity, similarity, continuity, and closure are all
specific ways the system achieves the simplest reading. That makes Prägnanz harder to apply directly, because it is not
a single technique — it is a **test you apply to a whole composition**:

> Does this layout have more distinct shapes, alignments, weights, and colors than it needs to convey its meaning?

Every element that does not carry information is a candidate for removal. Every distinct alignment is a candidate for
merging. Every extra weight, radius, or tint is a candidate for the bin. The goal is not minimalism as a style; it is
**the minimum number of distinctions required to make the structure readable**.

## Numbers that matter

| Quantity | Value | Consequence for the interface |
|---|---|---|
| Type sizes per screen | **≤5** (ideally 3–4) | More sizes read as noise, not hierarchy |
| Font weights per screen | **≤2** | 300/400/500/600/700 all at once is visual static |
| Distinct alignments | **1** (one grid) | Every extra alignment is a new edge to track |
| Visual hierarchy levels | 3 | Primary, secondary, tertiary — a fourth is invisible |
| Accent colors | **1** | A second accent halves the first one's meaning |
| Distinct corner radii | 2 (small, large) | Mixed radii imply different component types |

## Apply it

### Do

- **Reduce distinctions until removing one would break the meaning.** That is the test. Not "can I remove it?" but
  "does removing it change what the user understands?"
- **Use one alignment grid** for everything. Left-aligned text in one column, one consistent gutter.
- **Establish hierarchy with two levers only**: size and weight. Color is a third, used sparingly.
- **Merge similar components.** If two buttons differ only in shade, they are one component with a variant.
- **Simplify shapes.** Rounded rectangles at one radius beat a mix of pills, circles, and squares.
- **Make the reading path obvious.** A page should resolve into one dominant element, then a clear order.

### Don't

- Don't confuse simplicity with emptiness. Prägnanz is about *fewer distinctions*, not less content.
- Don't use more than one accent color for meaning. The second accent makes both ambiguous.
- Don't add decoration that competes with content — background patterns, gradients behind text, ornamental dividers.
- Don't use five font sizes to create hierarchy you could create with two plus spacing.
- Don't mix icon styles (outline + filled + duotone) in one set; that is three visual languages.

## Pattern

```css
/* A Prägnanz-compliant type system: 4 sizes, 2 weights */
:root {
  --text-sm: .875rem;   /* meta, captions        */
  --text-base: 1rem;    /* body                  */
  --text-lg: 1.25rem;   /* section headings      */
  --text-2xl: 2rem;     /* page title            */
}

/* No colours are defined here. The project's adapter supplies one accent and
   two text steps: --accent, --text-primary, --text-secondary. */
```

```html
<!-- Three hierarchy levels, no fourth -->
<article>
  <h1 class="t-title">Pricing</h1>
  <p class="t-lead">Simple plans that scale with your team.</p>
  <h2 class="t-section">Billing</h2>
  <p class="t-body">Change or cancel any time.</p>
</article>
```

```css
.t-title   { font-size: var(--text-2xl);  font-weight: 600;   color: var(--text-primary); }
.t-lead    { font-size: var(--text-lg);   font-weight: 400; color: var(--text-secondary); }
.t-section { font-size: var(--text-lg);   font-weight: 600;   color: var(--text-primary); }
.t-body    { font-size: var(--text-base); font-weight: 400; color: var(--text-primary); }
```

## Audit question

> List every distinct type size, weight, radius, accent color, and alignment on the screen. For each one, ask what
> meaning it carries. Anything that carries none is noise.

## Further reading

| Reading | Author / Publisher |
|---|---|
| [Design Principles: Visual Perception And The Principles Of Gestalt](https://www.smashingmagazine.com/2014/03/design-principles-visual-perception-and-the-principles-of-gestalt/) | Steven Bradley \| Smashing Magazine |
| [The Laws of Figure/Ground, Prägnanz, Closure, and Common Fate](https://www.interaction-design.org/literature/article/the-laws-of-figure-ground-praegnanz-closure-and-common-fate-gestalt-principles-3) | Mads Soegaard \| Interation Design Foundation |

---

**Site page** · [lawsofux.com/law-of-prägnanz](https://lawsofux.com/law-of-pr%C3%A4gnanz/)
