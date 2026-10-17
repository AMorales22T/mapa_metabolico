# =============================================================================
# MÓDULO DE REVISIÓN: Generador de la Lanzadera Glicerol-3-Fosfato
# =============================================================================
# Archivo original : 02_RESPIRACION_Y_ENERGIA/via_08_lanzaderas/generar_lanzadera_glicerol_p.py (líneas 1 a 337 de 337)
# Descripción      : Transferencia rápida vía FADH2 y CoQ en músculo esquelético y cerebro.
# =============================================================================

#!/usr/bin/env python3
"""
GENERADOR VECTORIAL DE LA LANZADERA DE GLICEROL-3-FOSFATO (SVG / HTML)
======================================================================
Ruta metabólica individual: Lanzadera mitocondrial predominante en músculo
esquelético y cerebro para la reoxidación ultrarrápida del NADH citosólico.

ESTILO VISUAL EDITORIAL IDÉNTICO A LA GLUCÓLISIS Y MALATO-ASPARTATO:
- Moléculas suspendidas libremente sin cajas cuadradas artificiales.
- Tipografía Inter (800) y JetBrains Mono para enzimas, EC y cofactores.
- Membrana Mitocondrial Externa (con porinas VDAC) y Membrana Interna (MMI).
- Flavoproteína mGPDH anclada a la MMI entregando electrones a la Coenzima Q.
- Balance energético de 1.5 ATP / NADH citosólico claramente contrastado.
"""

import os
import subprocess
from estructuras_lanzadera import (
    DIHIDROXIACETONA_FOSFATO,
    GLICEROL_3_FOSFATO
)

ANCHO = 1380
ALTO = 680

CABECERA_HTML = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Lanzadera de Glicerol-3-Fosfato | Mapa Metabólico</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;600;700;800&display=swap" rel="stylesheet">
  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: 'Inter', sans-serif;
      background: #e2e8f0;
      color: #0f172a;
      padding: 30px 15px;
      display: flex;
      flex-direction: column;
      align-items: center;
    }}
    .lienzo-svg {{
      width: {ANCHO}px;
      background: #ffffff;
      border: 1px solid #cbd5e1;
      border-radius: 8px;
      box-shadow: 0 15px 35px rgba(0, 0, 0, 0.12);
      overflow: hidden;
    }}
    svg {{ display: block; width: 100%; height: auto; }}
    svg text {{ stroke: none; }}
  </style>
</head>
<body>
  <div class="lienzo-svg">
    <svg width="{ANCHO}" height="{ALTO}" viewBox="0 0 {ANCHO} {ALTO}" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <!-- Flecha de flujo metabólico principal (Naranja) -->
        <marker id="arrowFlow" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
          <path d="M 0 0 L 6 3 L 0 6 Z" fill="#ea580c" />
        </marker>
        <!-- Flecha de reactivo / gasto (Rojo carmesí) -->
        <marker id="arrowRed" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#dc2626" />
        </marker>
        <!-- Flecha de salida / producto (Gris pizarra) -->
        <marker id="arrowSlate" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#475569" />
        </marker>
        <!-- Flecha de ganancia / poder reductor (Verde esmeralda) -->
        <marker id="arrowGreen" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#059669" />
        </marker>
        <!-- Flecha de Coenzima Q / Cadena respiratoria (Azul oscuro) -->
        <marker id="arrowBlue" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#0284c7" />
        </marker>

        <!-- Gradiente Citosol -->
        <linearGradient id="gradCitosol" x1="0%" y1="0%" x2="100%" y2="0%">
          <stop offset="0%" stop-color="#f8fafc" />
          <stop offset="100%" stop-color="#f1f5f9" />
        </linearGradient>

        <!-- Gradiente Espacio Intermembrana (EIM) -->
        <linearGradient id="gradEIM" x1="0%" y1="0%" x2="100%" y2="0%">
          <stop offset="0%" stop-color="#fff7ed" />
          <stop offset="100%" stop-color="#ffedd5" />
        </linearGradient>

        <!-- Gradiente Matriz Mitocondrial -->
        <linearGradient id="gradMatriz" x1="0%" y1="0%" x2="100%" y2="0%">
          <stop offset="0%" stop-color="#fef3c7" />
          <stop offset="100%" stop-color="#fffbeb" />
        </linearGradient>
      </defs>
