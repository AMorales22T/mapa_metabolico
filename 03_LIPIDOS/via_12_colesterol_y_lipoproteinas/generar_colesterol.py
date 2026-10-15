#!/usr/bin/env python3
"""
GENERADOR DE LA SÍNTESIS DE COLESTEROL Y VÍA DEL MEVALONATO
============================================================
Diseñado en concordancia 100% estricta con el estilo editorial de:
- 01_CARBOHIDRATOS/via_01_glucolisis/Glucolisis.svg
- 02_RESPIRACION_Y_ENERGIA/via_06_ciclo_de_krebs/Ciclo_de_Krebs.svg
- 03_LIPIDOS/via_10_lipogenesis/Lipogenesis.svg

Características:
- Lienzo vertical clásico de 1000 x 2300 px.
- Flujo central libre sobre fondo biológico real (Citosol ➔ Membrana del REL ➔ Citosol/Vesículas).
- Sin tarjetas ni globos artificiales; metabolitos y enzimas libres.
- Trazos oscuros #0f172a, oxígenos en rojo #dc2626, OH en azul #0284c7, PPi en naranja #ea580c, S-CoA en púrpura #7c3aed.
- Todas las rutas y curvas de Bézier tienen fill="none" (cero polígonos/triángulos negros).
- Todo elemento móvil identificado con data-arrastrable="1" e IDs semánticos.
"""

import os
from estructuras_colesterol import (
    ACETOACETIL_COA_COLEST,
    HMG_COA_CITOSOL,
    MEVALONATO,
    ISOPENTENIL_PP,
    FARNESIL_PP,
    ESCUALENO,
    LANOSTEROL,
    COLESTEROL
)
from entorno_colesterol import DEFS_ENTORNO_COLESTEROL, generar_entorno_colesterol_svg

CABECERA_HTML = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Síntesis de Colesterol (Vía del Mevalonato) en Entorno Biológico Real</title>
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
    <svg width="1000" height="2300" viewBox="0 0 1000 2300" xmlns="http://www.w3.org/2000/svg">
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

        """ + DEFS_ENTORNO_COLESTEROL + """
      </defs>
"""

PIE_HTML = """
    </svg>
  </div>
