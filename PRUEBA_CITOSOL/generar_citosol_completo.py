#!/usr/bin/env python3
"""
EL MAPA METABÓLICO INTEGRADO: CITOSOL COMPLETO Y GRAN MATRIZ MITOCONDRIAL
==========================================================================
Este mapa resuelve la visión integral de la célula:
1. CITOSOL COMO COMPARTIMENTO CERRADO Y BIOLÓGICO:
   - Membrana plasmática continua con bicapa lipídica exterior.
   - Receptor GLUT-4 completo con su LUPA DE AUMENTO MOLECULAR (difusión facilitada).
   - Textura biológica real: filamentos de citoesqueleto cruzando el citoplasma,
     polirribosomas en racimos y vesículas lipídicas de doble contorno.
   - Fondo con gradiente acuoso citoplasmático suave (#ffffff -> #f8fafc -> #f0fdf4).
2. RUTAS TOTALMENTE DESARROLLADAS:
   - Glucólisis completa (11 metabolitos y 10 reacciones).
   - Vía de las Pentosas Fosfato completa (10 metabolitos, Fase Oxidativa y
     No Oxidativa con Transcetolasa 1, Transaldolasa y Transcetolasa 2, con sus
     retornos a F6P y GAP).
3. TERRITORIOS DE LAS RUTAS CITOSÓLICAS RESTANTES:
   - Glucógeno (G6P <-> G1P <-> UDP-Glucosa <-> Glucógeno) a la izquierda.
   - Bypass de Gluconeogénesis (G6Pasa, FBPasa-1, PEPCK citosol).
   - Lípidos Citosólicos (Glicerol-3P -> TAGs y Lipogénesis FAS con NADPH).
   - Síntesis de Nucleótidos (PRPP -> Purinas y Pirimidinas) a la derecha.
   - Destinos del Piruvato (L-Lactato/LDH, L-Alanina/ALT).
   - Tramo Citosólico del Ciclo de la Urea (Citrulina -> Argininosuccinato -> Arginina -> Urea).
4. GRAN MATRIZ MITOCONDRIAL ESPACIOSA Y REAL:
   - Doble membrana anatómica (externa e interna con crestas onduladas profundas).
   - Espacio intermembrana para gradiente de protones (H⁺).
   - Amplio espacio interior para albergar con total claridad:
     * Complejo Piruvato Deshidrogenasa (PDH).
     * Rueda completa del Ciclo de Krebs (TCA) con sus 8 intermediarios y cofactores.
     * Cadena Respiratoria y ATP Sintasa en las crestas.
     * Lanzadera de Citrato (CIC) y Lanzadera de Citrulina/Ornitina (ORNT).
"""

import os
import sys

# Rutas a los módulos existentes
DIR_RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(os.path.join(DIR_RAIZ, "01_CARBOHIDRATOS", "via_01_glucolisis"))
sys.path.append(os.path.join(DIR_RAIZ, "01_CARBOHIDRATOS", "via_04_pentosas_fosfato"))

from estructuras_glucosa import (
    GLUCOSA, GLUCOSA_6_FOSFATO, FRUCTOSA_6_FOSFATO, FRUCTOSA_1_6_BISFOSFATO,
    DIHIDROXIACETONA_FOSFATO, GLICERALDEHIDO_3_FOSFATO, BISFOSFOGLICERATO_1_3,
    FOSFOGLICERATO_3, FOSFOGLICERATO_2, FOSFOENOLPIRUVATO, PIRUVATO
)

from estructuras_pentosas import (
    FOSFOGLUCONO_LACTONA_6, FOSFOGLUCONATO_6, RIBULOSA_5_FOSFATO,
    RIBOSA_5_FOSFATO, XILULOSA_5_FOSFATO, SEDOHEPTULOSA_7_FOSFATO, ERITROSA_4_FOSFATO
)

ANCHO_CANVAS = 2600
ALTO_CANVAS = 3100

# -----------------------------------------------------------------------------
# GENERADORES DE METABOLITOS Y REACCIONES EDITORIALES
# -----------------------------------------------------------------------------
def crear_metabolito(x, y, nombre, carbonos, detalle="", svg_estructura="", texto_izquierda=False):
    """Construye el bloque SVG de un metabolito libre con su estructura y textos."""
    if texto_izquierda:
        pos_estructura = "translate(150, 0)"
        pos_texto = "translate(130, 25)"
        alineacion = 'text-anchor="end"'
    else:
        pos_estructura = "translate(0, 0)"
        pos_texto = "translate(135, 25)"
        alineacion = ''

    return f"""
    <!-- Metabolito: {nombre} -->
    <g transform="translate({x}, {y})">
      <g transform="{pos_estructura}">
        {svg_estructura}
      </g>
      <g transform="{pos_texto}">
        <text x="0" y="0" fill="#0f172a" font-size="15" font-weight="800" {alineacion}>{nombre}</text>
        <text x="0" y="17" fill="#ea580c" font-size="11.5" font-weight="700" {alineacion}>{carbonos}</text>
        <text x="0" y="32" fill="#64748b" font-size="10.5" {alineacion}>{detalle}</text>
      </g>
    </g>
    """

def crear_reaccion(x, y, enzima, ec="", regulacion="", entra_energia="", sale_energia="", 
                   reversible=False, es_ganancia=False, salida_agua=False, altura=48):
    """Genera una reacción vertical con cofactores y enzimas."""
    curvas_energia = ""
    if entra_energia:
        color_entrada = "#dc2626" if not es_ganancia else "#475569"
        marcador_entrada = "url(#arrowRed)" if not es_ganancia else "url(#arrowSlate)"
        curvas_energia += f"""
        <path d="M -75 8 Q -25 8 -4 18" fill="none" stroke="{color_entrada}" stroke-width="1.8" marker-end="{marcador_entrada}"/>
        <text x="-80" y="11" fill="{color_entrada}" font-size="10.5" font-weight="800" text-anchor="end">{entra_energia}</text>
        """
    if sale_energia:
        color_salida = "#059669" if es_ganancia else "#475569"
        marcador_salida = "url(#arrowGreen)" if es_ganancia else "url(#arrowSlate)"
        curvas_energia += f"""
        <path d="M -4 24 Q -25 34 -75 34" fill="none" stroke="{color_salida}" stroke-width="1.8" marker-end="{marcador_salida}"/>
        <text x="-80" y="37" fill="{color_salida}" font-size="10.5" font-weight="800" text-anchor="end">{sale_energia}</text>
        """
    if salida_agua:
        curvas_energia += """
        <path d="M -4 24 Q -25 34 -70 34" fill="none" stroke="#0284c7" stroke-width="1.8" marker-end="url(#arrowBlue)"/>
        <text x="-75" y="37" fill="#0284c7" font-size="10.5" font-weight="800" text-anchor="end">- 2 H₂O</text>
        """

    if reversible:
        flecha = f"""
        <line x1="-3" y1="0" x2="-3" y2="{altura}" stroke="#ea580c" stroke-width="1.8" marker-end="url(#arrowFlow)"/>
        <line x1="3" y1="{altura}" x2="3" y2="0" stroke="#ea580c" stroke-width="1.8" marker-end="url(#arrowFlow)"/>
        """
    else:
        flecha = f"""
        <line x1="0" y1="0" x2="0" y2="{altura}" stroke="#ea580c" stroke-width="2.5" marker-end="url(#arrowFlow)"/>
        """

    regulacion_svg = ""
    if regulacion:
        color_reg = "#e11d48" if "⊣" in regulacion else "#16a34a"
        regulacion_svg = f'<text x="0" y="26" fill="{color_reg}" font-size="9.5" font-weight="700">{regulacion}</text>'

    return f"""
    <!-- Reacción: {enzima} -->
    <g transform="translate({x}, {y})">
      {flecha}
      {curvas_energia}
      <g transform="translate(18, 12)">
        <text x="0" y="0" fill="#0f172a" font-size="12" font-weight="800">{enzima}</text>
        <text x="0" y="13" fill="#64748b" font-size="9.5" font-family="'JetBrains Mono', monospace">{ec}</text>
        {regulacion_svg}
      </g>
    </g>
    """

