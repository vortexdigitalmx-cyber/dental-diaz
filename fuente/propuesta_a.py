from comun import *

CSS = CSS_COMUN + '''
.hero-a { padding-block: clamp(40px, 6vw, 88px) clamp(56px, 7vw, 96px); }
.hero-a__grid { display: grid; grid-template-columns: 1.1fr 0.9fr; gap: clamp(32px, 5vw, 80px); align-items: center; }
.hero-a__tx { display: grid; gap: 26px; }
.hero-a__tx .lead { max-width: 34ch; }
.hero-a__acciones { display: flex; flex-wrap: wrap; gap: 12px; }
.hero-a__media { position: relative; display: grid; }
.hero-a__media .foto { aspect-ratio: 4 / 5; border-radius: var(--r-xl); position: relative; z-index: 1; }
.hero-a__nubo { position: relative; width: 44%; margin-left: 8%; margin-bottom: -14px; z-index: 0; }
.hero-a__nubo .nubo-asoma { animation-name: asoma-arriba; }
@keyframes asoma-arriba { from { transform: translateY(80%); } to { transform: translateY(0); } }
.hero-a .chip-flota.uno { left: -28px; bottom: 56px; animation-delay: 700ms; }
.hero-a .chip-flota.dos { right: -18px; top: 38%; animation-delay: 900ms; }
@media (max-width: 900px) {
  .hero-a__grid { grid-template-columns: 1fr; }
  .hero-a__media { max-width: 460px; width: 100%; margin-inline: auto; }
  .hero-a__nubo { width: 50%; }
  .hero-a__media .foto { aspect-ratio: 4 / 4.4; }
  .hero-a .chip-flota.uno { left: -6px; bottom: 20px; }
  .hero-a .chip-flota.dos { right: -6px; top: 40%; }
}

.trat-a { display: grid; grid-template-columns: 0.85fr 1.15fr; gap: clamp(24px, 4vw, 56px); align-items: start; }
.trat-a__panel { gap: 22px; padding: 14px; border-radius: var(--r-xl); background: var(--marfil); border: 1px solid var(--linea); }
.trat-a__panel .foto { aspect-ratio: 16 / 10; border-radius: calc(var(--r-xl) - 10px); }
.trat-a__panel-tx { padding: 6px 14px 16px; display: grid; gap: 14px; }
@media (max-width: 900px) {
  .trat-a { grid-template-columns: 1fr; }
  .trat-a .selector-tx__lista { display: flex; overflow-x: auto; scroll-snap-type: x mandatory; gap: 8px; margin-inline: calc(var(--gutter) * -1); padding-inline: var(--gutter); scrollbar-width: none; }
  .trat-a .selector-tx__lista::-webkit-scrollbar { display: none; }
  .trat-a .selector-tx__tab { flex: none; width: auto; scroll-snap-align: start; padding: 12px 18px; border-color: var(--linea-fuerte); border-radius: var(--r-pill); }
  .trat-a .selector-tx__tab strong { font-size: 1rem; }
  .trat-a .selector-tx__tab small, .trat-a .selector-tx__tab .i { display: none; }
}

.visita-a { border-radius: var(--r-xl); background: var(--marino); color: var(--marfil); padding: clamp(28px, 5vw, 72px); display: grid; grid-template-columns: 0.8fr 1.2fr; gap: clamp(28px, 5vw, 72px); align-items: center; }
.visita-a .h2 { max-width: 14ch; }
.visita-a__escena { position: relative; display: grid; place-items: center; aspect-ratio: 1; border-radius: 50%; background: rgba(163, 175, 209, 0.16); }
.visita-a__escena .nubo { width: 78%; }
.visita-a__precio { display: inline-flex; align-items: baseline; gap: 10px; margin-top: 8px; padding: 10px 16px; border-radius: var(--r-pill); background: rgba(250, 248, 243, 0.1); font-size: 0.9375rem; }
.visita-a__precio strong { font-size: 1.4rem; letter-spacing: -0.02em; }
.visita-a .pasos-int__detalle p { margin: 28px 0 0; font-size: clamp(1.25rem, 1.1rem + 0.8vw, 1.75rem); line-height: 1.35; letter-spacing: -0.015em; max-width: 30ch; }
@media (max-width: 900px) { .visita-a { grid-template-columns: 1fr; } .visita-a__escena { max-width: 260px; width: 70%; margin-inline: auto; } }

.miedos-a { display: grid; grid-template-columns: 1fr 1fr; gap: clamp(28px, 5vw, 72px); align-items: center; }
.miedos-a__conversa { display: grid; grid-template-columns: 240px 1fr; gap: 12px; align-items: end; }
.miedos-a__conversa .nubo { width: 240px; }
.miedos-a__conversa .burbuja { margin-bottom: 120px; }
@media (max-width: 900px) { .miedos-a { grid-template-columns: 1fr; } .miedos-a__conversa { grid-template-columns: 1fr; } .miedos-a__conversa .nubo { width: 170px; order: 2; } .miedos-a__conversa .burbuja { margin-bottom: 0; } }

.historia__pista { position: relative; height: calc(4 * 80vh + 100vh); }
.historia__marca { position: absolute; left: 0; right: 0; height: 80vh; pointer-events: none; }
.historia__escena { position: sticky; top: 88px; height: calc(100vh - 104px); min-height: 520px; max-height: 760px; }
.historia__panel { height: 100%; border-radius: var(--r-xl); background: var(--marino); color: var(--marfil); padding: clamp(28px, 4vw, 56px); display: grid; grid-template-columns: 0.9fr 1.1fr; gap: clamp(24px, 4vw, 64px); overflow: hidden; position: relative; }
.historia__izq { display: flex; flex-direction: column; justify-content: space-between; gap: 24px; min-height: 0; }
.historia__izq .h2 { max-width: 12ch; }
.historia__lista { list-style: none; margin: 0; padding: 0 0 0 28px; position: relative; display: grid; gap: 18px; }
.historia__lista::before { content: ""; position: absolute; left: 6px; top: 6px; bottom: 6px; width: 2px; background: rgba(250, 248, 243, 0.18); border-radius: 2px; }
.historia__linea { position: absolute; left: 6px; top: 6px; width: 2px; height: calc(100% - 12px); background: var(--lavanda); border-radius: 2px; transform-origin: top; transform: scaleY(0.25); transition: transform 700ms var(--ease-out); }
.historia__lista li { position: relative; font-size: 1.05rem; font-weight: 600; color: rgba(250, 248, 243, 0.5); transition: color var(--dur-base); }
.historia__lista li::before { content: ""; position: absolute; left: -27px; top: 6px; width: 12px; height: 12px; border-radius: 50%; background: var(--marino); border: 2px solid rgba(250, 248, 243, 0.35); transition: background var(--dur-base), border-color var(--dur-base); }
.historia__lista li.hecho, .historia__lista li.activo { color: var(--marfil); }
.historia__lista li.hecho::before, .historia__lista li.activo::before { background: var(--lavanda); border-color: var(--lavanda); }
.historia__der { position: relative; display: grid; grid-template-rows: 1fr auto; align-items: end; min-height: 0; }
.historia__escenario { position: relative; display: grid; place-items: center; min-height: 0; height: 100%; }
.historia__escenario::before { content: ""; position: absolute; width: min(78%, 420px); aspect-ratio: 1; border-radius: 50%; background: rgba(163, 175, 209, 0.14); }
.historia__escenario .nubo { position: relative; width: min(72%, 380px); transition: transform 900ms var(--ease-out); }
.historia[data-paso="1"] .historia__escenario .nubo { transform: translateX(-8%); }
.historia[data-paso="2"] .historia__escenario .nubo { transform: translateX(6%) rotate(-2deg); }
.historia[data-paso="3"] .historia__escenario .nubo { transform: translateY(-4%) scale(1.04); }
.historia__prop { position: absolute; right: 4%; top: 12%; width: 92px; height: 92px; border-radius: 28px; display: grid; place-items: center; background: var(--lavanda); color: var(--marino); box-shadow: 0 18px 40px rgba(0, 0, 0, 0.22); }
.historia__prop .i { width: 44px; height: 44px; stroke-width: 1.5; }
.historia__prop.cambia { animation: prop-cambia 700ms var(--ease-rebote) both; }
@keyframes prop-cambia { from { opacity: 0; transform: translateY(18px) rotate(-12deg) scale(0.7); } to { opacity: 1; transform: none; } }
.historia__texto { min-height: 9.5em; }
.historia__contador { font-family: var(--font-mono); font-size: 0.8125rem; color: var(--lavanda); }
.historia__texto h3 { margin: 8px 0 10px; font-size: clamp(1.6rem, 1.2rem + 1.6vw, 2.6rem); letter-spacing: -0.03em; line-height: 1.05; }
.historia__texto p { margin: 0; font-size: clamp(1.05rem, 1rem + 0.4vw, 1.3rem); line-height: 1.45; color: rgba(250, 248, 243, 0.8); max-width: 34ch; }
.historia__texto.cambia > * { animation: texto-entra 600ms var(--ease-out) both; }
@keyframes texto-entra { from { opacity: 0; transform: translateY(14px); } to { opacity: 1; transform: none; } }
.historia__texto.cambia > *:nth-child(2) { animation-delay: 60ms; }
.historia__texto.cambia > *:nth-child(3) { animation-delay: 120ms; }
.historia__precio { display: inline-flex; align-items: baseline; gap: 10px; width: fit-content; padding: 10px 16px; border-radius: var(--r-pill); background: rgba(250, 248, 243, 0.1); font-size: 0.9375rem; }
.historia__precio strong { font-size: 1.35rem; letter-spacing: -0.02em; }
.historia__barra-m { display: none; }
@media (max-width: 900px) {
  .historia__escena { top: 72px; height: calc(100svh - 168px); min-height: 480px; }
  .historia__panel { grid-template-columns: 1fr; grid-template-rows: auto 1fr; padding: 22px; gap: 12px; }
  .historia__lista, .historia__izq .btn { display: none; }
  .historia__izq { gap: 10px; }
  .historia__izq .h2 { font-size: 1.6rem; max-width: none; }
  .historia__barra-m { display: block; height: 3px; border-radius: 3px; background: rgba(250, 248, 243, 0.18); overflow: hidden; }
  .historia__barra-m span { display: block; height: 100%; background: var(--lavanda); transform-origin: left; transform: scaleX(0.25); transition: transform 700ms var(--ease-out); }
  .historia__prop { width: 64px; height: 64px; border-radius: 20px; }
  .historia__prop .i { width: 30px; height: 30px; }
  .historia__texto { min-height: 8.5em; }
}

.mito-a { display: grid; grid-template-columns: 0.8fr 1.2fr; gap: clamp(28px, 5vw, 72px); align-items: center; }
.mito-a__lado { display: grid; gap: 18px; justify-items: start; }
.mito-a__lado .nubo { width: min(260px, 70%); }
.mito-a .mito { min-height: 360px; }
.mito-a .mito__cara { min-height: 360px; }
.mito-a .mito__frente, .mito-a .mito__vuelta { border-radius: var(--r-xl); padding: clamp(28px, 4vw, 48px); }
@media (max-width: 900px) { .mito-a { grid-template-columns: 1fr; } .mito-a__lado .nubo { width: 150px; } }

.hero-n { position: relative; overflow: hidden; display: grid; grid-template-columns: minmax(0, 1fr); grid-template-rows: auto 1fr; padding-top: clamp(24px, 4vw, 56px); text-align: center; }
.hero-n::before { content: ""; position: absolute; left: 50%; bottom: -30%; width: min(1100px, 140vw); aspect-ratio: 1; transform: translateX(-50%); border-radius: 50%; background: radial-gradient(closest-side, rgba(163, 175, 209, 0.45), transparent 70%); pointer-events: none; }
.hero-n__tx { position: relative; z-index: 2; display: grid; gap: 24px; justify-items: center; }
.hero-n__tx .h1-hero { max-width: 15ch; font-size: clamp(2.5rem, 1.5rem + 3.6vw, 4.4rem); }
.hero-n__tx .lead { max-width: 52ch; }
.hero-n__acciones { display: flex; flex-wrap: wrap; justify-content: center; gap: 12px; }
.hero-n__nubo { position: relative; align-self: end; justify-self: center; width: max(320px, min(112vw, 820px, calc((100svh - 470px) * 2.1))); margin-top: clamp(20px, 3vw, 36px); z-index: 1; }
.hero-n__nubo .nubo-asoma { animation: asoma-grande 1.3s var(--ease-rebote) 0.5s both; }
@keyframes asoma-grande { from { transform: translateY(100%); } to { transform: translateY(0); } }
.hero-n .chip-flota.uno { right: 92%; top: 22%; white-space: nowrap; animation-delay: 1.3s; }
.hero-n .chip-flota.dos { left: 92%; top: 46%; white-space: nowrap; animation-delay: 1.5s; }
.hero-n + .franja-sec .franja { border-top: 0; }
@media (max-width: 720px) {
  .hero-n { min-height: 0; padding-bottom: 0; }
  .hero-n .chip-flota.uno { right: auto; left: 4%; top: auto; bottom: 66%; }
  .hero-n .chip-flota.dos { display: none; }
}

.doctora-a { display: grid; grid-template-columns: 0.9fr 1.1fr; gap: clamp(28px, 5vw, 80px); align-items: center; }
.doctora-a .foto { aspect-ratio: 3 / 4; border-radius: var(--r-xl); }
.doctora-a__nombre { font-size: clamp(2rem, 1.4rem + 2.4vw, 3.4rem); font-weight: 700; letter-spacing: -0.035em; line-height: 1.04; margin: 0; }
.doctora-a__datos { display: grid; gap: 0; margin: 28px 0; padding: 0; list-style: none; border-top: 1px solid var(--linea); }
.doctora-a__datos li { display: flex; gap: 14px; align-items: center; padding: 16px 0; border-bottom: 1px solid var(--linea); }
.doctora-a__datos .i { color: var(--lavanda-sombra); width: 22px; height: 22px; }
@media (max-width: 900px) { .doctora-a { grid-template-columns: 1fr; } .doctora-a .foto { max-width: 420px; } }

.visitanos-a { display: grid; grid-template-columns: 0.9fr 1.1fr; gap: 16px; }
.visitanos-a__info { padding: clamp(24px, 3vw, 40px); border-radius: var(--r-xl); background: var(--marfil); border: 1px solid var(--linea); display: grid; gap: 22px; align-content: start; }
.visitanos-a .mapa { min-height: 420px; border-radius: var(--r-xl); }
.resena-a { display: flex; align-items: center; gap: 14px; padding: 16px; border-radius: var(--r-md); background: var(--crema); }
.resena-a strong { font-size: 2rem; letter-spacing: -0.03em; line-height: 1; }
@media (max-width: 900px) { .visitanos-a { grid-template-columns: 1fr; } .visitanos-a .mapa { min-height: 300px; } }
'''

