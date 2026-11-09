from comun import *

CSS_AG = CSS_COMUN + '''
.migas { display: flex; gap: 8px; align-items: center; font-size: 0.875rem; color: var(--texto-suave); }
.migas a { text-decoration: none; }
.migas a:hover { color: var(--marino); }
.ag-hero { padding-block: clamp(32px, 5vw, 64px) clamp(28px, 4vw, 48px); }
.ag-hero__grid { display: grid; grid-template-columns: 1.2fr 0.8fr; gap: 32px; align-items: end; }
.ag-hero h1 { margin: 16px 0 0; font-size: clamp(2.4rem, 1.6rem + 3vw, 4rem); letter-spacing: -0.04em; line-height: 1.02; font-weight: 700; }
.ag-hero .lead { margin-top: 18px; max-width: 46ch; }
.ag-datos { display: grid; gap: 10px; }
.ag-dato { display: flex; align-items: center; gap: 14px; padding: 14px 18px; border-radius: var(--r-md); background: var(--marfil); border: 1px solid var(--linea); }
.ag-dato .i { width: 22px; height: 22px; color: var(--lavanda-sombra); }
.ag-dato strong { display: block; font-size: 0.9875rem; }
.ag-dato small { color: var(--texto-suave); font-size: 0.8125rem; }
@media (max-width: 900px) { .ag-hero__grid { grid-template-columns: 1fr; } }

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
.chat__top .migas { margin-right: auto; }
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
.ticket { position: relative; padding: 24px; border-radius: var(--r-lg); background: var(--marino); color: var(--marfil); }
.ticket::before, .ticket::after { content: ""; position: absolute; top: 92px; width: 22px; height: 22px; border-radius: 50%; background: var(--crema); }
.ticket::before { left: -11px; } .ticket::after { right: -11px; }
.ticket h2 { margin: 0 0 6px; font-size: 1.15rem; letter-spacing: -0.015em; }
.ticket > p { margin: 0 0 22px; font-size: 0.875rem; color: rgba(250, 248, 243, 0.7); }
.ticket ul { list-style: none; margin: 0; padding: 18px 0 0; border-top: 2px dashed rgba(250, 248, 243, 0.25); display: grid; gap: 12px; }
.ticket li { display: flex; justify-content: space-between; gap: 12px; font-size: 0.9375rem; }
.ticket li span { color: rgba(250, 248, 243, 0.6); }
.ticket li strong { color: rgba(250, 248, 243, 0.35); font-weight: 600; text-align: right; }
.ticket li.lleno strong { color: var(--marfil); animation: texto-entra 400ms var(--ease-out) both; }
.chat.confirmado .ticket { box-shadow: 0 0 0 4px var(--lavanda); }
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
  .ticket::before, .ticket::after { display: none; }
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

# ---------- Propuesta A: página directa ----------
form = agenda_html(pasos=True).replace('<h2 class="h2">Agenda tu valoración</h2>', '<h2 class="h2">Elige tu horario</h2>', 1)
cuerpo_a = f'''
<section class="ag-hero"><div class="contenedor ag-hero__grid">
  <div>
    <nav class="migas" aria-label="Ruta"><a href="index.html">Inicio</a><span aria-hidden="true">/</span><span aria-current="page">Agendar</span></nav>
    <h1 data-palabras>Agenda tu valoración</h1>
    <p class="lead">45 minutos con la doctora. Revisamos con calma, tomamos dos radiografías y te llevas tu plan por escrito.</p>
  </div>
  <div class="ag-datos revela" data-escalonar>
    <div class="ag-dato">{ic("clock")}<div><strong>45 minutos</strong><small>Con la Dra. Díaz</small></div></div>
    <div class="ag-dato">{ic("receipt-2")}<div><strong>$350</strong><small>Se descuenta de tu tratamiento</small></div></div>
    <div class="ag-dato">{ic("brand-whatsapp")}<div><strong>Confirmación por WhatsApp</strong><small>Sin pago en línea</small></div></div>
  </div>
</div></section>
{form}
<section class="seccion" style="padding-top: 0"><div class="contenedor">
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

# ---------- Propuesta B: conversación con Nubo ----------
cuerpo_b = f'''
<section class="contenedor chat" data-chat-agenda>
  <div class="chat__escena">
    <div class="chat__riel"><span class="chat__barra" data-chat-barra></span></div>
    <div class="chat__top">
      <nav class="migas" aria-label="Ruta"><a href="index.html">Inicio</a><span aria-hidden="true">/</span><span aria-current="page">Agendar</span></nav>
      <span class="chat__contador" data-chat-contador>Paso 1 de 6</span>
    </div>
    <div class="chat__cuerpo">
      <div class="chat__nubo"><div class="nubo" data-nubo="saluda" data-chat-nubo data-mirada data-saluda aria-label="Nubo"></div></div>
      <div>
        <h1 class="chat__pregunta" data-chat-pregunta aria-live="polite">Hola, soy Nubo. ¿Qué te gustaría revisar?</h1>
        <div class="chat__area" data-chat-area></div>
        <button type="button" class="chat__atras" data-chat-atras hidden>{ic("arrow-right")} Atrás</button>
      </div>
    </div>
  </div>
  <aside class="chat__lado">
    <div class="ticket"><h2>Tu valoración</h2><p>Dental Díaz · 45 minutos · $350</p><ul data-chat-ticket></ul></div>
    <div class="mini-info"><strong>Incluye</strong><ul><li>{ic("check")} Revisión completa</li><li>{ic("check")} Dos radiografías periapicales</li><li>{ic("check")} Plan por escrito, con precio</li></ul></div>
    <div class="mini-info"><span class="estado-abierto" data-abierto>Horario</span><span class="texto chico">2da Norte Oriente #438, Terán</span><a class="enlace" href="{MAPS}" target="_blank" rel="noopener">{ic("navigation")} Cómo llegar</a></div>
  </aside>
</section>
<section class="seccion" style="padding-top: clamp(32px, 5vw, 64px)"><div class="contenedor ag-faq">
  <div class="ag-faq__lado revela"><h2 class="h2">Dudas sobre tu cita</h2><a class="btn btn--whatsapp btn--chico" href="{WA}" target="_blank" rel="noopener">{ic("brand-whatsapp")} Pregúntanos</a></div>
  <div class="revela">{faq()}</div>
</div></section>
'''

def armar(tag, cuerpo, archivo, extra=""):
    html = cabeza(f"Agenda tu valoración · Dental Díaz · {tag}", CSS_AG) + nav(tag) + "<main>" + cuerpo + "</main>\n" + pie()
    html = html.replace('href="#agenda">Agenda tu valoración', 'href="#agenda" aria-current="page">Agenda tu valoración')
    if extra:
        html = html.replace("</body>", extra + "\n</body>")
    open(archivo, "w").write(html)
    print("ok", archivo, len(html))

armar("Agendar A · Directa", cuerpo_a, "../agendar-a.html")
armar("Agendar B · Con Nubo", cuerpo_b, "../agendar-b.html", '<style>@media (max-width: 960px) { .barra-movil { display: none !important; } body { padding-bottom: 0 !important; } }</style><script src="assets/js/agenda-chat.js"></script><script>document.querySelectorAll(\'a[href="#agenda"]\').forEach(function(a){a.setAttribute("href","#")});</script>')
