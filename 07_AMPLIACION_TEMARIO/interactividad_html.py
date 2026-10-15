"""
MÓDULO DE INTERACTIVIDAD PARA VISORES METABÓLICOS HTML (MOTOR DE ESTUDIO CIENTÍFICO)
====================================================================================
Genera interfaces interactivas de alta fidelidad con:
- Clic para resaltar/atenuar vías (distingue clic de arrastre <= 4px)
- Índice lateral desplegable (25 vías) con zoom animado centrado vectorial (CTM / getBBox)
- Buscador global sin acentos ni mayúsculas con pulso animado y navegación
- Ficha flotante / Tooltip para metabolitos (m_*) y enzimas (rx_*)
- Selector de Estados Metabólicos (Normal, Posprandial, Ayuno)
- Soporte táctil completo (arrastre 1 dedo, zoom pellizco 2 dedos)
- Atajos de teclado ('/' busca, 'Esc' limpia, 'F' ajusta)
- Menú de navegación entre vistas y descarga PDF
- Optimización print sin elementos UI
"""
import json
import os
import sys

DIR_INTERACT = os.path.dirname(os.path.abspath(__file__))
DIR_ROOT = os.path.dirname(DIR_INTERACT)
sys.path.append(os.path.join(DIR_ROOT, "06_REGULACION_Y_LEYENDA"))

try:
    import reacciones_estequiometria as re_est
    TABLA_REACCIONES_DATA = re_est.REACCIONES_ESTEQUIOMETRIA
except Exception:
    TABLA_REACCIONES_DATA = {}

