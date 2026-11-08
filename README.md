# Dental Díaz · Demo del sitio

Demo estática (HTML, CSS y JS sin build) del sitio institucional de Dental Díaz, hecha por Vortex Digital. Se publica en Netlify sin comando de build, desde la raíz.

## Estructura

- `index.html`: Inicio final (V2 con preocupaciones de V1). Selector de hero Nubo/Fotos solo para la demo; también `?hero=foto`.
- `inicio-a.html`, `inicio-a2.html`, `inicio-b.html`, `inicio-c.html`, `inicio-v1.html`, `inicio-v2.html`: propuestas anteriores, solo referencia.
- `fuente/`: generadores en Python de las páginas (`python3 fuente/inicio_v.py`).
- `base-visual.html`: sistema visual (colores, tipografía, botones, componentes, Nubo, fotografía, movimiento).
- `assets/css/tokens.css`: colores, tipografía, espacios, esquinas y movimiento.
- `assets/css/components.css`: componentes compartidos por todas las páginas.
- `assets/js/nubo.js` y `assets/js/nubo-states.js`: Nubo animado (respira, parpadea, sigue el cursor, saluda). Uso: `<div class="nubo" data-nubo="explica" data-mirada></div>`.
- `assets/js/ui.js`: aparición al hacer scroll, preguntas frecuentes y chips.
- `assets/img/`: símbolo y los 10 estados de Nubo más el hero, en SVG.

## Reglas

- Colores tomados de los SVG del banco de identidad (no del PDF).
- DM Sans para todo; DM Mono solo para datos.
- Textos del sitio de tú. Sin precios de tratamientos; solo la valoración y los paquetes.
