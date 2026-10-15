#!/usr/bin/env python3
"""
ACTUALIZADOR DE INTERACTIVIDAD PARA AMPLIACIÓN DEL TEMARIO (BLOQUES A–E)
=========================================================================
Convierte ampliacion_metabolismo_intermediario.html en una suite interactiva
con resaltado/atenuación por clic, índice lateral (A a E), buscador y zoom vectorial.
"""

import os
import re
import shutil

DIR_SCRIPT = os.path.dirname(os.path.abspath(__file__))
DIR_BASE = os.path.dirname(DIR_SCRIPT)
DIR_HTML = os.path.join(DIR_BASE, "versiones_html")

RUTA_HTML_TEMARIO = os.path.join(DIR_SCRIPT, "ampliacion_metabolismo_intermediario.html")
RUTA_COPIA_HTML = os.path.join(DIR_HTML, "ampliacion_metabolismo_intermediario.html")


def actualizar_ampliacion_temario():
    with open(RUTA_HTML_TEMARIO, "r", encoding="utf-8") as f:
        contenido = f.read()

    # Extraer el SVG
    svg_start = contenido.find("<svg")
    svg_end = contenido.rfind("</svg>") + 6
    svg_raw = contenido[svg_start:svg_end]

    # Modificar los círculos indicadores de sección para darles clase badge-via e ID
    svg_raw = re.sub(
        r'<circle cx="85" cy="183" r="16" fill="#0d9488"/>\s*<text x="85" y="189"[^>]*>A</text>',
        r'<g id="badge_seccion_A" class="badge-via" data-via="A" style="cursor: pointer;"><circle cx="85" cy="183" r="16" fill="#0d9488"/><text x="85" y="189" font-family="Inter, Arial, sans-serif" font-size="16" font-weight="900" fill="#ffffff" text-anchor="middle">A</text></g>',
        svg_raw
    )
    svg_raw = re.sub(
        r'<circle cx="1275" cy="183" r="16" fill="#7c3aed"/>\s*<text x="1275" y="189"[^>]*>B</text>',
        r'<g id="badge_seccion_B" class="badge-via" data-via="B" style="cursor: pointer;"><circle cx="1275" cy="183" r="16" fill="#7c3aed"/><text x="1275" y="189" font-family="Inter, Arial, sans-serif" font-size="16" font-weight="900" fill="#ffffff" text-anchor="middle">B</text></g>',
        svg_raw
    )
    svg_raw = re.sub(
        r'<circle cx="2465" cy="183" r="16" fill="#ea580c"/>\s*<text x="2465" y="189"[^>]*>C</text>',
        r'<g id="badge_seccion_C" class="badge-via" data-via="C" style="cursor: pointer;"><circle cx="2465" cy="183" r="16" fill="#ea580c"/><text x="2465" y="189" font-family="Inter, Arial, sans-serif" font-size="16" font-weight="900" fill="#ffffff" text-anchor="middle">C</text></g>',
        svg_raw
    )
    svg_raw = re.sub(
        r'<circle cx="85" cy="1618" r="16" fill="#059669"/>\s*<text x="85" y="1624"[^>]*>D</text>',
        r'<g id="badge_seccion_D" class="badge-via" data-via="D" style="cursor: pointer;"><circle cx="85" cy="1618" r="16" fill="#059669"/><text x="85" y="1624" font-family="Inter, Arial, sans-serif" font-size="16" font-weight="900" fill="#ffffff" text-anchor="middle">D</text></g>',
        svg_raw
    )
    svg_raw = re.sub(
        r'<circle cx="1590" cy="1618" r="16" fill="#2563eb"/>\s*<text x="1590" y="1624"[^>]*>E</text>',
        r'<g id="badge_seccion_E" class="badge-via" data-via="E" style="cursor: pointer;"><circle cx="1590" cy="1618" r="16" fill="#2563eb"/><text x="1590" y="1624" font-family="Inter, Arial, sans-serif" font-size="16" font-weight="900" fill="#ffffff" text-anchor="middle">E</text></g>',
        svg_raw
    )

    # Envolver cada sección en su propio grupo
    # Sección A: desde id="badge_seccion_A" hasta antes de id="badge_seccion_B"
    pos_A = svg_raw.find('id="badge_seccion_A"')
    pos_B = svg_raw.find('id="badge_seccion_B"')
    pos_C = svg_raw.find('id="badge_seccion_C"')
    pos_D = svg_raw.find('id="badge_seccion_D"')
    pos_E = svg_raw.find('id="badge_seccion_E"')
    pos_fin = svg_raw.rfind('</svg>')

    if all(p != -1 for p in [pos_A, pos_B, pos_C, pos_D, pos_E]):
        bloque_pre = svg_raw[:pos_A]
        bloque_A = svg_raw[pos_A:pos_B]
        bloque_B = svg_raw[pos_B:pos_C]
        bloque_C = svg_raw[pos_C:pos_D]
        bloque_D = svg_raw[pos_D:pos_E]
        bloque_E = svg_raw[pos_E:pos_fin]
        bloque_post = svg_raw[pos_fin:]

        svg_nuevo = (
            bloque_pre +
            '<g id="seccion_A_digestion" class="ruta-metabolica">' + bloque_A + '</g>\n' +
            '<g id="seccion_B_tag_fosfolipidos" class="ruta-metabolica">' + bloque_B + '</g>\n' +
            '<g id="seccion_C_colesterol" class="ruta-metabolica">' + bloque_C + '</g>\n' +
            '<g id="seccion_D_aminoacidos" class="ruta-metabolica">' + bloque_D + '</g>\n' +
            '<g id="seccion_E_integracion" class="ruta-metabolica">' + bloque_E + '</g>\n' +
            bloque_post
        )
    else:
        svg_nuevo = svg_raw

    html_interactivo = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Ampliación del Temario — Metabolismo Intermediario (Bloques A–E)</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@600;700;800&display=swap" rel="stylesheet">
  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: 'Inter', system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      background: #0f172a;
      color: #f8fafc;
      display: flex;
      flex-direction: column;
      height: 100vh;
      overflow: hidden;
      user-select: none;
      -webkit-user-select: none;
    }}

    .ui_dimmed {{
      opacity: 0.12 !important;
      transition: opacity 0.22s cubic-bezier(0.4, 0, 0.2, 1);
      filter: grayscale(45%);
    }}
    .ui_highlighted {{
      opacity: 1 !important;
      transition: opacity 0.22s cubic-bezier(0.4, 0, 0.2, 1);
    }}
    .ui_search_pulse {{
      animation: uiPulse 1.4s infinite cubic-bezier(0.4, 0, 0.6, 1);
      transform-box: fill-box;
      transform-origin: center;
    }}
    @keyframes uiPulse {{
      0%, 100% {{ filter: drop-shadow(0 0 4px #38bdf8); }}
      50% {{ filter: drop-shadow(0 0 20px #0284c7) drop-shadow(0 0 35px #0284c7); }}
    }}

    .header-bar {{
      width: 100%;
      min-height: 56px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: #1e293b;
      padding: 8px 18px;
      border-bottom: 1px solid #334155;
      z-index: 50;
      gap: 12px;
      flex-wrap: wrap;
    }}
    .header-title-box h2 {{
      color: #38bdf8;
      font-size: 0.98rem;
      font-weight: 800;
      letter-spacing: -0.2px;
    }}
    .header-title-box p {{
      color: #94a3b8;
      font-size: 0.74rem;
      font-weight: 600;
    }}
    .controls {{
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }}

    #ui_search_container {{
      position: relative;
      display: flex;
      align-items: center;
      background: #0f172a;
      border: 1px solid #475569;
      border-radius: 8px;
      padding: 3px 8px;
      gap: 6px;
      transition: border-color 0.2s, box-shadow 0.2s;
    }}
    #ui_search_container:focus-within {{
      border-color: #38bdf8;
      box-shadow: 0 0 0 2px rgba(56, 189, 248, 0.25);
    }}
    #ui_search_input {{
      background: transparent;
      border: none;
      outline: none;
      color: #f8fafc;
      font-family: 'Inter', sans-serif;
      font-size: 0.78rem;
      width: 190px;
    }}
    #ui_search_counter {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.7rem;
      color: #94a3b8;
      min-width: 32px;
      text-align: center;
    }}
    .ui_search_btn {{
      background: transparent;
      border: none;
      color: #94a3b8;
      cursor: pointer;
      padding: 2px 4px;
      border-radius: 4px;
      font-size: 0.75rem;
    }}
    .ui_search_btn:hover {{ color: #f8fafc; background: rgba(255,255,255,0.1); }}

    .controls button, .controls a {{
      background: #334155;
      color: #ffffff;
      border: 1px solid #475569;
      padding: 6px 11px;
      border-radius: 6px;
      font-weight: 800;
      font-size: 0.8rem;
      cursor: pointer;
      text-decoration: none;
      transition: background 0.15s;
    }}
    .controls button:hover, .controls a:hover {{ background: #475569; }}
    #zoomLevel {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.82rem;
      font-weight: 800;
      color: #38bdf8;
      min-width: 48px;
      text-align: center;
    }}

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
      width: 3600px;
      height: 3000px;
    }}
    svg {{ display: block; width: 100%; height: 100%; }}

    #ui_sidebar_panel {{
      position: absolute;
      top: 0;
      left: 0;
      bottom: 0;
      width: 380px;
      background: rgba(15, 23, 42, 0.96);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      border-right: 1px solid #334155;
      z-index: 100;
      display: flex;
      flex-direction: column;
      transform: translateX(-100%);
      transition: transform 0.28s cubic-bezier(0.4, 0, 0.2, 1);
      box-shadow: 4px 0 24px rgba(0, 0, 0, 0.6);
    }}
    #ui_sidebar_panel.ui_open {{ transform: translateX(0); }}
    .ui_sidebar_header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 14px 18px;
      border-bottom: 1px solid #334155;
      background: rgba(30, 41, 59, 0.7);
    }}
    .ui_sidebar_header h3 {{
      font-size: 0.98rem;
      font-weight: 800;
      color: #38bdf8;
    }}
    .ui_sidebar_header p {{
      font-size: 0.72rem;
      color: #94a3b8;
    }}
    .ui_sidebar_close {{
      background: transparent !important;
      border: none !important;
      color: #94a3b8 !important;
      font-size: 1.2rem;
      cursor: pointer;
      padding: 4px 8px !important;
    }}
    .ui_sidebar_close:hover {{ color: #ffffff !important; }}
    .ui_sidebar_list {{
      flex: 1;
      overflow-y: auto;
      padding: 12px 14px;
      display: flex;
      flex-direction: column;
      gap: 8px;
    }}
    .ui_sidebar_item {{
      display: flex;
      align-items: flex-start;
      gap: 12px;
      padding: 12px 14px;
      border-radius: 8px;
      background: #1e293b;
      border: 1px solid #334155;
      cursor: pointer;
      transition: all 0.16s ease;
    }}
    .ui_sidebar_item:hover {{
      background: #334155;
      border-color: #64748b;
      transform: translateX(3px);
    }}
    .ui_sidebar_item.ui_active {{
      background: rgba(2, 132, 199, 0.25);
      border-color: #38bdf8;
      box-shadow: 0 0 12px rgba(56, 189, 248, 0.2);
    }}
    .ui_sidebar_badge {{
      width: 28px;
      height: 28px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.85rem;
      font-weight: 900;
      flex-shrink: 0;
      box-shadow: 0 2px 6px rgba(0, 0, 0, 0.4);
    }}
    .ui_sidebar_info h4 {{
      font-size: 0.88rem;
      font-weight: 800;
      color: #f8fafc;
      margin-bottom: 3px;
    }}
    .ui_sidebar_info p {{
      font-size: 0.72rem;
      color: #94a3b8;
      line-height: 1.35;
    }}

    #ui_highlight_banner {{
      position: absolute;
      top: 14px;
      left: 50%;
      transform: translateX(-50%) translateY(-40px);
      background: rgba(2, 132, 199, 0.95);
      backdrop-filter: blur(10px);
      color: #ffffff;
      border-radius: 20px;
      padding: 6px 18px;
      display: flex;
      align-items: center;
      gap: 10px;
      z-index: 60;
      box-shadow: 0 4px 16px rgba(2, 132, 199, 0.4);
      opacity: 0;
      pointer-events: none;
      font-size: 0.82rem;
      font-weight: 800;
      transition: all 0.22s cubic-bezier(0.4, 0, 0.2, 1);
    }}
    #ui_highlight_banner.ui_visible {{
      opacity: 1;
      pointer-events: auto;
      transform: translateX(-50%) translateY(0);
    }}
    #ui_highlight_banner button {{
      background: rgba(0, 0, 0, 0.3);
      border: none;
      color: #ffffff;
      padding: 3px 8px;
      border-radius: 10px;
      font-size: 0.72rem;
      cursor: pointer;
    }}

    #ui_btn_sidebar_floating {{
      position: absolute;
      bottom: 20px;
      left: 20px;
      z-index: 40;
      background: #0284c7;
      color: #ffffff;
      border: none;
      border-radius: 24px;
      padding: 10px 18px;
      font-weight: 800;
      font-size: 0.84rem;
      display: flex;
      align-items: center;
      gap: 8px;
      cursor: pointer;
      box-shadow: 0 6px 20px rgba(2, 132, 199, 0.45);
      transition: transform 0.18s, background 0.18s;
    }}
    #ui_btn_sidebar_floating:hover {{
      background: #0369a1;
      transform: translateY(-2px);
    }}

    @media print {{
      .header-bar, #ui_sidebar_panel, #ui_btn_sidebar_floating, #ui_highlight_banner {{
        display: none !important;
      }}
      .ui_dimmed {{ opacity: 1 !important; filter: none !important; }}
    }}
  </style>