def construir_html_mapa_ampliado(svg_final, w_canvas=7320, h_canvas=5490, vb_x=-760, vb_y=-250):
    """
    Empaqueta el SVG ampliado de 25 vías en un visor interactivo de estudio completo.
    """
    html_plantilla = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Mapa Metabólico Integrado — Herramienta Interactiva Ampliada (25 Vías)</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@600;700;800&display=swap" rel="stylesheet">
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: 'Inter', system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      background: #0f172a;
      color: #f8fafc;
      display: flex;
      flex-direction: column;
      height: 100vh;
      overflow: hidden;
      user-select: none;
      -webkit-user-select: none;
    }

    /* =============================================================
       ESTILOS DE LA HERRAMIENTA DE ESTUDIO INTERACTIVA (PREFIJO ui_)
       ============================================================= */

    /* Atenuación y resaltado de vías de alto rendimiento */
    .ui_dimmed {
      opacity: 0.12 !important;
      transition: opacity 0.22s cubic-bezier(0.4, 0, 0.2, 1);
      filter: grayscale(45%);
    }
    .ui_highlighted {
      opacity: 1 !important;
      transition: opacity 0.22s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .ui_state_active {
      opacity: 1 !important;
      transition: opacity 0.22s cubic-bezier(0.4, 0, 0.2, 1);
    }

    /* Animación de pulso para la búsqueda */
    .ui_search_pulse {
      outline: 5px solid #38bdf8 !important;
      outline-offset: 6px;
      border-radius: 8px;
      animation: ui_anim_pulse 1.4s infinite alternate ease-in-out;
    }
    @keyframes ui_anim_pulse {
      0% { filter: drop-shadow(0 0 4px #0284c7); }
      100% { filter: drop-shadow(0 0 20px #38bdf8); }
    }

    /* Cursor interactivo */
    [id^="m_"], [id^="rx_"], .badge-via, .ruta-metabolica {
      cursor: pointer !important;
    }

    /* Header Bar */
    .header-bar {
      width: 100%;
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: #1e293b;
      padding: 8px 20px;
      border-bottom: 1px solid #334155;
      z-index: 20;
      gap: 12px;
      flex-wrap: wrap;
    }
    .header-title-box h2 {
      color: #38bdf8;
      font-size: 1.05rem;
      font-weight: 800;
      margin-bottom: 2px;
    }
    .header-title-box p {
      color: #94a3b8;
      font-size: 0.74rem;
    }

    .controls {
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }

    /* Botón Sidebar */
    #ui_btn_toggle_sidebar {
      background: #0284c7;
      color: #ffffff;
      border: none;
      padding: 6px 12px;
      border-radius: 6px;
      font-weight: 800;
      font-size: 0.82rem;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 5px;
      transition: background 0.15s;
    }
    #ui_btn_toggle_sidebar:hover { background: #0369a1; }

    /* Estados Metabólicos */
    .ui_state_group {
      display: inline-flex;
      background: #0f172a;
      border: 1px solid #334155;
      border-radius: 7px;
      padding: 2px;
      gap: 2px;
    }
    .ui_state_btn {
      background: transparent;
      color: #94a3b8;
      border: none;
      padding: 5px 10px;
      border-radius: 5px;
      font-size: 0.78rem;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.15s ease;
    }
    .ui_state_btn:hover { color: #ffffff; background: rgba(255,255,255,0.06); }
    .ui_state_btn.ui_active { background: #0284c7; color: #ffffff; box-shadow: 0 1px 3px rgba(0,0,0,0.4); }
    .ui_state_btn#ui_btn_state_fasting.ui_active { background: #ea580c; }
    .ui_state_btn#ui_btn_state_fed.ui_active { background: #10b981; }

    /* Buscador */
    #ui_search_container {
      display: flex;
      align-items: center;
      background: #0f172a;
      border: 1px solid #334155;
      border-radius: 7px;
      padding: 2px 8px;
      gap: 6px;
      min-width: 240px;
      max-width: 300px;
      transition: border-color 0.2s, box-shadow 0.2s;
    }
    #ui_search_container:focus-within {
      border-color: #38bdf8;
      box-shadow: 0 0 0 2px rgba(56, 189, 248, 0.25);
    }
    .ui_search_icon { font-size: 0.8rem; color: #64748b; }
    #ui_search_input {
      background: transparent;
      border: none;
      outline: none;
      color: #f8fafc;
      font-size: 0.8rem;
      font-family: inherit;
      width: 100%;
    }
    #ui_search_input::placeholder { color: #64748b; }
    #ui_search_counter {
      font-size: 0.72rem;
      font-weight: 800;
      color: #38bdf8;
      font-family: 'JetBrains Mono', monospace;
      white-space: nowrap;
    }
    .ui_search_btn {
      background: transparent;
      border: none;
      color: #94a3b8;
      padding: 2px 4px;
      font-size: 0.72rem;
      cursor: pointer;
      border-radius: 4px;
    }
    .ui_search_btn:hover { color: #f8fafc; background: rgba(255,255,255,0.1); }

    /* Zoom Controls */
    .controls button, .controls a {
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
    }
    .controls button:hover, .controls a:hover { background: #475569; }
    #zoomLevel {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.82rem;
      font-weight: 800;
      color: #38bdf8;
      min-width: 48px;
      text-align: center;
    }

    /* Viewport & PanLayer */
    .viewport {
      flex: 1;
      width: 100%;
      overflow: hidden;
      position: relative;
      cursor: grab;
      background: #0f172a;
    }
    .viewport.grabbing { cursor: grabbing; }
    #panLayer {
      position: absolute;
      top: 0;
      left: 0;
      transform-origin: 0 0;
      width: __W_CANVAS__px;
      height: __H_CANVAS__px;
    }
    svg { display: block; width: 100%; height: 100%; }

    /* Sidebar Panel (Glassmorphic) */
    #ui_sidebar_panel {
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
      transition: transform 0.26s cubic-bezier(0.4, 0, 0.2, 1);
      box-shadow: 6px 0 28px rgba(0, 0, 0, 0.6);
    }
    #ui_sidebar_panel.ui_open { transform: translateX(0); }
    .ui_sidebar_header {
      padding: 14px 18px;
      border-bottom: 1px solid #334155;
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: #1e293b;
    }
    .ui_sidebar_header h3 { font-size: 0.95rem; font-weight: 800; color: #38bdf8; margin: 0; }
    .ui_sidebar_header p { font-size: 0.72rem; color: #94a3b8; margin: 2px 0 0 0; }
    .ui_sidebar_close {
      background: transparent;
      border: none;
      color: #94a3b8;
      font-size: 1.2rem;
      cursor: pointer;
      padding: 4px;
      border-radius: 4px;
    }
    .ui_sidebar_close:hover { color: #f8fafc; background: rgba(255, 255, 255, 0.1); }
    .ui_sidebar_filter {
      padding: 10px 14px;
      border-bottom: 1px solid #334155;
      background: #0f172a;
    }
    #ui_sidebar_search {
      width: 100%;
      background: #1e293b;
      border: 1px solid #334155;
      border-radius: 6px;
      padding: 7px 10px;
      color: #f8fafc;
      font-size: 0.8rem;
      font-family: inherit;
      outline: none;
    }
    #ui_sidebar_search:focus { border-color: #38bdf8; }
    .ui_sidebar_list {
      flex: 1;
      overflow-y: auto;
      padding: 8px 10px;
      display: flex;
      flex-direction: column;
      gap: 6px;
    }
    .ui_sidebar_item {
      display: flex;
      align-items: center;
      gap: 12px;
      padding: 9px 12px;
      border-radius: 8px;
      background: #1e293b;
      border: 1px solid #334155;
      cursor: pointer;
      transition: all 0.15s ease;
      text-align: left;
    }
    .ui_sidebar_item:hover {
      background: #253349;
      border-color: #38bdf8;
      transform: translateX(3px);
    }
    .ui_sidebar_item.ui_active {
      background: #0369a1 !important;
      border-color: #38bdf8 !important;
      box-shadow: 0 0 12px rgba(56, 189, 248, 0.4);
    }
    .ui_sidebar_badge {
      min-width: 26px;
      height: 26px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.74rem;
      font-weight: 900;
      font-family: 'JetBrains Mono', monospace;
      flex-shrink: 0;
    }
    .ui_sidebar_info h4 {
      font-size: 0.8rem;
      font-weight: 800;
      color: #f8fafc;
      margin: 0 0 2px 0;
    }
    .ui_sidebar_info p {
      font-size: 0.7rem;
      color: #94a3b8;
      margin: 0;
      line-height: 1.25;
    }

    /* Floating Badge Button for Sidebar */
    #ui_btn_sidebar_floating {
      position: absolute;
      top: 14px;
      left: 14px;
      background: rgba(15, 23, 42, 0.9);
      backdrop-filter: blur(10px);
      border: 1px solid #334155;
      color: #38bdf8;
      padding: 7px 12px;
      border-radius: 20px;
      font-size: 0.78rem;
      font-weight: 800;
      display: flex;
      align-items: center;
      gap: 6px;
      cursor: pointer;
      z-index: 50;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4);
      transition: all 0.2s;
    }
    #ui_btn_sidebar_floating:hover {
      background: #0284c7;
      color: #ffffff;
      border-color: #38bdf8;
    }

    /* Banners */
    #ui_highlight_banner {
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
    }
    #ui_highlight_banner.ui_visible {
      opacity: 1;
      pointer-events: auto;
      transform: translateX(-50%) translateY(0);
    }
    #ui_highlight_banner button {
      background: rgba(0, 0, 0, 0.3);
      border: none;
      color: #ffffff;
      padding: 3px 8px;
      border-radius: 10px;
      font-size: 0.72rem;
      cursor: pointer;
    }

    #ui_state_banner {
      position: absolute;
      bottom: 14px;
      left: 50%;
      transform: translateX(-50%) translateY(40px);
      background: rgba(15, 23, 42, 0.94);
      backdrop-filter: blur(10px);
      border: 1px solid #334155;
      color: #cbd5e1;
      border-radius: 20px;
      padding: 8px 20px;
      display: flex;
      align-items: center;
      gap: 12px;
      z-index: 60;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
      opacity: 0;
      pointer-events: none;
      font-size: 0.78rem;
      transition: all 0.22s cubic-bezier(0.4, 0, 0.2, 1);
      max-width: 85%;
      text-align: center;
    }
    #ui_state_banner.ui_visible {
      opacity: 1;
      pointer-events: auto;
      transform: translateX(-50%) translateY(0);
    }
    #ui_state_banner button {
      background: #334155;
      border: none;
      color: #ffffff;
      padding: 3px 8px;
      border-radius: 12px;
      font-size: 0.72rem;
      font-weight: 800;
      cursor: pointer;
    }

    /* Tooltip Card (Ficha Inteligente de Reacciones y Metabolitos) */
    #ui_tooltip_card {
      position: absolute;
      display: none;
      z-index: 250;
      background: rgba(15, 23, 42, 0.98);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      border: 1px solid #0284c7;
      border-radius: 12px;
      padding: 14px 18px;
      color: #f8fafc;
      box-shadow: 0 10px 32px rgba(0,0,0,0.7);
      pointer-events: none;
      max-width: 440px;
      min-width: 270px;
      font-size: 0.8rem;
      transition: border-color 0.2s, box-shadow 0.2s;
    }
    #ui_tooltip_card.ui_tt_pinned {
      pointer-events: auto !important;
      border: 1.8px solid #38bdf8 !important;
      box-shadow: 0 16px 45px rgba(0, 0, 0, 0.85), 0 0 24px rgba(56, 189, 248, 0.35) !important;
    }
    .ui_tt_close_btn {
      position: absolute;
      top: 10px;
      right: 12px;
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.15);
      color: #94a3b8;
      width: 22px;
      height: 22px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 11px;
      font-weight: 900;
      cursor: pointer;
      transition: all 0.15s;
    }
    .ui_tt_close_btn:hover {
      background: #ef4444;
      color: #ffffff;
      border-color: #ef4444;
    }
    .ui_tt_header_row {
      display: flex;
      align-items: center;
      gap: 6px;
      flex-wrap: wrap;
      margin-bottom: 6px;
    }
    .ui_tt_badge_via {
      display: inline-block;
      color: #ffffff;
      border-radius: 4px;
      padding: 2px 7px;
      font-size: 9.5px;
      font-weight: 900;
      letter-spacing: 0.3px;
    }
    .ui_tt_badge_ec {
      display: inline-block;
      background: #312e81;
      border: 1px solid #4f46e5;
      color: #c7d2fe;
      border-radius: 4px;
      padding: 2px 6px;
      font-size: 9px;
      font-weight: 800;
      font-family: 'JetBrains Mono', monospace;
    }
    #ui_tooltip_card h4 {
      font-size: 0.98rem;
      font-weight: 900;
      color: #38bdf8;
      margin: 2px 0 6px 0;
      line-height: 1.25;
      padding-right: 22px;
    }
    .ui_tt_eq_box {
      background: rgba(2, 132, 199, 0.1);
      border: 1px solid rgba(56, 189, 248, 0.3);
      border-left: 3.5px solid #38bdf8;
      border-radius: 6px;
      padding: 8px 10px;
      margin: 8px 0;
    }
    .ui_tt_eq_label {
      font-size: 8.5px;
      font-weight: 900;
      color: #38bdf8;
      letter-spacing: 0.8px;
      margin-bottom: 3px;
    }
    .ui_tt_eq_text {
      font-family: 'JetBrains Mono', monospace;
      font-size: 11px;
      font-weight: 800;
      color: #ffffff;
      line-height: 1.4;
      word-break: break-word;
    }
    .ui_tt_grid {
      display: flex;
      flex-direction: column;
      gap: 3px;
      margin: 6px 0;
      font-size: 10.5px;
    }
    .ui_tt_grid_row {
      display: flex;
      line-height: 1.35;
    }
    .ui_tt_label {
      color: #94a3b8;
      font-weight: 800;
      width: 82px;
      flex-shrink: 0;
    }
    .ui_tt_val {
      color: #e2e8f0;
      flex-grow: 1;
    }
    .ui_tt_reg_box {
      background: rgba(30, 41, 59, 0.7);
      border: 1px solid #334155;
      border-radius: 6px;
      padding: 6px 9px;
      margin-top: 6px;
      font-size: 10.5px;
      color: #cbd5e1;
      line-height: 1.35;
    }
    .ui_tt_pin_hint {
      margin-top: 6px;
      padding-top: 4px;
      border-top: 1px dashed rgba(148, 163, 184, 0.25);
      font-size: 9px;
      color: #64748b;
      font-style: italic;
      text-align: right;
    }

    @media print {
      .header-bar, #ui_sidebar_panel, #ui_btn_sidebar_floating, #ui_highlight_banner, #ui_state_banner, #ui_tooltip_card {
        display: none !important;
      }
      .ui_dimmed { opacity: 1 !important; filter: none !important; }
    }
  </style>
