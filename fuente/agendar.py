from comun import *

CSS_AG = CSS_COMUN + '''
.migas { display: flex; gap: 8px; align-items: center; font-size: 0.875rem; color: var(--texto-suave); }
.migas a { text-decoration: none; }
.migas a:hover { color: var(--marino); }
.ag-hero { padding-block: clamp(32px, 5vw, 64px) clamp(28px, 4vw, 48px); }
.ag-hero__grid { display: grid; gap: 0; }
.ag-hero h1 { margin: 16px 0 0; font-size: clamp(2.4rem, 1.6rem + 3vw, 4rem); letter-spacing: -0.04em; line-height: 1.02; font-weight: 700; }
.ag-hero .lead { margin-top: 18px; max-width: 46ch; }
.ag-datos { display: flex; flex-wrap: wrap; gap: 10px; margin-top: 26px; }
.ag-dato { display: flex; align-items: center; gap: 12px; padding: 12px 18px 12px 14px; border-radius: var(--r-md); background: var(--marfil); border: 1px solid var(--linea); }
.ag-dato .i { width: 22px; height: 22px; color: var(--lavanda-sombra); }
.ag-dato strong { display: block; font-size: 0.9875rem; }
.ag-dato small { color: var(--texto-suave); font-size: 0.8125rem; }
@media (max-width: 700px) { .ag-datos { display: grid; } }

.antes { display: grid; grid-template-columns: 1.3fr 1fr 1fr; gap: 16px; }
.antes > div { padding: clamp(22px, 3vw, 32px); border-radius: var(--r-lg); background: var(--marfil); border: 1px solid var(--linea); display: grid; gap: 14px; align-content: start; }
.antes > div:first-child { background: var(--marino); color: var(--marfil); border-color: var(--marino); }
.antes > div:first-child .texto { color: rgba(250, 248, 243, 0.78); }
.antes ul { list-style: none; margin: 0; padding: 0; display: grid; gap: 10px; }
.antes li { display: flex; gap: 10px; align-items: flex-start; font-size: 0.9875rem; line-height: 1.45; }
.antes li .i { width: 20px; height: 20px; flex: none; margin-top: 2px; color: var(--lavanda-sombra); }
.antes > div:first-child li .i { color: var(--lavanda); }
.por-confirmar { font-family: var(--font-mono); font-size: 0.6875rem; padding: 2px 8px; border-radius: 999px; background: rgba(163, 175, 209, 0.35); color: var(--marino); white-space: nowrap; }
@media (max-width: 900px) { .antes { grid-template-columns: 1fr; } }

.ag-faq { display: grid; grid-template-columns: 0.8fr 1.2fr; gap: clamp(28px, 5vw, 72px); align-items: start; }
.ag-faq__lado { display: grid; gap: 16px; justify-items: start; position: sticky; top: 110px; }
.ag-faq__lado .nubo { width: 200px; }
@media (max-width: 900px) { .ag-faq { grid-template-columns: 1fr; } .ag-faq__lado { position: static; } .ag-faq__lado .nubo { width: 130px; } }

.ag-lugar { display: grid; grid-template-columns: 0.9fr 1.1fr; gap: 16px; }
.ag-lugar__info { padding: clamp(24px, 3vw, 36px); border-radius: var(--r-lg); background: var(--marfil); border: 1px solid var(--linea); display: grid; gap: 18px; align-content: start; }
.ag-lugar .mapa { min-height: 360px; }
@media (max-width: 900px) { .ag-lugar { grid-template-columns: 1fr; } .ag-lugar .mapa { min-height: 280px; } }

.chat { min-height: calc(100svh - 76px); display: grid; grid-template-columns: 1fr 340px; gap: clamp(20px, 3vw, 40px); padding-block: clamp(20px, 3vw, 40px); align-items: stretch; }
.chat__escena { position: relative; display: grid; grid-template-rows: auto 1fr; border-radius: var(--r-xl); background: var(--marfil); border: 1px solid var(--linea); overflow: hidden; }
.chat__top { display: flex; align-items: center; gap: 14px; padding: 18px 22px; border-bottom: 1px solid var(--linea); }
.chat__top .mini-titulo { margin-right: auto; font-weight: 600; font-size: 0.9375rem; }
.chat__riel { position: absolute; left: 0; right: 0; top: 0; height: 4px; background: var(--niebla); }
.chat__barra { display: block; height: 100%; background: var(--marino); transform-origin: left; transform: scaleX(0.14); transition: transform 600ms var(--ease-out); }
.chat__contador { font-family: var(--font-mono); font-size: 0.8125rem; color: var(--texto-suave); }
.chat__cuerpo { display: grid; grid-template-columns: 220px 1fr; gap: clamp(16px, 3vw, 40px); padding: clamp(24px, 4vw, 56px); align-content: center; }
.chat__nubo { align-self: start; }
.chat__nubo .nubo { width: 220px; }
.chat__pregunta { margin: 0 0 28px; padding: 22px 26px; border-radius: 26px 26px 26px 6px; background: var(--lavanda); color: var(--marino); font-size: clamp(1.35rem, 1.1rem + 1vw, 2rem); font-weight: 700; letter-spacing: -0.025em; line-height: 1.2; max-width: 26ch; }
.chat__pregunta.entra { animation: burbuja-entra 520ms var(--ease-rebote) both; }
.chat__area.entra { animation: texto-entra 520ms var(--ease-out) 120ms both; }
.chat-opciones { display: flex; flex-wrap: wrap; gap: 10px; }
.chat-op { min-height: 56px; padding: 0 24px; border-radius: var(--r-pill); border: 1.5px solid var(--linea-fuerte); background: var(--crema); color: var(--texto); font-size: 1.05rem; font-weight: 600; cursor: pointer; transition: transform var(--dur-base) var(--ease-rebote), background var(--dur-rapida), color var(--dur-rapida), border-color var(--dur-rapida); }
.chat-op:hover { border-color: var(--marino); transform: translateY(-2px); }
.chat-op[aria-pressed="true"] { background: var(--marino); border-color: var(--marino); color: var(--marfil); }
.chat-op:disabled { opacity: 0.38; cursor: not-allowed; text-decoration: line-through; transform: none; }
.chat-op--hora { font-family: var(--font-mono); font-size: 0.9375rem; min-width: 90px; }
.chat-dias { display: flex; flex-wrap: wrap; gap: 10px; }
.chat-dias .dia { width: 84px; padding: 14px 0; }
.chat-campos { display: grid; gap: 16px; max-width: 460px; }
.chat-campos .btn { justify-self: start; }
.chat-final { display: flex; flex-wrap: wrap; gap: 12px; }
.chat__atras { display: inline-flex; align-items: center; gap: 6px; border: 0; background: none; cursor: pointer; font-weight: 600; font-size: 0.9375rem; color: var(--texto-suave); padding: 6px 0; }
.chat__atras:hover { color: var(--marino); }
.chat__atras[hidden] { display: none; }
.chat__atras .i { transform: scaleX(-1); }
.chat__lado { display: grid; gap: 14px; align-content: start; }
.tu-cita { padding: 22px; border-radius: var(--r-lg); background: var(--marfil); border: 1px solid var(--linea); display: grid; gap: 16px; transition: box-shadow var(--dur-base), border-color var(--dur-base); }
.tu-cita__cab { display: flex; justify-content: space-between; align-items: start; gap: 12px; }
.tu-cita h2 { margin: 0; font-size: 1.2rem; letter-spacing: -0.02em; }
.tu-cita__cab p { margin: 2px 0 0; font-size: 0.875rem; color: var(--texto-suave); }
.tu-cita__estado { font-size: 0.75rem; font-weight: 600; padding: 4px 10px; border-radius: 999px; background: var(--crema); color: var(--texto-suave); white-space: nowrap; }
.tu-cita ul { list-style: none; margin: 0; padding: 0; display: grid; gap: 4px; }
.tu-cita li { display: grid; grid-template-columns: 32px auto 1fr; gap: 10px; align-items: center; padding: 8px 0; font-size: 0.9375rem; border-bottom: 1px solid var(--linea); }
.tu-cita li:last-child { border-bottom: 0; }
.tu-cita li > span:nth-child(2) { color: var(--texto-suave); }
.tu-cita li strong { text-align: right; font-weight: 600; color: #A0A5B5; font-weight: 500; }
.tu-cita li.lleno strong { color: var(--marino); font-weight: 600; animation: texto-entra 400ms var(--ease-out) both; }
.tu-cita__ic { width: 32px; height: 32px; border-radius: 10px; display: grid; place-items: center; background: var(--crema); color: var(--lavanda-sombra); }
.tu-cita__ic .i { width: 17px; height: 17px; }
.tu-cita li.lleno .tu-cita__ic { background: var(--marino); color: var(--marfil); animation: pop 420ms var(--ease-rebote) both; }
@keyframes pop { from { transform: scale(0.6); } to { transform: none; } }
.chat.confirmado .tu-cita { border-color: var(--marino); box-shadow: 0 0 0 3px var(--lavanda); }
.chat.confirmado .tu-cita__estado { background: var(--marino); color: var(--marfil); }

.conv { display: grid; grid-template-columns: minmax(0, 1fr) 320px; gap: clamp(20px, 3vw, 40px); align-items: start; }
.conv__ventana { display: grid; grid-template-rows: auto 1fr auto; height: min(700px, calc(100svh - 120px)); border-radius: var(--r-xl); background: var(--marfil); border: 1px solid var(--linea); overflow: hidden; box-shadow: var(--sombra-suave); }
.conv__cab { display: flex; align-items: center; gap: 12px; padding: 12px 18px; border-bottom: 1px solid var(--linea); background: var(--marfil); }
.conv__avatar { width: 46px; height: 46px; border-radius: 50%; background: var(--crema); border: 1px solid var(--linea); display: grid; place-items: end center; overflow: hidden; flex: none; }
.conv__avatar .nubo { width: 42px; margin-bottom: -10px; }
.conv__cab strong { display: block; font-size: 1rem; }
.conv__cab small { font-size: 0.8125rem; color: var(--ok); }
.conv__cab [data-conv-contador] { margin-left: auto; font-family: var(--font-mono); font-size: 0.8125rem; color: var(--texto-suave); }
.conv__hilo { overflow-y: auto; padding: 22px clamp(14px, 3vw, 28px); display: flex; flex-direction: column; gap: 8px; background: radial-gradient(circle at 1px 1px, rgba(48, 59, 91, 0.06) 1px, transparent 0) 0 0 / 18px 18px, var(--crema); scroll-behavior: smooth; }
.msg { flex-shrink: 0; max-width: min(78%, 460px); padding: 11px 15px; border-radius: 18px; font-size: 1rem; line-height: 1.45; animation: msg-entra 360ms var(--ease-rebote) both; }
.msg--nubo { align-self: flex-start; background: var(--marfil); color: var(--texto); border-bottom-left-radius: 6px; box-shadow: 0 1px 2px rgba(48, 59, 91, 0.08); }
.msg--yo { align-self: flex-end; background: var(--marino); color: var(--marfil); border-bottom-right-radius: 6px; display: grid; justify-items: end; gap: 2px; transform-origin: right bottom; }
.msg__cambiar { border: 0; background: none; padding: 0; font: inherit; font-size: 0.75rem; color: var(--lavanda); cursor: pointer; text-decoration: underline; text-underline-offset: 2px; }
.msg--escribe { display: flex; gap: 5px; padding: 15px 16px; }
.msg--escribe i { width: 7px; height: 7px; border-radius: 50%; background: var(--lavanda-sombra); animation: punto 1s infinite ease-in-out; }
.msg--escribe i:nth-child(2) { animation-delay: 0.15s; } .msg--escribe i:nth-child(3) { animation-delay: 0.3s; }
@keyframes punto { 0%, 60%, 100% { transform: translateY(0); opacity: 0.5; } 30% { transform: translateY(-4px); opacity: 1; } }
@keyframes msg-entra { from { opacity: 0; transform: translateY(10px) scale(0.96); } to { opacity: 1; transform: none; } }
.msg--tarjeta { padding: 0; overflow: hidden; width: min(78%, 380px); }
.conv-resumen__cab { display: flex; justify-content: space-between; padding: 14px 16px; background: var(--marino); color: var(--marfil); font-size: 0.95rem; }
.conv-resumen__cab span { font-family: var(--font-mono); font-size: 0.8125rem; color: var(--lavanda); }
.conv-resumen ul { list-style: none; margin: 0; padding: 6px 16px 10px; }
.conv-resumen li { display: flex; justify-content: space-between; gap: 12px; padding: 7px 0; border-bottom: 1px solid var(--linea); font-size: 0.9rem; }
.conv-resumen li:last-child { border-bottom: 0; }
.conv-resumen li span { color: var(--texto-suave); }
.conv-resumen li strong { text-align: right; }
.conv__entrada { padding: 14px clamp(14px, 3vw, 22px) 16px; border-top: 1px solid var(--linea); background: var(--marfil); min-height: 76px; display: grid; align-content: center; }
.conv__entrada.lista > * { animation: texto-entra 380ms var(--ease-out) both; }
.conv-ops { display: flex; flex-wrap: wrap; gap: 8px; }
.conv .chat-op { min-height: 46px; padding: 0 18px; font-size: 0.975rem; }
.conv-dias { display: flex; gap: 8px; overflow-x: auto; scrollbar-width: none; }
.conv-dias .dia { flex: none; width: 70px; padding: 10px 0; }
.conv-horas { display: grid; gap: 10px; }
.conv-horas__g { display: grid; gap: 6px; }
.conv-horas__g > span { font-size: 0.8125rem; font-weight: 600; color: var(--texto-suave); }
.conv .chat-op--hora { min-width: 78px; padding: 0 12px; }
.conv-campos { display: grid; grid-template-columns: 1fr 1fr auto; gap: 10px; align-items: end; }
.conv-campos .campo input { height: 50px; }
.conv-enviar { width: 50px; height: 50px; min-height: 50px; padding: 0; border-radius: 50%; }
.conv-error { font-size: 0.8125rem; color: var(--error); font-weight: 600; }
.conv-error:empty { display: none; }
.conv-final { display: flex; flex-wrap: wrap; gap: 10px; }
.conv__lado { display: grid; gap: 14px; position: sticky; top: 100px; }
.conv__lado .nubo { width: 200px; justify-self: center; }
@media (max-width: 1000px) {
  .conv { grid-template-columns: 1fr; }
  .conv__lado { position: static; }
  .conv__lado .nubo { display: none; }
  .conv__ventana { height: calc(100svh - 96px); border-radius: var(--r-lg); }
  .conv-campos { grid-template-columns: 1fr auto; }
  .conv-campos .campo:first-child { grid-column: 1 / -1; }
  .msg { max-width: 86%; }
}
.mini-info { padding: 20px; border-radius: var(--r-lg); background: var(--marfil); border: 1px solid var(--linea); display: grid; gap: 10px; font-size: 0.9375rem; }
.mini-info li { display: flex; gap: 10px; }
.mini-info ul { list-style: none; margin: 0; padding: 0; display: grid; gap: 8px; }
.mini-info .i { width: 20px; height: 20px; color: var(--lavanda-sombra); flex: none; }
@keyframes texto-entra { from { opacity: 0; transform: translateY(14px); } to { opacity: 1; transform: none; } }
@media (max-width: 1000px) {
  .chat { grid-template-columns: 1fr; min-height: 0; }
  .chat__cuerpo { grid-template-columns: 1fr; padding: 22px; }
  .chat__nubo { display: flex; align-items: flex-end; gap: 12px; }
  .chat__nubo .nubo { width: 96px; }
  .chat__pregunta { font-size: 1.3rem; margin-bottom: 20px; }
  .chat-op { min-height: 50px; padding: 0 18px; font-size: 1rem; }
  .chat-dias { flex-wrap: nowrap; overflow-x: auto; scrollbar-width: none; margin-inline: -22px; padding-inline: 22px; }
  .chat-dias .dia { flex: none; width: 74px; }
}
'''

