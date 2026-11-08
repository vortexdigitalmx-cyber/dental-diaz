(function () {
  var NS = 'http://www.w3.org/2000/svg';
  var reduceMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var instances = [];

  function build(el) {
    var state = el.getAttribute('data-nubo') || 'saluda';
    var markup = (window.NUBO_STATES || {})[state];
    if (!markup) return;
    var isHero = state === 'hero';
    var svg = document.createElementNS(NS, 'svg');
    svg.setAttribute('viewBox', isHero ? '64 28 310 147' : '0 0 456 390');
    svg.setAttribute('role', 'img');
    svg.setAttribute('aria-label', el.getAttribute('aria-label') || 'Nubo, la mascota de Dental Díaz');
    if (isHero) svg.style.overflow = 'hidden';
    svg.innerHTML = '<g class="n-respira' + (el.hasAttribute('data-entrar') ? ' entrar' : '') + '">' + markup + '</g>';
    el.innerHTML = '';
    el.appendChild(svg);

    svg.querySelectorAll('.n-ojos ellipse').forEach(function (e) {
      var f = (e.getAttribute('fill') || '').toUpperCase();
      e.classList.add(f === '#303B5B' ? 'pupila' : 'ojo-blanco');
    });
    if (el.hasAttribute('data-saluda') && (state === 'saluda' || state === 'guina')) {
      var arm = svg.querySelector('.n-brazos path');
      if (arm) arm.classList.add('brazo-saluda');
    }
    el._hasEyes = svg.querySelectorAll('.pupila').length > 0;
    el._svg = svg;
    el._follow = el.hasAttribute('data-mirada');
    el._max = isHero ? 7 : 5;
  }

  function scheduleBlink(el) {
    if (reduceMotion) return;
    clearTimeout(el._blinkT);
    el._blinkT = setTimeout(function () {
      if (el._hasEyes) {
        el.classList.add('parpadea');
        setTimeout(function () { el.classList.remove('parpadea'); }, 150);
        if (Math.random() < 0.18) setTimeout(function () {
          el.classList.add('parpadea');
          setTimeout(function () { el.classList.remove('parpadea'); }, 130);
        }, 320);
      }
      scheduleBlink(el);
    }, 2600 + Math.random() * 3400);
  }

  function onPointer(x, y) {
    instances.forEach(function (el) {
      if (!el._follow || !el._svg) return;
      var r = el._svg.getBoundingClientRect();
      var cx = r.left + r.width / 2, cy = r.top + r.height * 0.4;
      var dx = x - cx, dy = y - cy;
      var d = Math.sqrt(dx * dx + dy * dy) || 1;
      var k = Math.min(1, d / 320);
      el._svg.style.setProperty('--px', (dx / d * el._max * k).toFixed(2) + 'px');
      el._svg.style.setProperty('--py', (dy / d * el._max * k).toFixed(2) + 'px');
    });
  }

  window.Nubo = {
    mount: function (root) {
      (root || document).querySelectorAll('[data-nubo]').forEach(function (el) {
        build(el);
        if (instances.indexOf(el) === -1) instances.push(el);
        scheduleBlink(el);
      });
    },
    set: function (el, state) {
      el.setAttribute('data-nubo', state);
      el.setAttribute('data-entrar', '');
      build(el);
    }
  };

  if (!reduceMotion) {
    window.addEventListener('pointermove', function (e) { onPointer(e.clientX, e.clientY); }, { passive: true });
  }
  document.addEventListener('DOMContentLoaded', function () { window.Nubo.mount(); });
})();
