#!/usr/bin/env python3
"""
GENERADOR DE LA RUTA DE LA GLUCOGÉNESIS (SÍNTESIS DE GLUCÓGENO)
===============================================================
Ruta completa con rigor editorial biológico y zoom mecanístico:
1. Conector biológico: G-6-P desde la Glucólisis.
2. Reacción 1: Fosfoglucomutasa (G-6-P ⇄ G-1-P) con cofactor G-1,6-BP.
3. Reacción 2: UDP-Glucosa Pirofosforilasa (G-1-P + UTP ➔ UDP-Glucosa + PPi)
   acoplada a la Pirofosfatasa Inorgánica (PPi + H2O ➔ 2 Pi).
4. El Cebador Molecular Real: Glucogenina dímero con residuo Tyr-194 y cadena
   (Glucosa)₈ con extremo 4-OH aceptor libre.
5. LUPA DE ZOOM MOLECULAR: Acoplamiento activo entre el extremo 4-OH del cebador
   y el bolsillo catalítico de la Glucógeno Sintasa, ataque Sn2 y salida de UDP.
6. Reacción 3: Glucógeno Sintasa (Elongación de cadenas α-1,4).
7. Reacción 4: Enzima Ramificadora del Glucógeno (Amilo-α(1,4→1,6)-transglucosidasa).
8. Polímero de Glucógeno ramificado con enlaces α(1→4) y α(1→6).
9. El Gránulo Citosólico de Inclusión: Por qué se almacena como orgánulo no
   membranoso insoluble en el citosol y cómo sale únicamente como glucosa libre.
10. Balance energético compacto.
"""

import os
from estructuras_glucogeno import (
    GLUCOSA_6_FOSFATO,
    GLUCOSA_1_FOSFATO,
    UDP_GLUCOSA,
    CEBADOR_GLUCOGENINA,
    LUPA_MECANISMO_CEBADOR,
    CADENA_GLUCOGENO,
    GRANULO_CITOSOLICO_INCLUSION
)

ANCHO = 1000
ALTO = 2450

CABECERA_HTML = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ruta de la Glucogénesis - Síntesis de Glucógeno en Citosol</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&family=JetBrains+Mono:wght@600;700;800&display=swap" rel="stylesheet">
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
      width: 1000px;
      background: #ffffff;
      border: 1px solid #cbd5e1;
      border-radius: 8px;
      box-shadow: 0 15px 35px rgba(0, 0, 0, 0.12);
      overflow: hidden;
    }}
    svg {{ display: block; width: 100%; height: auto; }}
  </style>
</head>
<body>
  <div class="lienzo-svg">
    <svg width="{ANCHO}" height="{ALTO}" viewBox="0 0 {ANCHO} {ALTO}" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <!-- Marcadores de flujo -->
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

        <!-- Gradiente Citosólico Biológico -->
        <linearGradient id="gradCitosolGlucogeno" x1="0%" y1="0%" x2="0%" y2="100%">
          <stop offset="0%" stop-color="#ffffff" stop-opacity="1" />
          <stop offset="15%" stop-color="#f8fafc" stop-opacity="0.8" />
          <stop offset="50%" stop-color="#fffbeb" stop-opacity="0.35" />
          <stop offset="85%" stop-color="#f8fafc" stop-opacity="0.8" />
          <stop offset="100%" stop-color="#ffffff" stop-opacity="1" />
        </linearGradient>
      </defs>
"""

PIE_HTML = """
    </svg>
  </div>
