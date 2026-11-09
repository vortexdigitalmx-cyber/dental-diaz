import propuesta_a as pa
from comun import *

def seccion(html, marcador):
    i = html.index(marcador)
    ini = html.rindex('<section', 0, i)
    fin = html.index('</section>', i) + len('</section>')
    return html[ini:fin]

H, H2 = pa.html, pa.html2
hero = H2[H2.index('<section class="hero-n">'):H2.index('</section>', H2.index('<section class="franja-sec">')) + len('</section>')]
trat = seccion(H, 'id="tratamientos"')
historia = seccion(H, 'id="primera-visita"')
doctora = seccion(H, 'id="clinica"')
mito = seccion(H, 'class="contenedor mito-a"')
visitanos = seccion(H, 'id="visitanos"')
cierre = seccion(H, 'class="cierre revela"').replace('id="agenda"', 'id="cierre"')
historia_script = H[H.index('<script>window.HISTORIA'):H.index('</script>', H.index('<script>window.HISTORIA')) + len('</script>')]

RESENAS = [
    ("Marcela Clemente", "MC", "Excelente espacio, son todas muy respetuosos, me encanta su profesionalismo…"),
    ("Ague Morales", "AM", "Excelente trato al paciente."),
    ("Araceli Chacon", "AC", "Muy buen trato la verda muy satisfecho."),
    (None, "", "Reseña pendiente: se copia tal cual del perfil de Google."),
    (None, "", "Reseña pendiente: se copia tal cual del perfil de Google."),
]
GALERIA = [
    ("Recepción", "Horizontal, luz natural, sin gente."),
    ("Consultorio", "Los dos sillones con la luz encendida."),
    ("Radiografía digital", "Monitor con una radiografía, sin datos del paciente."),
    ("Sala de espera", "Desde la entrada, ordenada."),
    ("Fachada", "Con el logo nuevo cuando esté instalado."),
    ("Detalle", "Un rincón de la recepción con buena luz."),
]

CSS_V = pa.CSS + '''
.hero-n { min-height: calc(100svh - 76px); }
@media (max-width: 960px) { .hero-n { min-height: calc(100svh - 64px); } }
.franja-sec .franja { margin-top: 0; }

.banda { position: relative; padding-block: clamp(64px, 9vw, 120px); margin-block: clamp(24px, 4vw, 56px); background: var(--lavanda); }
.banda::before, .banda::after { content: ""; position: absolute; left: 0; right: 0; height: 40px; background: var(--crema); }
.banda::before { top: -1px; border-radius: 0 0 50% 50% / 0 0 100% 100%; }
.banda::after { bottom: -1px; border-radius: 50% 50% 0 0 / 100% 100% 0 0; }
.banda .miedo { background: var(--marfil); border-color: transparent; }
.banda .miedo[aria-pressed="true"] { background: var(--marino); }
.circulo-nubo { display: grid; place-items: center; aspect-ratio: 1; border-radius: 50%; background: var(--marfil); }

.resenas { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 16px; }
.resena-c { display: grid; gap: 14px; align-content: space-between; padding: 26px; border-radius: var(--r-lg); background: var(--marfil); border: 1px solid var(--linea); min-height: 220px; }
.resena-c p { margin: 0; font-size: 1.1rem; line-height: 1.5; letter-spacing: -0.005em; }
.resena-c--pendiente { background: transparent; border-style: dashed; border-color: var(--linea-fuerte); }
.resena-c--pendiente p { color: var(--texto-suave); font-size: 0.9375rem; }
.resena-c__autor { display: flex; align-items: center; gap: 12px; }
.resena-c__autor .avatar { width: 40px; height: 40px; border-radius: 50%; background: var(--lavanda); display: grid; place-items: center; font-weight: 700; font-size: 0.875rem; }
.resena-c__autor small { display: block; color: var(--texto-suave); font-size: 0.8125rem; }
.resenas-cab { display: flex; flex-wrap: wrap; justify-content: space-between; align-items: end; gap: 20px; margin-bottom: clamp(28px, 4vw, 48px); }
.resenas-cab__nota { display: flex; align-items: center; gap: 16px; }
.resenas-cab__nota strong { font-size: clamp(3rem, 2rem + 3vw, 4.5rem); font-weight: 700; letter-spacing: -0.05em; line-height: 0.9; }
@media (max-width: 900px) { .resenas { grid-template-columns: 1fr; } }
'''

