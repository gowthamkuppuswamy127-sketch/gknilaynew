#!/usr/bin/env python3
"""
Regenerates the four HTML pages from shared fragments.

The SITE DOES NOT NEED THIS. The generated .html files are plain static pages
that work on their own. This script exists only so the header, footer and other
repeated markup stay identical across the four pages when you change them.

    python3 tools/build_pages.py

Edit the fragments below, re-run, commit the regenerated .html.
"""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent

# ---------------------------------------------------------------------------
# Business facts. Only the values marked REAL are verified.
# ---------------------------------------------------------------------------
NAME       = "Nilayaa Interiors"
PHONE_DISP = "099455 58884"          # REAL
PHONE_TEL  = "+919945558884"         # REAL
WA_NUMBER  = "919945558884"          # REAL
LOCALITY   = "Basavanagudi"          # REAL
CITY       = "Bengaluru"             # REAL
REGION     = "Karnataka"             # REAL
RATING     = "4.8"                   # REAL — Google
RATING_N   = "161"                   # REAL — Google
SITE_URL   = "https://nilayaainteriors.com"   # TODO: real domain
EMAIL      = "hello@nilayaainteriors.com"     # TODO: real address

WA_MSG = "Hi%20Nilayaa%20Interiors%2C%20I%27d%20like%20to%20book%20a%20consultation."
WA_URL = f"https://wa.me/{WA_NUMBER}?text={WA_MSG}"

NAV = [("index.html", "Home"), ("portfolio.html", "Portfolio"),
       ("services.html", "Services"), ("contact.html", "Contact")]

SERVICES = [
    ("01", "Full Home Interiors", "services.html#full-home", "service-full-home.jpg",
     "End-to-end design and delivery for 2, 3 and 4 BHK homes — layout, joinery, "
     "lighting, finishes and styling on one coordinated timeline.",
     ["Space planning and layout", "3D visualisation before work begins",
      "Carpentry, civil and electrical", "Lighting, finishes and styling",
      "Site supervision to handover"]),
    ("02", "Modular Kitchens &amp; Wardrobes", "services.html#modular", "service-modular.jpg",
     "Ergonomic modular systems built around how you actually cook and store, "
     "in L, U, parallel and island layouts.",
     ["L, U, parallel and island layouts", "Soft-close hardware throughout",
      "Acrylic, laminate and PU finishes", "Loft, corner and pull-out storage",
      "Wardrobes, lofts and dressers"]),
    ("03", "Commercial &amp; Office Interiors", "services.html#commercial", "service-commercial.jpg",
     "Workspaces, clinics, retail and cafés designed for footfall, brand and "
     "compliance — executed in phases around your business hours.",
     ["Space planning for teams", "Reception and brand walls",
      "Acoustics and lighting design", "Phased, after-hours execution",
      "Furniture and storage systems"]),
    ("04", "Renovation &amp; Remodelling", "services.html#renovation", "service-renovation.jpg",
     "Reworking homes you already live in — room by room, with minimum "
     "disruption and a clear sequence of work.",
     ["False ceiling and electrical", "Flooring and tiling",
      "Kitchen and bathroom upgrades", "Painting and finishing",
      "Room-by-room staged execution"]),
]

# (title, category, image, aspect) — titles are TYPOLOGY PLACEHOLDERS, not real
# project names. Every one carries a TODO ribbon until replaced.
PROJECTS = [
    ("3 BHK Apartment",      "residential", "project-01.jpg"),
    ("Modular Kitchen",      "kitchen",     "project-02.jpg"),
    ("Primary Bedroom",      "residential", "project-03.jpg"),
    ("Office Fit-Out",       "commercial",  "project-04.jpg"),
    ("Walk-In Wardrobe",     "kitchen",     "project-05.jpg"),
    ("Living &amp; Dining",  "residential", "project-06.jpg"),
    ("Apartment Renovation", "renovation",  "project-07.jpg"),
    ("Clinic Reception",     "commercial",  "project-08.jpg"),
    ("Kitchen Remodel",      "renovation",  "project-09.jpg"),
]

CAT_LABEL = {"residential": "Residential", "kitchen": "Modular Kitchen",
             "commercial": "Commercial", "renovation": "Renovation"}

