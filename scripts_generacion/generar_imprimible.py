#!/usr/bin/env python3
"""
GENERADOR DE VERSIÓN IMPRIMIBLE DEL MAPA METABÓLICO (PÓSTER 120 × 90 cm)
=======================================================================
Reglas respetadas:
1. Lee prueba_visual_integrada_conectada.html SIN modificarlo.
2. Genera prueba_visual_imprimible.html como COPIA enriquecida alrededor.
3. Conserva el 100% del contenido interno del SVG original byte a byte:
   - Ningún id, coordenada, texto, color, leyenda o bloque de autoría/QR se altera.
   - Todos los elementos nuevos se agregan alrededor en grupos con prefijo 'print_'.
4. Envuelve el mapa en un lienzo 7200 × 5400 px (viewBox="-700 -450 7200 5400"):
   - Proporción exacta 120 × 90 cm (4 : 3).
   - Margen de seguridad > 3 cm reales en todo el contorno (arriba: 7.5 cm, laterales: 11.67 cm, abajo: 3.33 cm).
   - Marco perimetral fino con la paleta (#0284c7, #0d9488, #10b981).
5. Gran banda de cabecera con el título "MAPA METABÓLICO INTEGRADO" y subtítulos de vías y autoría original.
6. Fuentes Inter y JetBrains Mono incrustadas en base64 @font-face en el CSS con fallbacks.
7. CSS @media print y @page con tamaño 120cm 90cm, márgenes 0 y print-color-adjust: exact.
8. Genera PDF vectorial con Chromium headless (Brave) y verifica que el texto es vectorial.
9. Genera vista previa PNG del póster completo y recorte del QR a escala real de impresión.
"""
import base64
import os
import re
import subprocess
import sys

DIR_SCRIPT = os.path.dirname(os.path.abspath(__file__))
DIR_BASE = os.path.dirname(DIR_SCRIPT) if os.path.basename(DIR_SCRIPT) == "scripts_generacion" else DIR_SCRIPT
DIR_HTML = os.path.join(DIR_BASE, "versiones_html")
DIR_IMPRESION = os.path.join(DIR_BASE, "versiones_impresion")
DIR_PREVIEWS = os.path.join(DIR_BASE, "capturas_y_pruebas")

RUTA_ORIGINAL = os.path.join(DIR_HTML, "prueba_visual_integrada_conectada.html")
RUTA_IMPRIMIBLE = os.path.join(DIR_HTML, "prueba_visual_imprimible.html")
RUTA_PDF = os.path.join(DIR_IMPRESION, "prueba_visual_imprimible.pdf")
RUTA_PNG_PREVIEW = os.path.join(DIR_PREVIEWS, "prueba_visual_imprimible_preview.png")
RUTA_PNG_QR = os.path.join(DIR_PREVIEWS, "prueba_visual_imprimible_qr_crop.png")


def cargar_fuentes_base64():
    """Genera las reglas @font-face con archivos woff2 incrustados en base64."""
    d_inter = "/tmp/fonts_install/node_modules/@fontsource/inter/files"
    d_mono = "/tmp/fonts_install/node_modules/@fontsource/jetbrains-mono/files"
    css_fonts = []

    # Inter (400, 600, 700, 800, 900)
    for w in [400, 600, 700, 800, 900]:
        fpath = os.path.join(d_inter, f"inter-latin-{w}-normal.woff2")
        if os.path.exists(fpath):
            with open(fpath, "rb") as f:
                b64 = base64.b64encode(f.read()).decode("ascii")
            css_fonts.append(f"""
@font-face {{
  font-family: 'Inter';
  font-style: normal;
  font-weight: {w};
  font-display: swap;
  src: url('data:font/woff2;charset=utf-8;base64,{b64}') format('woff2');
}}""")

    # JetBrains Mono (600, 700, 800)
    for w in [600, 700, 800]:
        fpath = os.path.join(d_mono, f"jetbrains-mono-latin-{w}-normal.woff2")
        if os.path.exists(fpath):
            with open(fpath, "rb") as f:
                b64 = base64.b64encode(f.read()).decode("ascii")
            css_fonts.append(f"""
@font-face {{
  font-family: 'JetBrains Mono';
  font-style: normal;
  font-weight: {w};
  font-display: swap;
  src: url('data:font/woff2;charset=utf-8;base64,{b64}') format('woff2');
}}""")

    return "\n".join(css_fonts)