CSS_V1 = CSS_V + '''
.trat-a { align-items: stretch; }
.trat-a .selector-tx__lista { align-content: space-between; }
.trat-a .selector-tx__tab { padding: 14px 20px; }
.trat-a__panel { height: 100%; align-content: start; }
.trat-a__panel .foto { aspect-ratio: 16 / 8; }

.miedos-v1 { display: grid; grid-template-columns: 1fr 1fr; gap: clamp(28px, 5vw, 72px); align-items: center; }
.miedos-v1__conversa { display: grid; grid-template-columns: 300px 1fr; gap: 16px; align-items: end; }
.miedos-v1__conversa .circulo-nubo .nubo { width: 82%; }
.miedos-v1 .burbuja { margin-bottom: 40%; }
@media (max-width: 900px) { .miedos-v1 { grid-template-columns: 1fr; } .miedos-v1__conversa { grid-template-columns: 1fr; justify-items: center; } .miedos-v1__conversa .circulo-nubo { width: 200px; } .miedos-v1 .burbuja { margin-bottom: 0; min-height: 0; border-radius: 24px; } }

.galeria-v1 { display: grid; grid-template-columns: 1.4fr 1fr 1fr; grid-template-rows: 240px 240px; gap: 14px; }
.galeria-v1 .foto { height: 100%; border-radius: var(--r-lg); }
.galeria-v1 .g1 { grid-row: span 2; }
.galeria-v1 .g4, .galeria-v1 .g5 { grid-row: 2; }
@media (max-width: 900px) { .galeria-v1 { grid-template-columns: 1fr 1fr; grid-template-rows: none; grid-auto-rows: 180px; } .galeria-v1 .g1 { grid-column: span 2; grid-row: auto; } .galeria-v1 .g4, .galeria-v1 .g5 { grid-row: auto; } }
'''