</head>
<body>
  <!-- HEADER BAR -->
  <div class="header-bar">
    <div class="header-title-box">
      <h2>Ampliación del Temario — Metabolismo Intermediario (Bloques A–E)</h2>
      <p>5 Bloques Temáticos • Digestión • Triacilgliceroles • Colesterol • Aminoácidos • Integración por Órganos</p>
    </div>

    <div class="controls">
      <button id="ui_btn_toggle_sidebar" onclick="toggleSidebar()" title="Índice de Bloques (A–E)">📑 Bloques (A–E)</button>
      
      <!-- Buscador -->
      <div id="ui_search_container">
        <span class="ui_search_icon">🔍</span>
        <input type="text" id="ui_search_input" placeholder="Buscar metabolito / enzima... [/]" autocomplete="off" spellcheck="false">
        <span id="ui_search_counter"></span>
        <button class="ui_search_btn" id="ui_search_prev" onclick="searchPrev()" title="Anterior (Shift+Enter)">▲</button>
        <button class="ui_search_btn" id="ui_search_next" onclick="searchNext()" title="Siguiente (Enter)">▼</button>
        <button class="ui_search_btn" id="ui_search_clear" onclick="clearSearch()" title="Limpiar (Esc)">✕</button>
      </div>

      <div style="width: 1px; height: 20px; background: #475569; margin: 0 4px;"></div>
      <button onclick="zoomOut()">−</button>
      <span id="zoomLevel">100%</span>
      <button onclick="zoomIn()">+</button>
      <button onclick="resetView()">Reset</button>
      <button style="background: #16a34a;" onclick="fitView()" title="Ajustar vista (F)">Ajustar</button>

      <!-- Selector de Vistas / Menú -->
      <div class="ui_dropdown_wrapper" style="position: relative; display: inline-block;">
        <button id="ui_btn_menu_views" onclick="toggleMenuViews(event)" title="Cambiar de vista" style="background: #1e293b; border: 1px solid #475569; color: #f8fafc; font-weight: 700; border-radius: 6px; padding: 6px 12px; cursor: pointer; display: inline-flex; align-items: center; gap: 6px; font-size: 0.82rem;">
          <span>🌐 Vistas</span> <span style="font-size: 9px;">▼</span>
        </button>
        <div id="ui_menu_views" style="display: none; position: absolute; right: 0; top: 100%; margin-top: 6px; background: #0f172a; border: 1px solid #334155; border-radius: 8px; box-shadow: 0 10px 25px rgba(0,0,0,0.6); min-width: 260px; z-index: 1000; padding: 6px 0; text-align: left;">
          <a href="mapa_cartulina_ampliado.html" style="display: block; padding: 8px 14px; color: #e2e8f0; text-decoration: none; font-size: 0.8rem;">🎓 Mapa Ampliado Completo (25 Vías)</a>
          <a href="ampliacion_rutas_18_25_interactiva.html" style="display: block; padding: 8px 14px; color: #e2e8f0; text-decoration: none; font-size: 0.8rem;">🧩 Ampliación V3 (Vías 18–25)</a>
          <a href="ampliacion_metabolismo_intermediario.html" style="display: block; padding: 8px 14px; color: #38bdf8; text-decoration: none; font-size: 0.8rem; font-weight: 700;">📋 Cuadro Temario (Bloques A–E)</a>
          <a href="../versiones_html/prueba_visual_interactiva.html" style="display: block; padding: 8px 14px; color: #e2e8f0; text-decoration: none; font-size: 0.8rem;">🗺️ Mapa Central (17 Vías)</a>
        </div>
      </div>
    </div>
  </div>

  <!-- PANEL LATERAL PLEGABLE: ÍNDICE DE BLOQUES (A a E) -->
  <div id="ui_sidebar_panel">
    <div class="ui_sidebar_header">
      <div>
        <h3>Bloques de la Ampliación</h3>
        <p>5 secciones temáticas complementarias</p>
      </div>
      <button class="ui_sidebar_close" onclick="toggleSidebar()" title="Cerrar índice (Esc)">✕</button>
    </div>
    <div class="ui_sidebar_list" id="ui_sidebar_list">
      <!-- Se puebla con JS -->
    </div>
  </div>

  <!-- BOTÓN FLOTANTE PARA ÍNDICE -->
  <button id="ui_btn_sidebar_floating" onclick="toggleSidebar()">
    <span>📑</span>
    <span>Índice Bloques (A–E)</span>
  </button>

  <!-- BANNER FLOTANTE DE SECCIÓN RESALTADA -->
  <div id="ui_highlight_banner">
    <span id="ui_highlight_title">Bloque resaltado</span>
    <button onclick="clearSectionHighlight()" title="Quitar resaltado (Esc)">✕ Quitar</button>
  </div>

  <!-- VIEWPORT & LIENZO VECTORIAL -->
  <div class="viewport" id="viewport">
    <div id="panLayer">
      {svg_nuevo}
    </div>
  </div>

  <script>
    const W_CANVAS = 3600;
    const H_CANVAS = 3000;

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
      if (zoomLevelEl) zoomLevelEl.textContent = Math.round(scale * 100) + '%';
    }}

    function zoomIn() {{ scale = Math.min(scale * 1.25, 4.0); updateTransform(); }}
    function zoomOut() {{ scale = Math.max(scale / 1.25, 0.1); updateTransform(); }}
    function resetView() {{ scale = 1; pointX = 0; pointY = 0; updateTransform(); }}
    function fitView() {{
      const vw = viewport.clientWidth;
      const vh = viewport.clientHeight;
      scale = Math.min(vw / W_CANVAS, vh / H_CANVAS) * 0.96;
      pointX = (vw - W_CANVAS * scale) / 2;
      pointY = (vh - H_CANVAS * scale) / 2;
      updateTransform();
    }}

    const TABLA_BLOQUES = {{
      "A": {{ id: "A", grupo: "seccion_A_digestion", badge: "badge_seccion_A", letra: "A", nombre: "Digestión, transporte y movilización", subtitulo: "Intestino • Lipasa pancreática • Enterocito • Quilomicrones • Tejido Adiposo", color: "#0d9488" }},
      "B": {{ id: "B", grupo: "seccion_B_tag_fosfolipidos", badge: "badge_seccion_B", letra: "B", nombre: "Triacilgliceroles y fosfolípidos", subtitulo: "Glicerol-3-P • LPA • PA • DAG • TAG • Fosfatidilcolina/etanolamina", color: "#7c3aed" }},
      "C": {{ id: "C", grupo: "seccion_C_colesterol", badge: "badge_seccion_C", letra: "C", nombre: "Colesterol, esteroides e isoprenoides", subtitulo: "HMG-CoA • Mevalonato • FPP • Colesterol • Esteroides • Sales biliares • Lipoproteínas", color: "#ea580c" }},
      "D": {{ id: "D", grupo: "seccion_D_aminoacidos", badge: "badge_seccion_D", letra: "D", nombre: "Biosíntesis de aminoácidos", subtitulo: "Alanina, Serina, Glicina, Cisteína, Aspartato, Asparagina, Glutamato, Glutamina, Prolina, Tirosina", color: "#059669" }},
      "E": {{ id: "E", grupo: "seccion_E_integracion", badge: "badge_seccion_E", letra: "E", nombre: "Integración por órgano y estado", subtitulo: "Perfiles metabólicos: Cerebro, Músculo, Hígado, Adipocito • Posprandial, Ayuno, Ejercicio, Diabetes", color: "#2563eb" }}
    }};

    let bloqueResaltado = null;
    let pointerDownX = 0;
    let pointerDownY = 0;

    function uiNormalize(str) {{
      return (str || '').normalize('NFD').replace(/[\\u0300-\\u036f]/g, '').toLowerCase().trim();
    }}

    function highlightSection(bId, shouldZoom = false) {{
      const blk = TABLA_BLOQUES[bId];
      if (!blk) return;
      bloqueResaltado = bId;

      Object.values(TABLA_BLOQUES).forEach(b => {{
        const el = document.getElementById(b.grupo);
        if (el) {{
          if (b.id === bId) {{
            el.classList.add('ui_highlighted');
            el.classList.remove('ui_dimmed');
          }} else {{
            el.classList.add('ui_dimmed');
            el.classList.remove('ui_highlighted');
          }}
        }}
      }});

      const banner = document.getElementById('ui_highlight_banner');
      const bannerTitle = document.getElementById('ui_highlight_title');
      if (banner && bannerTitle) {{
        bannerTitle.innerHTML = `<span style="background:${{blk.color}}; color:#fff; border-radius:50%; width:20px; height:20px; display:inline-flex; align-items:center; justify-content:center; font-size:11px; font-weight:900; margin-right:8px;">${{blk.letra}}</span> Bloque ${{blk.letra}}: ${{blk.nombre}}`;
        banner.classList.add('ui_visible');
      }}

      document.querySelectorAll('.ui_sidebar_item').forEach(it => {{
        if (it.getAttribute('data-block') === bId) {{
          it.classList.add('ui_active');
          it.scrollIntoView({{ block: 'nearest', behavior: 'smooth' }});
        }} else {{
          it.classList.remove('ui_active');
        }}
      }});

      if (shouldZoom) {{
        const mainEl = document.getElementById(blk.grupo);
        if (mainEl) zoomToElement(mainEl);
      }}
    }}

    function clearSectionHighlight() {{
      bloqueResaltado = null;
      Object.values(TABLA_BLOQUES).forEach(b => {{
        const el = document.getElementById(b.grupo);
        if (el) {{
          el.classList.remove('ui_dimmed');
          el.classList.remove('ui_highlighted');
        }}
      }});
      const banner = document.getElementById('ui_highlight_banner');
      if (banner) banner.classList.remove('ui_visible');
      document.querySelectorAll('.ui_sidebar_item').forEach(it => it.classList.remove('ui_active'));
    }}

    function zoomToElement(el) {{
      try {{
        const bbox = el.getBBox();
        const vw = viewport.clientWidth;
        const vh = viewport.clientHeight;
        const targetScale = Math.min(Math.max((vw / (bbox.width * 1.5)), 0.35), 2.5);
        const cx = bbox.x + bbox.width / 2;
        const cy = bbox.y + bbox.height / 2;
        scale = targetScale;
        pointX = vw / 2 - cx * scale;
        pointY = vh / 2 - cy * scale;
        updateTransform();
      }} catch (e) {{}}
    }}

    function toggleSidebar() {{
      const p = document.getElementById('ui_sidebar_panel');
      const btn = document.getElementById('ui_btn_toggle_sidebar');
      if (p) p.classList.toggle('ui_open');
      if (btn) btn.classList.toggle('ui_active');
    }}

    function poblarSidebar() {{
      const list = document.getElementById('ui_sidebar_list');
      if (!list) return;
      list.innerHTML = '';
      Object.values(TABLA_BLOQUES).forEach(b => {{
        const item = document.createElement('div');
        item.className = 'ui_sidebar_item';
        item.setAttribute('data-block', b.id);
        item.onclick = () => highlightSection(b.id, true);
        item.innerHTML = `
          <div class="ui_sidebar_badge" style="background: ${{b.color}}; color: #ffffff;">${{b.letra}}</div>
          <div class="ui_sidebar_info">
            <h4>${{b.nombre}}</h4>
            <p>${{b.subtitulo}}</p>
          </div>
        `;
        list.appendChild(item);
      }});
    }}

    function toggleMenuViews(e) {{
      e.stopPropagation();
      const menu = document.getElementById('ui_menu_views');
      if (menu) menu.style.display = menu.style.display === 'block' ? 'none' : 'block';
    }}

    document.addEventListener('click', (e) => {{
      const menu = document.getElementById('ui_menu_views');
      if (menu && !e.target.closest('.ui_dropdown_wrapper')) {{
        menu.style.display = 'none';
      }}
    }});

    // Buscador
    let INDICE_BUSQUEDA = [];
    function construirIndiceBusqueda() {{
      INDICE_BUSQUEDA = [];
      const svg = document.querySelector('#panLayer svg');
      if (!svg) return;
      svg.querySelectorAll('text').forEach(tNode => {{
        const raw = tNode.textContent.trim();
        if (!raw || raw.length < 2) return;
        const norm = uiNormalize(raw);
        INDICE_BUSQUEDA.push({{ element: tNode, text: raw, norm: norm }});
      }});
    }}

    let searchMatches = [];
    let searchIndex = -1;

    function ejecutarBusqueda() {{
      const inp = document.getElementById('ui_search_input');
      const counter = document.getElementById('ui_search_counter');
      if (!inp) return;
      const q = uiNormalize(inp.value);
      limpiarResaltadoBusqueda();
      if (!q || q.length < 2) {{
        if (counter) counter.textContent = '';
        return;
      }}
      searchMatches = INDICE_BUSQUEDA.filter(it => it.norm.includes(q));
      if (counter) counter.textContent = `${{searchMatches.length}}`;
      if (searchMatches.length > 0) {{
        searchIndex = 0;
        enfocarCoincidencia(searchIndex);
      }} else {{
        searchIndex = -1;
      }}
    }}

    function limpiarResaltadoBusqueda() {{
      document.querySelectorAll('.ui_search_pulse').forEach(el => {{
        el.classList.remove('ui_search_pulse');
        el.style.outline = '';
      }});
    }}

    function enfocarCoincidencia(idx) {{
      if (idx < 0 || idx >= searchMatches.length) return;
      limpiarResaltadoBusqueda();
      const match = searchMatches[idx];
      match.element.classList.add('ui_search_pulse');
      zoomToElement(match.element);
      const counter = document.getElementById('ui_search_counter');
      if (counter) counter.textContent = `${{idx + 1}}/${{searchMatches.length}}`;
    }}

    function searchNext() {{
      if (searchMatches.length === 0) return;
      searchIndex = (searchIndex + 1) % searchMatches.length;
      enfocarCoincidencia(searchIndex);
    }}
    function searchPrev() {{
      if (searchMatches.length === 0) return;
      searchIndex = (searchIndex - 1 + searchMatches.length) % searchMatches.length;
      enfocarCoincidencia(searchIndex);
    }}
    function clearSearch() {{
      const inp = document.getElementById('ui_search_input');
      const counter = document.getElementById('ui_search_counter');
      if (inp) inp.value = '';
      if (counter) counter.textContent = '';
      limpiarResaltadoBusqueda();
      searchMatches = [];
      searchIndex = -1;
    }}

    // Interacción ratón y clic
    function manejarClicEnLienzo(e, clientX, clientY) {{
      const target = document.elementFromPoint(clientX, clientY);
      if (!target) return;

      const badge = target.closest('.badge-via');
      if (badge) {{
        const bId = badge.getAttribute('data-via');
        if (bId && TABLA_BLOQUES[bId]) {{
          highlightSection(bId, false);
          return;
        }}
      }}

      const sec = target.closest('[id^="seccion_"]');
      if (sec) {{
        const bKey = Object.keys(TABLA_BLOQUES).find(k => TABLA_BLOQUES[k].grupo === sec.id);
        if (bKey) {{
          highlightSection(bKey, false);
          return;
        }}
      }}

      if (target.tagName === 'svg' || target.id === 'viewport' || target.id === 'panLayer' || target.tagName === 'rect') {{
        clearSectionHighlight();
      }}
    }}

    viewport.addEventListener('mousedown', (e) => {{
      if (e.target.closest('#ui_sidebar_panel, .header-bar, #ui_btn_sidebar_floating, #ui_highlight_banner')) return;
      isPanning = true;
      startX = e.clientX - pointX;
      startY = e.clientY - pointY;
      pointerDownX = e.clientX;
      pointerDownY = e.clientY;
      viewport.classList.add('grabbing');
    }});

    window.addEventListener('mousemove', (e) => {{
      if (!isPanning) return;
      pointX = e.clientX - startX;
      pointY = e.clientY - startY;
      updateTransform();
    }});

    window.addEventListener('mouseup', (e) => {{
      if (isPanning) {{
        isPanning = false;
        viewport.classList.remove('grabbing');
        const dist = Math.hypot(e.clientX - pointerDownX, e.clientY - pointerDownY);
        if (dist <= 4) {{
          manejarClicEnLienzo(e, e.clientX, e.clientY);
        }}
      }}
    }});

    viewport.addEventListener('wheel', (e) => {{
      e.preventDefault();
      const xs = (e.clientX - pointX) / scale;
      const ys = (e.clientY - pointY) / scale;
      const delta = -e.deltaY;
      const factor = delta > 0 ? 1.15 : 0.85;
      scale = Math.min(Math.max(scale * factor, 0.1), 4.0);
      pointX = e.clientX - xs * scale;
      pointY = e.clientY - ys * scale;
      updateTransform();
    }}, {{ passive: false }});

    window.addEventListener('keydown', (e) => {{
      if (e.key === 'Escape') {{
        clearSectionHighlight();
        clearSearch();
        const p = document.getElementById('ui_sidebar_panel');
        if (p) p.classList.remove('ui_open');
      }} else if (e.key === '/' && document.activeElement.tagName !== 'INPUT') {{
        e.preventDefault();
        const inp = document.getElementById('ui_search_input');
        if (inp) inp.focus();
      }} else if (e.key === 'f' || e.key === 'F') {{
        if (document.activeElement.tagName !== 'INPUT') fitView();
      }}
    }});

    const searchInputEl = document.getElementById('ui_search_input');
    if (searchInputEl) searchInputEl.addEventListener('input', ejecutarBusqueda);

    window.addEventListener('resize', fitView);

    window.addEventListener('DOMContentLoaded', () => {{
      poblarSidebar();
      construirIndiceBusqueda();
      fitView();
    }});
    if (document.readyState !== 'loading') {{
      poblarSidebar();
      construirIndiceBusqueda();
      fitView();
    }}
  </script>
</body>
</html>"""

    ruta_copia_html_num = os.path.join(DIR_HTML, "04_cuadro_temario_bloques_A_E.html")
    with open(RUTA_HTML_TEMARIO, "w", encoding="utf-8") as f:
        f.write(html_interactivo)
    with open(RUTA_COPIA_HTML, "w", encoding="utf-8") as f:
        f.write(html_interactivo)
    with open(ruta_copia_html_num, "w", encoding="utf-8") as f:
        f.write(html_interactivo)

    print(f"✓ Ampliación del temario actualizada con interactividad:")
    print(f"  - {ruta_copia_html_num} (Entregable numerado temario)")
    print(f"  - {RUTA_HTML_TEMARIO}")
    print(f"  - {RUTA_COPIA_HTML}")


if __name__ == "__main__":
    actualizar_ampliacion_temario()
