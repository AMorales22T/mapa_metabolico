#!/usr/bin/env python3
"""
GENERADOR DE LA BETA-OXIDACIÓN DE ÁCIDOS GRASOS EN SU ENTORNO CELULAR REAL
===========================================================================
Diseñado en concordancia 100% estricta con el estilo editorial de:
- 01_CARBOHIDRATOS/01_glucolisis/Glucolisis.svg
- 02_RESPIRACION_Y_ENERGIA/02_ciclo_de_krebs/Ciclo_de_Krebs.svg

Características:
- Lienzo vertical clásico de 1000 x 2250 px.
- Flujo central libre sobre fondo acuoso citosólico y matriz mitocondrial.
- Sin tarjetas ni globos artificiales; metabolitos y enzimas libres.
- Trazos oscuros #0f172a, oxígenos en rojo #dc2626, OH en azul #0284c7, Coenzima A en púrpura #7c3aed.
- Todas las rutas y curvas de Bézier tienen fill="none" (cero polígonos/triángulos negros).
- Todo elemento móvil identificado con data-arrastrable="1" e IDs semánticos.
"""

import os
from estructuras_beta_oxidacion import (
    PALMITATO,
    PALMITOIL_COA,
    PALMITOIL_CARNITINA,
    TRANS_DELTA2_ENOIL_COA,
    L_BETA_HIDROXIACIL_COA,
    BETA_CETOACIL_COA,
    ACETIL_COA_BETA,
    MIRISTOIL_COA
)
from entorno_beta_oxidacion import DEFS_ENTORNO_BETA_OX, generar_entorno_beta_oxidacion_svg

CABECERA_HTML = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Beta-Oxidación de Ácidos Grasos en Entorno Biológico Real</title>
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
      width: 1000px;
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
    <svg width="1000" height="1750" viewBox="0 0 1000 1750" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <!-- Flecha de flujo metabólico principal (Ámbar / Naranja) -->
        <marker id="arrowFlow" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
          <path d="M 0 0 L 6 3 L 0 6 Z" fill="#ea580c" />
        </marker>
        <!-- Flecha de gasto de energía / reactivo (Roja) -->
        <marker id="arrowRed" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#dc2626" />
        </marker>
        <!-- Flecha de subproducto / cofactor gastado (Gris pizarra) -->
        <marker id="arrowSlate" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#475569" />
        </marker>
        <!-- Flecha de ganancia / poder reductor (Verde esmeralda) -->
        <marker id="arrowGreen" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#059669" />
        </marker>
        <!-- Flecha de agua (Azul) -->
        <marker id="arrowBlue" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#0284c7" />
        </marker>
        <!-- Flecha de Coenzima A (Púrpura) -->
        <marker id="arrowPurple" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#7c3aed" />
        </marker>

        """ + DEFS_ENTORNO_BETA_OX + """
      </defs>
"""

PIE_HTML = """
    </svg>
  </div>