def tabs():
    out = []
    for i, t in enumerate(TRATAMIENTOS):
        sel = "true" if i == 0 else "false"
        out.append(f'<button class="selector-tx__tab" role="tab" data-tab="{t[0]}" aria-selected="{sel}" tabindex="{0 if i == 0 else -1}"><span><strong>{t[1]}</strong><small>{t[2]}</small></span>{ic("arrow-right")}</button>')
    return "\n".join(out)

def paneles():
    out = []
    for i, t in enumerate(TRATAMIENTOS):
        act = " activo" if i == 0 else ""
        datos = "".join(f'<span class="dato">{ic(a)}{b}</span>' for a, b in t[4])
        out.append(f'''<div class="selector-tx__panel trat-a__panel{act}" role="tabpanel" data-panel="{t[0]}">
  {foto("Foto pendiente", t[5])}
  <div class="trat-a__panel-tx">
    <h3 class="h3" style="margin:0">{t[1]}</h3>
    <p class="texto">{t[3]}</p>
    <div class="datos">{datos}</div>
    <a class="enlace" href="#">Conoce el tratamiento {ic("arrow-right")}</a>
  </div>
</div>''')
    return "\n".join(out)

def pasos():
    btns = "".join(f'<button class="pasos-int__btn" data-paso data-estado="{p[2]}"><span>{"0"+str(i+1)}</span><strong>{p[0]}</strong></button>' for i, p in enumerate(PASOS))
    dets = "".join(f'<div class="pasos-int__detalle" data-detalle><p>{p[1]}</p></div>' for p in PASOS)
    return btns, dets

