(function () {
  var DIAS = ['Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado'];
  var DC = ['Dom', 'Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb'];
  var MESES = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'];
  var ETAPAS = [
    ['nuevo', 'Nuevo'], ['agendo', 'Agendó'], ['asistio', 'Asistió'], ['presupuesto', 'Con presupuesto'], ['tratamiento', 'En tratamiento'], ['no_regreso', 'No regresó']
  ];
  var ETQ = {}; ETAPAS.forEach(function (e) { ETQ[e[0]] = e[1]; });
  var VORTEX = ['Instagram', 'Facebook', 'Google', 'Anuncio', 'Sitio web'];
  var COMISIONABLES = ['Blanqueamiento', 'Ortodoncia', 'Prótesis'];
  function ic(n, c) { return '<svg class="i' + (c ? ' ' + c : '') + '" aria-hidden="true"><use href="#i-' + n + '"/></svg>'; }
  function $(s, r) { return (r || document).querySelector(s); }
  function $$(s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); }
  function dinero(n) { return '$' + Math.round(n).toLocaleString('es-MX'); }

  function hoyMx() {
    var p = new Intl.DateTimeFormat('en-CA', { timeZone: 'America/Mexico_City', year: 'numeric', month: '2-digit', day: '2-digit' }).formatToParts(new Date());
    var o = {}; p.forEach(function (x) { o[x.type] = x.value; });
    return new Date(Date.UTC(+o.year, +o.month - 1, +o.day));
  }
  var HOY = hoyMx();
  var LUNES = new Date(HOY); var wd = HOY.getUTCDay();
  LUNES.setUTCDate(HOY.getUTCDate() + (wd === 0 ? 1 : 1 - wd));
  function diaN(n) { var d = new Date(LUNES); d.setUTCDate(LUNES.getUTCDate() + n); return d; }
  function fechaCorta(d) { return DC[d.getUTCDay()] + ' ' + d.getUTCDate(); }
  function fechaLarga(d) { return DIAS[d.getUTCDay()] + ' ' + d.getUTCDate() + ' de ' + MESES[d.getUTCMonth()]; }
  var DIA_DEMO = HOY.getUTCDay() === 0 ? 0 : HOY.getUTCDay() - 1;
  var AHORA = (function () { var p = new Intl.DateTimeFormat('en-GB', { timeZone: 'America/Mexico_City', hour: '2-digit', minute: '2-digit', hour12: false }).format(new Date()).split(':'); return (+p[0] % 24) * 60 + (+p[1]); })();
  function aMin(h) { var p = h.split(':'); return +p[0] * 60 + +p[1]; }
  function saludo() { if (HOY.getUTCDay() === 0) return 'Buenos días, doctora'; return AHORA < 12 * 60 ? 'Buenos días, doctora' : AHORA < 19 * 60 ? 'Buenas tardes, doctora' : 'Buenas noches, doctora'; }

  var P = [
    { id: 1, n: 'Mariana Gómez Ruiz', tel: '961 214 3381', i: 'Blanqueamiento', f: 'Instagram', e: 'tratamiento', t: 'Blanqueamiento', m: 3500, nino: false },
    { id: 2, n: 'Luis Alberto Pérez', tel: '961 330 9142', i: 'Ortodoncia', f: 'Facebook', e: 'tratamiento', t: 'Ortodoncia', m: 6000, nino: false },
    { id: 3, n: 'Fernanda López', tel: '961 118 2207', i: 'Limpieza o revisión', f: 'Me recomendaron', e: 'asistio', t: '', m: 0, nino: false },
    { id: 4, n: 'Diego Hernández', tel: '961 455 0193', i: 'Ortodoncia', f: 'Anuncio', e: 'presupuesto', t: 'Ortodoncia', m: 0, nino: false },
    { id: 5, n: 'Sofía Martínez (8 años)', tel: '961 287 6650', i: 'Limpieza o revisión', f: 'Google', e: 'agendo', t: '', m: 0, nino: true },
    { id: 6, n: 'Rosa Elena Cruz', tel: '961 602 1185', i: 'Prótesis', f: 'Pasé por ahí', e: 'tratamiento', t: 'Prótesis', m: 4200, nino: false },
    { id: 7, n: 'Jorge Velázquez', tel: '961 774 3029', i: 'Prótesis', f: 'Facebook', e: 'tratamiento', t: 'Prótesis', m: 5000, nino: false },
    { id: 8, n: 'Andrea Moreno', tel: '961 139 8846', i: 'Blanqueamiento', f: 'Instagram', e: 'agendo', t: '', m: 0, nino: false },
    { id: 9, n: 'Carlos Aguilar', tel: '961 520 4471', i: 'No estoy seguro', f: 'Sitio web', e: 'nuevo', t: '', m: 0, nino: false },
    { id: 10, n: 'Valeria Ramírez', tel: '961 368 2954', i: 'Blanqueamiento', f: 'Anuncio', e: 'agendo', t: '', m: 0, nino: false },
    { id: 11, n: 'Emiliano Castillo (11 años)', tel: '961 247 1108', i: 'Ortodoncia', f: 'Me recomendaron', e: 'presupuesto', t: 'Ortodoncia', m: 0, nino: true },
    { id: 12, n: 'Patricia Domínguez', tel: '961 813 5520', i: 'Limpieza o revisión', f: 'Google', e: 'no_regreso', t: '', m: 0, nino: false },
    { id: 13, n: 'Ricardo Ozuna', tel: '961 690 3347', i: 'Blanqueamiento', f: 'Instagram', e: 'agendo', t: '', m: 0, nino: false },
    { id: 14, n: 'Guadalupe Torres', tel: '961 145 7762', i: 'Prótesis', f: 'Sitio web', e: 'agendo', t: '', m: 0, nino: false }
  ];
  function pac(id) { for (var k = 0; k < P.length; k++) if (P[k].id === id) return P[k]; }
  var C = [
    [0, '10:00', 5], [0, '11:30', 8], [0, '16:45', 10], [0, '18:15', 2],
    [1, '10:45', 13], [1, '17:30', 4], [2, '12:15', 6], [2, '16:00', 11], [2, '19:00', 14],
    [3, '10:00', 7], [3, '13:00', 1], [4, '11:30', 3]
  ].map(function (c, k) { var pasada = c[0] < DIA_DEMO || (c[0] === DIA_DEMO && HOY.getUTCDay() !== 0 && aMin(c[1]) + 45 <= AHORA); return { id: k + 1, d: c[0], h: c[1], p: c[2], st: pasada ? 'llego' : 'pendiente' }; });
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
    ['Dominio', 'Nombre y acceso para conectarlo', 'pendiente'],
    ['Aviso de publicidad COFEPRIS', 'Número y leyenda para el pie de página', 'pendiente'],
    ['Edades en odontopediatría', 'Desde qué edad atienden', 'en_revision'],
    ['Reseñas de Google', 'Faltan 2 textos completos', 'en_revision'],
    ['Horario', 'Lunes a sábado, confirmado', 'listo']
  ];

  function toast(t) {
    var el = $('#toast');
    el.textContent = t; el.classList.add('visible');
    clearTimeout(el._t); el._t = setTimeout(function () { el.classList.remove('visible'); }, 2400);
  }
  function chipEtapa(e) { return '<span class="etapa etapa--' + e + '">' + ETQ[e] + '</span>'; }
  function esVortex(p) { return VORTEX.indexOf(p.f) > -1; }
  function waUrl(p, txt) { return 'https://wa.me/52' + p.tel.replace(/\D/g, '') + '?text=' + encodeURIComponent(txt); }

  var V = {};

  V.resumen = function () {
    var semana = C.length;
    var nuevos = P.filter(function (p) { return p.e === 'nuevo' || p.e === 'agendo'; }).length;
    var llegaron = C.filter(function (c) { return c.st === 'llego'; }).length, faltaron = C.filter(function (c) { return c.st === 'falto'; }).length;
    var com = P.filter(function (p) { return esVortex(p) && p.e === 'tratamiento' && COMISIONABLES.indexOf(p.t) > -1; }).reduce(function (a, p) { return a + p.m * 0.3; }, 0);
    var fuentes = {}; P.forEach(function (p) { fuentes[p.f] = (fuentes[p.f] || 0) + 1; });
    var orden = Object.keys(fuentes).sort(function (a, b) { return fuentes[b] - fuentes[a]; });
    var max = fuentes[orden[0]];
    var emb = [['Agendaron', P.filter(function (p) { return p.e !== 'nuevo'; }).length], ['Asistieron', P.filter(function (p) { return ['asistio', 'presupuesto', 'tratamiento'].indexOf(p.e) > -1; }).length], ['Con presupuesto', P.filter(function (p) { return ['presupuesto', 'tratamiento'].indexOf(p.e) > -1; }).length], ['En tratamiento', P.filter(function (p) { return p.e === 'tratamiento'; }).length]];
    var proximas = C.filter(function (c) { return c.d >= DIA_DEMO && c.st === 'pendiente'; }).slice(0, 5);
    return '<div class="kpis">' +
      kpi('calendar', 'Citas esta semana', semana, 'Lunes a sábado') +
      kpi('users', 'Pacientes nuevos', nuevos, 'Por contactar o agendados') +
      kpi('check', 'Asistencia del mes', '88%', '22 de 25 llegaron a su cita') +
      kpi('receipt-2', 'Comisión del mes', dinero(com), '30% de tratamientos de Vortex') + '</div>' +
      '<div class="grid-resumen">' +
      '<div class="tarjeta-p"><div class="tarjeta-p__cab"><h3>Pacientes por fuente</h3><span class="mini">Este mes</span></div><div class="barras">' + orden.map(function (f) {
        return '<div class="barra"><span>' + f + (esVortex({ f: f }) ? ' <em>Vortex</em>' : '') + '</span><div class="barra__pista"><i style="width:' + (fuentes[f] / max * 100) + '%"></i></div><strong>' + fuentes[f] + '</strong></div>';
      }).join('') + '</div></div>' +
      '<div class="tarjeta-p"><div class="tarjeta-p__cab"><h3>De la cita al tratamiento</h3><span class="mini">Este mes</span></div><div class="embudo">' + emb.map(function (x) {
        return '<div class="embudo__paso"><div class="embudo__barra" style="width:' + (x[1] / emb[0][1] * 100) + '%"><strong>' + x[1] + '</strong></div><span>' + x[0] + '</span></div>';
      }).join('') + '</div></div>' +
      '<div class="tarjeta-p"><div class="tarjeta-p__cab"><h3>Próximas citas</h3><a href="#agenda" class="mini enlace">Ver agenda</a></div><ul class="lista-citas">' + proximas.map(function (c) {
        var p = pac(c.p); return '<li><span class="hora tabular">' + fechaCorta(diaN(c.d)) + ', ' + c.h + '</span><span class="nombre">' + p.n + '</span><span class="mini">' + p.i + '</span></li>';
      }).join('') + '</ul></div>' +
      '<div class="tarjeta-p"><div class="tarjeta-p__cab"><h3>Páginas más visitadas</h3><span class="mini">Últimos 7 días</span></div><ul class="lista-paginas">' + [['Inicio', 612], ['Agendar', 233], ['Blanqueamiento', 148], ['Ortodoncia', 97], ['Nubo explica', 41]].map(function (x, k, a) {
        return '<li><span>' + x[0] + '</span><div class="barra__pista"><i style="width:' + (x[1] / a[0][1] * 100) + '%"></i></div><strong class="tabular">' + x[1] + '</strong></li>';
      }).join('') + '</ul></div></div>';
  };
  function kpi(i, t, v, s) { return '<div class="kpi"><span class="kpi__icono">' + ic(i) + '</span><span class="kpi__t">' + t + '</span><strong class="kpi__v tabular">' + v + '</strong><span class="mini">' + s + '</span></div>'; }

  V.agenda = function () {
    var horas = ['10:00', '10:45', '11:30', '12:15', '13:00', '16:00', '16:45', '17:30', '18:15', '19:00'];
    var html = '<div class="agenda-cab"><div><h3 style="margin:0">Semana del ' + fechaLarga(diaN(0)).toLowerCase() + '</h3><span class="mini">Sincroniza con Google Calendar cuando se conecte</span></div><div class="leyenda"><span class="ley ley--pendiente">Por llegar</span><span class="ley ley--llego">Llegó</span><span class="ley ley--falto">No llegó</span></div></div>';
    html += '<div class="semana"><div class="semana__grid" style="grid-template-columns: 64px repeat(6, minmax(120px, 1fr))"><div></div>';
    for (var d = 0; d < 6; d++) html += '<div class="semana__dia' + (d === DIA_DEMO ? ' hoy' : '') + '">' + fechaCorta(diaN(d)) + '</div>';
    horas.forEach(function (h) {
      html += '<div class="semana__hora tabular">' + h + '</div>';
      for (var d = 0; d < 6; d++) {
        var c = C.filter(function (x) { return x.d === d && x.h === h; })[0];
        var cerrado = d === 5 && h >= '16:00';
        html += '<div class="semana__celda' + (cerrado ? ' cerrada' : '') + '">' + (c ? citaBloque(c) : '') + '</div>';
      }
    });
    return html + '</div></div>';
  };
  function citaBloque(c) { var p = pac(c.p); return '<button class="cita cita--' + c.st + '" data-cita="' + c.id + '"><strong>' + p.n.split(' ').slice(0, 2).join(' ') + '</strong><span>' + p.i + '</span></button>'; }

  V.pacientes = function () {
    return '<div class="filtros"><label class="buscador">' + ic('search') + '<input type="search" placeholder="Buscar paciente" data-buscar></label><div class="chips" data-filtro-etapa><button class="chip" aria-pressed="true" data-etapa="">Todos</button>' + ETAPAS.map(function (e) { return '<button class="chip" aria-pressed="false" data-etapa="' + e[0] + '">' + e[1] + '</button>'; }).join('') + '</div></div>' +
      '<div class="tabla-envuelta"><table class="tabla tabla-movil"><thead><tr><th>Paciente</th><th>Interés</th><th>Fuente</th><th>Etapa</th><th class="der">Monto</th></tr></thead><tbody data-tbody></tbody></table></div>';
  };
  function filasPacientes(q, et) {
    return P.filter(function (p) { return (!et || p.e === et) && (!q || p.n.toLowerCase().indexOf(q) > -1); }).map(function (p) {
      return '<tr data-pac="' + p.id + '" tabindex="0"><td><strong>' + p.n + '</strong><span class="mini tabular">' + p.tel + '</span></td><td>' + p.i + '</td><td>' + p.f + (esVortex(p) ? ' <em class="vx">Vortex</em>' : '') + '</td><td>' + chipEtapa(p.e) + '</td><td class="der tabular">' + (p.m ? dinero(p.m) : '') + '</td></tr>';
    }).join('') || '<tr><td colspan="5" class="vacio">Ningún paciente con ese filtro.</td></tr>';
  }

  V.pipeline = function () {
    return '<p class="mini" style="margin:0 0 14px">Arrastra a un paciente para cambiar su etapa. En celular, toca y elige la etapa.</p><div class="kanban">' + ETAPAS.map(function (e) {
      var ps = P.filter(function (p) { return p.e === e[0]; });
      return '<div class="kanban__col" data-col="' + e[0] + '"><div class="kanban__cab">' + chipEtapa(e[0]) + '<span class="tabular">' + ps.length + '</span></div><div class="kanban__lista">' + ps.map(function (p) {
        return '<div class="kcard" draggable="true" data-pac="' + p.id + '" tabindex="0"><strong>' + p.n + '</strong><span>' + p.i + '</span><div class="kcard__pie"><span class="fuente">' + p.f + '</span>' + (p.m ? '<span class="tabular">' + dinero(p.m) + '</span>' : '') + '</div></div>';
      }).join('') + '</div></div>';
    }).join('') + '</div>';
  };

  V.hoy = function () {
    var d = DIA_DEMO, citas = C.filter(function (c) { return c.d === d; });
    var llegan = citas.filter(function (c) { return c.st === 'llego'; }).length;
    return '<div class="hoy-cab"><div class="nubo" data-nubo="saluda" data-mirada data-saluda></div><div><span class="mini">' + fechaLarga(diaN(d)) + (d === DIA_DEMO && HOY.getUTCDay() === 0 ? ' (mañana)' : '') + '</span><h2>' + saludo() + '</h2><p>' + (HOY.getUTCDay() === 0 ? 'Mañana hay' : 'Hoy hay') + ' <strong>' + citas.length + ' citas</strong>. ' + (llegan === 1 ? 'Una ya llegó.' : llegan ? llegan + ' ya llegaron.' : 'Ninguna ha llegado todavía.') + '</p></div></div>' +
      '<div class="kpis kpis--compacto">' + kpi('calendar', 'Esta semana', C.length, 'citas') + kpi('users', 'Por contactar', P.filter(function (p) { return p.e === 'nuevo'; }).length, 'pacientes nuevos') + kpi('receipt-2', 'Comisión del mes', dinero(P.filter(function (p) { return esVortex(p) && p.e === 'tratamiento' && COMISIONABLES.indexOf(p.t) > -1; }).reduce(function (a, p) { return a + p.m * 0.3; }, 0)), '30% Vortex') + '</div>' +
      '<h3 class="sub-p">' + (HOY.getUTCDay() === 0 ? 'Citas de mañana' : 'Citas de hoy') + '</h3><ul class="linea-hoy">' + citas.map(function (c) {
        var p = pac(c.p);
        return '<li class="cita-hoy cita-hoy--' + c.st + '" data-cita="' + c.id + '"><span class="hora tabular">' + c.h + '</span><div class="cita-hoy__info"><strong>' + p.n + '</strong><span>' + p.i + ' · ' + p.f + '</span></div><div class="cita-hoy__acciones">' +
          '<a class="icono-btn" target="_blank" rel="noopener" href="' + waUrl(p, 'Hola ' + p.n.split(' ')[0] + ', te escribimos de Dental Díaz para confirmar tu valoración de hoy a las ' + c.h + '.') + '" aria-label="Confirmar por WhatsApp">' + ic('brand-whatsapp') + '</a>' +
          '<button class="btn btn--chico ' + (c.st === 'llego' ? 'btn--primario' : 'btn--secundario') + '" data-marcar="llego">' + ic('check') + ' Llegó</button>' +
          '<button class="btn btn--chico btn--secundario" data-marcar="falto">No llegó</button></div></li>';
      }).join('') + '</ul>';
  };

  V.agendaDias = function () {
    var html = '<div class="dias-tabs" role="tablist">';
    for (var d = 0; d < 6; d++) html += '<button class="dia" role="tab" aria-pressed="' + (d === DIA_DEMO ? 'true' : 'false') + '" data-ver-dia="' + d + '"><span>' + DC[diaN(d).getUTCDay()] + '</span><strong>' + diaN(d).getUTCDate() + '</strong><small>' + C.filter(function (c) { return c.d === d; }).length + ' citas</small></button>';
    return html + '</div><ul class="linea-hoy" data-lista-dia></ul>';
  };
  function listaDia(d) {
    var citas = C.filter(function (c) { return c.d === d; });
    return citas.map(function (c) { var p = pac(c.p); return '<li class="cita-hoy cita-hoy--' + c.st + '"><span class="hora tabular">' + c.h + '</span><div class="cita-hoy__info"><strong>' + p.n + '</strong><span>' + p.i + ' · ' + p.f + '</span></div>' + chipEtapa(p.e) + '</li>'; }).join('') || '<li class="vacio">Sin citas este día.</li>';
  }

  V.ligas = function () {
    return '<div class="tarjeta-p ligas-form"><h3>Crear liga</h3><p class="mini">Cada liga guarda de dónde llegó el paciente. Así sabemos qué funciona y qué cuenta para la comisión.</p><div class="ligas-form__campos"><div class="campo"><label for="lg-n">Nombre</label><input id="lg-n" placeholder="Anuncio ortodoncia diciembre"></div><div class="campo"><label for="lg-f">Fuente</label><select id="lg-f"><option>Anuncio</option><option>Instagram</option><option>Facebook</option><option>Google</option><option>Sitio web</option></select></div><button class="btn btn--primario" data-crear-liga>' + ic('plus') + ' Crear</button></div></div>' +
      '<div class="tabla-envuelta"><table class="tabla tabla-movil"><thead><tr><th>Liga</th><th>Fuente</th><th class="der">Clics</th><th class="der">Citas</th><th></th></tr></thead><tbody data-ligas>' + filasLigas() + '</tbody></table></div>';
  };
  function filasLigas() {
    return L.map(function (l, k) { var url = 'dentaldiaz.mx/?src=' + l.slug; return '<tr><td><strong>' + l.nombre + '</strong><span class="mini mono">' + url + '</span></td><td>' + l.f + '</td><td class="der tabular">' + l.clics + '<span class="solo-movil"> clics</span></td><td class="der tabular">' + l.citas + '<span class="solo-movil"> citas</span></td><td class="der"><button class="btn btn--chico btn--secundario" data-copiar="' + url + '">' + ic('copy') + ' Copiar</button></td></tr>'; }).join('');
  }

  V.comision = function () {
    var filas = P.filter(function (p) { return p.e === 'tratamiento' && COMISIONABLES.indexOf(p.t) > -1; });
    var total = 0;
    var cuerpo = filas.map(function (p) {
      var cuenta = esVortex(p); var c = cuenta ? p.m * 0.3 : 0; total += c;
      return '<tr class="' + (cuenta ? '' : 'apagada') + '"><td><strong>' + p.n + '</strong></td><td>' + p.t + '</td><td>' + p.f + (cuenta ? ' <em class="vx">Vortex</em>' : '') + '</td><td class="der tabular">' + dinero(p.m) + '</td><td class="der tabular"><strong>' + (cuenta ? dinero(c) : 'No aplica') + '</strong></td></tr>';
    }).join('');
    return '<div class="com-cab"><div class="kpi kpi--grande"><span class="kpi__t">Comisión de ' + MESES[HOY.getUTCMonth()] + '</span><strong class="kpi__v tabular">' + dinero(total) + '</strong><span class="mini">30% sobre blanqueamiento, ortodoncia y prótesis de pacientes que llegaron por Vortex. Se calcula solo con lo que la clínica marca como cobrado.</span></div></div>' +
      '<div class="tabla-envuelta"><table class="tabla tabla-movil"><thead><tr><th>Paciente</th><th>Tratamiento</th><th>Fuente</th><th class="der">Cobrado</th><th class="der">Comisión</th></tr></thead><tbody>' + cuerpo + '</tbody><tfoot><tr><td colspan="4">Total del periodo</td><td class="der tabular"><strong>' + dinero(total) + '</strong></td></tr></tfoot></table></div>';
  };

  V.pendientes = function () {
    var est = { pendiente: 'Pendiente', en_revision: 'En revisión', listo: 'Listo' };
    return '<p class="mini" style="margin:0 0 16px">Lo que necesitamos de la clínica para terminar el sitio. Sube el archivo o escribe la respuesta y nos llega directo.</p><div class="pendientes">' + PEND.map(function (x, k) {
      return '<div class="pend pend--' + x[2] + '"><div><strong>' + x[0] + '</strong><span class="mini">' + x[1] + '</span></div><span class="estado estado--' + x[2] + '">' + est[x[2]] + '</span>' + (x[2] !== 'listo' ? '<button class="btn btn--chico btn--secundario" data-subir="' + k + '">' + ic('upload') + ' Subir</button>' : '<span></span>') + '</div>';
    }).join('') + '</div>';
  };

  V.contenido = function () {
    return '<div class="contenido-grid"><div class="tarjeta-p"><h3>Inicio</h3><div class="campo"><label>Título principal</label><input value="Te explicamos todo antes de empezar"></div><div class="campo"><label>Texto debajo del título</label><textarea rows="3">Clínica dental familiar en Terán. Revisamos con calma, te enseñamos tus radiografías y tu plan va por escrito.</textarea></div></div>' +
      '<div class="tarjeta-p"><h3>Horario</h3><div class="campo"><label>Lunes a viernes</label><input value="10:00 a 14:00 y 16:00 a 20:00"></div><div class="campo"><label>Sábado</label><input value="10:00 a 14:00"></div><div class="campo"><label>Aviso en el sitio</label><input placeholder="Cerrado el 12 de diciembre"></div></div>' +
      '<div class="tarjeta-p"><h3>Preguntas frecuentes</h3><div class="campo"><label>¿La valoración tiene costo?</label><textarea rows="3">Sí, $350. Incluye revisión completa, dos radiografías periapicales, diagnóstico y tu plan de tratamiento por escrito.</textarea></div><button class="enlace" style="border:0; background-color: transparent; cursor:pointer">' + ic('plus') + ' Agregar pregunta</button></div>' +
      '<div class="tarjeta-p"><h3>Fotos</h3><div class="fotos-mini">' + ['Hero', 'Doctora', 'Recepción', 'Consultorio'].map(function (f) { return '<button class="foto-mini">' + ic('camera') + '<span>' + f + '</span></button>'; }).join('') + '</div></div></div>' +
      '<div class="guardar-barra"><span class="mini">Los cambios se publican al momento.</span><button class="btn btn--primario" data-guardar>Guardar cambios</button></div>';
  };

  function drawer(p) {
    var d = $('#drawer');
    d.querySelector('[data-drawer-cuerpo]').innerHTML = '<h3>' + p.n + '</h3><p class="mini tabular">' + p.tel + '</p>' +
      '<dl class="ficha"><div><dt>Interés</dt><dd>' + p.i + '</dd></div><div><dt>Fuente</dt><dd>' + p.f + (esVortex(p) ? ' <em class="vx">Vortex</em>' : '') + '</dd></div><div><dt>Para</dt><dd>' + (p.nino ? 'Un niño' : 'Adulto') + '</dd></div></dl>' +
      '<div class="campo"><label for="dr-etapa">Etapa</label><select id="dr-etapa">' + ETAPAS.map(function (e) { return '<option value="' + e[0] + '"' + (e[0] === p.e ? ' selected' : '') + '>' + e[1] + '</option>'; }).join('') + '</select></div>' +
      '<div class="campo"><label for="dr-t">Tratamiento</label><select id="dr-t"><option value="">Sin tratamiento</option>' + ['Blanqueamiento', 'Ortodoncia', 'Prótesis', 'Limpieza', 'Resina', 'Endodoncia', 'Implante'].map(function (t) { return '<option' + (t === p.t ? ' selected' : '') + '>' + t + '</option>'; }).join('') + '</select></div>' +
      '<div class="campo"><label for="dr-m">Monto cobrado</label><input id="dr-m" inputmode="numeric" value="' + (p.m || '') + '" placeholder="0"></div>' +
      '<div class="campo"><label for="dr-n">Notas</label><textarea id="dr-n" rows="3" placeholder="Lo que conviene recordar para la próxima cita"></textarea></div>' +
      '<div class="drawer__acciones"><a class="btn btn--whatsapp btn--chico" target="_blank" rel="noopener" href="' + waUrl(p, 'Hola ' + p.n.split(' ')[0] + ', te escribimos de Dental Díaz.') + '">' + ic('brand-whatsapp') + ' WhatsApp</a><button class="btn btn--primario btn--chico" data-guardar-pac="' + p.id + '">Guardar</button></div>';
    d.classList.add('abierto'); d.setAttribute('aria-hidden', 'false');
    $('#velo').classList.add('visible');
  }
  function cerrarDrawer() { $('#drawer').classList.remove('abierto'); $('#drawer').setAttribute('aria-hidden', 'true'); $('#velo').classList.remove('visible'); }

  var TITULOS = { resumen: 'Resumen', agenda: 'Agenda', pacientes: 'Pacientes', ligas: 'Ligas', comision: 'Comisión', pendientes: 'Pendientes', contenido: 'Contenido', hoy: 'Hoy' };

  function render(vista) {
    var app = document.body.getAttribute('data-panel');
    var mapa = app === 'b' ? { hoy: V.hoy, agenda: V.agendaDias, pacientes: V.pipeline, ligas: V.ligas, comision: V.comision, pendientes: V.pendientes, contenido: V.contenido } : { resumen: V.resumen, agenda: V.agenda, pacientes: V.pacientes, ligas: V.ligas, comision: V.comision, pendientes: V.pendientes, contenido: V.contenido };
    if (!mapa[vista]) vista = app === 'b' ? 'hoy' : 'resumen';
    var main = $('[data-vista-cuerpo]');
    $('[data-vista-titulo]').textContent = TITULOS[vista];
    document.body.setAttribute('data-vista', vista);
    main.innerHTML = mapa[vista]();
    main.classList.remove('entra'); void main.offsetWidth; main.classList.add('entra');
    $$('[data-ir]').forEach(function (a) { a.setAttribute('aria-current', a.getAttribute('data-ir') === vista ? 'page' : 'false'); });
    var masBtn = $('[data-mas]'); if (masBtn) masBtn.setAttribute('aria-current', ['ligas', 'comision', 'pendientes', 'contenido'].indexOf(vista) > -1 ? 'page' : 'false');
    if (window.Nubo) Nubo.mount(main);
    if (vista === 'pacientes' && app !== 'b') {
      var tb = $('[data-tbody]'), q = '', et = '';
      tb.innerHTML = filasPacientes(q, et);
      $('[data-buscar]').addEventListener('input', function (e) { q = e.target.value.toLowerCase(); tb.innerHTML = filasPacientes(q, et); });
      $('[data-filtro-etapa]').addEventListener('click', function (e) {
        var b = e.target.closest('[data-etapa]'); if (!b) return;
        $$('[data-etapa]').forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
        et = b.getAttribute('data-etapa'); tb.innerHTML = filasPacientes(q, et);
      });
    }
    if (vista === 'agenda' && app === 'b') {
      var l = $('[data-lista-dia]'); l.innerHTML = listaDia(DIA_DEMO);
      $$('[data-ver-dia]').forEach(function (b) { b.addEventListener('click', function () { $$('[data-ver-dia]').forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); }); l.innerHTML = listaDia(+b.getAttribute('data-ver-dia')); }); });
    }
    if (vista === 'pacientes' && app === 'b') activarKanban();
    window.scrollTo(0, 0);
    if ($('.mas-hoja')) $('.mas-hoja').classList.remove('abierta');
  }

  function activarKanban() {
    var arrastrado = null;
    $$('.kcard').forEach(function (c) {
      c.addEventListener('dragstart', function () { arrastrado = c; c.classList.add('arrastrando'); });
      c.addEventListener('dragend', function () { c.classList.remove('arrastrando'); });
    });
    $$('.kanban__col').forEach(function (col) {
      col.addEventListener('dragover', function (e) { e.preventDefault(); col.classList.add('sobre'); });
      col.addEventListener('dragleave', function () { col.classList.remove('sobre'); });
      col.addEventListener('drop', function (e) {
        e.preventDefault(); col.classList.remove('sobre');
        if (!arrastrado) return;
        var p = pac(+arrastrado.getAttribute('data-pac')); p.e = col.getAttribute('data-col');
        toast(p.n.split(' ')[0] + ' pasó a ' + ETQ[p.e]);
        render('pacientes');
      });
    });
  }

  document.addEventListener('DOMContentLoaded', function () {
    document.addEventListener('click', function (e) {
      var ir = e.target.closest('[data-ir]');
      if (ir) { e.preventDefault(); document.body.classList.remove('lateral-abierto'); if ($('.mas-hoja')) $('.mas-hoja').classList.remove('abierta'); location.hash = ir.getAttribute('data-ir'); return; }
      var fila = e.target.closest('[data-pac]');
      if (fila && !e.target.closest('a,button.btn')) { drawer(pac(+fila.getAttribute('data-pac'))); return; }
      var cita = e.target.closest('.cita[data-cita]');
      if (cita) { var c = C[+cita.getAttribute('data-cita') - 1]; drawer(pac(c.p)); return; }
      var m = e.target.closest('[data-marcar]');
      if (m) {
        var li = m.closest('[data-cita]'), c2 = C[+li.getAttribute('data-cita') - 1];
        c2.st = m.getAttribute('data-marcar');
        if (c2.st === 'llego') { var pp = pac(c2.p); if (pp.e === 'agendo') pp.e = 'asistio'; }
        toast(pac(c2.p).n.split(' ')[0] + (c2.st === 'llego' ? ' llegó a su cita' : ' no llegó'));
        render('hoy'); return;
      }
      if (e.target.closest('[data-cerrar-drawer]') || e.target.id === 'velo') { cerrarDrawer(); return; }
      var g = e.target.closest('[data-guardar-pac]');
      if (g) {
        var p = pac(+g.getAttribute('data-guardar-pac'));
        p.e = $('#dr-etapa').value; p.t = $('#dr-t').value; p.m = +($('#dr-m').value.replace(/\D/g, '')) || 0;
        cerrarDrawer(); toast('Paciente actualizado'); render(location.hash.slice(1)); return;
      }
      var cp = e.target.closest('[data-copiar]');
      if (cp) { try { navigator.clipboard.writeText('https://' + cp.getAttribute('data-copiar')); } catch (x) {} toast('Liga copiada'); return; }
      if (e.target.closest('[data-crear-liga]')) {
        var n = $('#lg-n').value.trim(); if (!n) { $('#lg-n').closest('.campo').classList.add('con-error'); return; }
        var slug = n.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
        L.unshift({ nombre: n, f: $('#lg-f').value, slug: slug, clics: 0, citas: 0 });
        $('[data-ligas]').innerHTML = filasLigas(); $('#lg-n').value = ''; toast('Liga creada'); return;
      }
      if (e.target.closest('[data-subir]')) { toast('Aquí se abre para subir el archivo'); return; }
      if (e.target.closest('[data-guardar]')) { toast('Cambios publicados'); return; }
      if (e.target.closest('[data-mas]')) { $('.mas-hoja').classList.toggle('abierta'); return; }
      if (e.target.closest('[data-menu-lateral]')) { document.body.classList.toggle('lateral-abierto'); return; }
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') cerrarDrawer();
      if (e.key === 'Enter' && e.target.matches('tr[data-pac], .kcard')) drawer(pac(+e.target.getAttribute('data-pac')));
    });
    document.addEventListener('change', function (e) { if (e.target.id === 'lg-n') e.target.closest('.campo').classList.remove('con-error'); });
    $$('[data-fecha-hoy]').forEach(function (el) { el.textContent = fechaLarga(HOY); });
    window.addEventListener('hashchange', function () { document.body.classList.remove('lateral-abierto'); render(location.hash.slice(1)); });
    render(location.hash.slice(1));
  });
})();