</body>
</html>
"""

def crear_metabolito(x, y, id_tag, nombre, carbonos, detalle="", svg_estructura="", texto_izquierda=False):
    """Construye un metabolito libre idéntico al estándar de Glucólisis."""
    if texto_izquierda:
        pos_estructura = "translate(150, 0)"
        pos_texto = "translate(130, 25)"
        alineacion = 'text-anchor="end"'
    else:
        pos_estructura = "translate(0, 0)"
        pos_texto = "translate(275, 25)"
        alineacion = ''

    return f"""
    <!-- Metabolito: {nombre} -->
    <g id="{id_tag}" data-arrastrable="1" transform="translate({x}, {y})">
      <g transform="{pos_estructura}">
        {svg_estructura}
      </g>
      <g transform="{pos_texto}">
        <text x="0" y="0" fill="#0f172a" font-size="16.5" font-weight="800" font-family="'Inter', sans-serif" {alineacion}>{nombre}</text>
        <text x="0" y="18" fill="#ea580c" font-size="12" font-weight="700" font-family="'JetBrains Mono', monospace" {alineacion}>{carbonos}</text>
        <text x="0" y="34" fill="#64748b" font-size="11" font-family="'Inter', sans-serif" {alineacion}>{detalle}</text>
      </g>
    </g>
    """

def crear_reaccion(x, y, id_tag, enzima, ec="", regulacion="", entra_energia="", sale_energia="", 
                   es_ganancia=False, entrada_agua=False, entrada_coa=False, altura=55):
    """Genera una reacción con arcos curvados idéntica a Glucólisis y Ciclo de Krebs."""
    curvas_energia = ""
    
    # 1. Entrada de energía o reactivo (desde la izquierda hacia el centro)
    if entra_energia:
        color_entrada = "#dc2626" if not es_ganancia else "#475569"
        marcador_entrada = "url(#arrowRed)" if not es_ganancia else "url(#arrowSlate)"
        curvas_energia += f"""
        <path d="M -80 10 Q -30 10 -4 20" fill="none" stroke="{color_entrada}" stroke-width="1.8" marker-end="{marcador_entrada}"/>
        <text x="-85" y="13" fill="{color_entrada}" font-size="11" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">{entra_energia}</text>
        """
        
    # 2. Salida de producto energético (desde el centro hacia la izquierda)
    if sale_energia:
        color_salida = "#059669" if es_ganancia else "#475569"
        marcador_salida = "url(#arrowGreen)" if es_ganancia else "url(#arrowSlate)"
        curvas_energia += f"""
        <path d="M -4 26 Q -30 36 -80 36" fill="none" stroke="{color_salida}" stroke-width="1.8" marker-end="{marcador_salida}"/>
        <text x="-85" y="39" fill="{color_salida}" font-size="11" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">{sale_energia}</text>
        """

    # 3. Entrada de agua (Crotonasa)
    if entrada_agua:
        curvas_energia += f"""
        <path d="M -75 16 Q -25 16 -4 26" fill="none" stroke="#0284c7" stroke-width="1.8" marker-end="url(#arrowBlue)"/>
        <text x="-80" y="19" fill="#0284c7" font-size="11" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">+ 1 H₂O</text>
        """

    # 4. Entrada de Coenzima A (Tiolasa)
    if entrada_coa:
        curvas_energia += f"""
        <path d="M -75 16 Q -25 16 -4 26" fill="none" stroke="#7c3aed" stroke-width="1.8" marker-end="url(#arrowPurple)"/>
        <text x="-80" y="19" fill="#7c3aed" font-size="11" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">+ 1 CoA-SH</text>
        """

    # Rótulo de regulación (en rojo)
    reg_svg = ""
    if regulacion:
        reg_svg = f"""<text x="0" y="27" fill="#e11d48" font-size="10" font-weight="800" font-family="'Inter', sans-serif">{regulacion}</text>"""

    return f"""
    <!-- Reacción: {enzima} -->
    <g id="{id_tag}" data-arrastrable="1" transform="translate({x}, {y})">
      <!-- Flecha central de flujo -->
      <line x1="0" y1="0" x2="0" y2="{altura}" stroke="#ea580c" stroke-width="2.6" marker-end="url(#arrowFlow)"/>
      
      <!-- Acoplamiento de reactivos y energía -->
      {curvas_energia}
      
      <!-- Textos informativos de la enzima a la derecha -->
      <g transform="translate(18, 14)">
        <text x="0" y="0" fill="#0f172a" font-size="12.5" font-weight="800" font-family="'Inter', sans-serif">{enzima}</text>
        <text x="0" y="14" fill="#64748b" font-size="10" font-family="'JetBrains Mono', monospace">{ec}</text>
        {reg_svg}
      </g>
    </g>
    """

def generar_svg_completo():
    """Genera el contenido SVG total de la Beta-Oxidación."""
    partes = []

    # 1. Fondo celular y compartimentos (MME en y=450, MMI en y=590-640)
    partes.append(generar_entorno_beta_oxidacion_svg(ancho=1000, alto=2400, y_mme=450, y_mmi_ini=590, y_mmi_fin=640))

    # =========================================================================
    # FASE 1: CITOSOL • ACTIVACIÓN DEL ÁCIDO GRASO
    # =========================================================================
    x_eje = 385
    x_metab = 240

    # 1. Palmitato
    partes.append(crear_metabolito(
        x=x_metab, y=105,
        id_tag="m_palmitato",
        nombre="Palmitato (Ácido Palmítico)",
        carbonos="16 Carbonos (Ácido Graso Libre)",
        detalle="Sustrato lipídico liberado en el citoplasma",
        svg_estructura=PALMITATO
    ))

    # Reacción 1: Acil-CoA Sintetasa
    partes.append(crear_reaccion(
        x=x_eje, y=205,
        id_tag="rx_activacion",
        enzima="Acil-CoA Sintetasa (Tiocinasa)",
        ec="EC 6.2.1.3 • Requiere ATP + CoA-SH",
        regulacion="Activación irreversible (pirofosfatasa)",
        entra_energia="- 2 ATP eq (ATP + CoA)",
        sale_energia="+ AMP + 2 Pi",
        es_ganancia=False,
        altura=60
    ))

    # 2. Palmitoil-CoA (Citosol)
    partes.append(crear_metabolito(
        x=x_metab, y=305,
        id_tag="m_palmitoil_coa_cit",
        nombre="Palmitoil-CoA (Citosol)",
        carbonos="16 Carbonos (Acil-CoA Activado)",
        detalle="Impermeable a la membrana mitocondrial interna",
        svg_estructura=PALMITOIL_COA
    ))

    # =========================================================================
    # FASE 2: LANZADERA DE CARNITINA (MME ➔ EIM ➔ MMI)
    # =========================================================================
    # Línea de entrada a CPT-I (y=395 a 445)
    partes.append(f"""
    <line x1="{x_eje}" y1="395" x2="{x_eje}" y2="445" stroke="#ea580c" stroke-width="2.6" marker-end="url(#arrowFlow)"/>
    """)

    # Transportador CPT-I incrustado en MME (y=450)
    partes.append(f"""
    <!-- CPT-I en MME -->
    <g id="complejo_cpt1" data-arrastrable="1" transform="translate({x_eje}, 450)">
      <rect x="-65" y="-14" width="130" height="28" rx="8" fill="#fef3c7" stroke="#b45309" stroke-width="2"/>
      <text x="0" y="4" fill="#78350f" font-size="12" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">CPT-I (CAT-I)</text>
      
      <!-- Entrada de Carnitina y salida de CoA -->
      <path d="M -75 -6 Q -30 -6 -4 0" fill="none" stroke="#d97706" stroke-width="1.6" marker-end="url(#arrowFlow)"/>
      <text x="-80" y="-3" fill="#b45309" font-size="10" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">+ Carnitina</text>
      
      <!-- Badge de Inhibición alostérica despejado -->
      <rect x="75" y="-12" width="165" height="22" rx="5" fill="#fef2f2" stroke="#dc2626" stroke-width="1.4"/>
      <text x="157" y="3" fill="#dc2626" font-size="9.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">⊣ Inhibida por Malonil-CoA</text>
    </g>
    """)

    # Metabolito en EIM: Palmitoilcarnitina (y=485)
    partes.append(crear_metabolito(
        x=x_metab, y=485,
        id_tag="m_palmitoilcarnitina_eim",
        nombre="Palmitoilcarnitina",
        carbonos="Éster Acil-Carnitina (EIM)",
        detalle="Cruza el Espacio Intermembrana hacia CACT",
        svg_estructura=PALMITOIL_CARNITINA
    ))

    # Translocasa CACT en MMI (y=615) y CPT-II en cara interna (y=665)
    partes.append(f"""
    <!-- Conexión a CACT -->
    <line x1="{x_eje}" y1="545" x2="{x_eje}" y2="603" stroke="#ea580c" stroke-width="2.6" marker-end="url(#arrowFlow)"/>
    
    <!-- CACT en MMI -->
    <g id="complejo_cact" data-arrastrable="1" transform="translate({x_eje}, 615)">
      <rect x="-65" y="-12" width="130" height="24" rx="6" fill="#e0f2fe" stroke="#0284c7" stroke-width="2"/>
      <text x="0" y="4" fill="#0369a1" font-size="11" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">CACT (Antiporte)</text>
    </g>

    <!-- Conexión hacia CPT-II -->
    <line x1="{x_eje}" y1="627" x2="{x_eje}" y2="652" stroke="#ea580c" stroke-width="2.6" marker-end="url(#arrowFlow)"/>

    <!-- CPT-II en Matriz -->
    <g id="complejo_cpt2" data-arrastrable="1" transform="translate({x_eje}, 665)">
      <rect x="-65" y="-12" width="130" height="26" rx="6" fill="#fef3c7" stroke="#b45309" stroke-width="2"/>
      <text x="0" y="5" fill="#78350f" font-size="11.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">CPT-II (Matriz)</text>
      <text x="75" y="4" fill="#059669" font-size="10" font-weight="800" font-family="'Inter', sans-serif">➔ Reconstituye Acil-CoA</text>
    </g>

    <!-- Retorno de Carnitina Libre hacia el Citosol (Arco punteado con fill='none') -->
    <path d="M 320 665 C 160 640, 160 450, 315 450" fill="none" stroke="#db2777" stroke-width="2" stroke-dasharray="6 4" marker-end="url(#arrowFlow)"/>
    <text x="150" y="555" fill="#db2777" font-size="10" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">
      Retorno: Carnitina Libre
    </text>

    <!-- Flecha descendente desde CPT-II hacia el primer sustrato de la espiral -->
    <line x1="{x_eje}" y1="680" x2="{x_eje}" y2="725" stroke="#ea580c" stroke-width="2.6" marker-end="url(#arrowFlow)"/>
    """)

    # =========================================================================
    # FASE 3: MATRIZ MITOCONDRIAL • LA ESPIRAL DE LYNEN (4 REACCIONES)
    # =========================================================================
    
    # 3. Palmitoil-CoA en Matriz (y=735)
    partes.append(crear_metabolito(
        x=x_metab, y=735,
        id_tag="m_palmitoil_coa_mat",
        nombre="Palmitoil-CoA (Matriz)",
        carbonos="16 Carbonos (Acil-CoA Matricial)",
        detalle="Sustrato que inicia el ciclo de 4 pasos de la espiral",
        svg_estructura=PALMITOIL_COA
    ))

    # Reacción 2: Paso 1 de la Espiral - Acil-CoA Deshidrogenasa (VLCAD/LCAD)
    partes.append(crear_reaccion(
        x=x_eje, y=820,
        id_tag="rx_paso1_dh",
        enzima="1. Acil-CoA Deshidrogenasa",
        ec="VLCAD / LCAD (EC 1.3.8.8)",
        regulacion="Introduce doble enlace trans-Δ²",
        entra_energia="FAD",
        sale_energia="+ 1 FADH₂ (➔ 1.5 ATP)",
        es_ganancia=True,
        altura=60
    ))

    # 4. trans-Δ²-Enoil-CoA (y=925)
    partes.append(crear_metabolito(
        x=x_metab, y=925,
        id_tag="m_trans_enoil_coa",
        nombre="trans-Δ²-Enoil-CoA",
        carbonos="16 Carbonos (Alqueno conjugado trans)",
        detalle="Doble enlace entre C-α (C2) y C-β (C3)",
        svg_estructura=TRANS_DELTA2_ENOIL_COA
    ))

    # Reacción 3: Paso 2 de la Espiral - Enoil-CoA Hidratasa (Crotonasa)
    partes.append(crear_reaccion(
        x=x_eje, y=1030,
        id_tag="rx_paso2_crotonasa",
        enzima="2. Enoil-CoA Hidratasa",
        ec="Crotonasa (EC 4.2.1.17)",
        regulacion="Adición estereoespecífica en C-β",
        entrada_agua=True,
        altura=60
    ))

    # 5. L-β-Hidroxiacil-CoA (y=1135)
    partes.append(crear_metabolito(
        x=x_metab, y=1135,
        id_tag="m_hidroxiacil_coa",
        nombre="L-β-Hidroxiacil-CoA",
        carbonos="16 Carbonos (Alcohol secundario L)",
        detalle="Isómero L obligatorio para la deshidrogenasa",
        svg_estructura=L_BETA_HIDROXIACIL_COA
    ))

    # Reacción 4: Paso 3 de la Espiral - L-β-Hidroxiacil-CoA Deshidrogenasa (L-HAD)
    partes.append(crear_reaccion(
        x=x_eje, y=1240,
        id_tag="rx_paso3_bhad",
        enzima="3. β-Hidroxiacil-CoA Deshidrogenasa",
        ec="L-HAD (EC 1.1.1.35)",
        regulacion="Oxida -OH secundario a β-ceto carbonilo",
        entra_energia="NAD⁺",
        sale_energia="+ 1 NADH + H⁺ (➔ 2.5 ATP)",
        es_ganancia=True,
        altura=60
    ))

    # 6. β-Cetoacil-CoA (y=1345)
    partes.append(crear_metabolito(
        x=x_metab, y=1345,
        id_tag="m_cetoacil_coa",
        nombre="β-Cetoacil-CoA",
        carbonos="16 Carbonos (β-Dicarbonilo)",
        detalle="Enlace Cα-Cβ altamente reactivo a la tiólisis",
        svg_estructura=BETA_CETOACIL_COA
    ))

    # Reacción 5: Paso 4 de la Espiral - β-Cetotiolasa (Tiolasa)
    partes.append(crear_reaccion(
        x=x_eje, y=1450,
        id_tag="rx_paso4_tiolasa",
        enzima="4. β-Cetotiolasa (Tiolasa / ACAT)",
        ec="EC 2.3.1.16 • Clivaje tiolítico",
        regulacion="Corte entre carbono α y β: libera 2C",
        entrada_coa=True,
        altura=65
    ))

    # =========================================================================
    # BIFURCACIÓN DE PRODUCTOS: ACETIL-CoA [2C] Y ACIL-CoA ACORTADO [14C]
    # =========================================================================
    partes.append(f"""
    <!-- Bifurcación tiolítica (fill='none' estricto) -->
    <path d="M {x_eje} 1520 Q {x_eje} 1565 540 1590" fill="none" stroke="#ea580c" stroke-width="2.6" marker-end="url(#arrowFlow)"/>
    <path d="M {x_eje} 1520 Q {x_eje} 1565 230 1590" fill="none" stroke="#ea580c" stroke-width="2.6" marker-end="url(#arrowFlow)"/>
    """)

    # Producto A: Acetil-CoA [2C] a la derecha (y=1575)
    partes.append(f"""
    <g id="m_acetil_coa_prod" data-arrastrable="1" transform="translate(540, 1575)">
      <g transform="translate(0, 0)">
        {ACETIL_COA_BETA}
      </g>
      <g transform="translate(135, 25)">
        <text x="0" y="0" fill="#0f172a" font-size="16.5" font-weight="800" font-family="'Inter', sans-serif">Acetil-CoA</text>
        <text x="0" y="18" fill="#ea580c" font-size="12" font-weight="700" font-family="'JetBrains Mono', monospace">[2C]</text>
        <text x="0" y="34" fill="#059669" font-size="11" font-weight="800" font-family="'Inter', sans-serif">➔ Alimenta Ciclo de Krebs (Citrato Sintasa)</text>
      </g>
    </g>
    """)

    # Producto B: Miristoil-CoA [14C] a la izquierda (y=1575)
    partes.append(f"""
    <g id="m_miristoil_coa_prod" data-arrastrable="1" transform="translate(40, 1575)">
      <g transform="translate(0, 0)">
        {MIRISTOIL_COA}
      </g>
      <g transform="translate(210, 25)">
        <text x="0" y="0" fill="#0f172a" font-size="15" font-weight="800" font-family="'Inter', sans-serif">Acil-CoA Acortado</text>
        <text x="0" y="18" fill="#ea580c" font-size="12" font-weight="700" font-family="'JetBrains Mono', monospace">[14C] Miristoil-CoA</text>
        <text x="0" y="34" fill="#64748b" font-size="10.5" font-family="'Inter', sans-serif">Reingresa al ciclo</text>
      </g>
    </g>
    """)

    # Bucle de retorno de la Espiral de Lynen hacia Palmitoil-CoA (Matriz) en y=730
    partes.append(f"""
    <!-- Bucle de Reingreso a la Espiral de Lynen (fill='none' estricto) -->
    <path d="M 50 1575 C -15 1575, -15 750, 230 750" fill="none" stroke="#ea580c" stroke-width="2.6" stroke-dasharray="8 6" marker-end="url(#arrowFlow)"/>
    
    <!-- Texto sobre el bucle -->
    <g transform="translate(45, 1150)">
      <text x="0" y="0" fill="#b45309" font-size="11.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle" transform="rotate(-90 0 0)">
        Espiral de Lynen: 7 Ciclos Completos (16C ➔ 8 Acetil-CoA)
      </text>
    </g>
    """)

    return "\n".join(partes)

def main():
    contenido_svg = generar_svg_completo()
    
    # 1. Guardar SVG
    ruta_svg = "/home/dolfius/Escritorio/materias/mapa_metabolico/03_LIPIDOS/01_beta_oxidacion/Beta_Oxidacion.svg"
    svg_final = f'<svg width="1000" height="1750" viewBox="0 0 1000 1750" xmlns="http://www.w3.org/2000/svg">\n{contenido_svg}\n</svg>'
    with open(ruta_svg, "w", encoding="utf-8") as f:
        f.write(svg_final)
    print(f"SVG generado en {ruta_svg}")

    # 2. Guardar HTML interactivo
    ruta_html = "/home/dolfius/Escritorio/materias/mapa_metabolico/03_LIPIDOS/01_beta_oxidacion/Beta_Oxidacion.html"
    html_final = CABECERA_HTML + contenido_svg + PIE_HTML
    with open(ruta_html, "w", encoding="utf-8") as f:
        f.write(html_final)
    print(f"HTML generado en {ruta_html}")

if __name__ == "__main__":
    main()
