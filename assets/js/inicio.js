(function () {
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function horarioAhora() {
    var partes = new Intl.DateTimeFormat('es-MX', { timeZone: 'America/Mexico_City', weekday: 'short', hour: '2-digit', minute: '2-digit', hour12: false }).formatToParts(new Date());
    var dia = '', h = 0, m = 0;
    partes.forEach(function (p) {
      if (p.type === 'weekday') dia = p.value.toLowerCase().replace('.', '');
      if (p.type === 'hour') h = parseInt(p.value, 10) % 24;
      if (p.type === 'minute') m = parseInt(p.value, 10);
    });
    var idx = { dom: 0, lun: 1, mar: 2, 'mié': 3, mie: 3, jue: 4, vie: 5, 'sáb': 6, sab: 6 }[dia];
    var t = h + m / 60;
    var bloques = idx >= 1 && idx <= 5 ? [[10, 14], [16, 20]] : idx === 6 ? [[10, 14]] : [];
    for (var i = 0; i < bloques.length; i++) {
      if (t >= bloques[i][0] && t < bloques[i][1]) return { abierto: true, texto: 'Abierto ahora, cierra a las ' + bloques[i][1] + ':00' };
      if (t < bloques[i][0]) return { abierto: false, texto: 'Cerrado, abre hoy a las ' + bloques[i][0] + ':00' };
    }
    var siguiente = idx === 6 || idx === 0 ? 'el lunes' : 'mañana';
    return { abierto: false, texto: 'Cerrado, abre ' + siguiente + ' a las 10:00' };
  }

  document.addEventListener('DOMContentLoaded', function () {
    var nav = document.querySelector('.nav');
    var ham = document.querySelector('.nav__hamburguesa');
    if (nav && ham) {
      ham.addEventListener('click', function () {
        var abierto = nav.classList.toggle('nav--abierto');
        ham.setAttribute('aria-expanded', abierto ? 'true' : 'false');
        ham.querySelector('use').setAttribute('href', abierto ? '#i-x' : '#i-menu-2');
      });
      nav.querySelectorAll('.menu-movil a').forEach(function (a) {
        a.addEventListener('click', function () { nav.classList.remove('nav--abierto'); });
      });
    }

    var est = horarioAhora();
    document.querySelectorAll('[data-abierto]').forEach(function (el) {
      el.textContent = est.texto;
      el.classList.toggle('abierto', est.abierto);
    });

    document.querySelectorAll('[data-selector]').forEach(function (sel) {
      var tabs = sel.querySelectorAll('[data-tab]');
      var paneles = sel.querySelectorAll('[data-panel]');
      var nubo = sel.querySelector('[data-selector-nubo]');
      function activar(id) {
        tabs.forEach(function (t) { var on = t.getAttribute('data-tab') === id; t.setAttribute('aria-selected', on ? 'true' : 'false'); t.tabIndex = on ? 0 : -1; });
        paneles.forEach(function (p) { p.classList.toggle('activo', p.getAttribute('data-panel') === id); });
        var tab = sel.querySelector('[data-tab="' + id + '"]');
        if (nubo && tab && tab.getAttribute('data-estado') && window.Nubo) Nubo.set(nubo, tab.getAttribute('data-estado'));
      }
      tabs.forEach(function (t, i) {
        t.addEventListener('click', function () { activar(t.getAttribute('data-tab')); });
        if (sel.hasAttribute('data-hover')) t.addEventListener('mouseenter', function () { if (window.matchMedia('(hover: hover)').matches) activar(t.getAttribute('data-tab')); });
        t.addEventListener('keydown', function (e) {
          var dir = (e.key === 'ArrowDown' || e.key === 'ArrowRight') ? 1 : (e.key === 'ArrowUp' || e.key === 'ArrowLeft') ? -1 : 0;
          if (!dir) return;
          e.preventDefault();
          var n = tabs[(i + dir + tabs.length) % tabs.length];
          n.focus(); activar(n.getAttribute('data-tab'));
        });
      });
    });

    document.querySelectorAll('[data-miedos]').forEach(function (box) {
      var burbuja = box.querySelector('[data-respuesta]');
      var nubo = box.querySelector('.nubo');
      box.querySelectorAll('[data-miedo]').forEach(function (b) {
        b.addEventListener('click', function () {
          box.querySelectorAll('[data-miedo]').forEach(function (o) { o.setAttribute('aria-pressed', o === b ? 'true' : 'false'); });
          burbuja.classList.remove('entra');
          void burbuja.offsetWidth;
          burbuja.textContent = b.getAttribute('data-miedo');
          burbuja.classList.add('entra');
          if (nubo && b.getAttribute('data-estado')) Nubo.set(nubo, b.getAttribute('data-estado'));
        });
      });
    });

    document.querySelectorAll('[data-voltear]').forEach(function (c) {
      c.addEventListener('click', function () {
        var v = c.classList.toggle('volteada');
        c.setAttribute('aria-pressed', v ? 'true' : 'false');
      });
    });

    var narrador = document.querySelector('[data-narrador]');
    if (narrador && 'IntersectionObserver' in window) {
      var actual = narrador.getAttribute('data-nubo');
      var burb = document.querySelector('[data-narrador-texto]');
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (en) {
          if (!en.isIntersecting) return;
          var est = en.target.getAttribute('data-nubo-estado');
          if (est && est !== actual) { actual = est; Nubo.set(narrador, est); }
          if (burb && en.target.getAttribute('data-nubo-dice')) {
            burb.classList.remove('entra'); void burb.offsetWidth;
            burb.textContent = en.target.getAttribute('data-nubo-dice'); burb.classList.add('entra');
          }
        });
      }, { rootMargin: '-45% 0px -45% 0px' });
      document.querySelectorAll('[data-nubo-estado]').forEach(function (s) { io.observe(s); });
      var relato = narrador.closest('.relato');
      if (relato) new IntersectionObserver(function (en) { document.body.classList.toggle('relato-activo', en[0].isIntersecting); }, { rootMargin: '-20% 0px -30% 0px' }).observe(relato);
    }


    document.querySelectorAll('[data-historia]').forEach(function (sec) {
      var datos = window.HISTORIA || [];
      var marcas = sec.querySelectorAll('[data-historia-marca]');
      var items = sec.querySelectorAll('[data-historia-item]');
      var linea = sec.querySelector('[data-historia-linea]');
      var barraM = sec.querySelector('[data-historia-barra-m]');
      var texto = sec.querySelector('[data-historia-texto]');
      var prop = sec.querySelector('[data-historia-prop]');
      var nubo = sec.querySelector('.nubo');
      var actual = -1;
      function ir(i) {
        if (i === actual || !datos[i]) return;
        actual = i;
        sec.setAttribute('data-paso', i);
        items.forEach(function (li, k) { li.classList.toggle('activo', k === i); li.classList.toggle('hecho', k < i); });
        var f = (i + 1) / datos.length;
        if (linea) linea.style.transform = 'scaleY(' + f + ')';
        if (barraM) barraM.style.transform = 'scaleX(' + f + ')';
        texto.innerHTML = '<span class="historia__contador">Paso ' + (i + 1) + ' de ' + datos.length + '</span><h3>' + datos[i].t + '</h3><p>' + datos[i].d + '</p>';
        texto.classList.remove('cambia'); void texto.offsetWidth; texto.classList.add('cambia');
        if (prop) {
          prop.querySelector('use').setAttribute('href', '#i-' + datos[i].i);
          prop.classList.remove('cambia'); void prop.offsetWidth; prop.classList.add('cambia');
        }
        if (nubo && window.Nubo) Nubo.set(nubo, datos[i].e);
      }
      if ('IntersectionObserver' in window) {
        var io = new IntersectionObserver(function (en) {
          en.forEach(function (e) { if (e.isIntersecting) ir(parseInt(e.target.getAttribute('data-historia-marca'), 10)); });
        }, { rootMargin: '-50% 0px -50% 0px' });
        marcas.forEach(function (m) { io.observe(m); });
      }
      ir(0);
    });
    document.querySelectorAll('[data-pasos]').forEach(function (box) {
      var botones = box.querySelectorAll('[data-paso]');
      var detalles = box.querySelectorAll('[data-detalle]');
      var barra = box.querySelector('[data-progreso]');
      var nubo = box.querySelector('.nubo');
      var i = 0, timer;
      function ir(n, usuario) {
        i = n;
        botones.forEach(function (b, k) { b.setAttribute('aria-current', k === n ? 'step' : 'false'); b.classList.toggle('hecho', k < n); });
        detalles.forEach(function (d, k) { d.classList.toggle('activo', k === n); });
        if (barra) barra.style.transform = 'scaleX(' + ((n + 1) / botones.length) + ')';
        var est = botones[n].getAttribute('data-estado');
        if (nubo && est) Nubo.set(nubo, est);
        if (usuario) clearInterval(timer);
      }
      botones.forEach(function (b, k) { b.addEventListener('click', function () { ir(k, true); }); });
      ir(0);
      if (!reduce && 'IntersectionObserver' in window) {
        var vis = new IntersectionObserver(function (en) {
          en.forEach(function (e) {
            clearInterval(timer);
            if (e.isIntersecting) timer = setInterval(function () { ir((i + 1) % botones.length); }, 4200);
          });
        }, { threshold: 0.4 });
        vis.observe(box);
        box.addEventListener('pointerenter', function () { clearInterval(timer); });
      }
    });

    if (!reduce) {
      document.querySelectorAll('[data-palabras]').forEach(function (h) {
        var html = h.innerHTML;
        var tmp = document.createElement('div'); tmp.innerHTML = html;
        var k = 0;
        function envolver(nodo) {
          Array.prototype.slice.call(nodo.childNodes).forEach(function (n) {
            if (n.nodeType === 3) {
              var frag = document.createDocumentFragment();
              n.textContent.split(/(\s+)/).forEach(function (w) {
                if (!w) return;
                if (/^\s+$/.test(w)) { frag.appendChild(document.createTextNode(w)); return; }
                var o = document.createElement('span'); o.className = 'palabra';
                var in_ = document.createElement('span'); in_.textContent = w; in_.style.animationDelay = (120 + k * 70) + 'ms'; k++;
                o.appendChild(in_); frag.appendChild(o);
              });
              n.parentNode.replaceChild(frag, n);
            } else if (n.nodeType === 1) { envolver(n); }
          });
        }
        envolver(tmp);
        h.innerHTML = tmp.innerHTML;
        h.classList.add('palabras-listas');
      });
    }
  });
})();