def crear_reaccion_oxidativa(x, y, enzima, ec="", regulacion="", genera_nadph=False, entra_agua=False, salida_co2=False, altura=48):
    """Genera una reacción de la fase oxidativa de pentosas fosfato."""
    curvas = ""
    if genera_nadph:
        curvas += """
        <path d="M -65 8 Q -25 8 -4 18" fill="none" stroke="#475569" stroke-width="1.8" marker-end="url(#arrowSlate)"/>
        <text x="-70" y="11" fill="#475569" font-size="10" font-weight="800" text-anchor="end">+ NADP⁺</text>
        <path d="M -4 24 Q -25 34 -70 34" fill="none" stroke="#059669" stroke-width="1.8" marker-end="url(#arrowGreen)"/>
        <text x="-75" y="38" fill="#059669" font-size="10" font-weight="800" text-anchor="end">+ NADPH + H⁺</text>
        """
    if entra_agua:
        curvas += """
        <path d="M -65 8 Q -25 8 -4 18" fill="none" stroke="#0284c7" stroke-width="1.8" marker-end="url(#arrowBlue)"/>
        <text x="-70" y="11" fill="#0284c7" font-size="10" font-weight="800" text-anchor="end">+ H₂O</text>
        """
    if salida_co2:
        curvas += """
        <path d="M 4 24 Q 25 34 65 34" fill="none" stroke="#475569" stroke-width="1.8" marker-end="url(#arrowSlate)"/>
        <text x="70" y="38" fill="#475569" font-size="10" font-weight="800">+ CO₂</text>
        """

    regulacion_svg = ""
    if regulacion:
        color_reg = "#e11d48" if "⊣" in regulacion else "#16a34a"
        regulacion_svg = f'<text x="0" y="26" fill="{color_reg}" font-size="9" font-weight="700">{regulacion}</text>'

    return f"""
    <!-- Reacción Oxidativa: {enzima} -->
    <g transform="translate({x}, {y})">
      <line x1="0" y1="0" x2="0" y2="{altura}" stroke="#ea580c" stroke-width="2.5" marker-end="url(#arrowFlow)"/>
      {curvas}
      <g transform="translate(18, 12)">
        <text x="0" y="0" fill="#0f172a" font-size="12" font-weight="800">{enzima}</text>
        <text x="0" y="13" fill="#64748b" font-size="9.5" font-family="'JetBrains Mono', monospace">{ec}</text>
        {regulacion_svg}
      </g>
    </g>
    """

def crear_paso_no_oxidativo(x, y, enzima, ec, sustratos_txt, productos_txt):
    """Genera un nodo de transferencia no oxidativa."""
    return f"""
    <!-- Reacción de Transferencia: {enzima} -->
    <g transform="translate({x}, {y})">
      <line x1="-3" y1="0" x2="-3" y2="45" stroke="#ea580c" stroke-width="1.8" marker-end="url(#arrowFlow)"/>
      <line x1="3" y1="45" x2="3" y2="0" stroke="#ea580c" stroke-width="1.8" marker-end="url(#arrowFlow)"/>
      <g transform="translate(18, 10)">
        <text x="0" y="0" fill="#0f172a" font-size="12.5" font-weight="800">{enzima}</text>
        <text x="0" y="14" fill="#64748b" font-size="9.5" font-family="'JetBrains Mono', monospace">{ec}</text>
        <text x="0" y="28" fill="#c2410c" font-size="9.5" font-weight="700">{sustratos_txt} ⇄ {productos_txt}</text>
      </g>
    </g>
    """

