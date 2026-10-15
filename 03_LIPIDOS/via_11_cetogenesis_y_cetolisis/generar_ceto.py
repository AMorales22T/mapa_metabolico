#!/usr/bin/env python3
"""
GENERADOR COMPLETO: CETOGÉNESIS Y CETÓLISIS (ESTILO GLUCÓLISIS Y LANZADERA CON LUPA INTERÓRGANO)
================================================================================================
Aplica las directrices de las skills:
- scientific-schematics: Claridad fisiológica, sin textos de bloque estorbando, Okabe-Ito, contraste.
- excalidraw-diagram: Multi-Zoom Architecture (Lupa circular cónica para Cetólisis extrahepática).
- Estilo del proyecto: Fondo orgánico con gradientes acuosos, bicapa de fosfolípidos con cabezas polares,
  transportador transmembrana proteico MCT real con poro acuoso y lóbulos proteicos,
  microfilamentos sutiles de citoesqueleto y lupa de aumento científico.
"""

import os
from estructuras_ceto import (
    ACETIL_COA_CETO,
    ACETOACETIL_COA,
    HMG_COA,
    ACETOACETATO,
    D_BETA_HIDROXIBUTIRATO,
    ACETONA,
    SUCCINIL_COA_BADGE,
    SUCCINATO_BADGE
)
from entorno_ceto import DEFS_ENTORNO_CETO_ORGANICO, generar_entorno_organico_svg

CABECERA_HTML = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Cetogénesis y Cetólisis con Lupa de Proyección Interórgano</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&family=JetBrains+Mono:wght@600;700;800&display=swap" rel="stylesheet">
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: 'Inter', sans-serif;
      background: #e2e8f0;
      color: #0f172a;
      padding: 30px 15px;
      display: flex;
      flex-direction: column;
      align-items: center;
    }
    .lienzo-svg {
      width: 1100px;
      background: #ffffff;
      border: 1px solid #cbd5e1;
      border-radius: 8px;
      box-shadow: 0 15px 35px rgba(0, 0, 0, 0.12);
      overflow: hidden;
    }
    svg { display: block; width: 100%; height: auto; }
  </style>
</head>
<body>
  <div class="lienzo-svg">
    <svg width="1100" height="2250" viewBox="0 0 1100 2250" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <!-- Flecha de flujo metabólico principal (Ámbar / Naranja) -->
        <marker id="arrowFlow" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
          <path d="M 0 0 L 6 3 L 0 6 Z" fill="#ea580c" />
        </marker>
        <!-- Flecha de cofactor / Coenzima A (Púrpura) -->
        <marker id="arrowPurple" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#7c3aed" />
        </marker>
        <!-- Flecha de gasto / reactivo (Roja) -->
        <marker id="arrowRed" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#dc2626" />
        </marker>
        <!-- Flecha de poder reductor NADH (Verde esmeralda) -->
        <marker id="arrowGreen" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#059669" />
        </marker>
        <!-- Flecha de subproducto / gas (Gris pizarra) -->
        <marker id="arrowSlate" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#475569" />
        </marker>
        <!-- Flecha de agua (Azul) -->
        <marker id="arrowBlue" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#0284c7" />
        </marker>

        {DEFS_ENTORNO_CETO_ORGANICO}
      </defs>
"""

PIE_HTML = """
    </svg>
  </div>
