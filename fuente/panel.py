from comun import ic

NAV = [
    ("Día a día", [("hoy", "sun", "Hoy"), ("agenda", "calendar-week", "Agenda"), ("pacientes", "layout-kanban", "Pacientes")]),
    ("Negocio", [("resumen", "chart-bar", "Resumen"), ("cobros", "credit-card", "Cobros"), ("comision", "receipt-2", "Comisión"), ("ligas", "link", "Ligas")]),
    ("Sitio", [("contenido", "pencil", "Contenido"), ("pendientes", "checklist", "Pendientes")]),
    ("Cuenta", [("equipo", "users-group", "Equipo")]),
]
BASICAS = ("hoy", "agenda", "pacientes")

def item(k, i, t, cls):
    extra = "" if k in BASICAS else " data-solo-admin"
    cuenta = '<span class="cuenta">5</span>' if k == "pendientes" else ""
    return f'<a class="{cls}" href="#{k}" data-ir="{k}"{extra}>{ic(i)}<span>{t}</span>{cuenta}</a>'

def html():
    lateral = "".join(f'<div class="lateral__grupo"><span class="lateral__etq">{g}</span>' + "".join(item(k, i, t, "lateral__item") for k, i, t in its) + "</div>" for g, its in NAV)
    barra = "".join(item(k, i, t, "") for k, i, t in NAV[0][1])
    mas = "".join(item(k, i, t, "") for _, its in NAV[1:] for k, i, t in its)
    return f'''<!doctype html>
<html lang="es-MX">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Panel · Dental Díaz</title>
<meta name="robots" content="noindex">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,600;9..40,700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/tokens.css">
<link rel="stylesheet" href="assets/css/components.css">
<link rel="stylesheet" href="assets/css/agenda.css">
<link rel="stylesheet" href="assets/css/panel.css">
</head>
<body class="panel">
<div class="pa">
  <aside class="lateral" aria-label="Menú del panel">
    <a class="logo" href="index.html"><img src="assets/img/simbolo-marino.svg" alt=""><span>Dental Díaz</span></a>
    <nav>{lateral}</nav>
    <div class="lateral__pie"><span class="avatar">MD</span><div><strong>Dra. Díaz</strong><small>Administradora</small></div></div>
  </aside>
  <main class="pa__main">
    <header class="pa__top">
      <a class="logo solo-movil-flex" href="index.html"><img src="assets/img/simbolo-marino.svg" alt=""></a>
      <div class="pa__titulo"><h1 data-vista-titulo>Hoy</h1><span class="mini" data-fecha-hoy></span></div>
      <div class="pa__top-der">
        <label class="ver-como"><span>Ver como</span><select data-rol><option value="admin">Administración</option><option value="recepcion">Recepción</option><option value="vortex">Vortex</option></select></label>
        <span class="demo-chip">Datos de ejemplo</span>
      </div>
    </header>
    <div data-vista-cuerpo></div>
  </main>
</div>
<div class="mas-hoja" role="menu">{mas}</div>
<nav class="tabbar" aria-label="Secciones">{barra}<button type="button" data-mas>{ic("dots")}<span>Más</span></button></nav>
<div class="velo" id="velo"></div>
<aside class="drawer" id="drawer" aria-hidden="true" aria-label="Ficha del paciente">
  <div class="drawer__top"><span class="mini">Ficha del paciente</span><button class="icono-btn" data-cerrar-drawer aria-label="Cerrar">{ic("x")}</button></div>
  <div class="drawer__cuerpo" data-drawer-cuerpo></div>
</aside>
<div class="modal" id="modal" role="dialog" aria-modal="true" aria-hidden="true">
  <div class="modal__top"><h2 data-modal-titulo></h2><button class="icono-btn" data-cerrar-modal aria-label="Cerrar">{ic("x")}</button></div>
  <div class="modal__cuerpo" data-modal-cuerpo></div>
  <div class="modal__pie"><button class="btn btn--chico btn--secundario" data-cerrar-modal>Cancelar</button><button class="btn btn--chico btn--primario" data-modal-ok>Guardar</button></div>
</div>
<div class="toast" id="toast" role="status" aria-live="polite"></div>
<script src="assets/js/iconos.js"></script>
<script src="assets/js/nubo-states.js"></script>
<script src="assets/js/nubo.js"></script>
<script src="assets/js/panel.js"></script>
</body>
</html>
'''

if __name__ == "__main__":
    h = html()
    open("../panel.html", "w").write(h)
    print("ok panel.html", len(h))
