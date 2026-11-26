"""Genera las páginas HTML finales a partir de src/*.html (solo el contenido).
Uso: python3 tools/build.py
Cada archivo de src empieza con una línea de metadatos:
<!-- title: ... | desc: ... | nav: marcas -->
"""
import pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
U = "https://jimsports.com/wp-content/uploads"

NAV = [
    ("marcas", "/marcas", "Marcas"),
    ("catalogos", "/catalogos", "Catálogos"),
    ("crea-tu-marca", "/crea-tu-marca", "Crea tu marca"),
    ("nosotros", "/nosotros", "Nosotros"),
    ("rsc", "/rsc", "Compromiso"),
    ("noticias", "/noticias", "Noticias"),
    ("contacto", "/contacto", "Contacto"),
]

SEARCH_ICON = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#555" stroke-width="2" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/></svg>'

def header(active):
    links = "".join(
        f'<a href="{href}"{" aria-current=\"page\"" if key == active else ""}>{label}</a>'
        for key, href, label in NAV
    )
    return f"""
<div class="demo-bar" role="note">Propuesta de rediseño · Demo no oficial preparada para Grupo Jim Sports</div>
<div class="topbar"><div class="wrap">
  <span class="info">Distribución deportiva B2B desde 1997 · Palas de Rei (Lugo) · <a href="tel:+34982286100">+34 982 28 61 00</a></span>
  <div class="langs"><span aria-current="true">ES</span><span>EN</span><span>PT</span><span>FR</span><span>DE</span><span>IT</span>
  <a href="https://jimsports.shop/" target="_blank" rel="noopener">Área clientes →</a></div>
</div></div>
<header class="site-header"><div class="wrap">
  <a class="brand" href="/" aria-label="Grupo Jim Sports, inicio"><span><b>Jim</b> Sports</span></a>
  <nav class="nav" id="nav" aria-label="Principal">{links}</nav>
  <form class="search" role="search" action="/catalogos"><label class="sr-only" for="q">Buscar</label>{SEARCH_ICON}<input id="q" name="q" type="search" placeholder="Referencia, EAN o producto"></form>
  <a class="btn btn-red" href="/hazte-cliente">Hazte cliente</a>
  <button class="menu-btn" aria-label="Abrir menú" aria-expanded="false" aria-controls="nav"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#161616" stroke-width="2.4" aria-hidden="true"><path d="M3 6h18M3 12h18M3 18h18"/></svg></button>
</div></header>
"""

SOCIAL = [
    ("Facebook", "https://www.facebook.com/grupo.jimsports", "Fb"),
    ("LinkedIn", "https://es.linkedin.com/company/grupo-jim-sports", "In"),
    ("Instagram", "https://www.instagram.com/grupojimsports/", "Ig"),
    ("WhatsApp", "https://api.whatsapp.com/send?phone=34683408532", "Wa"),
    ("X", "https://x.com/GrupoJimSports", "X"),
    ("TikTok", "https://www.tiktok.com/@grupojimsports", "Tk"),
]

def footer():
    social = "".join(
        f'<a href="{u}" target="_blank" rel="noopener" aria-label="{n}">{t}</a>' for n, u, t in SOCIAL
    )
    return f"""
<footer class="site-footer"><div class="wrap">
 <div class="cols">
  <div><a class="brand" href="/"><span><b>Jim</b> Sports</span></a>
   <p class="mt-24">Grupo Jim Sports · Impulsando el deporte desde 1997.<br>Polígono Industrial de Palas de Rei, s/n<br>27200 Palas de Rei (Lugo)<br><a href="tel:+34982286100">+34 982 28 61 00</a> · <a href="mailto:info@jimsports.com">info@jimsports.com</a></p>
   <div class="social">{social}</div></div>
  <div><h4>Clientes</h4><ul>
   <li><a href="/hazte-cliente">Hazte cliente</a></li>
   <li><a href="https://jimsports.shop/" target="_blank" rel="noopener">Área clientes</a></li>
   <li><a href="/catalogos">Catálogos</a></li>
   <li><a href="/crea-tu-marca">Crea tu marca</a></li>
   <li><a href="/crea-tu-marca#equipaciones">Equipaciones personalizadas</a></li></ul></div>
  <div><h4>Grupo</h4><ul>
   <li><a href="/nosotros">Nosotros</a></li>
   <li><a href="/marcas">Marcas</a></li>
   <li><a href="/rsc">Responsabilidad Social Corporativa</a></li>
   <li><a href="/noticias">Noticias</a></li>
   <li><a href="https://jimsports.com/trabaja-con-nosotros/" target="_blank" rel="noopener">Trabaja con nosotros</a></li>
   <li><a href="https://jimsports.com/codigo-de-conducta/" target="_blank" rel="noopener">Código de conducta para proveedores</a></li></ul></div>
  <div><h4>Legal</h4><ul>
   <li><a href="https://jimsports.com/condiciones-de-venta/" target="_blank" rel="noopener">Condiciones de venta</a></li>
   <li><a href="https://jimsports.com/politicas-de-calidad-y-medio-ambiente/" target="_blank" rel="noopener">Calidad y medio ambiente</a></li>
   <li><a href="https://jimsports.com/politica-de-privacidad/" target="_blank" rel="noopener">Privacidad</a></li>
   <li><a href="https://jimsports.com/politica-de-cookies/" target="_blank" rel="noopener">Cookies</a></li>
   <li><a href="https://jimsports.com/feder/" target="_blank" rel="noopener">FEDER y FSE</a></li></ul></div>
 </div>
 <div class="legal"><span>© 2026 Jim Sports Technology, S.L. · Todos los derechos reservados</span>
  <a href="https://jimsports.com/feder/" target="_blank" rel="noopener"><img src="{U}/2026/08/logo_blanco2-EU.png" alt="Cofinanciado por la Unión Europea"></a></div>
</div></footer>
"""

TEMPLATE = """<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="noindex, nofollow">
<meta name="theme-color" content="#E31B23">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:wght@400;700&family=Big+Shoulders+Display:wght@700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/styles.css">
</head>
<body>
{header}
<main id="main">
{body}
</main>
{footer}
<script src="/assets/site.js" defer></script>
</body>
</html>
"""

def build():
    for f in sorted(SRC.glob("*.html")):
        raw = f.read_text(encoding="utf-8")
        m = re.match(r"<!--\s*(.*?)\s*-->\n", raw)
        meta = dict(p.split(":", 1) for p in m.group(1).split(" | "))
        meta = {k.strip(): v.strip() for k, v in meta.items()}
        body = raw[m.end():].replace("{U}", U)
        out = TEMPLATE.format(
            title=meta["title"], desc=meta["desc"],
            header=header(meta.get("nav", "")), body=body, footer=footer(),
        )
        (ROOT / f.name).write_text(out, encoding="utf-8")
        print("ok", f.name)

if __name__ == "__main__":
    build()