</head>
<body>
  <!-- HEADER BAR -->
  <div class="header-bar">
    <div class="header-title-box">
      <h2>Mapa Metabólico Integrado — Versión Ampliada (1200 × 900 mm)</h2>
      <p>25 Vías Integradas • Digestión • Adipocito • Sarcómero • Cerebro • Lipoproteínas • Membrana • Aminoácidos • Hepatocito Central</p>
    </div>

    <div class="controls">
      <!-- Botón de Índice -->
      <button id="ui_btn_toggle_sidebar" onclick="toggleSidebar()" title="Índice de Vías (25)">📑 Vías (25)</button>
      
      <!-- Modos de Estado Metabólico -->
      <div class="ui_state_group">
        <button class="ui_state_btn ui_active" id="ui_btn_state_normal" onclick="setMetabolicState('normal')" title="Mapa completo sin atenuación">Normal</button>
        <button class="ui_state_btn" id="ui_btn_state_fed" onclick="setMetabolicState('posprandial')" title="Insulina alta ↑ • Glucagón bajo ↓">🍽️ Posprandial</button>
        <button class="ui_state_btn" id="ui_btn_state_fasting" onclick="setMetabolicState('ayuno')" title="Glucagón alto ↑ • Insulina baja ↓">⚡ Ayuno</button>
      </div>

      <!-- Buscador Global -->
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

      <!-- Selector de Vistas / Descargas -->
      <div class="ui_dropdown_wrapper" style="position: relative; display: inline-block;">
        <button id="ui_btn_menu_views" onclick="toggleMenuViews(event)" title="Cambiar de vista o descargar" style="background: #1e293b; border: 1px solid #475569; color: #f8fafc; font-weight: 700; border-radius: 6px; padding: 6px 12px; cursor: pointer; display: inline-flex; align-items: center; gap: 6px; font-size: 0.82rem;">
          <span>🌐 Vistas / PDF</span> <span style="font-size: 9px;">▼</span>
        </button>
        <div id="ui_menu_views" style="display: none; position: absolute; right: 0; top: 100%; margin-top: 6px; background: #0f172a; border: 1px solid #334155; border-radius: 8px; box-shadow: 0 10px 25px rgba(0,0,0,0.6); min-width: 260px; z-index: 1000; padding: 6px 0; text-align: left;">
          <a href="01_mapa_ampliado_completo_25_vias.html" style="display: block; padding: 8px 14px; color: #38bdf8; text-decoration: none; font-size: 0.8rem; font-weight: 700;">🌟 01. Mapa Ampliado (25 Vías)</a>
          <a href="02_ampliacion_rutas_18_25.html" style="display: block; padding: 8px 14px; color: #e2e8f0; text-decoration: none; font-size: 0.8rem;">🧩 02. Ampliación Vías 18–25 (Standalone)</a>
          <a href="03_mapa_central_interactivo_17_vias.html" style="display: block; padding: 8px 14px; color: #e2e8f0; text-decoration: none; font-size: 0.8rem;">🗺️ 03. Mapa Central (17 Vías)</a>
          <a href="04_cuadro_temario_bloques_A_E.html" style="display: block; padding: 8px 14px; color: #e2e8f0; text-decoration: none; font-size: 0.8rem;">📋 04. Temario A–E (Metabolismo Intermediario)</a>
          <div style="height: 1px; background: #334155; margin: 4px 0;"></div>
          <a href="../versiones_impresion/01_mapa_ampliado_completo_120x90cm.pdf" target="_blank" style="display: block; padding: 8px 14px; color: #4ade80; text-decoration: none; font-size: 0.8rem; font-weight: 700;">📥 Descargar PDF 25 Vías (120×90 cm)</a>
          <a href="../versiones_impresion/02_ampliacion_rutas_18_25.pdf" target="_blank" style="display: block; padding: 8px 14px; color: #4ade80; text-decoration: none; font-size: 0.8rem;">📥 Descargar PDF Standalone Vías 18–25</a>
        </div>
      </div>
    </div>
  </div>

  <!-- PANEL LATERAL PLEGABLE: ÍNDICE DE VÍAS (25) -->
  <div id="ui_sidebar_panel">
    <div class="ui_sidebar_header">
      <div>
        <h3>Índice de Vías Metabólicas</h3>
        <p>25 rutas integradas • Clic para centrar y resaltar</p>
      </div>
      <button class="ui_sidebar_close" onclick="toggleSidebar()" title="Cerrar índice (Esc)">✕</button>
    </div>
    <div class="ui_sidebar_filter">
      <input type="text" id="ui_sidebar_search" placeholder="Filtrar vías (ej. Krebs, Lipólisis, Kennedy)..." oninput="filtrarSidebarVias()">
    </div>
    <div class="ui_sidebar_list" id="ui_sidebar_list">
      <!-- Se puebla dinámicamente con JavaScript desde TABLA_VIAS -->
    </div>
  </div>

  <!-- BOTÓN FLOTANTE PARA ÍNDICE (CUANDO ESTÁ REPLEGADO) -->
  <button id="ui_btn_sidebar_floating" onclick="toggleSidebar()">
    <span>📑</span>
    <span>Índice de Vías</span>
  </button>

  <!-- BANNER FLOTANTE DE VÍA RESALTADA -->
  <div id="ui_highlight_banner">
    <span id="ui_highlight_title">Vía resaltada</span>
    <button onclick="clearPathwayHighlight()" title="Quitar resaltado (Esc)">✕ Quitar</button>
  </div>

  <!-- RÓTULO FLOTANTE DE ESTADO METABÓLICO -->
  <div id="ui_state_banner">
    <span id="ui_state_banner_text">Estado activo</span>
    <button onclick="setMetabolicState('normal')">✕ Normal</button>
  </div>

  <!-- FICHA FLOTANTE / TOOLTIP -->
  <div id="ui_tooltip_card"></div>

  <!-- VIEWPORT & LIENZO VECTORIAL -->
  <div class="viewport" id="viewport">
    <div id="panLayer">
      __SVG_FINAL__
    </div>
  </div>

  <script>
    // =========================================================================
    // CONFIGURACIÓN VECTORIAL Y PARÁMETROS GEOMÉTRICOS DEL LIENZO
    // =========================================================================
    const W_CANVAS = __W_CANVAS__;
    const H_CANVAS = __H_CANVAS__;
    const VB_X = __VB_X__;
    const VB_Y = __VB_Y__;

    const viewport = document.getElementById('viewport');
    const panLayer = document.getElementById('panLayer');
    const zoomLevelEl = document.getElementById('zoomLevel');

    let scale = 1;
    let pointX = 0;
    let pointY = 0;
    let startX = 0;
    let startY = 0;
    let isPanning = false;

    function updateTransform() {
      panLayer.style.transform = `translate(${pointX}px, ${pointY}px) scale(${scale})`;
      if (zoomLevelEl) zoomLevelEl.textContent = Math.round(scale * 100) + '%';
    }

    function zoomIn() { scale = Math.min(scale * 1.25, 4.0); updateTransform(); }
    function zoomOut() { scale = Math.max(scale / 1.25, 0.08); updateTransform(); }
    function resetView() { scale = 1; pointX = 0; pointY = 0; updateTransform(); }
    function fitView() {
      const vw = viewport.clientWidth;
      const vh = viewport.clientHeight;
      scale = Math.min(vw / W_CANVAS, vh / H_CANVAS) * 0.96;
      pointX = (vw - W_CANVAS * scale) / 2;
      pointY = (vh - H_CANVAS * scale) / 2;
      updateTransform();
    }

    // =========================================================================
    // BASE DE DATOS DE REACCIONES QUÍMICAS Y ESTEQUIOMETRÍA BALANCEADA
    // =========================================================================
    const TABLA_REACCIONES_ESTEQUIOMETRIA = __TABLA_REACCIONES_JSON__;

    // =========================================================================
    // TABLA MAESTRA DE LAS 25 VÍAS METABÓLICAS INTEGRADAS
    // =========================================================================
    const TABLA_VIAS = {
      "1": { numero: "1", id: "1", nombre: "Glucólisis", subtitulo: "Glucosa → 2 Piruvato (+2 ATP, +2 NADH)", grupos: ["ruta_glucolisis", "badge_via_1"], color: "#0284c7" },
      "2": { numero: "2", id: "2", nombre: "Gluconeogénesis", subtitulo: "Piruvato → Glucosa (4 enzimas específicas) · hepática", grupos: ["ruta_gluconeogenesis", "badge_via_2"], color: "#7c3aed" },
      "3": { numero: "3", id: "3", nombre: "Glucogenogénesis y glucogenólisis", subtitulo: "Síntesis y degradación del glucógeno", grupos: ["ruta_glucogeno", "badge_via_3"], color: "#ea580c" },
      "4": { numero: "4", id: "4", nombre: "Vía de las pentosas fosfato", subtitulo: "G6P → NADPH + Ribosa-5-P (fase oxidativa y no oxidativa)", grupos: ["ruta_pentosas", "badge_via_4"], color: "#059669" },
      "5": { numero: "5", id: "5", nombre: "Complejo piruvato deshidrogenasa (PDH)", subtitulo: "Piruvato → Acetil-CoA + CO₂ + NADH", grupos: ["lupa_piruvato_deshidrogenasa", "badge_via_5"], color: "#c2410c" },
      "6": { numero: "6", id: "6", nombre: "Ciclo de Krebs", subtitulo: "Acetil-CoA → 2 CO₂ + 3 NADH + FADH₂ + GTP", grupos: ["ruta_krebs", "badge_via_6"], color: "#d97706" },
      "7": { numero: "7", id: "7", nombre: "Cadena respiratoria y ATP sintasa", subtitulo: "Fosforilación oxidativa (acoplamiento quimiosmótico)", grupos: ["lupa_cadena_respiratoria", "badge_via_7"], color: "#16a34a" },
      "8": { numero: "8", id: "8", nombre: "Lanzadera malato-aspartato", subtitulo: "Transporte de equivalentes redox (NADH citosólico a matriz)", grupos: ["lupa_lanzadera_malato_aspartato", "badge_via_8"], color: "#0284c7" },
      "8B": { numero: "8B", id: "8B", nombre: "Lanzadera glicerol-3-fosfato", subtitulo: "DHAP ➔ G3P (Reoxidación rápida de NADH hacia FAD en MMI)", grupos: ["lupa_lanzadera_glicerol_p", "badge_via_8B"], color: "#0d9488" },
      "9": { numero: "9", id: "9", nombre: "β-oxidación (y lanzadera de carnitina)", subtitulo: "Palmitoil-CoA → 8 Acetil-CoA + FADH₂ + NADH", grupos: ["ruta_beta_ox", "badge_via_9"], color: "#b45309" },
      "10": { numero: "10", id: "10", nombre: "Lipogénesis (síntesis de ácidos grasos)", subtitulo: "Acetil-CoA → Malonil-CoA → Palmitato (FAS)", grupos: ["ruta_lipogenesis", "badge_via_10"], color: "#0d9488" },
      "11": { numero: "11", id: "11", nombre: "Cetogénesis", subtitulo: "Acetil-CoA → Acetoacetato / β-Hidroxibutirato", grupos: ["ruta_ceto", "badge_via_11"], color: "#be123c" },
      "12": { numero: "12", id: "12", nombre: "Síntesis de colesterol", subtitulo: "Acetil-CoA → HMG-CoA → Mevalonato → Colesterol", grupos: ["ruta_colesterol", "badge_via_12"], color: "#4f46e5" },
      "12B": { numero: "12B", id: "12B", nombre: "Destinos esqueletos carbonados AA", subtitulo: "Convergencia de los 20 AA en Krebs, Piruvato y Cuerpos Cetónicos", grupos: ["ruta_destinos_aa", "badge_via_12B"], color: "#6366f1" },
      "13": { numero: "13", id: "13", nombre: "Transaminación y desaminación oxidativa", subtitulo: "Recogida del grupo amino en Glutamato → NH₄⁺", grupos: ["ruta_transaminacion_desaminacion", "badge_via_13"], color: "#2563eb" },
      "14": { numero: "14", id: "14", nombre: "Ciclo de la urea", subtitulo: "NH₄⁺ + HCO₃⁻ + Aspartato → Urea", grupos: ["ruta_ciclo_urea", "badge_via_14"], color: "#0891b2" },
      "15": { numero: "15", id: "15", nombre: "Biosíntesis de nucleótidos", subtitulo: "Rutas convergentes sobre PRPP (purinas y pirimidinas)", grupos: ["ruta_sintesis_nucleotidos", "badge_via_15"], color: "#0284c7" },
      "16": { numero: "16", id: "16", nombre: "Catabolismo de nucleótidos y ácido úrico", subtitulo: "Degradación de purinas a Ácido Úrico y pirimidinas a β-Alanina", grupos: ["ruta_degradacion_nucleotidos", "badge_via_16"], color: "#475569" },
      "17": { numero: "17", id: "17", nombre: "Ciclo de Cori", subtitulo: "Lactato muscular anaeróbico → Sangre → Glucosa hepática (GNG) → Músculo (-4 ATP neto)", grupos: ["ruta_ciclo_cori", "badge_via_17"], color: "#be123c" },
      "18": { numero: "18", id: "18", nombre: "Digestión y transporte de lípidos", subtitulo: "Luz intestinal • Emulsión micelar • Enterocito • Linfa quilífera", grupos: ["ruta_digestion_lipidos", "badge_via_18", "badge_leyenda_18"], color: "#0d9488" },
      "19": { numero: "19", id: "19", nombre: "Tejido adiposo (lipólisis ATGL/HSL/MGL)", subtitulo: "Gota lipídica • Cascada secuencial TAG ➔ DAG ➔ MAG ➔ Glicerol", grupos: ["ruta_tejido_adiposo", "badge_via_19", "badge_leyenda_19"], color: "#ea580c" },
      "20": { numero: "20", id: "20", nombre: "Músculo esquelético y sarcómero (Cori/Cahill)", subtitulo: "Sarcómero estriado en contracción • Cori (Lactato) • Cahill (Alanina)", grupos: ["ruta_musculo_esqueletico", "badge_via_20", "badge_leyenda_20"], color: "#9f1239" },
      "21": { numero: "21", id: "21", nombre: "Cerebro y combustibles neuronales", subtitulo: "Barrera hematoencefálica • GLUT1/3 • Adaptación a cuerpos cetónicos", grupos: ["ruta_cerebro_combustibles", "badge_via_21", "badge_leyenda_21"], color: "#2563eb" },
      "22": { numero: "22", id: "22", nombre: "Lipoproteínas plasmáticas (VLDL/LDL/HDL)", subtitulo: "VLDL ➔ LDL (LDLR) • HDL y transporte reverso de colesterol (SR-B1)", grupos: ["ruta_lipoproteinas", "badge_via_22", "badge_leyenda_22"], color: "#2563eb" },
      "23": { numero: "23", id: "23", nombre: "Biosíntesis de TAG y fosfolípidos (Kennedy)", subtitulo: "Glicerol-3-P ➔ LPA ➔ PA ➔ DAG ➔ TAG / Fosfatidilcolina", grupos: ["ruta_sintesis_tag_fosfolipidos", "badge_via_23", "badge_leyenda_23"], color: "#7c3aed" },
      "24": { numero: "24", id: "24", nombre: "Biosíntesis de aminoácidos no esenciales", subtitulo: "10 aminoácidos desde esqueletos de Glucólisis y Ciclo de Krebs", grupos: ["ruta_biosintesis_aminoacidos", "badge_via_24", "badge_leyenda_24"], color: "#059669" },
      "25": { numero: "25", id: "25", nombre: "Integración y conmutador nutricional", subtitulo: "Flujos de combustible: Posprandial vs Ayuno vs Ejercicio vigoroso", grupos: ["ruta_conmutador_estados", "badge_via_25", "badge_leyenda_25"], color: "#ea580c" }
    };

    const TABLA_ESTADOS_METABOLICOS = {
      normal: {
        id: "normal",
        nombre: "Normal (Mapa Completo)",
        subtitulo: "Visualización de referencia",
        descripcion: "Todas las 25 vías se muestran con su intensidad gráfica estándar.",
        activas: [],
        atenuadas: []
      },
      posprandial: {
        id: "posprandial",
        nombre: "Estado Posprandial",
        hormonas: "Insulina alta ↑ • Glucagón bajo ↓",
        descripcion: "Favorece utilización de glucosa, almacenamiento de glucógeno, lipogénesis, vía de pentosas, digestión lipídica (quilomicrones), VLDL, vía de Kennedy y biosíntesis de aminoácidos.",
        activas: ["1", "3", "4", "5", "6", "7", "10", "12", "18", "22", "23", "24"],
        atenuadas: ["2", "9", "11", "19"]
      },
      ayuno: {
        id: "ayuno",
        nombre: "Estado de Ayuno",
        hormonas: "Glucagón alto ↑ • Insulina baja ↓",
        descripcion: "Favorece gluconeogénesis hepática, lipólisis masiva adiposa (ATGL/HSL/MGL), β-oxidación, cetogénesis, ciclo de la urea, ciclo de Cori/Cahill muscular y adaptación cerebral a cetonas.",
        activas: ["2", "3", "9", "11", "14", "17", "19", "20", "21"],
        atenuadas: ["1", "10", "12", "18", "23"]
      }
    };

    // Variables de estado
    let viaResaltadaActual = null;
    let estadoMetabolicoActual = 'normal';
    let pointerDownX = 0;
    let pointerDownY = 0;
    let searchMatches = [];
    let searchMatchIndex = 0;
    let searchPulseElement = null;

    // Conjunto de todos los grupos registrados
    const TODOS_LOS_GRUPOS_VIAS = new Set();
    Object.values(TABLA_VIAS).forEach(v => {
      v.grupos.forEach(gid => TODOS_LOS_GRUPOS_VIAS.add(gid));
    });

    // Normalizador de texto
    function uiNormalize(str) {
      return (str || '')
        .normalize('NFD')
        .replace(/[\\u0300-\\u036f]/g, '')
        .toLowerCase()
        .trim();
    }

    // =========================================================================
    // 1. RESALTADO Y ATENUACIÓN DE VÍAS
    // =========================================================================
    function highlightPathway(viaId, shouldZoom = false) {
      const via = TABLA_VIAS[viaId];
      if (!via) return;

      viaResaltadaActual = viaId;

      TODOS_LOS_GRUPOS_VIAS.forEach(gid => {
        const el = document.getElementById(gid);
        if (el) {
          if (via.grupos.includes(gid)) {
            el.classList.add('ui_highlighted');
            el.classList.remove('ui_dimmed');
          } else {
            el.classList.add('ui_dimmed');
            el.classList.remove('ui_highlighted');
          }
        }
      });

      // Fondo y organelas
      const cxLayer = document.getElementById('capa_conexiones_inter_ruta');
      if (cxLayer) cxLayer.classList.add('ui_dimmed');

      const mitoBio = document.getElementById('mitocondria_biologica');
      const viasMito = ["2", "5", "6", "7", "8", "8B", "9", "11", "13", "14"];
      if (mitoBio) {
        if (viasMito.includes(viaId)) mitoBio.classList.remove('ui_dimmed');
        else mitoBio.classList.add('ui_dimmed');
      }

      // Gluconeogénesis: dejar glucólisis a 0.55
      const glucoTroncal = document.getElementById('ruta_glucolisis');
      if (glucoTroncal) {
        if (viaId === "2") {
          glucoTroncal.classList.remove('ui_dimmed');
          glucoTroncal.style.opacity = '0.55';
        } else {
          glucoTroncal.style.opacity = '';
        }
      }

      // Banner flotante
      const banner = document.getElementById('ui_highlight_banner');
      const bannerTitle = document.getElementById('ui_highlight_title');
      if (banner && bannerTitle) {
        bannerTitle.innerHTML = `<span style="background:${via.color}; color:#fff; border-radius:50%; width:20px; height:20px; display:inline-flex; align-items:center; justify-content:center; font-size:11px; font-weight:900; margin-right:8px;">${via.numero}</span> Vía ${via.numero}: ${via.nombre}`;
        banner.classList.add('ui_visible');
      }

      // Sidebar item activo
      document.querySelectorAll('.ui_sidebar_item').forEach(it => {
        if (it.getAttribute('data-via') === viaId) {
          it.classList.add('ui_active');
          it.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
        } else {
          it.classList.remove('ui_active');
        }
      });

      if (shouldZoom) {
        const mainEl = document.getElementById(via.grupos[0]);
        if (mainEl) zoomToElement(mainEl);
      }
    }

    function clearPathwayHighlight() {
      viaResaltadaActual = null;

      const glucoTroncal = document.getElementById('ruta_glucolisis');
      if (glucoTroncal) glucoTroncal.style.opacity = '';

      if (estadoMetabolicoActual !== 'normal') {
        setMetabolicState(estadoMetabolicoActual);
        const banner = document.getElementById('ui_highlight_banner');
        if (banner) banner.classList.remove('ui_visible');
        return;
      }

      TODOS_LOS_GRUPOS_VIAS.forEach(gid => {
        const el = document.getElementById(gid);
        if (el) {
          el.classList.remove('ui_dimmed');
          el.classList.remove('ui_highlighted');
        }
      });

      const cxLayer = document.getElementById('capa_conexiones_inter_ruta');
      if (cxLayer) cxLayer.classList.remove('ui_dimmed');
      const mitoBio = document.getElementById('mitocondria_biologica');
      if (mitoBio) mitoBio.classList.remove('ui_dimmed');

      const banner = document.getElementById('ui_highlight_banner');
      if (banner) banner.classList.remove('ui_visible');

      document.querySelectorAll('.ui_sidebar_item').forEach(it => it.classList.remove('ui_active'));
    }

    // =========================================================================
    // 2. ZOOM VECTORIAL CON MATRIZ CTM Y OFFSET DE LIENZO
    // =========================================================================
    function getElementSvgBounds(el) {
      try {
        const bbox = el.getBBox();
        const svg = document.querySelector('#panLayer svg');
        const ctm = el.getCTM();
        const svgCtm = svg ? svg.getCTM() : null;
        if (ctm && svgCtm) {
          const m = svgCtm.inverse().multiply(ctm);
          const pt1 = svg.createSVGPoint(); pt1.x = bbox.x; pt1.y = bbox.y;
          const pt2 = svg.createSVGPoint(); pt2.x = bbox.x + bbox.width; pt2.y = bbox.y + bbox.height;
          const p1 = pt1.matrixTransform(m);
          const p2 = pt2.matrixTransform(m);
          return {
            x: Math.min(p1.x, p2.x),
            y: Math.min(p1.y, p2.y),
            width: Math.abs(p2.x - p1.x),
            height: Math.abs(p2.y - p1.y)
          };
        }
        return bbox;
      } catch (e) {
        return null;
      }
    }

    function zoomToElement(el, paddingFactor = 1.6) {
      if (!el) return;
      const bounds = getElementSvgBounds(el);
      if (!bounds || bounds.width === 0 || bounds.height === 0) return;

      const vw = viewport.clientWidth;
      const vh = viewport.clientHeight;

      const targetScale = Math.min(
        Math.max((vw / (bounds.width * paddingFactor)), 0.35),
        2.5
      );

      const cx = bounds.x + bounds.width / 2;
      const cy = bounds.y + bounds.height / 2;

      // Conversión a coordenadas en panLayer teniendo en cuenta VB_X y VB_Y
      const px = cx - VB_X;
      const py = cy - VB_Y;

      scale = targetScale;
      pointX = vw / 2 - px * scale;
      pointY = vh / 2 - py * scale;
      updateTransform();
    }

    // =========================================================================
    // 3. PANEL LATERAL (ÍNDICE DE VÍAS)
    // =========================================================================
    function toggleSidebar() {
      const panel = document.getElementById('ui_sidebar_panel');
      const btn = document.getElementById('ui_btn_toggle_sidebar');
      if (!panel) return;
      panel.classList.toggle('ui_open');
      if (btn) btn.classList.toggle('ui_active');
    }

    function poblarSidebarVias() {
      const listEl = document.getElementById('ui_sidebar_list');
      if (!listEl) return;
      listEl.innerHTML = '';

      let viasCount = 0;
      Object.values(TABLA_VIAS).forEach(via => {
        const existeEnDoc = via.grupos.some(gid => document.getElementById(gid) !== null);
        if (!existeEnDoc) return;
        viasCount++;

        const item = document.createElement('div');
        item.className = 'ui_sidebar_item';
        item.setAttribute('data-via', via.id);
        item.onclick = () => {
          highlightPathway(via.id, true);
        };

        item.innerHTML = `
          <div class="ui_sidebar_badge" style="background: ${via.color}; color: #ffffff;">${via.numero}</div>
          <div class="ui_sidebar_info">
            <h4>${via.nombre}</h4>
            <p>${via.subtitulo}</p>
          </div>
        `;
        listEl.appendChild(item);
      });

      const btnToggle = document.getElementById('ui_btn_toggle_sidebar');
      if (btnToggle) {
        btnToggle.textContent = `📑 Vías (${viasCount})`;
        btnToggle.title = `Índice de Vías (${viasCount})`;
      }
    }

    function filtrarSidebarVias() {
      const input = document.getElementById('ui_sidebar_search');
      if (!input) return;
      const q = uiNormalize(input.value);
      document.querySelectorAll('.ui_sidebar_item').forEach(it => {
        const vid = it.getAttribute('data-via');
        const v = TABLA_VIAS[vid];
        if (!v) return;
        const texto = uiNormalize(v.numero + ' ' + v.nombre + ' ' + v.subtitulo);
        it.style.display = texto.includes(q) ? 'flex' : 'none';
      });
    }

    // =========================================================================
    // 4. BUSCADOR GLOBAL
    // =========================================================================
    let INDICE_BUSQUEDA = [];
    function construirIndiceBusqueda() {
      INDICE_BUSQUEDA = [];
      const svg = document.querySelector('#panLayer svg');
      if (!svg) return;

      const textNodes = svg.querySelectorAll('text');
      textNodes.forEach(tNode => {
        const raw = tNode.textContent.trim();
        if (!raw || raw.length < 2) return;
        const norm = uiNormalize(raw);
        const parentElem = tNode.closest('[id^="m_"], [id^="rx_"], [id^="ruta_"], [id^="lupa_"], .badge-via, .encabezado-seccion') || tNode;
        INDICE_BUSQUEDA.push({
          textoRaw: raw,
          textoNorm: norm,
          elemento: parentElem,
          textNode: tNode
        });
      });
    }

    function ejecutarBusqueda() {
      const input = document.getElementById('ui_search_input');
      const counter = document.getElementById('ui_search_counter');
      if (!input || !counter) return;

      const q = uiNormalize(input.value);

      if (searchPulseElement) {
        searchPulseElement.classList.remove('ui_search_pulse');
        searchPulseElement = null;
      }

      if (!q || q.length < 2) {
        searchMatches = [];
        searchMatchIndex = 0;
        counter.textContent = '';
        return;
      }

      const seen = new Set();
      searchMatches = [];
      INDICE_BUSQUEDA.forEach(item => {
        if (item.textoNorm.includes(q) && !seen.has(item.elemento)) {
          seen.add(item.elemento);
          searchMatches.push(item);
        }
      });

      if (searchMatches.length > 0) {
        searchMatchIndex = 0;
        irACoincidencia(searchMatchIndex);
      } else {
        counter.textContent = '0 de 0';
      }
    }

    function irACoincidencia(idx) {
      const counter = document.getElementById('ui_search_counter');
      if (searchMatches.length === 0) return;

      searchMatchIndex = (idx + searchMatches.length) % searchMatches.length;
      const match = searchMatches[searchMatchIndex];

      if (counter) counter.textContent = `${searchMatchIndex + 1} de ${searchMatches.length}`;

      if (searchPulseElement) searchPulseElement.classList.remove('ui_search_pulse');

      searchPulseElement = match.elemento;
      searchPulseElement.classList.add('ui_search_pulse');

      zoomToElement(match.elemento, 2.2);
    }

    function searchNext() {
      if (searchMatches.length > 0) irACoincidencia(searchMatchIndex + 1);
    }

    function searchPrev() {
      if (searchMatches.length > 0) irACoincidencia(searchMatchIndex - 1);
    }

    function clearSearch() {
      const input = document.getElementById('ui_search_input');
      const counter = document.getElementById('ui_search_counter');
      if (input) input.value = '';
      if (counter) counter.textContent = '';
      if (searchPulseElement) {
        searchPulseElement.classList.remove('ui_search_pulse');
        searchPulseElement = null;
      }
      searchMatches = [];
      searchMatchIndex = 0;
    }

    // =========================================================================
    // 5. FICHA FLOTANTE INTELIGENTE / TOOLTIP ESTEQUIOMÉTRICO
    // =========================================================================
    const tooltipEl = document.getElementById('ui_tooltip_card');
    let isTooltipPinned = false;
    let pinnedElement = null;

    function unpinTooltip() {
      isTooltipPinned = false;
      pinnedElement = null;
      if (tooltipEl) {
        tooltipEl.classList.remove('ui_tt_pinned');
        tooltipEl.style.pointerEvents = 'none';
        tooltipEl.style.display = 'none';
      }
    }

    function pinTooltip(el, mouseX, mouseY) {
      if (!tooltipEl) return;
      isTooltipPinned = true;
      pinnedElement = el;
      mostrarTooltip(el, mouseX, mouseY, true);
    }

    function buscarViaDeElemento(el) {
      const parentRuta = el.closest('[id^="ruta_"], [id^="lupa_"]');
      if (!parentRuta) return null;
      const rid = parentRuta.id;
      for (const via of Object.values(TABLA_VIAS)) {
        if (via.grupos.includes(rid)) return via;
      }
      return null;
    }

    function mostrarTooltip(el, mouseX, mouseY, pinned = false) {
      if (!tooltipEl || (isPanning && !isTooltipPinned)) return;
      if (isTooltipPinned && !pinned) return; // Si ya está fijada, no sobreescribir con hover

      const isMetabolito = el.id && el.id.startsWith('m_');
      const isEnzima = el.id && el.id.startsWith('rx_');
      if (!isMetabolito && !isEnzima) return;

      const via = buscarViaDeElemento(el);
      const textArr = Array.from(el.querySelectorAll('text')).map(t => t.textContent.trim()).filter(Boolean);

      let htmlContenido = '';
      const closeBtnHtml = pinned ? `<button class="ui_tt_close_btn" onclick="unpinTooltip()" title="Cerrar ficha (Esc)">✕</button>` : '';
      const pinHintHtml = !pinned 
        ? `<div class="ui_tt_pin_hint">Clic para fijar ficha y ver ecuación completa</div>` 
        : `<div class="ui_tt_pin_hint" style="color:#38bdf8;">Ficha fijada • Presiona Esc o clica fuera para cerrar</div>`;

      // CASO 1: REACCIÓN / ENZIMA CON ESTEQUIOMETRÍA
      if (isEnzima) {
        const rxData = (typeof TABLA_REACCIONES_ESTEQUIOMETRIA !== 'undefined') ? TABLA_REACCIONES_ESTEQUIOMETRIA[el.id] : null;
        const colorVia = via ? via.color : '#0284c7';
        const nombreVia = via ? `Vía ${via.numero}: ${via.nombre}` : (rxData ? rxData.via : 'Vía Metabólica');

        if (rxData) {
          const ecBadge = rxData.ec ? `<span class="ui_tt_badge_ec">${rxData.ec}</span>` : '';
          htmlContenido = `
            ${closeBtnHtml}
            <div class="ui_tt_header_row">
              <span class="ui_tt_badge_via" style="background:${colorVia}">${nombreVia}</span>
              ${ecBadge}
              <span style="font-size:9.5px; color:#94a3b8; margin-left:auto;">${rxData.compartimento || ''}</span>
            </div>
            <h4>${rxData.enzima}</h4>
            <div class="ui_tt_eq_box">
              <div class="ui_tt_eq_label">ECUACIÓN QUÍMICA BALANCEADA:</div>
              <div class="ui_tt_eq_text">${rxData.ecuacion}</div>
            </div>
            <div class="ui_tt_grid">
              <div class="ui_tt_grid_row"><span class="ui_tt_label">Sustratos:</span> <span class="ui_tt_val">${rxData.sustratos.join(', ')}</span></div>
              <div class="ui_tt_grid_row"><span class="ui_tt_label">Productos:</span> <span class="ui_tt_val" style="color:#38bdf8; font-weight:700;">${rxData.productos.join(', ')}</span></div>
              ${rxData.coproductos ? `<div class="ui_tt_grid_row"><span class="ui_tt_label">Coproductos:</span> <span class="ui_tt_val">${rxData.coproductos}</span></div>` : ''}
              ${rxData.deltaG ? `<div class="ui_tt_grid_row"><span class="ui_tt_label">Termodinámica:</span> <span class="ui_tt_val">${rxData.deltaG}</span></div>` : ''}
            </div>
            ${rxData.regulacion ? `<div class="ui_tt_reg_box"><strong style="color:#fbbf24;">Regulación:</strong> ${rxData.regulacion}</div>` : ''}
            ${rxData.relevancia ? `<div style="margin-top:6px; font-size:10px; color:#94a3b8; line-height:1.3;">${rxData.relevancia}</div>` : ''}
            ${pinHintHtml}
          `;
        } else {
          // Reacción sin ficha estequiométrica específica: extraer del SVG
          let titulo = textArr[0] || el.id;
          let sub = textArr.find(t => t.includes('EC ')) || '';
          let filas = textArr.filter(t => t !== titulo && t !== sub).map(t => `<div class="ui_tt_row">• ${t}</div>`).join('');
          htmlContenido = `
            ${closeBtnHtml}
            <div class="ui_tt_header_row">
              <span class="ui_tt_badge_via" style="background:${colorVia}">${nombreVia}</span>
              ${sub ? `<span class="ui_tt_badge_ec">${sub}</span>` : ''}
            </div>
            <h4>${titulo}</h4>
            ${filas}
            ${pinHintHtml}
          `;
        }
      } else {
        // CASO 2: METABOLITO
        const formulaAtoms = new Set(['O', 'H', 'OH', 'HO', 'CH₂OH', 'Ⓟ', 'O-PO₃²⁻', 'NH₃⁺', 'COO⁻', 'CH₂', 'CH₃']);
        const realNames = textArr.filter(t => !formulaAtoms.has(t) && !t.startsWith('[') && !t.endsWith(']'));
        let titulo = realNames[0] || textArr[0] || el.id;
        const carbonTag = textArr.find(t => t.startsWith('[') && t.endsWith(']'));
        const colorVia = via ? via.color : '#0284c7';
        const nombreVia = via ? `Vía ${via.numero}: ${via.nombre}` : 'Metabolito Intermediario';

        let filas = [];
        textArr.forEach(t => {
          if (t !== titulo && t !== carbonTag && !formulaAtoms.has(t)) {
            filas.push(`<div class="ui_tt_row">• ${t}</div>`);
          }
        });

        htmlContenido = `
          ${closeBtnHtml}
          <div class="ui_tt_header_row">
            <span class="ui_tt_badge_via" style="background:${colorVia}">${nombreVia}</span>
            ${carbonTag ? `<span class="ui_tt_badge_ec" style="background:#0f766e; border-color:#14b8a6; color:#ccfbf1;">${carbonTag} Carbonos</span>` : ''}
          </div>
          <h4>${titulo}</h4>
          ${filas.join('')}
          ${pinHintHtml}
        `;
      }

      tooltipEl.innerHTML = htmlContenido;
      if (pinned) {
        tooltipEl.classList.add('ui_tt_pinned');
      } else {
        tooltipEl.classList.remove('ui_tt_pinned');
      }

      tooltipEl.style.display = 'block';
      const tw = tooltipEl.offsetWidth || 340;
      const th = tooltipEl.offsetHeight || 160;
      let left = mouseX + 16;
      let top = mouseY + 16;
      if (left + tw > window.innerWidth - 14) left = mouseX - tw - 16;
      if (top + th > window.innerHeight - 14) top = mouseY - th - 16;
      tooltipEl.style.left = `${Math.max(12, left)}px`;
      tooltipEl.style.top = `${Math.max(12, top)}px`;
    }

    function ocultarTooltip() {
      if (tooltipEl && !isTooltipPinned) tooltipEl.style.display = 'none';
    }

    // =========================================================================
    // 6. ESTADOS METABÓLICOS
    // =========================================================================
    function setMetabolicState(stateId) {
      const st = TABLA_ESTADOS_METABOLICOS[stateId] || TABLA_ESTADOS_METABOLICOS.normal;
      estadoMetabolicoActual = st.id;

      document.querySelectorAll('.ui_state_btn').forEach(btn => {
        if (btn.id === `ui_btn_state_${st.id === 'posprandial' ? 'fed' : st.id === 'ayuno' ? 'fasting' : 'normal'}`) {
          btn.classList.add('ui_active');
        } else {
          btn.classList.remove('ui_active');
        }
      });

      const banner = document.getElementById('ui_state_banner');
      const bannerText = document.getElementById('ui_state_banner_text');

      if (st.id === 'normal') {
        TODOS_LOS_GRUPOS_VIAS.forEach(gid => {
          const el = document.getElementById(gid);
          if (el) {
            el.classList.remove('ui_dimmed');
            el.classList.remove('ui_state_active');
          }
        });
        const cxLayer = document.getElementById('capa_conexiones_inter_ruta');
        if (cxLayer) cxLayer.classList.remove('ui_dimmed');
        const mitoBio = document.getElementById('mitocondria_biologica');
        if (mitoBio) mitoBio.classList.remove('ui_dimmed');
        if (banner) banner.classList.remove('ui_visible');
        return;
      }

      const gruposActivos = new Set();
      st.activas.forEach(vid => {
        const v = TABLA_VIAS[vid];
        if (v) v.grupos.forEach(gid => gruposActivos.add(gid));
      });

      const gruposAtenuados = new Set();
      st.atenuadas.forEach(vid => {
        const v = TABLA_VIAS[vid];
        if (v) v.grupos.forEach(gid => gruposAtenuados.add(gid));
      });

      TODOS_LOS_GRUPOS_VIAS.forEach(gid => {
        const el = document.getElementById(gid);
        if (el) {
          if (gruposActivos.has(gid)) {
            el.classList.add('ui_state_active');
            el.classList.remove('ui_dimmed');
          } else if (gruposAtenuados.has(gid)) {
            el.classList.add('ui_dimmed');
            el.classList.remove('ui_state_active');
          } else {
            el.classList.add('ui_dimmed');
            el.classList.remove('ui_state_active');
          }
        }
      });

      if (banner && bannerText) {
        bannerText.innerHTML = `<strong>${st.nombre} (${st.hormonas})</strong> • ${st.descripcion}`;
        banner.classList.add('ui_visible');
      }
    }

    // =========================================================================
    // 7. DISTINCIÓN CLIC VS ARRASTRE Y EVENTOS DE INTERACCIÓN
    // =========================================================================
    function manejarClicEnLienzo(e, clientX, clientY) {
      const target = document.elementFromPoint(clientX, clientY);
      if (!target) return;

      // Clic en badge de vía (en mapa, leyenda o encabezado)
      const badge = target.closest('.badge-via');
      if (badge) {
        const dataVia = badge.getAttribute('data-via');
        if (dataVia && TABLA_VIAS[dataVia]) {
          highlightPathway(dataVia, false);
          return;
        }
        const viaEntry = Object.values(TABLA_VIAS).find(v => v.grupos.includes(badge.id));
        if (viaEntry) {
          highlightPathway(viaEntry.id, false);
          return;
        }
      }

      // Clic en encabezado de sección
      const enc = target.closest('.encabezado-seccion');
      if (enc) {
        const badgeChild = enc.querySelector('.badge-via');
        if (badgeChild) {
          const dataVia = badgeChild.getAttribute('data-via');
          if (dataVia && TABLA_VIAS[dataVia]) {
            highlightPathway(dataVia, false);
            return;
          }
          const viaEntry = Object.values(TABLA_VIAS).find(v => v.grupos.includes(badgeChild.id));
          if (viaEntry) {
            highlightPathway(viaEntry.id, false);
            return;
          }
        }
      }

      // Clic en ruta o sección
      const ruta = target.closest('[id^="ruta_"], [id^="lupa_"]');
      if (ruta) {
        const viaEntry = Object.values(TABLA_VIAS).find(v => v.grupos.includes(ruta.id));
        if (viaEntry) {
          highlightPathway(viaEntry.id, false);
          return;
        }
      }

      // Clic en enzima o metabolito -> FIJAR FICHA ESTEQUIOMÉTRICA
      const targetRx = target.closest('[id^="rx_"], [id^="m_"]');
      if (targetRx) {
        pinTooltip(targetRx, clickX, clickY);
        return;
      }

      // Clic fuera de reacción y fuera de tooltip -> desanclar ficha
      if (!target.closest('#ui_tooltip_card')) {
        unpinTooltip();
      }

      // Clic en fondo o espacio vacío
      if (target.tagName === 'svg' || target.id === 'viewport' || target.id === 'panLayer' || target.id === 'print_fondo_base' || target.id === 'print_fondo_izq' || target.id === 'print_fondo_der' || target.tagName === 'rect') {
        clearPathwayHighlight();
      }
    }

    viewport.addEventListener('mousedown', (e) => {
      if (e.target.closest('#ui_sidebar_panel, .header-bar, #ui_btn_sidebar_floating, #ui_highlight_banner, #ui_state_banner, #ui_tooltip_card')) return;
      isPanning = true;
      startX = e.clientX - pointX;
      startY = e.clientY - pointY;
      pointerDownX = e.clientX;
      pointerDownY = e.clientY;
      viewport.classList.add('grabbing');
    });

    window.addEventListener('mousemove', (e) => {
      if (!isPanning) return;
      pointX = e.clientX - startX;
      pointY = e.clientY - startY;
      updateTransform();
    });

    window.addEventListener('mouseup', (e) => {
      if (isPanning) {
        isPanning = false;
        viewport.classList.remove('grabbing');
        const dist = Math.hypot(e.clientX - pointerDownX, e.clientY - pointerDownY);
        if (dist <= 4) {
          manejarClicEnLienzo(e, e.clientX, e.clientY);
        }
      }
    });

    viewport.addEventListener('wheel', (e) => {
      e.preventDefault();
      const xs = (e.clientX - pointX) / scale;
      const ys = (e.clientY - pointY) / scale;
      const delta = -e.deltaY;
      const factor = delta > 0 ? 1.15 : 0.85;
      scale = Math.min(Math.max(scale * factor, 0.08), 5.0);
      pointX = e.clientX - xs * scale;
      pointY = e.clientY - ys * scale;
      updateTransform();
    }, { passive: false });

    // Tooltip en movimiento de ratón
    viewport.addEventListener('mousemove', (e) => {
      if (isPanning) {
        if (!isTooltipPinned) ocultarTooltip();
        return;
      }
      if (isTooltipPinned) return; // Si está fijada, no la movemos con el cursor
      const target = e.target.closest('[id^="m_"], [id^="rx_"]');
      if (target) {
        mostrarTooltip(target, e.clientX, e.clientY, false);
      } else {
        ocultarTooltip();
      }
    });

    viewport.addEventListener('mouseleave', () => {
      if (!isTooltipPinned) ocultarTooltip();
    });

    // =========================================================================
    // 8. SOPORTE TÁCTIL (PAN Y PELLIZCO PARA ZOOM)
    // =========================================================================
    let touchPinching = false;
    let touchStartDist = 0;
    let touchStartScale = 1;
    let touchMidX = 0;
    let touchMidY = 0;

    viewport.addEventListener('touchstart', (e) => {
      ocultarTooltip();
      if (e.target.closest('#ui_sidebar_panel, .header-bar, #ui_btn_sidebar_floating, #ui_highlight_banner, #ui_state_banner, #ui_tooltip_card')) return;
      if (e.touches.length === 1) {
        isPanning = true;
        startX = e.touches[0].clientX - pointX;
        startY = e.touches[0].clientY - pointY;
        pointerDownX = e.touches[0].clientX;
        pointerDownY = e.touches[0].clientY;
      } else if (e.touches.length === 2) {
        isPanning = false;
        touchPinching = true;
        touchStartDist = Math.hypot(
          e.touches[0].clientX - e.touches[1].clientX,
          e.touches[0].clientY - e.touches[1].clientY
        );
        touchStartScale = scale;
        touchMidX = (e.touches[0].clientX + e.touches[1].clientX) / 2;
        touchMidY = (e.touches[0].clientY + e.touches[1].clientY) / 2;
      }
    }, { passive: true });

    viewport.addEventListener('touchmove', (e) => {
      if (isPanning && e.touches.length === 1) {
        pointX = e.touches[0].clientX - startX;
        pointY = e.touches[0].clientY - startY;
        updateTransform();
      } else if (touchPinching && e.touches.length === 2) {
        const curDist = Math.hypot(
          e.touches[0].clientX - e.touches[1].clientX,
          e.touches[0].clientY - e.touches[1].clientY
        );
        const xs = (touchMidX - pointX) / scale;
        const ys = (touchMidY - pointY) / scale;
        const newScale = Math.min(Math.max(touchStartScale * (curDist / touchStartDist), 0.08), 5.0);
        scale = newScale;
        pointX = touchMidX - xs * scale;
        pointY = touchMidY - ys * scale;
        updateTransform();
      }
    }, { passive: true });

    viewport.addEventListener('touchend', (e) => {
      if (isPanning && e.changedTouches.length === 1) {
        isPanning = false;
        const dist = Math.hypot(e.changedTouches[0].clientX - pointerDownX, e.changedTouches[0].clientY - pointerDownY);
        if (dist <= 6) {
          manejarClicEnLienzo(e, e.changedTouches[0].clientX, e.changedTouches[0].clientY);
        }
      }
      if (e.touches.length < 2) touchPinching = false;
    });

    // =========================================================================
    // 9. ATAJOS DE TECLADO
    // =========================================================================
    window.addEventListener('keydown', (e) => {
      const activeTag = document.activeElement ? document.activeElement.tagName.toLowerCase() : '';
      if (activeTag === 'input' || activeTag === 'textarea') {
        if (e.key === 'Escape') {
          document.activeElement.blur();
          clearSearch();
        } else if (e.key === 'Enter') {
          e.preventDefault();
          if (e.shiftKey) searchPrev();
          else searchNext();
        }
        return;
      }

      if (e.key === '/') {
        e.preventDefault();
        const searchInput = document.getElementById('ui_search_input');
        if (searchInput) searchInput.focus();
      } else if (e.key === 'Escape') {
        unpinTooltip();
        clearPathwayHighlight();
        clearSearch();
        const panel = document.getElementById('ui_sidebar_panel');
        if (panel && panel.classList.contains('ui_open')) toggleSidebar();
        const menuViews = document.getElementById('ui_menu_views');
        if (menuViews) menuViews.style.display = 'none';
      } else if (e.key.toLowerCase() === 'f') {
        fitView();
      }
    });

    // Dropdown menú de vistas
    function toggleMenuViews(event) {
      event.stopPropagation();
      const menu = document.getElementById('ui_menu_views');
      if (menu) menu.style.display = menu.style.display === 'block' ? 'none' : 'block';
    }
    document.addEventListener('click', () => {
      const menu = document.getElementById('ui_menu_views');
      if (menu) menu.style.display = 'none';
    });

    // Inicialización del buscador y vista
    const searchInputEl = document.getElementById('ui_search_input');
    if (searchInputEl) {
      searchInputEl.addEventListener('input', ejecutarBusqueda);
    }

    window.addEventListener('resize', fitView);

    window.addEventListener('DOMContentLoaded', () => {
      poblarSidebarVias();
      construirIndiceBusqueda();
      fitView();
    });

    // Por si el DOM ya estaba listo
    if (document.readyState !== 'loading') {
      poblarSidebarVias();
      construirIndiceBusqueda();
      fitView();
    }
  </script>
</body>
</html>"""

    # Reemplazar marcadores
    html_res = html_plantilla
    html_res = html_res.replace("__W_CANVAS__", str(w_canvas))
    html_res = html_res.replace("__H_CANVAS__", str(h_canvas))
    html_res = html_res.replace("__VB_X__", str(vb_x))
    html_res = html_res.replace("__VB_Y__", str(vb_y))
    html_res = html_res.replace("__TABLA_REACCIONES_JSON__", json.dumps(TABLA_REACCIONES_DATA, ensure_ascii=False))
    html_res = html_res.replace("__SVG_FINAL__", svg_final)
    return html_res