</body>
</html>
"""

def crear_metabolito(x, y, id_tag, nombre, carbonos, detalle="", svg_estructura="", texto_arriba=False, dx_texto=None):
    """Metabolito con fórmula química libre y textos claros sin colisiones."""
    if texto_arriba:
        pos_texto = "translate(0, -10)"
        pos_estructura = "translate(0, 15)"
    else:
        dist_x = dx_texto if dx_texto is not None else 210
        pos_estructura = "translate(0, 0)"
        pos_texto = f"translate({dist_x}, 25)"

    return f"""
    <!-- Metabolito: {nombre} -->
    <g id="{id_tag}" data-arrastrable="1" transform="translate({x}, {y})">
      <g transform="{pos_estructura}">
        {svg_estructura}
      </g>
      <g transform="{pos_texto}">
        <text x="0" y="0" font-family="'Inter', sans-serif" font-size="14.5" font-weight="900" fill="#0f172a">{nombre}</text>
        <text x="0" y="18" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#ea580c">[{carbonos}] {detalle}</text>
      </g>
    </g>
    """

def crear_enzima(x, y, id_tag, numero, nombre, ec="", regulacion=""):
    """Enzima editorial con badge numerado y tipografía clara."""
    reg_svg = ""
    if regulacion:
        reg_svg = f"""<text x="5" y="29" font-family="'Inter', sans-serif" font-size="9.5" font-weight="700" fill="#dc2626">{regulacion}</text>"""

    return f"""
    <!-- Enzima {numero}: {nombre} -->
    <g id="{id_tag}" data-arrastrable="1" transform="translate({x}, {y})">
      <circle cx="-12" cy="-4" r="9" fill="#0f172a" />
      <text x="-12" y="0" font-family="'Inter', sans-serif" font-size="9" font-weight="900" fill="#ffffff" text-anchor="middle">{numero}</text>
      
      <text x="5" y="0" font-family="'Inter', sans-serif" font-size="13" font-weight="800" fill="#0f172a">{nombre}</text>
      <text x="5" y="14" font-family="'JetBrains Mono', monospace" font-size="9.5" font-weight="600" fill="#64748b">EC {ec}</text>
      {reg_svg}
    </g>
    """

def generar_svg_contenido():
    svg_parts = []
    
    # 1. Fondo biológico orgánico (Matriz, Bicapa y Lupa científica)
    svg_parts.append(generar_entorno_organico_svg())

    # =========================================================================
    # SECCIÓN 1: CETOGÉNESIS HEPÁTICA (MATRIZ MITOCONDRIAL) [y = 60 a 980]
    # =========================================================================

    # 1. 2 x Acetil-CoA
    # Eje central X=380
    svg_parts.append(crear_metabolito(
        x=280, y=95,
        id_tag="ceto-met-2acetilcoa",
        nombre="2 x Acetil-CoA",
        carbonos="2C cada uno",
        detalle="Exceso proveniente de β-oxidación",
        svg_estructura=ACETIL_COA_CETO
    ))

    # Reacción 1: Tiolasa
    svg_parts.append("""
    <path d="M 380 160 L 380 220" stroke="#ea580c" stroke-width="2.5" fill="none" marker-end="url(#arrowFlow)"/>
    <!-- Salida de CoA-SH -->
    <path d="M 380 185 Q 430 185 470 170" stroke="#7c3aed" stroke-width="2" stroke-dasharray="3 3" fill="none" marker-end="url(#arrowPurple)"/>
    <text x="480" y="173" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#7c3aed">+ CoA-SH liberado</text>
    """)
    svg_parts.append(crear_enzima(
        x=80, y=190,
        id_tag="ceto-enz-tiolasa",
        numero="1",
        nombre="Tiolasa Mitocondrial (ACAT1)",
        ec="2.3.1.9",
        regulacion="Condensación de Claisen reversible"
    ))

    # 2. Acetoacetil-CoA
    svg_parts.append(crear_metabolito(
        x=280, y=230,
        id_tag="ceto-met-acetoacetilcoa",
        nombre="Acetoacetil-CoA",
        carbonos="4C",
        detalle="Intermediario activado",
        svg_estructura=ACETOACETIL_COA
    ))

    # Reacción 2: HMG-CoA Sintasa (Paso Marcapasos)
    svg_parts.append("""
    <path d="M 380 300 L 380 370" stroke="#ea580c" stroke-width="2.5" fill="none" marker-end="url(#arrowFlow)"/>
    
    <!-- Entrada de Acetil-CoA -->
    <path d="M 520 310 Q 440 310 380 330" stroke="#ea580c" stroke-width="2" fill="none" marker-end="url(#arrowFlow)"/>
    <text x="530" y="313" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#ea580c">+ Acetil-CoA [2C] + H₂O</text>
    
    <!-- Salida de CoA-SH -->
    <path d="M 380 345 Q 440 360 480 360" stroke="#7c3aed" stroke-width="2" stroke-dasharray="3 3" fill="none" marker-end="url(#arrowPurple)"/>
    <text x="490" y="364" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#7c3aed">+ CoA-SH</text>
    """)
    svg_parts.append(crear_enzima(
        x=40, y=330,
        id_tag="ceto-enz-hmgsintasa",
        numero="2",
        nombre="HMG-CoA Sintasa Mitocondrial (HMGCS2)",
        ec="2.3.3.10",
        regulacion="★ MARCAPASOS: Inducida por ayuno / glucagón / SIRT3"
    ))

    # 3. HMG-CoA
    svg_parts.append(crear_metabolito(
        x=280, y=385,
        id_tag="ceto-met-hmgcoa",
        nombre="HMG-CoA",
        carbonos="6C",
        detalle="3-Hidroxi-3-Metilglutaril-CoA",
        svg_estructura=HMG_COA
    ))

    # Reacción 3: HMG-CoA Liasa
    svg_parts.append("""
    <path d="M 380 465 L 380 530" stroke="#ea580c" stroke-width="2.5" fill="none" marker-end="url(#arrowFlow)"/>
    
    <!-- Salida de Acetil-CoA regenerado -->
    <path d="M 380 495 Q 440 495 480 480" stroke="#ea580c" stroke-width="2" stroke-dasharray="3 3" fill="none" marker-end="url(#arrowFlow)"/>
    <text x="490" y="484" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#ea580c">+ Acetil-CoA [2C] regenerado</text>
    """)
    svg_parts.append(crear_enzima(
        x=70, y=495,
        id_tag="ceto-enz-hmgliasa",
        numero="3",
        nombre="HMG-CoA Liasa Mitocondrial (HMGCL)",
        ec="4.1.3.4",
        regulacion="Escisión C-C exclusiva de la matriz mitocondrial"
    ))

    # 4. Acetoacetato Hepático
    svg_parts.append(crear_metabolito(
        x=280, y=545,
        id_tag="ceto-met-acetoacetato-hep",
        nombre="Acetoacetato",
        carbonos="4C",
        detalle="1er Cuerpo Cetónico Generado",
        svg_estructura=ACETOACETATO,
        dx_texto=185
    ))

    # Bifurcación 1: Hacia Acetona (Izquierda)
    svg_parts.append("""
    <!-- Flujo hacia Acetona -->
    <text x="110" y="570" font-family="'Inter', sans-serif" font-size="10" font-weight="800" fill="#dc2626">Descarboxilación espontánea (-CO₂)</text>
    <text x="110" y="583" font-family="'Inter', sans-serif" font-size="9" font-weight="600" fill="#64748b">No enzimática / Lenta</text>
    <path d="M 280 595 Q 180 625 120 675" stroke="#64748b" stroke-width="2.2" stroke-dasharray="4 3" fill="none" marker-end="url(#arrowSlate)"/>
    """)
    svg_parts.append(crear_metabolito(
        x=30, y=680,
        id_tag="ceto-met-acetona",
        nombre="Acetona",
        carbonos="3C",
        detalle="Volátil, exhalada en aliento",
        svg_estructura=ACETONA,
        dx_texto=135
    ))

    # Bifurcación 2: Hacia D-β-Hidroxibutirato (Derecha)
    svg_parts.append("""
    <!-- Flujo hacia D-beta-hidroxibutirato partiendo limpiamente de la molécula -->
    <path d="M 420 595 Q 560 610 710 680" stroke="#ea580c" stroke-width="2.5" fill="none" marker-end="url(#arrowFlow)"/>
    
    <!-- Reacción Redox con NADH bien visible -->
    <path d="M 530 635 Q 580 655 630 635" stroke="#059669" stroke-width="2" fill="none" marker-end="url(#arrowGreen)"/>
    <text x="525" y="668" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#059669">NADH + H⁺ ➔ NAD⁺</text>
    <text x="525" y="680" font-family="'Inter', sans-serif" font-size="8.5" font-weight="600" fill="#64748b">(Regulado por relación NADH/NAD⁺)</text>
    """)
    svg_parts.append(crear_enzima(
        x=570, y=515,
        id_tag="ceto-enz-bdh1-hep",
        numero="4",
        nombre="D-β-Hidroxibutirato DH (BDH1)",
        ec="1.1.1.30",
        regulacion="Reversible según potencial redox mitocondrial"
    ))

    # 5. D-β-Hidroxibutirato Hepático
    svg_parts.append(crear_metabolito(
        x=680, y=680,
        id_tag="ceto-met-hidroxibutirato-hep",
        nombre="D-β-Hidroxibutirato",
        carbonos="4C",
        detalle="Forma predominante en sangre (~4:1)",
        svg_estructura=D_BETA_HIDROXIBUTIRATO,
        dx_texto=200
    ))


    # =========================================================================
    # SECCIÓN 2: SALIDA A TRAVÉS DE LOS TRANSPORTADORES MCT Y EXHALACIÓN
    # =========================================================================

    # Salida Acetoacetato hacia transportador MCT1 (y = 985)
    svg_parts.append("""
    <path d="M 380 620 L 380 985" stroke="#ea580c" stroke-width="2.5" fill="none"/>
    <path d="M 380 1025 L 380 1090" stroke="#ea580c" stroke-width="2.5" fill="none" marker-end="url(#arrowFlow)"/>

    <!-- Salida D-beta-hidroxibutirato hacia transportador MCT2 (y = 985) -->
    <path d="M 770 755 L 770 985" stroke="#ea580c" stroke-width="2.5" fill="none"/>
    <path d="M 770 1025 L 770 1090" stroke="#ea580c" stroke-width="2.5" fill="none" marker-end="url(#arrowFlow)"/>

    <!-- Acetona volátil que escapa hacia el aliento -->
    <path d="M 120 750 L 120 950" stroke="#64748b" stroke-width="2" stroke-dasharray="4 3" fill="none" marker-end="url(#arrowSlate)"/>
    <g id="ceto-pulmones" data-arrastrable="1" transform="translate(35, 960)">
      <rect x="0" y="0" width="170" height="42" rx="8" fill="#ffffff" stroke="#94a3b8" stroke-width="1.5"/>
      <text x="85" y="18" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#334155" text-anchor="middle">EXHALACIÓN PULMONAR</text>
      <text x="85" y="32" font-family="'Inter', sans-serif" font-size="9" font-weight="700" fill="#64748b" text-anchor="middle">Aliento cetósico olor frutal</text>
    </g>
    """)


    # =========================================================================
    # SECCIÓN 3: DENTRO DE LA LUPA DE AUMENTO CIENTÍFICO (CETÓLISIS EXTRAHEPÁTICA)
    # =========================================================================
    # El centro de la lupa está en (550, 1750)

    # 1. Cuerpos Cetónicos en Tránsito Capilar (y = 1380 dentro de la lupa)
    svg_parts.append(crear_metabolito(
        x=280, y=1380,
        id_tag="ceto-met-acetoacetato-plasma",
        nombre="Acetoacetato",
        carbonos="4C",
        detalle="Tránsito capilar soluble libre",
        svg_estructura=ACETOACETATO,
        dx_texto=185
    ))

    svg_parts.append(crear_metabolito(
        x=680, y=1380,
        id_tag="ceto-met-hidroxibutirato-plasma",
        nombre="D-β-Hidroxibutirato",
        carbonos="4C",
        detalle="Captación periférica por MCT1",
        svg_estructura=D_BETA_HIDROXIBUTIRATO,
        dx_texto=200
    ))

    # Flujo de Acetoacetato bajando al punto de activación
    svg_parts.append("""
    <path d="M 380 1450 L 380 1580" stroke="#ea580c" stroke-width="2.5" fill="none" marker-end="url(#arrowFlow)"/>
    """)

    # Flujo de D-β-Hidroxibutirato hacia su reoxidación generadora de NADH
    svg_parts.append("""
    <!-- Curva de reoxidación hacia el Acetoacetato -->
    <path d="M 770 1450 Q 640 1495 490 1605" stroke="#ea580c" stroke-width="2.5" fill="none" marker-end="url(#arrowFlow)"/>
    
    <!-- Generación de 1 NADH -->
    <path d="M 640 1550 Q 590 1575 540 1550" stroke="#059669" stroke-width="2" fill="none" marker-end="url(#arrowGreen)"/>
    <text x="510" y="1590" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#059669">NAD⁺ ➔ NADH + H⁺ (+2.5 ATP)</text>
    """)
    svg_parts.append(crear_enzima(
        x=700, y=1470,
        id_tag="ceto-enz-bdh1-extra",
        numero="5",
        nombre="D-β-Hidroxibutirato DH (BDH1)",
        ec="1.1.1.30",
        regulacion="Reoxidación en matriz periférica"
    ))

    # 2. Acetoacetato Extrahepático (Punto de activación energética, y = 1600)
    svg_parts.append(crear_metabolito(
        x=280, y=1600,
        id_tag="ceto-met-acetoacetato-extra",
        nombre="Acetoacetato",
        carbonos="4C",
        detalle="Substrato de activación obligada",
        svg_estructura=ACETOACETATO,
        dx_texto=185
    ))

    # Reacción 6: Tioforasa (SCOT / OXCT1)
    svg_parts.append("""
    <path d="M 380 1660 L 380 1770" stroke="#ea580c" stroke-width="2.5" fill="none" marker-end="url(#arrowFlow)"/>
    
    <!-- Transferencia acoplada de Succinil-CoA a Succinato -->
    <path d="M 480 1685 Q 430 1720 480 1755" stroke="#7c3aed" stroke-width="2" fill="none" marker-end="url(#arrowPurple)"/>
    """)
    # Badges de donación de CoA
    svg_parts.append(f"""
    <g id="ceto-badge-succinilcoa" data-arrastrable="1" transform="translate(490, 1675)">
      {SUCCINIL_COA_BADGE}
    </g>
    <g id="ceto-badge-succinato" data-arrastrable="1" transform="translate(490, 1745)">
      {SUCCINATO_BADGE}
    </g>
    """)
    svg_parts.append(crear_enzima(
        x=40, y=1710,
        id_tag="ceto-enz-tioforasa",
        numero="6",
        nombre="Tioforasa (SCOT / OXCT1)",
        ec="2.8.3.5",
        regulacion="★ ENZIMA EXCLUSIVA EXTRAHEPÁTICA: Ausente en hígado"
    ))

    # 3. Acetoacetil-CoA Extrahepático (y = 1785)
    svg_parts.append(crear_metabolito(
        x=280, y=1785,
        id_tag="ceto-met-acetoacetilcoa-extra",
        nombre="Acetoacetil-CoA",
        carbonos="4C",
        detalle="Forma tioéster reactiva activada",
        svg_estructura=ACETOACETIL_COA
    ))

    # Reacción 7: Tiolasa Extrahepática (Tiólisis)
    svg_parts.append("""
    <path d="M 380 1860 L 380 1940" stroke="#ea580c" stroke-width="2.5" fill="none" marker-end="url(#arrowFlow)"/>
    
    <!-- Entrada de CoA-SH -->
    <path d="M 490 1890 Q 440 1900 390 1900" stroke="#7c3aed" stroke-width="2" fill="none" marker-end="url(#arrowPurple)"/>
    <text x="500" y="1895" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#7c3aed">+ CoA-SH</text>
    """)
    svg_parts.append(crear_enzima(
        x=90, y=1895,
        id_tag="ceto-enz-tiolasa-extra",
        numero="7",
        nombre="Tiolasa Mitocondrial (ACAT1)",
        ec="2.3.1.9",
        regulacion="Tiólisis exergónica: Clivaje en 2 unidades de 2C"
    ))

    # 4. 2 x Acetil-CoA producido (y = 1955)
    svg_parts.append(crear_metabolito(
        x=280, y=1955,
        id_tag="ceto-met-2acetilcoa-extra",
        nombre="2 x Acetil-CoA",
        carbonos="2C cada uno",
        detalle="Combustión aeróbica celular",
        svg_estructura=ACETIL_COA_CETO
    ))

    # Destino terminal al Ciclo de Krebs dentro de la célula periférica
    svg_parts.append("""
    <path d="M 380 2035 L 380 2105" stroke="#ea580c" stroke-width="2.5" fill="none" marker-end="url(#arrowFlow)"/>
    
    <g id="ceto-destino-krebs" data-arrastrable="1" transform="translate(250, 2110)">
      <rect x="0" y="0" width="280" height="42" rx="8" fill="#ffffff" stroke="#ea580c" stroke-width="2"/>
      <circle cx="20" cy="21" r="7" fill="#ea580c"/>
      <text x="38" y="26" font-family="'Inter', sans-serif" font-size="12.5" font-weight="900" fill="#9a3412">INGRESO AL CICLO DE KREBS (TCA)</text>
    </g>
    <text x="545" y="2136" font-family="'Inter', sans-serif" font-size="11.5" font-weight="700" fill="#ea580c">Rinde ~20 ATP netos por cada Acetoacetato oxidado</text>
    """)

    return "\n".join(svg_parts)

def construir_archivos():
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    contenido_svg = generar_svg_contenido()

    # 1. HTML
    html_total = CABECERA_HTML.replace("{DEFS_ENTORNO_CETO_ORGANICO}", DEFS_ENTORNO_CETO_ORGANICO) + contenido_svg + PIE_HTML
    ruta_html = os.path.join(directorio_actual, "Cetogenesis_y_Cetolisis.html")
    with open(ruta_html, "w", encoding="utf-8") as f:
        f.write(html_total)
    print(f"HTML generado con éxito en: {ruta_html}")

    # 2. SVG Puro
    svg_autonomo = f"""<svg width="1100" height="2250" viewBox="0 0 1100 2250" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&amp;family=JetBrains+Mono:wght@600;700;800&amp;display=swap');
      text {{ font-family: 'Inter', system-ui, -apple-system, sans-serif; }}
    </style>
    <marker id="arrowFlow" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
      <path d="M 0 0 L 6 3 L 0 6 Z" fill="#ea580c" />
    </marker>
    <marker id="arrowPurple" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
      <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#7c3aed" />
    </marker>
    <marker id="arrowRed" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
      <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#dc2626" />
    </marker>
    <marker id="arrowGreen" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
      <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#059669" />
    </marker>
    <marker id="arrowSlate" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
      <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#475569" />
    </marker>
    <marker id="arrowBlue" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
      <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#0284c7" />
    </marker>
    {DEFS_ENTORNO_CETO_ORGANICO}
  </defs>
  {contenido_svg}
</svg>"""

    ruta_svg = os.path.join(directorio_actual, "Cetogenesis_y_Cetolisis.svg")
    with open(ruta_svg, "w", encoding="utf-8") as f:
        f.write(svg_autonomo)
    print(f"SVG generado con éxito en: {ruta_svg}")

if __name__ == "__main__":
    construir_archivos()