# -----------------------------------------------------------------------------
# DIBUJO DEL ENTORNO BIOLÓGICO: CITOSOL CERRADO, CITOESQUELETO Y MITOCONDRIA
# -----------------------------------------------------------------------------
def generar_entorno_completo(ancho, alto):
    """Genera la anatomía de toda la célula biológica con citoesqueleto y mitocondria gigante."""
    return f"""
    <!-- Medio Extracelular circundante -->
    <rect width="{ancho}" height="{alto}" fill="#e2e8f0"/>

    <!-- ============================================================= -->
    <!-- FORMA CERRADA DE LA CÉLULA (MEMBRANA PLASMÁTICA ENVOLVENTE)   -->
    <!-- ============================================================= -->
    <path d="M 180,120 
             C 800,50 1800,50 2420,120 
             C 2560,200 2560,2800 2400,3000 
             C 1800,3080 700,3080 160,3000 
             C 20,2800 20,200 180,120 Z" 
          fill="#ffffff" 
          stroke="#0284c7" 
          stroke-width="14" 
          stroke-linejoin="round"/>

    <!-- Capa interior de fosfolípidos (bicapa lipídica) -->
    <path d="M 180,120 
             C 800,50 1800,50 2420,120 
             C 2560,200 2560,2800 2400,3000 
             C 1800,3080 700,3080 160,3000 
             C 20,2800 20,200 180,120 Z" 
          fill="url(#gradCitosolCelular)" 
          stroke="#38bdf8" 
          stroke-width="4" 
          stroke-dasharray="8 5"/>

    <text x="1300" y="42" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#64748b" text-anchor="middle" letter-spacing="2">
      ESPACIO EXTRACELULAR (SANGRE / LÍQUIDO INTERSTICIAL)
    </text>

    <!-- ============================================================= -->
    <!-- CITOESQUELETO BIOLÓGICO REAL, POLIRRIBOSOMAS Y VESÍCULAS      -->
    <!-- ============================================================= -->
    <g opacity="0.32" stroke="#94a3b8" fill="none">
      <!-- Microfilamentos de actina y microtúbulos -->
      <path d="M 80 260 Q 600 180 1300 280 T 2480 230" stroke-width="1.8" stroke-dasharray="8 6"/>
      <path d="M 100 580 Q 700 660 1400 600 T 2460 620" stroke-width="1.5" stroke-dasharray="7 7"/>
      <path d="M 70 940 Q 650 880 1350 950 T 2490 920" stroke-width="1.7" stroke-dasharray="8 5"/>
      <path d="M 90 1380 Q 750 1450 1450 1400 T 2470 1420" stroke-width="1.6" stroke-dasharray="8 6"/>
      <path d="M 80 1820 Q 650 1760 1300 1840 T 2480 1800" stroke-width="1.6" stroke-dasharray="6 6"/>
      <path d="M 100 2150 Q 550 2200 1100 2150" stroke-width="1.5" stroke-dasharray="7 6"/>
    </g>

    <!-- Polirribosomas en racimos celulares libres en el citoplasma -->
    <g fill="#94a3b8" opacity="0.25">
      <circle cx="200" cy="200" r="2.5"/><circle cx="206" cy="202" r="2"/><circle cx="204" cy="208" r="2.3"/><circle cx="198" cy="207" r="2.1"/>
      <circle cx="980" cy="260" r="2.5"/><circle cx="986" cy="262" r="2"/><circle cx="984" cy="268" r="2.3"/>
      <circle cx="1750" cy="220" r="2.5"/><circle cx="1757" cy="222" r="2"/><circle cx="1754" cy="228" r="2.3"/>
      <circle cx="2400" cy="400" r="2.5"/><circle cx="2406" cy="402" r="2"/><circle cx="2404" cy="408" r="2.3"/>
      <circle cx="220" cy="850" r="2.5"/><circle cx="226" cy="852" r="2"/><circle cx="224" cy="858" r="2.3"/>
      <circle cx="1020" cy="890" r="2.5"/><circle cx="1026" cy="892" r="2"/><circle cx="1024" cy="898" r="2.3"/>
      <circle cx="2420" cy="1200" r="2.5"/><circle cx="2426" cy="1202" r="2"/><circle cx="2424" cy="1208" r="2.3"/>
      <circle cx="240" cy="1650" r="2.5"/><circle cx="246" cy="1652" r="2"/><circle cx="244" cy="1658" r="2.3"/>
      <circle cx="980" cy="1720" r="2.5"/><circle cx="986" cy="1722" r="2"/><circle cx="984" cy="1728" r="2.3"/>
    </g>

    <!-- Vesículas citoplasmáticas translúcidas de doble contorno -->
    <g opacity="0.28">
      <circle cx="210" cy="480" r="24" fill="#e0f2fe" stroke="#38bdf8" stroke-width="1.8" stroke-dasharray="4 2"/>
      <circle cx="210" cy="480" r="17" fill="none" stroke="#7dd3fc" stroke-width="1"/>
      <circle cx="1120" cy="620" r="20" fill="#e0f2fe" stroke="#38bdf8" stroke-width="1.8" stroke-dasharray="4 2"/>
      <circle cx="1120" cy="620" r="14" fill="none" stroke="#7dd3fc" stroke-width="1"/>
      <circle cx="2380" cy="720" r="26" fill="#e0f2fe" stroke="#38bdf8" stroke-width="1.8" stroke-dasharray="4 2"/>
      <circle cx="2380" cy="720" r="19" fill="none" stroke="#7dd3fc" stroke-width="1"/>
      <circle cx="180" cy="1950" r="22" fill="#e0f2fe" stroke="#38bdf8" stroke-width="1.8" stroke-dasharray="4 2"/>
      <circle cx="180" cy="1950" r="15" fill="none" stroke="#7dd3fc" stroke-width="1"/>
    </g>

    <!-- ============================================================= -->
    <!-- RECEPTOR GLUT-4 Y SU LUPA DE AUMENTO MOLECULAR CIENTÍFICA     -->
    <!-- ============================================================= -->
    <g transform="translate(680, 70)">
      <path d="M 0 5 C 10 -12, 28 -12, 34 5 C 38 18, 34 36, 25 42 C 12 45, 2 35, 0 22 Z" fill="#0284c7" stroke="#0369a1" stroke-width="2.2"/>
      <path d="M 80 5 C 70 -12, 52 -12, 46 5 C 42 18, 46 36, 55 42 C 68 45, 78 35, 80 22 Z" fill="#0284c7" stroke="#0369a1" stroke-width="2.2"/>
      <ellipse cx="40" cy="20" rx="10" ry="18" fill="#e0f2fe" stroke="#38bdf8" stroke-width="1.8"/>
      <polygon points="40,14 45,17 45,23 40,26 35,23 35,17" fill="#ffffff" stroke="#ea580c" stroke-width="1.6"/>
      <circle cx="35" cy="17" r="2" fill="#dc2626"/>
      <text x="40" y="49" fill="#0369a1" font-size="10" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">GLUT-4</text>
    </g>

    <line x1="720" y1="45" x2="720" y2="70" stroke="#ea580c" stroke-width="2.2"/>
    <line x1="720" y1="110" x2="720" y2="135" stroke="#ea580c" stroke-width="2.5" marker-end="url(#arrowFlow)"/>

    <!-- LUPA MOLECULAR CON PROYECCIONES CÓNICAS -->
    <g stroke="#38bdf8" stroke-width="1.4" stroke-dasharray="4 3" opacity="0.7">
      <line x1="680" y1="90" x2="525" y2="115" />
      <line x1="690" y1="70" x2="490" y2="65" />
    </g>
    <g transform="translate(420, 110)">
      <circle cx="0" cy="0" r="70" fill="#ffffff" stroke="#0284c7" stroke-width="3.5" />
      <circle cx="0" cy="0" r="66" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1" />
      <g opacity="0.85">
        <g fill="#0284c7">
          <circle cx="-55" cy="-8" r="5"/><circle cx="-40" cy="-8" r="5"/><circle cx="-25" cy="-8" r="5"/>
          <circle cx="25" cy="-8" r="5"/><circle cx="40" cy="-8" r="5"/><circle cx="55" cy="-8" r="5"/>
        </g>
        <g stroke="#94a3b8" stroke-width="1.4" fill="none">
          <path d="M -55 -3 Q -57 2 -53 7"/><path d="M -40 -3 Q -42 2 -38 7"/><path d="M -25 -3 Q -27 2 -23 7"/>
          <path d="M 25 -3 Q 23 2 27 7"/><path d="M 40 -3 Q 38 2 42 7"/><path d="M 55 -3 Q 53 2 57 7"/>
          <path d="M -55 17 Q -57 12 -53 7"/><path d="M -40 17 Q -42 12 -38 7"/><path d="M -25 17 Q -27 12 -23 7"/>
          <path d="M 25 17 Q 23 12 27 7"/><path d="M 40 17 Q 38 12 42 7"/><path d="M 55 17 Q 53 12 57 7"/>
        </g>
        <g fill="#0284c7">
          <circle cx="-55" cy="22" r="5"/><circle cx="-40" cy="22" r="5"/><circle cx="-25" cy="22" r="5"/>
          <circle cx="25" cy="22" r="5"/><circle cx="40" cy="22" r="5"/><circle cx="55" cy="22" r="5"/>
        </g>
      </g>
      <path d="M -18 -24 C -9 -28, -4 -16, -4 0 C -4 16, -9 28, -18 24 C -27 20, -25 -20, -18 -24 Z" fill="#0284c7" stroke="#0369a1" stroke-width="2"/>
      <path d="M 18 -24 C 9 -28, 4 -16, 4 0 C 4 16, 9 28, 18 24 C 27 20, 25 -20, 18 -24 Z" fill="#0284c7" stroke="#0369a1" stroke-width="2"/>
      <ellipse cx="0" cy="0" rx="7" ry="20" fill="#bae6fd" opacity="0.6"/>
      <g transform="translate(0, -7)">
        <polygon points="0,-11 10,-5 10,6 0,13 -10,6 -10,-5" fill="#ffffff" stroke="#0f172a" stroke-width="2"/>
        <circle cx="-10" cy="-5" r="3" fill="#ffffff"/>
        <text x="-10" y="-3" fill="#dc2626" font-size="6" font-weight="900" text-anchor="middle">O</text>
        <circle cx="15" cy="6" r="4.5" fill="#ffedd5" stroke="#ea580c" stroke-width="1.2"/>
        <text x="15" y="8.5" fill="#ea580c" font-size="5.5" font-weight="900" text-anchor="middle">OH</text>
      </g>
      <path d="M 0 -28 L 0 -17" stroke="#ea580c" stroke-width="2.2" marker-end="url(#arrowFlow)"/>
      <path d="M 0 11 L 0 28" stroke="#ea580c" stroke-width="2.2" marker-end="url(#arrowFlow)"/>
      <rect x="-60" y="47" width="120" height="16" rx="4" fill="#0f172a" opacity="0.9"/>
      <text x="0" y="59" fill="#ffffff" font-size="8" font-weight="800" text-anchor="middle" letter-spacing="0.5">DIFUSIÓN FACILITADA</text>
    </g>


    <!-- ============================================================= -->
    <!-- LA GRAN MITOCONDRIA BIOLÓGICA ESPACIOSA (ZONA INFERIOR)       -->
    <!-- ============================================================= -->
    <!-- Gran estructura arriñonada con espacio inmenso para PDH, Krebs y Cadena Respiratoria -->
    <g id="gran-mitocondria" transform="translate(680, 2150)">
      <!-- Membrana Mitocondrial Externa Lisa (Ámbar) -->
      <path d="M 0,90 
               C 300,10 1100,10 1780,90 
               C 1880,180 1880,750 1750,860 
               C 1100,920 300,920 30,860 
               C -50,750 -50,180 0,90 Z" 
            fill="#fffbeb" 
            stroke="#ea580c" 
            stroke-width="5"/>

      <!-- Espacio Intermembrana (acumulación de H+) -->
      <path d="M 15,105 
               C 310,30 1090,30 1765,105 
               C 1855,190 1855,735 1735,845 
               C 1090,905 310,905 45,845 
               C -30,735 -30,190 15,105 Z" 
            fill="none" 
            stroke="#f59e0b" 
            stroke-width="3" 
            stroke-dasharray="8 5"/>

      <!-- Matriz Mitocondrial Interior (Cálida y espaciosa) -->
      <path d="M 35,120 
               C 320,50 1080,50 1745,120 
               C 1830,200 1830,720 1720,830 
               C 1080,885 320,885 60,830 
               C -15,720 -15,200 35,120 Z" 
            fill="#fef3c7" 
            stroke="#d97706" 
            stroke-width="3.5" 
            opacity="0.95"/>

      <!-- Crestas Mitocondriales Reales (Invaginaciones donde se sitúa la Cadena Respiratoria) -->
      <g stroke="#b45309" stroke-width="3" fill="none" opacity="0.6">
        <!-- Cresta 1 (arriba izquierda) -->
        <path d="M 80,140 Q 150,220 80,300"/>
        <!-- Cresta 2 (abajo izquierda) -->
        <path d="M 70,550 Q 140,640 70,720"/>
        <!-- Cresta 3 (fondo inferior) -->
        <path d="M 350,860 Q 420,780 490,860"/>
        <path d="M 850,870 Q 920,790 990,870"/>
        <path d="M 1350,860 Q 1420,780 1490,860"/>
        <!-- Cresta 4 (lateral derecho) -->
        <path d="M 1720,320 Q 1640,400 1720,480"/>
        <path d="M 1710,600 Q 1630,680 1710,760"/>
      </g>

      <!-- TRANSPORTADORES DE LA MEMBRANA MITOCONDRIAL -->
      <!-- 1. Transportador MPC (Piruvato) -->
      <g transform="translate(60, 75)">
        <rect x="-18" y="-18" width="36" height="42" rx="8" fill="#ea580c" stroke="#fed7aa" stroke-width="2.5"/>
        <text x="0" y="7" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="900" fill="#ffffff" text-anchor="middle">MPC</text>
        <text x="26" y="7" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#c2410c">MPC (Entrada de Piruvato)</text>
      </g>

      <!-- 2. Transportador Tricarboxilato (CIC: Salida de Citrato para Lipogénesis) -->
      <g transform="translate(480, 50)">
        <rect x="-18" y="-18" width="36" height="42" rx="8" fill="#d97706" stroke="#fde68a" stroke-width="2.5"/>
        <text x="0" y="7" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="900" fill="#ffffff" text-anchor="middle">CIC</text>
        <text x="26" y="7" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#b45309">CIC (Salida de Citrato)</text>
      </g>

      <!-- 3. Lanzadera Ornitina/Citrulina (ORNT: Ciclo de la Urea) -->
      <g transform="translate(1300, 60)">
        <rect x="-18" y="-18" width="36" height="42" rx="8" fill="#059669" stroke="#a7f3d0" stroke-width="2.5"/>
        <text x="0" y="7" font-family="'JetBrains Mono', monospace" font-size="10.5" font-weight="900" fill="#ffffff" text-anchor="middle">ORNT</text>
        <text x="26" y="7" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#047857">ORNT (Citrulina/Ornitina)</text>
      </g>

      <!-- =========================================================== -->
      <!-- TERRITORIOS DENTRO DE LA GRAN MATRIZ MITOCONDRIAL           -->
      <!-- =========================================================== -->
      <!-- TÍTULO DE LA MATRIZ -->
      <text x="880" y="160" font-family="'Inter', sans-serif" font-size="16" font-weight="900" fill="#b45309" text-anchor="middle" letter-spacing="2">
        MATRIZ MITOCONDRIAL (TERRITORIO DE ALTA ENERGÍA)
      </text>

      <!-- A) COMPLEJO PIRUVATO DESHIDROGENASA (PDH) -->
      <g transform="translate(140, 240)">
        <rect x="0" y="0" width="360" height="150" rx="10" fill="#ffffff" stroke="#ea580c" stroke-width="2"/>
        <text x="15" y="24" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#c2410c">COMPLEJO PIRUVATO DESHIDROGENASA (PDH)</text>
        <text x="15" y="42" font-family="'JetBrains Mono', monospace" font-size="9.5" fill="#64748b">E1 (TPP) • E2 (Lipoamida) • E3 (FAD)</text>
        
        <path d="M 40 85 L 120 85" stroke="#ea580c" stroke-width="2.5" marker-end="url(#arrowFlow)"/>
        <text x="80" y="75" font-family="'Inter', sans-serif" font-size="9" font-weight="700" fill="#059669" text-anchor="middle">NAD⁺ ➔ NADH + CO₂</text>
        
        <rect x="135" y="65" width="180" height="40" rx="6" fill="#ffedd5" stroke="#ea580c" stroke-width="1.8"/>
        <text x="225" y="85" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="900" fill="#9a3412" text-anchor="middle">ACETIL-CoA (2C)</text>
        <text x="225" y="100" font-family="'Inter', sans-serif" font-size="8.5" fill="#c2410c" text-anchor="middle">Sustrato de entrada al Ciclo de Krebs</text>
      </g>

      <!-- Conexión MPC -> PDH -->
      <path d="M 60 110 Q 60 180 140 280" fill="none" stroke="#ea580c" stroke-width="2.5" marker-end="url(#arrowFlow)"/>

      <!-- B) EL GRAN CICLO DE KREBS (CICLO DEL ÁCIDO CÍTRICO - TCA) -->
      <g transform="translate(880, 480)">
        <!-- Anillo central del ciclo -->
        <circle cx="0" cy="0" r="160" fill="none" stroke="#d97706" stroke-width="3" stroke-dasharray="10 5"/>
        <circle cx="0" cy="0" r="150" fill="#ffffff" opacity="0.85"/>
        <text x="0" y="-10" font-family="'Inter', sans-serif" font-size="14" font-weight="900" fill="#92400e" text-anchor="middle">CICLO DE KREBS</text>
        <text x="0" y="8" font-family="'Inter', sans-serif" font-size="10" font-weight="700" fill="#b45309" text-anchor="middle">(8 Reacciones Enzimáticas)</text>
        <text x="0" y="26" font-family="'JetBrains Mono', monospace" font-size="9" fill="#059669" text-anchor="middle">3 NADH • 1 FADH₂ • 1 GTP</text>

        <!-- Los 8 Metabolitos del Ciclo en círculo amplio -->
        <!-- 1. Citrato (arriba) -->
        <g transform="translate(0, -160)">
          <rect x="-45" y="-14" width="90" height="28" rx="5" fill="#fef3c7" stroke="#d97706" stroke-width="1.6"/>
          <text x="0" y="4" font-family="'Inter', sans-serif" font-size="10" font-weight="800" fill="#78350f" text-anchor="middle">Citrato (6C)</text>
        </g>
        <!-- 2. Isocitrato -->
        <g transform="translate(120, -100)">
          <rect x="-45" y="-14" width="90" height="28" rx="5" fill="#fef3c7" stroke="#d97706" stroke-width="1.6"/>
          <text x="0" y="4" font-family="'Inter', sans-serif" font-size="10" font-weight="800" fill="#78350f" text-anchor="middle">Isocitrato (6C)</text>
        </g>
        <!-- 3. α-Cetoglutarato -->
        <g transform="translate(160, 20)">
          <rect x="-55" y="-14" width="110" height="28" rx="5" fill="#fef3c7" stroke="#d97706" stroke-width="1.6"/>
          <text x="0" y="4" font-family="'Inter', sans-serif" font-size="9.5" font-weight="800" fill="#78350f" text-anchor="middle">α-Cetoglutarato (5C)</text>
        </g>
        <!-- 4. Succinil-CoA -->
        <g transform="translate(110, 130)">
          <rect x="-50" y="-14" width="100" height="28" rx="5" fill="#fef3c7" stroke="#d97706" stroke-width="1.6"/>
          <text x="0" y="4" font-family="'Inter', sans-serif" font-size="9.5" font-weight="800" fill="#78350f" text-anchor="middle">Succinil-CoA (4C)</text>
        </g>
        <!-- 5. Succinato -->
        <g transform="translate(0, 160)">
          <rect x="-45" y="-14" width="90" height="28" rx="5" fill="#fef3c7" stroke="#d97706" stroke-width="1.6"/>
          <text x="0" y="4" font-family="'Inter', sans-serif" font-size="10" font-weight="800" fill="#78350f" text-anchor="middle">Succinato (4C)</text>
        </g>
        <!-- 6. Fumarato -->
        <g transform="translate(-120, 110)">
          <rect x="-45" y="-14" width="90" height="28" rx="5" fill="#fef3c7" stroke="#d97706" stroke-width="1.6"/>
          <text x="0" y="4" font-family="'Inter', sans-serif" font-size="10" font-weight="800" fill="#78350f" text-anchor="middle">Fumarato (4C)</text>
        </g>
        <!-- 7. L-Malato -->
        <g transform="translate(-160, 0)">
          <rect x="-45" y="-14" width="90" height="28" rx="5" fill="#fef3c7" stroke="#d97706" stroke-width="1.6"/>
          <text x="0" y="4" font-family="'Inter', sans-serif" font-size="10" font-weight="800" fill="#78350f" text-anchor="middle">L-Malato (4C)</text>
        </g>
        <!-- 8. Oxalacetato -->
        <g transform="translate(-110, -110)">
          <rect x="-50" y="-14" width="100" height="28" rx="5" fill="#fef3c7" stroke="#d97706" stroke-width="1.6"/>
          <text x="0" y="4" font-family="'Inter', sans-serif" font-size="9.5" font-weight="800" fill="#78350f" text-anchor="middle">Oxalacetato (4C)</text>
        </g>
      </g>

      <!-- Conexión Acetil-CoA -> Citrato -->
      <path d="M 500 310 Q 700 290 850 320" fill="none" stroke="#ea580c" stroke-width="2.5" marker-end="url(#arrowFlow)"/>
      <text x="680" y="285" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#b45309" text-anchor="middle">Citrato Sintasa (+ OAA 4C)</text>

      <!-- Salida de Citrato hacia el transportador CIC -->
      <path d="M 880 300 Q 600 200 480 85" fill="none" stroke="#d97706" stroke-width="2.2" stroke-dasharray="6 3" marker-end="url(#arrowFlow)"/>

      <!-- C) CADENA DE TRANSPORTE DE ELECTRONES Y FOSFORILACIÓN OXIDATIVA -->
      <g transform="translate(1300, 260)">
        <rect x="0" y="0" width="380" height="150" rx="10" fill="#ffffff" stroke="#059669" stroke-width="2"/>
        <text x="15" y="24" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#047857">CADENA RESPIRATORIA EN CRESTAS</text>
        <text x="15" y="42" font-family="'Inter', sans-serif" font-size="9.5" fill="#065f46">Bombeo de protones H⁺ hacia el espacio intermembrana</text>

        <!-- Complejos I, II, III, IV y ATP Sintasa -->
        <g transform="translate(20, 65)">
          <rect x="0" y="0" width="45" height="34" rx="4" fill="#dcfce7" stroke="#059669" stroke-width="1.5"/>
          <text x="22" y="21" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="900" fill="#065f46" text-anchor="middle">I</text>
          
          <rect x="55" y="0" width="45" height="34" rx="4" fill="#dcfce7" stroke="#059669" stroke-width="1.5"/>
          <text x="77" y="21" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="900" fill="#065f46" text-anchor="middle">II</text>
          
          <rect x="110" y="0" width="45" height="34" rx="4" fill="#dcfce7" stroke="#059669" stroke-width="1.5"/>
          <text x="132" y="21" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="900" fill="#065f46" text-anchor="middle">III</text>

          <rect x="165" y="0" width="45" height="34" rx="4" fill="#dcfce7" stroke="#059669" stroke-width="1.5"/>
          <text x="187" y="21" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="900" fill="#065f46" text-anchor="middle">IV</text>

          <rect x="230" y="-8" width="105" height="50" rx="6" fill="#fef08a" stroke="#ca8a04" stroke-width="2"/>
          <text x="282" y="14" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#854d0e" text-anchor="middle">ATP SINTASA</text>
          <text x="282" y="30" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="800" fill="#a16207" text-anchor="middle">ADP + Pi ➔ ATP</text>
        </g>
        <text x="15" y="130" font-family="'Inter', sans-serif" font-size="9" font-weight="700" fill="#047857">NADH ➔ 2.5 ATP | FADH₂ ➔ 1.5 ATP</text>
      </g>

      <!-- Alimentación de electrones desde Krebs hacia la Cadena Respiratoria -->
      <path d="M 1030 450 Q 1200 380 1300 340" fill="none" stroke="#059669" stroke-width="2.5" stroke-dasharray="6 3" marker-end="url(#arrowGreen)"/>
      <text x="1150" y="370" font-family="'Inter', sans-serif" font-size="9" font-weight="800" fill="#047857">NADH / FADH₂</text>

      <!-- D) FASE MITOCONDRIAL DEL CICLO DE LA UREA (CPS-1 Y OTC) -->
      <g transform="translate(1320, 520)">
        <rect x="0" y="0" width="340" height="120" rx="10" fill="#eff6ff" stroke="#3b82f6" stroke-width="2"/>
        <text x="15" y="22" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#1d4ed8">CICLO DE LA UREA (MATRIZ MITOCONDRIAL)</text>
        <text x="15" y="40" font-family="'Inter', sans-serif" font-size="8.5" fill="#2563eb">CPS-1: NH₄⁺ + HCO₃⁻ + 2 ATP ➔ Carbamil-P</text>
        <text x="15" y="58" font-family="'Inter', sans-serif" font-size="8.5" fill="#2563eb">OTC: Carbamil-P + Ornitina ➔ L-Citrulina</text>
        
        <!-- Flecha hacia transportador ORNT -->
        <path d="M 170 70 Q 170 110 80 110" fill="none" stroke="#3b82f6" stroke-width="2" marker-end="url(#arrowBlue)"/>
        <text x="170" y="90" font-family="'Inter', sans-serif" font-size="9" font-weight="800" fill="#1d4ed8">Citrulina sale al Citosol</text>
      </g>
    </g>
    """