CSS_V2 = CSS_V + '''
.trat-v2__tabs { display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 20px; }
.trat-v2__tabs .selector-tx__tab { width: auto; padding: 12px 22px; border-radius: var(--r-pill); border: 1.5px solid var(--linea-fuerte); background: transparent; }
.trat-v2__tabs .selector-tx__tab strong { font-size: 1rem; letter-spacing: -0.01em; }
.trat-v2__tabs .selector-tx__tab small, .trat-v2__tabs .selector-tx__tab .i { display: none; }
.trat-v2__tabs .selector-tx__tab[aria-selected="true"] { background: var(--marino); border-color: var(--marino); color: var(--marfil); }
.trat-v2__panel { grid-template-columns: 1.1fr 0.9fr; gap: clamp(20px, 3vw, 40px); align-items: center; padding: 14px; border-radius: var(--r-xl); background: var(--marfil); border: 1px solid var(--linea); }
.trat-v2__panel .foto { aspect-ratio: 4 / 3; border-radius: calc(var(--r-xl) - 10px); }
.trat-v2__tx { display: grid; gap: 16px; padding: 12px clamp(8px, 2vw, 24px); }
.trat-v2__tx .h2 { margin: 0; }
@media (max-width: 900px) {
  .trat-v2__tabs { flex-wrap: nowrap; overflow-x: auto; margin-inline: calc(var(--gutter) * -1); padding-inline: var(--gutter); scrollbar-width: none; }
  .trat-v2__tabs .selector-tx__tab { flex: none; }
  .trat-v2__panel { grid-template-columns: 1fr; }
}

.miedos-v2 { display: grid; grid-template-columns: 1fr minmax(280px, 400px) 1fr; gap: clamp(20px, 3vw, 40px); align-items: center; }
.miedos-v2__col { display: grid; gap: 16px; }
.miedo-c { display: grid; gap: 10px; text-align: left; padding: 22px; border-radius: var(--r-lg); border: 0; background: var(--marfil); cursor: pointer; transition: transform var(--dur-base) var(--ease-out), background var(--dur-base), color var(--dur-base), box-shadow var(--dur-base); }
.miedo-c .i { width: 28px; height: 28px; color: var(--lavanda-sombra); }
.miedo-c strong { font-size: 1.15rem; letter-spacing: -0.015em; }
.miedo-c:hover { transform: translateY(-3px); box-shadow: var(--sombra-suave); }
.miedo-c[aria-pressed="true"] { background: var(--marino); color: var(--marfil); }
.miedo-c[aria-pressed="true"] .i { color: var(--lavanda); }
.miedos-v2__centro { display: grid; gap: 18px; justify-items: center; text-align: center; }
.miedos-v2__centro .circulo-nubo { width: 100%; }
.miedos-v2__centro .circulo-nubo .nubo { width: 80%; }
.miedos-v2__centro .burbuja { min-height: 6em; border-radius: 24px; text-align: left; }
.miedos-v2__titulo { text-align: center; margin: 0 auto clamp(32px, 4vw, 56px); max-width: 640px; }
@media (max-width: 900px) {
  .miedos-v2 { grid-template-columns: 1fr 1fr; }
  .miedos-v2__centro { grid-column: span 2; order: -1; }
  .miedos-v2__centro .circulo-nubo { width: 220px; }
  .miedos-v2__col { display: contents; }
}

.galeria-v2 { display: flex; gap: 14px; overflow-x: auto; scroll-snap-type: x mandatory; padding-bottom: 8px; margin-inline: calc(var(--gutter) * -1); padding-inline: var(--gutter); scrollbar-width: none; cursor: grab; }
.galeria-v2::-webkit-scrollbar { display: none; }
.galeria-v2 .foto { flex: none; width: clamp(260px, 32vw, 440px); aspect-ratio: 4 / 5; border-radius: var(--r-lg); scroll-snap-align: start; }
.galeria-v2 .foto:nth-child(even) { aspect-ratio: 4 / 4.2; align-self: end; }
.galeria-nav { display: flex; gap: 8px; }

.marquesina { overflow: hidden; mask-image: linear-gradient(90deg, transparent, #000 8%, #000 92%, transparent); }
.marquesina__pista { display: flex; gap: 16px; width: max-content; animation: marquesina 48s linear infinite; }
.marquesina:hover .marquesina__pista, .marquesina:focus-within .marquesina__pista { animation-play-state: paused; }
.marquesina .resena-c { width: 360px; flex: none; }
@keyframes marquesina { to { transform: translateX(calc(-50% - 8px)); } }
@media (prefers-reduced-motion: reduce) { .marquesina { overflow-x: auto; } .marquesina__pista { animation: none; } }
'''

def resena_card(r):
    nombre, ini, texto = r
    if not nombre:
        return f'<div class="resena-c resena-c--pendiente">{ic("brand-google")}<p>{texto}</p></div>'
    return f'<figure class="resena-c" style="margin:0">{estrellas()}<blockquote style="margin:0"><p>"{texto}"</p></blockquote><figcaption class="resena-c__autor"><span class="avatar">{ini}</span><span><strong>{nombre}</strong><small>Reseña de Google</small></span></figcaption></figure>'

def resenas_cab():
    return f'''<div class="resenas-cab revela"><div><h2 class="h2">Lo que dicen nuestros pacientes</h2></div>
<div class="resenas-cab__nota"><strong>4.9</strong><div>{estrellas()}<p class="texto chico" style="margin:4px 0 0">5 reseñas en Google</p></div></div></div>'''

def resenas_v1():
    cards = "".join(resena_card(r) for r in RESENAS[:3])
    return f'''<section class="seccion" style="padding-top: 0"><div class="contenedor">{resenas_cab()}<div class="resenas revela" data-escalonar>{cards}</div>
<p class="texto chico" style="margin-top: 16px">Las otras 2 reseñas se agregan tal cual del perfil de Google.</p></div></section>'''

def resenas_v2():
    cards = "".join(resena_card(r) for r in RESENAS[:3]) * 2
    return f'''<section class="seccion" style="padding-top: 0"><div class="contenedor">{resenas_cab()}</div>
<div class="marquesina revela" tabindex="0" aria-label="Reseñas de Google"><div class="marquesina__pista">{cards}{cards.replace('<figure', '<figure aria-hidden="true"').replace('<div class="resena-c', '<div aria-hidden="true" class="resena-c')}</div></div></section>'''

