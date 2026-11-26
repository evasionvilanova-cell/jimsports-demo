# Jim Sports — demo de rediseño (opción A)

Propuesta de rediseño de jimsports.com, no oficial. Web estática, sin dependencias.

- Páginas finales: `*.html` en la raíz (las sirve Vercel con URLs limpias).
- Contenido de cada página: `src/*.html`. Cabecera y pie: `tools/build.py`.
- Tras editar `src/` o `tools/build.py`: `python3 tools/build.py`.
- Las imágenes se cargan desde jimsports.com. Los formularios no envían datos.
- `noindex` activado para que no aparezca en Google.

## Desplegar en Vercel
Add New → Project → importar este repositorio → Framework: *Other* → Deploy.