PROCESS = [
    ("1", "Consultation", "We visit the site, understand how you live or work, and agree a scope and budget band before anything is drawn."),
    ("2", "Design &amp; 3D", "Layouts, material palettes and 3D views, revised with you until the space reads right on screen."),
    ("3", "Execution", "Carpentry, civil, electrical and finishing run to a dated schedule with supervision at every stage."),
    ("4", "Handover", "Snag list closed, surfaces cleaned, hardware checked and warranties handed over with the keys."),
]

# ---------------------------------------------------------------------------
# Icons
# ---------------------------------------------------------------------------
def svg(body, w=16, h=16, vb="0 0 24 24", stroke=True):
    attrs = ('fill="none" stroke="currentColor" stroke-width="1.6" '
             'stroke-linecap="round" stroke-linejoin="round"') if stroke else 'fill="currentColor"'
    return (f'<svg width="{w}" height="{h}" viewBox="{vb}" {attrs} '
            f'aria-hidden="true" focusable="false">{body}</svg>')

I_ARROW = svg('<path d="M5 12h14M13 6l6 6-6 6"/>', 15, 15)
I_STAR  = svg('<path d="M12 2.6l2.9 5.9 6.5.95-4.7 4.58 1.11 6.47L12 17.45 '
              '6.19 20.5 7.3 14.03 2.6 9.45l6.5-.95L12 2.6z"/>', 17, 17, stroke=False)
I_CLOSE = svg('<path d="M6 6l12 12M18 6L6 18"/>', 22, 22)
I_ZOOM  = svg('<circle cx="11" cy="11" r="7"/><path d="M20 20l-3.6-3.6M11 8.4v5.2M8.4 11h5.2"/>', 19, 19)
I_PREV  = svg('<path d="M15 6l-6 6 6 6"/>', 22, 22)
I_NEXT  = svg('<path d="M9 6l6 6-6 6"/>', 22, 22)
I_PHONE = svg('<path d="M6.3 3.5h3l1.5 3.8-2 1.3a12 12 0 006.6 6.6l1.3-2 3.8 1.5v3a1.7 '
              '1.7 0 01-1.9 1.7A16.5 16.5 0 014.6 5.4 1.7 1.7 0 016.3 3.5z"/>', 16, 16)
I_WA    = svg('<path d="M12.04 2c-5.5 0-9.96 4.46-9.96 9.96 0 1.76.46 3.48 1.34 '
              '5l-1.42 5.18 5.31-1.39a9.9 9.9 0 004.73 1.2h.01c5.5 0 9.96-4.46 '
              '9.96-9.96A9.9 9.9 0 0012.04 2zm5.8 14.06c-.24.68-1.42 1.31-1.95 '
              '1.36-.5.05-.98.23-3.3-.69-2.78-1.1-4.55-3.95-4.69-4.13-.14-.18-1.12-1.49-1.12-2.84 '
              '0-1.35.71-2.02.96-2.29a1 1 0 01.73-.34h.52c.17 0 .39-.06.61.47.24.56.8 '
              '1.94.87 2.08.07.14.12.3.02.48-.1.18-.15.3-.29.46l-.44.51c-.14.14-.29.3-.12.59.17.28.75 '
              '1.24 1.62 2.01 1.11.99 2.05 1.3 2.34 1.44.29.15.46.12.63-.07.17-.2.73-.85.93-1.14.2-.29.39-.24.66-.14.27.1 '
              '1.7.8 1.99.95.29.14.48.22.55.34.07.12.07.7-.17 1.38z"/>', 17, 17, stroke=False)

STARS = f'<span class="stars" aria-hidden="true">{I_STAR * 5}</span>'


def media(img, alt, ar="4/5", speed=None, dims="1600×2000", dark=False,
          tag="div", eager=False, extra=""):
    """One media frame.

    A real <img> (not a CSS background) so that: the path resolves against the
    DOCUMENT rather than site.css, screen readers get alt text, and the browser
    can lazy-load. If the file is absent the img is removed by site.js and the
    warm tonal gradient underneath shows through — never a broken-image icon.
    """
    cls = "media media--dark" if dark else "media"
    if ar == "auto":
        cls += " media--bleed"      # caption moves out of the headline's way
    sp = f' data-speed="{speed}"' if speed else ""
    load = ' fetchpriority="high"' if eager else ' loading="lazy"'
    return (
        f'<{tag} class="{cls}" style="--ar:{ar}" data-ph="{img} · {dims}"{extra}>'
        f'<{tag} class="media__inner"{sp}>'
        f'<img class="media__img" src="assets/images/{img}" alt="{alt}"{load} decoding="async">'
        f'</{tag}></{tag}>'
    )


