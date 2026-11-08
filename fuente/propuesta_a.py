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
.miedos-a__conversa { display: grid; grid-template-columns: 150px 1fr; gap: 18px; align-items: end; }
.miedos-a__conversa .nubo { width: 150px; }
@media (max-width: 900px) { .miedos-a { grid-template-columns: 1fr; } .miedos-a__conversa { grid-template-columns: 96px 1fr; } .miedos-a__conversa .nubo { width: 96px; } }

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

<section class="seccion" id="primera-visita" style="padding-top: 0">
  <div class="contenedor">
    <div class="visita-a revela" data-pasos>
      <div class="visita-a__escena"><div class="nubo" data-nubo="escucha" data-mirada aria-label="Nubo"></div></div>
      <div>
        <h2 class="h2">Así es tu primera visita</h2>
        <div class="visita-a__precio">Valoración de 45 minutos <strong>$350</strong></div>
        <div class="pasos-int" style="margin-top: 40px">
          <div class="pasos-int__nav"><span class="pasos-int__riel"></span><span class="pasos-int__barra" data-progreso></span>{btns}</div>
          {dets}
        </div>
        <a class="btn btn--claro" href="#agenda" style="margin-top: 36px">Agenda tu valoración {ic("arrow-right","flecha")}</a>
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

open("../inicio-a.html", "w").write(html)
print("ok A", len(html))
