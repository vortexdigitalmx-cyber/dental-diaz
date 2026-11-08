from comun import *

NUBE = "M 189 55 C 207 41 220 37 231 39 C 248 41 244 59 251 68 C 260 79 275 62 291 66 C 315 71 330 102 343 137 C 359 178 367 222 363 256 C 360 285 348 305 327 312 C 305 320 281 315 256 308 C 232 302 211 302 188 310 C 161 318 140 326 120 321 C 96 316 83 300 82 277 C 79 249 87 207 100 171 C 120 117 151 78 189 55 Z"

CSS = CSS_COMUN + '''
.hero-b { position: relative; overflow: hidden; padding-block: clamp(32px, 5vw, 72px) clamp(48px, 6vw, 96px); }
.hero-b__grid { display: grid; grid-template-columns: 1.05fr 0.95fr; gap: 24px; align-items: center; min-height: min(78vh, 720px); }
.hero-b__tx { display: grid; gap: 26px; position: relative; z-index: 2; }
.hero-b__tx .lead { max-width: 34ch; }
.hero-b__escena { position: relative; display: grid; place-items: center; }
.hero-b__nube { position: absolute; width: 132%; left: -8%; top: 50%; transform: translateY(-52%); fill: var(--lavanda); opacity: 0.32; animation: nube-flota 9s ease-in-out infinite alternate; }
@keyframes nube-flota { from { transform: translateY(-52%) rotate(-3deg) scale(1); } to { transform: translateY(-48%) rotate(2deg) scale(1.03); } }
.hero-b__escena .nubo { width: 92%; max-width: 560px; position: relative; z-index: 1; }
.hero-b .chip-flota.uno { right: 4%; top: 8%; animation-delay: 800ms; }
.hero-b .chip-flota.dos { left: 2%; bottom: 10%; animation-delay: 1000ms; }
.hero-b__saludo { position: absolute; left: 6%; top: 6%; z-index: 2; padding: 12px 16px; border-radius: 20px 20px 20px 4px; background: var(--marino); color: var(--marfil); font-weight: 600; font-size: 0.9375rem; animation: flota-entra 700ms var(--ease-rebote) 1.2s both; }
@media (max-width: 900px) {
  .hero-b__grid { grid-template-columns: 1fr; min-height: 0; }
  .hero-b__escena { max-width: 420px; width: 100%; margin-inline: auto; padding-bottom: 64px; }
  .hero-b .chip-flota.uno { right: 0; top: auto; bottom: 0; }
  .hero-b .chip-flota.dos { display: none; }
  .relato__guia { opacity: 0; transform: translateY(16px); transition: opacity var(--dur-base), transform var(--dur-base) var(--ease-out); }
  body.relato-activo .relato__guia { opacity: 1; transform: none; }
}

.relato { display: grid; grid-template-columns: 320px 1fr; gap: clamp(32px, 5vw, 80px); align-items: start; }
.relato__guia { position: sticky; top: 110px; display: grid; gap: 16px; justify-items: start; }
.relato__guia .nubo { width: 240px; }
.relato__guia .burbuja { min-height: 0; font-size: 1.1rem; border-radius: 24px 24px 24px 6px; }
.capitulo { padding-block: clamp(56px, 8vw, 112px); border-top: 1px solid var(--linea); }
.capitulo:first-child { border-top: 0; padding-top: 0; }
.capitulo .h2 { margin-bottom: clamp(24px, 3vw, 40px); max-width: 16ch; }
@media (max-width: 900px) {
  .relato { grid-template-columns: 1fr; }
  .relato__guia { position: fixed; top: auto; left: 12px; bottom: 92px; z-index: 40; grid-template-columns: 72px auto; align-items: end; gap: 8px; pointer-events: none; max-width: calc(100vw - 24px); }
  .relato__guia .nubo { width: 72px; }
  .relato__guia .burbuja { font-size: 0.8125rem; padding: 10px 12px; max-width: 220px; box-shadow: var(--sombra-flotante); }
}

.lista-tx { list-style: none; margin: 0; padding: 0; border-top: 1px solid var(--linea-fuerte); }
.lista-tx li { border-bottom: 1px solid var(--linea-fuerte); }
.lista-tx a { display: grid; grid-template-columns: 1fr auto; gap: 8px 24px; padding: 24px 4px; text-decoration: none; align-items: center; }
.lista-tx__nombre { font-size: clamp(2rem, 1.3rem + 2.8vw, 3.6rem); font-weight: 700; letter-spacing: -0.04em; line-height: 1; transition: transform var(--dur-lenta) var(--ease-out), color var(--dur-base); }
.lista-tx__flecha { width: 56px; height: 56px; border-radius: 50%; display: grid; place-items: center; border: 1.5px solid var(--linea-fuerte); transition: background var(--dur-base), color var(--dur-base), transform var(--dur-base) var(--ease-out); }
.lista-tx__mas { grid-column: 1 / -1; display: grid; grid-template-rows: 0fr; transition: grid-template-rows var(--dur-lenta) var(--ease-out); }
.lista-tx__mas > div { overflow: hidden; display: grid; grid-template-columns: 1fr 200px; gap: 24px; align-items: center; }
.lista-tx__mas p { margin: 0; max-width: 46ch; color: var(--texto-suave); }
.lista-tx__mas .foto { aspect-ratio: 4 / 3; border-radius: var(--r-md); }
.lista-tx__mas .foto__guia { font-size: 0.6875rem; padding: 8px 10px; margin: 8px; }
.lista-tx a:hover .lista-tx__nombre, .lista-tx a:focus-visible .lista-tx__nombre { transform: translateX(10px); }
.lista-tx a:hover .lista-tx__flecha { background: var(--marino); color: var(--marfil); transform: rotate(-45deg); }
.lista-tx a:hover .lista-tx__mas, .lista-tx a:focus-visible .lista-tx__mas { grid-template-rows: 1fr; }
.lista-tx a:hover .lista-tx__mas > div, .lista-tx a:focus-visible .lista-tx__mas > div { padding-top: 16px; }
@media (hover: none) { .lista-tx__mas { grid-template-rows: 1fr; } .lista-tx__mas > div { padding-top: 12px; grid-template-columns: 1fr; } .lista-tx__mas .foto { display: none; } }

.linea-t { position: relative; list-style: none; margin: 0; padding: 0 0 0 48px; display: grid; gap: 40px; }
.linea-t::before { content: ""; position: absolute; left: 15px; top: 8px; bottom: 8px; width: 2px; background: var(--linea-fuerte); border-radius: 2px; }
.linea-t li { position: relative; }
.linea-t li::before { content: ""; position: absolute; left: -41px; top: 6px; width: 18px; height: 18px; border-radius: 50%; background: var(--crema); border: 3px solid var(--lavanda-sombra); }
.linea-t li.visible::before { background: var(--marino); border-color: var(--marino); transition: background 400ms 300ms, border-color 400ms 300ms; }
.linea-t strong { display: block; font-size: clamp(1.4rem, 1.2rem + 0.8vw, 2rem); letter-spacing: -0.025em; line-height: 1.1; margin-bottom: 8px; }

.preguntas-b details { border-bottom: 1px solid var(--linea-fuerte); }
.preguntas-b details:first-child { border-top: 1px solid var(--linea-fuerte); }
.preguntas-b summary { list-style: none; display: flex; justify-content: space-between; align-items: center; gap: 16px; padding: 24px 0; cursor: pointer; font-size: clamp(1.25rem, 1.1rem + 0.6vw, 1.6rem); font-weight: 700; letter-spacing: -0.02em; }
.preguntas-b summary::-webkit-details-marker { display: none; }
.preguntas-b summary .i { transition: transform var(--dur-base) var(--ease-out); width: 26px; height: 26px; }
.preguntas-b details[open] summary .i { transform: rotate(45deg); }
.preguntas-b details p { margin: 0 0 24px; max-width: 52ch; color: var(--texto-suave); font-size: 1.0625rem; }

.doc-b { display: grid; grid-template-columns: 1fr 1fr; gap: 24px; align-items: stretch; }
.doc-b .foto { border-radius: var(--r-lg); min-height: 320px; }
.doc-b__tx { padding: 28px; border-radius: var(--r-lg); background: var(--marfil); border: 1px solid var(--linea); display: grid; gap: 14px; align-content: start; }
.doc-b .mito { min-height: 300px; grid-column: 1 / -1; }
@media (max-width: 720px) { .doc-b { grid-template-columns: 1fr; } }

.lugar-b { display: grid; gap: 16px; }
.lugar-b .mapa { min-height: 340px; }
.lugar-b__fila { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
.lugar-b__fila > div { padding: 24px; border-radius: var(--r-lg); background: var(--marfil); border: 1px solid var(--linea); display: grid; gap: 14px; align-content: start; }
@media (max-width: 720px) { .lugar-b__fila { grid-template-columns: 1fr; } }
'''

