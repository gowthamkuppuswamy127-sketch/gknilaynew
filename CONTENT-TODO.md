# Content to replace before going live

Everything on the site is real **except** the items below. They are marked in
two ways so nothing placeholder can be published by accident:

* an **amber ⚠ TODO ribbon** on the page itself
* an entry in this file

When you have replaced them all, open each of the four `.html` files and change
`<html lang="en" data-draft="true">` to `data-draft="false"`. That hides every
ribbon, every placeholder caption and the draft notice in one move.

---

## What is already real

Taken from your Google listing — no need to touch these.

| Fact | Value |
|---|---|
| Business name | Nilayaa Interiors |
| Locality | Basavanagudi, Bengaluru, Karnataka |
| Phone | 099455 58884 (`tel:` and WhatsApp links are live) |
| Google rating | 4.8 |
| Review count | 161 |

---

## 1. Photographs — the big one

Drop your files into `assets/images/` using **exactly** these names and they
appear immediately. No code changes. Full list with dimensions is in
`assets/images/README.md`.

Until a file exists, that slot shows a warm tonal panel with the filename
printed on it. **This also means your browser console will show a 404 for each
missing photo — that is expected and disappears as you add them.**

Priority order, best work first:

1. `hero.jpg` — the single most important image on the site
2. `project-01.jpg` … `project-09.jpg` — portfolio grid
3. `service-full-home.jpg`, `service-modular.jpg`, `service-commercial.jpg`, `service-renovation.jpg`
4. `page-portfolio.jpg`, `page-services.jpg`, `page-contact.jpg`, `cta.jpg`
5. `og-image.jpg` — the preview card when the site is shared on WhatsApp/social

## 2. Project names and localities — 9 projects

**Where:** `portfolio.html` and `index.html`, ribbon *"Replace with a real project name and locality"*

Right now each project is labelled by typology only (`3 BHK Apartment`,
`Modular Kitchen`, …). These are honest placeholders, not invented project
names. Replace with the real thing, e.g. `3 BHK · Jayanagar`.

Edit `tools/build_pages.py` → the `PROJECTS` list, then run
`python3 tools/build_pages.py`. Or edit the HTML directly — change both the
`data-title` attribute (used by the lightbox) and the visible
`<span class="project__title">`, and the image `alt` text.

## 3. Google reviews — 3 quotes

**Where:** `index.html`, ribbons *"Paste Google review 1 / 2 / 3"*

The 4.8★ / 161 figure is real and already displayed. The three quote cards are
placeholders — I did not write testimonials, because inventing customer quotes
for a real business is not something to ship. Paste three real reviews from your
Google listing, with the reviewer's name and locality.

## 4. Business details

| Item | Where | Ribbon |
|---|---|---|
| Street address + PIN | `contact.html` | *Add full street address and PIN code* |
| Email address | `contact.html`, footer on all pages | *Add real email* |
| Working hours | `contact.html` | *Confirm working hours* |
| Years active / projects delivered | `index.html` trust strip | *Add a real figure* |
| Brand line ("From *nilaya* — a dwelling…") | footer, all pages | *Confirm or replace this brand line* |
| Map embed | `contact.html` | *Replace with the exact Google Maps place embed* |

For the map: open your Google Business listing → Share → Embed a map → copy the
`<iframe>` and swap it in. The current one is a name search, which is close but
not pinned to your exact location.

For the four process stages (Consultation → Design & 3D → Execution → Handover),
confirm they match how you actually work — ribbon *"Confirm these four stages
match your actual process"* on `index.html` and `services.html`.

## 5. Connect the enquiry form

The form validates properly but is not wired to an inbox yet. Submitting shows
a clear notice saying so.

1. Create a free form at <https://formspree.io> (50 submissions/month free).
2. Copy your endpoint — it looks like `https://formspree.io/f/abcdwxyz`.
3. Open `assets/js/site.js`, line ~12, and set:
   ```js
   var FORMSPREE_ENDPOINT = 'https://formspree.io/f/abcdwxyz';
   ```

WhatsApp and the call button already work and need nothing.

## 6. Domain

`tools/build_pages.py` has `SITE_URL = "https://nilayaainteriors.com"`. This is
used for canonical URLs and social preview tags. Set it to your real domain and
rebuild, or find-and-replace it across the four HTML files.