FAQ_AG = [
    ("¿La valoración tiene costo?", "Sí, $350. Incluye revisión completa, dos radiografías periapicales, diagnóstico y tu plan de tratamiento por escrito. Si empiezas tu tratamiento con nosotros, se descuenta del total."),
    ("¿Cuánto dura?", "45 minutos."),
    ("¿Cómo pago la valoración?", "En la clínica, el día de tu cita. No hay pago en línea."),
    ("¿Puedo cambiar mi cita?", "Sí. Escríbenos por WhatsApp al 961 138 5698 y te damos otro horario."),
    ("¿Atienden niños?", "Sí. Al agendar, elige \"Para un niño\" y le damos el tiempo que necesite."),
]

def faq():
    return '<div class="faq">' + "".join(
        f'<div class="faq__item{" abierto" if i == 0 else ""}"><button class="faq__pregunta" aria-expanded="{"true" if i == 0 else "false"}">{q}<span class="faq__mas">{ic("plus")}</span></button><div class="faq__respuesta"><div><p>{a}</p></div></div></div>'
        for i, (q, a) in enumerate(FAQ_AG)) + '</div>'

lugar = f'''<section class="seccion" style="padding-top: 0"><div class="contenedor">
<div class="titular revela"><h2 class="h2">Aquí te esperamos</h2></div>
<div class="ag-lugar">
  <div class="ag-lugar__info revela">
    <span class="estado-abierto" data-abierto>Horario</span>
    <ul class="horario tabular"><li><span>Lunes a viernes</span><span>10:00 a 14:00 y 16:00 a 20:00</span></li><li><span>Sábado</span><span>10:00 a 14:00</span></li><li><span>Domingo</span><span>Cerrado</span></li></ul>
    <p class="texto">2da Norte Oriente #438, Terán. A un costado del parque de Terán, Tuxtla Gutiérrez.</p>
    <div style="display:flex; flex-wrap: wrap; gap: 10px"><a class="btn btn--primario btn--chico" href="{MAPS}" target="_blank" rel="noopener">{ic("navigation")} Cómo llegar</a><a class="btn btn--secundario btn--chico" href="{WA}" target="_blank" rel="noopener">{ic("brand-whatsapp")} Escríbenos</a></div>
  </div>
  <div class="mapa revela"><iframe src="{MAPA_EMBED}" loading="lazy" title="Mapa de Dental Díaz en Terán" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
</div></div></section>'''

