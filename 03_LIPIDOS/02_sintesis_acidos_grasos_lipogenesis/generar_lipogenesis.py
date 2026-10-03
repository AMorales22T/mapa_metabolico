#!/usr/bin/env python3
"""
GENERADOR DE LA LIPOGÉNESIS (SÍNTESIS DE NOVO DE ÁCIDOS GRASOS)
================================================================
Diseñado en concordancia 100% estricta con el estilo editorial de:
- 01_CARBOHIDRATOS/01_glucolisis/Glucolisis.svg
- 02_RESPIRACION_Y_ENERGIA/02_ciclo_de_krebs/Ciclo_de_Krebs.svg
- 03_LIPIDOS/01_beta_oxidacion/Beta_Oxidacion.svg

Características:
- Lienzo vertical clásico de 1000 x 1950 px.
- Flujo central libre sobre fondo biológico real (Matriz mitocondrial arriba ➔ Citosol abajo).
- Sin tarjetas ni globos artificiales; metabolitos y enzimas libres.
- Trazos oscuros #0f172a, oxígenos en rojo #dc2626, OH en azul #0284c7, S-CoA en púrpura #7c3aed, S-ACP en verde azulado #0d9488.
- Todas las rutas y curvas de Bézier tienen fill="none" (cero polígonos/triángulos negros).
- Todo elemento móvil identificado con data-arrastrable="1" e IDs semánticos.
"""

import os
from estructuras_lipogenesis import (
    CITRATO,
    ACETIL_COA_LIPO,
    MALONIL_COA,
    ACETOACETIL_ACP,
    D_BETA_HIDROXIACIL_ACP,
    TRANS_DELTA2_ENOIL_ACP,
    BUTIRIL_ACP,
    PALMITATO_LIBRE
)
from entorno_lipogenesis import DEFS_ENTORNO_LIPOGENESIS, generar_entorno_lipogenesis_svg

CABECERA_HTML = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Lipogénesis (Síntesis de Ácidos Grasos) en Entorno Biológico Real</title>
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
    <svg width="1000" height="1950" viewBox="0 0 1000 1950" xmlns="http://www.w3.org/2000/svg">
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
        <!-- Flecha de NADPH / Reducción (Verde azulado) -->
        <marker id="arrowTeal" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#0d9488" />
        </marker>

        """ + DEFS_ENTORNO_LIPOGENESIS + """
      </defs>
"""

PIE_HTML = """
    </svg>
  </div>