# ---------------------------------------------------------------------------
# Shared fragments
# ---------------------------------------------------------------------------
def head(page, title, desc, extra=""):
    canonical = f"{SITE_URL}/{page}" if page != "index.html" else f"{SITE_URL}/"
    return f"""<!doctype html>
<html lang="en" data-draft="true">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<meta name="theme-color" content="#2A241E">

<meta property="og:type" content="website">
<meta property="og:site_name" content="{NAME}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE_URL}/assets/images/og-image.jpg">
<meta name="twitter:card" content="summary_large_image">

<link rel="preload" href="assets/fonts/fraunces-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/fonts/inter-tight-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/css/site.css">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'><rect width='32' height='32' fill='%232A241E'/><text x='16' y='23' font-family='Georgia,serif' font-size='20' font-weight='bold' fill='%23A98B5D' text-anchor='middle'>N</text></svg>">
{extra}
<script>
  /* Only hide animated blocks once we know scripting is available. If this
     never runs, or motion.js fails, the page renders fully visible. */
  document.documentElement.classList.add('js-ready');
</script>
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
"""


def header(active):
    def cur(href):
        return ' aria-current="page"' if href == active else ''
    links = "".join(
        f'<a class="nav__link" href="{href}"{cur(href)}>{label}</a>'
        for href, label in NAV)
    dlinks = "".join(
        f'<a class="drawer__link" href="{href}"{cur(href)}>{label}</a>'
        for href, label in NAV)
    dark = " is-over-dark" if active in ("index.html",) else " is-over-dark"
    return f"""
<header class="site-header{dark}" data-header>
  <div class="site-header__inner">
    <a class="brand" href="index.html" aria-label="{NAME} — home">
      <span class="brand__mark">N</span>
      <span>Nilayaa</span>
      <span class="brand__sub">Interiors</span>
    </a>
    <nav class="nav" aria-label="Primary">{links}</nav>
    <a class="btn btn--ghost header__cta magnetic" href="contact.html">Book a consultation</a>
    <button class="burger" type="button" data-drawer-open aria-label="Open menu" aria-haspopup="dialog">
      <span></span><span></span><span></span>
    </button>
  </div>
</header>

<dialog class="drawer" data-drawer aria-label="Menu">
  <div class="drawer__inner">
    <div class="drawer__top">
      <button class="drawer__close" type="button" data-drawer-close aria-label="Close menu">{I_CLOSE}</button>
    </div>
    <nav class="drawer__nav" aria-label="Mobile">{dlinks}</nav>
    <div class="drawer__foot">
      <a class="btn btn--brass" href="contact.html">Book a consultation</a>
      <p class="drawer__meta">{LOCALITY}, {CITY}<br><a href="tel:{PHONE_TEL}">{PHONE_DISP}</a></p>
    </div>
  </div>
</dialog>

<div id="smooth-wrapper">
<div id="smooth-content">
"""


def cta_band():
    return f"""
<section class="section cta-band" aria-labelledby="cta-h">
  <div class="cta-band__media" aria-hidden="true">
    {media("cta.jpg", "", ar="auto", speed="0.9", dims="2400×1200", dark=True)}
  </div>
  <div class="container cta-band__inner">
    <p class="eyebrow" data-anim="fade">Start here</p>
    <h2 class="h2" id="cta-h" data-anim="rise">Tell us about<br>your space.</h2>
    <p class="lede" data-anim="rise">Share your floor plan, your timeline and roughly what you
      have in mind. We will come back with a scope, a budget band and the next step.</p>
    <div class="btn-row" data-anim="rise" style="justify-content:center">
      <a class="btn btn--brass magnetic" href="contact.html">Book a consultation {I_ARROW}</a>
      <a class="btn btn--wa" href="{WA_URL}" target="_blank" rel="noopener">{I_WA} WhatsApp us</a>
    </div>
  </div>
</section>
"""