def galeria_v1():
    fotos = "".join(f'<div class="g{i+1} revela">{foto(t, d)}</div>' for i, (t, d) in enumerate(GALERIA[:5]))
    return f'''<section class="seccion" style="padding-top: 0"><div class="contenedor">
<div class="titular revela"><h2 class="h2">Así es la clínica</h2><p class="texto">Para que la conozcas antes de venir.</p></div>
<div class="galeria-v1">{fotos}</div></div></section>'''

def galeria_v2():
    fotos = "".join(foto(t, d, "revela") for t, d in GALERIA)
    return f'''<section class="seccion" style="padding-top: 0"><div class="contenedor">
<div class="resenas-cab revela"><div><h2 class="h2">Así es la clínica</h2><p class="texto" style="margin-top: 12px; font-size: var(--fs-lead)">Para que la conozcas antes de venir.</p></div>
<div class="galeria-nav"><button class="icono-btn" data-galeria="-1" aria-label="Anterior"><svg class="i" aria-hidden="true" style="transform: scaleX(-1)"><use href="#i-arrow-right"/></svg></button><button class="icono-btn" data-galeria="1" aria-label="Siguiente">{ic("arrow-right")}</button></div></div>
<div class="galeria-v2" data-galeria-pista>{fotos}</div></div></section>'''

def miedos_v1():
    ops = "".join(f'<button class="miedo" data-miedo="{m[1]}" data-estado="{m[2]}" aria-pressed="{"true" if i == 0 else "false"}">{m[0]}</button>' for i, m in enumerate(MIEDOS))
    return f'''<section class="banda" id="preocupaciones"><div class="contenedor miedos-v1" data-miedos>
<div class="revela"><h2 class="h2">Sabemos qué te preocupa</h2><p class="texto" style="margin: 16px 0 28px; font-size: var(--fs-lead); max-width: 38ch; color: var(--marino)">Toca lo que más te pesa. Nubo te cuenta cómo lo cuidamos.</p><div class="miedos__opciones">{ops}</div></div>
<div class="miedos-v1__conversa revela" style="--retraso: 120ms"><div class="circulo-nubo"><div class="nubo" data-nubo="empatico" data-mirada aria-label="Nubo"></div></div><div class="burbuja" data-respuesta aria-live="polite">{MIEDOS[0][1]}</div></div>
</div></section>'''

ICONOS_MIEDO = ["mood-smile", "receipt-2", "scan", "heart-handshake"]
def miedos_v2():
    def card(i):
        m = MIEDOS[i]
        return f'<button class="miedo-c revela" data-miedo="{m[1]}" data-estado="{m[2]}" aria-pressed="{"true" if i == 0 else "false"}">{ic(ICONOS_MIEDO[i])}<strong>{m[0]}</strong></button>'
    return f'''<section class="banda" id="preocupaciones"><div class="contenedor" data-miedos>
<div class="miedos-v2__titulo revela"><h2 class="h2">Sabemos qué te preocupa</h2><p class="texto" style="margin-top: 14px; font-size: var(--fs-lead); color: var(--marino)">Toca lo que más te pesa.</p></div>
<div class="miedos-v2"><div class="miedos-v2__col">{card(0)}{card(1)}</div>
<div class="miedos-v2__centro revela"><div class="circulo-nubo"><div class="nubo" data-nubo="empatico" data-mirada aria-label="Nubo"></div></div><div class="burbuja" data-respuesta aria-live="polite">{MIEDOS[0][1]}</div></div>
<div class="miedos-v2__col">{card(2)}{card(3)}</div></div></div></section>'''

