from comun import ic

def cabeza_panel(titulo, panel):
    return f'''<!doctype html>
<html lang="es-MX">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{titulo}</title>
<meta name="robots" content="noindex">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,600;9..40,700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/tokens.css">
<link rel="stylesheet" href="assets/css/components.css">
<link rel="stylesheet" href="assets/css/agenda.css">
<link rel="stylesheet" href="assets/css/panel.css">
</head>
<body class="panel {"pa-body" if panel == "a" else "pb"}" data-panel="{panel}">
'''

def comunes(etiqueta):
    return f'''<div class="velo" id="velo"></div>
<aside class="drawer" id="drawer" aria-hidden="true" aria-label="Ficha del paciente">
  <div class="drawer__top"><span class="mini">Ficha del paciente</span><button class="icono-btn" data-cerrar-drawer aria-label="Cerrar">{ic("x")}</button></div>
  <div class="drawer__cuerpo" data-drawer-cuerpo></div>
</aside>
<div class="toast" id="toast" role="status" aria-live="polite"></div>
<script src="assets/js/iconos.js"></script>
<script src="assets/js/nubo-states.js"></script>
<script src="assets/js/nubo.js"></script>
<script src="assets/js/panel.js"></script>
</body>
</html>
'''

ITEMS_A = [("resumen", "layout-dashboard", "Resumen"), ("agenda", "calendar-week", "Agenda"), ("pacientes", "users-group", "Pacientes"),
           ("ligas", "link", "Ligas"), ("comision", "receipt-2", "Comisión"), ("pendientes", "checklist", "Pendientes"), ("contenido", "pencil", "Contenido")]

def panel_a():
    nav = "".join(f'<a class="lateral__item" href="#{k}" data-ir="{k}">{ic(i)}<span>{t}</span>{"<span class=cuenta>5</span>" if k == "pendientes" else ""}</a>' for k, i, t in ITEMS_A)
    return cabeza_panel("Panel · Dental Díaz", "a") + f'''<div class="pa">
  <aside class="lateral" aria-label="Menú del panel">
    <a class="logo" href="index.html"><img src="assets/img/simbolo-marino.svg" alt=""><span>Dental Díaz</span></a>
    <nav>{nav}</nav>
    <div class="lateral__pie"><span class="avatar">MD</span><div><strong>Dra. Díaz</strong><small>Administradora</small></div></div>
  </aside>
  <div class="lateral-velo" data-menu-lateral></div>
  <main class="pa__main">
    <header class="pa__top">
      <button class="icono-btn btn-menu" data-menu-lateral aria-label="Abrir menú">{ic("menu-2")}</button>
      <div><h1 data-vista-titulo>Resumen</h1><span class="mini" data-fecha-hoy></span></div>
      <div class="pa__top-der"><span class="demo-chip">Propuesta A<span class="solo-escritorio"> · datos de ejemplo</span></span><span class="avatar">MD</span></div>
    </header>
    <div data-vista-cuerpo></div>
  </main>
</div>
''' + comunes("A")

TABS_B = [("hoy", "sun", "Hoy"), ("agenda", "calendar-week", "Agenda"), ("pacientes", "layout-kanban", "Pacientes")]
MAS_B = [("ligas", "link", "Ligas"), ("comision", "receipt-2", "Comisión"), ("pendientes", "checklist", "Pendientes"), ("contenido", "pencil", "Contenido")]

def panel_b():
    tabs = "".join(f'<a class="pb__tab" href="#{k}" data-ir="{k}">{ic(i)}{t}</a>' for k, i, t in TABS_B + MAS_B)
    barra = "".join(f'<a href="#{k}" data-ir="{k}">{ic(i)}<span>{t}</span></a>' for k, i, t in TABS_B)
    mas = "".join(f'<a href="#{k}" data-ir="{k}">{ic(i)}{t}</a>' for k, i, t in MAS_B)
    return cabeza_panel("Panel · Dental Díaz", "b") + f'''<header class="pb__top">
  <div class="pb__top-in">
    <a class="logo" href="index.html"><img src="assets/img/simbolo-marino.svg" alt=""><span>Dental Díaz</span></a>
    <nav class="pb__tabs" aria-label="Secciones">{tabs}</nav>
    <div class="pb__top-der"><span class="demo-chip">Propuesta B<span class="solo-escritorio"> · datos de ejemplo</span></span><span class="avatar">MD</span></div>
  </div>
</header>
<main class="pb__main">
  <h1 class="pb__titulo" data-vista-titulo>Hoy</h1>
  <div data-vista-cuerpo></div>
</main>
<div class="mas-hoja" role="menu">{mas}</div>
<nav class="tabbar" aria-label="Secciones">{barra}<button type="button" data-mas>{ic("dots")}<span>Más</span></button></nav>
''' + comunes("B")

if __name__ == "__main__":
    for nombre, html in (("panel-a.html", panel_a()), ("panel-b.html", panel_b())):
        open("../" + nombre, "w").write(html)
        print("ok", nombre, len(html))