</body>
</html>
"""

def crear_metabolito(x, y, id_tag, nombre, carbonos, detalle="", svg_estructura="", texto_izquierda=False):
    """Construye un metabolito libre idéntico al estándar de Glucólisis y Beta-Oxidación."""
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
                   es_ganancia=False, entrada_agua=False, salida_agua=False, entrada_coa=False, 
                   es_nadph=False, altura=55):
    """Genera una reacción con arcos curvados idéntica a Glucólisis y Ciclo de Krebs."""
    curvas_energia = ""
    
    # 1. Entrada de energía o reactivo (desde la izquierda hacia el centro)
    if entra_energia:
        if es_nadph:
            color_entrada = "#0d9488"
            marcador_entrada = "url(#arrowTeal)"
        elif es_ganancia:
            color_entrada = "#475569"
            marcador_entrada = "url(#arrowSlate)"
        else:
            color_entrada = "#dc2626"
            marcador_entrada = "url(#arrowRed)"

        curvas_energia += f"""
        <path d="M -80 10 Q -30 10 -4 20" fill="none" stroke="{color_entrada}" stroke-width="1.8" marker-end="{marcador_entrada}"/>
        <text x="-85" y="13" fill="{color_entrada}" font-size="11" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">{entra_energia}</text>
        """
        
    # 2. Salida de producto energético (desde el centro hacia la izquierda)
    if sale_energia:
        if es_nadph:
            color_salida = "#475569"
            marcador_salida = "url(#arrowSlate)"
        elif es_ganancia:
            color_salida = "#059669"
            marcador_salida = "url(#arrowGreen)"
        else:
            color_salida = "#475569"
            marcador_salida = "url(#arrowSlate)"

        curvas_energia += f"""
        <path d="M -4 26 Q -30 36 -80 36" fill="none" stroke="{color_salida}" stroke-width="1.8" marker-end="{marcador_salida}"/>
        <text x="-85" y="39" fill="{color_salida}" font-size="11" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">{sale_energia}</text>
        """

    # 3. Entrada o salida de agua
    if entrada_agua:
        curvas_energia += f"""
        <path d="M -75 16 Q -25 16 -4 26" fill="none" stroke="#0284c7" stroke-width="1.8" marker-end="url(#arrowBlue)"/>
        <text x="-80" y="19" fill="#0284c7" font-size="11" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">+ 1 H₂O</text>
        """
    elif salida_agua:
        curvas_energia += f"""
        <path d="M -4 26 Q -25 36 -75 36" fill="none" stroke="#0284c7" stroke-width="1.8" marker-end="url(#arrowBlue)"/>
        <text x="-80" y="39" fill="#0284c7" font-size="11" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">- 1 H₂O</text>
        """

    # 4. Entrada de Coenzima A
    if entrada_coa:
        curvas_energia += f"""
        <path d="M -75 16 Q -25 16 -4 26" fill="none" stroke="#7c3aed" stroke-width="1.8" marker-end="url(#arrowPurple)"/>
        <text x="-80" y="19" fill="#7c3aed" font-size="11" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">+ 1 CoA-SH</text>
        """

    # Rótulo de regulación
    reg_svg = ""
    if regulacion:
        reg_svg = f"""<text x="0" y="27" fill="#059669" font-size="10" font-weight="800" font-family="'Inter', sans-serif">{regulacion}</text>"""

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
    """Genera el contenido SVG total de la Lipogénesis."""
    partes = []

    # 1. Fondo celular y compartimentos (MMI en y=220-265)
    partes.append(generar_entorno_lipogenesis_svg(ancho=1000, alto=1950, y_mmi_ini=220, y_mmi_fin=265))

    # Eje central de las reacciones: x = 385. Metabolitos: x = 240
    x_eje = 385
    x_metab = 240

    # =========================================================================
    # FASE 1: MATRIZ MITOCONDRIAL ➔ LANZADERA DEL CITRATO (MMI)
    # =========================================================================
    # 1. Citrato en la Matriz Mitocondrial (origen del sustrato carbonado)
    partes.append(crear_metabolito(
        x=x_metab, y=85,
        id_tag="m_citrato_matriz",
        nombre="Citrato (Matriz Mitocondrial)",
        carbonos="6 Carbonos (Tricarboxilato)",
        detalle="Condensación de Acetil-CoA + Oxalacetato en Krebs",
        svg_estructura=CITRATO
    ))

    # Transportador SLC25A1 incrustado en la MMI (y=242)
    partes.append(f"""
    <!-- Línea hacia el transportador -->
    <line x1="{x_eje}" y1="165" x2="{x_eje}" y2="230" stroke="#ea580c" stroke-width="2.6" marker-end="url(#arrowFlow)"/>

    <!-- Transportador SLC25A1 -->
    <g id="carrier_citrato" data-arrastrable="1" transform="translate({x_eje}, 242)">
      <rect x="-70" y="-13" width="140" height="26" rx="6" fill="#fef3c7" stroke="#b45309" stroke-width="2"/>
      <text x="0" y="5" fill="#78350f" font-size="11.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">SLC25A1 (Carrier)</text>
      <text x="78" y="4" fill="#0284c7" font-size="9.5" font-weight="800" font-family="'Inter', sans-serif">Antiporte Citrato / Malato</text>
    </g>

    <!-- Línea saliente hacia el citosol -->
    <line x1="{x_eje}" y1="255" x2="{x_eje}" y2="285" stroke="#ea580c" stroke-width="2.6" marker-end="url(#arrowFlow)"/>
    """)

    # 2. Citrato en el Citosol (y=330)
    partes.append(crear_metabolito(
        x=x_metab, y=330,
        id_tag="m_citrato_citosol",
        nombre="Citrato (Citosol)",
        carbonos="6 Carbonos (Sustrato Citosólico)",
        detalle="Exportado desde la mitocondria para alimentar la síntesis",
        svg_estructura=CITRATO
    ))

    # =========================================================================
    # FASE 2: CLIVAJE Y ACTIVACIÓN (ATP CITRATO LIASA Y ACC)
    # =========================================================================
    # Reacción 1: ATP Citrato Liasa
    partes.append(crear_reaccion(
        x=x_eje, y=425,
        id_tag="rx_citrato_liasa",
        enzima="ATP Citrato Liasa (ACLY)",
        ec="EC 2.3.3.8 • Citrato + CoA + ATP",
        regulacion="Libera Oxalacetato (➔ NADPH por Enzima Málica)",
        entra_energia="- 1 ATP + CoA-SH",
        sale_energia="+ Oxalacetato + ADP",
        es_ganancia=False,
        altura=60
    ))

    # 3. Acetil-CoA Citosólico (y=530)
    partes.append(crear_metabolito(
        x=x_metab, y=530,
        id_tag="m_acetil_coa_cit",
        nombre="Acetil-CoA (Citosol)",
        carbonos="2 Carbonos (Unidad de Cebado)",
        detalle="Unidad carbonada fundamental para la cadena",
        svg_estructura=ACETIL_COA_LIPO
    ))

    # Reacción 2: Acetil-CoA Carboxilasa (ACC) [PASO COMPROMETIDO / MARCAPASOS]
    partes.append(crear_reaccion(
        x=x_eje, y=630,
        id_tag="rx_acc_carboxilasa",
        enzima="Acetil-CoA Carboxilasa (ACC)",
        ec="EC 6.4.1.2 • Marcapasos alostérico",
        regulacion="⊕ Activada por Citrato • ⊣ Glucagón / AMPK",
        entra_energia="- 1 ATP + HCO₃⁻",
        sale_energia="+ ADP + Pi",
        es_ganancia=False,
        altura=60
    ))

    # 4. Malonil-CoA (y=735)
    partes.append(crear_metabolito(
        x=x_metab, y=735,
        id_tag="m_malonil_coa",
        nombre="Malonil-CoA",
        carbonos="3 Carbonos (Unidad de Elongación)",
        detalle="Aporta unidades de 2C con descarboxilación impulsora",
        svg_estructura=MALONIL_COA
    ))

    # Señal reguladora cruzada de Malonil-CoA hacia Beta-Oxidación
    partes.append(f"""
    <!-- Conexión inhibitoria hacia CPT-I (curva amplia a la izquierda del texto) -->
    <path d="M 180 765 C 18 765, 18 590, 60 565" fill="none" stroke="#dc2626" stroke-width="2" stroke-dasharray="6 4" marker-end="url(#arrowRed)"/>
    <g transform="translate(68, 645)">
      <text x="0" y="0" fill="#dc2626" font-size="10" font-weight="900" font-family="'Inter', sans-serif">
        ⛔ Señal Cruzada:
      </text>
      <text x="0" y="14" fill="#b91c1c" font-size="9" font-weight="800" font-family="'Inter', sans-serif">
        Inhibe CPT-I en β-Oxidación
      </text>
    </g>
    """)

    # =========================================================================
    # FASE 3: EL COMPLEJO ÁCIDO GRASO SINTASA (FASN) • CICLO DE 4 PASOS
    # =========================================================================
    # Transición de carga al complejo FASN (y=815 a 850)
    partes.append(f"""
    <line x1="{x_eje}" y1="815" x2="{x_eje}" y2="850" stroke="#ea580c" stroke-width="2.6" marker-end="url(#arrowFlow)"/>
    
    <!-- Rótulo de cebado en la FASN -->
    <g transform="translate({x_eje + 20}, 833)">
      <text x="0" y="0" fill="#0f766e" font-size="12" font-weight="900" font-family="'Inter', sans-serif">Cebado de FASN (MAT):</text>
      <text x="0" y="14" fill="#64748b" font-size="10" font-family="'JetBrains Mono', monospace">Acetil-CoA (en KS) + Malonil-CoA (en ACP)</text>
    </g>
    """)

    # 5. Acetoacetil-ACP (Paso 1: Condensación por KS) (y=875)
    partes.append(crear_metabolito(
        x=x_metab, y=875,
        id_tag="m_acetoacetil_acp",
        nombre="Acetoacetil-ACP",
        carbonos="4 Carbonos (Condensación KS)",
        detalle="Unión de acilo + malonilo con liberación de CO₂",
        svg_estructura=ACETOACETIL_ACP
    ))

    # Reacción 3: 1ª Reducción - β-Cetoacil-ACP Reductasa (KR)
    partes.append(crear_reaccion(
        x=x_eje, y=975,
        id_tag="rx_paso1_kr",
        enzima="1. β-Cetoacil-ACP Reductasa (KR)",
        ec="Dominio KR de FASN",
        regulacion="Reduce carbonilo β a alcohol D-β",
        entra_energia="- 1 NADPH + H⁺",
        sale_energia="+ NADP⁺",
        es_nadph=True,
        altura=60
    ))

    # 6. D-β-Hidroxiacil-ACP (y=1080)
    partes.append(crear_metabolito(
        x=x_metab, y=1080,
        id_tag="m_hidroxiacil_acp",
        nombre="D-β-Hidroxiacil-ACP",
        carbonos="4 Carbonos (Alcohol Secundario D)",
        detalle="Isómero D obligatorio característico de la síntesis",
        svg_estructura=D_BETA_HIDROXIACIL_ACP
    ))

    # Reacción 4: Deshidratación - β-Hidroxiacil-ACP Deshidratasa (DH)
    partes.append(crear_reaccion(
        x=x_eje, y=1180,
        id_tag="rx_paso2_dh",
        enzima="2. β-Hidroxiacil-ACP Deshidratasa (DH)",
        ec="Dominio DH de FASN",
        regulacion="Introduce doble enlace trans-Δ²",
        salida_agua=True,
        altura=60
    ))

    # 7. trans-Δ²-Enoil-ACP (y=1285)
    partes.append(crear_metabolito(
        x=x_metab, y=1285,
        id_tag="m_trans_enoil_acp",
        nombre="trans-Δ²-Enoil-ACP",
        carbonos="4 Carbonos (Alqueno conjugado trans)",
        detalle="Intermedio insaturado trans previo a la saturación",
        svg_estructura=TRANS_DELTA2_ENOIL_ACP
    ))

    # Reacción 5: 2ª Reducción - Enoil-ACP Reductasa (ER)
    partes.append(crear_reaccion(
        x=x_eje, y=1385,
        id_tag="rx_paso3_er",
        enzima="3. Enoil-ACP Reductasa (ER)",
        ec="Dominio ER de FASN",
        regulacion="Saturación completa del enlace a simple",
        entra_energia="- 1 NADPH + H⁺",
        sale_energia="+ NADP⁺",
        es_nadph=True,
        altura=60
    ))

    # 8. Butiril-ACP (y=1490)
    partes.append(crear_metabolito(
        x=x_metab, y=1490,
        id_tag="m_butiril_acp",
        nombre="Butiril-ACP (Ciclo 1)",
        carbonos="4 Carbonos (Acilo saturado elongado)",
        detalle="Se transfiere a KS para recibir otro Malonil-ACP",
        svg_estructura=BUTIRIL_ACP
    ))

    # Bucle de Elongación de la FASN (7 vueltas completas)
    partes.append(f"""
    <!-- Bucle de Reingreso y Elongación FASN (fill='none' estricto) -->
    <path d="M 60 1525 C -5 1525, -5 890, 230 890" fill="none" stroke="#0d9488" stroke-width="2.6" stroke-dasharray="8 6" marker-end="url(#arrowFlow)"/>
    
    <!-- Texto sobre el bucle FASN -->
    <g transform="translate(45, 1210)">
      <text x="0" y="0" fill="#0f766e" font-size="11.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle" transform="rotate(-90 0 0)">
        Elongación FASN: 7 Ciclos Completos (+2C por ciclo con Malonil-ACP)
      </text>
    </g>
    """)

    # =========================================================================
    # FASE 4: TERMINACIÓN POR TIOESTERASA (TE) Y PRODUCTO FINAL
    # =========================================================================
    # Reacción 6: Tioesterasa (TE)
    partes.append(crear_reaccion(
        x=x_eje, y=1595,
        id_tag="rx_tioesterasa",
        enzima="4. Tioesterasa (TE / Palmitoil Proteína Tioesterasa)",
        ec="Dominio TE de FASN • Clivaje esterolítico",
        regulacion="Específica para cadenas C16: libera Palmitato",
        entrada_agua=True,
        altura=60
    ))

    # 9. Producto Final: Palmitato Libre (y=1700)
    partes.append(crear_metabolito(
        x=x_metab, y=1700,
        id_tag="m_palmitato_prod",
        nombre="Palmitato (Ácido Palmítico)",
        carbonos="16 Carbonos (Ácido Graso Libre Saturado)",
        detalle="Producto neto liberado por la Ácido Graso Sintasa",
        svg_estructura=PALMITATO_LIBRE
    ))

    # Conexión elegante hacia la Gota Lipídica / Esterificación en TAGs
    partes.append(f"""
    <!-- Flecha hacia la Gota Lipídica que apunta limpiamente al texto sin cruzarlo -->
    <path d="M {x_eje} 1775 Q {x_eje} 1865 605 1865" fill="none" stroke="#ea580c" stroke-width="2.6" stroke-dasharray="6 4" marker-end="url(#arrowFlow)"/>
    <g transform="translate(615, 1860)">
      <text x="0" y="0" fill="#d97706" font-size="12" font-weight="900" font-family="'Inter', sans-serif">
        ➔ Incorporación a Triacilgliceroles (TAGs)
      </text>
      <text x="0" y="16" fill="#92400e" font-size="10" font-weight="700" font-family="'Inter', sans-serif">
        Acil-CoA Sintetasa + Glicerol-3-Fosfato (RE)
      </text>
    </g>
    """)

    return "\n".join(partes)

def main():
    contenido_svg = generar_svg_completo()
    
    # 1. Guardar SVG
    ruta_svg = "/home/dolfius/Escritorio/materias/mapa_metabolico/03_LIPIDOS/02_sintesis_acidos_grasos_lipogenesis/Lipogenesis.svg"
    svg_final = f'<svg width="1000" height="1950" viewBox="0 0 1000 1950" xmlns="http://www.w3.org/2000/svg">\n{contenido_svg}\n</svg>'
    with open(ruta_svg, "w", encoding="utf-8") as f:
        f.write(svg_final)
    print(f"SVG generado en {ruta_svg}")

    # 2. Guardar HTML interactivo
    ruta_html = "/home/dolfius/Escritorio/materias/mapa_metabolico/03_LIPIDOS/02_sintesis_acidos_grasos_lipogenesis/Lipogenesis.html"
    html_final = CABECERA_HTML + contenido_svg + PIE_HTML
    with open(ruta_html, "w", encoding="utf-8") as f:
        f.write(html_final)
    print(f"HTML generado en {ruta_html}")

if __name__ == "__main__":
    main()