HERO = f'''
<section class="ag-hero"><div class="contenedor ag-hero__grid">
  <nav class="migas" aria-label="Ruta"><a href="index.html">Inicio</a><span aria-hidden="true">/</span><span aria-current="page">Agendar</span></nav>
  <h1 data-palabras>Agenda tu valoración</h1>
  <p class="lead">45 minutos con la doctora. Revisamos con calma, tomamos dos radiografías y te llevas tu plan por escrito.</p>
  <div class="ag-datos">
    <div class="ag-dato">{ic("clock")}<div><strong>45 minutos</strong><small>Con la Dra. Díaz</small></div></div>
    <div class="ag-dato">{ic("receipt-2")}<div><strong>$350</strong><small>Se descuenta de tu tratamiento</small></div></div>
    <div class="ag-dato">{ic("brand-whatsapp")}<div><strong>Confirmación por WhatsApp</strong><small>Sin pago en línea</small></div></div>
  </div>
</div></section>'''

INFO = f'''
<section class="seccion"><div class="contenedor">
  <div class="titular revela"><h2 class="h2">Antes de tu cita</h2></div>
  <div class="antes" data-escalonar>
    <div class="revela"><h3 class="h3" style="margin:0">Qué incluye</h3><ul><li>{ic("check")} Revisión completa de tu boca</li><li>{ic("check")} Dos radiografías periapicales digitales</li><li>{ic("check")} Diagnóstico explicado con tus radiografías</li><li>{ic("check")} Plan de tratamiento con precio, por escrito</li></ul></div>
    <div class="revela"><h3 class="h3" style="margin:0">Qué traer</h3><ul><li>{ic("file-text")} Radiografías o estudios anteriores, si tienes</li><li>{ic("mood-smile")} Tus dudas: anótalas para preguntarle a la doctora</li></ul><span class="por-confirmar">Por confirmar con la clínica</span></div>
    <div class="revela"><h3 class="h3" style="margin:0">Cómo pagar</h3><ul><li>{ic("receipt-2")} La valoración se paga en la clínica</li><li>{ic("credit-card")} Hasta 6 meses sin intereses en tratamientos mayores a $6,000</li><li>{ic("calendar")} Prótesis en abonos por cita</li></ul></div>
  </div>
</div></section>
<section class="seccion" style="padding-top: 0"><div class="contenedor ag-faq">
  <div class="ag-faq__lado revela"><div class="nubo" data-nubo="piensa" data-mirada aria-label="Nubo"></div><h2 class="h2">Dudas sobre tu cita</h2><a class="btn btn--whatsapp btn--chico" href="{WA}" target="_blank" rel="noopener">{ic("brand-whatsapp")} Pregúntanos</a></div>
  <div class="revela">{faq()}</div>
</div></section>
{lugar}
'''

