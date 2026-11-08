from comun import *

CSS = CSS_COMUN + '''
.bento { display: grid; gap: 14px; }
.celda { position: relative; overflow: hidden; border-radius: var(--r-lg); background: var(--marfil); border: 1px solid var(--linea); padding: clamp(20px, 2.2vw, 28px); display: flex; flex-direction: column; justify-content: space-between; gap: 16px; transition: transform var(--dur-lenta) var(--ease-out), box-shadow var(--dur-lenta) var(--ease-out); }
a.celda { text-decoration: none; }
a.celda:hover { transform: translateY(-4px); box-shadow: var(--sombra-flotante); }
.celda--marino { background: var(--marino); color: var(--marfil); border-color: var(--marino); }
.celda--marino .texto, .celda--marino .chico { color: rgba(250, 248, 243, 0.76); }
.celda--lavanda { background: var(--lavanda); border-color: var(--lavanda); }
.celda--foto { padding: 0; }
.celda--foto .foto { position: absolute; inset: 0; border-radius: 0; }
.celda .grande { font-size: clamp(2.6rem, 1.8rem + 2.6vw, 4rem); font-weight: 700; letter-spacing: -0.045em; line-height: 0.95; }

.hero-c { padding-block: clamp(16px, 3vw, 40px) clamp(48px, 6vw, 88px); }
.hero-c .bento { grid-template-columns: repeat(4, minmax(0, 1fr)); grid-template-rows: repeat(3, minmax(170px, auto)); }
.c-titulo { grid-column: span 2; grid-row: span 2; justify-content: flex-end; gap: 24px; padding: clamp(28px, 3.5vw, 48px); }
.c-titulo .lead { max-width: 32ch; }
.c-foto { grid-column: 3; grid-row: span 2; }
.c-nubo { grid-column: 4; justify-content: flex-start; padding: 0; min-height: 190px; }
.c-nubo .nubo { position: absolute; left: -12%; bottom: -2px; width: 124%; }
.c-nubo__txt { position: relative; z-index: 2; margin: 18px; padding: 8px 12px; border-radius: 16px 16px 16px 4px; background: var(--marfil); color: var(--marino); font-size: 0.875rem; font-weight: 600; align-self: flex-start; }
.c-google { grid-column: 4; }
.c-abierto { grid-column: 1; }
.c-precio { grid-column: 2; }
.c-meses { grid-column: span 2; }
.c-meses__bancos { display: flex; flex-wrap: wrap; gap: 6px; }
.c-meses__bancos span { padding: 5px 10px; border-radius: 999px; background: var(--crema); font-size: 0.8125rem; font-weight: 600; }
@media (max-width: 1024px) {
  .hero-c .bento { grid-template-columns: repeat(2, minmax(0, 1fr)); grid-template-rows: none; }
  .c-titulo { grid-column: span 2; grid-row: auto; }
  .c-foto { grid-column: 1; grid-row: span 2; min-height: 360px; }
  .c-nubo, .c-google { grid-column: 2; }
  .c-abierto { grid-column: 1; } .c-precio { grid-column: 2; }
  .c-meses { grid-column: span 2; }
}
@media (max-width: 560px) {
  .hero-c .bento { grid-template-columns: 1fr 1fr; }
  .c-titulo { order: 0; }
  .c-nubo { order: 1; grid-column: 1; min-height: 170px; }
  .c-google { order: 2; grid-column: 2; }
  .c-foto { order: 3; grid-column: span 2; grid-row: auto; min-height: 320px; }
  .c-precio { order: 4; grid-column: 2; } .c-abierto { order: 4; grid-column: 1; }
  .c-meses { order: 6; }
}

.trat-c { grid-template-columns: repeat(4, minmax(0, 1fr)); grid-auto-rows: minmax(200px, auto); }
.t-blanq { grid-column: span 2; grid-row: span 2; padding: 0; justify-content: flex-end; }
.t-blanq .foto { position: absolute; inset: 0; border-radius: 0; }
.t-blanq__tx { position: relative; z-index: 2; margin: 14px; padding: 22px; border-radius: var(--r-md); background: rgba(250, 248, 243, 0.94); display: grid; gap: 10px; }
.t-orto { grid-column: span 2; }
.t-ninos { padding-right: 40%; }
.t-ninos .nubo { position: absolute; right: -14%; bottom: -10%; width: 70%; }
.t-general { grid-column: span 4; flex-direction: row; align-items: center; flex-wrap: wrap; }
.t-general .datos { flex: 1; justify-content: flex-end; }
.celda__pie { display: flex; justify-content: space-between; align-items: center; font-weight: 600; font-size: 0.9375rem; }
.celda__pie .circulo { width: 40px; height: 40px; border-radius: 50%; display: grid; place-items: center; background: var(--crema); color: var(--marino); transition: transform var(--dur-base) var(--ease-out), background var(--dur-base), color var(--dur-base); }
a.celda:hover .circulo { transform: rotate(-45deg); background: var(--marino); color: var(--marfil); }
.celda--marino .celda__pie .circulo { background: rgba(250, 248, 243, 0.14); color: var(--marfil); }
@media (max-width: 900px) {
  .trat-c { grid-template-columns: 1fr 1fr; }
  .t-blanq { grid-column: span 2; min-height: 420px; }
  .t-orto { grid-column: span 2; }
  .t-general { grid-column: span 2; }
  .t-general .datos { justify-content: flex-start; }
}
@media (max-width: 560px) { .t-prot, .t-ninos { grid-column: span 2; } }

.visita-c { display: grid; grid-template-columns: 1fr 340px; gap: 14px; }
.visita-c__pasos { padding: clamp(24px, 3.5vw, 48px); }
.visita-c__pasos .pasos-int__detalle p { margin: 28px 0 0; font-size: clamp(1.2rem, 1.05rem + 0.7vw, 1.6rem); line-height: 1.4; max-width: 34ch; letter-spacing: -0.01em; }
.visita-c__nubo { align-items: center; justify-content: center; }
.visita-c__nubo .nubo { width: 86%; }
@media (max-width: 900px) { .visita-c { grid-template-columns: 1fr; } .visita-c__nubo { order: -1; min-height: 240px; } .visita-c__nubo .nubo { width: 220px; } }

.dupla-c { display: grid; grid-template-columns: 1.2fr 0.8fr; gap: 14px; }
.dupla-c .burbuja { min-height: 6.5em; background: var(--crema); }
.dupla-c .mito { min-height: 340px; }
.dupla-c .mito__cara, .dupla-c .mito__frente, .dupla-c .mito__vuelta { border-radius: var(--r-lg); }
@media (max-width: 900px) { .dupla-c { grid-template-columns: 1fr; } }

.lugar-c { display: grid; grid-template-columns: 1fr 1fr 1fr; grid-template-rows: auto auto; gap: 14px; }
.lugar-c .mapa { grid-column: span 2; grid-row: span 2; min-height: 420px; border-radius: var(--r-lg); }
@media (max-width: 900px) { .lugar-c { grid-template-columns: 1fr; } .lugar-c .mapa { grid-column: auto; grid-row: auto; min-height: 300px; } }
'''