def footer(lightbox=False):
    srv = "".join(f'<li><a href="{s[2]}">{s[1]}</a></li>' for s in SERVICES)
    nav = "".join(f'<li><a href="{h}">{l}</a></li>' for h, l in NAV)
    lb = f"""
<dialog class="lightbox" data-lightbox aria-label="Project image">
  <div class="lightbox__box">
    <button class="lightbox__close" type="button" data-lb-close aria-label="Close">{I_CLOSE}</button>
    <button class="lightbox__ctrl lightbox__ctrl--prev" type="button" data-lb-prev aria-label="Previous project">{I_PREV}</button>
    <button class="lightbox__ctrl lightbox__ctrl--next" type="button" data-lb-next aria-label="Next project">{I_NEXT}</button>
    <div class="media media--dark" data-lb-media>
      <div class="media__inner media__inner--lb">
        <img class="media__img" data-lb-img alt="">
      </div>
    </div>
    <div class="lightbox__bar">
      <div>
        <p class="lightbox__tag" data-lb-tag></p>
        <p class="lightbox__title" data-lb-title></p>
      </div>
      <p class="lightbox__count" data-lb-count></p>
    </div>
  </div>
</dialog>
""" if lightbox else ""

    return f"""
<footer class="site-footer">
  <div class="container">
    <div class="footer__grid">
      <div>
        <p class="footer__brand">Nilayaa</p>
        <p class="footer__tag" data-todo="Confirm or replace this brand line">
          From <em>nilaya</em> — a dwelling, a place to settle. Interiors for homes
          and workspaces across {CITY}.</p>
      </div>
      <div>
        <p class="footer__h">Explore</p>
        <ul class="footer__list">{nav}</ul>
      </div>
      <div>
        <p class="footer__h">Studio</p>
        <ul class="footer__list">
          <li><a href="tel:{PHONE_TEL}">{PHONE_DISP}</a></li>
          <li><a href="{WA_URL}" target="_blank" rel="noopener">WhatsApp</a></li>
          <li><span data-todo="Add real email">{EMAIL}</span></li>
          <li>{LOCALITY}, {CITY} {REGION}</li>
        </ul>
      </div>
    </div>
    <div class="footer__bar">
      <p>&copy; <span data-year>2026</span> {NAME}. All rights reserved.</p>
      <p>{RATING}&#9733; from {RATING_N} Google reviews</p>
    </div>
  </div>
</footer>

</div><!-- /#smooth-content -->
</div><!-- /#smooth-wrapper -->

<div class="mobile-bar" data-mobile-bar>
  <a href="tel:{PHONE_TEL}">{I_PHONE} Call</a>
  <a href="{WA_URL}" target="_blank" rel="noopener">{I_WA} WhatsApp</a>
</div>

<aside class="draft-banner" data-draft-banner>
  <div>
    <strong>Draft mode</strong>
    Amber ribbons mark placeholder content. See <code>CONTENT-TODO.md</code>,
    then set <code>data-draft="false"</code> on &lt;html&gt;.
  </div>
  <button class="draft-banner__x" type="button" data-draft-dismiss aria-label="Hide draft notice">&times;</button>
</aside>
{lb}
<script src="assets/vendor/gsap/gsap.min.js"></script>
<script src="assets/vendor/gsap/ScrollTrigger.min.js"></script>
<script src="assets/vendor/gsap/ScrollSmoother.min.js"></script>
<script src="assets/vendor/gsap/SplitText.min.js"></script>
<script src="assets/js/site.js"></script>
<script src="assets/js/motion.js"></script>
</body>
</html>
"""


def page_hero(crumb, eyebrow, title, lede, img):
    return f"""
<section class="page-hero">
  <div class="page-hero__media" aria-hidden="true">
    {media(img, "", ar="auto", speed="0.88", dims="2400×1200", dark=True)}
  </div>
  <div class="container page-hero__inner">
    <nav class="crumbs" aria-label="Breadcrumb">
      <a href="index.html">Home</a><span aria-hidden="true">/</span><span>{crumb}</span>
    </nav>
    <p class="eyebrow" data-anim="fade">{eyebrow}</p>
    <h1 class="display" data-split>{title}</h1>
    <p class="lede" data-anim="rise">{lede}</p>
  </div>
</section>
"""


