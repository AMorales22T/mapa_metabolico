# =============================================================================
# MÓDULO DE REVISIÓN: Defs SVG, Marcadores de Flechas y Ensamblaje Final
# =============================================================================
# Archivo original : scripts_generacion/generar_prueba_visual_integrada.py (líneas 3716 a 4188 de 4188)
# Descripción      : Definición de gradientes, sombras, puntas de flecha y envoltura HTML/SVG del mapa central.
# =============================================================================

    # 14. BLOQUE INSTITUCIONAL Y AUTORÍA DE CÓDIGO ABIERTO
    partes.append(generar_bloque_leyenda(100, 4220))
    partes.append(generar_bloque_autoria(3800, 4220))
    partes.append('</g> <!-- Fin entorno_hepatocito -->')

    # Defs y Marcadores
    defs_svg = f"""
    <defs>
      <marker id="arrowFlow" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
        <path d="M 0 0 L 6 3 L 0 6 Z" fill="#ea580c" />
      </marker>
      <marker id="arrowTeal" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
        <path d="M 0 0 L 6 3 L 0 6 Z" fill="#0d9488" />
      </marker>
      <marker id="arrowBlueAmino" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
        <path d="M 0 0 L 6 3 L 0 6 Z" fill="#2563eb" />
      </marker>
      <marker id="arrowCobalt" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
        <path d="M 0 0 L 6 3 L 0 6 Z" fill="#1d4ed8" />
      </marker>
      <marker id="arrowSlate" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
        <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#475569" />
      </marker>
      <marker id="arrowRed" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
        <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#dc2626" />
      </marker>
      <marker id="arrowGreen" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
        <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#059669" />
      </marker>
      <marker id="arrowBlue" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
        <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#0284c7" />
      </marker>
      <marker id="arrowPurple" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
        <path d="M 0 0 L 6 3 L 0 6 Z" fill="#7c3aed" />
      </marker>
      <marker id="arrowAmber" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
        <path d="M 0 0 L 6 3 L 0 6 Z" fill="#b45309" />
      </marker>

      <linearGradient id="gradMiocitoCori" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#fff1f2" stop-opacity="0.95" />
        <stop offset="100%" stop-color="#ffe4e6" stop-opacity="0.9" />
      </linearGradient>

      <!-- Gradientes histológicos anatómicos del músculo esquelético -->
      <linearGradient id="gradVientreMuscular" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#fff1f2" stop-opacity="0.96" />
        <stop offset="30%" stop-color="#ffe4e6" stop-opacity="0.92" />
        <stop offset="70%" stop-color="#fecdd3" stop-opacity="0.88" />
        <stop offset="100%" stop-color="#fda4af" stop-opacity="0.82" />
      </linearGradient>

      <linearGradient id="gradFasciaTendinosa" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#f1f5f9" stop-opacity="0.95"/>
        <stop offset="45%" stop-color="#e2e8f0" stop-opacity="0.9"/>
        <stop offset="100%" stop-color="#fff1f2" stop-opacity="0.1"/>
      </linearGradient>

      <linearGradient id="gradSarcoplasma" x1="0%" y1="0%" x2="0%" y2="100%">
        <stop offset="0%" stop-color="#fff5f5" stop-opacity="0.95" />
        <stop offset="50%" stop-color="#ffe4e6" stop-opacity="0.75" />
        <stop offset="100%" stop-color="#fff1f2" stop-opacity="0.95" />
      </linearGradient>

      <linearGradient id="gradCapilarMuscular" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#7f1d1d" stop-opacity="0.9" />
        <stop offset="50%" stop-color="#991b1b" stop-opacity="0.8" />
        <stop offset="100%" stop-color="#b91c1c" stop-opacity="0.85" />
      </linearGradient>

      <linearGradient id="gradHeaderAutoria" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#0284c7" />
        <stop offset="50%" stop-color="#0d9488" />
        <stop offset="100%" stop-color="#10b981" />
      </linearGradient>

      <filter id="shadowCard" x="-5%" y="-5%" width="110%" height="115%">
        <feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="#0f172a" flood-opacity="0.12" />
      </filter>

      <linearGradient id="gradCitosolUnificado" x1="0%" y1="0%" x2="0%" y2="100%">
        <stop offset="0%" stop-color="#f8fafc" stop-opacity="1" />
        <stop offset="15%" stop-color="#f1f5f9" stop-opacity="0.8" />
        <stop offset="50%" stop-color="#f8fafc" stop-opacity="0.6" />
        <stop offset="85%" stop-color="#f1f5f9" stop-opacity="0.75" />
        <stop offset="100%" stop-color="#f8fafc" stop-opacity="1" />
      </linearGradient>

      <radialGradient id="haloCitosolUnificado" cx="50%" cy="48%" r="72%">
        <stop offset="0%" stop-color="#e2e8f0" stop-opacity="0.22" />
        <stop offset="55%" stop-color="#f1f5f9" stop-opacity="0.10" />
        <stop offset="100%" stop-color="#ffffff" stop-opacity="0" />
      </radialGradient>

      <radialGradient id="gradMitocondria" cx="50%" cy="100%" r="90%">
        <stop offset="0%" stop-color="#fef3c7" stop-opacity="1" />
        <stop offset="45%" stop-color="#fffbeb" stop-opacity="0.95" />
        <stop offset="75%" stop-color="#fed7aa" stop-opacity="0.9" />
        <stop offset="100%" stop-color="#f59e0b" stop-opacity="0.8" />
      </radialGradient>

      <linearGradient id="gradTorrenteSanguineo" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#7f1d1d" stop-opacity="0.95" />
        <stop offset="15%" stop-color="#991b1b" stop-opacity="0.9" />
        <stop offset="50%" stop-color="#b91c1c" stop-opacity="0.85" />
        <stop offset="85%" stop-color="#991b1b" stop-opacity="0.9" />
        <stop offset="100%" stop-color="#7f1d1d" stop-opacity="0.95" />
      </linearGradient>

      <linearGradient id="gradPlasmaSanguineo" x1="0%" y1="0%" x2="0%" y2="100%">
        <stop offset="0%" stop-color="#450a0a" stop-opacity="0.95" />
        <stop offset="60%" stop-color="#7f1d1d" stop-opacity="0.88" />
        <stop offset="100%" stop-color="#991b1b" stop-opacity="0.82" />
      </linearGradient>

      <radialGradient id="gradEritrocito" cx="38%" cy="38%" r="62%">
        <stop offset="0%" stop-color="#ef4444" stop-opacity="0.95" />
        <stop offset="45%" stop-color="#dc2626" stop-opacity="0.9" />
        <stop offset="70%" stop-color="#b91c1c" stop-opacity="0.95" />
        <stop offset="100%" stop-color="#7f1d1d" stop-opacity="1" />
      </radialGradient>

      <radialGradient id="gradEritrocitoCentro" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stop-color="#7f1d1d" stop-opacity="0.8" />
        <stop offset="100%" stop-color="#ef4444" stop-opacity="0" />
      </radialGradient>

      <!-- Defs originales de la Cadena Transportadora de Electrones del usuario -->
      {cte_defs}
    </defs>
    """

    svg_completo = f"""<svg width="{ANCHO_CANVAS}" height="{ALTO_CANVAS}" viewBox="0 0 {ANCHO_CANVAS} {ALTO_CANVAS}" xmlns="http://www.w3.org/2000/svg">
      {defs_svg}
      {''.join(partes)}
    </svg>"""

    html_out = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Prueba Visual Integrada — Entorno Celular Real (Sin Globos)</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@600;700;800&display=swap" rel="stylesheet">
  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: 'Inter', sans-serif;
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
    .controls {{
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .controls button {{
      background: #0284c7;
      color: #ffffff;
      border: none;
      padding: 6px 12px;
      border-radius: 6px;
      font-weight: 800;
      font-size: 0.82rem;
      cursor: pointer;
    }}
    .controls button:hover {{ background: #0369a1; }}
    #zoomLevel {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.85rem;
      font-weight: 800;
      color: #38bdf8;
      min-width: 52px;
      text-align: center;
    }}
    .viewport {{
      flex: 1;
      width: 100%;
      overflow: hidden;
      position: relative;
      cursor: grab;
      background: #1e293b;
    }}
    .viewport.grabbing {{ cursor: grabbing; }}
    #panLayer {{
      position: absolute;
      top: 0;
      left: 0;
      transform-origin: 0 0;
      width: {ANCHO_CANVAS}px;
      height: {ALTO_CANVAS}px;
    }}
    svg {{ display: block; width: 100%; height: 100%; }}
  </style>