"""

PIE_HTML = """
    </svg>
  </div>
</body>
</html>
"""


def main():
    svg_elements = []

    # =========================================================================
    # 1. FONDOS BIOLÓGICOS Y COMPARTIMENTACIÓN CELULAR
    # =========================================================================
    # Citosol (X: 0 a 580)
    svg_elements.append(f'<rect x="0" y="0" width="580" height="{ALTO}" fill="url(#gradCitosol)" />')
    
    # Membrana Mitocondrial Externa (MME en X=580 a 640)
    svg_elements.append(f'<rect x="580" y="0" width="60" height="{ALTO}" fill="#e2e8f0" opacity="0.8"/>')
    svg_elements.append(f'<line x1="580" y1="0" x2="580" y2="{ALTO}" stroke="#94a3b8" stroke-width="2"/>')
    svg_elements.append(f'<line x1="640" y1="0" x2="640" y2="{ALTO}" stroke="#94a3b8" stroke-width="2"/>')

    # Espacio Intermembrana (EIM en X=640 a 900)
    svg_elements.append(f'<rect x="640" y="0" width="260" height="{ALTO}" fill="url(#gradEIM)" opacity="0.6"/>')

    # Membrana Mitocondrial Interna (MMI en X=900 a 970)
    svg_elements.append(f'<rect x="900" y="0" width="70" height="{ALTO}" fill="#fed7aa" opacity="0.9"/>')
    svg_elements.append(f'<line x1="900" y1="0" x2="900" y2="{ALTO}" stroke="#ea580c" stroke-width="2.5"/>')
    svg_elements.append(f'<line x1="970" y1="0" x2="970" y2="{ALTO}" stroke="#ea580c" stroke-width="2.5"/>')

    # Matriz Mitocondrial (X: 970 a ANCHO)
    svg_elements.append(f'<rect x="970" y="0" width="{ANCHO - 970}" height="{ALTO}" fill="url(#gradMatriz)" />')

    # Rótulos sutiles de compartimento en la parte superior (Y=112 para no tocar el encabezado)
    svg_elements.append("""
    <!-- Rótulos de compartimentos -->
    <text x="300" y="112" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#64748b" text-anchor="middle" letter-spacing="2">CITOSOL CELULAR</text>
    <text x="610" y="112" font-family="'Inter', sans-serif" font-size="10" font-weight="800" fill="#475569" text-anchor="middle" letter-spacing="1">MME</text>
    <text x="770" y="112" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#c2410c" text-anchor="middle" letter-spacing="1.5">ESPACIO INTERMEMBRANA</text>
    <text x="935" y="112" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#9a3412" text-anchor="middle" letter-spacing="1">MMI</text>
    <text x="1170" y="112" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#b45309" text-anchor="middle" letter-spacing="2">MATRIZ MITOCONDRIAL</text>

    <!-- Porina VDAC en MME -->
    <g transform="translate(590, 400)">
      <rect x="0" y="0" width="40" height="70" rx="8" fill="#cbd5e1" stroke="#475569" stroke-width="1.8"/>
      <text x="20" y="32" font-family="'Inter', sans-serif" font-size="9" font-weight="900" fill="#1e293b" text-anchor="middle">VDAC</text>
      <text x="20" y="46" font-family="'JetBrains Mono', monospace" font-size="7.5" font-weight="700" fill="#475569" text-anchor="middle">Porina</text>
    </g>
    """)

    # =========================================================================
    # 2. ENCABEZADO Y TÍTULO EDITORIAL
    # =========================================================================
    svg_elements.append("""
    <g transform="translate(60, 36)">
      <circle cx="18" cy="18" r="16" fill="#ea580c"/>
      <text x="18" y="24" font-family="'Inter', sans-serif" font-size="14" font-weight="900" fill="#ffffff" text-anchor="middle">8B</text>
      <text x="45" y="15" font-family="'Inter', sans-serif" font-size="19" font-weight="900" fill="#0f172a">LANZADERA DE GLICEROL-3-FOSFATO</text>
      <text x="45" y="32" font-family="'Inter', sans-serif" font-size="12" font-weight="700" fill="#ea580c">Transferencia de equivalentes de reducción a la Cadena Respiratoria (FAD ➔ CoQ)</text>
    </g>
    """)

    # =========================================================================
    # 3. BRAZO CITOSÓLICO (IZQUIERDA): cGPDH (GPD1)
    # =========================================================================
    # DHAP en Citosol (X=170, Y=165)
    svg_elements.append(f"""
    <g transform="translate(170, 165)">
      {DIHIDROXIACETONA_FOSFATO}
      <g transform="translate(120, 35)">
        <text x="0" y="0" fill="#0f172a" font-size="16" font-weight="900">Dihidroxiacetona Fosfato (DHAP)</text>
        <text x="0" y="18" fill="#ea580c" font-size="12" font-weight="800">[3C] · Triosa Cetosa libre</text>
        <text x="0" y="33" fill="#64748b" font-size="10.5" font-weight="600">Intermediario común de la Glucólisis</text>
      </g>
    </g>
    """)

    # Reacción cGPDH hacia Glicerol-3-P (Eje vertical en X=250, Y=315)
    svg_elements.append("""
    <g transform="translate(250, 315)">
      <!-- Flecha principal vertical descendente -->
      <line x1="0" y1="0" x2="0" y2="90" stroke="#ea580c" stroke-width="2.6" marker-end="url(#arrowFlow)"/>
      
      <!-- Entrada de NADH citosólico (curva Bézier roja entrando desde la izquierda) -->
      <path d="M -80 20 Q -30 20 -4 35" fill="none" stroke="#dc2626" stroke-width="2" marker-end="url(#arrowRed)"/>
      <text x="-85" y="24" fill="#dc2626" font-size="11" font-weight="900" text-anchor="end">- NADH + H⁺</text>
      <text x="-85" y="38" fill="#64748b" font-size="9" font-family="'JetBrains Mono', monospace" text-anchor="end">(GAPDH / Glucólisis)</text>

      <!-- Salida de NAD+ regenerado (curva Bézier verde saliendo hacia la izquierda) -->
      <path d="M -4 55 Q -30 70 -80 70" fill="none" stroke="#059669" stroke-width="2" marker-end="url(#arrowGreen)"/>
      <text x="-85" y="74" fill="#059669" font-size="11" font-weight="900" text-anchor="end">+ NAD⁺</text>
      <text x="-85" y="88" fill="#059669" font-size="9.5" font-weight="700" text-anchor="end">(Regenerado)</text>

      <!-- Nombre de la enzima y detalles a la derecha -->
      <g transform="translate(18, 25)">
        <text x="0" y="0" fill="#0f172a" font-size="13" font-weight="900">Glicerol-3-Fosfato Deshidrogenasa Citosólica (cGPDH / GPD1)</text>
        <text x="0" y="16" fill="#64748b" font-size="10.5" font-family="'JetBrains Mono', monospace">EC 1.1.1.8 · Reducción dependiente de NADH</text>
        <text x="0" y="32" fill="#16a34a" font-size="10" font-weight="800">Regenera NAD⁺ citosólico para sostener la glucólisis activa</text>
      </g>
    </g>
    """)

    # Glicerol-3-P en Citosol (X=170, Y=455)
    svg_elements.append(f"""
    <g transform="translate(170, 455)">
      {GLICEROL_3_FOSFATO}
      <g transform="translate(120, 35)">
        <text x="0" y="0" fill="#0f172a" font-size="16" font-weight="900">L-Glicerol-3-Fosfato</text>
        <text x="0" y="18" fill="#ea580c" font-size="12" font-weight="800">[3C] · Portador de electrones</text>
        <text x="0" y="33" fill="#64748b" font-size="10.5" font-weight="600">Transporta poder reductor hacia la mitocondria</text>
      </g>
    </g>
    """)

    # =========================================================================
    # 4. PASO A TRAVÉS DE LA MEMBRANA EXTERNA (PORINAS VDAC)
    # =========================================================================
    # Flecha fluida de Glicerol-3-P cruzando la MME hacia mGPDH
    svg_elements.append("""
    <!-- Ruta de ida de Glicerol-3-P: Citosol ➔ EIM ➔ Cara externa MMI -->
    <path d="M 480 540 Q 610 540 760 510" fill="none" stroke="#ea580c" stroke-width="2.6" marker-end="url(#arrowFlow)"/>
    <text x="610" y="565" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#c2410c" text-anchor="middle">Difusión por VDAC</text>

    <!-- Ruta de retorno de DHAP: EIM ➔ Citosol -->
    <path d="M 760 250 Q 610 220 480 220" fill="none" stroke="#ea580c" stroke-width="2.4" stroke-dasharray="5 3" marker-end="url(#arrowFlow)"/>
    <text x="610" y="210" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#64748b" text-anchor="middle">Retorno al Citosol</text>
    """)

    # =========================================================================
    # 5. BRAZO MITOCONDRIAL: FLAVOPROTEÍNA mGPDH (GPD2) EN MMI
    # =========================================================================
    # Complejo mGPDH anclado en MMI (X=860, Y=300)
    svg_elements.append("""
    <g transform="translate(860, 300)">
      <!-- Cuerpo globular de la proteína integral mGPDH insertada en la MMI -->
      <path d="M 40,0 Q 120,-30 140,80 Q 150,180 40,160 Q 0,110 0,60 Z" fill="#fed7aa" stroke="#c2410c" stroke-width="2.5"/>
      
      <!-- Sitio catalítico en la cara externa (hacia el EIM) -->
      <circle cx="45" cy="80" r="14" fill="#ffedd5" stroke="#ea580c" stroke-width="2"/>
      <text x="45" y="84" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#9a3412" text-anchor="middle">FAD</text>

      <!-- Rótulo de la enzima en MMI -->
      <g transform="translate(155, 35)">
        <text x="0" y="0" fill="#0f172a" font-size="13" font-weight="900">mGPDH (GPD2)</text>
        <text x="0" y="15" fill="#64748b" font-size="10" font-family="'JetBrains Mono', monospace">EC 1.1.5.3</text>
        <text x="0" y="30" fill="#9a3412" font-size="10" font-weight="800">Flavoproteína en cara externa MMI</text>
      </g>

      <!-- Reoxidación de Glicerol-3-P a DHAP en mGPDH -->
      <path d="M -80 180 Q -10 130 30 85" fill="none" stroke="#ea580c" stroke-width="2.4" marker-end="url(#arrowFlow)"/>
      <path d="M 30 75 Q -10 30 -80 -20" fill="none" stroke="#ea580c" stroke-width="2.4" marker-end="url(#arrowFlow)"/>

      <!-- Ciclo interno FAD ➔ FADH2 -->
      <path d="M 35 60 Q 55 45 65 75 Q 75 105 45 98" fill="none" stroke="#d97706" stroke-width="2" marker-end="url(#arrowFlow)"/>
      <text x="80" y="90" font-family="'Inter', sans-serif" font-size="9.5" font-weight="900" fill="#b45309">FADH₂</text>

      <!-- Transferencia de electrones a la Coenzima Q en la membrana lipídica -->
      <path d="M 65 75 Q 110 75 160 110" fill="none" stroke="#0284c7" stroke-width="2.6" marker-end="url(#arrowBlue)"/>
      
      <!-- Coenzima Q en la membrana (diseño estilizado) -->
      <g transform="translate(170, 95)">
        <rect x="0" y="0" width="115" height="42" rx="8" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.8"/>
        <text x="57" y="18" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#0369a1" text-anchor="middle">CoQ ➔ CoQH₂</text>
        <text x="57" y="32" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="700" fill="#0284c7" text-anchor="middle">Ubiquinona lipídica</text>
      </g>

      <!-- Flecha hacia Complejo III en la Cadena Respiratoria -->
      <path d="M 290 116 L 360 116" fill="none" stroke="#0284c7" stroke-width="2.6" marker-end="url(#arrowBlue)"/>
      <g transform="translate(370, 95)">
        <rect x="0" y="0" width="130" height="42" rx="8" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.8"/>
        <text x="65" y="18" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#15803d" text-anchor="middle">COMPLEJO III</text>
        <text x="65" y="32" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="700" fill="#16a34a" text-anchor="middle">Citocromo bc₁</text>
      </g>
    </g>
    """)

# Generación y guardado
    codigo_svg = "\n".join(svg_elements)
    documento_html = CABECERA_HTML + codigo_svg + PIE_HTML

    dir_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_html = os.path.join(dir_actual, "Lanzadera_Glicerol_3_Fosfato.html")
    ruta_svg = os.path.join(dir_actual, "Lanzadera_Glicerol_3_Fosfato.svg")
    ruta_png = os.path.join(dir_actual, "Lanzadera_Glicerol_3_Fosfato_preview.png")

    with open(ruta_html, "w", encoding="utf-8") as f:
        f.write(documento_html)
    print(f"✓ Archivo HTML guardado: {ruta_html}")

    svg_completo = f"""<svg width="{ANCHO}" height="{ALTO}" viewBox="0 0 {ANCHO} {ALTO}" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arrowFlow" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
          <path d="M 0 0 L 6 3 L 0 6 Z" fill="#ea580c" />
        </marker>
        <marker id="arrowRed" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#dc2626" />
        </marker>
        <marker id="arrowSlate" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#475569" />
        </marker>
        <marker id="arrowGreen" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#059669" />
        </marker>
        <marker id="arrowBlue" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#0284c7" />
        </marker>
        <linearGradient id="gradCitosol" x1="0%" y1="0%" x2="100%" y2="0%">
          <stop offset="0%" stop-color="#f8fafc" />
          <stop offset="100%" stop-color="#f1f5f9" />
        </linearGradient>
        <linearGradient id="gradEIM" x1="0%" y1="0%" x2="100%" y2="0%">
          <stop offset="0%" stop-color="#fff7ed" />
          <stop offset="100%" stop-color="#ffedd5" />
        </linearGradient>
        <linearGradient id="gradMatriz" x1="0%" y1="0%" x2="100%" y2="0%">
          <stop offset="0%" stop-color="#fef3c7" />
          <stop offset="100%" stop-color="#fffbeb" />
        </linearGradient>
      </defs>
      {codigo_svg}
    </svg>"""

    with open(ruta_svg, "w", encoding="utf-8") as f:
        f.write(svg_completo)
    print(f"✓ Archivo SVG guardado: {ruta_svg}")

    try:
        subprocess.run(["rsvg-convert", "-w", str(ANCHO * 2), ruta_svg, "-o", ruta_png], check=True)
        print(f"✓ Preview PNG generado con éxito: {ruta_png}")
    except Exception as e:
        print(f"! Error generando preview PNG: {e}")


if __name__ == "__main__":
    main()