def process_section(dark=True):
    steps = "".join(f"""
      <div class="process__step" data-step data-anim="rise">
        <span class="process__dot">{n}</span>
        <h3>{t}</h3>
        <p>{d}</p>
      </div>""" for n, t, d in PROCESS)
    return f"""
<section class="section section--dark" data-process aria-labelledby="process-h">
  <div class="container">
    <div class="section-head">
      <div>
        <p class="eyebrow" data-anim="fade">How we work</p>
        <h2 class="h2" id="process-h" data-anim="rise">Four stages,<br>one timeline.</h2>
      </div>
      <p class="lede" data-anim="rise" data-todo="Confirm these four stages match your actual process">
        Every project runs the same route, so you always know what is happening
        on site and what comes next.</p>
    </div>
    <div class="process__track">
      <span class="process__fill" data-process-fill aria-hidden="true"></span>
      {steps}
    </div>
  </div>
</section>
"""


def project_card(i, title, cat, img, featured=False):
    ar = "16/9" if featured else "4/5"
    return f"""
        <button class="project" type="button" data-project data-cat="{cat}"
                data-title="{title}" data-tag="{CAT_LABEL[cat]}"
                data-img="assets/images/{img}" data-index="{i}"
                aria-label="View {title} — {CAT_LABEL[cat]}">
          <span class="project__frame" data-todo="Replace with a real project name and locality">
            <span class="media" style="--ar:{ar}" data-ph="{img} · 1600×2000">
              <span class="media__inner" data-speed="{1.04 if i % 2 else 0.96}">
                <img class="media__img" src="assets/images/{img}"
                     alt="{title} — {CAT_LABEL[cat]} project by Nilayaa Interiors"
                     loading="lazy" decoding="async">
              </span>
            </span>
            <span class="project__zoom">{I_ZOOM}</span>
          </span>
          <span class="project__meta">
            <span class="project__title">{title}</span>
            <span class="project__tag">{CAT_LABEL[cat]}</span>
          </span>
        </button>"""


# ---------------------------------------------------------------------------
# Pages
# ---------------------------------------------------------------------------
def build_index():
    cards = "".join(f"""
      <a class="card" href="{link}" data-anim="rise">
        <span class="card__num">{num}</span>
        <span class="card__title">{name}</span>
        <span class="card__body">{blurb}</span>
        <span class="card__go">Explore {I_ARROW}</span>
      </a>""" for num, name, link, _img, blurb, _b in SERVICES)

    feat = "".join(project_card(i, t, c, im, featured=(i == 0))
                   for i, (t, c, im) in enumerate(PROJECTS[:5]))

    reviews = "".join(f"""
        <figure class="review" data-anim="rise" data-todo="Paste Google review {n}">
          {STARS}
          <blockquote class="review__quote">&ldquo;Placeholder review text. Replace this
            with a real review from your Google listing before publishing.&rdquo;</blockquote>
          <figcaption class="review__by"><b>[Client name]</b>[Locality] &middot; [Project type]</figcaption>
        </figure>""" for n in (1, 2, 3))

    jsonld = f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "HomeAndConstructionBusiness",
  "additionalType": "https://schema.org/InteriorDesignService",
  "name": "{NAME}",
  "telephone": "{PHONE_TEL}",
  "url": "{SITE_URL}",
  "image": "{SITE_URL}/assets/images/og-image.jpg",
  "address": {{
    "@type": "PostalAddress",
    "addressLocality": "{LOCALITY}",
    "addressRegion": "{REGION}",
    "addressCountry": "IN"
  }},
  "areaServed": {{ "@type": "City", "name": "{CITY}" }},
  "aggregateRating": {{
    "@type": "AggregateRating",
    "ratingValue": "{RATING}",
    "reviewCount": "{RATING_N}",
    "bestRating": "5"
  }}
}}
</script>
<!-- TODO: add "streetAddress" and "postalCode" above, plus "openingHours",
     once confirmed. They are omitted rather than guessed. -->"""

    return (
        head("index.html",
             f"{NAME} — Interior Designers in {LOCALITY}, {CITY}",
             f"Full home interiors, modular kitchens, commercial fit-outs and renovation "
             f"in {CITY}. Rated {RATING} by {RATING_N} clients on Google.",
             jsonld)
        + header("index.html")
        + f"""
