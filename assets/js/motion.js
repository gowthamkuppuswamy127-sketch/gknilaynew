/* ==========================================================================
   Nilayaa Interiors — motion.js
   All animation. Delete this file and the site still works; it just stops moving.
   Everything animates transform/opacity only, so it stays on the compositor.
   ========================================================================== */
(function () {
  'use strict';

  var html = document.documentElement;

  /* If GSAP did not load, un-hide everything and stop. Never leave the page
     blank because an animation library is missing. */
  function bail(why) {
    html.classList.remove('js-ready');
    html.classList.remove('has-smoother');
    document.querySelectorAll('[data-split]').forEach(function (el) {
      el.style.visibility = 'visible';
    });
    if (why && window.console) console.warn('[nilayaa] motion disabled:', why);
  }

  if (!window.gsap) { bail('gsap not found'); return; }

  try {
    gsap.registerPlugin(ScrollTrigger, ScrollSmoother, SplitText);
  } catch (e) { bail(e.message); return; }

  ScrollTrigger.config({ limitCallbacks: true, ignoreMobileResize: true });

  var REDUCED = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ------------------------------------------------------------------ */
  /* Reduced motion: show everything, wire nothing.                      */
  /* ------------------------------------------------------------------ */
  if (REDUCED) {
    gsap.set('[data-anim]', { opacity: 1, y: 0, scale: 1, clearProps: 'transform' });
    document.querySelectorAll('[data-split]').forEach(function (el) {
      el.style.visibility = 'visible';
    });
    // Header + mobile bar still need to respond to native scroll.
    return;
  }

  var smoother = null;

  /* ------------------------------------------------------------------ */
  /* Smooth scrolling                                                    */
  /* ------------------------------------------------------------------ */
  if (document.getElementById('smooth-wrapper') && document.getElementById('smooth-content')) {
    try {
      smoother = ScrollSmoother.create({
        wrapper: '#smooth-wrapper',
        content: '#smooth-content',
        smooth: 1.15,
        effects: true,          // enables data-speed / data-lag parallax
        smoothTouch: false,     // native scroll on touch — never fight the OS
        normalizeScroll: false,
        ignoreMobileResize: true
      });
      window.__nilayaaSmoother = smoother;
      html.classList.add('has-smoother');
    } catch (e) {
      if (window.console) console.warn('[nilayaa] smoother failed, native scroll:', e.message);
    }
  }

  /* ------------------------------------------------------------------ */
  /* Header + mobile bar, driven off the virtualised scroll position     */
  /* ------------------------------------------------------------------ */
  (function () {
    var header = document.querySelector('[data-header]');
    var bar    = document.querySelector('[data-mobile-bar]');
    if (!header && !bar) return;
    ScrollTrigger.create({
      start: 0,
      end: 'max',
      onUpdate: function (self) {
        var y = self.scroll();
        if (header) header.classList.toggle('is-stuck', y > 40);
        if (bar)    bar.classList.toggle('is-visible', y > 280);
      }
    });
  })();

  /* ------------------------------------------------------------------ */
  /* Scroll-triggered reveals                                            */
  /* ------------------------------------------------------------------ */
  var FROM = {
    rise:  { opacity: 0, y: 38 },
    fade:  { opacity: 0 },
    scale: { opacity: 0, scale: 1.04 }
  };

  function revealBatch(kind) {
    var sel = '[data-anim="' + kind + '"]';
    if (!document.querySelector(sel)) return;
    ScrollTrigger.batch(sel, {
      start: 'top 88%',
      once: true,
      onEnter: function (batch) {
        gsap.fromTo(batch, FROM[kind], {
          opacity: 1, y: 0, scale: 1,
          duration: 0.95,
          ease: 'power3.out',
          stagger: 0.075,
          overwrite: true,
          clearProps: 'willChange'
        });
      }
    });
  }
  ['rise', 'fade', 'scale'].forEach(revealBatch);

  /* Re-stagger a set of elements — used when the portfolio filter changes. */
  window.__nilayaaRestagger = function (els) {
    if (!els || !els.length) return;
    gsap.fromTo(els,
      { opacity: 0, y: 26 },
      { opacity: 1, y: 0, duration: 0.7, ease: 'power3.out', stagger: 0.05, overwrite: true });
  };

  /* ------------------------------------------------------------------ */
  /* Hero: split headline + slow settle on the image                     */
  /* ------------------------------------------------------------------ */
  function runHero() {
    var heads = document.querySelectorAll('[data-split]');

    heads.forEach(function (el) {
      var split;
      try {
        split = new SplitText(el, {
          type: 'lines,chars',
          linesClass: 'split-line',
          aria: 'auto'           // keeps the heading readable to screen readers
        });
      } catch (e) {
        el.style.visibility = 'visible';
        return;
      }
      // Older SplitText builds have no `aria` option — belt and braces.
      if (!el.getAttribute('aria-label')) {
        el.setAttribute('aria-label', (el.textContent || '').trim());
      }
      el.style.visibility = 'visible';

      gsap.from(split.chars, {
        yPercent: 118,
        opacity: 0,
        duration: 1.0,
        ease: 'power4.out',
        stagger: 0.016,
        delay: 0.12
      });
    });

    var heroImg = document.querySelector('[data-hero-img]');
    if (heroImg) {
      gsap.fromTo(heroImg,
        { scale: 1.16 },
        { scale: 1, duration: 2.6, ease: 'power2.out' });
    }

    var cue = document.querySelector('.scroll-cue');
    if (cue) gsap.from(cue, { opacity: 0, duration: 1, delay: 1.1 });

    ScrollTrigger.refresh();
  }

  // Split only once webfonts are in, or the line breaks are computed wrong.
  if (document.fonts && document.fonts.ready) {
    document.fonts.ready.then(runHero).catch(runHero);
    // Failsafe: never leave the headline invisible if fonts.ready never settles.
    setTimeout(function () {
      document.querySelectorAll('[data-split]').forEach(function (el) {
        if (el.style.visibility !== 'visible') { el.style.visibility = 'visible'; }
      });
    }, 2500);
  } else {
    runHero();
  }

  /* ------------------------------------------------------------------ */
  /* Breakpoint-scoped effects                                           */
  /* ------------------------------------------------------------------ */
  var mm = gsap.matchMedia();

  /* Pinned, scrubbed process timeline — desktop only. Pinning on a phone
     costs more than it gives. */
  mm.add('(min-width: 900px)', function () {
    var section = document.querySelector('[data-process]');
    if (!section) return;
    var fill  = section.querySelector('[data-process-fill]');
    var steps = gsap.utils.toArray('[data-step]', section);
    if (!fill || !steps.length) return;

    var proxy = { p: 0 };

    var tl = gsap.timeline({
      scrollTrigger: {
        trigger: section,
        start: 'top top',
        end: '+=' + Math.round(window.innerHeight * 1.5),
        pin: true,
        pinSpacing: true,
        anticipatePin: 1,
        scrub: 0.65,
        invalidateOnRefresh: true
      }
    });

    tl.fromTo(fill, { scaleX: 0 }, { scaleX: 1, ease: 'none' }, 0)
      .fromTo(proxy, { p: 0 }, {
        p: 1,
        ease: 'none',
        onUpdate: function () {
          var active = Math.floor(proxy.p * steps.length - 0.0001);
          steps.forEach(function (s, i) { s.classList.toggle('is-active', i <= active); });
        }
      }, 0);

    return function () {
      steps.forEach(function (s) { s.classList.remove('is-active'); });
      gsap.set(fill, { clearProps: 'all' });
    };
  });

  /* Magnetic pull on primary CTAs — real pointers only. */
  mm.add('(pointer: fine)', function () {
    var els = gsap.utils.toArray('.magnetic');
    var cleanups = [];

    els.forEach(function (el) {
      var xTo = gsap.quickTo(el, 'x', { duration: 0.55, ease: 'power3' });
      var yTo = gsap.quickTo(el, 'y', { duration: 0.55, ease: 'power3' });

      function move(e) {
        var r = el.getBoundingClientRect();
        xTo((e.clientX - (r.left + r.width / 2)) * 0.26);
        yTo((e.clientY - (r.top + r.height / 2)) * 0.32);
      }
      function leave() { xTo(0); yTo(0); }

      el.addEventListener('mousemove', move);
      el.addEventListener('mouseleave', leave);
      cleanups.push(function () {
        el.removeEventListener('mousemove', move);
        el.removeEventListener('mouseleave', leave);
        gsap.set(el, { clearProps: 'transform' });
      });
    });

    return function () { cleanups.forEach(function (fn) { fn(); }); };
  });

  /* ------------------------------------------------------------------ */
  /* Keep measurements honest                                            */
  /* ------------------------------------------------------------------ */
  window.addEventListener('load', function () { ScrollTrigger.refresh(); });

})();