def trat_v2():
    tabs = "".join(f'<button class="selector-tx__tab" role="tab" data-tab="{t[0]}" aria-selected="{"true" if i == 0 else "false"}" tabindex="{0 if i == 0 else -1}"><span><strong>{t[1]}</strong><small></small></span>{ic("arrow-right")}</button>' for i, t in enumerate(TRATAMIENTOS))
    pan = ""
    for i, t in enumerate(TRATAMIENTOS):
        datos = "".join(f'<span class="dato">{ic(a)}{b}</span>' for a, b in t[4])
        pan += f'''<div class="selector-tx__panel trat-v2__panel{" activo" if i == 0 else ""}" role="tabpanel" data-panel="{t[0]}">{foto("Foto pendiente", t[5])}
<div class="trat-v2__tx"><h3 class="h2">{t[1]}</h3><p class="texto" style="font-size: var(--fs-lead)">{t[3]}</p><div class="datos">{datos}</div>
<div style="display:flex; flex-wrap: wrap; gap: 12px; margin-top: 8px"><a class="btn btn--primario btn--chico" href="#agenda">Agenda tu valoración</a><a class="enlace" href="#">Conoce el tratamiento {ic("arrow-right")}</a></div></div></div>'''
    return f'''<section class="seccion" id="tratamientos"><div class="contenedor"><div class="titular revela"><h2 class="h2">¿Qué necesitas hoy?</h2></div>
<div data-selector><div class="trat-v2__tabs revela" role="tablist" aria-label="Tratamientos">{tabs}</div><div class="revela">{pan}</div></div></div></section>'''

GALERIA_JS = '''<script>
document.querySelectorAll('[data-galeria]').forEach(function (b) {
  b.addEventListener('click', function () {
    var p = document.querySelector('[data-galeria-pista]');
    p.scrollBy({ left: (+b.getAttribute('data-galeria')) * p.firstElementChild.getBoundingClientRect().width * 1.05, behavior: 'smooth' });
  });
});
(function () {
  var p = document.querySelector('[data-galeria-pista]'); if (!p) return;
  var x0 = 0, s0 = 0, down = false;
  p.addEventListener('pointerdown', function (e) { if (e.pointerType !== 'mouse') return; down = true; x0 = e.clientX; s0 = p.scrollLeft; p.style.scrollSnapType = 'none'; p.style.cursor = 'grabbing'; });
  window.addEventListener('pointerup', function () { if (!down) return; down = false; p.style.scrollSnapType = ''; p.style.cursor = ''; });
  p.addEventListener('pointermove', function (e) { if (down) p.scrollLeft = s0 - (e.clientX - x0); });
})();
</script>'''

def armar(css, tag, cuerpo, archivo, extra_js=""):
    html = cabeza(f"Dental Díaz · Inicio · {tag}", css) + nav(tag) + "<main>\n" + cuerpo + "\n</main>\n" + historia_script + extra_js + pie()
    open(archivo, "w").write(html)
    print("ok", archivo, len(html))

v1 = "\n".join([hero, trat, historia, agenda_html(pasos=False), miedos_v1(), doctora, galeria_v1(), mito, resenas_v1(), visitanos, cierre])
v2 = "\n".join([hero, trat_v2(), historia, agenda_html(pasos=True), miedos_v2(), doctora, galeria_v2(), resenas_v2(), mito, visitanos, cierre])
armar(CSS_V1, "V1 · Ajustes", v1, "../inicio-v1.html")
armar(CSS_V2, "V2 · Propuesta completa", v2, "../inicio-v2.html", GALERIA_JS)

# ---------- Versión final: V2 + preocupaciones de V1 + selector de hero ----------
hero_n_sola = hero[:hero.index('<section class="franja-sec">')]
hero_a = seccion(H, '<section class="hero-a">'.replace('<section ', '')) if False else H[H.index('<section class="hero-a">'):H.index('</section>', H.index('<section class="hero-a">')) + len('</section>')]
hero_a = hero_a[:hero_a.index('<div class="contenedor">\n    <div class="franja revela"')] + '</section>'
hero_a = hero_a.replace('<section class="hero-a">', '<section class="hero-a" data-hero="foto" hidden>')
hero_n_sola = hero_n_sola.replace('<section class="hero-n">', '<section class="hero-n" data-hero="nubo">')
hero_n_sola = hero_n_sola.replace('<div class="hero-n__nubo">', '<div class="hero-n__nubo"><div class="hero-n__figura">').replace('<span>Se descuenta de tu tratamiento</span></div></div>\n  </div>\n</section>', '<span>Se descuenta de tu tratamiento</span></div></div>\n  </div></div>\n</section>')