def generar_html_mapa_celular():
    """Ensambla el documento HTML completo con todas las rutas y detalles."""
    svg_parts = []

    # 1. Anatomía Celular con citoesqueleto, membrana cerrada y mitocondria gigante
    svg_parts.append(generar_entorno_completo(ANCHO_CANVAS, ALTO_CANVAS))

    # =========================================================================
    # EJE 1: GLUCÓLISIS Y BYPASS DE GLUCONEOGÉNESIS (EJE CENTRAL-IZQUIERDO)
    # =========================================================================
    X_GLU = 675
    X_FLECHA = 720

    # 1. D-Glucosa
    svg_parts.append(crear_metabolito(
        x=X_GLU, y=145,
        nombre="D-Glucosa",
        carbonos="6 Carbonos (Hexosa)",
        detalle="Entrada al citosol desde el GLUT-4",
        svg_estructura=GLUCOSA
    ))

    # Reacción 1: Hexoquinasa vs G6Pasa
    svg_parts.append(crear_reaccion(
        x=X_FLECHA, y=255,
        enzima="Hexoquinasa",
        ec="EC 2.7.1.1 (Mg²⁺)",
        regulacion="⊣ G-6-P | ⊕ Insulina",
        entra_energia="- 1 ATP",
        sale_energia="+ 1 ADP"
    ))
    svg_parts.append("""
    <g transform="translate(635, 255)">
      <path d="M 0 48 L 0 0" stroke="#0284c7" stroke-width="1.8" stroke-dasharray="5 3" marker-end="url(#arrowBlue)"/>
      <text x="-10" y="24" font-family="'Inter', sans-serif" font-size="9" font-weight="700" fill="#0284c7" text-anchor="end">G-6-Fosfatasa (H₂O→Pi)</text>
    </g>
    """)

    # 2. Glucosa-6-Fosfato (NODO UNIVERSAL)
    svg_parts.append(crear_metabolito(
        x=X_GLU, y=365,
        nombre="Glucosa-6-Fosfato",
        carbonos="6 Carbonos (Hexosa Ⓟ)",
        detalle="Nodo central: Glucólisis • Glucógeno • Pentosas",
        svg_estructura=GLUCOSA_6_FOSFATO
    ))

    # Reacción 2: Fosfoglucosa Isomerasa
    svg_parts.append(crear_reaccion(
        x=X_FLECHA, y=505,
        enzima="Fosfoglucosa Isomerasa",
        ec="EC 5.3.1.9 (⇄)",
        reversible=True
    ))

    # 3. Fructosa-6-Fosfato
    svg_parts.append(crear_metabolito(
        x=X_GLU, y=605,
        nombre="Fructosa-6-Fosfato",
        carbonos="6 Carbonos (Cetosa Ⓟ)",
        detalle="Receptor del retorno de Pentosas Fosfato",
        svg_estructura=FRUCTOSA_6_FOSFATO
    ))

    # Reacción 3: PFK-1 vs FBPasa-1
    svg_parts.append(crear_reaccion(
        x=X_FLECHA, y=750,
        enzima="Fosfofructoquinasa-1 (PFK-1)",
        ec="EC 2.7.1.11 (Compromiso Clave)",
        regulacion="⊣ ATP, Citrato | ⊕ AMP, F-2,6-BP",
        entra_energia="- 1 ATP",
        sale_energia="+ 1 ADP"
    ))
    svg_parts.append("""
    <g transform="translate(635, 750)">
      <path d="M 0 48 L 0 0" stroke="#0284c7" stroke-width="1.8" stroke-dasharray="5 3" marker-end="url(#arrowBlue)"/>
      <text x="-10" y="24" font-family="'Inter', sans-serif" font-size="9" font-weight="700" fill="#0284c7" text-anchor="end">FBPasa-1 (H₂O→Pi)</text>
    </g>
    """)

    # 4. Fructosa-1,6-Bisfosfato
    svg_parts.append(crear_metabolito(
        x=X_GLU, y=850,
        nombre="Fructosa-1,6-Bisfosfato",
        carbonos="6 Carbonos (Hexosa Bis-Ⓟ)",
        detalle="Sustrato de escisión aldólica",
        svg_estructura=FRUCTOSA_1_6_BISFOSFATO
    ))

    # Aldolasa y Triosas
    svg_parts.append(f"""
    <g transform="translate({X_FLECHA}, 970)">
      <path d="M -15 0 Q -100 25 -140 65" fill="none" stroke="#ea580c" stroke-width="2" marker-end="url(#arrowFlow)"/>
      <path d="M 15 0 Q 100 25 150 65" fill="none" stroke="#ea580c" stroke-width="2" marker-end="url(#arrowFlow)"/>
      <g transform="translate(0, 24)">
        <text x="0" y="0" fill="#0f172a" font-size="12" font-weight="800" text-anchor="middle">Aldolasa</text>
        <text x="0" y="13" fill="#64748b" font-size="9.5" font-family="'JetBrains Mono', monospace" text-anchor="middle">EC 4.1.2.13 (⇄)</text>
      </g>
    </g>

    <!-- DHAP (Izquierda) -->
    {crear_metabolito(
        x=450, y=1050,
        nombre="Dihidroxiacetona-P",
        carbonos="3 Carbonos (Cetotriosa)",
        detalle="Precursor de síntesis de TAGs",
        svg_estructura=DIHIDROXIACETONA_FOSFATO,
        texto_izquierda=True
    )}

    <!-- GAP (Derecha) -->
    {crear_metabolito(
        x=890, y=1050,
        nombre="Gliceraldehído-3-P",
        carbonos="3 Carbonos (Aldotriosa)",
        detalle="Continúa hacia el rendimiento",
        svg_estructura=GLICERALDEHIDO_3_FOSFATO
    )}

    <!-- TPI Horizontal -->
    <g transform="translate({X_FLECHA}, 1080)">
      <line x1="-90" y1="-3" x2="80" y2="-3" stroke="#ea580c" stroke-width="1.8" marker-end="url(#arrowFlow)"/>
      <line x1="80" y1="3" x2="-90" y2="3" stroke="#ea580c" stroke-width="1.8" marker-end="url(#arrowFlow)"/>
      <text x="-5" y="-12" fill="#0f172a" font-size="10.5" font-weight="800" text-anchor="middle">Triosa Fosfato Isomerasa (TPI)</text>
      <text x="-5" y="16" fill="#64748b" font-size="9" font-family="'JetBrains Mono', monospace" text-anchor="middle">EC 5.3.1.1 (⇄)</text>
    </g>

    <path d="M 930 1150 Q 930 1185 720 1205" fill="none" stroke="#ea580c" stroke-width="2.2" marker-end="url(#arrowFlow)"/>
    <g transform="translate(720, 1190)">
      <rect x="-95" y="-11" width="190" height="22" rx="11" fill="#ffedd5" stroke="#ea580c" stroke-width="1.8"/>
      <text x="0" y="4" fill="#c2410c" font-size="10.5" font-weight="800" text-anchor="middle">FASE 2: RENDIMIENTO (× 2)</text>
    </g>
    """)

    # Fase 2 Rendimiento
    svg_parts.append(crear_reaccion(
        x=X_FLECHA, y=1225,
        enzima="GAPDH",
        ec="EC 1.2.1.12 (⇄)",
        entra_energia="+ 2 NAD⁺ + 2 Pi",
        sale_energia="+ 2 NADH + 2 H⁺",
        reversible=True,
        es_ganancia=True
    ))

    # 5. 1,3-BPG
    svg_parts.append(crear_metabolito(
        x=X_GLU, y=1320,
        nombre="1,3-Bisfosfoglicerato",
        carbonos="3 Carbonos (Acil-fosfato)",
        detalle="Fosforilación a nivel de sustrato",
        svg_estructura=BISFOSFOGLICERATO_1_3
    ))

    svg_parts.append(crear_reaccion(
        x=X_FLECHA, y=1440,
        enzima="PGK",
        ec="EC 2.7.2.3 (⇄)",
        entra_energia="- 2 ADP",
        sale_energia="+ 2 ATP",
        reversible=True,
        es_ganancia=True
    ))

    # 6. 3-PG
    svg_parts.append(crear_metabolito(
        x=X_GLU, y=1535,
        nombre="3-Fosfoglicerato",
        carbonos="3 Carbonos (Ácido carboxílico Ⓟ)",
        detalle="Intermediario glucolítico",
        svg_estructura=FOSFOGLICERATO_3
    ))

    svg_parts.append(crear_reaccion(
        x=X_FLECHA, y=1655,
        enzima="Fosfogliceromutasa",
        ec="EC 5.4.2.11 (⇄)",
        reversible=True
    ))

    # 7. 2-PG
    svg_parts.append(crear_metabolito(
        x=X_GLU, y=1745,
        nombre="2-Fosfoglicerato",
        carbonos="3 Carbonos (Éster interno)",
        detalle="Sustrato de la enolasa",
        svg_estructura=FOSFOGLICERATO_2
    ))

    svg_parts.append(crear_reaccion(
        x=X_FLECHA, y=1855,
        enzima="Enolasa",
        ec="EC 4.2.1.11 (Mg²⁺, ⇄)",
        salida_agua=True,
        reversible=True
    ))

    # 8. PEP
    svg_parts.append(crear_metabolito(
        x=X_GLU, y=1955,
        nombre="Fosfoenolpiruvato (PEP)",
        carbonos="3 Carbonos (Enol-fosfato)",
        detalle="Compuesto fosforilante de alta energía",
        svg_estructura=FOSFOENOLPIRUVATO
    ))

    svg_parts.append(crear_reaccion(
        x=X_FLECHA, y=2085,
        enzima="Piruvato Quinasa",
        ec="EC 2.7.1.40 (K⁺, Mg²⁺)",
        regulacion="⊣ ATP, Alanina | ⊕ F-1,6-BP",
        entra_energia="- 2 ADP",
        sale_energia="+ 2 ATP",
        es_ganancia=True
    ))
    svg_parts.append("""
    <g transform="translate(635, 2085)">
      <path d="M 0 48 L 0 0" stroke="#0284c7" stroke-width="1.8" stroke-dasharray="5 3" marker-end="url(#arrowBlue)"/>
      <text x="-10" y="24" font-family="'Inter', sans-serif" font-size="9" font-weight="700" fill="#0284c7" text-anchor="end">PEPCK citosol (GTP→GDP+CO₂)</text>
    </g>
    """)

    # 9. Piruvato
    svg_parts.append(crear_metabolito(
        x=X_GLU, y=2185,
        nombre="Piruvato",
        carbonos="3 Carbonos (α-Cetoácido)",
        detalle="Nodo terminal citosólico hacia MPC / LDH",
        svg_estructura=PIRUVATO
    ))

    # Conexión directa hacia el transportador MPC de la gran mitocondria
    svg_parts.append("""
    <path d="M 830 2235 Q 920 2235 740 2225" fill="none" stroke="#ea580c" stroke-width="3" marker-end="url(#arrowFlow)"/>
    """)


    # =========================================================================
    # RUTAS CITOSÓLICAS: GLUCÓGENO, LÍPIDOS, DESTINOS PIRUVATO Y UREA
    # =========================================================================
    # GLUCÓGENO
    svg_parts.append("""
    <g transform="translate(180, 320)">
      <rect x="0" y="0" width="380" height="150" rx="10" fill="#fffbeb" stroke="#f59e0b" stroke-width="1.8" stroke-dasharray="6 4" opacity="0.95"/>
      <text x="15" y="22" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#b45309">METABOLISMO DEL GLUCÓGENO</text>
      
      <g transform="translate(260, 65)">
        <line x1="100" y1="0" x2="30" y2="0" stroke="#ea580c" stroke-width="1.8" marker-end="url(#arrowFlow)"/>
        <line x1="30" y1="6" x2="100" y2="6" stroke="#ea580c" stroke-width="1.8" marker-end="url(#arrowFlow)"/>
        <text x="65" y="-8" font-family="'Inter', sans-serif" font-size="8.5" font-weight="700" fill="#d97706" text-anchor="middle">Fosfoglucomutasa</text>
        <rect x="-25" y="-14" width="50" height="28" rx="5" fill="#ffffff" stroke="#f59e0b" stroke-width="1.5"/>
        <text x="0" y="4" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="800" fill="#0f172a" text-anchor="middle">G-1-P</text>
      </g>

      <g transform="translate(130, 65)">
        <line x1="90" y1="0" x2="30" y2="0" stroke="#ea580c" stroke-width="1.8" marker-end="url(#arrowFlow)"/>
        <text x="60" y="-8" font-family="'Inter', sans-serif" font-size="8" font-weight="700" fill="#d97706" text-anchor="middle">UDP-Glucosa (UTP)</text>
        <circle cx="0" cy="0" r="24" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
        <circle cx="0" cy="0" r="6" fill="#b45309"/>
        <circle cx="-10" cy="-8" r="4" fill="#d97706"/><circle cx="10" cy="-8" r="4" fill="#d97706"/>
        <circle cx="-10" cy="8" r="4" fill="#d97706"/><circle cx="10" cy="8" r="4" fill="#d97706"/>
        <text x="0" y="38" font-family="'Inter', sans-serif" font-size="9.5" font-weight="800" fill="#92400e" text-anchor="middle">GLUCÓGENO (n)</text>
      </g>

      <path d="M 130 90 Q 200 120 260 90" fill="none" stroke="#d97706" stroke-width="1.8" stroke-dasharray="5 3" marker-end="url(#arrowFlow)"/>
      <text x="200" y="125" font-family="'Inter', sans-serif" font-size="8.5" font-weight="700" fill="#b45309" text-anchor="middle">Glucógeno Fosforilasa (+ Pi)</text>
    </g>
    <path d="M 660 395 L 565 395" stroke="#ea580c" stroke-width="2.2" marker-end="url(#arrowFlow)"/>
    """)

    # LÍPIDOS CITOSÓLICOS
    svg_parts.append("""
    <g transform="translate(140, 1020)">
      <rect x="0" y="0" width="280" height="260" rx="10" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.8" stroke-dasharray="6 4" opacity="0.95"/>
      <text x="15" y="22" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#15803d">LÍPIDOS CITOSÓLICOS</text>

      <g transform="translate(140, 70)">
        <rect x="-80" y="-16" width="160" height="32" rx="6" fill="#ffffff" stroke="#16a34a" stroke-width="1.5"/>
        <text x="0" y="4" font-family="'Inter', sans-serif" font-size="10" font-weight="800" fill="#166534" text-anchor="middle">L-Glicerol-3-Fosfato</text>
        <text x="0" y="26" font-family="'Inter', sans-serif" font-size="8" fill="#15803d" text-anchor="middle">Glicerol-3-P DH (NADH→NAD⁺)</text>

        <line x1="0" y1="32" x2="0" y2="60" stroke="#16a34a" stroke-width="2" marker-end="url(#arrowGreen)"/>
        <rect x="-60" y="62" width="120" height="26" rx="6" fill="#dcfce7" stroke="#15803d" stroke-width="1.5"/>
        <text x="0" y="78" font-family="'Inter', sans-serif" font-size="9.5" font-weight="800" fill="#14532d" text-anchor="middle">TRIGLICÉRIDOS (TAG)</text>
      </g>

      <g transform="translate(140, 195)">
        <text x="0" y="-12" font-family="'Inter', sans-serif" font-size="10" font-weight="800" fill="#166534" text-anchor="middle">LIPOGÉNESIS (FAS)</text>
        <rect x="-100" y="-4" width="200" height="26" rx="5" fill="#ffffff" stroke="#16a34a" stroke-width="1.5"/>
        <text x="0" y="13" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="700" fill="#0f172a" text-anchor="middle">Malonil-CoA ➔ Palmitato</text>
        <text x="0" y="36" font-family="'Inter', sans-serif" font-size="8" fill="#15803d" text-anchor="middle">Consume NADPH de Pentosas</text>
      </g>
    </g>

    <path d="M 430 1090 L 320 1090" stroke="#16a34a" stroke-width="2.2" marker-end="url(#arrowGreen)"/>
    <!-- Salida de Citrato desde la gran mitocondria hacia la lipogénesis citosólica -->
    <path d="M 1160 2150 C 1100 1700 450 1400 320 1230" fill="none" stroke="#d97706" stroke-width="2.2" stroke-dasharray="6 4" marker-end="url(#arrowFlow)"/>
    """)

    # DESTINOS PIRUVATO (FERMENTACIÓN Y ALANINA)
    svg_parts.append("""
    <g transform="translate(650, 2235)">
      <line x1="-15" y1="-2" x2="-140" y2="-2" stroke="#ea580c" stroke-width="1.8" marker-end="url(#arrowFlow)"/>
      <line x1="-140" y1="4" x2="-15" y2="4" stroke="#ea580c" stroke-width="1.8" marker-end="url(#arrowFlow)"/>
      <path d="M -50 -10 Q -80 -25 -110 -10" fill="none" stroke="#059669" stroke-width="1.6" marker-end="url(#arrowGreen)"/>
      <text x="-80" y="-28" font-family="'Inter', sans-serif" font-size="8.5" font-weight="700" fill="#059669" text-anchor="middle">NADH + H⁺ ⇄ NAD⁺</text>
      <text x="-80" y="18" font-family="'Inter', sans-serif" font-size="9.5" font-weight="800" fill="#0f172a" text-anchor="middle">LDH</text>
    </g>
    <g transform="translate(370, 2200)">
      <rect x="0" y="0" width="130" height="60" rx="8" fill="#fdf2f8" stroke="#db2777" stroke-width="1.8"/>
      <text x="65" y="24" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#9d174d" text-anchor="middle">L-Lactato</text>
      <text x="65" y="42" font-family="'Inter', sans-serif" font-size="9" fill="#be185d" text-anchor="middle">Destino Anaerobio / Sangre</text>
    </g>

    <g transform="translate(720, 2260)">
      <line x1="0" y1="15" x2="0" y2="55" stroke="#059669" stroke-width="1.8" marker-end="url(#arrowGreen)"/>
      <text x="12" y="38" font-family="'Inter', sans-serif" font-size="9" font-weight="800" fill="#047857">ALT (Glutamato ⇄ α-KG)</text>
      <rect x="-60" y="60" width="120" height="28" rx="6" fill="#ecfdf5" stroke="#059669" stroke-width="1.5"/>
      <text x="0" y="78" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#065f46" text-anchor="middle">L-Alanina</text>
    </g>
    """)


    # =========================================================================
    # EJE 2: VÍA DE LAS PENTOSAS FOSFATO (DERECHA)
    # =========================================================================
    svg_parts.append("""
    <path d="M 830 395 Q 1150 365 1370 395" fill="none" stroke="#7c3aed" stroke-width="2.5" marker-end="url(#arrowPurple)"/>
    <g transform="translate(1100, 355)">
      <rect x="-85" y="-12" width="170" height="24" rx="12" fill="#f5f3ff" stroke="#7c3aed" stroke-width="1.8"/>
      <text x="0" y="4" fill="#6d28d9" font-size="10" font-weight="800" text-anchor="middle">ENTRADA AL SHUNT DE PENTOSAS</text>
    </g>
    """)

    # G6PDH
    svg_parts.append(f"""
    <g transform="translate(1250, 395)">
      <path d="M -30 -15 Q -10 -25 10 -15" fill="none" stroke="#475569" stroke-width="1.8" marker-end="url(#arrowSlate)"/>
      <text x="-25" y="-30" font-family="'Inter', sans-serif" font-size="9" font-weight="700" fill="#475569">+ NADP⁺</text>
      <path d="M -30 15 Q -10 25 10 15" fill="none" stroke="#059669" stroke-width="1.8" marker-end="url(#arrowGreen)"/>
      <text x="-25" y="32" font-family="'Inter', sans-serif" font-size="9" font-weight="800" fill="#059669">+ NADPH + H⁺</text>
      <text x="0" y="-8" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#0f172a" text-anchor="middle">G6PDH</text>
      <text x="0" y="7" font-family="'JetBrains Mono', monospace" font-size="9" fill="#64748b" text-anchor="middle">EC 1.1.1.49</text>
    </g>
    """)

    # 1. 6-Fosfoglucono-δ-Lactona
    svg_parts.append(crear_metabolito(
        x=1400, y=365,
        nombre="6-Fosfoglucono-δ-Lactona",
        carbonos="6 Carbonos (Lactona)",
        detalle="Éster intramolecular hidrolizable",
        svg_estructura=FOSFOGLUCONO_LACTONA_6
    ))

    # Lactonasa
    svg_parts.append("""
    <g transform="translate(1660, 415)">
      <line x1="0" y1="0" x2="60" y2="0" stroke="#ea580c" stroke-width="2.5" marker-end="url(#arrowFlow)"/>
      <path d="M 10 -15 Q 30 -25 50 -15" fill="none" stroke="#0284c7" stroke-width="1.8" marker-end="url(#arrowBlue)"/>
      <text x="30" y="-30" font-family="'Inter', sans-serif" font-size="9" font-weight="700" fill="#0284c7" text-anchor="middle">+ H₂O</text>
      <text x="30" y="16" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#0f172a" text-anchor="middle">6-P-Gluconolactonasa</text>
      <text x="30" y="28" font-family="'JetBrains Mono', monospace" font-size="9" fill="#64748b" text-anchor="middle">EC 3.1.1.31</text>
    </g>
    """)

    # 2. 6-Fosfogluconato
    svg_parts.append(crear_metabolito(
        x=1770, y=365,
        nombre="6-Fosfogluconato",
        carbonos="6 Carbonos (Cadena lineal)",
        detalle="Ácido descarboxilable generador de NADPH",
        svg_estructura=FOSFOGLUCONATO_6
    ))

    # 6-PGDH
    svg_parts.append(crear_reaccion_oxidativa(
        x=1900, y=530,
        enzima="6-Fosfogluconato Deshidrogenasa",
        ec="EC 1.1.1.44 (Descarboxilación)",
        genera_nadph=True,
        salida_co2=True,
        altura=54
    ))

    # 3. Ribulosa-5-P
    svg_parts.append(crear_metabolito(
        x=1770, y=620,
        nombre="D-Ribulosa-5-Fosfato",
        carbonos="5 Carbonos (Pentosa Cetosa)",
        detalle="Cruce a la fase no oxidativa",
        svg_estructura=RIBULOSA_5_FOSFATO
    ))

    # Ramificación X5P y R5P
    svg_parts.append("""
    <g transform="translate(1900, 775)">
      <path d="M -20 0 Q -110 30 -160 70" fill="none" stroke="#ea580c" stroke-width="2" marker-end="url(#arrowFlow)"/>
      <g transform="translate(-175, 25)">
        <text x="0" y="0" fill="#0f172a" font-size="11" font-weight="800" text-anchor="end">Fosfopentosa Epimerasa</text>
        <text x="0" y="13" fill="#64748b" font-size="9" font-family="'JetBrains Mono', monospace" text-anchor="end">EC 5.1.3.1 (⇄)</text>
      </g>
      <path d="M 20 0 Q 110 30 180 70" fill="none" stroke="#ea580c" stroke-width="2" marker-end="url(#arrowFlow)"/>
      <g transform="translate(175, 25)">
        <text x="0" y="0" fill="#0f172a" font-size="11" font-weight="800">Fosfopentosa Isomerasa</text>
        <text x="0" y="13" fill="#64748b" font-size="9" font-family="'JetBrains Mono', monospace">EC 5.3.1.6 (⇄)</text>
      </g>
    </g>
    """)

    # 4a. Xilulosa-5-P
    svg_parts.append(crear_metabolito(
        x=1500, y=855,
        nombre="D-Xilulosa-5-P",
        carbonos="5 Carbonos (Epímero C3)",
        detalle="Donador de 2C (TPP)",
        svg_estructura=XILULOSA_5_FOSFATO,
        texto_izquierda=True
    ))

    # 4b. Ribosa-5-P
    svg_parts.append(crear_metabolito(
        x=2050, y=855,
        nombre="D-Ribosa-5-P",
        carbonos="5 Carbonos (Pentosa Aldosa)",
        detalle="Precursora de Nucleótidos",
        svg_estructura=RIBOSA_5_FOSFATO
    ))

    # SÍNTESIS DE NUCLEÓTIDOS
    svg_parts.append("""
    <g transform="translate(2100, 990)">
      <line x1="0" y1="0" x2="0" y2="40" stroke="#7c3aed" stroke-width="2.5" marker-end="url(#arrowPurple)"/>
      <text x="12" y="24" font-family="'Inter', sans-serif" font-size="9" font-weight="800" fill="#7c3aed">PRPP Sintetasa (ATP→AMP)</text>

      <g transform="translate(0, 48)">
        <rect x="-100" y="0" width="200" height="75" rx="8" fill="#f5f3ff" stroke="#7c3aed" stroke-width="1.8"/>
        <text x="0" y="18" fill="#6d28d9" font-size="11" font-weight="900" text-anchor="middle">SÍNTESIS DE NUCLEÓTIDOS</text>
        <text x="0" y="34" fill="#7c3aed" font-size="9.5" font-weight="700" text-anchor="middle">PRPP ➔ Purinas (IMP, AMP, GMP)</text>
        <text x="0" y="49" fill="#7c3aed" font-size="9.5" font-weight="700" text-anchor="middle">PRPP ➔ Pirimidinas (UMP, CTP, TMP)</text>
        <text x="0" y="64" fill="#94a3b8" font-size="8.5" text-anchor="middle">Precursores de ARN / ADN en citosol</text>
      </g>
    </g>
    """)

    # FASE NO OXIDATIVA DE PENTOSAS: TK1, TA, TK2
    svg_parts.append(crear_paso_no_oxidativo(
        x=1820, y=1045,
        enzima="Transcetolasa (TK1)",
        ec="EC 2.2.1.1 (Cofactor: TPP, Mg²⁺)",
        sustratos_txt="Xilulosa-5-P (5C) + Ribosa-5-P (5C)",
        productos_txt="GAP (3C) + Sedoheptulosa-7-P (7C)"
    ))

    # Sedoheptulosa-7-P
    svg_parts.append(crear_metabolito(
        x=1500, y=1125,
        nombre="Sedoheptulosa-7-P",
        carbonos="7 Carbonos (Cetosa)",
        detalle="Intermediario de 7C",
        svg_estructura=SEDOHEPTULOSA_7_FOSFATO,
        texto_izquierda=True
    ))

    # GAP intermediario
    svg_parts.append(crear_metabolito(
        x=2050, y=1125,
        nombre="Gliceraldehído-3-P",
        carbonos="3 Carbonos (Triosa)",
        detalle="Intermediario transferible",
        svg_estructura=GLICERALDEHIDO_3_FOSFATO
    ))

    # TA
    svg_parts.append(crear_paso_no_oxidativo(
        x=1820, y=1275,
        enzima="Transaldolasa (TA)",
        ec="EC 2.2.1.2 (Base de Schiff con Lisina)",
        sustratos_txt="Sedoheptulosa-7-P (7C) + GAP (3C)",
        productos_txt="Fructosa-6-P (6C) + Eritrosa-4-P (4C)"
    ))

    # Eritrosa-4-P
    svg_parts.append(crear_metabolito(
        x=1500, y=1355,
        nombre="D-Eritrosa-4-P",
        carbonos="4 Carbonos (Tetrosa)",
        detalle="Aceptor para segunda transcetolasa",
        svg_estructura=ERITROSA_4_FOSFATO,
        texto_izquierda=True
    ))

    # F6P (1er reingreso)
    svg_parts.append(crear_metabolito(
        x=2050, y=1355,
        nombre="Fructosa-6-Fosfato",
        carbonos="6 Carbonos (Hexosa)",
        detalle="¡1.er Reingreso a la Glucólisis!",
        svg_estructura=FRUCTOSA_6_FOSFATO
    ))

    # TK2
    svg_parts.append(crear_paso_no_oxidativo(
        x=1820, y=1505,
        enzima="Transcetolasa (TK2)",
        ec="EC 2.2.1.1 (Cofactor: TPP, Mg²⁺)",
        sustratos_txt="Xilulosa-5-P (5C) + Eritrosa-4-P (4C)",
        productos_txt="Fructosa-6-P (6C) + GAP (3C)"
    ))

    # F6P (2º reingreso)
    svg_parts.append(crear_metabolito(
        x=1500, y=1585,
        nombre="Fructosa-6-Fosfato",
        carbonos="6 Carbonos (Hexosa)",
        detalle="¡2.º Reingreso a la Glucólisis!",
        svg_estructura=FRUCTOSA_6_FOSFATO,
        texto_izquierda=True
    ))

    # GAP (2º reingreso)
    svg_parts.append(crear_metabolito(
        x=2050, y=1585,
        nombre="Gliceraldehído-3-P",
        carbonos="3 Carbonos (Triosa)",
        detalle="¡Reingreso de triosa a la Glucólisis!",
        svg_estructura=GLICERALDEHIDO_3_FOSFATO
    ))

    # RETORNOS A LA GLUCÓLISIS
    svg_parts.append("""
    <path d="M 2040 1395 C 1650 1320 1200 950 830 635" fill="none" stroke="#059669" stroke-width="2.5" stroke-dasharray="8 5" marker-end="url(#arrowGreen)"/>
    <g transform="translate(1320, 900)">
      <rect x="-85" y="-11" width="170" height="22" rx="11" fill="#ecfdf5" stroke="#059669" stroke-width="1.6"/>
      <text x="0" y="4" fill="#047857" font-size="10" font-weight="800" text-anchor="middle">RETORNO: F-6-P A GLUCÓLISIS</text>
    </g>

    <path d="M 2040 1620 C 1650 1560 1200 1320 1010 1095" fill="none" stroke="#059669" stroke-width="2.5" stroke-dasharray="8 5" marker-end="url(#arrowGreen)"/>
    <g transform="translate(1480, 1420)">
      <rect x="-85" y="-11" width="170" height="22" rx="11" fill="#ecfdf5" stroke="#059669" stroke-width="1.6"/>
      <text x="0" y="4" fill="#047857" font-size="10" font-weight="800" text-anchor="middle">RETORNO: GAP A GLUCÓLISIS</text>
    </g>
    """)

    # CICLO DE LA UREA (CITOSOL)
    svg_parts.append("""
    <g transform="translate(1980, 1850)">
      <rect x="0" y="0" width="380" height="240" rx="10" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8" stroke-dasharray="6 4" opacity="0.95"/>
      <text x="15" y="22" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#1d4ed8">CICLO DE LA UREA (CITOSOL)</text>

      <g transform="translate(60, 60)">
        <rect x="-40" y="-14" width="80" height="28" rx="5" fill="#ffffff" stroke="#3b82f6" stroke-width="1.5"/>
        <text x="0" y="4" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="800" fill="#1e40af" text-anchor="middle">Citrulina</text>
        <text x="0" y="24" font-family="'Inter', sans-serif" font-size="8" fill="#60a5fa" text-anchor="middle">(Sale de matriz)</text>
      </g>

      <path d="M 110 60 L 190 60" stroke="#3b82f6" stroke-width="2" marker-end="url(#arrowBlue)"/>
      <text x="150" y="52" font-family="'Inter', sans-serif" font-size="8" font-weight="700" fill="#1d4ed8" text-anchor="middle">+ Aspartato / ATP</text>

      <g transform="translate(250, 60)">
        <rect x="-50" y="-14" width="100" height="28" rx="5" fill="#ffffff" stroke="#3b82f6" stroke-width="1.5"/>
        <text x="0" y="4" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="800" fill="#1e40af" text-anchor="middle">Argininosuccinato</text>
      </g>

      <path d="M 250 80 L 250 125" stroke="#3b82f6" stroke-width="2" marker-end="url(#arrowBlue)"/>
      <text x="260" y="105" font-family="'Inter', sans-serif" font-size="8" font-weight="700" fill="#1d4ed8">— Fumarato</text>

      <g transform="translate(250, 145)">
        <rect x="-40" y="-14" width="80" height="28" rx="5" fill="#ffffff" stroke="#3b82f6" stroke-width="1.5"/>
        <text x="0" y="4" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="800" fill="#1e40af" text-anchor="middle">L-Arginina</text>
      </g>

      <path d="M 200 145 L 120 145" stroke="#3b82f6" stroke-width="2" marker-end="url(#arrowBlue)"/>
      <text x="160" y="137" font-family="'Inter', sans-serif" font-size="8" font-weight="800" fill="#2563eb" text-anchor="middle">Arginasa (+ H₂O)</text>

      <g transform="translate(70, 145)">
        <rect x="-45" y="-16" width="90" height="32" rx="6" fill="#dbeafe" stroke="#1d4ed8" stroke-width="2"/>
        <text x="0" y="4" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="900" fill="#1e3a8a" text-anchor="middle">UREA</text>
        <text x="0" y="28" font-family="'Inter', sans-serif" font-size="8" font-weight="800" fill="#2563eb" text-anchor="middle">Excreción renal</text>
      </g>

      <path d="M 70 170 Q 70 210 20 230" fill="none" stroke="#3b82f6" stroke-width="1.8" stroke-dasharray="5 3" marker-end="url(#arrowBlue)"/>
      <text x="60" y="210" font-family="'Inter', sans-serif" font-size="8" font-weight="700" fill="#1d4ed8">Ornitina (a matriz)</text>
    </g>

    <!-- Conexión entre transportador ORNT de la gran mitocondria y el ciclo citosólico -->
    <path d="M 1980 2210 L 2040 2100" stroke="#059669" stroke-width="2.2" stroke-dasharray="5 3" marker-end="url(#arrowGreen)"/>
    """)

    # Ensamblar SVG
    svg_final = "\n".join(svg_parts)

    html_template = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>El Citosol Celular y Gran Matriz Mitocondrial</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&family=JetBrains+Mono:wght@600;700;800&display=swap" rel="stylesheet">
  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: 'Inter', sans-serif;
      background: #cbd5e1;
      color: #0f172a;
      padding: 20px;
      display: flex;
      flex-direction: column;
      align-items: center;
    }}
    .lienzo-svg {{
      width: 100%;
      max-width: {ANCHO_CANVAS}px;
      background: #e2e8f0;
      border: 1px solid #94a3b8;
      border-radius: 12px;
      box-shadow: 0 20px 50px rgba(0, 0, 0, 0.15);
      overflow: hidden;
    }}
    svg {{
      display: block;
      width: 100%;
      height: auto;
    }}
  </style>