</head>
<body>
  <div class="header-bar">
    <div>
      <h2 style="color: #38bdf8; font-size: 1.1rem;">Entorno Celular: Citosol y Gran Mitocondria</h2>
      <p style="color: #94a3b8; font-size: 0.78rem;">Glucólisis • Glucógeno • Pentosas • Lanzadera • Krebs • Cadena Respiratoria • β-Oxidación • Cetogénesis</p>
    </div>
    <div class="controls">
      <button onclick="zoomOut()">−</button>
      <span id="zoomLevel">100%</span>
      <button onclick="zoomIn()">+</button>
      <button onclick="resetView()">Reset</button>
      <button style="background: #16a34a;" onclick="fitView()">Ajustar</button>
      <div style="width: 1px; height: 20px; background: #475569; margin: 0 4px;"></div>
      <button id="btnCopiarSvg" style="background: #7c3aed;" onclick="copiarSvgModificado()">💾 Copiar SVG</button>
      <button id="btnCopiarJson" style="background: #0284c7;" onclick="copiarAjustesJson()">📋 Copiar Ajustes JSON</button>
      <button style="background: #dc2626;" onclick="resetearPosiciones()">↺ Resetear Ajustes</button>
      <span id="statusStorage" style="font-size: 0.75rem; color: #a7f3d0; margin-left: 6px;"></span>
    </div>
  </div>
  <div class="viewport" id="viewport">
    <div id="panLayer">
      {svg_completo}
    </div>
  </div>

  <script>
    const viewport = document.getElementById('viewport');
    const panLayer = document.getElementById('panLayer');
    const zoomLevelEl = document.getElementById('zoomLevel');
    const statusStorage = document.getElementById('statusStorage');
    
    let scale = 1;
    let pointX = 0;
    let pointY = 0;
    let startX = 0;
    let startY = 0;
    let isPanning = false;

    // --- SISTEMA DE ARRASTRE Y PERSISTENCIA (localStorage) ---
    const STORAGE_KEY = 'mapa_metabolico_offsets_v1';
    let offsetsGuardados = {{}};
    try {{
      offsetsGuardados = JSON.parse(localStorage.getItem(STORAGE_KEY) || '{{}}');
    }} catch (e) {{
      offsetsGuardados = {{}};
    }}

    let arrastrandoElemento = null;
    let dragStartX = 0;
    let dragStartY = 0;
    let elemOrigTx = 0;
    let elemOrigTy = 0;

    function parseTranslate(transformAttr) {{
      if (!transformAttr) return {{ x: 0, y: 0 }};
      const m = transformAttr.match(/translate\\(([-0-9.]+)[,\\s]+([-0-9.]+)\\)/);
      if (m) return {{ x: parseFloat(m[1]), y: parseFloat(m[2]) }};
      return {{ x: 0, y: 0 }};
    }}

    function aplicarOffsetsGuardados() {{
      let count = 0;
      for (const [id, offset] of Object.entries(offsetsGuardados)) {{
        const el = document.getElementById(id);
        if (el) {{
          if (!el.hasAttribute('data-base-transform')) {{
            el.setAttribute('data-base-transform', el.getAttribute('transform') || '');
          }}
          const baseTrans = el.getAttribute('data-base-transform');
          const base = parseTranslate(baseTrans);
          const finalX = base.x + offset.dx;
          const finalY = base.y + offset.dy;
          const otherTransforms = baseTrans.replace(/translate\\([ -0-9.,]+\\)/g, '').trim();
          el.setAttribute('transform', `translate(${{finalX}}, ${{finalY}}) ${{otherTransforms}}`.trim());
          count++;
        }}
      }}
      if (count > 0 && statusStorage) {{
        statusStorage.textContent = `✓ ${{count}} elementos restaurados`;
      }}
    }}

    function guardarOffset(id, dx, dy) {{
      offsetsGuardados[id] = {{ dx, dy }};
      localStorage.setItem(STORAGE_KEY, JSON.stringify(offsetsGuardados));
      const count = Object.keys(offsetsGuardados).length;
      if (statusStorage) statusStorage.textContent = `✓ Guardado (${{count}} movidos)`;
    }}

    function resetearPosiciones() {{
      if (confirm("¿Deseas resetear todas las posiciones manuales y volver al diseño original?")) {{
        localStorage.removeItem(STORAGE_KEY);
        offsetsGuardados = {{}};
        location.reload();
      }}
    }}

    function copiarAjustesJson() {{
      const dataStr = JSON.stringify(offsetsGuardados, null, 2);
      navigator.clipboard.writeText(dataStr).then(() => {{
        alert("¡Ajustes copiados al portapapeles en formato JSON! Puedes pegarlos en el chat.");
      }}).catch(() => {{
        prompt("Copia los ajustes JSON:", dataStr);
      }});
    }}

    function copiarSvgModificado() {{
      const svgEl = document.querySelector('#panLayer svg');
      if (!svgEl) return;
      const svgText = svgEl.outerHTML;
      navigator.clipboard.writeText(svgText).then(() => {{
        alert("¡SVG completo con tus posiciones exactas copiado al portapapeles!");
      }}).catch(() => {{
        alert("No se pudo copiar automáticamente. Puedes usar la consola del navegador.");
      }});
    }}

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
      scale = Math.max(0.15, Math.min(scale, 5));

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
      scale = Math.min(vw / {ANCHO_CANVAS}, vh / {ALTO_CANVAS});
      pointX = (vw - {ANCHO_CANVAS} * scale) / 2;
      pointY = (vh - {ALTO_CANVAS} * scale) / 2;
      updateTransform();
    }}

    viewport.addEventListener('wheel', (e) => {{
      e.preventDefault();
      const delta = e.deltaY < 0 ? 1.15 : 0.85;
      zoom(delta, e.clientX, e.clientY);
    }}, {{ passive: false }});

    viewport.addEventListener('mousedown', (e) => {{
      if (e.button !== 0) return;

      // Comprobar si el clic fue en un elemento arrastrable
      const arrastrable = e.target.closest('[data-arrastrable="1"]');
      if (arrastrable && arrastrable.id) {{
        arrastrandoElemento = arrastrable;
        dragStartX = e.clientX;
        dragStartY = e.clientY;

        if (!arrastrable.hasAttribute('data-base-transform')) {{
          arrastrable.setAttribute('data-base-transform', arrastrable.getAttribute('transform') || '');
        }}

        const baseTrans = arrastrable.getAttribute('data-base-transform');
        const base = parseTranslate(baseTrans);
        const currentOffset = offsetsGuardados[arrastrable.id] || {{ dx: 0, dy: 0 }};
        elemOrigTx = base.x + currentOffset.dx;
        elemOrigTy = base.y + currentOffset.dy;

        arrastrable.style.cursor = 'grabbing';
        e.stopPropagation();
        return;
      }}

      isPanning = true;
      startX = e.clientX - pointX;
      startY = e.clientY - pointY;
      viewport.classList.add('grabbing');
    }});

    window.addEventListener('mousemove', (e) => {{
      if (arrastrandoElemento) {{
        const dxScreen = e.clientX - dragStartX;
        const dyScreen = e.clientY - dragStartY;
        const dxSvg = dxScreen / scale;
        const dySvg = dyScreen / scale;

        const baseTrans = arrastrandoElemento.getAttribute('data-base-transform');
        const base = parseTranslate(baseTrans);
        const totalDx = (elemOrigTx - base.x) + dxSvg;
        const totalDy = (elemOrigTy - base.y) + dySvg;

        const finalX = base.x + totalDx;
        const finalY = base.y + totalDy;
        const otherTransforms = baseTrans.replace(/translate\\([ -0-9.,]+\\)/g, '').trim();
        arrastrandoElemento.setAttribute('transform', `translate(${{finalX}}, ${{finalY}}) ${{otherTransforms}}`.trim());
        return;
      }}

      if (!isPanning) return;
      pointX = e.clientX - startX;
      pointY = e.clientY - startY;
      updateTransform();
    }});

    window.addEventListener('mouseup', (e) => {{
      if (arrastrandoElemento) {{
        const dxScreen = e.clientX - dragStartX;
        const dyScreen = e.clientY - dragStartY;
        const dxSvg = dxScreen / scale;
        const dySvg = dyScreen / scale;

        const baseTrans = arrastrandoElemento.getAttribute('data-base-transform');
        const base = parseTranslate(baseTrans);
        const totalDx = Math.round((elemOrigTx - base.x) + dxSvg);
        const totalDy = Math.round((elemOrigTy - base.y) + dySvg);

        guardarOffset(arrastrandoElemento.id, totalDx, totalDy);
        arrastrandoElemento.style.cursor = '';
        arrastrandoElemento = null;
        return;
      }}

      isPanning = false;
      viewport.classList.remove('grabbing');
    }});

    // Ajustar vista y restaurar posiciones manuales al inicio
    window.addEventListener('load', () => {{
      fitView();
      aplicarOffsetsGuardados();
    }});
  </script>
</body>
</html>
"""
    return html_out, svg_completo

if __name__ == "__main__":
    html_str, svg_str = construir_mapa_organico()
    
    ruta_html = os.path.join(DIR_HTML, "prueba_visual_integrada.html")
    with open(ruta_html, "w", encoding="utf-8") as f:
        f.write(html_str)

    ruta_svg = os.path.join(DIR_HTML, "prueba_visual_integrada.svg")
    with open(ruta_svg, "w", encoding="utf-8") as f:
        f.write(svg_str)

    print(f"Mapa Orgánico Celular generado en HTML: {ruta_html}")
    print(f"Mapa Orgánico Celular generado en SVG: {ruta_svg}")
