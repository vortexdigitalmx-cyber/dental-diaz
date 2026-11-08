WA = "https://wa.me/529611385698?text=Hola%2C%20quiero%20informes%20de%20una%20valoraci%C3%B3n"
MAPS = "https://share.google/V82Wj5DA7v3PU01So"
MAPA_EMBED = "https://maps.google.com/maps?q=2da%20Norte%20Oriente%20438%2C%20Ter%C3%A1n%2C%20Tuxtla%20Guti%C3%A9rrez%2C%20Chiapas&z=16&output=embed"

def ic(n, cls=""):
    extra = (" " + cls) if cls else ""
    rel = " i--relleno" if n == "star-filled" else ""
    return f'<svg class="i{rel}{extra}" aria-hidden="true"><use href="#i-{n}"/></svg>'

def estrellas():
    return '<span class="estrellas" aria-label="5 estrellas">' + "".join(ic("star-filled") for _ in range(5)) + "</span>"

def foto(titulo, texto, extra=""):
    return f'<div class="foto {extra}"><div class="foto__guia"><b>{ic("camera")} {titulo}</b>{texto}</div></div>'

def cabeza(titulo, css_extra):
    return f'''<!doctype html>
<html lang="es-MX">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titulo}</title>
<meta name="description" content="Clínica dental familiar en Terán, Tuxtla Gutiérrez. Valoración con radiografías y plan por escrito. Blanqueamiento, ortodoncia, prótesis y odontopediatría.">
<meta name="robots" content="noindex">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,600;9..40,700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/tokens.css">
<link rel="stylesheet" href="assets/css/components.css">
<link rel="stylesheet" href="assets/css/inicio.css">
<link rel="stylesheet" href="assets/css/agenda.css">
<style>
{css_extra}
</style>
</head>
<body>
'''

def nav(propuesta):
    return f'''<header class="nav">
  <div class="contenedor nav__fila">
    <a class="logo" href="#" aria-label="Dental Díaz, inicio"><img src="assets/img/simbolo-marino.svg" alt=""><span>Dental Díaz</span></a>
    <ul class="nav__menu">
      <li><a class="tiene-sub" href="#tratamientos">Tratamientos {ic("chevron-down")}</a></li>
      <li><a href="#primera-visita">Tu primera visita</a></li>
      <li><a href="#clinica">La clínica</a></li>
      <li><a href="#">Nubo explica</a></li>
      <li><a href="#visitanos">Contacto</a></li>
    </ul>
    <div class="nav__acciones">
      <a class="icono-btn" href="{WA}" target="_blank" rel="noopener" aria-label="Escríbenos por WhatsApp">{ic("brand-whatsapp")}</a>
      <a class="btn btn--primario btn--chico" href="#agenda">Agenda tu valoración</a>
      <button class="icono-btn nav__hamburguesa" aria-label="Abrir menú" aria-expanded="false">{ic("menu-2")}</button>
    </div>
  </div>
  <nav class="menu-movil" aria-label="Menú">
    <a href="#tratamientos">Tratamientos</a>
    <a href="#primera-visita">Tu primera visita</a>
    <a href="#clinica">La clínica</a>
    <a href="#">Nubo explica</a>
    <a href="#visitanos">Contacto</a>
    <a class="btn btn--primario" href="#agenda">Agenda tu valoración</a>
  </nav>
</header>
<div class="propuesta-tag">Propuesta {propuesta}</div>
'''

def pie():
    return f'''<footer class="pie">
  <div class="contenedor">
    <div class="pie__grid">
      <div>
        <a class="logo" href="#" style="color: var(--marfil)"><img src="assets/img/simbolo-marino.svg" alt="" style="filter: brightness(0) invert(0.97) sepia(0.06)"><span>Dental Díaz</span></a>
        <p style="margin: 18px 0 0; font-size: .9375rem; opacity: .78; max-width: 32ch">Clínica dental familiar en Terán. Te explicamos todo antes de empezar.</p>
      </div>
      <div><h4>Tratamientos</h4><ul><li><a href="#">Blanqueamiento</a></li><li><a href="#">Ortodoncia</a></li><li><a href="#">Prótesis</a></li><li><a href="#">Odontopediatría</a></li><li><a href="#">Odontología general</a></li></ul></div>
      <div><h4>Visítanos</h4><ul><li>2da Norte Oriente #438, Terán</li><li>A un costado del parque de Terán</li><li><a href="{MAPS}" target="_blank" rel="noopener">Cómo llegar</a></li></ul></div>
      <div><h4>Horario</h4><ul><li class="tabular">Lun a vie, 10:00 a 14:00</li><li class="tabular">y 16:00 a 20:00</li><li class="tabular">Sábado, 10:00 a 14:00</li><li><a href="{WA}" target="_blank" rel="noopener">WhatsApp 961 138 5698</a></li></ul></div>
    </div>
    <div class="pie__legal">
      <span>Dra. María Concepción Díaz Márquez. Cédula profesional 15529125. UNISUR.</span>
      <span class="pie__cofepris">Aviso de publicidad COFEPRIS: pendiente</span>
      <span><a href="#">Aviso de privacidad</a></span>
    </div>
  </div>
</footer>
<div class="barra-movil">
  <a class="btn btn--primario" href="#agenda">Agenda tu valoración</a>
  <a class="btn btn--whatsapp" href="{WA}" target="_blank" rel="noopener" aria-label="WhatsApp">{ic("brand-whatsapp")}</a>
</div>
<script src="assets/js/iconos.js"></script>
<script src="assets/js/nubo-states.js"></script>
<script src="assets/js/nubo.js"></script>
<script src="assets/js/ui.js"></script>
<script src="assets/js/inicio.js"></script>
<script src="assets/js/agenda.js"></script>
</body>
</html>
'''