def lista():
    out = []
    for t in TRATAMIENTOS:
        out.append(f'''<li><a href="#"><span class="lista-tx__nombre">{t[1]}</span><span class="lista-tx__flecha">{ic("arrow-up-right")}</span>
  <span class="lista-tx__mas"><div><p>{t[3]}</p>{foto("Foto", t[5])}</div></span></a></li>''')
    return "\n".join(out)

pasos = "".join(f'<li class="revela"><strong>{p[0]}</strong><p class="texto">{p[1]}</p></li>' for p in PASOS)
preguntas = "".join(f'<details{" open" if i == 0 else ""}><summary>{m[0]}{ic("plus")}</summary><p>{m[1]}</p></details>' for i, m in enumerate(MIEDOS))

html = cabeza("Dental Díaz · Inicio · Propuesta B", CSS) + nav("B · Nubo te acompaña") + f'''
<main>
<section class="hero-b">
  <div class="contenedor hero-b__grid">
    <div class="hero-b__tx">
      <h1 class="h1-hero" data-palabras>Te explicamos <span class="subrayado">todo</span> antes de empezar</h1>
      <p class="lead">Clínica dental familiar en Terán. Revisamos con calma, te enseñamos tus radiografías y tu plan va por escrito.</p>
      <div style="display:flex; flex-wrap:wrap; gap:12px">
        <a class="btn btn--primario" href="#agenda">Agenda tu valoración {ic("arrow-right","flecha")}</a>
        <a class="btn btn--secundario" href="{WA}" target="_blank" rel="noopener">{ic("brand-whatsapp")} Escríbenos</a>
      </div>
    </div>
    <div class="hero-b__escena">
      <svg class="hero-b__nube" viewBox="70 30 310 300" aria-hidden="true"><path d="{NUBE}"/></svg>
      <div class="nubo nubo-entra-b" data-nubo="saluda" data-mirada data-saluda data-entrar aria-label="Nubo saludando"></div>
      <div class="hero-b__saludo">Hola, soy Nubo</div>
      <div class="chip-flota uno"><span class="chip-flota__icono">{ic("star-filled")}</span><div><strong>4.9 en Google</strong><span>5 reseñas</span></div></div>
      <div class="chip-flota dos"><span class="chip-flota__icono">{ic("receipt-2")}</span><div><strong>Valoración $350</strong><span>Se descuenta de tu tratamiento</span></div></div>
    </div>
  </div>
</section>

<section class="seccion" style="padding-top: clamp(24px, 4vw, 56px)">
  <div class="contenedor relato">
    <aside class="relato__guia" aria-hidden="true">
      <div class="nubo" data-nubo="explica" data-narrador data-mirada></div>
      <div class="burbuja" data-narrador-texto>Te cuento qué hacemos aquí.</div>
    </aside>
    <div>
      <div class="capitulo" id="tratamientos" data-nubo-estado="explica" data-nubo-dice="Te cuento qué hacemos aquí.">
        <h2 class="h2 revela">Tratamientos</h2>
        <ul class="lista-tx revela">{lista()}</ul>
      </div>
      <div class="capitulo" id="primera-visita" data-nubo-estado="escucha" data-nubo-dice="Tu primera visita dura 45 minutos. Así es:">
        <h2 class="h2 revela">Así es tu primera visita</h2>
        <ol class="linea-t">{pasos}</ol>
        <a class="btn btn--primario" href="#agenda" style="margin-top: 40px">Agenda tu valoración {ic("arrow-right","flecha")}</a>
      </div>
      <div class="capitulo" data-nubo-estado="empatico" data-nubo-dice="Si te da nervio, es normal. ¿Qué te preocupa?">
        <h2 class="h2 revela">Sabemos qué te preocupa</h2>
        <div class="preguntas-b revela">{preguntas}</div>
      </div>
      <div class="capitulo" id="clinica" data-nubo-estado="sorprendido" data-nubo-dice="Ella es la doctora Díaz. Y abajo, un mito que ella quiere aclarar.">
        <h2 class="h2 revela">Quién te atiende</h2>
        <div class="doc-b">
          <div class="revela">{foto("Foto 2 · Retrato", "La doctora de frente, sonriendo, con bata. Horizontal 4:3.")}</div>
          <div class="doc-b__tx revela" style="--retraso: 100ms">
            <h3 class="h3" style="margin:0">Dra. María Concepción Díaz Márquez</h3>
            <p class="texto">Fundó Dental Díaz en 2021, en Terán. Estudió en UNISUR y se está actualizando en odontología estética adhesiva.</p>
            <span class="dato" style="width: fit-content">{ic("file-text")} Cédula 15529125</span>
            <a class="enlace" href="#">Conoce la clínica {ic("arrow-right")}</a>
          </div>
          <button class="mito revela" data-voltear aria-pressed="false" aria-label="Voltear tarjeta del mito">
            <div class="mito__cara">
              <div class="mito__frente"><span class="mito__pista">{ic("refresh")} Mito</span><p class="h2" style="margin:0; max-width: 18ch">"Con la edad, los dientes se tienen que caer"</p><span class="mito__pista">Toca para ver la realidad</span></div>
              <div class="mito__vuelta"><span class="mito__pista">{ic("check")} Realidad</span><p class="h3" style="margin:0; max-width: 30ch; font-weight: 600">Perder dientes no es parte normal de envejecer. Con revisiones y cuidado, te pueden acompañar toda la vida.</p><span class="mito__pista">La doctora lo explica en Nubo explica</span></div>
            </div>
          </button>
        </div>
      </div>
      <div class="capitulo" id="visitanos" data-nubo-estado="invita" data-nubo-dice="Te esperamos a un costado del parque de Terán.">
        <h2 class="h2 revela">Visítanos</h2>
        <div class="lugar-b">
          <div class="mapa revela"><iframe src="{MAPA_EMBED}" loading="lazy" title="Mapa de Dental Díaz en Terán" referrerpolicy="no-referrer-when-downgrade"></iframe><a class="mapa__pin" href="{MAPS}" target="_blank" rel="noopener">{ic("navigation")} Cómo llegar</a></div>
          <div class="lugar-b__fila">
            <div class="revela"><span class="estado-abierto" data-abierto>Horario</span><ul class="horario tabular"><li><span>Lun a vie</span><span>10:00 a 14:00 y 16:00 a 20:00</span></li><li><span>Sábado</span><span>10:00 a 14:00</span></li></ul></div>
            <div class="revela" style="--retraso: 100ms"><strong style="font-size: 1.1rem">2da Norte Oriente #438, Terán</strong><span class="texto">A un costado del parque de Terán, Tuxtla Gutiérrez.</span><a class="enlace" href="tel:+529611385698">{ic("phone")} 961 138 5698</a></div>
          </div>
        </div>
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
      <div class="nubo" data-nubo="celebra" aria-label="Nubo celebrando"></div>
    </div>
  </div>
</section>
</main>
''' + pie()

open("../inicio-b.html", "w").write(html)
print("ok B", len(html))
