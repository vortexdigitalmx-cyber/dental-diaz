(function () {
  var DIAS = ['Dom', 'Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb'];
  var MESES = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'];
  var MANANA = ['10:00', '10:45', '11:30', '12:15', '13:00'];
  var TARDE = ['16:00', '16:45', '17:30', '18:15', '19:00'];
  var WA = '529611385698';

  function hoyMx() {
    var p = new Intl.DateTimeFormat('en-CA', { timeZone: 'America/Mexico_City', year: 'numeric', month: '2-digit', day: '2-digit', hour: '2-digit', minute: '2-digit', hour12: false }).formatToParts(new Date());
    var o = {}; p.forEach(function (x) { o[x.type] = x.value; });
    return { fecha: new Date(Date.UTC(+o.year, +o.month - 1, +o.day)), min: (+o.hour % 24) * 60 + (+o.minute) };
  }
  function proximosDias(n) {
    var h = hoyMx(), out = [], d = new Date(h.fecha);
    while (out.length < n) {
      var wd = d.getUTCDay();
      if (wd !== 0) out.push({ fecha: new Date(d), wd: wd, hoy: out.length === 0 && d.getTime() === h.fecha.getTime(), min: h.min });
      d.setUTCDate(d.getUTCDate() + 1);
    }
    return out;
  }
  function ocupadas(fecha) {
    var s = fecha.toISOString().slice(0, 10), x = 0;
    for (var i = 0; i < s.length; i++) x = (x * 31 + s.charCodeAt(i)) % 9973;
    var todas = MANANA.concat(TARDE), r = [];
    for (var k = 0; k < 3; k++) r.push(todas[(x + k * 7) % todas.length]);
    return r;
  }
  function aMin(h) { var p = h.split(':'); return +p[0] * 60 + +p[1]; }

  function init(form) {
    var caja = form.closest('[data-agenda]');
    var nubo = caja.querySelector('.agenda-lado .nubo');
    var diasBox = form.querySelector('[data-dias]');
    var horasBox = form.querySelector('[data-horas]');
    var dias = proximosDias(6);
    var estado = { interes: '', para: '', dia: null, hora: '', como: '' };

    diasBox.innerHTML = dias.map(function (d, i) {
      return '<button type="button" class="dia" data-i="' + i + '" aria-pressed="false"><span>' + (d.hoy ? 'Hoy' : DIAS[d.wd]) + '</span><strong>' + d.fecha.getUTCDate() + '</strong><small>' + MESES[d.fecha.getUTCMonth()].slice(0, 3) + '</small></button>';
    }).join('');

    function pintarHoras() {
      if (!estado.dia) { horasBox.innerHTML = '<p class="texto chico" style="margin:0">Elige un día para ver los horarios.</p>'; return; }
      var d = estado.dia, oc = ocupadas(d.fecha);
      function grupo(nombre, lista) {
        return '<div class="agenda-horas__grupo"><span>' + nombre + '</span><div class="chips">' + lista.map(function (h) {
          var no = oc.indexOf(h) > -1 || (d.hoy && aMin(h) <= d.min + 30);
          return '<button type="button" class="chip chip--hora" data-hora="' + h + '" aria-pressed="false"' + (no ? ' disabled aria-label="' + h + ', no disponible"' : '') + '>' + h + '</button>';
        }).join('') + '</div></div>';
      }
      horasBox.innerHTML = grupo('Mañana', MANANA) + (d.wd === 6 ? '' : grupo('Tarde', TARDE));
      estado.hora = '';
    }
    pintarHoras();

    function marcar(nombre, ok) {
      var b = form.querySelector('[data-bloque="' + nombre + '"]');
      if (b) b.classList.toggle('con-error', !ok);
      return ok;
    }
    function nuboEstado(e) { if (nubo && window.Nubo && nubo.getAttribute('data-nubo') !== e) Nubo.set(nubo, e); }

    form.addEventListener('click', function (e) {
      var c = e.target.closest('[data-opcion]');
      if (c) {
        var g = c.getAttribute('data-opcion');
        form.querySelectorAll('[data-opcion="' + g + '"]').forEach(function (o) { o.setAttribute('aria-pressed', o === c ? 'true' : 'false'); });
        estado[g] = c.textContent.trim();
        marcar(g, true);
        if (g === 'interes') nuboEstado('explica');
        return;
      }
      var d = e.target.closest('.dia');
      if (d) {
        diasBox.querySelectorAll('.dia').forEach(function (o) { o.setAttribute('aria-pressed', o === d ? 'true' : 'false'); });
        estado.dia = dias[+d.getAttribute('data-i')];
        marcar('dia', true); pintarHoras();
        return;
      }
      var h = e.target.closest('[data-hora]');
      if (h && !h.disabled) {
        horasBox.querySelectorAll('[data-hora]').forEach(function (o) { o.setAttribute('aria-pressed', o === h ? 'true' : 'false'); });
        estado.hora = h.getAttribute('data-hora');
        marcar('dia', true);
        nuboEstado('escucha');
      }
    });

    function validarPaso1() {
      var a = marcar('interes', !!estado.interes);
      var b = marcar('para', !!estado.para);
      var c = marcar('dia', !!(estado.dia && estado.hora));
      return a && b && c;
    }
    function validarPaso2() {
      var nombre = form.querySelector('[name="nombre"]'), wa = form.querySelector('[name="whatsapp"]');
      var okN = nombre.value.trim().length > 1, okW = wa.value.replace(/\D/g, '').length === 10;
      nombre.closest('.campo').classList.toggle('con-error', !okN);
      wa.closest('.campo').classList.toggle('con-error', !okW);
      nombre.closest('.campo').querySelector('.campo__ayuda').textContent = okN ? 'Como quieres que te llamemos.' : 'Escribe tu nombre.';
      wa.closest('.campo').querySelector('.campo__ayuda').textContent = okW ? 'Ahí te confirmamos tu cita.' : 'Escribe tu WhatsApp a 10 dígitos.';
      var okC = marcar('como', !!estado.como);
      return okN && okW && okC;
    }
    form.querySelectorAll('input').forEach(function (i) { i.addEventListener('input', function () { i.closest('.campo').classList.remove('con-error'); }); });

    var paso1 = form.querySelector('[data-paso-agenda="1"]');
    var paso2 = form.querySelector('[data-paso-agenda="2"]');
    var indic = caja.querySelectorAll('[data-indicador]');
    function mostrarPaso(n) {
      if (!paso2) return;
      paso1.hidden = n !== 1; paso2.hidden = n !== 2;
      indic.forEach(function (s, k) { s.classList.toggle('activo', k === n - 1); s.classList.toggle('hecho', k < n - 1); });
      var res = form.querySelector('[data-resumen]');
      if (res && n === 2) res.innerHTML = '<span class="dato">' + estado.interes + '</span><span class="dato">' + DIAS[estado.dia.wd] + ' ' + estado.dia.fecha.getUTCDate() + ', ' + estado.hora + '</span><button type="button" class="enlace" data-volver style="border:0;background-color:transparent;cursor:pointer">Cambiar</button>';
      caja.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
    form.addEventListener('click', function (e) {
      if (e.target.closest('[data-continuar]')) { if (validarPaso1()) mostrarPaso(2); }
      if (e.target.closest('[data-volver]')) mostrarPaso(1);
    });

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var ok1 = validarPaso1();
      if (!ok1) { if (paso2 && !paso2.hidden) mostrarPaso(1); return; }
      if (!validarPaso2()) return;
      var nombre = form.querySelector('[name="nombre"]').value.trim();
      var fechaTxt = DIAS[estado.dia.wd].toLowerCase() + ' ' + estado.dia.fecha.getUTCDate() + ' de ' + MESES[estado.dia.fecha.getUTCMonth()];
      var okBox = caja.querySelector('.agenda-ok');
      okBox.querySelector('[data-ok-nombre]').textContent = nombre.split(' ')[0];
      okBox.querySelector('[data-ok-ficha]').innerHTML =
        '<li><span>Día</span><strong>' + fechaTxt + '</strong></li>' +
        '<li><span>Hora</span><strong>' + estado.hora + '</strong></li>' +
        '<li><span>Valoración</span><strong>' + estado.interes + (estado.para === 'Para un niño' ? ', niño' : '') + '</strong></li>' +
        '<li><span>Folio</span><strong class="tabular">DD-1001</strong></li>';
      var msg = 'Hola, soy ' + nombre + '. Aparté una valoración el ' + fechaTxt + ' a las ' + estado.hora + ' (' + estado.interes + '). Folio DD-1001.';
      okBox.querySelector('[data-ok-wa]').href = 'https://wa.me/' + WA + '?text=' + encodeURIComponent(msg);
      form.hidden = true;
      okBox.classList.add('visible');
      var on = okBox.querySelector('.nubo'); if (on && window.Nubo) Nubo.set(on, 'celebra');
      nuboEstado('celebra');
      caja.scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
    caja.querySelector('[data-otra]').addEventListener('click', function () {
      caja.querySelector('.agenda-ok').classList.remove('visible');
      form.hidden = false; form.reset();
      estado = { interes: '', para: '', dia: null, hora: '', como: '' };
      form.querySelectorAll('[aria-pressed="true"]').forEach(function (o) { o.setAttribute('aria-pressed', 'false'); });
      pintarHoras(); mostrarPaso(1); nuboEstado('escucha');
    });
  }


  window.DDAgenda = { proximosDias: proximosDias, ocupadas: ocupadas, MANANA: MANANA, TARDE: TARDE, DIAS: DIAS, MESES: MESES, aMin: aMin, WA: WA };

  function frenoAgenda() {
    var sec = document.querySelector('.agenda-sec');
    if (!sec || (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches)) return;
    var visto = 0, usado = 0, timer, ultimoY = window.scrollY, muestras = [];
    function revisar() {
      var top = sec.getBoundingClientRect().top;
      var bajando = window.scrollY > ultimoY;
      ultimoY = window.scrollY;
      var ahora = Date.now();
      muestras.push([ahora, window.scrollY]);
      while (muestras.length && ahora - muestras[0][0] > 700) muestras.shift();
      if (top > -60 && top < window.innerHeight * 0.7) visto = Date.now();
      clearTimeout(timer);
      timer = setTimeout(function () {
        var t = sec.getBoundingClientRect().top;
        var recorrido = muestras.length ? muestras[muestras.length - 1][1] - muestras[0][1] : 0;
        var rapido = Date.now() - visto < 1100 && recorrido > window.innerHeight * 0.8;
        if (bajando && rapido && t < -120 && t > -window.innerHeight * 1.8 && Date.now() - usado > 8000) {
          usado = Date.now();
          sec.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      }, 140);
    }
    window.addEventListener('scroll', revisar, { passive: true });
  }
  document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('[data-agenda] form').forEach(init);
    frenoAgenda();
  });
})();