CSS_COMUN = '''.propuesta-tag { position: fixed; left: 16px; bottom: 16px; z-index: 70; padding: 6px 12px; border-radius: 999px; background: var(--marino); color: var(--marfil); font-family: var(--font-mono); font-size: 0.75rem; }
@media (max-width: 960px) { .propuesta-tag { bottom: auto; top: 72px; left: auto; right: 12px; } }
.h1-hero { font-size: clamp(2.6rem, 1.5rem + 4.4vw, 5rem); letter-spacing: -0.04em; line-height: 1.02; font-weight: 700; margin: 0; text-wrap: balance; }
.h1-hero .subrayado { z-index: 0; }
'''

TRATAMIENTOS = [
  ("blanq", "Blanqueamiento", "Dientes más blancos en 2 a 3 visitas", "Después de tu valoración, aclaramos tus dientes en 2 a 3 visitas y te damos indicaciones claras para cuidarlos.", [("calendar","2 a 3 visitas"),("clock","Dieta blanca de 48 a 72 h"),("file-text","Indicaciones por escrito")], "Sonrisa real de cerca, luz natural, sin retoque exagerado.", "celebra"),
  ("orto", "Ortodoncia", "Brackets metálicos, estéticos o autoligados", "Un plan claro desde el inicio y controles cada mes. Tú eliges el tipo de brackets con la doctora.", [("calendar","De 1 a 2 años"),("clock","Control cada mes"),("credit-card","Hasta 6 meses sin intereses*")], "Paciente con brackets sonriendo, perfil 3/4.", "explica"),
  ("protesis", "Prótesis", "Total o removible, en abonos", "Tu prótesis queda lista en 2 semanas a 1 mes. El costo se divide entre tus citas.", [("calendar","De 3 a 6 citas"),("clock","Lista en 2 semanas a 1 mes"),("receipt-2","Abonos por cita")], "La doctora mostrando un modelo al paciente.", "tranquilo"),
  ("ninos", "Odontopediatría", "Atendemos a los más pequeños", "Revisiones con calma, explicando todo a su ritmo para que la visita no dé miedo.", [("mood-kid","Para niños"),("heart-handshake","A su ritmo")], "Niño en el sillón con la doctora, ambos sonriendo. Con permiso de los papás.", "guina"),
  ("general", "Odontología general", "Limpieza, resinas y más", "Limpieza, resinas, extracciones, endodoncia y cirugía de tercer molar, en la misma clínica.", [("sparkles","Limpieza"),("dental","Resinas"),("dental","Endodoncia"),("stethoscope","Extracciones")], "Detalle del consultorio con luz encendida.", "explica"),
]

PASOS = [
  ("Revisión completa", "Revisamos toda tu boca, sin prisa y explicándote lo que vamos viendo.", "escucha"),
  ("Dos radiografías", "Radiografías periapicales digitales, incluidas en tu valoración.", "explica"),
  ("Diagnóstico", "Te enseñamos lo que encontramos en tus radiografías y te explicamos por qué.", "piensa"),
  ("Plan por escrito", "Tu plan con el precio. Si empiezas tu tratamiento aquí, se descuentan los $350.", "celebra"),
]

MIEDOS = [
  ("Me da miedo el dolor", "Antes de cada paso te explicamos qué vamos a hacer y vamos a tu ritmo. Puedes preguntar todo lo que quieras.", "empatico"),
  ("No sé cuánto me va a costar", "Lo sabes desde la valoración: tu plan va por escrito, con el precio. Hay meses sin intereses y abonos en prótesis.", "explica"),
  ("Que me vendan de más", "Te enseñamos tus radiografías y te explicamos qué necesitas y por qué. Tú decides qué hacer y cuándo.", "escucha"),
  ("Tuve una mala experiencia", "Cuéntanos qué pasó antes de empezar. Lo tomamos en cuenta y vamos con calma, sin regaños.", "empatico"),
]


