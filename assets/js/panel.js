(function () {
  var DIAS = ['Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado'];
  var DC = ['Dom', 'Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb'];
  var MESES = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'];
  var MANANA = ['10:00', '10:45', '11:30', '12:15', '13:00'], TARDE = ['16:00', '16:45', '17:30', '18:15', '19:00'];
  var ETAPAS = [
    ['contactar', 'Por contactar', 'Dejó sus datos o escribió. Todavía no agenda.'],
    ['agendo', 'Agendó', 'Tiene su valoración apartada.'],
    ['presupuesto', 'Con presupuesto', 'Ya se valoró y tiene su plan. Falta que lo acepte.'],
    ['tratamiento', 'En tratamiento', 'Aceptó su plan y está en citas.'],
    ['aldia', 'Al día', 'Atendido, sin nada pendiente. Toca revisión en 6 meses.'],
    ['no_regreso', 'No regresó', 'Faltó o dejó de contestar.']
  ];
  var ETQ = {}; ETAPAS.forEach(function (e) { ETQ[e[0]] = e[1]; });
  var VORTEX = ['Instagram', 'Facebook', 'Google', 'Anuncio', 'Sitio web'];
  var FUENTES = ['Instagram', 'Facebook', 'Google', 'Anuncio', 'Sitio web', 'Me recomendaron', 'Pasó por ahí', 'WhatsApp directo', 'Paciente de antes'];
  var COMISIONABLES = ['Blanqueamiento', 'Ortodoncia', 'Prótesis'];
  var TRATS = ['Blanqueamiento', 'Ortodoncia', 'Prótesis', 'Limpieza', 'Resina', 'Endodoncia', 'Extracción', 'Implante'];
  var INTERESES = ['Blanqueamiento', 'Ortodoncia', 'Prótesis', 'Limpieza o revisión', 'No estoy seguro'];
  function ic(n, c) { return '<svg class="i' + (c ? ' ' + c : '') + '" aria-hidden="true"><use href="#i-' + n + '"/></svg>'; }
  function $(s, r) { return (r || document).querySelector(s); }
  function $$(s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); }
  function dinero(n) { return '$' + Math.round(n).toLocaleString('es-MX'); }
  function esc(t) { return String(t).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function aMin(h) { var p = h.split(':'); return +p[0] * 60 + +p[1]; }

  function hoyMx() {
    var p = new Intl.DateTimeFormat('en-CA', { timeZone: 'America/Mexico_City', year: 'numeric', month: '2-digit', day: '2-digit' }).formatToParts(new Date());
    var o = {}; p.forEach(function (x) { o[x.type] = x.value; });
    return new Date(Date.UTC(+o.year, +o.month - 1, +o.day));
  }
  var HOY = hoyMx(), DOMINGO = HOY.getUTCDay() === 0;
  var AHORA = (function () { var p = new Intl.DateTimeFormat('en-GB', { timeZone: 'America/Mexico_City', hour: '2-digit', minute: '2-digit', hour12: false }).format(new Date()).split(':'); return (+p[0] % 24) * 60 + (+p[1]); })();
  var LUNES = new Date(HOY); LUNES.setUTCDate(HOY.getUTCDate() + (DOMINGO ? 1 : 1 - HOY.getUTCDay()));
  function diaN(n) { var d = new Date(LUNES); d.setUTCDate(LUNES.getUTCDate() + n); return d; }
  function fechaCorta(d) { return DC[d.getUTCDay()] + ' ' + d.getUTCDate(); }
  function fechaLarga(d) { return DIAS[d.getUTCDay()] + ' ' + d.getUTCDate() + ' de ' + MESES[d.getUTCMonth()]; }
  function fechaPago(d) { return d.getUTCDate() + ' ' + MESES[d.getUTCMonth()].slice(0, 3); }
  var DIA_HOY = DOMINGO ? 0 : HOY.getUTCDay() - 1;
  function saludo() { if (DOMINGO || AHORA < 12 * 60) return 'Buenos días, doctora'; return AHORA < 19 * 60 ? 'Buenas tardes, doctora' : 'Buenas noches, doctora'; }

  // ---------- Datos de ejemplo ----------
  var P = [
    { id: 1, n: 'Mariana Gómez Ruiz', tel: '961 214 3381', i: 'Blanqueamiento', f: 'Instagram', e: 'tratamiento', pres: { t: 'Blanqueamiento', m: 3500, est: 'Aceptado' } },
    { id: 2, n: 'Luis Alberto Pérez', tel: '961 330 9142', i: 'Ortodoncia', f: 'Facebook', e: 'tratamiento', pres: { t: 'Ortodoncia', m: 18000, est: 'Aceptado' } },
    { id: 3, n: 'Fernanda López', tel: '961 118 2207', i: 'Limpieza o revisión', f: 'Me recomendaron', e: 'aldia', rev: 'mayo de 2027' },
    { id: 4, n: 'Diego Hernández', tel: '961 455 0193', i: 'Ortodoncia', f: 'Anuncio', e: 'presupuesto', pres: { t: 'Ortodoncia', m: 21000, est: 'Por aceptar' } },
    { id: 5, n: 'Sofía Martínez', tel: '961 287 6650', i: 'Limpieza o revisión', f: 'Google', e: 'agendo', nino: true },
    { id: 6, n: 'Rosa Elena Cruz', tel: '961 602 1185', i: 'Prótesis', f: 'Pasó por ahí', e: 'tratamiento', pres: { t: 'Prótesis', m: 9000, est: 'Aceptado' } },
    { id: 7, n: 'Jorge Velázquez', tel: '961 774 3029', i: 'Prótesis', f: 'Facebook', e: 'tratamiento', pres: { t: 'Prótesis', m: 7500, est: 'Aceptado' } },
    { id: 8, n: 'Andrea Moreno', tel: '961 139 8846', i: 'Blanqueamiento', f: 'Instagram', e: 'agendo' },
    { id: 9, n: 'Carlos Aguilar', tel: '961 520 4471', i: 'No estoy seguro', f: 'Sitio web', e: 'contactar' },
    { id: 10, n: 'Valeria Ramírez', tel: '961 368 2954', i: 'Blanqueamiento', f: 'Anuncio', e: 'agendo' },
    { id: 11, n: 'Emiliano Castillo', tel: '961 247 1108', i: 'Ortodoncia', f: 'Me recomendaron', e: 'presupuesto', nino: true, pres: { t: 'Ortodoncia', m: 16500, est: 'Por aceptar' } },
    { id: 12, n: 'Patricia Domínguez', tel: '961 813 5520', i: 'Limpieza o revisión', f: 'Google', e: 'no_regreso' },
    { id: 13, n: 'Ricardo Ozuna', tel: '961 690 3347', i: 'Blanqueamiento', f: 'Instagram', e: 'agendo' },
    { id: 14, n: 'Guadalupe Torres', tel: '961 145 7762', i: 'Prótesis', f: 'Sitio web', e: 'agendo' },
    { id: 15, n: 'Héctor Ruiz', tel: '961 402 6619', i: 'Ortodoncia', f: 'Instagram', e: 'contactar' },
    { id: 16, n: 'Lucía Pérez', tel: '961 577 2041', i: 'Limpieza o revisión', f: 'Facebook', e: 'aldia', rev: 'mayo de 2027' }
  ];
  P.forEach(function (p) { p.notas = p.notas || ''; });
  function pac(id) { for (var k = 0; k < P.length; k++) if (P[k].id === id) return P[k]; }
  var sigId = 100;
  var C = [
    [0, '10:00', 5, 'Valoración'], [0, '11:30', 8, 'Valoración'], [0, '13:00', 2, 'Sesión'], [0, '16:45', 10, 'Valoración'], [0, '18:15', 7, 'Sesión'],
    [1, '10:45', 13, 'Valoración'], [1, '17:30', 4, 'Seguimiento'],
    [2, '12:15', 6, 'Sesión'], [2, '16:00', 11, 'Seguimiento'], [2, '19:00', 14, 'Valoración'],
    [3, '10:00', 1, 'Sesión'], [5, '10:00', 1, 'Sesión']
  ].map(function (c, k) {
    var pasada = c[0] < DIA_HOY || (c[0] === DIA_HOY && !DOMINGO && aMin(c[1]) + 45 <= AHORA);
    return { id: k + 1, d: c[0], h: c[1], p: c[2], tipo: c[3], st: pasada ? 'llego' : 'pendiente', rec: false };
  });
  function cita(id) { for (var k = 0; k < C.length; k++) if (C[k].id === id) return C[k]; }
  var B = [{ d: 4, desde: '16:00', hasta: '20:00', motivo: 'Curso de la doctora' }];
  var PAGOS = [
    { p: 1, f: '3 nov', c: 'Blanqueamiento', m: 3500 },
    { p: 2, f: '4 nov', c: 'Ortodoncia', m: 4000, nota: 'Enganche' },
    { p: 6, f: '5 nov', c: 'Prótesis', m: 3000, nota: 'Abono 1' },
    { p: 7, f: '6 nov', c: 'Prótesis', m: 2500, nota: 'Abono 1' },
    { p: 16, f: '2 nov', c: 'Limpieza', m: 600 },
    { p: 3, f: '7 nov', c: 'Valoración', m: 350 }
  ];
  var L = [
    { nombre: 'Anuncio blanqueamiento noviembre', f: 'Anuncio', slug: 'anuncio-blanqueamiento-nov', clics: 214, citas: 6 },
    { nombre: 'Bio de Instagram', f: 'Instagram', slug: 'instagram-bio', clics: 131, citas: 4 },
    { nombre: 'Publicaciones de Facebook', f: 'Facebook', slug: 'facebook-posts', clics: 88, citas: 3 },
    { nombre: 'Perfil de Google', f: 'Google', slug: 'google-perfil', clics: 57, citas: 2 }
  ];
  var PEND = [
    ['Fotos de la clínica y de la doctora', 'Se toman en la primera grabación', 'pendiente'],
    ['Imagen de la garantía', 'Para la sección de confianza', 'pendiente'],
    ['Paquetes y precios', 'Incluido el paquete de bienvenida', 'pendiente'],
    ['Dominio', 'Acceso para conectarlo', 'pendiente'],
    ['Aviso de publicidad COFEPRIS', 'Número y leyenda para el pie de página', 'pendiente'],
    ['Edades en odontopediatría', 'Desde qué edad atienden', 'en_revision'],
    ['Reseñas de Google', 'Faltan 2 textos completos', 'en_revision'],
    ['Horario', 'Lunes a sábado, confirmado', 'listo']
  ];
  var EQUIPO = [
    { n: 'Dra. María Concepción Díaz', r: 'Administradora', est: 'Activa' },
    { n: 'Kaled', r: 'Administrador', est: 'Activo' },
    { n: 'Recepción', r: 'Recepción', est: 'Invitación enviada' },
    { n: 'Santiago', r: 'Vortex', est: 'Activo' },
    { n: 'Fede', r: 'Vortex', est: 'Activo' }
  ];
  var ROLES = {
    'Administradora': 'Ve y edita todo, incluidos cobros y comisión.',
    'Recepción': 'Ve Hoy, Agenda y Pacientes. No ve montos.',
    'Vortex': 'Ve todo para dar seguimiento a la campaña.'
  };

  // ---------- Utilidades ----------
  var ROL = 'admin';
  function puede(v) { return ROL !== 'recepcion' || ['hoy', 'agenda', 'pacientes'].indexOf(v) > -1; }
  function dineroVisible() { return ROL !== 'recepcion'; }
  function toast(t) { var el = $('#toast'); el.textContent = t; el.classList.add('visible'); clearTimeout(el._t); el._t = setTimeout(function () { el.classList.remove('visible'); }, 2400); }
  function chipEtapa(e) { return '<span class="etapa etapa--' + e + '">' + ETQ[e] + '</span>'; }
  function esVortex(f) { return VORTEX.indexOf(f) > -1; }
  function waUrl(p, txt) { return 'https://wa.me/52' + p.tel.replace(/\D/g, '') + '?text=' + encodeURIComponent(txt); }
  function nombre1(p) { return p.n.split(' ')[0]; }
  function kpi(i, t, v, s, cls) { return '<div class="kpi' + (cls ? ' ' + cls : '') + '"><span class="kpi__icono">' + ic(i) + '</span><span class="kpi__t">' + t + '</span><strong class="kpi__v tabular">' + v + '</strong><span class="mini">' + s + '</span></div>'; }
  function comisionDe(pg) {
    var p = pac(pg.p);
    if (!esVortex(p.f)) return [0, 'Llegó por ' + p.f.toLowerCase()];
    if (COMISIONABLES.indexOf(pg.c) < 0) return [0, pg.c === 'Implante' ? 'Implantes no cuentan' : 'No es tratamiento con comisión'];
    return [pg.m * 0.3, 'Cuenta'];
  }
  function comisionMes() { return PAGOS.reduce(function (a, pg) { return a + comisionDe(pg)[0]; }, 0); }
  function presPendientes() { return P.filter(function (p) { return p.e === 'presupuesto' && p.pres; }); }
  function ocupado(d, h) { return C.some(function (c) { return c.d === d && c.h === h && c.st !== 'cancelada'; }); }
  function bloqueado(d, h) { return B.some(function (b) { return b.d === d && aMin(h) >= aMin(b.desde) && aMin(h) < aMin(b.hasta); }); }
  function horasDe(d) { return d === 5 ? MANANA : MANANA.concat(TARDE); }
  function tipoTxt(c) { var p = pac(c.p); return c.tipo === 'Sesión' && p.pres ? 'Sesión de ' + p.pres.t.toLowerCase() : c.tipo === 'Valoración' ? 'Valoración · ' + p.i.toLowerCase() : c.tipo; }

  var V = {};

  // ---------- Hoy ----------
  V.hoy = function () {
    var d = DIA_HOY, citas = C.filter(function (c) { return c.d === d; }).sort(function (a, b) { return aMin(a.h) - aMin(b.h); });
    var llegan = citas.filter(function (c) { return c.st === 'llego'; }).length;
    var sig = d + 1 > 5 ? null : d + 1;
    var manana = sig === null ? [] : C.filter(function (c) { return c.d === sig; }).sort(function (a, b) { return aMin(a.h) - aMin(b.h); });
    var porContactar = P.filter(function (p) { return p.e === 'contactar'; });
    var pres = presPendientes();
    var noReg = P.filter(function (p) { return p.e === 'no_regreso'; });
    var html = '<div class="hoy-cab"><div class="nubo" data-nubo="saluda" data-mirada data-saluda></div><div><span class="mini">' + fechaLarga(diaN(d)) + (DOMINGO ? ' · mañana' : '') + '</span><h2>' + saludo() + '</h2><p>' + (DOMINGO ? 'Mañana hay' : 'Hoy hay') + ' <strong>' + citas.length + ' citas</strong>. ' + (llegan === 1 ? 'Una ya llegó.' : llegan ? llegan + ' ya llegaron.' : DOMINGO ? 'Aquí abajo las tienes en orden.' : 'Ninguna ha llegado todavía.') + '</p></div></div>';
    html += '<div class="kpis">' + kpi('calendar', DOMINGO ? 'Citas mañana' : 'Citas hoy', citas.length, citas.filter(function (c) { return c.tipo === 'Valoración'; }).length + ' valoraciones') +
      kpi('users', 'Por contactar', porContactar.length, 'Escribirles hoy') +
      (dineroVisible() ? kpi('file-text', 'Presupuestos por aceptar', dinero(pres.reduce(function (a, p) { return a + p.pres.m; }, 0)), pres.length + ' pacientes') + kpi('receipt-2', 'Comisión del mes', dinero(comisionMes()), '30% Vortex')
        : kpi('file-text', 'Con presupuesto', pres.length, 'Por dar seguimiento') + kpi('calendar-week', 'Esta semana', C.length, 'citas')) + '</div>';
    html += '<div class="hoy-grid"><div><div class="sub-cab"><h3 class="sub-p">' + (DOMINGO ? 'Citas de mañana' : 'Citas de hoy') + '</h3><button class="btn btn--chico btn--secundario" data-modal="cita" data-dia="' + d + '">' + ic('plus') + ' Agregar cita</button></div><ul class="linea-hoy">' + (citas.map(function (c) {
      var p = pac(c.p);
      var acc = c.st === 'falto' ? '<button class="btn btn--chico btn--primario" data-reagendar="' + c.id + '">' + ic('calendar') + ' Reagendar</button>'
        : '<a class="icono-btn" target="_blank" rel="noopener" href="' + waUrl(p, 'Hola ' + nombre1(p) + ', te escribimos de Dental Díaz para confirmar tu cita de ' + (DOMINGO ? 'mañana' : 'hoy') + ' a las ' + c.h + '.') + '" aria-label="Confirmar por WhatsApp">' + ic('brand-whatsapp') + '</a>' +
          '<button class="btn btn--chico ' + (c.st === 'llego' ? 'btn--primario' : 'btn--secundario') + '" data-marcar="llego">' + ic('check') + ' Llegó</button>' +
          '<button class="btn btn--chico btn--secundario" data-marcar="falto">No llegó</button>';
      return '<li class="cita-hoy cita-hoy--' + c.st + '" data-cita="' + c.id + '"><span class="hora tabular">' + c.h + '</span><div class="cita-hoy__info" data-abrir="' + p.id + '"><strong>' + esc(p.n) + (p.nino ? ' <span class="mini-et">Niño</span>' : '') + '</strong><span>' + tipoTxt(c) + '</span></div><div class="cita-hoy__acciones">' + acc + '</div></li>';
    }).join('') || '<li class="vacio">Sin citas.</li>') + '</ul>';
    if (sig !== null) {
      html += '<div class="sub-cab"><h3 class="sub-p">Recordatorios para ' + fechaLarga(diaN(sig)).toLowerCase() + '</h3><span class="mini">Se mandan un día antes</span></div><ul class="lista-simple">' + (manana.map(function (c) {
        var p = pac(c.p);
        return '<li><span class="hora tabular">' + c.h + '</span><div data-abrir="' + p.id + '"><strong>' + esc(p.n) + '</strong><span class="mini">' + tipoTxt(c) + '</span></div>' + (c.rec ? '<span class="estado estado--listo">' + ic('check') + ' Enviado</span>' : '<a class="btn btn--chico btn--whatsapp" target="_blank" rel="noopener" data-recordar="' + c.id + '" href="' + waUrl(p, 'Hola ' + nombre1(p) + ', te recordamos tu cita en Dental Díaz mañana ' + fechaLarga(diaN(sig)).toLowerCase() + ' a las ' + c.h + '. Si necesitas cambiarla, respóndenos aquí.') + '">' + ic('bell') + ' Recordar</a>') + '</li>';
      }).join('') || '<li class="vacio">Sin citas.</li>') + '</ul>';
    }
    html += '</div><aside><div class="tarjeta-p"><div class="tarjeta-p__cab"><h3>Para dar seguimiento</h3><a class="mini enlace" href="#pacientes" data-ir="pacientes">Ver pacientes</a></div><ul class="seguir">' +
      porContactar.map(function (p) { return seguirItem(p, 'Escribió por ' + p.f.toLowerCase() + ', sin cita', 'Hola ' + nombre1(p) + ', te escribimos de Dental Díaz. ¿Te ayudamos a apartar tu valoración?'); }).join('') +
      pres.map(function (p) { return seguirItem(p, 'Presupuesto de ' + p.pres.t.toLowerCase() + (dineroVisible() ? ' · ' + dinero(p.pres.m) : ''), 'Hola ' + nombre1(p) + ', te escribimos de Dental Díaz. ¿Te quedó alguna duda de tu plan de ' + p.pres.t.toLowerCase() + '?'); }).join('') +
      noReg.map(function (p) { return seguirItem(p, 'No regresó', 'Hola ' + nombre1(p) + ', te escribimos de Dental Díaz. ¿Quieres que te apartemos una nueva cita?'); }).join('') +
      '</ul></div></aside></div>';
    return html;
  };
  function seguirItem(p, txt, msg) { return '<li><div data-abrir="' + p.id + '"><strong>' + esc(p.n) + '</strong><span class="mini">' + txt + '</span></div>' + chipEtapa(p.e) + '<a class="icono-btn" target="_blank" rel="noopener" href="' + waUrl(p, msg) + '" aria-label="Escribir por WhatsApp">' + ic('brand-whatsapp') + '</a></li>'; }

  // ---------- Resumen ----------
  V.resumen = function () {
    var fuentes = {}; P.forEach(function (p) { fuentes[p.f] = (fuentes[p.f] || 0) + 1; });
    var orden = Object.keys(fuentes).sort(function (a, b) { return fuentes[b] - fuentes[a]; }), max = fuentes[orden[0]];
    function en(l) { return P.filter(function (p) { return l.indexOf(p.e) > -1; }).length; }
    var emb = [['Agendaron', en(['agendo', 'presupuesto', 'tratamiento', 'aldia', 'no_regreso'])], ['Se valoraron', en(['presupuesto', 'tratamiento', 'aldia'])], ['Recibieron presupuesto', en(['presupuesto', 'tratamiento'])], ['Empezaron tratamiento', en(['tratamiento'])]];
    var cobrado = PAGOS.reduce(function (a, x) { return a + x.m; }, 0);
    return '<div class="kpis">' + kpi('calendar-week', 'Citas esta semana', C.length, 'Lunes a sábado') + kpi('users', 'Pacientes nuevos', P.filter(function (p) { return ['contactar', 'agendo'].indexOf(p.e) > -1; }).length, 'Este mes') +
      kpi('check', 'Asistencia del mes', '88%', '22 de 25 llegaron') + kpi('receipt-2', 'Cobrado en ' + MESES[HOY.getUTCMonth()], dinero(cobrado), 'Comisión ' + dinero(comisionMes())) + '</div>' +
      '<div class="grid-resumen"><div class="tarjeta-p"><div class="tarjeta-p__cab"><h3>Pacientes por fuente</h3><span class="mini">Este mes</span></div><div class="barras">' + orden.map(function (f) {
        return '<div class="barra"><span>' + f + (esVortex(f) ? ' <em>Vortex</em>' : '') + '</span><div class="barra__pista"><i style="width:' + (fuentes[f] / max * 100) + '%"></i></div><strong>' + fuentes[f] + '</strong></div>';
      }).join('') + '</div></div>' +
      '<div class="tarjeta-p"><div class="tarjeta-p__cab"><h3>De la cita al tratamiento</h3><span class="mini">Este mes</span></div><div class="embudo">' + emb.map(function (x) {
        return '<div class="embudo__paso"><div class="embudo__barra" style="width:' + Math.max(x[1] / emb[0][1] * 100, 12) + '%"><strong>' + x[1] + '</strong></div><span>' + x[0] + '</span></div>';
      }).join('') + '</div></div>' +
      '<div class="tarjeta-p"><div class="tarjeta-p__cab"><h3>Presupuestos por aceptar</h3><span class="mini">' + dinero(presPendientes().reduce(function (a, p) { return a + p.pres.m; }, 0)) + '</span></div><ul class="lista-citas">' + presPendientes().map(function (p) {
        return '<li data-abrir="' + p.id + '"><span class="hora tabular">' + dinero(p.pres.m) + '</span><span class="nombre">' + esc(p.n) + '</span><span class="mini">' + p.pres.t + '</span></li>';
      }).join('') + '</ul></div>' +
      '<div class="tarjeta-p"><div class="tarjeta-p__cab"><h3>Páginas más visitadas</h3><span class="mini">Últimos 7 días</span></div><ul class="lista-paginas">' + [['Inicio', 612], ['Agendar', 233], ['Blanqueamiento', 148], ['Ortodoncia', 97], ['Nubo explica', 41]].map(function (x, k, a) {
        return '<li><span>' + x[0] + '</span><div class="barra__pista"><i style="width:' + (x[1] / a[0][1] * 100) + '%"></i></div><strong class="tabular">' + x[1] + '</strong></li>';
      }).join('') + '</ul></div></div>';
  };

  // ---------- Agenda ----------
  var AG = { vista: 'cal', rango: 'semana', dia: DIA_HOY };
  V.agenda = function () {
    var titulo = AG.rango === 'semana' ? 'Semana del ' + fechaLarga(diaN(0)).toLowerCase() : fechaLarga(diaN(AG.dia));
    var html = '<div class="ag-barra"><div class="ag-barra__izq"><div class="segmento" role="group" aria-label="Estilo"><button data-ag-vista="cal" aria-pressed="' + (AG.vista === 'cal') + '">' + ic('calendar-week') + ' Calendario</button><button data-ag-vista="tar" aria-pressed="' + (AG.vista === 'tar') + '">' + ic('layout-kanban') + ' Tarjetas</button></div>' +
      '<div class="segmento" role="group" aria-label="Rango"><button data-ag-rango="dia" aria-pressed="' + (AG.rango === 'dia') + '">Día</button><button data-ag-rango="semana" aria-pressed="' + (AG.rango === 'semana') + '">Semana</button></div></div>' +
      '<div class="ag-barra__der"><button class="btn btn--chico btn--secundario" data-modal="bloqueo">' + ic('x') + ' Bloquear<span class="solo-escritorio"> horario</span></button><button class="btn btn--chico btn--primario" data-modal="cita" data-dia="' + AG.dia + '">' + ic('plus') + ' Agregar cita</button></div></div>';
    html += '<div class="agenda-cab"><div><h3>' + titulo + '</h3><span class="mini">Se sincroniza con Google Calendar cuando se conecte</span></div><div class="leyenda"><span class="ley ley--pendiente">Por llegar</span><span class="ley ley--llego">Llegó</span><span class="ley ley--falto">No llegó</span><span class="ley ley--bloq">Bloqueado</span></div></div>';
    if (AG.rango === 'dia') {
      html += '<div class="dias-tabs">';
      for (var d = 0; d < 6; d++) html += '<button class="dia" aria-pressed="' + (d === AG.dia) + '" data-ag-dia="' + d + '"><span>' + DC[diaN(d).getUTCDay()] + '</span><strong>' + diaN(d).getUTCDate() + '</strong><small>' + C.filter(function (c) { return c.d === d; }).length + ' citas</small></button>';
      html += '</div>';
    }
    var dias = AG.rango === 'semana' ? [0, 1, 2, 3, 4, 5] : [AG.dia];
    if (AG.vista === 'cal') {
      var horas = MANANA.concat(TARDE);
      html += '<div class="semana' + (AG.rango === 'dia' ? ' semana--dia' : '') + '"><div class="semana__grid" style="grid-template-columns: 64px repeat(' + dias.length + ', minmax(' + (dias.length > 1 ? '118px' : '0') + ', 1fr))"><div class="semana__esq"></div>';
      dias.forEach(function (d) { html += '<div class="semana__dia' + (d === DIA_HOY ? ' hoy' : '') + '">' + fechaCorta(diaN(d)) + '</div>'; });
      horas.forEach(function (h) {
        html += '<div class="semana__hora tabular">' + h + '</div>';
        dias.forEach(function (d) {
          var c = C.filter(function (x) { return x.d === d && x.h === h; })[0];
          var cerrado = d === 5 && aMin(h) >= 16 * 60;
          var bl = bloqueado(d, h) ? B.filter(function (b) { return b.d === d && aMin(h) >= aMin(b.desde) && aMin(h) < aMin(b.hasta); })[0] : null;
          html += '<div class="semana__celda' + (cerrado ? ' cerrada' : '') + (bl ? ' bloq' : '') + '"' + (!c && !cerrado && !bl ? ' data-hueco="' + d + '|' + h + '"' : '') + '>' + (c ? citaBloque(c, AG.rango === 'dia') : bl && h === bl.desde ? '<span class="bloq__txt">' + esc(bl.motivo) + '</span>' : '') + '</div>';
        });
      });
      html += '</div></div>';
    } else {
      html += '<div class="ag-tarjetas">' + dias.map(function (d) {
        var cs = C.filter(function (c) { return c.d === d; }).sort(function (a, b) { return aMin(a.h) - aMin(b.h); });
        var bls = B.filter(function (b) { return b.d === d; });
        return '<section class="ag-dia"><header class="ag-dia__cab"><strong>' + fechaLarga(diaN(d)) + '</strong>' + (d === DIA_HOY ? '<span class="mini-et">' + (DOMINGO ? 'Mañana' : 'Hoy') + '</span>' : '') + '<span class="mini">' + cs.length + ' citas</span><button class="icono-btn icono-btn--chico" data-modal="cita" data-dia="' + d + '" aria-label="Agregar cita este día">' + ic('plus') + '</button></header><ul class="linea-hoy">' +
          bls.map(function (b) { return '<li class="cita-hoy cita-hoy--bloq"><span class="hora tabular">' + b.desde + '</span><div class="cita-hoy__info"><strong>Bloqueado hasta las ' + b.hasta + '</strong><span>' + esc(b.motivo) + '</span></div></li>'; }).join('') +
          (cs.map(function (c) { var p = pac(c.p); return '<li class="cita-hoy cita-hoy--' + c.st + '" data-abrir="' + p.id + '"><span class="hora tabular">' + c.h + '</span><div class="cita-hoy__info"><strong>' + esc(p.n) + '</strong><span>' + tipoTxt(c) + ' · ' + p.f + '</span></div>' + chipEtapa(p.e) + '</li>'; }).join('') || (bls.length ? '' : '<li class="vacio">Sin citas.</li>')) + '</ul></section>';
      }).join('') + '</div>';
    }
    return html;
  };
  function citaBloque(c, largo) { var p = pac(c.p); return '<button class="cita cita--' + c.st + (c.tipo !== 'Valoración' ? ' cita--sesion' : '') + '" data-abrir="' + p.id + '"><strong>' + esc(largo ? p.n : p.n.split(' ').slice(0, 2).join(' ')) + '</strong><span>' + tipoTxt(c) + (largo ? ' · ' + p.tel : '') + '</span></button>'; }

  // ---------- Pacientes ----------
  var PQ = '';
  V.pacientes = function () {
    return '<div class="ag-barra"><label class="buscador">' + ic('search') + '<input type="search" placeholder="Buscar paciente" data-buscar value="' + esc(PQ) + '"></label><div class="ag-barra__der"><button class="btn btn--chico btn--primario" data-modal="paciente">' + ic('plus') + ' Agregar paciente</button></div></div>' +
      '<p class="mini" style="margin:0 0 14px">Arrastra a un paciente para cambiar su etapa. En celular, tócalo y elige la etapa en su ficha.</p><div class="kanban" data-kanban>' + kanbanCols() + '</div>';
  };
  function kanbanCols() {
    return ETAPAS.map(function (e) {
      var ps = P.filter(function (p) { return p.e === e[0] && (!PQ || p.n.toLowerCase().indexOf(PQ) > -1); });
      return '<div class="kanban__col" data-col="' + e[0] + '"><div class="kanban__cab">' + chipEtapa(e[0]) + '<span class="tabular">' + ps.length + '</span></div><p class="kanban__desc">' + e[2] + '</p><div class="kanban__lista">' + ps.map(function (p) {
        var extra = p.e === 'presupuesto' && p.pres && dineroVisible() ? '<span class="tabular">' + dinero(p.pres.m) + '</span>' : p.e === 'aldia' && p.rev ? '<span>Revisión ' + p.rev.split(' ')[0] + '</span>' : '';
        return '<div class="kcard" draggable="true" data-abrir="' + p.id + '" tabindex="0"><strong>' + esc(p.n) + '</strong><span>' + (p.pres ? p.pres.t : p.i) + '</span><div class="kcard__pie"><span class="fuente">' + p.f + '</span>' + extra + '</div></div>';
      }).join('') + '</div></div>';
    }).join('');
  }

  // ---------- Ligas, cobros, comisión, pendientes, contenido, equipo ----------
  V.ligas = function () {
    return '<div class="tarjeta-p ligas-form"><h3>Crear liga</h3><p class="mini">Cada liga guarda de dónde llegó el paciente. Así sabemos qué funciona y qué cuenta para la comisión.</p><div class="ligas-form__campos"><div class="campo"><label for="lg-n">Nombre</label><input id="lg-n" placeholder="Anuncio ortodoncia diciembre"></div><div class="campo"><label for="lg-f">Fuente</label><select id="lg-f"><option>Anuncio</option><option>Instagram</option><option>Facebook</option><option>Google</option><option>Sitio web</option></select></div><button class="btn btn--primario" data-crear-liga>' + ic('plus') + ' Crear</button></div></div>' +
      '<div class="tabla-envuelta"><table class="tabla tabla-movil"><thead><tr><th>Liga</th><th>Fuente</th><th class="der">Clics</th><th class="der">Citas</th><th></th></tr></thead><tbody data-ligas>' + filasLigas() + '</tbody></table></div>';
  };
  function filasLigas() { return L.map(function (l) { var url = 'dentaldiaz.mx/?src=' + l.slug; return '<tr><td><strong>' + esc(l.nombre) + '</strong><span class="mini mono">' + url + '</span></td><td>' + l.f + '</td><td class="der tabular">' + l.clics + '<span class="solo-movil"> clics</span></td><td class="der tabular">' + l.citas + '<span class="solo-movil"> citas</span></td><td class="der"><button class="btn btn--chico btn--secundario" data-copiar="' + url + '">' + ic('copy') + ' Copiar</button></td></tr>'; }).join(''); }

  V.cobros = function () {
    var total = PAGOS.reduce(function (a, x) { return a + x.m; }, 0), por = {};
    PAGOS.forEach(function (x) { por[x.c] = (por[x.c] || 0) + x.m; });
    var orden = Object.keys(por).sort(function (a, b) { return por[b] - por[a]; });
    return '<div class="ag-barra"><div></div><div class="ag-barra__der"><button class="btn btn--chico btn--primario" data-modal="pago">' + ic('plus') + ' Registrar cobro</button></div></div>' +
      '<div class="grid-resumen"><div class="kpi kpi--grande"><span class="kpi__t">Cobrado en ' + MESES[HOY.getUTCMonth()] + '</span><strong class="kpi__v tabular">' + dinero(total) + '</strong><span class="mini">' + PAGOS.length + ' cobros registrados. Cada abono o mensualidad se registra por separado.</span></div>' +
      '<div class="tarjeta-p"><h3>Por tratamiento</h3><div class="barras">' + orden.map(function (c) { return '<div class="barra"><span>' + c + '</span><div class="barra__pista"><i style="width:' + (por[c] / por[orden[0]] * 100) + '%"></i></div><strong class="tabular" style="min-width:64px">' + dinero(por[c]) + '</strong></div>'; }).join('') + '</div></div></div>' +
      '<div class="tabla-envuelta" style="margin-top:14px"><table class="tabla tabla-movil"><thead><tr><th>Paciente</th><th>Concepto</th><th>Fecha</th><th></th><th class="der">Monto</th></tr></thead><tbody>' + PAGOS.slice().reverse().map(function (x) {
        var p = pac(x.p); return '<tr data-abrir="' + p.id + '"><td><strong>' + esc(p.n) + '</strong></td><td>' + x.c + (x.nota ? ' · ' + esc(x.nota) : '') + '</td><td class="tabular">' + x.f + '</td><td></td><td class="der tabular"><strong>' + dinero(x.m) + '</strong></td></tr>';
      }).join('') + '</tbody></table></div>';
  };

  V.comision = function () {
    var total = comisionMes();
    return '<div class="com-cab"><div class="kpi kpi--grande"><span class="kpi__t">Comisión de ' + MESES[HOY.getUTCMonth()] + '</span><strong class="kpi__v tabular">' + dinero(total) + '</strong><span class="mini">30% de lo cobrado en blanqueamiento, ortodoncia y prótesis a pacientes que llegaron por Vortex. En ortodoncia cuentan las mensualidades de los tres meses del piloto. Implantes no cuentan. Se paga en efectivo.</span></div></div>' +
      '<div class="tabla-envuelta"><table class="tabla tabla-movil"><thead><tr><th>Paciente</th><th>Cobro</th><th>Fuente</th><th class="der">Cobrado</th><th class="der">Comisión</th></tr></thead><tbody>' + PAGOS.map(function (x) {
        var p = pac(x.p), c = comisionDe(x);
        return '<tr class="' + (c[0] ? '' : 'apagada') + '" data-abrir="' + p.id + '"><td><strong>' + esc(p.n) + '</strong></td><td>' + x.c + ' · ' + x.f + '</td><td>' + p.f + (esVortex(p.f) ? ' <em class="vx">Vortex</em>' : '') + '</td><td class="der tabular">' + dinero(x.m) + '</td><td class="der tabular"><strong>' + (c[0] ? dinero(c[0]) : '<span class="mini">' + c[1] + '</span>') + '</strong></td></tr>';
      }).join('') + '</tbody><tfoot><tr><td colspan="4">Total del mes</td><td class="der tabular"><strong>' + dinero(total) + '</strong></td></tr></tfoot></table></div>';
  };

  V.pendientes = function () {
    var est = { pendiente: 'Pendiente', en_revision: 'En revisión', listo: 'Listo' };
    return '<p class="mini" style="margin:0 0 16px">Lo que necesitamos de la clínica para terminar el sitio. Sube el archivo o escribe la respuesta y nos llega directo.</p><div class="pendientes">' + PEND.map(function (x, k) {
      return '<div class="pend pend--' + x[2] + '"><div><strong>' + x[0] + '</strong><span class="mini">' + x[1] + '</span></div><span class="estado estado--' + x[2] + '">' + est[x[2]] + '</span>' + (x[2] !== 'listo' ? '<button class="btn btn--chico btn--secundario" data-subir="' + k + '">' + ic('upload') + ' Subir</button>' : '<span></span>') + '</div>';
    }).join('') + '</div>';
  };

  var CT = 'inicio';
  V.contenido = function () {
    var tabs = [['inicio', 'Inicio'], ['horario', 'Horario'], ['preguntas', 'Preguntas'], ['fotos', 'Fotos']];
    var cuerpo = {
      inicio: '<div class="campo"><label>Título principal</label><input value="Te explicamos todo antes de empezar"></div><div class="campo"><label>Texto debajo del título</label><textarea rows="3">Clínica dental familiar en Terán. Revisamos con calma, te enseñamos tus radiografías y tu plan va por escrito.</textarea></div><div class="campo"><label>Aviso en la parte de arriba del sitio</label><input placeholder="Ejemplo: cerrado el 12 de diciembre"></div>',
      horario: '<div class="campo"><label>Lunes a viernes</label><input value="10:00 a 14:00 y 16:00 a 20:00"></div><div class="campo"><label>Sábado</label><input value="10:00 a 14:00"></div><div class="campo"><label>Domingo</label><input value="Cerrado"></div><p class="mini">Para cerrar un día en específico, usa "Bloquear horario" en la agenda.</p>',
      preguntas: [['¿La valoración tiene costo?', 'Sí, $350. Incluye revisión completa, dos radiografías periapicales, diagnóstico y tu plan de tratamiento por escrito.'], ['¿Cuánto dura?', '45 minutos.'], ['¿Cómo pago la valoración?', 'En la clínica, el día de tu cita.']].map(function (q) { return '<div class="pregunta-ed"><div class="campo"><label>Pregunta</label><input value="' + q[0] + '"></div><div class="campo"><label>Respuesta</label><textarea rows="2">' + q[1] + '</textarea></div></div>'; }).join('') + '<button class="btn btn--chico btn--secundario" style="justify-self:start">' + ic('plus') + ' Agregar pregunta</button>',
      fotos: '<div class="fotos-mini">' + ['Hero', 'Doctora', 'Recepción', 'Consultorio', 'Radiografía', 'Fachada'].map(function (f) { return '<button class="foto-mini" data-subir="f">' + ic('camera') + '<span>' + f + '</span></button>'; }).join('') + '</div>'
    };
    return '<div class="tabs-p" role="tablist">' + tabs.map(function (t) { return '<button role="tab" aria-selected="' + (t[0] === CT) + '" data-ct="' + t[0] + '">' + t[1] + '</button>'; }).join('') + '</div><div class="tarjeta-p contenido-panel">' + cuerpo[CT] + '</div>' +
      '<div class="guardar-barra"><span class="mini">Los cambios se publican al momento.</span><button class="btn btn--primario" data-guardar>Guardar cambios</button></div>';
  };

  V.equipo = function () {
    return '<div class="grid-equipo"><div class="tabla-envuelta"><table class="tabla tabla-movil"><thead><tr><th>Persona</th><th>Rol</th><th>Estado</th><th></th><th></th></tr></thead><tbody data-equipo>' + filasEquipo() + '</tbody></table></div>' +
      '<div class="tarjeta-p"><h3>Invitar a alguien</h3><p class="mini">Le llega un correo para entrar. No necesita contraseña.</p><div class="campo"><label for="eq-c">Correo</label><input id="eq-c" type="email" placeholder="nombre@correo.com"></div><div class="campo"><label for="eq-r">Rol</label><select id="eq-r"><option>Recepción</option><option>Administradora</option><option>Vortex</option></select></div><button class="btn btn--primario" data-invitar>Enviar invitación</button>' +
      '<ul class="roles">' + Object.keys(ROLES).map(function (r) { return '<li><strong>' + r + '</strong><span class="mini">' + ROLES[r] + '</span></li>'; }).join('') + '</ul></div></div>';
  };
  function filasEquipo() { return EQUIPO.map(function (m) { return '<tr><td><strong>' + esc(m.n) + '</strong></td><td>' + m.r + '</td><td><span class="estado ' + (m.est.indexOf('Invit') === 0 ? 'estado--pendiente' : 'estado--listo') + '">' + m.est + '</span></td><td></td><td></td></tr>'; }).join(''); }

  // ---------- Ficha del paciente ----------
  function ficha(p) {
    var citas = C.filter(function (c) { return c.p === p.id; });
    var pagos = PAGOS.filter(function (x) { return x.p === p.id; });
    var html = '<h3>' + esc(p.n) + '</h3><p class="mini tabular">' + p.tel + (p.nino ? ' · Paciente niño' : '') + '</p>' +
      '<div class="ficha-acciones"><a class="btn btn--whatsapp btn--chico" target="_blank" rel="noopener" href="' + waUrl(p, 'Hola ' + nombre1(p) + ', te escribimos de Dental Díaz.') + '">' + ic('brand-whatsapp') + ' WhatsApp</a><button class="btn btn--chico btn--secundario" data-modal="cita" data-pac="' + p.id + '">' + ic('calendar') + ' Agendar cita</button></div>' +
      '<dl class="ficha"><div><dt>Interés</dt><dd>' + p.i + '</dd></div><div><dt>Llegó por</dt><dd>' + p.f + (esVortex(p.f) ? ' <em class="vx">Vortex</em>' : '') + '</dd></div></dl>' +
      '<div class="campo"><label for="dr-etapa">Etapa</label><select id="dr-etapa">' + ETAPAS.map(function (e) { return '<option value="' + e[0] + '"' + (e[0] === p.e ? ' selected' : '') + '>' + e[1] + '</option>'; }).join('') + '</select><span class="campo__ayuda" data-etapa-desc>' + ETAPAS.filter(function (e) { return e[0] === p.e; })[0][2] + '</span></div>';
    html += '<section class="ficha-sec"><h4>Presupuesto</h4><div class="ficha-fila"><div class="campo"><label for="dr-pt">Tratamiento</label><select id="dr-pt"><option value="">Sin presupuesto</option>' + TRATS.map(function (t) { return '<option' + (p.pres && p.pres.t === t ? ' selected' : '') + '>' + t + '</option>'; }).join('') + '</select></div>' +
      (dineroVisible() ? '<div class="campo"><label for="dr-pm">Monto del plan</label><input id="dr-pm" inputmode="numeric" placeholder="0" value="' + (p.pres ? p.pres.m : '') + '"></div>' : '') + '</div>' + (p.pres ? '<span class="mini">Estado: ' + p.pres.est + '</span>' : '') + '</section>';
    if (dineroVisible()) {
      var pagado = pagos.reduce(function (a, x) { return a + x.m; }, 0);
      html += '<section class="ficha-sec"><h4>Cobros <span class="mini">' + dinero(pagado) + (p.pres && p.pres.est === 'Aceptado' ? ' de ' + dinero(p.pres.m) : '') + '</span></h4>' +
        (p.pres && p.pres.est === 'Aceptado' && p.pres.m ? '<div class="progreso"><i style="width:' + Math.min(100, pagado / p.pres.m * 100) + '%"></i></div>' : '') +
        '<ul class="lista-mini">' + (pagos.map(function (x) { return '<li><span>' + x.f + ' · ' + x.c + (x.nota ? ' · ' + esc(x.nota) : '') + '</span><strong class="tabular">' + dinero(x.m) + '</strong></li>'; }).join('') || '<li class="mini">Sin cobros registrados.</li>') + '</ul>' +
        '<div class="ficha-fila ficha-fila--pago"><div class="campo"><label for="dr-pc">Concepto</label><select id="dr-pc">' + ['Valoración'].concat(TRATS).map(function (t) { return '<option' + (p.pres && p.pres.t === t ? ' selected' : '') + '>' + t + '</option>'; }).join('') + '</select></div><div class="campo"><label for="dr-pmo">Monto</label><input id="dr-pmo" inputmode="numeric" placeholder="0"></div><button class="btn btn--chico btn--secundario" data-pago-ficha="' + p.id + '">' + ic('plus') + ' Registrar</button></div></section>';
    }
    html += '<section class="ficha-sec"><h4>Citas</h4><ul class="lista-mini">' + (citas.map(function (c) { return '<li><span>' + fechaCorta(diaN(c.d)) + ', ' + c.h + ' · ' + tipoTxt(c) + '</span><strong>' + ({ llego: 'Llegó', falto: 'No llegó', pendiente: 'Por llegar' })[c.st] + '</strong></li>'; }).join('') || '<li class="mini">Sin citas esta semana.</li>') + '</ul>' + (p.rev ? '<span class="mini">Próxima revisión: ' + p.rev + '</span>' : '') + '</section>' +
      '<div class="campo"><label for="dr-n">Notas de seguimiento</label><textarea id="dr-n" rows="3" placeholder="Ejemplo: prefiere que le escriban por la tarde">' + esc(p.notas) + '</textarea><span class="campo__ayuda">Solo seguimiento. El expediente clínico va aparte.</span></div>' +
      '<div class="drawer__acciones"><button class="btn btn--primario btn--chico" data-guardar-pac="' + p.id + '">Guardar</button></div>';
    $('[data-drawer-cuerpo]').innerHTML = html;
    var d = $('#drawer'); d.classList.add('abierto'); d.setAttribute('aria-hidden', 'false'); $('#velo').classList.add('visible');
    d.querySelector('.drawer__cuerpo').scrollTop = 0;
  }
  function cerrarDrawer() { $('#drawer').classList.remove('abierto'); $('#drawer').setAttribute('aria-hidden', 'true'); if (!$('#modal').classList.contains('abierto')) $('#velo').classList.remove('visible'); }

  // ---------- Modales ----------
  function opcionesHora(d, actual) {
    return horasDe(d).map(function (h) { var no = ocupado(d, h) || bloqueado(d, h); return '<option value="' + h + '"' + (no ? ' disabled' : '') + (h === actual ? ' selected' : '') + '>' + h + (no ? ' · ocupado' : '') + '</option>'; }).join('');
  }
  function opcionesDia(sel) { var s = ''; for (var d = 0; d < 6; d++) s += '<option value="' + d + '"' + (d === sel ? ' selected' : '') + '>' + fechaLarga(diaN(d)) + '</option>'; return s; }
  function selFuente(id) { return '<div class="campo"><label for="' + id + '">¿Cómo llegó?</label><select id="' + id + '"><option value="">Elige una opción</option>' + FUENTES.map(function (f) { return '<option>' + f + '</option>'; }).join('') + '</select><span class="campo__ayuda">Obligatorio. Define si cuenta para la comisión.</span></div>'; }
  var MODAL = {
    cita: function (o) {
      var p = o.pac ? pac(o.pac) : null, d = o.dia != null ? o.dia : AG.dia;
      return { t: o.reagendar ? 'Reagendar cita' : 'Agregar cita', h: (p ? '<input type="hidden" id="m-pid" value="' + p.id + '"><p class="m-pac"><strong>' + esc(p.n) + '</strong><span class="mini">' + p.tel + '</span></p>'
        : '<div class="campo"><label for="m-n">Paciente</label><input id="m-n" list="m-lista" placeholder="Nombre del paciente" autocomplete="off"><datalist id="m-lista">' + P.map(function (x) { return '<option value="' + esc(x.n) + '">'; }).join('') + '</datalist><span class="campo__ayuda">Si es nuevo, se crea su ficha.</span></div><div class="campo"><label for="m-t">WhatsApp</label><input id="m-t" inputmode="numeric" placeholder="961 123 4567"></div>') +
        '<div class="campo"><label for="m-tipo">Tipo de cita</label><select id="m-tipo"><option>Valoración</option><option>Sesión</option><option>Seguimiento</option></select></div>' +
        '<div class="ficha-fila"><div class="campo"><label for="m-d">Día</label><select id="m-d">' + opcionesDia(d) + '</select></div><div class="campo"><label for="m-h">Hora</label><select id="m-h">' + opcionesHora(d, o.hora) + '</select></div></div>' +
        (p ? '' : selFuente('m-f')) + '<p class="mini">Cada cita dura 45 minutos.</p>', ok: o.reagendar ? 'Reagendar' : 'Agregar cita' };
    },
    paciente: function () {
      return { t: 'Agregar paciente', h: '<div class="campo"><label for="m-n">Nombre</label><input id="m-n" placeholder="Nombre completo"></div><div class="campo"><label for="m-t">WhatsApp</label><input id="m-t" inputmode="numeric" placeholder="961 123 4567"></div><div class="campo"><label for="m-i">Le interesa</label><select id="m-i">' + INTERESES.map(function (i) { return '<option>' + i + '</option>'; }).join('') + '</select></div>' + selFuente('m-f') + '<p class="mini">Entra como "Por contactar".</p>', ok: 'Agregar paciente' };
    },
    bloqueo: function () {
      var hs = MANANA.concat(TARDE).concat(['20:00']);
      return { t: 'Bloquear horario', h: '<div class="campo"><label for="m-d">Día</label><select id="m-d">' + opcionesDia(AG.dia) + '</select></div><label class="check"><input type="checkbox" id="m-todo"> Todo el día</label><div class="ficha-fila" data-rango-horas><div class="campo"><label for="m-de">Desde</label><select id="m-de">' + hs.slice(0, -1).map(function (h) { return '<option>' + h + '</option>'; }).join('') + '</select></div><div class="campo"><label for="m-a">Hasta</label><select id="m-a">' + hs.slice(1).map(function (h) { return '<option' + (h === '14:00' || h === '13:00' ? '' : '') + '>' + h + '</option>'; }).join('') + '</select></div></div><div class="campo"><label for="m-mo">Motivo</label><input id="m-mo" placeholder="Ejemplo: vacaciones, curso"></div><p class="mini">Esas horas dejan de aparecer en el sitio para agendar.</p>', ok: 'Bloquear' };
    },
    pago: function () {
      return { t: 'Registrar cobro', h: '<div class="campo"><label for="m-pp">Paciente</label><select id="m-pp">' + P.map(function (x) { return '<option value="' + x.id + '">' + esc(x.n) + '</option>'; }).join('') + '</select></div><div class="ficha-fila"><div class="campo"><label for="m-pc">Concepto</label><select id="m-pc">' + ['Valoración'].concat(TRATS).map(function (t) { return '<option>' + t + '</option>'; }).join('') + '</select></div><div class="campo"><label for="m-pm">Monto</label><input id="m-pm" inputmode="numeric" placeholder="0"></div></div><div class="campo"><label for="m-pn">Nota</label><input id="m-pn" placeholder="Ejemplo: mensualidad 2 de 12"></div>', ok: 'Registrar' };
    }
  };
  var modalCtx = null;
  function abrirModal(tipo, o) {
    o = o || {}; modalCtx = { tipo: tipo, o: o };
    var m = MODAL[tipo](o), el = $('#modal');
    el.querySelector('[data-modal-titulo]').textContent = m.t;
    el.querySelector('[data-modal-cuerpo]').innerHTML = m.h;
    el.querySelector('[data-modal-ok]').textContent = m.ok;
    el.classList.add('abierto'); el.setAttribute('aria-hidden', 'false'); $('#velo').classList.add('visible');
    var f = el.querySelector('input:not([type=hidden]), select'); if (f && window.innerWidth > 700) f.focus();
  }
  function cerrarModal() { var el = $('#modal'); el.classList.remove('abierto'); el.setAttribute('aria-hidden', 'true'); if (!$('#drawer').classList.contains('abierto')) $('#velo').classList.remove('visible'); }
  function err(id, ok) { var c = $('#' + id); if (c) c.closest('.campo').classList.toggle('con-error', !ok); return ok; }
  function confirmarModal() {
    var t = modalCtx.tipo, o = modalCtx.o;
    if (t === 'cita') {
      var pid = $('#m-pid') ? +$('#m-pid').value : 0, p = pid ? pac(pid) : null;
      if (!p) {
        var n = $('#m-n').value.trim(), ex = P.filter(function (x) { return x.n.toLowerCase() === n.toLowerCase(); })[0];
        if (ex) p = ex;
        else {
          var a = err('m-n', n.length > 1), b = err('m-t', $('#m-t').value.replace(/\D/g, '').length === 10), c = err('m-f', !!$('#m-f').value);
          if (!(a && b && c)) return;
          p = { id: ++sigId, n: n, tel: $('#m-t').value, i: 'No estoy seguro', f: $('#m-f').value, e: 'agendo', notas: '' }; P.push(p);
        }
      }
      var d = +$('#m-d').value, h = $('#m-h').value;
      if (!err('m-h', h && !ocupado(d, h) && !bloqueado(d, h))) return;
      if (o.reagendar) { var vieja = cita(o.reagendar); vieja.st = 'reagendada'; C.splice(C.indexOf(vieja), 1); }
      C.push({ id: ++sigId, d: d, h: h, p: p.id, tipo: $('#m-tipo').value, st: 'pendiente', rec: false });
      if (p.e === 'contactar' || p.e === 'no_regreso') p.e = 'agendo';
      cerrarModal(); cerrarDrawer(); toast('Cita de ' + nombre1(p) + ': ' + fechaCorta(diaN(d)) + ', ' + h); render();
    } else if (t === 'paciente') {
      var n2 = $('#m-n').value.trim();
      var ok = err('m-n', n2.length > 1) & err('m-t', $('#m-t').value.replace(/\D/g, '').length === 10) & err('m-f', !!$('#m-f').value);
      if (!ok) return;
      P.push({ id: ++sigId, n: n2, tel: $('#m-t').value, i: $('#m-i').value, f: $('#m-f').value, e: 'contactar', notas: '' });
      cerrarModal(); toast(n2.split(' ')[0] + ' quedó en Por contactar'); render();
    } else if (t === 'bloqueo') {
      var todo = $('#m-todo').checked, de = todo ? '10:00' : $('#m-de').value, hasta = todo ? '20:00' : $('#m-a').value;
      if (!err('m-a', aMin(hasta) > aMin(de))) return;
      B.push({ d: +$('#m-d').value, desde: de, hasta: hasta, motivo: $('#m-mo').value.trim() || 'Bloqueado' });
      cerrarModal(); toast('Horario bloqueado'); render();
    } else if (t === 'pago') {
      var m = +$('#m-pm').value.replace(/\D/g, '');
      if (!err('m-pm', m > 0)) return;
      PAGOS.push({ p: +$('#m-pp').value, f: fechaPago(HOY), c: $('#m-pc').value, m: m, nota: $('#m-pn').value.trim() });
      cerrarModal(); toast('Cobro registrado'); render();
    }
  }

  // ---------- Router ----------
  var TITULOS = { hoy: 'Hoy', resumen: 'Resumen', agenda: 'Agenda', pacientes: 'Pacientes', ligas: 'Ligas', cobros: 'Cobros', comision: 'Comisión', pendientes: 'Pendientes', contenido: 'Contenido', equipo: 'Equipo' };
  var actual = 'hoy';
  function render(vista) {
    if (vista !== undefined) actual = vista;
    if (!V[actual] || !puede(actual)) actual = 'hoy';
    var main = $('[data-vista-cuerpo]');
    $('[data-vista-titulo]').textContent = TITULOS[actual];
    document.body.setAttribute('data-vista', actual);
    main.innerHTML = V[actual]();
    if (vista !== undefined) { main.classList.remove('entra'); void main.offsetWidth; main.classList.add('entra'); window.scrollTo(0, 0); }
    $$('[data-ir]').forEach(function (a) { a.setAttribute('aria-current', a.getAttribute('data-ir') === actual ? 'page' : 'false'); });
    var masBtn = $('[data-mas]'); if (masBtn) masBtn.setAttribute('aria-current', ['hoy', 'agenda', 'pacientes'].indexOf(actual) < 0 ? 'page' : 'false');
    $$('[data-solo-admin]').forEach(function (el) { el.hidden = !puede(el.getAttribute('data-ir')); });
    if (window.Nubo) Nubo.mount(main);
    if (actual === 'pacientes') activarKanban();
    var mh = $('.mas-hoja'); if (mh) mh.classList.remove('abierta');
  }
  function activarKanban() {
    var arr = null;
    $$('.kcard').forEach(function (c) {
      c.addEventListener('dragstart', function () { arr = c; c.classList.add('arrastrando'); });
      c.addEventListener('dragend', function () { c.classList.remove('arrastrando'); });
    });
    $$('.kanban__col').forEach(function (col) {
      col.addEventListener('dragover', function (e) { e.preventDefault(); col.classList.add('sobre'); });
      col.addEventListener('dragleave', function () { col.classList.remove('sobre'); });
      col.addEventListener('drop', function (e) {
        e.preventDefault(); col.classList.remove('sobre'); if (!arr) return;
        var p = pac(+arr.getAttribute('data-abrir')); p.e = col.getAttribute('data-col');
        var x = $('[data-kanban]').scrollLeft; toast(nombre1(p) + ' pasó a ' + ETQ[p.e]); render(); $('[data-kanban]').scrollLeft = x;
      });
    });
  }

  document.addEventListener('DOMContentLoaded', function () {
    document.addEventListener('click', function (e) {
      var t = e.target;
      var ir = t.closest('[data-ir]');
      if (ir) { e.preventDefault(); var mh = $('.mas-hoja'); if (mh) mh.classList.remove('abierta'); location.hash = ir.getAttribute('data-ir'); return; }
      var mo = t.closest('[data-modal]');
      if (mo) { abrirModal(mo.getAttribute('data-modal'), { dia: mo.hasAttribute('data-dia') ? +mo.getAttribute('data-dia') : null, pac: mo.hasAttribute('data-pac') ? +mo.getAttribute('data-pac') : null }); return; }
      var hueco = t.closest('[data-hueco]');
      if (hueco) { var x = hueco.getAttribute('data-hueco').split('|'); abrirModal('cita', { dia: +x[0], hora: x[1] }); return; }
      var re = t.closest('[data-reagendar]');
      if (re) { var c0 = cita(+re.getAttribute('data-reagendar')); abrirModal('cita', { pac: c0.p, dia: Math.min(c0.d + 1, 5), reagendar: c0.id }); return; }
      var m = t.closest('[data-marcar]');
      if (m) {
        var c = cita(+m.closest('[data-cita]').getAttribute('data-cita')), pp = pac(c.p);
        c.st = m.getAttribute('data-marcar');
        if (c.st === 'falto') pp.e = 'no_regreso';
        toast(nombre1(pp) + (c.st === 'llego' ? ' llegó. Al terminar, actualiza su etapa en su ficha' : ' no llegó. Puedes reagendarla.')); render(); return;
      }
      var rec = t.closest('[data-recordar]');
      if (rec) { cita(+rec.getAttribute('data-recordar')).rec = true; setTimeout(function () { render(); toast('Recordatorio enviado'); }, 300); return; }
      if (t.closest('a,input,select,textarea,label')) return;
      var ab = t.closest('[data-abrir]');
      if (ab) { ficha(pac(+ab.getAttribute('data-abrir'))); return; }
      if (t.closest('[data-cerrar-drawer]')) { cerrarDrawer(); return; }
      if (t.closest('[data-cerrar-modal]')) { cerrarModal(); return; }
      if (t.id === 'velo') { if ($('#modal').classList.contains('abierto')) cerrarModal(); else cerrarDrawer(); return; }
      if (t.closest('[data-modal-ok]')) { confirmarModal(); return; }
      var g = t.closest('[data-guardar-pac]');
      if (g) {
        var p = pac(+g.getAttribute('data-guardar-pac'));
        p.e = $('#dr-etapa').value; p.notas = $('#dr-n').value;
        var tr = $('#dr-pt').value;
        if (tr) { p.pres = p.pres || { est: 'Por aceptar', m: 0 }; p.pres.t = tr; if ($('#dr-pm')) p.pres.m = +$('#dr-pm').value.replace(/\D/g, '') || 0; if (p.e === 'tratamiento') p.pres.est = 'Aceptado'; } else p.pres = null;
        cerrarDrawer(); toast('Ficha actualizada'); render(); return;
      }
      var pf = t.closest('[data-pago-ficha]');
      if (pf) {
        var mo2 = +$('#dr-pmo').value.replace(/\D/g, '');
        if (!err('dr-pmo', mo2 > 0)) return;
        var p2 = pac(+pf.getAttribute('data-pago-ficha'));
        PAGOS.push({ p: p2.id, f: fechaPago(HOY), c: $('#dr-pc').value, m: mo2 });
        toast('Cobro registrado'); ficha(p2); render(); return;
      }
      var av = t.closest('[data-ag-vista]'); if (av) { AG.vista = av.getAttribute('data-ag-vista'); render(); return; }
      var ar = t.closest('[data-ag-rango]'); if (ar) { AG.rango = ar.getAttribute('data-ag-rango'); render(); return; }
      var ad = t.closest('[data-ag-dia]'); if (ad) { AG.dia = +ad.getAttribute('data-ag-dia'); render(); return; }
      var ct = t.closest('[data-ct]'); if (ct) { CT = ct.getAttribute('data-ct'); render(); return; }
      var cp = t.closest('[data-copiar]');
      if (cp) { try { navigator.clipboard.writeText('https://' + cp.getAttribute('data-copiar')); } catch (x2) {} toast('Liga copiada'); return; }
      if (t.closest('[data-crear-liga]')) {
        var nl = $('#lg-n').value.trim(); if (!err('lg-n', !!nl)) return;
        var slug = nl.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
        L.unshift({ nombre: nl, f: $('#lg-f').value, slug: slug, clics: 0, citas: 0 }); render(); toast('Liga creada'); return;
      }
      if (t.closest('[data-invitar]')) {
        var co = $('#eq-c').value.trim(); if (!err('eq-c', /.+@.+\..+/.test(co))) return;
        EQUIPO.push({ n: co, r: $('#eq-r').value, est: 'Invitación enviada' }); render(); toast('Invitación enviada a ' + co); return;
      }
      if (t.closest('[data-subir]')) { toast('Aquí se abre para subir el archivo'); return; }
      if (t.closest('[data-guardar]')) { toast('Cambios publicados'); return; }
      if (t.closest('[data-mas]')) { $('.mas-hoja').classList.toggle('abierta'); return; }
    });
    document.addEventListener('input', function (e) {
      if (e.target.matches('[data-buscar]')) { PQ = e.target.value.toLowerCase(); $('[data-kanban]').innerHTML = kanbanCols(); activarKanban(); }
      var c = e.target.closest('.campo'); if (c) c.classList.remove('con-error');
    });
    document.addEventListener('change', function (e) {
      if (e.target.id === 'm-d' && $('#m-h')) $('#m-h').innerHTML = opcionesHora(+e.target.value);
      if (e.target.id === 'm-todo') $('[data-rango-horas]').hidden = e.target.checked;
      if (e.target.id === 'dr-etapa') $('[data-etapa-desc]').textContent = ETAPAS.filter(function (x) { return x[0] === e.target.value; })[0][2];
      if (e.target.id === 'm-n' && $('#m-t')) { var ex = P.filter(function (x) { return x.n === e.target.value; })[0]; if (ex) { $('#m-t').value = ex.tel; $('#m-f') && ($('#m-f').closest('.campo').hidden = true); } else if ($('#m-f')) $('#m-f').closest('.campo').hidden = false; }
      if (e.target.matches('[data-rol]')) { ROL = e.target.value; toast(e.target.value === 'recepcion' ? 'Vista de recepción: sin montos' : 'Vista completa'); render(); }
      var c = e.target.closest('.campo'); if (c) c.classList.remove('con-error');
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') { if ($('#modal').classList.contains('abierto')) cerrarModal(); else cerrarDrawer(); }
      if (e.key === 'Enter' && e.target.matches('.kcard, [data-abrir][tabindex]')) ficha(pac(+e.target.getAttribute('data-abrir')));
    });
    $$('[data-fecha-hoy]').forEach(function (el) { el.textContent = fechaLarga(HOY); });
    window.addEventListener('hashchange', function () { render(location.hash.slice(1) || 'hoy'); });
    render(location.hash.slice(1) || 'hoy');
  });
})();