<main id="main">

<section class="hero">
  <div class="hero__media" aria-hidden="true">
    <div class="media media--dark media--bleed" data-ph="hero.jpg · 2400×1600" style="--ar:auto">
      <div class="media__inner" data-hero-img data-speed="0.82">
        <img class="media__img" src="assets/images/hero.jpg" alt="" fetchpriority="high" decoding="async">
      </div>
    </div>
  </div>
  <div class="hero__scrim" aria-hidden="true"></div>
  <div class="container hero__inner">
    <div class="hero__grid">
      <div>
        <p class="eyebrow" data-anim="fade">Interiors &middot; {LOCALITY}, {CITY}</p>
        <h1 class="display" data-split>Built around<br>how you live.</h1>
        <p class="lede hero__lede" data-anim="rise">{NAME} designs and delivers full home
          interiors, modular kitchens and commercial spaces across {CITY} — from the first
          drawing to the final handover.</p>
        <div class="btn-row" data-anim="rise">
          <a class="btn btn--brass magnetic" href="contact.html">Book a consultation {I_ARROW}</a>
          <a class="btn btn--ghost" href="portfolio.html">See our work</a>
        </div>
      </div>
      <aside class="hero__aside" data-anim="rise">
        <div class="hero__stat">
          <b>{RATING}&#9733;</b><span>Rated by {RATING_N} clients<br>on Google</span>
        </div>
        <div class="hero__stat">
          <b>4</b><span>Service lines, from full<br>homes to commercial</span>
        </div>
        <div class="hero__stat">
          <b>{LOCALITY}</b><span>Studio in South {CITY}<br>serving the whole city</span>
        </div>
      </aside>
    </div>
  </div>
  <div class="scroll-cue" aria-hidden="true">
    <span class="scroll-cue__line"></span><span>Scroll</span>
  </div>
</section>

<section class="section section--tight trust" aria-label="Credentials">
  <div class="container">
    <div class="trust__grid">
      <div class="trust__item" data-anim="rise">
        <span class="trust__k">{RATING} {STARS}</span>
        <span class="trust__v">Average rating from {RATING_N} verified Google reviews</span>
      </div>
      <div class="trust__item" data-anim="rise">
        <span class="trust__k">{LOCALITY}</span>
        <span class="trust__v">Studio in South {CITY}, working across the city</span>
      </div>
      <div class="trust__item" data-anim="rise" data-todo="Add a real figure — years active or projects delivered">
        <span class="trust__k">[00]</span>
        <span class="trust__v">[Years in practice / homes delivered]</span>
      </div>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="svc-h">
  <div class="container">
    <div class="section-head">
      <div>
        <p class="eyebrow" data-anim="fade">What we do</p>
        <h2 class="h2" id="svc-h" data-anim="rise">Four ways<br>we work.</h2>
      </div>
      <p class="lede" data-anim="rise">Whether it is an empty flat, a tired kitchen or a
        floor of offices, the work runs on one schedule with one team accountable for it.</p>
    </div>
  </div>
  <div class="container"><div class="cards">{cards}</div></div>
</section>

<section class="section section--sand" aria-labelledby="work-h">
  <div class="container">
    <div class="section-head">
      <div>
        <p class="eyebrow" data-anim="fade">Selected work</p>
        <h2 class="h2" id="work-h" data-anim="rise">Recent<br>projects.</h2>
      </div>
      <p class="lede" data-anim="rise">A cross-section of homes, kitchens and workspaces.
        <a class="link" href="portfolio.html" style="margin-left:.5rem">View all {I_ARROW}</a></p>
    </div>
    <div class="projects projects--featured">{feat}</div>
  </div>
</section>

{process_section()}

<section class="section" aria-labelledby="rev-h">
  <div class="container">
    <div class="section-head">
      <div>
        <p class="eyebrow" data-anim="fade">What clients say</p>
        <h2 class="h2" id="rev-h" data-anim="rise">Rated {RATING}<br>on Google.</h2>
      </div>
      <div class="rating-band" data-anim="rise">
        <span class="rating-band__score">{RATING}</span>
        <span class="rating-band__meta">
          {STARS}
          <span>{RATING_N} reviews on Google</span>
        </span>
      </div>
    </div>
    <div class="reviews">{reviews}</div>
  </div>