INTERESES = ["Blanqueamiento", "Ortodoncia", "Prótesis", "Limpieza o revisión", "No estoy seguro"]
COMO = ["Instagram", "Facebook", "Google", "Me recomendaron", "Pasé por ahí", "Otro"]

def _chips(grupo, opciones):
    return '<div class="chips">' + "".join(f'<button type="button" class="chip" data-opcion="{grupo}" aria-pressed="false">{o}</button>' for o in opciones) + '</div>'

def agenda_html(pasos=False, sec_id="agenda"):
    b_interes = f'''<fieldset class="agenda-bloque" data-bloque="interes"><legend>¿Qué te interesa?</legend>{_chips("interes", INTERESES)}<span class="agenda-error">Elige una opción.</span></fieldset>'''
    b_para = f'''<fieldset class="agenda-bloque" data-bloque="para"><legend>¿Para quién es la cita?</legend>{_chips("para", ["Para mí", "Para un niño"])}<span class="agenda-error">Elige una opción.</span></fieldset>'''
    b_dia = '''<fieldset class="agenda-bloque" data-bloque="dia"><legend>Día y hora <span class="opcional">La valoración dura 45 min</span></legend><div class="agenda-dias" data-dias></div><div class="agenda-horas" data-horas></div><span class="agenda-error">Elige día y hora.</span></fieldset>'''
    b_datos = '''<div class="agenda-campos">
      <div class="campo"><label for="ag-nombre">Tu nombre</label><input id="ag-nombre" name="nombre" type="text" placeholder="Ana López" autocomplete="name"><span class="campo__ayuda">Como quieres que te llamemos.</span></div>
      <div class="campo"><label for="ag-wa">WhatsApp</label><input id="ag-wa" name="whatsapp" type="tel" inputmode="numeric" placeholder="961 123 4567" autocomplete="tel"><span class="campo__ayuda">Ahí te confirmamos tu cita.</span></div>
    </div>'''
    b_como = f'''<fieldset class="agenda-bloque" data-bloque="como"><legend>¿Cómo nos conociste?</legend>{_chips("como", COMO)}<span class="agenda-error">Elige una opción.</span></fieldset>'''
    nota = '<p class="nota-precio" style="margin:0">Valoración <strong>$350</strong>, se descuenta de tu tratamiento. Sin pago en línea.</p>'
    if pasos:
        cuerpo = f'''<div class="agenda-pasos" aria-hidden="true"><span class="activo" data-indicador><b>1</b> Tu cita</span><i></i><span data-indicador><b>2</b> Tus datos</span></div>
    <div class="agenda-paso" data-paso-agenda="1">{b_interes}{b_para}{b_dia}<div class="agenda-acciones"><button type="button" class="btn btn--primario" data-continuar>Continuar {ic("arrow-right","flecha")}</button></div></div>
    <div class="agenda-paso" data-paso-agenda="2" hidden><div class="agenda-resumen" data-resumen></div>{b_datos}{b_como}<div class="agenda-acciones"><button class="btn btn--primario" type="submit">Confirmar valoración {ic("arrow-right","flecha")}</button></div>{nota}</div>'''
    else:
        cuerpo = f'''{b_interes}{b_para}{b_dia}{b_datos}{b_como}<div class="agenda-acciones"><button class="btn btn--primario" type="submit">Confirmar valoración {ic("arrow-right","flecha")}</button></div>{nota}'''
    return f'''<section class="seccion agenda-sec" id="{sec_id}" style="padding-top: 0">
  <div class="contenedor">
    <div class="agenda-caja revela" data-agenda>
      <div class="agenda-lado">
        <div style="display:grid; gap: 16px">
          <h2 class="h2">Agenda tu valoración</h2>
          <p>Elige día y hora. Te confirmamos por WhatsApp.</p>
          <ul class="agenda-incluye"><li>{ic("check")} Revisión completa</li><li>{ic("check")} Dos radiografías periapicales</li><li>{ic("check")} Diagnóstico y plan por escrito</li></ul>
        </div>
        <div class="nubo" data-nubo="escucha" data-mirada aria-label="Nubo"></div>
      </div>
      <div class="agenda-form">
        <form novalidate>{cuerpo}</form>
        <div class="agenda-ok" aria-live="polite">
          <div class="nubo" data-nubo="celebra" aria-label="Nubo celebrando"></div>
          <h3 class="h3" style="margin:0">Listo, <span data-ok-nombre></span>. Tu valoración quedó apartada</h3>
          <ul class="agenda-ok__ficha" data-ok-ficha></ul>
          <a class="btn btn--whatsapp" data-ok-wa href="#" target="_blank" rel="noopener">{ic("brand-whatsapp")} Confirmar por WhatsApp</a>
          <button type="button" class="enlace" data-otra style="border:0; background-color: transparent; cursor:pointer">Agendar otra cita</button>
        </div>
      </div>
    </div>
  </div>
</section>'''