CONFIANZA = [("map-pin", "Desde 2021 en Terán", "A un costado del parque"), ("scan", "Radiografía digital", "Incluida en tu valoración"), ("credit-card", "Hasta 6 meses sin intereses", "Aplican restricciones"), ("file-text", "Precio por escrito", "Antes de empezar")]
confianza = '<section class="confianza"><div class="contenedor"><ul class="confianza__lista revela" data-escalonar>' + "".join(
    f'<li><span class="confianza__icono">{ic(a)}</span><span><strong>{b}</strong><small>{c}</small></span></li>' for a, b, c in CONFIANZA) + '</ul></div></section>'

CSS_F = CSS_V2 + CSS_V1[len(CSS_V):] + '''
.confianza { position: relative; z-index: 3; margin-top: -1px; }
.confianza__lista { list-style: none; margin: 0; padding: 10px; display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 8px; border-radius: var(--r-xl); background: var(--marino); color: var(--marfil); box-shadow: var(--sombra-flotante); }
.confianza__lista li { display: flex; align-items: center; gap: 14px; padding: 16px 18px; border-radius: calc(var(--r-xl) - 8px); transition: background var(--dur-base); }
.confianza__lista li:hover { background: rgba(250, 248, 243, 0.06); }
.confianza__icono { width: 46px; height: 46px; flex: none; border-radius: 16px; display: grid; place-items: center; background: var(--lavanda); color: var(--marino); }
.confianza__icono .i { width: 24px; height: 24px; }
.confianza strong { display: block; font-size: 1rem; line-height: 1.2; letter-spacing: -0.01em; }
.confianza small { display: block; margin-top: 2px; font-size: 0.8125rem; color: rgba(250, 248, 243, 0.7); }
[data-hero="nubo"] + [data-hero="foto"] + .confianza .confianza__lista { margin-top: -28px; }
@media (max-width: 960px) { .confianza__lista { grid-template-columns: 1fr 1fr; } [data-hero="nubo"] + [data-hero="foto"] + .confianza .confianza__lista { margin-top: 0; } }
@media (max-width: 420px) { .confianza__lista li { padding: 12px; gap: 10px; } .confianza__icono { width: 38px; height: 38px; border-radius: 12px; } }

[data-hero][hidden] { display: none !important; }
.hero-n { height: calc(100svh - 76px); min-height: 600px; max-height: 1100px; padding-bottom: 0; }
.hero-n__nubo { position: relative; align-self: stretch; justify-self: stretch; width: auto; min-height: 150px; margin-top: clamp(16px, 2.5vw, 32px); }
.hero-n__figura { position: absolute; left: 50%; bottom: 0; height: 100%; aspect-ratio: 310 / 147; max-width: 112vw; transform: translateX(-50%); }
.hero-n__figura .nubo { width: 100%; height: 100%; }
.hero-n__figura .nubo svg { width: 100%; height: 100%; }
.hero-n .chip-flota.uno { right: 90%; left: auto; top: 18%; }
.hero-n .chip-flota.dos { left: 90%; right: auto; top: 46%; }
[data-hero="nubo"] + [data-hero="foto"] + .confianza .confianza__lista { margin-top: 0 !important; }
.confianza { padding-top: clamp(20px, 3vw, 32px); }
.hero-a { min-height: calc(100svh - 76px); display: grid; align-items: center; padding-block: clamp(16px, 3vh, 40px); }
.hero-a .h1-hero { font-size: clamp(2.5rem, 1.4rem + 3vw, 4.3rem); }
.hero-a__media .foto { aspect-ratio: auto; height: clamp(340px, calc(100svh - 300px), 640px); }
.hero-a__nubo { width: 34%; }
@media (max-width: 900px) { .hero-a { min-height: 0; } .hero-a__media { order: -1; max-width: 420px; } .hero-a__media .foto { height: auto; aspect-ratio: 4 / 3.6; } .hero-a__grid { gap: 28px; } }

#preocupaciones.banda { padding-block: clamp(56px, 6vw, 88px); }
.miedos-v2 { grid-template-columns: 1fr minmax(240px, 300px) 1fr; align-items: center; }
.miedos-v2__titulo { margin-bottom: clamp(24px, 3vw, 40px); }
.miedos-v2__centro { gap: 14px; }
.miedos-v2__centro .circulo-nubo { width: min(100%, 280px); }
.miedos-v2__centro .burbuja { min-height: 0; font-size: 1.05rem; padding: 18px 20px; }
@media (max-width: 900px) { .miedos-v2 { grid-template-columns: 1fr 1fr; gap: 12px; } .miedos-v2__centro .circulo-nubo { width: 200px; } .miedo-c { padding: 16px; } .miedo-c strong { font-size: 1rem; } }
@media (max-width: 960px) { .hero-n .chip-flota.uno { right: auto; left: 6%; top: -6%; } .hero-n .chip-flota.dos { display: none; } }
.selector-hero { position: fixed; left: 16px; bottom: 16px; z-index: 70; display: flex; align-items: center; gap: 4px; padding: 4px 4px 4px 14px; border-radius: 999px; background: var(--marino); color: var(--marfil); box-shadow: var(--sombra-flotante); font-size: 0.8125rem; font-weight: 600; }
.selector-hero button { border: 0; cursor: pointer; padding: 8px 14px; border-radius: 999px; background: transparent; color: rgba(250, 248, 243, 0.75); font-size: 0.8125rem; font-weight: 600; }
.selector-hero button[aria-pressed="true"] { background: var(--marfil); color: var(--marino); }
@media (max-width: 960px) { .selector-hero { bottom: auto; top: 72px; left: auto; right: 12px; padding: 3px; } .selector-hero > span { display: none; } .selector-hero button { padding: 6px 12px; } .hero-n { height: calc(100svh - 64px - 84px); min-height: 540px; padding-top: 64px; } .hero-a { padding-top: 64px; } }
'''

