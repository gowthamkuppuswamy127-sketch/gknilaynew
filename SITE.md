# Nilayaa Interiors — website

A four-page static marketing site. No build step, no framework, no backend.
Open `index.html` in a browser and it runs.

```
index.html        Hero, services, featured work, process, reviews, CTA
portfolio.html    Filterable project grid + lightbox
services.html     Four services in detail + process
contact.html      Enquiry form, WhatsApp, call, map
```

## Run it locally

Double-clicking `index.html` works, but a local server is closer to production:

```bash
python3 -m http.server 8000
# → http://127.0.0.1:8000
```

## Before you publish

Three things, in order of impact. Full checklist in **[CONTENT-TODO.md](CONTENT-TODO.md)**.

1. **Add photos** → `assets/images/`, names listed in
   [`assets/images/README.md`](assets/images/README.md). This matters more than
   everything else combined.
2. **Replace placeholder content** — project names, three Google review quotes,
   street address, email, hours. Every one is marked with an amber ⚠ ribbon on
   the page.
3. **Connect the form** — paste a Formspree endpoint into `FORMSPREE_ENDPOINT`
   near the top of `assets/js/site.js`. WhatsApp and the call button already work.

Then switch draft mode off — in all four `.html` files change:

```html
<html lang="en" data-draft="true">   →   data-draft="false"
```

That single attribute hides every ribbon, every placeholder caption and the
draft notice at once.

> While photos are missing your browser console logs a 404 for each empty slot.
> That is the placeholder system working as designed — the warm tonal panel you
> see is the fallback. The 404s disappear as you add the files.

## File map

```
assets/css/site.css        Everything: tokens, components, responsive, print
assets/css/fonts.css       @font-face for the two self-hosted families
assets/js/site.js          Behaviour — nav, filter, lightbox, form, sticky bar
assets/js/motion.js        Animation — delete this file and the site still works
assets/vendor/gsap/        GSAP 3.15.0, pinned. No CDN, no network dependency
assets/fonts/              Fraunces + Inter Tight, self-hosted woff2
assets/images/             Your photographs go here
tools/build_pages.py       Optional — keeps the header/footer identical
```

## Editing the pages

The four HTML files are plain and editable by hand. But the header, footer and
CTA band are repeated in all four, so changing them by hand means four edits.

`tools/build_pages.py` regenerates all four from shared fragments:

```bash
python3 tools/build_pages.py
```

Edit the fragments in that file, re-run, commit the regenerated HTML. **The site
never needs this script** — it is a convenience, not a build step. If you prefer
editing HTML directly, do that and ignore the script (just don't run it
afterwards, or it will overwrite your changes).

## Design system

| Token | Value | Use |
|---|---|---|
| `--ivory` | `#FAF7F2` | Page base |
| `--sand` | `#F1EBE1` | Alternating bands |
| `--espresso` | `#2A241E` | Dark sections, footer, buttons |
| `--taupe` | `#9A8D7E` | Hairlines, text on espresso |
| `--brass` | `#A98B5D` | Accent, rules, text on espresso |
| `--taupe-ink` | `#6B6055` | Secondary body text on light |
| `--brass-ink` | `#7D6238` | Eyebrows and small brass text on light |

The last two exist for a reason: `--taupe` and `--brass` measure 3.03:1 and
3.01:1 against ivory, which fails WCAG AA for body-size text. The `-ink`
variants are the same hues darkened to 5.73:1 and 5.35:1. **Use `--brass` for
rules, large display type and anything on espresso; use `--brass-ink` for small
text on ivory or sand.**

Type is Fraunces (display, weight 900, `SOFT 28 / WONK 1`) over Inter Tight
(body). Hero scales `clamp(52px, 9vw, 128px)`; body is 18px / 1.75.

## Motion

GSAP 3.15 — ScrollSmoother, ScrollTrigger and SplitText, all vendored locally.

| Effect | Where |
|---|---|
| Smooth scrolling | Whole site (native scroll retained on touch) |
| Per-character headline reveal | Every `<h1 data-split>` |
| Staggered section reveals | Anything with `data-anim="rise\|fade\|scale"` |
| Parallax | Anything with `data-speed` (0.82–1.06) |
| Pinned, scrubbed process timeline | Home + Services, ≥900px only |
| Magnetic buttons | `.magnetic`, fine pointers only |
| Page transitions | Native View Transitions, degrades silently |

To add motion to a new block, put `data-anim="rise"` on it — that is all.
To give an image parallax, put `data-speed="0.95"` on its `.media__inner`.

Everything animates transform and opacity only, so it stays GPU-composited.

**Safety rails, all verified:**

* `prefers-reduced-motion: reduce` — no smoother, no reveals, nothing hidden.
* No JavaScript — the page renders complete and readable. Animated blocks are
  only hidden after JS confirms it can animate them.
* If GSAP fails to load, `motion.js` un-hides everything rather than leaving a
  blank page.
* Pinning is disabled below 900px.

## Deploying

Any static host works — copy the folder up. For GitHub Pages, a workflow is
included at `.github/workflows/pages.yml`; it does nothing until you enable
Pages under **Settings → Pages → Source: GitHub Actions**.

If you publish to a project path (`user.github.io/repo/`) rather than a custom
domain, the relative paths all still work.

## Browser support

Chrome, Edge, Safari and Firefox, current versions. Two progressive
enhancements degrade silently where unsupported: cross-document View
Transitions (Firefox falls back to a normal navigation) and
`backdrop-filter` on the stuck header (falls back to a solid background).

## What was checked

Automated pass in real Chromium across `390 / 834 / 1440px` on all four pages:
no console errors, no non-image 404s, no horizontal overflow, every reveal
completes, reduced-motion leaves nothing invisible, the no-JS render is
readable, and the filter, lightbox (mouse + arrow keys + Escape), drawer and
form validation all behave.
