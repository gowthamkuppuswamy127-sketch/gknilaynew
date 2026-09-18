/* ==========================================================================
   Nilayaa Interiors — site.js
   Behaviour only. No animation lives here; see motion.js.
   Everything degrades: if this file fails, the pages are still readable.
   ========================================================================== */
(function () {
  'use strict';

  /* ------------------------------------------------------------------
     CONFIG — paste your Formspree endpoint here and the form goes live.
     Create one free at https://formspree.io  →  "https://formspree.io/f/xxxxxxxx"
     Until then the form stays inert and points people at WhatsApp.
     ------------------------------------------------------------------ */
  var FORMSPREE_ENDPOINT = ''; // e.g. 'https://formspree.io/f/abcdwxyz'

  var $  = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };


  /* ------------------------------------------------------------------ */
  /* Missing photos: drop the <img> so the tonal placeholder shows through.
     `error` does not bubble, hence the capture phase.                    */
  /* ------------------------------------------------------------------ */
  function dropBrokenImage(el) {
    if (!el || !el.classList || !el.classList.contains('media__img')) return;
    var frame = el.closest ? el.closest('.media') : null;
    if (frame) frame.classList.add('media--empty');
    // The lightbox reuses one <img>, so hide it rather than remove it.
    if (el.hasAttribute('data-lb-img')) el.style.display = 'none';
    else el.remove();
  }

  document.addEventListener('error', function (e) { dropBrokenImage(e.target); }, true);

  /* Images above the fold can 404 before this script parses, so their error
     event is never heard. Sweep for any that already failed. */
  function sweepBrokenImages() {
    $$('.media__img').forEach(function (img) {
      if (img.complete && img.naturalWidth === 0 && img.getAttribute('src')) {
        dropBrokenImage(img);
      }
    });
  }
  sweepBrokenImages();
  window.addEventListener('load', sweepBrokenImages);

  /* ------------------------------------------------------------------ */
  /* Footer year                                                         */
  /* ------------------------------------------------------------------ */
  $$('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });

  /* ------------------------------------------------------------------ */
  /* Draft notice — dismissible, remembered for the session              */
  /* ------------------------------------------------------------------ */
  (function () {
    var banner = $('[data-draft-banner]');
    if (!banner) return;
    try {
      if (sessionStorage.getItem('nilayaa:draft-dismissed') === '1') banner.hidden = true;
    } catch (e) { /* private mode — just show it */ }
    var btn = $('[data-draft-dismiss]', banner);
    if (btn) btn.addEventListener('click', function () {
      banner.hidden = true;
      try { sessionStorage.setItem('nilayaa:draft-dismissed', '1'); } catch (e) {}
    });
  })();

  /* ------------------------------------------------------------------ */
  /* Header state on scroll                                              */
  /* ------------------------------------------------------------------ */
  (function () {
    var header = $('[data-header]');
    if (!header) return;
    var ticking = false;
    function apply() {
      header.classList.toggle('is-stuck', (window.scrollY || window.pageYOffset) > 40);
      ticking = false;
    }
    // ScrollSmoother virtualises scroll, so motion.js drives this instead
    // when it is active. This listener is the fallback.
    window.addEventListener('scroll', function () {
      if (document.documentElement.classList.contains('has-smoother')) return;
      if (!ticking) { ticking = true; requestAnimationFrame(apply); }
    }, { passive: true });
    apply();
    window.__nilayaaHeaderSync = apply;
  })();

  /* ------------------------------------------------------------------ */
  /* Mobile call/WhatsApp bar — appears once you are past the hero       */
  /* ------------------------------------------------------------------ */
  (function () {
    var bar = $('[data-mobile-bar]');
    if (!bar) return;
    function sync(y) {
      bar.classList.toggle('is-visible', (y === undefined ? window.scrollY : y) > 280);
    }
    window.addEventListener('scroll', function () {
      if (document.documentElement.classList.contains('has-smoother')) return;
      sync();
    }, { passive: true });
    sync();
    window.__nilayaaBarSync = sync;
  })();

  /* ------------------------------------------------------------------ */
  /* Dialog helper — shared open/close with transition + scroll lock     */
  /* ------------------------------------------------------------------ */
  function openDialog(dlg) {
    if (!dlg || dlg.open) return;
    if (typeof dlg.showModal === 'function') dlg.showModal();
    else dlg.setAttribute('open', '');
    document.body.style.overflow = 'hidden';
    if (window.__nilayaaSmoother) window.__nilayaaSmoother.paused(true);
    requestAnimationFrame(function () { dlg.classList.add('is-open'); });
  }

  function closeDialog(dlg) {
    if (!dlg || !dlg.open) return;
    dlg.classList.remove('is-open');
    var done = false;
    function finish() {
      if (done) return;
      done = true;
      dlg.removeEventListener('transitionend', finish);
      if (typeof dlg.close === 'function') dlg.close();
      else dlg.removeAttribute('open');
      document.body.style.overflow = '';
      if (window.__nilayaaSmoother) window.__nilayaaSmoother.paused(false);
    }
    dlg.addEventListener('transitionend', finish);
    setTimeout(finish, 600); // guarantee close even if no transition fires
  }

  /* ------------------------------------------------------------------ */
  /* Mobile drawer                                                       */
  /* ------------------------------------------------------------------ */
  (function () {
    var drawer = $('[data-drawer]');
    if (!drawer) return;
    var opener = $('[data-drawer-open]');

    $$('[data-drawer-open]').forEach(function (b) {
      b.addEventListener('click', function () { openDialog(drawer); });
    });
    $$('[data-drawer-close]').forEach(function (b) {
      b.addEventListener('click', function () { closeDialog(drawer); });
    });
    // Esc is native on <dialog>; intercept so the slide-out still plays.
    drawer.addEventListener('cancel', function (e) {
      e.preventDefault();
      closeDialog(drawer);
    });
    drawer.addEventListener('close', function () {
      document.body.style.overflow = '';
      if (window.__nilayaaSmoother) window.__nilayaaSmoother.paused(false);
      if (opener) opener.focus();
    });
    // Click on the backdrop (the dialog element itself) closes it.
    drawer.addEventListener('click', function (e) {
      if (e.target === drawer) closeDialog(drawer);
    });
    // Navigating away should not leave it open on back-nav.
    $$('.drawer__link', drawer).forEach(function (a) {
      a.addEventListener('click', function () { closeDialog(drawer); });
    });
  })();

  /* ------------------------------------------------------------------ */
  /* Portfolio filter                                                    */
  /* ------------------------------------------------------------------ */
  (function () {
    var grid = $('[data-grid]');
    if (!grid) return;
    var buttons  = $$('[data-filter]');
    var projects = $$('[data-project]', grid);
    var empty    = $('[data-empty]', grid);

    function apply(cat) {
      var shown = 0;
      projects.forEach(function (p) {
        var match = cat === 'all' || p.getAttribute('data-cat') === cat;
        p.hidden = !match;
        if (match) shown++;
      });
      if (empty) empty.hidden = shown !== 0;
      buttons.forEach(function (b) {
        b.setAttribute('aria-pressed', String(b.getAttribute('data-filter') === cat));
      });
      // Re-run the entrance animation on whatever is now visible.
      if (window.__nilayaaRestagger) window.__nilayaaRestagger(projects.filter(function (p) { return !p.hidden; }));
      if (window.ScrollTrigger) window.ScrollTrigger.refresh();
    }

    buttons.forEach(function (b) {
      b.addEventListener('click', function () { apply(b.getAttribute('data-filter')); });
    });
  })();

  /* ------------------------------------------------------------------ */
  /* Lightbox                                                            */
  /* ------------------------------------------------------------------ */
  (function () {
    var lb = $('[data-lightbox]');
    if (!lb) return;
    var lbImg  = $('[data-lb-img]', lb);
    var elTag  = $('[data-lb-tag]', lb);
    var elTtl  = $('[data-lb-title]', lb);
    var elCnt  = $('[data-lb-count]', lb);
    var items  = [];
    var index  = 0;
    var lastFocus = null;

    function visible() {
      return $$('[data-project]').filter(function (p) { return !p.hidden; });
    }

    function render() {
      var p = items[index];
      if (!p) return;
      var src = p.getAttribute('data-img');
      var frame = $('[data-lb-media]', lb);
      if (frame) {
        frame.classList.remove('media--empty');
        frame.setAttribute('data-ph', src.split('/').pop());
      }
      if (lbImg) {
        lbImg.alt = p.getAttribute('data-title') || '';
        lbImg.src = src;
        lbImg.style.display = '';
      }
      elTag.textContent = p.getAttribute('data-tag') || '';
      elTtl.textContent = p.getAttribute('data-title') || '';
      elCnt.textContent = (index + 1) + ' / ' + items.length;
    }

    function open(p) {
      items = visible();
      index = Math.max(0, items.indexOf(p));
      lastFocus = document.activeElement;
      render();
      openDialog(lb);
    }

    function step(d) {
      if (!items.length) return;
      index = (index + d + items.length) % items.length;
      render();
    }

    document.addEventListener('click', function (e) {
      var btn = e.target.closest ? e.target.closest('[data-project]') : null;
      if (btn) { e.preventDefault(); open(btn); }
    });

    $$('[data-lb-close]', lb).forEach(function (b) {
      b.addEventListener('click', function () { closeDialog(lb); });
    });
    $('[data-lb-prev]', lb).addEventListener('click', function () { step(-1); });
    $('[data-lb-next]', lb).addEventListener('click', function () { step(1); });

    lb.addEventListener('cancel', function (e) { e.preventDefault(); closeDialog(lb); });
    lb.addEventListener('close', function () {
      document.body.style.overflow = '';
      if (window.__nilayaaSmoother) window.__nilayaaSmoother.paused(false);
      if (lastFocus && lastFocus.focus) lastFocus.focus();
    });
    lb.addEventListener('click', function (e) { if (e.target === lb) closeDialog(lb); });

    document.addEventListener('keydown', function (e) {
      if (!lb.open) return;
      if (e.key === 'ArrowLeft')  { e.preventDefault(); step(-1); }
      if (e.key === 'ArrowRight') { e.preventDefault(); step(1); }
    });
  })();

  /* ------------------------------------------------------------------ */
  /* Contact form                                                        */
  /* ------------------------------------------------------------------ */
  (function () {
    var form = $('[data-form]');
    if (!form) return;
    var status = $('[data-form-status]', form);
    var submit = $('[data-submit]', form);

    var RULES = {
      'f-name':  function (v) { return v.trim().length >= 2 || 'Please enter your name.'; },
      'f-phone': function (v) {
        var digits = v.replace(/\D/g, '');
        return (digits.length >= 10 && digits.length <= 13) || 'Enter a valid phone number.';
      },
      'f-email': function (v) {
        if (!v.trim()) return true; // optional
        return /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v.trim()) || 'Enter a valid email address.';
      },
      'f-msg':   function (v) { return v.trim().length >= 10 || 'A sentence or two is plenty.'; }
    };

    function setError(id, msg) {
      var field = document.getElementById(id);
      var slot  = $('[data-error-for="' + id + '"]', form);
      if (!field) return;
      if (msg) {
        field.setAttribute('aria-invalid', 'true');
        if (slot) { slot.textContent = msg; field.setAttribute('aria-describedby', slot.id || ''); }
      } else {
        field.removeAttribute('aria-invalid');
        if (slot) slot.textContent = '';
      }
    }

    function validate() {
      var firstBad = null;
      Object.keys(RULES).forEach(function (id) {
        var el = document.getElementById(id);
        if (!el) return;
        var res = RULES[id](el.value);
        var msg = res === true ? '' : res;
        setError(id, msg);
        if (msg && !firstBad) firstBad = el;
      });
      return firstBad;
    }

    Object.keys(RULES).forEach(function (id) {
      var el = document.getElementById(id);
      if (!el) return;
      el.addEventListener('blur', function () {
        var res = RULES[id](el.value);
        setError(id, res === true ? '' : res);
      });
      el.addEventListener('input', function () {
        if (el.getAttribute('aria-invalid') === 'true') {
          var res = RULES[id](el.value);
          if (res === true) setError(id, '');
        }
      });
    });

    function say(state, text) {
      if (!status) return;
      status.setAttribute('data-state', state);
      status.textContent = text;
    }

    form.addEventListener('submit', function (e) {
      e.preventDefault();

      var bad = validate();
      if (bad) { say('err', 'Please correct the highlighted fields.'); bad.focus(); return; }

      // Honeypot: real people leave this blank.
      var hp = form.querySelector('[name="_gotcha"]');
      if (hp && hp.value) { say('ok', 'Thank you — we will be in touch.'); form.reset(); return; }

      if (!FORMSPREE_ENDPOINT) {
        say('info',
          'The form is not connected to an inbox yet. Add your Formspree endpoint to ' +
          'FORMSPREE_ENDPOINT in assets/js/site.js — or message us on WhatsApp now.');
        return;
      }

      submit.setAttribute('aria-busy', 'true');
      say('info', 'Sending…');

      fetch(FORMSPREE_ENDPOINT, {
        method: 'POST',
        headers: { Accept: 'application/json' },
        body: new FormData(form)
      }).then(function (r) {
        if (!r.ok) throw new Error('HTTP ' + r.status);
        form.reset();
        say('ok', 'Thank you — your enquiry is in. We usually reply the same working day.');
      }).catch(function () {
        say('err',
          'Something went wrong sending that. Please call us on ' +
          (document.querySelector('a[href^="tel:"]') || {}).textContent +
          ' or message on WhatsApp.');
      }).then(function () {
        submit.removeAttribute('aria-busy');
      });
    });
  })();

})();