</section>

{cta_band()}
</main>
""" + footer())


def build_portfolio():
    filters = "".join(
        f'<button class="filter" type="button" data-filter="{k}" '
        f'aria-pressed="{"true" if k == "all" else "false"}">{v}</button>'
        for k, v in [("all", "All"), ("residential", "Residential"),
                     ("kitchen", "Modular Kitchen"), ("commercial", "Commercial"),
                     ("renovation", "Renovation")])
    grid = "".join(project_card(i, t, c, im) for i, (t, c, im) in enumerate(PROJECTS))

    return (
        head("portfolio.html", f"Portfolio — {NAME}",
             f"Homes, modular kitchens, workspaces and renovations delivered by {NAME} in {CITY}.")
        + header("portfolio.html")
        + page_hero("Portfolio", "Our work",
                    "Spaces we<br>have finished.",
                    "Filter by the kind of project you are planning. Every image opens larger.",
                    "page-portfolio.jpg")
        + f"""
<main id="main">
<section class="section">
  <div class="container">
    <div class="filters" role="group" aria-label="Filter projects">{filters}</div>
    <div class="projects" data-grid aria-live="polite">{grid}
      <p class="empty-state" data-empty hidden>No projects in this category yet.</p>
    </div>
  </div>
</section>
{cta_band()}
</main>
""" + footer(lightbox=True))


def build_services():
    blocks = []
    for i, (num, name, link, img, blurb, bullets) in enumerate(SERVICES):
        anchor = link.split("#")[1]
        lis = "".join(f"<li>{b}</li>" for b in bullets)
        flip = " services__block--flip" if i % 2 else ""
        blocks.append(f"""
<section class="section{' section--sand' if i % 2 else ''} services__block{flip}"
         id="{anchor}" aria-labelledby="s-{anchor}">
  <div class="container">
    <div class="services__grid">
      <div class="services__media">
        {media(img, name.replace("&amp;", "and") + " by Nilayaa Interiors",
               ar="4/5", speed=(0.92 if i % 2 else 1.06))}
      </div>
      <div class="services__body">
        <p class="eyebrow" data-anim="fade">{num} &mdash; Service</p>
        <h2 class="h2" id="s-{anchor}" data-anim="rise">{name}</h2>
        <p class="lede" data-anim="rise">{blurb}</p>
        <ul class="ticks" data-anim="rise">{lis}</ul>
        <div class="btn-row" data-anim="rise">
          <a class="btn magnetic" href="contact.html">Enquire about this {I_ARROW}</a>
        </div>
      </div>
    </div>
  </div>
</section>""")

    return (
        head("services.html", f"Services — {NAME}",
             f"Full home interiors, modular kitchens and wardrobes, commercial fit-outs "
             f"and renovation across {CITY}.")
        + header("services.html")
        + page_hero("Services", "What we do",
                    "Design, built<br>and delivered.",
                    "Four service lines, one team, one schedule. Every project runs the same "
                    "four stages from first visit to handover.",
                    "page-services.jpg")
        + '<main id="main">' + "".join(blocks) + process_section() + cta_band()
        + "</main>" + footer())


def build_contact():
    opts = "".join(f'<option value="{s[1]}">{s[1]}</option>' for s in SERVICES)
    map_q = f"{NAME}, {LOCALITY}, {CITY}".replace(" ", "+").replace(",", "%2C")

    return (
        head("contact.html", f"Contact — {NAME}",
             f"Book an interior design consultation with {NAME} in {LOCALITY}, {CITY}. "
             f"Call {PHONE_DISP} or message on WhatsApp.")
        + header("contact.html")
        + page_hero("Contact", "Get in touch",
                    "Book a<br>consultation.",
                    "Send the form, message us on WhatsApp, or just call. We usually reply "
                    "the same working day.",
                    "page-contact.jpg")
        + f"""