</head>
<body>
  <div class="lienzo-svg">
    <svg width="{ANCHO_CANVAS}" height="{ALTO_CANVAS}" viewBox="0 0 {ANCHO_CANVAS} {ALTO_CANVAS}" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <!-- Marcadores de flechas estandarizados -->
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
        <marker id="arrowPurple" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
          <path d="M 0 0 L 6 3 L 0 6 Z" fill="#7c3aed" />
        </marker>

        <!-- Gradiente biológico acuoso del citosol -->
        <linearGradient id="gradCitosolCelular" x1="0%" y1="0%" x2="0%" y2="100%">
          <stop offset="0%" stop-color="#ffffff" stop-opacity="1" />
          <stop offset="10%" stop-color="#f8fafc" stop-opacity="0.8" />
          <stop offset="50%" stop-color="#f0fdf4" stop-opacity="0.4" />
          <stop offset="85%" stop-color="#f8fafc" stop-opacity="0.8" />
          <stop offset="100%" stop-color="#ffffff" stop-opacity="1" />
        </linearGradient>
      </defs>

      {svg_final}
    </svg>
  </div>
</body>
</html>
"""
    return html_template

if __name__ == "__main__":
    ruta_salida = os.path.join(os.path.dirname(__file__), "citosol_completo.html")
    with open(ruta_salida, "w", encoding="utf-8") as f:
        f.write(generar_html_mapa_celular())
    print(f"✅ Mapa Celular Completo generado con éxito en: {ruta_salida}")