</body>
</html>
"""

def generar_entorno_celular_glucogeno():
    """Genera la ambientación celular: citoesqueleto, ribosomas, vesículas y membrana."""
    return f"""
    <!-- Fondo acuoso del citosol -->
    <rect x="0" y="0" width="{ANCHO}" height="{ALTO}" fill="url(#gradCitosolGlucogeno)"/>

    <!-- Membrana plasmática biológica (borde superior) -->
    <g opacity="0.85">
      <path d="M 0 60 Q 250 45 500 55 T 1000 50" fill="none" stroke="#0284c7" stroke-width="6"/>
      <path d="M 0 68 Q 250 53 500 63 T 1000 58" fill="none" stroke="#38bdf8" stroke-width="2.5" stroke-dasharray="6 4"/>
      <g fill="#0284c7" opacity="0.6">
        <circle cx="80" cy="56" r="2.5"/><circle cx="95" cy="57" r="2.5"/><circle cx="110" cy="58" r="2.5"/>
        <circle cx="450" cy="54" r="2.5"/><circle cx="465" cy="55" r="2.5"/><circle cx="480" cy="56" r="2.5"/>
        <circle cx="820" cy="51" r="2.5"/><circle cx="835" cy="52" r="2.5"/><circle cx="850" cy="53" r="2.5"/>
      </g>
    </g>

    <!-- Filamentos de Citoesqueleto que cruzan el citoplasma -->
    <g opacity="0.32" stroke="#94a3b8" fill="none">
      <path d="M 40 180 Q 300 120 600 190 T 960 160" stroke-width="1.5" stroke-dasharray="8 6"/>
      <path d="M 50 480 Q 350 540 650 490 T 950 510" stroke-width="1.5" stroke-dasharray="7 7"/>
      <path d="M 40 920 Q 280 860 620 930 T 960 890" stroke-width="1.6" stroke-dasharray="8 5"/>
      <path d="M 60 1480 Q 340 1540 680 1490 T 950 1510" stroke-width="1.5" stroke-dasharray="8 6"/>
      <path d="M 50 1980 Q 350 1920 650 1990 T 960 1950" stroke-width="1.6" stroke-dasharray="6 6"/>
    </g>

    <!-- Polirribosomas flotando en el citosol -->
    <g fill="#94a3b8" opacity="0.25">
      <circle cx="140" cy="140" r="2.5"/><circle cx="146" cy="142" r="2"/><circle cx="144" cy="148" r="2.3"/>
      <circle cx="820" cy="220" r="2.5"/><circle cx="826" cy="222" r="2"/><circle cx="824" cy="228" r="2.3"/>
      <circle cx="150" cy="720" r="2.5"/><circle cx="156" cy="722" r="2"/><circle cx="154" cy="728" r="2.3"/>
      <circle cx="880" cy="1250" r="2.5"/><circle cx="886" cy="1252" r="2"/><circle cx="884" cy="1258" r="2.3"/>
      <circle cx="140" cy="1820" r="2.5"/><circle cx="146" cy="1822" r="2"/><circle cx="144" cy="1828" r="2.3"/>
    </g>

    <!-- Vesículas citosólicas translúcidas -->
    <g opacity="0.28">
      <circle cx="180" cy="380" r="22" fill="#e0f2fe" stroke="#38bdf8" stroke-width="1.8" stroke-dasharray="4 2"/>
      <circle cx="180" cy="380" r="16" fill="none" stroke="#7dd3fc" stroke-width="1"/>
      <circle cx="850" cy="820" r="24" fill="#fef3c7" stroke="#f59e0b" stroke-width="1.8" stroke-dasharray="4 2"/>
      <circle cx="850" cy="820" r="17" fill="none" stroke="#fbbf24" stroke-width="1"/>
      <circle cx="160" cy="1350" r="26" fill="#e0f2fe" stroke="#38bdf8" stroke-width="1.8" stroke-dasharray="4 2"/>
      <circle cx="160" cy="1350" r="19" fill="none" stroke="#7dd3fc" stroke-width="1"/>
    </g>
    """

def crear_metabolito(x, y, nombre, carbonos, detalle="", svg_estructura="", texto_izquierda=False, dx_texto=135):
    """Bloque SVG de metabolito con desplazamiento de texto ajustable."""
    if texto_izquierda:
        pos_estructura = f"translate({dx_texto}, 0)"
        pos_texto = f"translate({dx_texto - 20}, 25)"
        alineacion = 'text-anchor="end"'
    else:
        pos_estructura = "translate(0, 0)"
        pos_texto = f"translate({dx_texto}, 25)"
        alineacion = ''

    return f"""
    <!-- Metabolito: {nombre} -->
    <g transform="translate({x}, {y})">
      <g transform="{pos_estructura}">
        {svg_estructura}
      </g>
      <g transform="{pos_texto}">
        <text x="0" y="0" fill="#0f172a" font-size="16" font-weight="800" {alineacion}>{nombre}</text>
        <text x="0" y="18" fill="#ea580c" font-size="12" font-weight="700" {alineacion}>{carbonos}</text>
        <text x="0" y="34" fill="#64748b" font-size="11" {alineacion}>{detalle}</text>
      </g>
    </g>
    """

def main():
    contenido_svg = []

    # 1. Capa de entorno biológico
    contenido_svg.append(generar_entorno_celular_glucogeno())

    # =========================================================================
    # CONECTOR BIOLÓGICO DESDE LA GLUCÓLISIS (G-6-P)
    # =========================================================================
    contenido_svg.append("""
    <g transform="translate(480, 85)">
      <path d="M 380 0 L 120 0" fill="none" stroke="#ea580c" stroke-width="2.5" marker-end="url(#arrowFlow)"/>
      <rect x="135" y="-14" width="230" height="26" rx="13" fill="#ffedd5" stroke="#ea580c" stroke-width="1.8"/>
      <text x="250" y="3" fill="#c2410c" font-size="10.5" font-weight="800" text-anchor="middle">
        PROVIENE DE LA GLUCÓLISIS (G-6-P)
      </text>
    </g>
    """)

    # =========================================================================
    # 1. GLUCOSA-6-FOSFATO (G6P)
    # =========================================================================
    Y_G6P = 140
    contenido_svg.append(crear_metabolito(
        x=340, y=Y_G6P,
        nombre="Glucosa-6-Fosfato",
        carbonos="6 Carbonos (Hexosa Ⓟ)",
        detalle="Sustrato inicial desviado al almacén",
        svg_estructura=GLUCOSA_6_FOSFATO
    ))

    # =========================================================================
    # REACCIÓN 1: FOSFOGLUCOMUTASA (G-6-P ⇄ G-1-P)
    # =========================================================================
    contenido_svg.append("""
    <!-- Reacción: Fosfoglucomutasa -->
    <g transform="translate(385, 275)">
      <line x1="-3" y1="0" x2="-3" y2="52" stroke="#ea580c" stroke-width="1.8" marker-end="url(#arrowFlow)"/>
      <line x1="3" y1="52" x2="3" y2="0" stroke="#ea580c" stroke-width="1.8" marker-end="url(#arrowFlow)"/>
      
      <path d="M -65 10 Q -25 10 -4 20" fill="none" stroke="#475569" stroke-width="1.8" marker-end="url(#arrowSlate)"/>
      <text x="-70" y="13" fill="#475569" font-size="10" font-weight="800" text-anchor="end">Ser-OH Fosforilada</text>
      <path d="M -4 30 Q -25 42 -65 42" fill="none" stroke="#475569" stroke-width="1.8" marker-end="url(#arrowSlate)"/>
      <text x="-70" y="45" fill="#475569" font-size="9.5" font-weight="700" text-anchor="end">(Interm. G-1,6-BP)</text>

      <g transform="translate(20, 14)">
        <text x="0" y="0" fill="#0f172a" font-size="13" font-weight="800">Fosfoglucomutasa</text>
        <text x="0" y="14" fill="#64748b" font-size="10.5" font-family="'JetBrains Mono', monospace">EC 5.4.2.2 (Mg²⁺, Reversible ⇄)</text>
        <text x="0" y="28" fill="#d97706" font-size="9.5" font-weight="700">Mecanismo: Transferencia intramolecular de Ⓟ</text>
      </g>
    </g>
    """)

    # =========================================================================
    # 2. α-D-GLUCOSA-1-FOSFATO (G-1-P)
    # =========================================================================
    Y_G1P = 385
    contenido_svg.append(crear_metabolito(
        x=340, y=Y_G1P,
        nombre="α-D-Glucosa-1-Fosfato",
        carbonos="6 Carbonos (Fosfato en C1-α)",
        detalle="Fosfato activo en carbono anomérico",
        svg_estructura=GLUCOSA_1_FOSFATO,
        dx_texto=180
    ))

    # =========================================================================
    # REACCIÓN 2: UDP-GLUCOSA PIROFOSFORILASA + PIROFOSFATASA INORGÁNICA
    # =========================================================================
    contenido_svg.append("""
    <!-- Reacción: UDP-Glucosa Pirofosforilasa -->
    <g transform="translate(385, 545)">
      <line x1="0" y1="0" x2="0" y2="70" stroke="#ea580c" stroke-width="2.5" marker-end="url(#arrowFlow)"/>

      <path d="M -75 12 Q -25 12 -4 24" fill="none" stroke="#dc2626" stroke-width="1.8" marker-end="url(#arrowRed)"/>
      <text x="-80" y="15" fill="#dc2626" font-size="11" font-weight="800" text-anchor="end">- 1 UTP</text>

      <path d="M -4 36 Q -25 48 -75 48" fill="none" stroke="#475569" stroke-width="1.8" marker-end="url(#arrowSlate)"/>
      <text x="-80" y="52" fill="#475569" font-size="10.5" font-weight="800" text-anchor="end">+ PPᵢ (Pirofosfato)</text>

      <path d="M -80 60 Q -110 75 -130 65" fill="none" stroke="#059669" stroke-width="1.8" marker-end="url(#arrowGreen)"/>
      <g transform="translate(-85, 78)">
        <text x="0" y="0" fill="#059669" font-size="9.5" font-weight="800" text-anchor="end">PPᵢ + H₂O ➔ 2 Pᵢ</text>
        <text x="0" y="12" fill="#047857" font-size="8.5" font-weight="700" text-anchor="end">ΔG'° = -19.2 kJ/mol (Irreversible)</text>
      </g>

      <g transform="translate(20, 20)">
        <text x="0" y="0" fill="#0f172a" font-size="13" font-weight="800">UDP-Glucosa Pirofosforilasa</text>
        <text x="0" y="14" fill="#64748b" font-size="10.5" font-family="'JetBrains Mono', monospace">EC 2.7.7.9 (Mg²⁺)</text>
        <text x="0" y="28" fill="#16a34a" font-size="9.5" font-weight="700">⊕ Impulsada por hidrólisis de PPᵢ</text>
      </g>
    </g>
    """)

    # =========================================================================
    # 3. UDP-GLUCOSA (TEXTO TOTALMENTE DESPEJADO A LA DERECHA)
    # =========================================================================
    Y_UDPG = 690
    contenido_svg.append(crear_metabolito(
        x=220, y=Y_UDPG,
        nombre="UDP-Glucosa",
        carbonos="Nucleótido-Azúcar activado",
        detalle="Donador de glucosa de alta energía libre",
        svg_estructura=UDP_GLUCOSA,
        dx_texto=280
    ))

    # =========================================================================
    # 4. EL CEBADOR MOLECULAR REAL (GLUCOGENINA) + LUPA DE ZOOM MOLECULAR
    # =========================================================================
    Y_CEBADOR = 860

    contenido_svg.append(f"""
    <!-- CEBADOR MOLECULAR DE GLUCOGENINA -->
    <g transform="translate(140, {Y_CEBADOR})">
      {CEBADOR_GLUCOGENINA}
      
      <!-- Textos del cebador a la derecha -->
      <g transform="translate(370, 25)">
        <text x="0" y="0" fill="#0f172a" font-size="15" font-weight="900">Cebador: Glucogenina-(Glc)₈</text>
        <text x="0" y="18" fill="#b45309" font-size="11.5" font-weight="700">Dímero autoglucosilante (EC 2.4.1.186)</text>
        <text x="0" y="34" fill="#64748b" font-size="10.5">• Anclaje covalente en residuo Tyr-194</text>
        <text x="0" y="48" fill="#dc2626" font-size="10.5" font-weight="800">• Extremo 4-OH libre: Sustrato aceptor</text>
        <text x="0" y="63" fill="#64748b" font-size="10">Requerido: Glucógeno Sintasa no inicia de novo</text>
      </g>
    </g>

    <!-- LÍNEAS DE PROYECCIÓN CÓNICA HACIA LA LUPA DE ZOOM MOLECULAR -->
    <g stroke="#ea580c" stroke-width="1.4" stroke-dasharray="4 3" opacity="0.65">
      <line x1="435" y1="{Y_CEBADOR + 35}" x2="255" y2="{Y_CEBADOR + 180}"/>
      <line x1="435" y1="{Y_CEBADOR + 15}" x2="160" y2="{Y_CEBADOR + 140}"/>
    </g>

    <!-- LUPA DE ZOOM MOLECULAR: ACOPLAMIENTO CATALÍTICO CEBADOR + SINTASA -->
    <g transform="translate(180, {Y_CEBADOR + 210})">
      {LUPA_MECANISMO_CEBADOR}
    </g>

    <!-- EXPLICACIÓN BIOQUÍMICA A LA DERECHA DE LA LUPA -->
    <g transform="translate(340, {Y_CEBADOR + 175})">
      <rect x="0" y="0" width="460" height="95" rx="8" fill="#f8fafc" stroke="#3b82f6" stroke-width="1.5"/>
      <text x="16" y="22" fill="#1d4ed8" font-size="12" font-weight="900">MECANISMO DE ACOPLAMIENTO Y ELONGACIÓN</text>
      <text x="16" y="40" fill="#0f172a" font-size="10.5" font-weight="600">
        1. La <tspan font-weight="800" fill="#2563eb">Glucógeno Sintasa</tspan> abraza el extremo <tspan font-weight="800" fill="#dc2626">4-OH</tspan> de la cadena cebadora.
      </text>
      <text x="16" y="58" fill="#0f172a" font-size="10.5" font-weight="600">
        2. El oxígeno ataca al <tspan font-weight="800" fill="#ea580c">C1</tspan> de la <tspan font-weight="800">UDP-Glucosa</tspan>, expulsando al grupo UDP.
      </text>
      <text x="16" y="76" fill="#059669" font-size="10.5" font-weight="800">
        3. Se forma el nuevo enlace α(1→4) y la cadena se alarga un residuo a la vez.
      </text>
    </g>
    """)

    # =========================================================================
    # REACCIÓN 3: GLUCÓGENO SINTASA (ELONGACIÓN LINEAL α-1,4)
    # =========================================================================
    Y_RX_SINTASA = Y_CEBADOR + 335

    contenido_svg.append(f"""
    <!-- Reacción: Glucógeno Sintasa -->
    <g transform="translate(385, {Y_RX_SINTASA})">
      <line x1="0" y1="0" x2="0" y2="65" stroke="#ea580c" stroke-width="2.5" marker-end="url(#arrowFlow)"/>

      <path d="M -4 30 Q -25 42 -75 42" fill="none" stroke="#0284c7" stroke-width="1.8" marker-end="url(#arrowBlue)"/>
      <text x="-80" y="45" fill="#0284c7" font-size="11" font-weight="800" text-anchor="end">+ UDP libre</text>
      <text x="-80" y="58" fill="#64748b" font-size="9" text-anchor="end">(UDP + ATP ⇄ UTP + ADP)</text>

      <g transform="translate(20, 16)">
        <text x="0" y="0" fill="#0f172a" font-size="13" font-weight="800">Glucógeno Sintasa</text>
        <text x="0" y="14" fill="#64748b" font-size="10.5" font-family="'JetBrains Mono', monospace">EC 2.4.1.11 (Paso Limitante Clave)</text>
        <text x="0" y="28" fill="#16a34a" font-size="9.5" font-weight="700">⊕ Insulina (vía Fosfoproteína Fosfatasa PP1), G-6-P</text>
        <text x="0" y="41" fill="#e11d48" font-size="9.5" font-weight="700">⊣ Glucagón, Adrenalina (vía PKA / GSK-3 fosforilante)</text>
      </g>
    </g>
    """)

    # =========================================================================
    # REACCIÓN 4: ENZIMA RAMIFICADORA DEL GLUCÓGENO (AMILO α-1,4 ➔ α-1,6)
    # =========================================================================
    Y_RX_RAMIF = Y_RX_SINTASA + 95

    contenido_svg.append(f"""
    <!-- Reacción: Enzima Ramificadora -->
    <g transform="translate(385, {Y_RX_RAMIF})">
      <line x1="0" y1="0" x2="0" y2="55" stroke="#ea580c" stroke-width="2.5" marker-end="url(#arrowFlow)"/>

      <g transform="translate(20, 14)">
        <text x="0" y="0" fill="#0f172a" font-size="13" font-weight="800">Enzima Ramificadora del Glucógeno</text>
        <text x="0" y="14" fill="#64748b" font-size="10" font-family="'JetBrains Mono', monospace">Amilo-α(1,4→1,6)-transglucosidasa (EC 2.4.1.18)</text>
        <text x="0" y="27" fill="#b45309" font-size="9.5" font-weight="700">Transfiere bloque terminal de ~7 glucosas al C6</text>
        <text x="0" y="40" fill="#64748b" font-size="9">Crea ramas α(1→6) cada 8-12 glucosas (aumenta solubilidad y velocidad metabólica)</text>
      </g>
    </g>
    """)

    # =========================================================================
    # PRODUCTO FINAL: POLÍMERO DE GLUCÓGENO RAMIFICADO
    # =========================================================================
    Y_GLUC = Y_RX_RAMIF + 85

    contenido_svg.append(f"""
    <!-- Polímero de Glucógeno Completo -->
    <g transform="translate(260, {Y_GLUC})">
      <g transform="translate(0, 40)">
        {CADENA_GLUCOGENO}
      </g>
      <g transform="translate(380, 25)">
        <text x="0" y="0" fill="#0f172a" font-size="17" font-weight="900">Glucógeno (n + 1)</text>
        <text x="0" y="18" fill="#d97706" font-size="12" font-weight="800">Polisacárido de Reserva Energética</text>
        <text x="0" y="34" fill="#64748b" font-size="10.5">Enlaces principales: α(1→4) glicosídicos</text>
        <text x="0" y="48" fill="#b45309" font-size="10.5" font-weight="700">Puntos de ramificación: α(1→6) cada 8-12 glucosas</text>
        <text x="0" y="63" fill="#64748b" font-size="10">Hasta 55,000 unidades de glucosa por gránulo</text>
      </g>
    </g>
    """)

    # =========================================================================
    # EL GRÁNULO CITOSÓLICO DE INCLUSIÓN: BIOLOGÍA DE ALMACENAMIENTO Y EXPORTACIÓN
    # =========================================================================
    Y_GRANULO = Y_GLUC + 175

    contenido_svg.append(f"""
    <!-- SECCIÓN ANATÓMICA: EL GRÁNULO DE GLUCÓGENO EN EL CITOSOL -->
    <g transform="translate(180, {Y_GRANULO})">
      <rect x="0" y="0" width="680" height="155" rx="10" fill="#fffbeb" stroke="#d97706" stroke-width="1.8"/>
      
      <!-- Dibujo de la inclusión citoplasmática esférica -->
      <g transform="translate(15, 12)">
        {GRANULO_CITOSOLICO_INCLUSION}
      </g>

      <!-- Explicación fisiológica: por qué está en citosol y cómo sale -->
      <g transform="translate(160, 22)">
        <text x="0" y="0" fill="#92400e" font-size="12.5" font-weight="900">¿POR QUÉ FLOTA EN EL CITOSOL Y CÓMO SALE DE LA CÉLULA?</text>
        
        <text x="0" y="20" fill="#0f172a" font-size="10" font-weight="700">
          • <tspan fill="#b45309">Orgánulo de Inclusión no membranoso:</tspan> En hígado y músculo, el glucógeno forma gránulos densos
        </text>
        <text x="12" y="34" fill="#475569" font-size="9.5">
          inmóviles de 20 a 30 nm (rosetas β). Permite almacenar miles de glucosas sin alterar la presión osmótica celular.
        </text>

        <text x="0" y="52" fill="#0f172a" font-size="10" font-weight="700">
          • <tspan fill="#dc2626">El glucógeno NUNCA sale como polímero:</tspan> Es insoluble y demasiado gigante para cruzar membranas.
        </text>

        <text x="0" y="70" fill="#0f172a" font-size="10" font-weight="700">
          • <tspan fill="#059669">¿Cómo sale entonces? (Solo en el hígado):</tspan> La <tspan font-weight="800">Glucógeno Fosforilasa</tspan> lo degrada in situ
        </text>
        <text x="12" y="84" fill="#047857" font-size="9.5">
          a G-1-P ➔ G-6-P ➔ la <tspan font-weight="800">Glucosa-6-Fosfatasa</tspan> (en REL) quita el fosfato y <tspan font-weight="800">solo la Glucosa libre</tspan> sale a la sangre por GLUT-2.
        </text>
        <text x="12" y="98" fill="#64748b" font-size="9">
          (En el músculo, no hay G-6-Pasa: la glucosa se queda al 100% dentro para su propia contracción).
        </text>
      </g>
    </g>
    """)

    # =========================================================================
    # BALANCE ENERGÉTICO COMPACTO
    # =========================================================================
    Y_BALANCE = Y_GRANULO + 175

    contenido_svg.append(f"""
    <!-- Balance Energético Compacto -->
    <g transform="translate(190, {Y_BALANCE})">
      <rect x="0" y="0" width="620" height="92" rx="8" fill="#f8fafc" stroke="#94a3b8" stroke-width="1.4"/>
      <text x="20" y="22" fill="#0f172a" font-size="12" font-weight="900">BALANCE ENERGÉTICO NETO</text>
      <text x="20" y="40" fill="#475569" font-size="10" font-weight="600">
        Glucogénesis: Glucosa + 1 ATP + 1 UTP + Glucógeno(n) ➔ Glucógeno(n+1) + ADP + UDP + 2 Pᵢ
      </text>
      <text x="20" y="56" fill="#b91c1c" font-size="9.5" font-weight="700">
        • Costo: 2 enlaces fosfato de alta energía (~97% de eficiencia de almacenamiento)
      </text>
      <line x1="20" y1="65" x2="600" y2="65" stroke="#e2e8f0" stroke-width="1"/>
      <text x="20" y="80" fill="#d97706" font-size="9.5" font-weight="800">⇄ Glucogenólisis:</text>
      <text x="120" y="80" fill="#64748b" font-size="9">Fosforilasa (+ Pᵢ) libera G-1-P sin gastar ATP ➔ G-6-P para glucólisis inmediata</text>
    </g>
    """)

    # Ensamblar todo
    html_final = CABECERA_HTML + "\n".join(contenido_svg) + PIE_HTML

    dir_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_salida = os.path.join(dir_actual, "Glucogenesis.html")
    with open(ruta_salida, "w", encoding="utf-8") as f:
        f.write(html_final)

    # Extraer y escribir Glucogenesis.svg puro
    inicio_svg = html_final.find("<svg ")
    fin_svg = html_final.rfind("</svg>") + 6
    if inicio_svg != -1 and fin_svg != -1:
        svg_puro = html_final[inicio_svg:fin_svg]
        ruta_svg = os.path.join(dir_actual, "Glucogenesis.svg")
        with open(ruta_svg, "w", encoding="utf-8") as f_svg:
            f_svg.write(svg_puro)
        print(f"✅ SVG puro guardado en: {ruta_svg}")

    print(f"✅ Lámina de Glucogénesis con Zoom y Gránulo Citosólico generada en: {ruta_salida}")

if __name__ == "__main__":
    main()