<main id="main">
<section class="section">
  <div class="container">
    <div class="contact-grid">

      <div data-anim="rise">
        <h2 class="h3" style="margin-bottom:var(--s6)">Tell us about the project</h2>
        <form class="form" data-form novalidate>
          <div class="form__row form__row--2">
            <div class="field">
              <label class="field__label" for="f-name">Name <span class="req">*</span></label>
              <input class="field__input" id="f-name" name="name" type="text"
                     autocomplete="name" required placeholder="Your full name">
              <p class="field__error" data-error-for="f-name"></p>
            </div>
            <div class="field">
              <label class="field__label" for="f-phone">Phone <span class="req">*</span></label>
              <input class="field__input" id="f-phone" name="phone" type="tel"
                     autocomplete="tel" required placeholder="10-digit mobile number">
              <p class="field__error" data-error-for="f-phone"></p>
            </div>
          </div>
          <div class="form__row form__row--2">
            <div class="field">
              <label class="field__label" for="f-email">Email</label>
              <input class="field__input" id="f-email" name="email" type="email"
                     autocomplete="email" placeholder="you@example.com">
              <p class="field__error" data-error-for="f-email"></p>
            </div>
            <div class="field">
              <label class="field__label" for="f-service">Service</label>
              <select class="field__input" id="f-service" name="service">
                <option value="">Not sure yet</option>{opts}
              </select>
            </div>
          </div>
          <div class="field">
            <label class="field__label" for="f-msg">About the space <span class="req">*</span></label>
            <textarea class="field__input" id="f-msg" name="message" required
              placeholder="Size, location, timeline, and anything you already have in mind."></textarea>
            <p class="field__error" data-error-for="f-msg"></p>
          </div>

          <div class="hp" aria-hidden="true">
            <label for="f-company">Company (leave blank)</label>
            <input id="f-company" name="_gotcha" type="text" tabindex="-1" autocomplete="off">
          </div>

          <p class="form__status" data-form-status role="status" aria-live="polite"></p>

          <div class="btn-row" style="margin-top:0">
            <button class="btn btn--brass magnetic" type="submit" data-submit>
              Send enquiry {I_ARROW}
            </button>
            <a class="btn btn--wa" href="{WA_URL}" target="_blank" rel="noopener">{I_WA} WhatsApp instead</a>
          </div>
        </form>
      </div>

      <aside class="studio" data-anim="rise">
        <div class="studio__row">
          <span class="studio__k">Call</span>
          <span class="studio__v"><a href="tel:{PHONE_TEL}">{PHONE_DISP}</a></span>
        </div>
        <div class="studio__row">
          <span class="studio__k">WhatsApp</span>
          <span class="studio__v"><a href="{WA_URL}" target="_blank" rel="noopener">Message the studio</a></span>
        </div>
        <div class="studio__row" data-todo="Add real email address">
          <span class="studio__k">Email</span>
          <span class="studio__v">{EMAIL}</span>
        </div>
        <div class="studio__row" data-todo="Add full street address and PIN code">
          <span class="studio__k">Studio</span>
          <span class="studio__v">[Street address]<br>{LOCALITY}, {CITY}<br>{REGION} [PIN]</span>
        </div>
        <div class="studio__row" data-todo="Confirm working hours">
          <span class="studio__k">Hours</span>
          <span class="studio__v">[Mon&ndash;Sat, 00:00&ndash;00:00]</span>
        </div>
        <div class="studio__row" style="border:0;padding:0">
          <span class="studio__k" style="margin-bottom:var(--s3)">Rating</span>
          <div class="rating-band">
            <span class="rating-band__score">{RATING}</span>
            <span class="rating-band__meta">{STARS}<span>{RATING_N} Google reviews</span></span>
          </div>
        </div>
      </aside>

    </div>
  </div>
</section>

<section class="section section--tight" aria-label="Location">
  <div class="container">
    <div class="map" data-anim="fade" data-todo="Replace with the exact Google Maps place embed">
      <iframe title="Map showing {LOCALITY}, {CITY}" loading="lazy"
        referrerpolicy="no-referrer-when-downgrade"
        src="https://maps.google.com/maps?q={map_q}&output=embed"></iframe>
    </div>
  </div>
</section>
</main>
""" + footer())


# ---------------------------------------------------------------------------
if __name__ == "__main__":
    for fn, builder in [("index.html", build_index), ("portfolio.html", build_portfolio),
                        ("services.html", build_services), ("contact.html", build_contact)]:
        (ROOT / fn).write_text(builder(), encoding="utf-8")
        print(f"  wrote {fn:16s} {(ROOT / fn).stat().st_size / 1024:6.1f} KB")