INCLUYE = f'''<div class="mini-info"><strong>Incluye</strong><ul><li>{ic("check")} Revisión completa</li><li>{ic("check")} Dos radiografías periapicales</li><li>{ic("check")} Plan por escrito, con precio</li></ul></div>
    <div class="mini-info"><span class="estado-abierto" data-abierto>Horario</span><span class="texto chico">2da Norte Oriente #438, Terán</span><a class="enlace" href="{MAPS}" target="_blank" rel="noopener">{ic("navigation")} Cómo llegar</a></div>'''

# ---------- Propuesta A: Nubo pregunta, la tarjeta se llena ----------
cuerpo_a = HERO + f'''
<section class="contenedor chat" id="agenda" data-chat-agenda style="min-height: 0; padding-top: 0; scroll-margin-top: 90px">
  <div class="chat__escena">
    <div class="chat__riel"><span class="chat__barra" data-chat-barra></span></div>
    <div class="chat__top">
      <span class="mini-titulo">Te hago 6 preguntas rápidas</span>
      <span class="chat__contador" data-chat-contador>Paso 1 de 6</span>
    </div>
    <div class="chat__cuerpo">
      <div class="chat__nubo"><div class="nubo" data-nubo="saluda" data-chat-nubo data-mirada data-saluda aria-label="Nubo"></div></div>
      <div>
        <h2 class="chat__pregunta" data-chat-pregunta aria-live="polite">Hola, soy Nubo. ¿Qué te gustaría revisar?</h2>
        <div class="chat__area" data-chat-area></div>
        <button type="button" class="chat__atras" data-chat-atras hidden>{ic("arrow-right")} Atrás</button>
      </div>
    </div>
  </div>
  <aside class="chat__lado">
    <div class="tu-cita"><div class="tu-cita__cab"><div><h2>Tu cita</h2><p>Valoración · 45 minutos · $350</p></div><span class="tu-cita__estado" data-cita-estado>En proceso</span></div><ul data-chat-ticket></ul></div>
    {INCLUYE}
  </aside>
</section>
''' + INFO