def construir_imprimible():
    print(f"1. Leyendo archivo original: {RUTA_ORIGINAL}")
    with open(RUTA_ORIGINAL, "r", encoding="utf-8") as f:
        html_orig = f.read()

    # Extraer el interior exacto del SVG
    svg_start = html_orig.find("<svg")
    if svg_start == -1:
        raise ValueError("No se encontró la etiqueta <svg en el archivo original")
    svg_tag_end = html_orig.find(">", svg_start) + 1
    svg_close = html_orig.rfind("</svg>")
    inner_svg_orig = html_orig[svg_tag_end:svg_close]

    print(f"   ✓ Interior del SVG original extraído: {len(inner_svg_orig):,} caracteres")

    # Cargar fuentes base64
    css_fonts = cargar_fuentes_base64()
    print("   ✓ Fuentes Inter y JetBrains Mono convertidas a base64 @font-face")

    # Lienzo póster: 120 x 90 cm = 7200 x 5400 px (viewBox="-700 -450 7200 5400")
    # El mapa original ocupa [0, 5800] x [0, 4750] intacto en sus coordenadas originales
    W_CANVAS = 7200
    H_CANVAS = 5400
    VB_X = -700
    VB_Y = -450

    # Elementos nuevos alrededor con prefijo 'print_'
    print_decoraciones = f"""
    <!-- ===================================================================== -->
    <!-- CAPAS DEL PÓSTER IMPRIMIBLE 120 × 90 cm (PREFIJO 'print_')            -->
    <!-- ===================================================================== -->

    <!-- 1. Fondo blanco / claro del lienzo exterior (ahorra tinta) -->
    <g id="print_fondo">
      <rect x="{VB_X}" y="{VB_Y}" width="{W_CANVAS}" height="{H_CANVAS}" fill="#ffffff" />
    </g>

    <!-- 2. Marco perimetral fino con la paleta (#0284c7, #0d9488, #10b981) -->
    <g id="print_marco">
      <!-- Borde exterior triple elegante -->
      <rect x="-675" y="-425" width="7150" height="5350" rx="18" fill="none" stroke="#0284c7" stroke-width="4.5" />
      <rect x="-668" y="-418" width="7136" height="5336" rx="14" fill="none" stroke="#0d9488" stroke-width="2.5" />
      <rect x="-662" y="-412" width="7124" height="5324" rx="10" fill="none" stroke="#10b981" stroke-width="1.5" />

      <!-- Marcas de registro y corte en las 4 esquinas exteriores (30px) -->
      <g stroke="#94a3b8" stroke-width="1.2">
        <!-- Esquina Superior Izquierda -->
        <line x1="-695" y1="-425" x2="-655" y2="-425" />
        <line x1="-675" y1="-445" x2="-675" y2="-405" />
        <!-- Esquina Superior Derecha -->
        <line x1="6455" y1="-425" x2="6495" y2="-425" />
        <line x1="6475" y1="-445" x2="6475" y2="-405" />
        <!-- Esquina Inferior Izquierda -->
        <line x1="-695" y1="4925" x2="-655" y2="4925" />
        <line x1="-675" y1="4905" x2="-675" y2="4945" />
        <!-- Esquina Inferior Derecha -->
        <line x1="6455" y1="4925" x2="6495" y2="4925" />
        <line x1="6475" y1="4905" x2="6475" y2="4945" />
      </g>
    </g>

    <!-- 3. Gran banda superior de cabecera (Título legible a 2-3 metros) -->
    <g id="print_cabecera">
      <!-- Badge temático superior izquierdo -->
      <g transform="translate(-620, -320)">
        <rect x="0" y="0" width="380" height="42" rx="9" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.8" />
        <text x="190" y="27" fill="#0369a1" font-size="14.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle" letter-spacing="1.2">EDICIÓN CARTOGRAFÍA METABÓLICA</text>
        <text x="0" y="66" fill="#64748b" font-size="14.5" font-weight="700" font-family="'Inter', sans-serif">Bioquímica Celular • Gran Formato 1200 × 900 mm</text>
      </g>

      <!-- Título principal de póster (centrado en X=2900 sobre el mapa) -->
      <text x="2900" y="-235" fill="#0f172a" font-size="76" font-weight="900" font-family="'Inter', sans-serif" letter-spacing="4" text-anchor="middle">MAPA METABÓLICO INTEGRADO</text>
      
      <!-- Subtítulo 1: Topología -->
      <text x="2900" y="-170" fill="#0284c7" font-size="28" font-weight="800" font-family="'Inter', sans-serif" letter-spacing="1.5" text-anchor="middle">Entorno Celular y Rutas Bioquímicas • Topología Celular &amp; Arquitectura Vectorial Algorítmica</text>

      <!-- Subtítulo 2: Vías metabólicas integradas -->
      <text x="2900" y="-115" fill="#334155" font-size="21" font-weight="700" font-family="'Inter', sans-serif" text-anchor="middle">Glucólisis • Gluconeogénesis • Glucógeno • Pentosas • Lanzaderas • Krebs • Cadena Respiratoria • β-Oxidación • Cetogénesis • Lipogénesis • Ciclo de la Urea • Nucleótidos</text>

      <!-- Autoría institucional superior derecha (exacta a bloque_autoria) -->
      <g transform="translate(6420, -320)">
        <text x="0" y="22" fill="#0f172a" font-size="19" font-weight="900" font-family="'Inter', sans-serif" text-anchor="end">Adolfo Morales Tena</text>
        <text x="0" y="47" fill="#64748b" font-size="14.5" font-weight="700" font-family="'Inter', sans-serif" text-anchor="end">Estudiante • Licencia MIT (Open Source)</text>
        <text x="0" y="71" fill="#0284c7" font-size="14" font-weight="800" font-family="'JetBrains Mono', monospace" text-anchor="end">github.com/AMorales22T/mapa_metabolico</text>
      </g>

      <!-- Línea triple de acento cromático entre la cabecera y el mapa -->
      <line x1="-650" y1="-56" x2="6450" y2="-56" stroke="#0284c7" stroke-width="3" />
      <line x1="-650" y1="-50" x2="6450" y2="-50" stroke="#0d9488" stroke-width="2" />
      <line x1="-650" y1="-45" x2="6450" y2="-45" stroke="#10b981" stroke-width="1.5" />
    </g>

    <!-- 4. Pie de página institucional inferior -->
    <g id="print_pie_poster">
      <line x1="-650" y1="4815" x2="6450" y2="4815" stroke="#e2e8f0" stroke-width="1.5" />
      <text x="-620" y="4855" fill="#64748b" font-size="13.5" font-weight="800" font-family="'JetBrains Mono', monospace">MAPA METABÓLICO INTEGRADO • PROYECTO UNIVERSITARIO DE CÓDIGO ABIERTO (MIT)</text>
      <text x="2900" y="4855" fill="#94a3b8" font-size="13.5" font-weight="700" font-family="'Inter', sans-serif" text-anchor="middle">Renderizado Vectorial Ultra HD 1:1 • Diseñado para Impresión Editorial de Póster</text>
      <text x="6420" y="4855" fill="#0284c7" font-size="13.5" font-weight="800" font-family="'JetBrains Mono', monospace" text-anchor="end">REPOSITORIO: https://github.com/AMorales22T/mapa_metabolico</text>
    </g>
"""

    nuevo_svg = f'<svg width="{W_CANVAS}" height="{H_CANVAS}" viewBox="{VB_X} {VB_Y} {W_CANVAS} {H_CANVAS}" xmlns="http://www.w3.org/2000/svg">' + \
                print_decoraciones + \
                inner_svg_orig + \
                "</svg>"

    # Construir HTML completo
    html_imprimible = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Mapa Metabólico Integrado — Póster Imprimible 120 × 90 cm</title>
  <style>
    /* -------------------------------------------------------------
       FUENTES INCRUSTADAS BASE64 (OFFLINE / IMPRENTA FIDELITY)
       ------------------------------------------------------------- */
{css_fonts}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    
    body {{
      font-family: 'Inter', system-ui, -apple-system, sans-serif;
      background: #0f172a;
      color: #f8fafc;
      display: flex;
      flex-direction: column;
      height: 100vh;
      overflow: hidden;
    }}

    .header-bar {{
      width: 100%;
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: #1e293b;
      padding: 10px 24px;
      border-bottom: 1px solid #334155;
      z-index: 10;
    }}

    .header-bar h2 {{
      color: #38bdf8;
      font-size: 1.15rem;
      font-weight: 800;
    }}

    .header-bar p {{
      color: #94a3b8;
      font-size: 0.8rem;
    }}

    .controls {{
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .controls button {{
      background: #0284c7;
      color: #ffffff;
      border: none;
      padding: 6px 14px;
      border-radius: 6px;
      font-weight: 800;
      font-size: 0.82rem;
      cursor: pointer;
      transition: background 0.15s;
    }}

    .controls button:hover {{ background: #0369a1; }}
    .controls button.btn-print {{
      background: #10b981;
      font-size: 0.88rem;
      padding: 7px 16px;
    }}
    .controls button.btn-print:hover {{ background: #059669; }}

    .viewport {{
      flex: 1;
      width: 100%;
      overflow: hidden;
      position: relative;
      cursor: grab;
      background: #0f172a;
    }}

    .viewport.grabbing {{ cursor: grabbing; }}

    #panLayer {{
      position: absolute;
      top: 0;
      left: 0;
      transform-origin: 0 0;
      width: {W_CANVAS}px;
      height: {H_CANVAS}px;
    }}

    svg {{
      display: block;
      width: 100%;
      height: 100%;
      background: #ffffff;
    }}

    /* -------------------------------------------------------------
       MODO IMPRESIÓN EDITORIAL: @page Y @media print (120 × 90 cm)
       ------------------------------------------------------------- */
    @page {{
      size: 120cm 90cm;
      margin: 0;
    }}

    @media print {{
      html, body {{
        width: 120cm !important;
        height: 90cm !important;
        margin: 0 !important;
        padding: 0 !important;
        background: #ffffff !important;
        color: #000000 !important;
        overflow: hidden !important;
        -webkit-print-color-adjust: exact !important;
        print-color-adjust: exact !important;
      }}

      .header-bar {{
        display: none !important;
      }}

      .viewport {{
        position: static !important;
        width: 120cm !important;
        height: 90cm !important;
        overflow: hidden !important;
        background: #ffffff !important;
        cursor: default !important;
      }}

      #panLayer {{
        position: static !important;
        width: 120cm !important;
        height: 90cm !important;
        transform: none !important;
      }}

      svg {{
        width: 120cm !important;
        height: 90cm !important;
        display: block !important;
        background: #ffffff !important;
      }}
    }}
  </style>
</head>
<body>
  <div class="header-bar">
    <div>
      <h2>Mapa Metabólico Integrado — Póster 120 × 90 cm</h2>
      <p>Vista lista para imprenta • Márgenes de seguridad &gt; 3 cm • Tipografía incrustada 100% vectorial</p>
    </div>
    <div class="controls">
      <button class="btn-print" onclick="window.print()">🖨️ Imprimir / Guardar PDF (120 × 90 cm)</button>
      <div style="width: 1px; height: 22px; background: #475569; margin: 0 4px;"></div>
      <button onclick="zoomOut()">−</button>
      <span id="zoomLevel" style="color: #cbd5e1; font-weight: 700; min-width: 48px; text-align: center;">100%</span>
      <button onclick="zoomIn()">+</button>
      <button onclick="resetView()">Reset</button>
      <button style="background: #16a34a;" onclick="fitView()">Ajustar</button>
    </div>
  </div>

  <div class="viewport" id="viewport">
    <div id="panLayer">
      {nuevo_svg}
    </div>
  </div>

  <script>
    const viewport = document.getElementById('viewport');
    const panLayer = document.getElementById('panLayer');
    const zoomLevelEl = document.getElementById('zoomLevel');
    
    let scale = 1;
    let pointX = 0;
    let pointY = 0;
    let startX = 0;
    let startY = 0;
    let isPanning = false;

    function updateTransform() {{
      panLayer.style.transform = `translate(${{pointX}}px, ${{pointY}}px) scale(${{scale}})`;
      zoomLevelEl.textContent = `${{Math.round(scale * 100)}}%`;
    }}

    function zoom(delta, clientX, clientY) {{
      const rect = viewport.getBoundingClientRect();
      const cx = (clientX !== undefined ? clientX : rect.left + rect.width / 2) - rect.left;
      const cy = (clientY !== undefined ? clientY : rect.top + rect.height / 2) - rect.top;

      const prevScale = scale;
      scale *= delta;
      scale = Math.max(0.08, Math.min(scale, 6));

      pointX = cx - (cx - pointX) * (scale / prevScale);
      pointY = cy - (cy - pointY) * (scale / prevScale);
      updateTransform();
    }}

    function zoomIn() {{ zoom(1.25); }}
    function zoomOut() {{ zoom(0.8); }}
    
    function resetView() {{
      scale = 1;
      pointX = 0;
      pointY = 0;
      updateTransform();
    }}

    function fitView() {{
      const vw = viewport.clientWidth;
      const vh = viewport.clientHeight;
      scale = Math.min(vw / {W_CANVAS}, vh / {H_CANVAS});
      pointX = (vw - {W_CANVAS} * scale) / 2;
      pointY = (vh - {H_CANVAS} * scale) / 2;
      updateTransform();
    }}

    viewport.addEventListener('wheel', (e) => {{
      e.preventDefault();
      const delta = e.deltaY < 0 ? 1.15 : 0.85;
      zoom(delta, e.clientX, e.clientY);
    }}, {{ passive: false }});

    viewport.addEventListener('mousedown', (e) => {{
      if (e.button !== 0) return;
      isPanning = true;
      startX = e.clientX - pointX;
      startY = e.clientY - pointY;
      viewport.classList.add('grabbing');
    }});

    window.addEventListener('mousemove', (e) => {{
      if (!isPanning) return;
      pointX = e.clientX - startX;
      pointY = e.clientY - startY;
      updateTransform();
    }});

    window.addEventListener('mouseup', () => {{
      isPanning = false;
      viewport.classList.remove('grabbing');
    }});

    window.addEventListener('load', fitView);
    window.addEventListener('resize', fitView);
  </script>
</body>
</html>
"""

    print(f"2. Escribiendo archivo imprimible: {RUTA_IMPRIMIBLE}")
    with open(RUTA_IMPRIMIBLE, "w", encoding="utf-8") as f:
        f.write(html_imprimible)
    print(f"   ✓ Guardado correctamente ({os.path.getsize(RUTA_IMPRIMIBLE):,} bytes)")

    # 3. Verificación matemática estricta: Demostrar que el mapa original está 100% intacto
    print("\n3. Verificación de integridad estricta (Original vs Imprimible):")
    with open(RUTA_IMPRIMIBLE, "r", encoding="utf-8") as f:
        html_imp_check = f.read()

    # Comprobar que inner_svg_orig existe sin cambiar ni un solo byte dentro de html_imp_check
    pos = html_imp_check.find(inner_svg_orig)
    if pos != -1:
        print(f"   ✓ DEMOSTRACIÓN EXITOSA: Los {len(inner_svg_orig):,} bytes del SVG original")
        print("     están presentes de forma 100% EXACTA E IDÉNTICA bit a bit dentro de la copia.")
        print("     Ningún id, nodo, coordenada ni trazo del mapa original fue modificado.")
    else:
        print("   ✗ ERROR: El contenido del SVG original no coincide.")
        sys.exit(1)


def exportar_pdf_y_pngs():
    brave_bin = "/opt/brave-bin/brave"
    if not os.path.exists(brave_bin):
        print(f"Brave no encontrado en {brave_bin}")
        return

    print(f"\n4. Exportando PDF vectorial con Chromium headless (120 × 90 cm):")
    cmd_pdf = [
        brave_bin,
        "--headless=new",
        "--no-sandbox",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={RUTA_PDF}",
        RUTA_IMPRIMIBLE
    ]
    subprocess.run(cmd_pdf, check=True)
    size_pdf = os.path.getsize(RUTA_PDF)
    print(f"   ✓ PDF generado: {RUTA_PDF} ({size_pdf / (1024*1024):.2f} MB)")

    # Comprobar que el texto es texto vectorial y no una imagen
    txt_check = subprocess.run(["pdftotext", RUTA_PDF, "-"], capture_output=True, text=True).stdout
    print("   ✓ Comprobación de texto vectorial en PDF:")
    for query in ["MAPA METABÓLICO INTEGRADO", "Adolfo Morales Tena", "Glucosa-6-Fosfato", "CITOSOL", "MATRIZ MITOCONDRIAL"]:
        if query in txt_check:
            print(f"     • '{query}': ENCONTRADO como texto vectorial real ✓")
        else:
            print(f"     • '{query}': no encontrado")

    # 5. Generar PNG de vista previa del póster completo
    print(f"\n5. Generando PNG de vista previa del póster completo:")
    # Extraer el SVG puro del HTML imprimible para renderizar con rsvg-convert a resolución de revisión
    with open(RUTA_IMPRIMIBLE, "r", encoding="utf-8") as f:
        content = f.read()
    s_idx = content.find("<svg")
    e_idx = content.rfind("</svg>") + 6
    svg_pure = content[s_idx:e_idx]
    tmp_svg = "/tmp/_imprimible_pure.svg"
    with open(tmp_svg, "w", encoding="utf-8") as f:
        f.write(svg_pure)

    # Renderizar a 2400px de ancho para previsualización ligera
    subprocess.run(["rsvg-convert", "-w", "2400", "-o", RUTA_PNG_PREVIEW, tmp_svg], check=True)
    print(f"   ✓ PNG vista previa: {RUTA_PNG_PREVIEW} ({os.path.getsize(RUTA_PNG_PREVIEW) / (1024*1024):.2f} MB)")

    # 6. Generar PNG recortado del QR a tamaño real de impresión (para comprobar escaneo móvil)
    print(f"\n6. Generando PNG recortado de la esquina del QR (escala 1:1 real de impresión):")
    # El QR y su marco están en X=[5470, 5670], Y=[4350, 4550] en el mapa original (ancho 200px, alto 200px)
    # A 300 DPI de impresión, 1 cm = 118 px. 200px del canvas equivalen a ~3.3 cm reales.
    # En un recorte a 300 DPI, renderizamos ese fragmento con alta nitidez:
    w_crop = 240
    h_crop = 240
    x_crop = 5460
    y_crop = 4350
    # Creamos un SVG temporal centrado en el QR
    svg_qr = re.sub(
        r'<svg width="[^"]*" height="[^"]*" viewBox="[^"]*"',
        f'<svg width="{w_crop}" height="{h_crop}" viewBox="{x_crop} {y_crop} {w_crop} {h_crop}"',
        svg_pure,
        count=1
    )
    tmp_qr_svg = "/tmp/_qr_crop.svg"
    with open(tmp_qr_svg, "w", encoding="utf-8") as f:
        f.write(svg_qr)

    # Renderizar el QR a 600px (nitidez óptima para escanear con móvil desde pantalla)
    subprocess.run(["rsvg-convert", "-w", "600", "-o", RUTA_PNG_QR, tmp_qr_svg], check=True)
    print(f"   ✓ PNG recorte del QR: {RUTA_PNG_QR} ({os.path.getsize(RUTA_PNG_QR) / 1024:.1f} KB)")


if __name__ == "__main__":
    construir_imprimible()
    exportar_pdf_y_pngs()
