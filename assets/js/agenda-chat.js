(function () {
  document.addEventListener('DOMContentLoaded', function () {
    var root = document.querySelector('[data-chat-agenda]');
    if (!root || !window.DDAgenda) return;
    var A = window.DDAgenda;
    var nubo = root.querySelector('[data-chat-nubo]');
    var pregunta = root.querySelector('[data-chat-pregunta]');
    var area = root.querySelector('[data-chat-area]');
    var barra = root.querySelector('[data-chat-barra]');
    var contador = root.querySelector('[data-chat-contador]');
    var atras = root.querySelector('[data-chat-atras]');
    var ticket = root.querySelector('[data-chat-ticket]');
    var dias = A.proximosDias(6);
    var d = { interes: '', para: '', dia: null, hora: '', nombre: '', wa: '', como: '' };
    var paso = 0;

    function chips(opciones, clave) {
      return '<div class="chat-opciones">' + opciones.map(function (o) {
        return '<button type="button" class="chat-op" data-valor="' + o + '" aria-pressed="' + (d[clave] === o ? 'true' : 'false') + '">' + o + '</button>';
      }).join('') + '</div>';
    }
    var PASOS = [
      { q: 'Hola, soy Nubo. ¿Qué te gustaría revisar?', e: 'saluda', render: function () { return chips(['Blanqueamiento', 'Ortodoncia', 'Prótesis', 'Limpieza o revisión', 'No estoy seguro'], 'interes'); }, clave: 'interes' },
      { q: '¿La cita es para ti o para un niño?', e: 'escucha', render: function () { return chips(['Para mí', 'Para un niño'], 'para'); }, clave: 'para' },
      { q: '¿Qué día te queda mejor?', e: 'piensa', render: function () {
          return '<div class="chat-dias">' + dias.map(function (x, i) {
            return '<button type="button" class="dia" data-dia="' + i + '" aria-pressed="' + (d.dia === x ? 'true' : 'false') + '"><span>' + (x.hoy ? 'Hoy' : A.DIAS[x.wd]) + '</span><strong>' + x.fecha.getUTCDate() + '</strong><small>' + A.MESES[x.fecha.getUTCMonth()].slice(0, 3) + '</small></button>';
          }).join('') + '</div>';
        } },
      { q: '¿A qué hora? La valoración dura 45 minutos.', e: 'explica', render: function () {
          var oc = A.ocupadas(d.dia.fecha);
          function grupo(n, l) {
            return '<div class="agenda-horas__grupo"><span>' + n + '</span><div class="chat-opciones">' + l.map(function (h) {
              var no = oc.indexOf(h) > -1 || (d.dia.hoy && A.aMin(h) <= d.dia.min + 30);
              return '<button type="button" class="chat-op chat-op--hora" data-hora="' + h + '" aria-pressed="' + (d.hora === h ? 'true' : 'false') + '"' + (no ? ' disabled' : '') + '>' + h + '</button>';
            }).join('') + '</div></div>';
          }
          return '<div class="agenda-horas">' + grupo('Mañana', A.MANANA) + (d.dia.wd === 6 ? '' : grupo('Tarde', A.TARDE)) + '</div>';
        } },
      { q: '¿Cómo te llamas y a qué WhatsApp te confirmamos?', e: 'escucha', render: function () {
          return '<div class="chat-campos"><div class="campo"><label for="ch-nombre">Tu nombre</label><input id="ch-nombre" type="text" placeholder="Ana López" autocomplete="name" value="' + d.nombre.replace(/"/g, '') + '"><span class="campo__ayuda">Como quieres que te llamemos.</span></div>' +
            '<div class="campo"><label for="ch-wa">WhatsApp</label><input id="ch-wa" type="tel" inputmode="numeric" placeholder="961 123 4567" autocomplete="tel" value="' + d.wa + '"><span class="campo__ayuda">Ahí te confirmamos tu cita.</span></div>' +
            '<button type="button" class="btn btn--primario" data-chat-siguiente>Continuar <svg class="i flecha" aria-hidden="true"><use href="#i-arrow-right"/></svg></button></div>';
        } },
      { q: 'Última: ¿cómo nos conociste?', e: 'guina', render: function () { return chips(['Instagram', 'Facebook', 'Google', 'Me recomendaron', 'Pasé por ahí', 'Otro'], 'como'); }, clave: 'como' }
    ];

    function fechaTxt() { return d.dia ? A.DIAS[d.dia.wd].toLowerCase() + ' ' + d.dia.fecha.getUTCDate() + ' de ' + A.MESES[d.dia.fecha.getUTCMonth()] : ''; }
    function pintarTicket() {
      var filas = [['sparkles', 'Valoración', d.interes], ['users', 'Para', d.para], ['calendar', 'Día', fechaTxt()], ['clock', 'Hora', d.hora], ['mood-smile', 'A nombre de', d.nombre]];
      ticket.innerHTML = filas.map(function (f) {
        return '<li class="' + (f[2] ? 'lleno' : '') + '"><span class="tu-cita__ic"><svg class="i" aria-hidden="true"><use href="#i-' + (f[2] ? 'check' : f[0]) + '"/></svg></span><span>' + f[1] + '</span><strong>' + (f[2] || 'Por elegir') + '</strong></li>';
      }).join('');
    }
    function nuboEstado(e) { if (window.Nubo && nubo.getAttribute('data-nubo') !== e) Nubo.set(nubo, e); }

    function mostrar(n) {
      paso = n;
      var p = PASOS[n];
      pregunta.classList.remove('entra'); void pregunta.offsetWidth;
      pregunta.textContent = n === 4 && d.interes ? 'Perfecto, ' + d.interes.toLowerCase() + ' el ' + fechaTxt() + ' a las ' + d.hora + '. ¿Cómo te llamas y a qué WhatsApp te confirmamos?' : p.q;
      pregunta.classList.add('entra');
      area.innerHTML = p.render();
      area.classList.remove('entra'); void area.offsetWidth; area.classList.add('entra');
      barra.style.transform = 'scaleX(' + ((n + 1) / (PASOS.length + 1)) + ')';
      contador.textContent = 'Paso ' + (n + 1) + ' de ' + PASOS.length;
      atras.hidden = n === 0;
      nuboEstado(n === 1 && d.para === 'Para un niño' ? 'guina' : p.e);
      var foco = area.querySelector('input, button:not([disabled])');
      if (foco && n > 0) foco.focus({ preventScroll: true });
      pintarTicket();
    }

    function avanzar() { setTimeout(function () { mostrar(paso + 1); }, 260); }

    area.addEventListener('click', function (e) {
      var op = e.target.closest('.chat-op');
      var dia = e.target.closest('[data-dia]');
      if (op && !op.disabled) {
        area.querySelectorAll('.chat-op').forEach(function (o) { o.setAttribute('aria-pressed', o === op ? 'true' : 'false'); });
        if (op.hasAttribute('data-hora')) d.hora = op.getAttribute('data-hora');
        else d[PASOS[paso].clave] = op.getAttribute('data-valor');
        pintarTicket();
        if (paso === PASOS.length - 1) return confirmar();
        return avanzar();
      }
      if (dia) {
        area.querySelectorAll('[data-dia]').forEach(function (o) { o.setAttribute('aria-pressed', o === dia ? 'true' : 'false'); });
        var nuevo = dias[+dia.getAttribute('data-dia')];
        if (nuevo !== d.dia) d.hora = '';
        d.dia = nuevo; pintarTicket(); return avanzar();
      }
      if (e.target.closest('[data-chat-siguiente]')) {
        var n = area.querySelector('#ch-nombre'), w = area.querySelector('#ch-wa');
        var okN = n.value.trim().length > 1, okW = A.waOk(w.value);
        n.closest('.campo').classList.toggle('con-error', !okN);
        w.closest('.campo').classList.toggle('con-error', !okW);
        n.closest('.campo').querySelector('.campo__ayuda').textContent = okN ? 'Como quieres que te llamemos.' : 'Escribe tu nombre.';
        w.closest('.campo').querySelector('.campo__ayuda').textContent = okW ? 'Ahí te confirmamos tu cita.' : 'Escribe tu WhatsApp a 10 dígitos.';
        if (okN && okW) { d.nombre = n.value.trim(); d.wa = w.value; pintarTicket(); mostrar(paso + 1); }
      }
    });
    area.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' && e.target.tagName === 'INPUT') { e.preventDefault(); var b = area.querySelector('[data-chat-siguiente]'); if (b) b.click(); }
    });
    atras.addEventListener('click', function () { if (paso > 0) mostrar(paso - 1); });

    function ics() {
      var f = d.dia.fecha, h = d.hora.split(':');
      var ini = new Date(Date.UTC(f.getUTCFullYear(), f.getUTCMonth(), f.getUTCDate(), +h[0] + 6, +h[1]));
      var fin = new Date(ini.getTime() + 45 * 60000);
      function z(x) { return x.toISOString().replace(/[-:]/g, '').replace(/\.\d{3}/, ''); }
      var txt = ['BEGIN:VCALENDAR', 'VERSION:2.0', 'PRODID:-//Dental Diaz//Agenda//ES', 'BEGIN:VEVENT', 'UID:dd-' + Date.now() + '@dentaldiaz', 'DTSTAMP:' + z(new Date()), 'DTSTART:' + z(ini), 'DTEND:' + z(fin),
        'SUMMARY:Valoración en Dental Díaz', 'LOCATION:2da Norte Oriente 438, Terán, Tuxtla Gutiérrez', 'DESCRIPTION:Valoración de 45 minutos. Folio DD-1001.', 'END:VEVENT', 'END:VCALENDAR'].join('\r\n');
      return URL.createObjectURL(new Blob([txt], { type: 'text/calendar' }));
    }

    function confirmar() {
      var msg = 'Hola, soy ' + d.nombre + '. Aparté una valoración el ' + fechaTxt() + ' a las ' + d.hora + ' (' + d.interes + '). Folio DD-1001.';
      root.classList.add('confirmado');
      barra.style.transform = 'scaleX(1)';
      contador.textContent = 'Listo';
      atras.hidden = true;
      pregunta.classList.remove('entra'); void pregunta.offsetWidth;
      pregunta.textContent = '¡Listo, ' + d.nombre.split(' ')[0] + '! Tu valoración quedó apartada. Te esperamos.';
      pregunta.classList.add('entra');
      nuboEstado('celebra');
      area.innerHTML = '<div class="chat-final"><a class="btn btn--whatsapp" target="_blank" rel="noopener" href="https://wa.me/' + A.WA + '?text=' + encodeURIComponent(msg) + '"><svg class="i" aria-hidden="true"><use href="#i-brand-whatsapp"/></svg> Confirmar por WhatsApp</a>' +
        '<a class="btn btn--secundario" download="valoracion-dental-diaz.ics" href="' + ics() + '"><svg class="i" aria-hidden="true"><use href="#i-calendar"/></svg> Agregar a mi calendario</a></div>';
      ticket.insertAdjacentHTML('beforeend', '<li class="lleno"><span class="tu-cita__ic"><svg class="i" aria-hidden="true"><use href="#i-file-text"/></svg></span><span>Folio</span><strong class="tabular">DD-1001</strong></li>');
      var est = root.querySelector('[data-cita-estado]'); if (est) est.textContent = 'Apartada';
      if (window.innerWidth < 1000) A.irA(root); 
      setTimeout(function () { A.confeti(root.querySelector('.chat__escena')); }, 300);
    }

    mostrar(0);
  });
})();