def miedos():
    return "".join(f'<button class="miedo" data-miedo="{m[1]}" data-estado="{m[2]}" aria-pressed="{"true" if i == 0 else "false"}">{m[0]}</button>' for i, m in enumerate(MIEDOS))

btns, dets = pasos()
PROPS = ["stethoscope", "scan", "mood-smile", "file-text"]
marcas = "".join(f'<div class="historia__marca" data-historia-marca="{i}" style="top: calc({i} * 80vh)"></div>' for i in range(4))
lista = "".join(f'<li data-historia-item>{p[0]}</li>' for p in PASOS)
p0t, p0d = PASOS[0][0], PASOS[0][1]
datos_historia = [{"t": p[0], "d": p[1], "e": p[2], "i": PROPS[k]} for k, p in enumerate(PASOS)]
import json as _json
html = cabeza("Dental Díaz · Inicio · Propuesta A", CSS) + nav("A · Clara") + f'''
<main>
<section class="hero-a">
  <div class="contenedor hero-a__grid">
    <div class="hero-a__tx">
      <h1 class="h1-hero" data-palabras>Te explicamos <span class="subrayado">todo</span> antes de empezar</h1>
      <p class="lead">Clínica dental familiar en Terán. Revisamos con calma, te enseñamos tus radiografías y tu plan va por escrito.</p>
      <div class="hero-a__acciones">
        <a class="btn btn--primario" href="#agenda">Agenda tu valoración {ic("arrow-right","flecha")}</a>
        <a class="btn btn--secundario" href="{WA}" target="_blank" rel="noopener">{ic("brand-whatsapp")} Escríbenos</a>
      </div>
    </div>
    <div class="hero-a__media">
      <div class="hero-a__nubo"><div class="nubo nubo-asoma" data-nubo="hero" data-mirada aria-label="Nubo asomándose"></div></div>
      {foto("Foto 1 · Hero", "La doctora explicando a un paciente con la radiografía en pantalla. Luz natural, vertical 4:5.")}
      <div class="chip-flota uno"><span class="chip-flota__icono">{ic("star-filled")}</span><div><strong>4.9 en Google</strong><span>5 reseñas</span></div></div>
      <div class="chip-flota dos"><span class="chip-flota__icono">{ic("receipt-2")}</span><div><strong>Valoración $350</strong><span>Se descuenta de tu tratamiento</span></div></div>
    </div>
  </div>
  <div class="contenedor">
    <div class="franja revela" style="margin-top: clamp(48px, 6vw, 80px)" data-escalonar>
      <div class="franja__item"><span class="franja__icono">{ic("map-pin")}</span><div><strong>Desde 2021 en Terán</strong><span>A un costado del parque</span></div></div>
      <div class="franja__item"><span class="franja__icono">{ic("scan")}</span><div><strong>Radiografía digital</strong><span>En tu valoración</span></div></div>
      <div class="franja__item"><span class="franja__icono">{ic("credit-card")}</span><div><strong>Hasta 6 meses sin intereses</strong><span>Aplican restricciones</span></div></div>
      <div class="franja__item"><span class="franja__icono">{ic("file-text")}</span><div><strong>Precio por escrito</strong><span>Antes de empezar</span></div></div>
    </div>
  </div>
</section>

<section class="seccion" id="tratamientos" style="padding-top: clamp(24px, 4vw, 48px)">
  <div class="contenedor">
    <div class="titular revela"><h2 class="h2">¿Qué necesitas hoy?</h2></div>
    <div class="trat-a" data-selector data-hover>
      <div class="selector-tx__lista revela" role="tablist" aria-label="Tratamientos">
{tabs()}
      </div>
      <div class="revela" style="--retraso: 120ms">
{paneles()}
      </div>
    </div>
  </div>
</section>

<section class="seccion historia" id="primera-visita" style="padding-top: 0" data-historia data-paso="0">
  <div class="contenedor">
    <div class="historia__pista">
      {marcas}
      <div class="historia__escena">
        <div class="historia__panel">
          <div class="historia__izq">
            <div style="display:grid; gap: 14px">
              <h2 class="h2">Así es tu primera visita</h2>
              <div class="historia__precio">Valoración de 45 minutos <strong>$350</strong></div>
              <div class="historia__barra-m"><span data-historia-barra-m></span></div>
            </div>
            <ol class="historia__lista"><span class="historia__linea" data-historia-linea></span>{lista}</ol>
            <a class="btn btn--claro" href="#agenda" style="width: fit-content">Agenda tu valoración {ic("arrow-right","flecha")}</a>
          </div>
          <div class="historia__der">
            <div class="historia__escenario">
              <div class="nubo" data-nubo="escucha" data-mirada aria-label="Nubo"></div>
              <div class="historia__prop" data-historia-prop>{ic("stethoscope")}</div>
            </div>
            <div class="historia__texto" data-historia-texto aria-live="polite">
              <span class="historia__contador">Paso 1 de 4</span>
              <h3>{p0t}</h3>
              <p>{p0d}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="seccion" style="padding-top: 0">
  <div class="contenedor miedos-a" data-miedos>
    <div class="revela">
      <h2 class="h2">Sabemos qué te preocupa</h2>
      <p class="texto" style="margin: 16px 0 28px; font-size: var(--fs-lead); max-width: 40ch">Toca lo que más te pesa. Nubo te cuenta cómo lo cuidamos.</p>
      <div class="miedos__opciones">{miedos()}</div>
    </div>
    <div class="miedos-a__conversa revela" style="--retraso: 120ms">
      <div class="nubo" data-nubo="empatico" aria-label="Nubo"></div>
      <div class="burbuja" data-respuesta aria-live="polite">{MIEDOS[0][1]}</div>
    </div>
  </div>
</section>

<section class="seccion" id="clinica" style="padding-top: 0">
  <div class="contenedor doctora-a">
    <div class="revela">{foto("Foto 2 · Retrato", "La doctora de frente, sonriendo, con bata. Fondo de la clínica desenfocado. Vertical 3:4.")}</div>
    <div class="revela" style="--retraso: 120ms">
      <h2 class="doctora-a__nombre">Dra. María Concepción Díaz Márquez</h2>
      <p class="lead" style="margin-top: 20px; max-width: 44ch">Fundó Dental Díaz en 2021, en Terán. Su forma de trabajar: sin prisa y con todo explicado.</p>
      <ul class="doctora-a__datos">
        <li>{ic("stethoscope")} Estudió en UNISUR</li>
        <li>{ic("sparkles")} Actualizándose en odontología estética adhesiva</li>
        <li>{ic("file-text")} Cédula profesional 15529125</li>
      </ul>
      <a class="enlace" href="#">Conoce la clínica {ic("arrow-right")}</a>
    </div>
  </div>
</section>

<section class="seccion" style="padding-top: 0">
  <div class="contenedor mito-a">
    <div class="mito-a__lado revela">
      <div class="nubo" data-nubo="sorprendido" data-mirada aria-label="Nubo sorprendido"></div>
      <h2 class="h2">¿Mito o realidad?</h2>
      <p class="texto" style="font-size: var(--fs-lead); max-width: 34ch">Un mito que la doctora quiere aclarar. Toca la tarjeta.</p>
      <a class="enlace" href="#">Más en Nubo explica {ic("arrow-right")}</a>
    </div>
    <button class="mito revela" data-voltear aria-pressed="false" aria-label="Voltear tarjeta del mito" style="--retraso: 120ms">
      <div class="mito__cara">
        <div class="mito__frente"><span class="mito__pista">{ic("refresh")} Mito o realidad</span><p class="h2" style="margin:0; max-width: 16ch">"Con la edad, los dientes se tienen que caer"</p><span class="mito__pista">Toca para ver la respuesta</span></div>
        <div class="mito__vuelta"><span class="mito__pista">{ic("check")} Es un mito</span><p class="h3" style="margin:0; max-width: 28ch; font-weight: 600">Perder dientes no es parte normal de envejecer. Con revisiones y cuidado, te pueden acompañar toda la vida.</p><span class="mito__pista">Respuesta por validar con la doctora</span></div>
      </div>
    </button>
  </div>
</section>

<section class="seccion" id="visitanos" style="padding-top: 0">
  <div class="contenedor">
    <div class="titular revela"><h2 class="h2">Estamos a un costado del parque de Terán</h2></div>
    <div class="visitanos-a">
      <div class="visitanos-a__info revela">
        <span class="estado-abierto" data-abierto>Horario</span>
        <ul class="horario tabular">
          <li><span>Lunes a viernes</span><span>10:00 a 14:00 y 16:00 a 20:00</span></li>
          <li><span>Sábado</span><span>10:00 a 14:00</span></li>
          <li><span>Domingo</span><span>Cerrado</span></li>
        </ul>
        <p class="texto">2da Norte Oriente #438, Terán, Tuxtla Gutiérrez.</p>
        <div class="resena-a">{estrellas()}<div><strong>4.9</strong></div><span class="texto chico">en Google, de 5 reseñas</span></div>
        <div style="display:flex; flex-wrap: wrap; gap: 10px">
          <a class="btn btn--primario btn--chico" href="{MAPS}" target="_blank" rel="noopener">{ic("navigation")} Cómo llegar</a>
          <a class="btn btn--secundario btn--chico" href="tel:+529611385698">{ic("phone")} Llamar</a>
        </div>
      </div>
      <div class="mapa revela" style="--retraso: 120ms">
        <iframe src="{MAPA_EMBED}" loading="lazy" title="Mapa de Dental Díaz en Terán" referrerpolicy="no-referrer-when-downgrade"></iframe>
      </div>
    </div>
  </div>
</section>

<section class="seccion" id="agenda" style="padding-top: 0">
  <div class="contenedor">
    <div class="cierre revela">
      <div>
        <h2 class="h1">Tu primera visita empieza con una pregunta</h2>
        <p>Agenda tu valoración de 45 minutos. Revisamos, te explicamos y te llevas tu plan por escrito.</p>
        <div class="cierre__acciones">
          <a class="btn btn--claro" href="#agenda">Agenda tu valoración {ic("arrow-right","flecha")}</a>
          <a class="btn btn--whatsapp" href="{WA}" target="_blank" rel="noopener">{ic("brand-whatsapp")} Escríbenos</a>
        </div>
      </div>
      <div class="nubo" data-nubo="invita" data-mirada aria-label="Nubo invitándote"></div>
    </div>
  </div>
</section>
</main>
''' + pie()

