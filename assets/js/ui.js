(function () {
  document.addEventListener('DOMContentLoaded', function () {
    var nav = document.querySelector('.nav');
    if (nav) {
      var onScroll = function () { nav.classList.toggle('con-borde', window.scrollY > 8); };
      onScroll();
      window.addEventListener('scroll', onScroll, { passive: true });
    }

    var reveals = document.querySelectorAll('.revela');
    if ('IntersectionObserver' in window) {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (en) {
          if (en.isIntersecting) { en.target.classList.add('visible'); io.unobserve(en.target); }
        });
      }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
      reveals.forEach(function (el) { io.observe(el); });
    } else {
      reveals.forEach(function (el) { el.classList.add('visible'); });
    }
    document.querySelectorAll('[data-escalonar]').forEach(function (group) {
      Array.prototype.forEach.call(group.children, function (child, i) {
        child.style.setProperty('--retraso', (i * 70) + 'ms');
      });
    });

    document.querySelectorAll('.faq__pregunta').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var item = btn.closest('.faq__item');
        var open = !item.classList.contains('abierto');
        item.parentNode.querySelectorAll('.faq__item.abierto').forEach(function (o) { if (o !== item) { o.classList.remove('abierto'); o.querySelector('.faq__pregunta').setAttribute('aria-expanded', 'false'); } });
        item.classList.toggle('abierto', open);
        btn.setAttribute('aria-expanded', open ? 'true' : 'false');
      });
    });

    document.querySelectorAll('[data-chips]').forEach(function (group) {
      var multi = group.getAttribute('data-chips') === 'multi';
      group.addEventListener('click', function (e) {
        var chip = e.target.closest('.chip');
        if (!chip || chip.disabled) return;
        if (!multi) group.querySelectorAll('.chip').forEach(function (c) { if (c !== chip) c.setAttribute('aria-pressed', 'false'); });
        chip.setAttribute('aria-pressed', chip.getAttribute('aria-pressed') === 'true' && multi ? 'false' : 'true');
        group.dispatchEvent(new CustomEvent('cambio', { detail: chip.getAttribute('data-valor') || chip.textContent.trim() }));
      });
    });
  });
})();