def trat(i):
    return TRATAMIENTOS[i]

b, o, p, n, g = TRATAMIENTOS
btns = "".join(f'<button class="pasos-int__btn" data-paso data-estado="{x[2]}"><span>{"0"+str(k+1)}</span><strong>{x[0]}</strong></button>' for k, x in enumerate(PASOS))
dets = "".join(f'<div class="pasos-int__detalle" data-detalle><p>{x[1]}</p></div>' for x in PASOS)
miedos = "".join(f'<button class="miedo" data-miedo="{m[1]}" data-estado="{m[2]}" aria-pressed="{"true" if k == 0 else "false"}">{m[0]}</button>' for k, m in enumerate(MIEDOS))
dg = "".join(f'<span class="dato">{ic(a)}{t}</span>' for a, t in [("sparkles","Limpieza"),("dental","Resinas"),("dental","Extracciones"),("dental","Endodoncia"),("stethoscope","Tercer molar")])

html = cabeza("Dental Díaz · Inicio · Propuesta C", CSS) + nav("C · Tablero") + f'''
<main>
<section class="hero-c">
  <div class="contenedor">
    <div class="bento" data-escalonar>
      <div class="celda c-titulo revela">
        <h1 class="h1-hero" style="font-size: clamp(2.4rem, 1.4rem + 3.4vw, 4.2rem)" data-palabras>Te explicamos <span class="subrayado">todo</span> antes de empezar</h1>
        <p class="lead">Clínica dental familiar en Terán. Revisamos con calma, te enseñamos tus radiografías y tu plan va por escrito.</p>
        <div style="display:flex; flex-wrap:wrap; gap:12px">
          <a class="btn btn--primario" href="#agenda">Agenda tu valoración {ic("arrow-right","flecha")}</a>
          <a class="btn btn--secundario" href="{WA}" target="_blank" rel="noopener">{ic("brand-whatsapp")} Escríbenos</a>
        </div>
      </div>
      <div class="celda celda--foto c-foto revela">{foto("Foto 1 · Hero", "La doctora explicando con la radiografía en pantalla. Vertical.")}</div>
      <div class="celda celda--marino c-nubo revela"><span class="c-nubo__txt">Hola, soy Nubo</span><div class="nubo nubo-asoma" data-nubo="hero" data-mirada aria-label="Nubo asomándose"></div></div>
      <div class="celda c-google revela">{estrellas()}<div><span class="grande">4.9</span><p class="texto chico" style="margin-top: 6px">en Google, de 5 reseñas</p></div></div>
      <div class="celda c-abierto revela"><span class="estado-abierto" data-abierto>Horario</span><p class="texto chico tabular">Lun a vie 10 a 14 y 16 a 20<br>Sábado 10 a 14</p></div>
      <div class="celda celda--marino c-precio revela"><span class="chico" style="font-weight:600">Valoración</span><div><span class="grande">$350</span><p class="chico" style="margin: 6px 0 0">Se descuenta de tu tratamiento</p></div></div>
      <div class="celda c-meses revela"><div style="display:flex; align-items:center; gap:12px"><span class="franja__icono" style="background: var(--crema)">{ic("credit-card")}</span><strong style="font-size: 1.15rem; letter-spacing: -0.015em">Hasta 6 meses sin intereses</strong></div><p class="texto chico">En tratamientos mayores a $6,000. Aplican restricciones.</p><div class="c-meses__bancos"><span>BBVA</span><span>Santander</span><span>Inbursa</span><span>Scotiabank</span><span>Liverpool</span><span>Banorte</span></div></div>
    </div>
  </div>
</section>

<section class="seccion" id="tratamientos" style="padding-top: 0">
  <div class="contenedor">
    <div class="titular revela"><h2 class="h2">Tratamientos</h2></div>
    <div class="bento trat-c" data-escalonar>
      <a class="celda t-blanq revela" href="#">{foto("Foto pendiente", b[5])}<div class="t-blanq__tx"><h3 class="h3" style="margin:0">{b[1]}</h3><p class="texto chico">{b[3]}</p><div class="celda__pie"><span>2 a 3 visitas</span><span class="circulo">{ic("arrow-right")}</span></div></div></a>
      <a class="celda celda--marino t-orto revela" href="#"><div><h3 class="h3" style="margin:0 0 8px">{o[1]}</h3><p class="texto chico" style="max-width: 40ch">{o[3]}</p></div><div class="celda__pie"><span>De 1 a 2 años, control cada mes</span><span class="circulo">{ic("arrow-right")}</span></div></a>
      <a class="celda t-prot revela" href="#"><div><h3 class="h3" style="margin:0 0 8px">{p[1]}</h3><p class="texto chico">Lista en 2 semanas a 1 mes. Pagas en abonos por cita.</p></div><div class="celda__pie"><span>3 a 6 citas</span><span class="circulo">{ic("arrow-right")}</span></div></a>
      <a class="celda t-ninos revela" href="#"><div><h3 class="h3" style="margin:0 0 8px">Niños</h3><p class="chico" style="margin:0">Revisiones con calma, a su ritmo.</p></div><span class="celda__pie"><span class="circulo">{ic("arrow-right")}</span></span><div class="nubo" data-nubo="guina" aria-label="Nubo guiñando"></div></a>
      <div class="celda t-general revela"><div><h3 class="h3" style="margin:0 0 4px">{g[1]}</h3><p class="texto chico">Todo en la misma clínica.</p></div><div class="datos">{dg}</div></div>
    </div>
  </div>
</section>

<section class="seccion" id="primera-visita" style="padding-top: 0">
  <div class="contenedor">
    <div class="visita-c" data-pasos>
      <div class="celda visita-c__pasos revela">
        <div><h2 class="h2" style="margin-bottom: 12px">Así es tu primera visita</h2><span class="dato">{ic("clock")} 45 minutos, $350</span></div>
        <div class="pasos-int" style="margin-top: 32px"><div class="pasos-int__nav"><span class="pasos-int__riel"></span><span class="pasos-int__barra" data-progreso></span>{btns}</div>{dets}</div>
      </div>
      <div class="celda celda--marino visita-c__nubo revela"><div class="nubo" data-nubo="escucha" data-mirada aria-label="Nubo"></div></div>
    </div>
  </div>
</section>

<section class="seccion" id="clinica" style="padding-top: 0">
  <div class="contenedor dupla-c">
    <div class="celda revela" data-miedos>
      <h2 class="h2">Sabemos qué te preocupa</h2>
      <div class="miedos__opciones">{miedos}</div>
      <div style="display:grid; grid-template-columns: 96px 1fr; gap: 14px; align-items: end"><div class="nubo" data-nubo="empatico" aria-label="Nubo"></div><div class="burbuja" data-respuesta aria-live="polite">{MIEDOS[0][1]}</div></div>
    </div>
    <button class="mito revela" data-voltear aria-pressed="false" aria-label="Voltear tarjeta del mito" style="--retraso: 100ms">
      <div class="mito__cara">
        <div class="mito__frente"><span class="mito__pista">{ic("refresh")} Mito o realidad</span><p class="h3" style="margin:0; font-size: clamp(1.5rem, 1.2rem + 1vw, 2rem)">"Con la edad, los dientes se tienen que caer"</p><span class="mito__pista">Toca para ver</span></div>
        <div class="mito__vuelta"><span class="mito__pista">{ic("check")} Mito</span><p style="margin:0; font-size: 1.15rem; line-height: 1.45">Perder dientes no es parte normal de envejecer. Con revisiones y cuidado, te pueden acompañar toda la vida.</p><span class="mito__pista">Más en Nubo explica</span></div>
      </div>
    </button>
  </div>
</section>

<section class="seccion" id="visitanos" style="padding-top: 0">
  <div class="contenedor">
    <div class="titular revela"><h2 class="h2">Visítanos en Terán</h2></div>
    <div class="lugar-c">
      <div class="mapa revela"><iframe src="{MAPA_EMBED}" loading="lazy" title="Mapa de Dental Díaz en Terán" referrerpolicy="no-referrer-when-downgrade"></iframe><a class="mapa__pin" href="{MAPS}" target="_blank" rel="noopener">{ic("navigation")} Cómo llegar</a></div>
      <div class="celda revela"><strong>2da Norte Oriente #438</strong><span class="texto chico">A un costado del parque de Terán, Tuxtla Gutiérrez.</span></div>
      <div class="celda celda--foto revela" style="min-height: 200px">{foto("Foto 3", "Fachada o recepción, horizontal.")}</div>
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

open("../inicio-c.html", "w").write(html)
print("ok C", len(html))