html = html.replace("</main>", "</main>\n<script>window.HISTORIA = " + _json.dumps(datos_historia, ensure_ascii=False) + ";</script>")
open("../inicio-a.html", "w").write(html)

ini = html.index('<section class="hero-a">')
fin = html.index('</section>', ini) + len('</section>')
franja = html[html.index('<div class="franja revela"', ini):html.index('</section>', ini)]
franja = franja[:franja.rindex('</div>')]
hero_n = f'''<section class="hero-n">
  <div class="contenedor hero-n__tx">
    <h1 class="h1-hero" data-palabras>Te explicamos <span class="subrayado">todo</span> antes de empezar</h1>
    <p class="lead">Clínica dental familiar en Terán. Revisamos con calma, te enseñamos tus radiografías y tu plan va por escrito.</p>
    <div class="hero-n__acciones">
      <a class="btn btn--primario" href="#agenda">Agenda tu valoración {ic("arrow-right","flecha")}</a>
      <a class="btn btn--secundario" href="{WA}" target="_blank" rel="noopener">{ic("brand-whatsapp")} Escríbenos</a>
    </div>
  </div>
  <div class="hero-n__nubo">
    <div class="nubo nubo-asoma" data-nubo="hero" data-mirada aria-label="Nubo asomándose"></div>
    <div class="chip-flota uno"><span class="chip-flota__icono">{ic("star-filled")}</span><div><strong>4.9 en Google</strong><span>5 reseñas</span></div></div>
    <div class="chip-flota dos"><span class="chip-flota__icono">{ic("receipt-2")}</span><div><strong>Valoración $350</strong><span>Se descuenta de tu tratamiento</span></div></div>
  </div>
</section>
<section class="franja-sec"><div class="contenedor">{franja.replace('style="margin-top: clamp(48px, 6vw, 80px)"', '')}</div></section>'''
html2 = html[:ini] + hero_n + html[fin:]
html2 = html2.replace("Propuesta A · Clara", "Propuesta A2 · Hero con Nubo").replace("Inicio · Propuesta A<", "Inicio · Propuesta A2<")
open("../inicio-a2.html", "w").write(html2)
print("ok A2", len(html2))
print("ok A", len(html))