SELECTOR = '''<div class="selector-hero" role="group" aria-label="Elegir hero (solo demo)"><span>Hero</span><button type="button" data-elegir-hero="nubo" aria-pressed="true">Nubo</button><button type="button" data-elegir-hero="foto" aria-pressed="false">Fotos</button></div>
<script>
(function () {
  var botones = document.querySelectorAll('[data-elegir-hero]');
  function elegir(cual, guardar) {
    document.querySelectorAll('[data-hero]').forEach(function (s) {
      var on = s.getAttribute('data-hero') === cual;
      if (on && s.hidden) {
        s.hidden = false;
        s.querySelectorAll('.palabras-listas').forEach(function (h) { h.classList.remove('palabras-listas'); void h.offsetWidth; h.classList.add('palabras-listas'); });
        s.querySelectorAll('.nubo-asoma, .chip-flota').forEach(function (n) { n.style.animation = 'none'; void n.offsetWidth; n.style.animation = ''; });
      } else if (!on) { s.hidden = true; }
    });
    botones.forEach(function (b) { b.setAttribute('aria-pressed', b.getAttribute('data-elegir-hero') === cual ? 'true' : 'false'); });
    if (guardar) { try { localStorage.setItem('dd-hero', cual); } catch (e) {} }
  }
  botones.forEach(function (b) { b.addEventListener('click', function () { elegir(b.getAttribute('data-elegir-hero'), true); }); });
  var inicial = 'nubo';
  try { inicial = new URLSearchParams(location.search).get('hero') || localStorage.getItem('dd-hero') || 'nubo'; } catch (e) {}
  if (inicial === 'foto') elegir('foto', false);
})();
</script>'''

import re as _re
def _limpiar_chips(t):
    t = _re.sub(r'<div class="chip-flota dos">.*?</div></div>', '', t, flags=_re.S)
    return t.replace('<div><strong>4.9 en Google</strong><span>5 reseñas</span></div>', '<div><strong>4.9 en Google</strong></div>')
hero_n_sola = _limpiar_chips(hero_n_sola)
hero_a = _limpiar_chips(hero_a)
final = "\n".join([hero_n_sola, hero_a, confianza, trat_v2(), historia, agenda_html(pasos=True), miedos_v2(), doctora, galeria_v2(), resenas_v2(), mito, visitanos, cierre])
html_f = cabeza("Dental Díaz · Clínica dental familiar en Terán, Tuxtla", CSS_F) + nav("final") + "<main>\n" + final + "\n</main>\n" + historia_script + GALERIA_JS + SELECTOR + pie()
html_f = html_f.replace('<div class="propuesta-tag">Propuesta final</div>\n', '')
open("../index.html", "w").write(html_f)
print("ok index", len(html_f))