# ---------- Propuesta B: conversación tipo WhatsApp ----------
cuerpo_b = HERO + f'''
<section class="contenedor conv" id="agenda" data-conv style="scroll-margin-top: 84px">
  <div class="conv__ventana">
    <header class="conv__cab"><span class="conv__avatar"><span class="nubo" data-nubo="tranquilo" aria-hidden="true"></span></span><div><strong>Nubo · Dental Díaz</strong><small>En línea</small></div><span data-conv-contador>Paso 1 de 6</span></header>
    <div class="conv__hilo" data-hilo aria-live="polite"></div>
    <div class="conv__entrada" data-entrada></div>
  </div>
  <aside class="conv__lado"><div class="nubo" data-nubo="saluda" data-conv-nubo data-mirada aria-label="Nubo"></div>{INCLUYE}</aside>
</section>
''' + INFO

def armar(tag, cuerpo, archivo, extra=""):
    html = cabeza("Agenda tu valoración · Dental Díaz", CSS_AG) + nav(tag).replace('<div class="propuesta-tag">Propuesta ' + tag + '</div>', '') + "<main>" + cuerpo + "</main>\n" + pie()
    html = html.replace('href="#agenda">Agenda tu valoración', 'href="#agenda" aria-current="page">Agenda tu valoración')
    extra = '<style>@media (max-width: 960px) { .barra-movil { display: none !important; } body { padding-bottom: 0 !important; } }</style>' + extra
    html = html.replace("</body>", extra + "\n</body>")
    open(archivo, "w").write(html)
    print("ok", archivo, len(html))

armar("Agendar", cuerpo_a, "../agendar.html", '<script src="assets/js/agenda-chat.js"></script>')