</body>
</html>
"""

def crear_metabolito(x, y, id_tag, nombre, carbonos, detalle, svg_estructura, alineacion_derecha=True, dx_texto=210):
    """Genera un metabolito 100% libre en el espacio biológico."""
    if alineacion_derecha:
        pos_texto = f'translate({dx_texto}, 26)'
        pos_estructura = 'translate(0, 0)'
        alineacion = ''
    else:
        pos_texto = 'translate(-25, 26)'
        pos_estructura = 'translate(0, 0)'
        alineacion = 'text-anchor="end"'

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
                   es_nadph=False, altura=55, marcapasos=False):
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
        <path d="M -85 10 Q -30 10 -4 20" fill="none" stroke="{color_entrada}" stroke-width="1.8" marker-end="{marcador_entrada}"/>
        <text x="-90" y="13" fill="{color_entrada}" font-size="11" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">{entra_energia}</text>
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
        <path d="M -4 26 Q -30 36 -85 36" fill="none" stroke="{color_salida}" stroke-width="1.8" marker-end="{marcador_salida}"/>
        <text x="-90" y="39" fill="{color_salida}" font-size="11" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">{sale_energia}</text>
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

    # Rótulo de regulación
    reg_svg = ""
    if regulacion:
        color_reg = "#dc2626" if marcapasos else "#059669"
        reg_svg = f"""<text x="0" y="27" fill="{color_reg}" font-size="10" font-weight="800" font-family="'Inter', sans-serif">{regulacion}</text>"""

    borde_marcapasos = ""
    if marcapasos:
        borde_marcapasos = f"""
        <rect x="-10" y="-8" width="280" height="48" rx="6" fill="#fef2f2" stroke="#dc2626" stroke-width="1.5" stroke-dasharray="4 3" opacity="0.65"/>
        """

    return f"""
    <!-- Reacción: {enzima} -->
    <g id="{id_tag}" data-arrastrable="1" transform="translate({x}, {y})">
      <!-- Flecha central de flujo -->
      <line x1="0" y1="0" x2="0" y2="{altura}" stroke="#ea580c" stroke-width="2.6" marker-end="url(#arrowFlow)"/>
      
      <!-- Acoplamiento de reactivos y energía -->
      {curvas_energia}
      
      <!-- Textos informativos de la enzima a la derecha -->
      <g transform="translate(18, 14)">
        {borde_marcapasos}
        <text x="0" y="0" fill="#0f172a" font-size="12.5" font-weight="800" font-family="'Inter', sans-serif">{enzima}</text>
        <text x="0" y="14" fill="#64748b" font-size="10" font-family="'JetBrains Mono', monospace">{ec}</text>
        {reg_svg}
      </g>
    </g>
    """

def generar_svg_completo():
    """Genera el contenido SVG total de la Síntesis de Colesterol."""
    partes = []

    # 1. Fondo celular y compartimentos (Citosol + Membrana del REL en y=510-560)
    partes.append(generar_entorno_colesterol_svg(ancho=1000, alto=2300, y_rel_ini=510, y_rel_fin=560))

    # Eje central de las reacciones: x = 385. Metabolitos: x = 240
    x_eje = 385
    x_metab = 240

    # =========================================================================
    # FASE 1: CITOSOL • CONDENSACIÓN TEMPRANA (3 ACETIL-CoA ➔ HMG-CoA)
    # =========================================================================
    # Rótulo de origen del Acetil-CoA Citosólico
    partes.append(f"""
    <g transform="translate(80, 80)">
      <rect x="0" y="0" width="310" height="38" rx="8" fill="#ffedd5" stroke="#ea580c" stroke-width="2"/>
      <text x="15" y="18" fill="#9a3412" font-size="11.5" font-weight="900" font-family="'Inter', sans-serif">2 Acetil-CoA (de ATP Citrato Liasa / Citosol)</text>
      <text x="15" y="30" fill="#c2410c" font-size="9.5" font-weight="700" font-family="'JetBrains Mono', monospace">Pool citosólico compartido con Lipogénesis</text>
    </g>
    <path d="M 390 99 L {x_eje} 99 L {x_eje} 130" fill="none" stroke="#ea580c" stroke-width="2.6" marker-end="url(#arrowFlow)"/>
    """)

    # Reacción 1: Tiolasa Citosólica (ACAT2)
    partes.append(crear_reaccion(
        x=x_eje, y=130,
        id_tag="rx_tiolasa_colest",
        enzima="Tiolasa Citosólica (ACAT2 / Acetil-CoA Acetiltransferasa)",
        ec="EC 2.3.1.9 • Reversible",
        regulacion="Condensación de 2 Acetil-CoA",
        entra_energia="+ Acetil-CoA",
        sale_energia="- CoA-SH",
        es_ganancia=False,
        altura=55
    ))

    # 1. Acetoacetil-CoA (y=215)
    partes.append(crear_metabolito(
        x=x_metab, y=215,
        id_tag="m_acetoacetil_coa_col",
        nombre="Acetoacetil-CoA",
        carbonos="4 Carbonos (Condensación Citosólica)",
        detalle="Intermedio común de síntesis de colesterol en citosol",
        svg_estructura=ACETOACETIL_COA_COLEST
    ))

    # Reacción 2: HMG-CoA Sintasa Citosólica (HMGCS1)
    partes.append(crear_reaccion(
        x=x_eje, y=310,
        id_tag="rx_hmg_sintasa_colest",
        enzima="HMG-CoA Sintasa Citosólica (HMGCS1)",
        ec="EC 2.3.3.10 • Isoforma citosólica (≠ mitocondrial)",
        regulacion="Incorpora el 3er Acetil-CoA con gasto de agua",
        entra_energia="+ Acetil-CoA + H₂O",
        sale_energia="- CoA-SH",
        es_ganancia=False,
        altura=60
    ))

    # 2. HMG-CoA Citosólico (y=400)
    partes.append(crear_metabolito(
        x=x_metab, y=400,
        id_tag="m_hmg_coa_cit",
        nombre="HMG-CoA (3-Hidroxi-3-Metilglutaril-CoA)",
        carbonos="6 Carbonos (Sustrato Clave del Marcapasos)",
        detalle="Listo para reducirse en la membrana del REL",
        svg_estructura=HMG_COA_CITOSOL
    ))

    # =========================================================================
    # FASE 2: RETÍCULO ENDOPLÁSMICO LISO (REL) • HMGCR (EL GRAN MARCAPASOS)
    # =========================================================================
    # Reacción 3: HMG-CoA Reductasa (HMGCR) [PASO COMPROMETIDO Y REGULADO]
    partes.append(crear_reaccion(
        x=x_eje, y=500,
        id_tag="rx_hmg_reductasa",
        enzima="HMG-CoA Reductasa (HMGCR) • [PASO LIMITANTE]",
        ec="EC 1.1.1.34 • Anclada a la membrana del REL",
        regulacion="⊕ Insulina, SREBP-2 • ⊣ Glucagón, AMPK, Estatinas",
        entra_energia="- 2 NADPH + 2 H⁺",
        sale_energia="+ 2 NADP⁺ + CoA-SH",
        es_nadph=True,
        altura=65,
        marcapasos=True
    ))

    # Anotación clínica: Diana de las Estatinas
    partes.append(f"""
    <!-- Bloque de diana terapéutica: Estatinas -->
    <g id="diana_estatinas" transform="translate(685, 495)">
      <rect x="0" y="0" width="265" height="52" rx="8" fill="#fee2e2" stroke="#dc2626" stroke-width="1.8"/>
      <text x="12" y="18" fill="#991b1b" font-size="11.5" font-weight="900" font-family="'Inter', sans-serif">💊 DIANA CLÍNICA: ESTATINAS</text>
      <text x="12" y="32" fill="#b91c1c" font-size="9.5" font-family="'Inter', sans-serif">Atorvastatina, Rosuvastatina, Simvastatina</text>
      <text x="12" y="44" fill="#7f1d1d" font-size="9" font-weight="700" font-family="'Inter', sans-serif">Inhibición competitiva reversible de HMGCR</text>
      <!-- Flecha indicadora -->
      <path d="M 0 26 L -25 26" fill="none" stroke="#dc2626" stroke-width="1.8" marker-end="url(#arrowRed)"/>
    </g>
    """)

    # 3. Mevalonato (y=605)
    partes.append(crear_metabolito(
        x=x_metab, y=605,
        id_tag="m_mevalonato",
        nombre="Mevalonato (Ácido Mevalónico)",
        carbonos="6 Carbonos (Paso Irreversible Cumplido)",
        detalle="Comprometido irrevocablemente a la síntesis de isoprenoides",
        svg_estructura=MEVALONATO
    ))

    # =========================================================================
    # FASE 3: FORMACIÓN DE UNIDADES ISOPRÉNICAS ACTIVADAS (IPP / DMAPP)
    # =========================================================================
    # Reacción 4: Fosforilaciones y Descarboxilación (3 ATP)
    partes.append(crear_reaccion(
        x=x_eje, y=705,
        id_tag="rx_mevalonato_a_ipp",
        enzima="Mevalonato Quinasa ➔ Fosfomevalonato Quinasa ➔ Descarboxilasa",
        ec="EC 2.7.1.36 ➔ EC 2.7.4.2 ➔ EC 4.1.1.33",
        regulacion="3 ATP consecutivos liberan CO₂ y Pi para activar la molécula",
        entra_energia="- 3 ATP",
        sale_energia="+ 3 ADP + CO₂ + Pi",
        es_ganancia=False,
        altura=60
    ))

    # 4. Isopentenil Pirofosfato (IPP) (y=800)
    partes.append(crear_metabolito(
        x=x_metab, y=800,
        id_tag="m_ipp",
        nombre="Isopentenil Pirofosfato (IPP)",
        carbonos="5 Carbonos (Unidad Isoprénica 'Ladrillo Biológico')",
        detalle="En equilibrio isomérico con Dimetilalil Pirofosfato (DMAPP)",
        svg_estructura=ISOPENTENIL_PP,
        dx_texto=210
    ))

    # Equilibrio IPP ⇄ DMAPP (desplazado a la derecha para no tocar el título)
    partes.append(f"""
    <g transform="translate(735, 805)">
      <path d="M 0 0 L 50 0" fill="none" stroke="#0ea5e9" stroke-width="2" marker-end="url(#arrowBlue)"/>
      <path d="M 50 8 L 0 8" fill="none" stroke="#0ea5e9" stroke-width="2" marker-end="url(#arrowBlue)"/>
      <text x="25" y="-8" fill="#0369a1" font-size="10" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Isomerasa</text>
      <text x="65" y="7" fill="#0f172a" font-size="12" font-weight="900" font-family="'Inter', sans-serif">DMAPP [5C]</text>
    </g>
    """)

    # =========================================================================
    # FASE 4: CONDENSACIÓN PRENÍLICA (IPP + DMAPP ➔ GPP ➔ FPP)
    # =========================================================================
    # Reacción 5: Preniltransferasas (Condensación cabeza-cola)
    partes.append(crear_reaccion(
        x=x_eje, y=905,
        id_tag="rx_farnesil_sintasa",
        enzima="Farnesil Pirofosfato Sintasa (Preniltransferasa)",
        ec="EC 2.5.1.10 • IPP (5C) + DMAPP (5C) ➔ Geranil-PP (10C) + IPP ➔ FPP (15C)",
        regulacion="Hidrólisis de PPi (Pirofosfato) impulsa fuertemente la síntesis",
        entra_energia="+ 2 IPP (5C)",
        sale_energia="+ 2 PPi",
        es_ganancia=False,
        altura=60
    ))

    # 5. Farnesil Pirofosfato (FPP) (y=1000)
    partes.append(crear_metabolito(
        x=x_metab, y=1000,
        id_tag="m_fpp",
        nombre="Farnesil Pirofosfato (FPP)",
        carbonos="15 Carbonos (Punto de Ramificación Isoprenoide)",
        detalle="Precursor no solo de colesterol, sino de CoQ10, Dolicol y Prenilación",
        svg_estructura=FARNESIL_PP,
        dx_texto=210
    ))

    # Ramificación lateral: Dolicol, CoQ10 y Prenilación de proteínas Ras
    partes.append(f"""
    <!-- Flechas y llamadas a vías paralelas desde FPP -->
    <path d="M 520 1025 Q 640 1025, 680 1000" fill="none" stroke="#7c3aed" stroke-width="2" stroke-dasharray="6 3" marker-end="url(#arrowPurple)"/>
    <g transform="translate(690, 995)">
      <text x="0" y="0" fill="#6d28d9" font-size="10.5" font-weight="900" font-family="'Inter', sans-serif">✦ Ramificaciones no-esterol:</text>
      <text x="0" y="14" fill="#7c3aed" font-size="9.5" font-family="'Inter', sans-serif">• Ubiquinona / CoQ₁₀ (Cadena Respiratoria)</text>
      <text x="0" y="26" fill="#7c3aed" font-size="9.5" font-family="'Inter', sans-serif">• Dolicol-Fosfato (N-glicosilación en RER)</text>
      <text x="0" y="38" fill="#7c3aed" font-size="9.5" font-family="'Inter', sans-serif">• Prenilación de proteínas (Ras, Rho)</text>
    </g>
    """)

    # =========================================================================
    # FASE 5: CONDENSACIÓN COLA-CON-COLA (FPP + FPP ➔ ESCUALENO)
    # =========================================================================
    # Reacción 6: Escualeno Sintasa
    partes.append(crear_reaccion(
        x=x_eje, y=1105,
        id_tag="rx_escualeno_sintasa",
        enzima="Escualeno Sintasa (FDFT1)",
        ec="EC 2.5.1.21 • Condensación reductora cabeza-con-cabeza (15C + 15C)",
        regulacion="Primer paso comprometido exclusivamente a la vía esteroidea",
        entra_energia="- 1 NADPH + H⁺",
        sale_energia="+ NADP⁺ + 2 PPi",
        es_nadph=True,
        altura=60
    ))

    # 6. Escualeno (y=1200)
    partes.append(crear_metabolito(
        x=x_metab, y=1200,
        id_tag="m_escualeno",
        nombre="Escualeno",
        carbonos="30 Carbonos (Hidrocarburo Lineal Completo)",
        detalle="Listo para la epoxidación y la gran ciclación molecular",
        svg_estructura=ESCUALENO,
        dx_texto=210
    ))

    # =========================================================================
    # FASE 6: OXIDACIÓN Y CICLACIÓN TETRACÍCLICA (LANOSTEROL)
    # =========================================================================
    # Reacción 7: Escualeno Monooxigenasa + Oxidoscualeno Ciclasa
    partes.append(crear_reaccion(
        x=x_eje, y=1310,
        id_tag="rx_ciclacion_escualeno",
        enzima="Escualeno Monooxigenasa + Oxidoscualeno Ciclasa (LSS)",
        ec="EC 1.14.14.17 ➔ EC 5.4.99.7 • Cascada catiónica estereocontrolada",
        regulacion="Oxida con O₂ a 2,3-epoxiescualeno y cierra los 4 anillos (A, B, C, D)",
        entra_energia="- 1 NADPH + O₂",
        sale_energia="+ NADP⁺ + H₂O",
        es_nadph=True,
        altura=65
    ))

    # 7. Lanosterol (y=1415, ancho de molécula ~250px -> dx_texto=270)
    partes.append(crear_metabolito(
        x=x_metab, y=1415,
        id_tag="m_lanosterol",
        nombre="Lanosterol",
        carbonos="30 Carbonos (Primer Esteroide Tetracíclico)",
        detalle="Núcleo esteroideo cerrado con 3 metilos adicionales (C4, C14)",
        svg_estructura=LANOSTEROL,
        dx_texto=270
    ))

    # =========================================================================
    # FASE 7: TRANSFORMACIÓN FINAL EN EL REL (19 PASOS ➔ COLESTEROL)
    # =========================================================================
    # Reacción 8: Red de Transformación del REL (Bloch y Kandutsch-Russell)
    partes.append(crear_reaccion(
        x=x_eje, y=1525,
        id_tag="rx_lanosterol_a_colesterol",
        enzima="Vías de Bloch &amp; Kandutsch-Russell (19 reacciones enzimáticas)",
        ec="Desmetilasas (CYP51A1), Δ14-Reductasa, Δ7-Δ8 Isomerasa, 7-DHC Reductasa",
        regulacion="Elimina 3 metilos (libera CO₂/formiato), reduce dobles enlaces (requiere NADPH)",
        entra_energia="- NADPH + O₂",
        sale_energia="+ NADP⁺ + 3 CO₂ / HCOOH",
        es_nadph=True,
        altura=65
    ))

    # 8. COLESTEROL (PRODUCTO FINAL) (y=1630, ancho de molécula ~280px -> dx_texto=300)
    partes.append(crear_metabolito(
        x=x_metab, y=1630,
        id_tag="m_colesterol_final",
        nombre="Colesterol (Colest-5-en-3β-ol)",
        carbonos="27 Carbonos (Esteroide Fundamental)",
        detalle="Componente esencial de membranas y precursor esteroideo universal",
        svg_estructura=COLESTEROL,
        dx_texto=300
    ))

    # =========================================================================
    # FASE 8: DESTINOS BIOLÓGICOS DEL COLESTEROL (ZONA INFERIOR)
    # =========================================================================
    # Destino 1: Membrana Plasmática
    partes.append(f"""
    <path d="M {x_eje} 1720 Q {x_eje} 1780, 240 1840" fill="none" stroke="#0284c7" stroke-width="2.6" marker-end="url(#arrowBlue)"/>
    <g transform="translate(140, 1850)">
      <rect x="0" y="0" width="230" height="50" rx="8" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.8"/>
      <text x="12" y="18" fill="#0369a1" font-size="11.5" font-weight="900" font-family="'Inter', sans-serif">1. FLUIDEZ DE MEMBRANA</text>
      <text x="12" y="32" fill="#0284c7" font-size="9.5" font-family="'Inter', sans-serif">Incorporación a balsas lipídicas (rafts)</text>
      <text x="12" y="44" fill="#075985" font-size="9" font-weight="700" font-family="'Inter', sans-serif">Regula permeabilidad y señalización celular</text>
    </g>
    """)

    # Destino 2: Ésteres de Colesterol (Gota Lipídica / VLDL)
    partes.append(f"""
    <path d="M {x_eje} 1720 L {x_eje} 1840" fill="none" stroke="#ea580c" stroke-width="2.6" marker-end="url(#arrowFlow)"/>
    <g transform="translate(395, 1850)">
      <rect x="0" y="0" width="240" height="50" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="1.8"/>
      <text x="12" y="18" fill="#92400e" font-size="11.5" font-weight="900" font-family="'Inter', sans-serif">2. ÉSTERES DE COLESTEROL (CE)</text>
      <text x="12" y="32" fill="#b45309" font-size="9.5" font-family="'Inter', sans-serif">ACAT (Células) / LCAT (HDL sanguíneo)</text>
      <text x="12" y="44" fill="#78350f" font-size="9" font-weight="700" font-family="'Inter', sans-serif">Empaquetamiento en VLDL ➔ Transporte</text>
    </g>
    """)

    # Destino 3: Ácidos Biliares y Hormonas Esteroideas
    partes.append(f"""
    <path d="M {x_eje} 1720 Q {x_eje} 1780, 720 1840" fill="none" stroke="#059669" stroke-width="2.6" marker-end="url(#arrowGreen)"/>
    <g transform="translate(660, 1850)">
      <rect x="0" y="0" width="250" height="50" rx="8" fill="#dcfce7" stroke="#059669" stroke-width="1.8"/>
      <text x="12" y="18" fill="#166534" font-size="11.5" font-weight="900" font-family="'Inter', sans-serif">3. ÁCIDOS BILIARES &amp; HORMONAS</text>
      <text x="12" y="32" fill="#15803d" font-size="9.5" font-family="'Inter', sans-serif">• 7α-Hidroxilasa ➔ Cólico y Quenodesoxicólico</text>
      <text x="12" y="44" fill="#14532d" font-size="9" font-weight="700" font-family="'Inter', sans-serif">• Desmolasa (CYP11A1) ➔ Pregnenolona / Cortisol</text>
    </g>
    """)

    # Resumen estequiométrico en pie de página
    partes.append(f"""
    <g transform="translate(200, 2020)">
      <rect x="0" y="0" width="600" height="70" rx="10" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
      <text x="20" y="24" fill="#0f172a" font-size="12" font-weight="900" font-family="'Inter', sans-serif">BALANCE BIOENERGÉTICO GLOBAL DE LA SÍNTESIS DE COLESTEROL:</text>
      <text x="20" y="44" fill="#ea580c" font-size="11.5" font-weight="800" font-family="'JetBrains Mono', monospace">18 Acetil-CoA + 36 ATP + 16 NADPH + O₂ ➔ Colesterol + 18 CoA + 36 ADP + 16 NADP⁺</text>
      <text x="20" y="60" fill="#64748b" font-size="10" font-family="'Inter', sans-serif">Altamente demandante de poder reductor provisto por la Vía de las Pentosas Fosfato y Enzima Málica.</text>
    </g>
    """)

    return "\n".join(partes)

def main():
    contenido_svg = generar_svg_completo()
    
    # 1. Guardar SVG
    ruta_svg = "/home/dolfius/Escritorio/materias/mapa_metabolico/03_LIPIDOS/via_12_colesterol_y_lipoproteinas/Colesterol.svg"
    svg_final = f'<svg width="1000" height="2300" viewBox="0 0 1000 2300" xmlns="http://www.w3.org/2000/svg">\n{contenido_svg}\n</svg>'
    with open(ruta_svg, "w", encoding="utf-8") as f:
        f.write(svg_final)
    print(f"SVG generado en {ruta_svg}")

    # 2. Guardar HTML interactivo
    ruta_html = "/home/dolfius/Escritorio/materias/mapa_metabolico/03_LIPIDOS/via_12_colesterol_y_lipoproteinas/Colesterol.html"
    html_final = CABECERA_HTML + contenido_svg + PIE_HTML
    with open(ruta_html, "w", encoding="utf-8") as f:
        f.write(html_final)
    print(f"HTML generado en {ruta_html}")

if __name__ == "__main__":
    main()
