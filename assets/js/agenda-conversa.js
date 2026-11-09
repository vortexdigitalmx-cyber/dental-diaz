(function () {
  document.addEventListener('DOMContentLoaded', function () {
    var root = document.querySelector('[data-conv]');
    if (!root || !window.DDAgenda) return;
    var A = window.DDAgenda;
    var hilo = root.querySelector('[data-hilo]');
    var entrada = root.querySelector('[data-entrada]');
    var contador = root.querySelector('[data-conv-contador]');
    var nubos = root.querySelectorAll('[data-conv-nubo]');
    var dias = A.proximosDias(6);
    var d = { interes: '', para: '', dia: null, hora: '', nombre: '', wa: '', como: '' };
    var paso = 0, ocupado = false;

    function fechaTxt() { return d.dia ? A.DIAS[d.dia.wd].toLowerCase() + ' ' + d.dia.fecha.getUTCDate() + ' de ' + A.MESES[d.dia.fecha.getUTCMonth()] : ''; }
    function esc(t) { return String(t).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
    function chips(ops, clave) { return '<div class="conv-ops">' + ops.map(function (o) { return '<button type="button" class="chat-op" data-valor="' + o + '" data-clave="' + clave + '">' + o + '</button>'; }).join('') + '</div>'; }

    var PASOS = [
      { q: function () { return ['Hola, soy Nubo. Te ayudo a apartar tu valoración en menos de un minuto.', '¿Qué te gustaría revisar?']; }, e: 'saluda', r: function () { return chips(['Blanqueamiento', 'Ortodoncia', 'Prótesis', 'Limpieza o revisión', 'No estoy seguro'], 'interes'); }, v: function () { return d.interes; } },
      { q: function () { return [d.interes === 'No estoy seguro' ? 'Sin problema, en la valoración lo vemos juntos.' : 'Buena elección.', '¿La cita es para ti o para un niño?']; }, e: 'escucha', r: function () { return chips(['Para mí', 'Para un niño'], 'para'); }, v: function () { return d.para; } },
      { q: function () { return [d.para === 'Para un niño' ? 'Le damos el tiempo que necesite, a su ritmo.' : 'Perfecto.', '¿Qué día te queda mejor?']; }, e: 'piensa', r: function () {
          return '<div class="conv-dias">' + dias.map(function (x, i) { return '<button type="button" class="dia" data-dia="' + i + '"><span>' + (x.hoy ? 'Hoy' : A.DIAS[x.wd]) + '</span><strong>' + x.fecha.getUTCDate() + '</strong><small>' + A.MESES[x.fecha.getUTCMonth()].slice(0, 3) + '</small></button>'; }).join('') + '</div>';
        }, v: function () { return fechaTxt(); } },
      { q: function () { return ['¿A qué hora el ' + fechaTxt() + '? La valoración dura 45 minutos.']; }, e: 'explica', r: function () {
          var oc = A.ocupadas(d.dia.fecha);
          function g(n, l) { return '<div class="conv-horas__g"><span>' + n + '</span><div class="conv-ops">' + l.map(function (h) { var no = oc.indexOf(h) > -1 || (d.dia.hoy && A.aMin(h) <= d.dia.min + 30); return '<button type="button" class="chat-op chat-op--hora" data-hora="' + h + '"' + (no ? ' disabled' : '') + '>' + h + '</button>'; }).join('') + '</div></div>'; }
          return '<div class="conv-horas">' + g('Mañana', A.MANANA) + (d.dia.wd === 6 ? '' : g('Tarde', A.TARDE)) + '</div>';
        }, v: function () { return d.hora; } },
      { q: function () { return ['Listo, ' + d.interes.toLowerCase() + ' el ' + fechaTxt() + ' a las ' + d.hora + '.', '¿A nombre de quién y a qué WhatsApp te confirmamos?']; }, e: 'escucha', r: function () {
          return '<div class="conv-campos"><div class="campo"><label for="cv-n">Nombre</label><input id="cv-n" type="text" placeholder="Ana López" autocomplete="name" value="' + esc(d.nombre) + '"></div><div class="campo"><label for="cv-w">WhatsApp</label><input id="cv-w" type="tel" inputmode="numeric" placeholder="961 123 4567" autocomplete="tel" value="' + esc(d.wa) + '"></div><button type="button" class="btn btn--primario conv-enviar" data-enviar aria-label="Enviar"><svg class="i" aria-hidden="true"><use href="#i-arrow-right"/></svg></button></div><span class="conv-error" data-error></span>';
        }, v: function () { return d.nombre + ' · ' + d.wa; } },
      { q: function () { return ['Gracias, ' + d.nombre.split(' ')[0] + '. Última pregunta: ¿cómo nos conociste?']; }, e: 'guina', r: function () { return chips(['Instagram', 'Facebook', 'Google', 'Me recomendaron', 'Pasé por ahí', 'Otro'], 'como'); }, v: function () { return d.como; } }
    ];

    function nuboEstado(e) { nubos.forEach(function (n) { if (window.Nubo && n.getAttribute('data-nubo') !== e) Nubo.set(n, e); }); }
    function bajar() { requestAnimationFrame(function () { hilo.scrollTo({ top: hilo.scrollHeight, behavior: 'smooth' }); }); setTimeout(function () { hilo.scrollTop = hilo.scrollHeight; }, 420); }
    function burbujaNubo(txt, extra) {
      var b = document.createElement('div'); b.className = 'msg msg--nubo' + (extra ? ' ' + extra : ''); b.innerHTML = txt; b.setAttribute('data-paso', paso);
      hilo.appendChild(b); bajar(); return b;
    }
    function escribiendo(cb, ms) {
      var t = document.createElement('div'); t.className = 'msg msg--nubo msg--escribe'; t.innerHTML = '<i></i><i></i><i></i>';
      hilo.appendChild(t); bajar();
      setTimeout(function () { t.remove(); cb(); }, ms || 650);
    }
    function preguntar(n) {
      paso = n; ocupado = true;
      entrada.innerHTML = ''; entrada.classList.remove('lista');
      contador.textContent = 'Paso ' + (n + 1) + ' de ' + PASOS.length;
      nuboEstado(PASOS[n].e);
      var textos = PASOS[n].q(), k = 0;
      (function sig() {
        escribiendo(function () {
          burbujaNubo(esc(textos[k]));
          k++;
          if (k < textos.length) sig();
          else { entrada.innerHTML = PASOS[n].r(); entrada.classList.add('lista'); ocupado = false; bajar(); var f = entrada.querySelector('input'); if (f && window.innerWidth > 900) f.focus({ preventScroll: true }); }
        }, k === 0 ? 700 : 520);
      })();
    }
    function responder(txt) {
      var b = document.createElement('div'); b.className = 'msg msg--yo'; b.setAttribute('data-paso', paso);
      b.innerHTML = '<span>' + esc(txt) + '</span>' + (paso < PASOS.length ? '<button type="button" class="msg__cambiar" data-cambiar="' + paso + '">Cambiar</button>' : '');
      hilo.appendChild(b); bajar();
      entrada.innerHTML = ''; entrada.classList.remove('lista');
      if (paso === PASOS.length - 1) return setTimeout(confirmar, 300);
      setTimeout(function () { preguntar(paso + 1); }, 250);
    }

    entrada.addEventListener('click', function (e) {
      if (ocupado) return;
      var op = e.target.closest('.chat-op'), dia = e.target.closest('[data-dia]');
      if (op && !op.disabled) {
        if (op.hasAttribute('data-hora')) d.hora = op.getAttribute('data-hora');
        else d[op.getAttribute('data-clave')] = op.getAttribute('data-valor');
        return responder(PASOS[paso].v());
      }
      if (dia) { var nuevo = dias[+dia.getAttribute('data-dia')]; if (nuevo !== d.dia) d.hora = ''; d.dia = nuevo; return responder(fechaTxt()); }
      if (e.target.closest('[data-enviar]')) {
        var n = entrada.querySelector('#cv-n'), w = entrada.querySelector('#cv-w');
        var okN = n.value.trim().length > 1, okW = A.waOk(w.value);
        n.closest('.campo').classList.toggle('con-error', !okN); w.closest('.campo').classList.toggle('con-error', !okW);
        entrada.querySelector('[data-error]').textContent = !okN ? 'Escribe tu nombre.' : !okW ? 'Escribe tu WhatsApp a 10 dígitos.' : '';
        if (okN && okW) { d.nombre = n.value.trim(); d.wa = w.value.trim(); responder(PASOS[paso].v()); }
        else nuboEstado('piensa');
      }
    });
    entrada.addEventListener('keydown', function (e) { if (e.key === 'Enter' && e.target.tagName === 'INPUT') { e.preventDefault(); var b = entrada.querySelector('[data-enviar]'); if (b) b.click(); } });
    entrada.addEventListener('input', function (e) { var c = e.target.closest('.campo'); if (c) c.classList.remove('con-error'); });
    hilo.addEventListener('click', function (e) {
      var c = e.target.closest('[data-cambiar]');
      if (!c || ocupado || root.classList.contains('confirmado')) return;
      var n = +c.getAttribute('data-cambiar');
      Array.prototype.slice.call(hilo.children).forEach(function (m) { if (+m.getAttribute('data-paso') >= n) m.remove(); });
      paso = n; ocupado = true;
      burbujaNubo('Va, lo cambiamos.');
      setTimeout(function () { entrada.innerHTML = PASOS[n].r(); entrada.classList.add('lista'); contador.textContent = 'Paso ' + (n + 1) + ' de ' + PASOS.length; nuboEstado(PASOS[n].e); ocupado = false; }, 350);
    });

    function ics() {
      var f = d.dia.fecha, h = d.hora.split(':');
      var ini = new Date(Date.UTC(f.getUTCFullYear(), f.getUTCMonth(), f.getUTCDate(), +h[0] + 6, +h[1])), fin = new Date(ini.getTime() + 45 * 60000);
      function z(x) { return x.toISOString().replace(/[-:]/g, '').replace(/\.\d{3}/, ''); }
      var txt = ['BEGIN:VCALENDAR', 'VERSION:2.0', 'PRODID:-//Dental Diaz//Agenda//ES', 'BEGIN:VEVENT', 'UID:dd-' + Date.now() + '@dentaldiaz', 'DTSTAMP:' + z(new Date()), 'DTSTART:' + z(ini), 'DTEND:' + z(fin), 'SUMMARY:Valoración en Dental Díaz', 'LOCATION:2da Norte Oriente 438, Terán, Tuxtla Gutiérrez', 'DESCRIPTION:Valoración de 45 minutos. Folio DD-1001.', 'END:VEVENT', 'END:VCALENDAR'].join('\r\n');
      return URL.createObjectURL(new Blob([txt], { type: 'text/calendar' }));
    }
    function confirmar() {
      paso = PASOS.length; ocupado = true;
      root.classList.add('confirmado');
      contador.textContent = 'Listo';
      hilo.querySelectorAll('.msg__cambiar').forEach(function (b) { b.remove(); });
      nuboEstado('celebra');
      var msg = 'Hola, soy ' + d.nombre + '. Aparté una valoración el ' + fechaTxt() + ' a las ' + d.hora + ' (' + d.interes + '). Folio DD-1001.';
      escribiendo(function () {
        burbujaNubo('¡Listo, ' + esc(d.nombre.split(' ')[0]) + '! Tu valoración quedó apartada. Te esperamos.');
        escribiendo(function () {
          var card = burbujaNubo('<div class="conv-resumen"><div class="conv-resumen__cab"><strong>Valoración apartada</strong><span class="tabular">DD-1001</span></div><ul><li><span>Día</span><strong>' + fechaTxt() + '</strong></li><li><span>Hora</span><strong>' + d.hora + '</strong></li><li><span>Valoración</span><strong>' + esc(d.interes) + (d.para === 'Para un niño' ? ', niño' : '') + '</strong></li><li><span>Dónde</span><strong>2da Norte Oriente #438, Terán</strong></li></ul></div>', 'msg--tarjeta');
          entrada.innerHTML = '<div class="conv-final"><a class="btn btn--whatsapp" target="_blank" rel="noopener" href="https://wa.me/' + A.WA + '?text=' + encodeURIComponent(msg) + '"><svg class="i" aria-hidden="true"><use href="#i-brand-whatsapp"/></svg> Confirmar por WhatsApp</a><a class="btn btn--secundario" download="valoracion-dental-diaz.ics" href="' + ics() + '"><svg class="i" aria-hidden="true"><use href="#i-calendar"/></svg> Agregar a mi calendario</a></div>';
          entrada.classList.add('lista'); bajar();
          A.confeti(card);
        }, 700);
      }, 600);
    }

    var arrancado = false;
    function arrancar() { if (arrancado) return; arrancado = true; preguntar(0); }
    if ('IntersectionObserver' in window) {
      var io = new IntersectionObserver(function (es) { if (es[0].isIntersecting) { arrancar(); io.disconnect(); } }, { threshold: 0.35 });
      io.observe(root);
    } else arrancar();
  });
})();
