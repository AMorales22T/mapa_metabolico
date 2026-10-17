# =============================================================================
# MÓDULO DE REVISIÓN: Generador de la Lanzadera Malato-Aspartato
# =============================================================================
# Archivo original : 02_RESPIRACION_Y_ENERGIA/via_08_lanzaderas/generar_lanzadera_malato_aspartato.py (líneas 1 a 544 de 544)
# Descripción      : Transferencia isopotencial de equivalentes reducidos NADH en hígado y corazón.
# =============================================================================

#!/usr/bin/env python3
"""
GENERADOR VECTORIAL DE LA LANZADERA MALATO-ASPARTATO (SVG / HTML)
================================================================
Ruta metabólica individual: Mecanismo de transporte de poder reductor NADH
desde el citosol celular hacia la matriz mitocondrial.

ESTILO VISUAL IDÉNTICO A LA GLUCÓLISIS:
- Moléculas suspendidas libremente en el espacio biológico (sin tarjetas blancas ni sombras).
- Tipografía limpia y jerarquizada (Inter 800 para metabolitos, JetBrains Mono para detalles y EC).
- Flechas metabólicas estándar naranja (#ea580c) con curvas de cofactores libres.
- Membrana Mitocondrial Interna (MMI) orgánica con bicapa lipídica y transportadores proteicos integrados.
- Letrero de balance energético integrado en el estilo editorial de Glucólisis (cápsula verde suave).
"""

import os
from estructuras_lanzadera import (
    OXALACETATO, MALATO, ASPARTATO, GLUTAMATO, ALFA_CETOGLUTARATO
)

ANCHO = 1460
ALTO = 840

CABECERA_HTML = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Lanzadera Malato-Aspartato | Mapa Metabólico</title>
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
        <!-- Flecha de flujo metabólico principal (Naranja Glucólisis) -->
        <marker id="arrowFlow" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
          <path d="M 0 0 L 6 3 L 0 6 Z" fill="#ea580c" />
        </marker>
        <!-- Flecha de gasto / reactivo (Roja) -->
        <marker id="arrowRed" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#dc2626" />
        </marker>
        <!-- Flecha de salida / producto no energético (Gris pizarra) -->
        <marker id="arrowSlate" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#475569" />
        </marker>
        <!-- Flecha de ganancia / poder reductor (Verde esmeralda Glucólisis) -->
        <marker id="arrowGreen" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#059669" />
        </marker>
        <!-- Flecha de agua / transporte acuoso (Azul) -->
        <marker id="arrowBlue" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#0284c7" />
        </marker>
        <!-- Flecha de aminoácido / transporte transaminación (Rosa/Púrpura) -->
        <marker id="arrowPink" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#db2777" />
        </marker>
        <marker id="arrowPurple" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#7c3aed" />
        </marker>

        <!-- Gradientes de compartimento biológico al estilo Glucólisis -->
        <linearGradient id="gradCitosol" x1="0%" y1="0%" x2="100%" y2="0%">
          <stop offset="0%" stop-color="#f8fafc" stop-opacity="1" />
          <stop offset="70%" stop-color="#f0fdf4" stop-opacity="0.6" />
          <stop offset="100%" stop-color="#f8fafc" stop-opacity="0.9" />
        </linearGradient>

        <linearGradient id="gradMMI" x1="0%" y1="0%" x2="100%" y2="0%">
          <stop offset="0%" stop-color="#fed7aa" stop-opacity="0.7" />
          <stop offset="50%" stop-color="#ffedd5" stop-opacity="0.9" />
          <stop offset="100%" stop-color="#fed7aa" stop-opacity="0.7" />
        </linearGradient>

        <radialGradient id="gradMatriz" cx="80%" cy="50%" r="80%">
          <stop offset="0%" stop-color="#fffbeb" stop-opacity="1" />
          <stop offset="60%" stop-color="#fef3c7" stop-opacity="0.85" />
          <stop offset="100%" stop-color="#fef9c3" stop-opacity="0.7" />
        </radialGradient>
      </defs>
"""

PIE_HTML = """
    </svg>
  </div>
</body>
</html>
"""

# =============================================================================
# FUNCIONES GENERADORAS DE ELEMENTOS (IDÉNTICAS A GLUCÓLISIS)
# =============================================================================

def crear_metabolito(x, y, nombre, carbonos, detalle="", svg_estructura="", texto_izquierda=False, dx_texto=105):
    """Construye el bloque SVG de un metabolito libre con su estructura y textos (igual que en Glucólisis)."""
    if texto_izquierda:
        pos_estructura = f"translate({dx_texto + 15}, 0)"
        pos_texto = f"translate({dx_texto}, 25)"
        alineacion = 'text-anchor="end"'
    else:
        pos_estructura = "translate(0, 0)"
        pos_texto = f"translate({dx_texto}, 25)"
        alineacion = ''

    return f"""
      <!-- Metabolito Libre: {nombre} -->
      <g transform="translate({x}, {y})">
        <g transform="{pos_estructura}">
          {svg_estructura}
        </g>
        <g transform="{pos_texto}">
          <text x="0" y="0" fill="#0f172a" font-family="'Inter', sans-serif" font-size="16" font-weight="800" {alineacion}>{nombre}</text>
          <text x="0" y="18" fill="#ea580c" font-family="'Inter', sans-serif" font-size="11.5" font-weight="700" {alineacion}>{carbonos}</text>
          <text x="0" y="33" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="9.5" {alineacion}>{detalle}</text>
        </g>
      </g>
    """


def crear_entorno_lanzadera_svg():
    """Genera el fondo celular orgánico al estilo de entorno_celular.py de Glucólisis."""
    return f"""
    <!-- ================================================================= -->
    <!-- CAPA 1: FONDOS BIOLÓGICOS CITOSOL / MATRIZ                        -->
    <!-- ================================================================= -->
    <!-- Citosol (Izquierda, x=0 a 580) -->
    <rect x="0" y="0" width="580" height="{ALTO}" fill="url(#gradCitosol)" />
    
    <!-- Microfilamentos de citoesqueleto y polirribosomas en Citosol (Estilo Glucólisis) -->
    <g opacity="0.25" stroke="#94a3b8" fill="none">
      <path d="M 20 80 Q 220 40 500 90" stroke-width="1.5" stroke-dasharray="8 6" />
      <path d="M 40 380 Q 250 420 520 370" stroke-width="1.4" stroke-dasharray="6 6" />
      <path d="M 30 720 Q 280 680 520 730" stroke-width="1.5" stroke-dasharray="8 6" />
    </g>
    <g fill="#94a3b8" opacity="0.2">
      <circle cx="90" cy="70" r="2.5"/><circle cx="96" cy="73" r="2"/><circle cx="93" cy="78" r="2.2"/>
      <circle cx="500" cy="410" r="2.5"/><circle cx="507" cy="412" r="2"/><circle cx="504" cy="418" r="2.2"/>
    </g>

    <!-- Matriz Mitocondrial (Derecha, x=740 a ANCHO) -->
    <rect x="740" y="0" width="{ANCHO - 740}" height="{ALTO}" fill="url(#gradMatriz)" />
    
    <!-- Crestas mitocondriales sutiles al fondo de la Matriz (Estilo Krebs) -->
    <g stroke="#d97706" stroke-width="1.8" fill="none" opacity="0.22">
      <path d="M 1460 220 C 1340 180, 1260 260, 1140 220" />
      <path d="M 1460 460 C 1320 420, 1220 500, 1100 460" />
      <path d="M 1460 680 C 1360 650, 1280 720, 1180 690" />
    </g>

    <!-- ================================================================= -->
    <!-- CAPA 2: MEMBRANA MITOCONDRIAL INTERNA (MMI) Y BICAPA REAL         -->
    <!-- ================================================================= -->
    <!-- Franja de la membrana interna (x=580 a 740, ancho=160px) -->
    <rect x="580" y="0" width="160" height="{ALTO}" fill="url(#gradMMI)" stroke="#d97706" stroke-width="1.5" opacity="0.85"/>

    <!-- Cabezas de fosfolípidos de la bicapa a lo largo de las caras de la membrana -->
    <g fill="#d97706" opacity="0.5">
      <!-- Hoja citosólica (x=585) -->
      <circle cx="585" cy="50" r="3"/><circle cx="585" cy="70" r="3"/><circle cx="585" cy="90" r="3"/>
      <circle cx="585" cy="270" r="3"/><circle cx="585" cy="290" r="3"/><circle cx="585" cy="310" r="3"/>
      <circle cx="585" cy="450" r="3"/><circle cx="585" cy="470" r="3"/><circle cx="585" cy="490" r="3"/>
      <circle cx="585" cy="670" r="3"/><circle cx="585" cy="690" r="3"/><circle cx="585" cy="710" r="3"/>

      <!-- Hoja matricial (x=735) -->
      <circle cx="735" cy="50" r="3"/><circle cx="735" cy="70" r="3"/><circle cx="735" cy="90" r="3"/>
      <circle cx="735" cy="270" r="3"/><circle cx="735" cy="290" r="3"/><circle cx="735" cy="310" r="3"/>
      <circle cx="735" cy="450" r="3"/><circle cx="735" cy="470" r="3"/><circle cx="735" cy="490" r="3"/>
      <circle cx="735" cy="670" r="3"/><circle cx="735" cy="690" r="3"/><circle cx="735" cy="710" r="3"/>
    </g>

    <!-- Encabezados biológicos discretos tipo Glucólisis (sin cajas duras) -->
    <text x="40" y="36" fill="#64748b" font-family="'Inter', sans-serif" font-size="11" font-weight="800" letter-spacing="1.5">CITOSOL CELULAR (GLUCÓLISIS AERÓBICA)</text>
    <text x="660" y="36" fill="#b45309" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" text-anchor="middle" letter-spacing="1">MMI (BICAPA LIPÍDICA)</text>
    <text x="780" y="36" fill="#92400e" font-family="'Inter', sans-serif" font-size="11" font-weight="800" letter-spacing="1.5">MATRIZ MITOCONDRIAL (KREBS / CTE)</text>

    <!-- ================================================================= -->
    <!-- CAPA 3: TRANSPORTADORES PROTEICOS EMBEBIDOS (ESTILO GLUT / MPC)   -->
    <!-- ================================================================= -->
    <!-- 1. TRANSPORTADOR SLC25A11 (OGC) - Malato / α-Cetoglutarato -->
    <g transform="translate(605, 120)">
      <!-- Lóbulos proteicos ámbar -->
      <path d="M 5 10 C 15 -10, 45 -10, 55 10 C 60 25, 55 50, 40 60 C 25 65, 10 50, 5 30 Z" fill="#f59e0b" stroke="#d97706" stroke-width="2"/>
      <path d="M 105 10 C 95 -10, 65 -10, 55 10 C 50 25, 55 50, 70 60 C 85 65, 100 50, 105 30 Z" fill="#f59e0b" stroke="#d97706" stroke-width="2"/>
      
      <!-- Poro central acuoso -->
      <ellipse cx="55" cy="35" rx="14" ry="32" fill="#fffbeb" stroke="#f59e0b" stroke-width="1.8"/>

      <!-- Flechas internas de antitransporte -->
      <line x1="15" y1="23" x2="95" y2="23" stroke="#0284c7" stroke-width="2.5" marker-end="url(#arrowBlue)"/>
      <line x1="95" y1="47" x2="15" y2="47" stroke="#ea580c" stroke-width="2.5" marker-end="url(#arrowFlow)"/>

      <!-- Placa identificadora de la proteína -->
      <g transform="translate(55, 82)">
        <rect x="-48" y="-10" width="96" height="20" rx="10" fill="#fef3c7" stroke="#d97706" stroke-width="1.4"/>
        <text x="0" y="4" fill="#92400e" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="900" text-anchor="middle">SLC25A11 (OGC)</text>
      </g>
      <text x="55" y="105" fill="#78350f" font-family="'Inter', sans-serif" font-size="8.5" font-weight="700" text-anchor="middle">Malato²⁻ ⇄ α-KG²⁻</text>
    </g>

    <!-- 2. TRANSPORTADOR SLC25A12 (ARALAR / AGC1) - Glutamato / Aspartato -->
    <g transform="translate(605, 520)">
      <!-- Lóbulos proteicos rosa/magenta -->
      <path d="M 5 10 C 15 -10, 45 -10, 55 10 C 60 25, 55 50, 40 60 C 25 65, 10 50, 5 30 Z" fill="#ec4899" stroke="#db2777" stroke-width="2"/>
      <path d="M 105 10 C 95 -10, 65 -10, 55 10 C 50 25, 55 50, 70 60 C 85 65, 100 50, 105 30 Z" fill="#ec4899" stroke="#db2777" stroke-width="2"/>
      
      <!-- Poro central acuoso -->
      <ellipse cx="55" cy="35" rx="14" ry="32" fill="#fdf2f8" stroke="#f472b6" stroke-width="1.8"/>

      <!-- Flechas internas de antitransporte -->
      <line x1="15" y1="23" x2="95" y2="23" stroke="#be185d" stroke-width="2.5" marker-end="url(#arrowPink)"/>
      <line x1="95" y1="47" x2="15" y2="47" stroke="#7c3aed" stroke-width="2.5" marker-end="url(#arrowPurple)"/>

      <!-- Placa identificadora de la proteína -->
      <g transform="translate(55, 82)">
        <rect x="-54" y="-10" width="108" height="20" rx="10" fill="#fdf2f8" stroke="#db2777" stroke-width="1.4"/>
        <text x="0" y="4" fill="#9d174d" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="900" text-anchor="middle">SLC25A12 (Aralar)</text>
      </g>
      <text x="55" y="105" fill="#831843" font-family="'Inter', sans-serif" font-size="8.5" font-weight="700" text-anchor="middle">Glu⁻ + H⁺ ⇄ Asp⁻ (ΔΨ)</text>
    </g>
    """


def generar_svg_lanzadera():
    svg = []

    # 1. Capa de fondo celular orgánico
    svg.append(crear_entorno_lanzadera_svg())

    # =========================================================================
    # 2. EJE SUPERIOR: REDUCCIÓN Y TRANSPORTE DE MALATO
    # =========================================================================

    # --- CITOSOL SUPERIOR ---
    # Oxalacetato (citosol)
    svg.append(crear_metabolito(
        x=45, y=90,
        nombre="Oxalacetato",
        carbonos="4 Carbonos",
        detalle="α-Cetoácido",
        svg_estructura=OXALACETATO
    ))

    # Reacción cMDH (Malato Deshidrogenasa citosólica - Estilo Glucólisis)
    svg.append("""
    <g transform="translate(235, 155)">
      <!-- Flecha principal horizontal -->
      <line x1="0" y1="0" x2="65" y2="0" stroke="#ea580c" stroke-width="2.2" marker-end="url(#arrowFlow)"/>

      <!-- Nombre y código EC de la enzima (libre, sin caja) -->
      <g transform="translate(32, -18)">
        <text x="0" y="0" fill="#0f172a" font-family="'Inter', sans-serif" font-size="12" font-weight="800" text-anchor="middle">cMDH</text>
        <text x="0" y="12" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="9" text-anchor="middle">EC 1.1.1.37</text>
      </g>

      <!-- Curvas de Cofactor estilo Glucólisis: Gasto de NADH -->
      <path d="M 0 16 Q 32 38 65 16" fill="none" stroke="#dc2626" stroke-width="1.8" marker-end="url(#arrowSlate)"/>
      <text x="32" y="44" fill="#dc2626" font-family="'Inter', sans-serif" font-size="9.5" font-weight="800" text-anchor="middle">NADH + H⁺ ➔ NAD⁺</text>
      <text x="32" y="55" fill="#047857" font-family="'JetBrains Mono', monospace" font-size="8" font-weight="700" text-anchor="middle">(de Glucólisis)</text>
    </g>
    """)

    # L-Malato (citosol)
    svg.append(crear_metabolito(
        x=335, y=90,
        nombre="L-Malato",
        carbonos="4 Carbonos",
        detalle="α-Hidroxiácido",
        svg_estructura=MALATO
    ))

    # Cruce hacia el transportador SLC25A11
    svg.append("""
    <line x1="520" y1="143" x2="615" y2="143" stroke="#0284c7" stroke-width="2.5" marker-end="url(#arrowBlue)"/>
    """)

    # --- MATRIZ SUPERIOR ---
    # Salida desde SLC25A11 hacia L-Malato matriz
    svg.append("""
    <line x1="705" y1="143" x2="775" y2="143" stroke="#0284c7" stroke-width="2.5" marker-end="url(#arrowBlue)"/>
    """)

    # L-Malato (matriz)
    svg.append(crear_metabolito(
        x=780, y=90,
        nombre="L-Malato",
        carbonos="4 Carbonos",
        detalle="Pool de Krebs",
        svg_estructura=MALATO
    ))

    # Reacción mMDH (Malato Deshidrogenasa mitocondrial - Estilo Glucólisis)
    svg.append("""
    <g transform="translate(970, 155)">
      <!-- Flecha principal horizontal -->
      <line x1="0" y1="0" x2="115" y2="0" stroke="#ea580c" stroke-width="2.4" marker-end="url(#arrowFlow)"/>

      <!-- Nombre y código EC de la enzima -->
      <g transform="translate(57, -18)">
        <text x="0" y="0" fill="#0f172a" font-family="'Inter', sans-serif" font-size="12.5" font-weight="800" text-anchor="middle">mMDH / MDH2</text>
        <text x="0" y="12" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="9" text-anchor="middle">EC 1.1.1.37 (Krebs)</text>
      </g>

      <!-- Curva de Cofactor estilo Glucólisis: Ganancia de NADH matricial -->
      <path d="M 10 16 Q 57 42 105 16" fill="none" stroke="#059669" stroke-width="2" marker-end="url(#arrowGreen)"/>
      <text x="57" y="44" fill="#047857" font-family="'Inter', sans-serif" font-size="10" font-weight="900" text-anchor="middle">NAD⁺ ➔ NADH + H⁺</text>

      <!-- Badge elegante de producto energético estilo Glucólisis -->
      <g transform="translate(57, 60)">
        <rect x="-65" y="-9" width="130" height="18" rx="9" fill="#dcfce7" stroke="#16a34a" stroke-width="1.2"/>
        <text x="0" y="4" fill="#15803d" font-family="'Inter', sans-serif" font-size="8.5" font-weight="900" text-anchor="middle">★ COMPLEJO I (~2.5 ATP)</text>
      </g>
    </g>
    """)

    # Oxalacetato (matriz)
    svg.append(crear_metabolito(
        x=1150, y=90,
        nombre="Oxalacetato",
        carbonos="4 Carbonos",
        detalle="Pool de Krebs / mAST",
        svg_estructura=OXALACETATO
    ))

    # =========================================================================
    # 3. EJE VERTICAL Y TRANSAMINACIONES (mAST y cAST)
    # =========================================================================

    # --- MATRIZ: TRANSAMINACIÓN mAST ---
    # Flecha vertical descendente desde Oxalacetato hacia L-Aspartato
    svg.append("""
    <g transform="translate(1250, 240)">
      <line x1="0" y1="10" x2="0" y2="265" stroke="#ea580c" stroke-width="2.4" marker-end="url(#arrowFlow)"/>

      <!-- Enzima mAST (libre al costado de la flecha, estilo Glucólisis) -->
      <g transform="translate(16, 120)">
        <text x="0" y="0" fill="#0f172a" font-family="'Inter', sans-serif" font-size="12.5" font-weight="800">mAST / GOT2</text>
        <text x="0" y="14" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="9">EC 2.6.1.1 • PLP</text>
        <text x="0" y="27" fill="#be185d" font-family="'Inter', sans-serif" font-size="8.5" font-weight="700">Aspartato Aminotransferasa</text>
      </g>

      <!-- Salida de α-Cetoglutarato hacia la izquierda (hacia su posición libre) -->
      <path d="M -8 115 L -165 115" fill="none" stroke="#ea580c" stroke-width="2.2" marker-end="url(#arrowFlow)"/>
      <text x="-85" y="106" fill="#c2410c" font-family="'Inter', sans-serif" font-size="9" font-weight="800" text-anchor="middle">+ α-Cetoglutarato</text>
    </g>
    """)

    # Molécula Libre: α-Cetoglutarato (matriz)
    svg.append(crear_metabolito(
        x=830, y=285,
        nombre="α-Cetoglutarato",
        carbonos="5 Carbonos",
        detalle="α-Cetoácido (Pool Krebs)",
        svg_estructura=ALFA_CETOGLUTARATO
    ))

    # Flecha desde α-Cetoglutarato hacia SLC25A11
    svg.append("""
    <path d="M 830 355 L 735 355 Q 715 355 715 167 L 705 167" fill="none" stroke="#ea580c" stroke-width="2.2" marker-end="url(#arrowFlow)"/>
    """)

    # Retorno de α-Cetoglutarato a través de MMI hacia Citosol y cAST (rodea por debajo a L-Malato)
    svg.append("""
    <path d="M 605 167 L 490 167 Q 445 167 445 205 Q 445 240 375 240 L 260 240 Q 185 240 155 350" fill="none" stroke="#ea580c" stroke-width="2" stroke-dasharray="6 3" marker-end="url(#arrowFlow)"/>
    <!-- Pill indicador estilo Glucólisis -->
    <g transform="translate(350, 240)">
      <rect x="-45" y="-9" width="90" height="18" rx="9" fill="#ffedd5" stroke="#ea580c" stroke-width="1.2"/>
      <text x="0" y="4" fill="#c2410c" font-family="'JetBrains Mono', monospace" font-size="8" font-weight="800" text-anchor="middle">α-KG ➔ cAST</text>
    </g>
    """)

    # --- CITOSOL: TRANSAMINACIÓN cAST ---
    # Flecha vertical ascendente desde L-Aspartato hacia Oxalacetato
    svg.append("""
    <g transform="translate(140, 240)">
      <line x1="0" y1="265" x2="0" y2="10" stroke="#ea580c" stroke-width="2.4" marker-end="url(#arrowFlow)"/>

      <!-- Enzima cAST (libre al costado de la flecha) -->
      <g transform="translate(-16, 120)">
        <text x="0" y="0" fill="#0f172a" font-family="'Inter', sans-serif" font-size="12.5" font-weight="800" text-anchor="end">cAST / GOT1</text>
        <text x="0" y="14" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="9" text-anchor="end">EC 2.6.1.1 • PLP</text>
        <text x="0" y="27" fill="#be185d" font-family="'Inter', sans-serif" font-size="8.5" font-weight="700" text-anchor="end">Aspartato Aminotransferasa</text>
      </g>

      <!-- Salida de L-Glutamato hacia la derecha (hacia tarjeta Glutamato citosol) -->
      <path d="M 8 135 C 50 145 130 180 185 270" fill="none" stroke="#be185d" stroke-width="2" marker-end="url(#arrowPink)"/>
      <text x="125" y="195" fill="#9d174d" font-family="'Inter', sans-serif" font-size="9" font-weight="800">+ L-Glutamato</text>
    </g>
    """)

    # =========================================================================
    # 4. EJE INFERIOR: TRANSPORTE DE GLUTAMATO Y ASPARTATO
    # =========================================================================

    # --- CITOSOL INFERIOR ---
    # L-Aspartato (citosol)
    svg.append(crear_metabolito(
        x=45, y=515,
        nombre="L-Aspartato",
        carbonos="4 Carbonos",
        detalle="Precursor de OAA",
        svg_estructura=ASPARTATO
    ))

    # L-Glutamato (citosol)
    svg.append(crear_metabolito(
        x=335, y=515,
        nombre="L-Glutamato",
        carbonos="5 Carbonos",
        detalle="Portador amino (citosol)",
        svg_estructura=GLUTAMATO
    ))

    # Cruce desde L-Glutamato citosol hacia SLC25A12
    svg.append("""
    <line x1="500" y1="543" x2="605" y2="543" stroke="#be185d" stroke-width="2.5" marker-end="url(#arrowPink)"/>
    """)

    # Retorno de L-Aspartato desde SLC25A12 hacia L-Aspartato citosol (Corredor inferior limpio)
    svg.append("""
    <path d="M 605 567 L 565 567 Q 545 567 545 620 L 545 685 Q 545 695 530 695 L 145 695 Q 135 695 135 685 L 135 665" fill="none" stroke="#7c3aed" stroke-width="2.2" marker-end="url(#arrowPurple)"/>
    <!-- Pill indicador estilo Glucólisis -->
    <g transform="translate(340, 695)">
      <rect x="-60" y="-9" width="120" height="18" rx="9" fill="#fdf2f8" stroke="#7c3aed" stroke-width="1.2"/>
      <text x="0" y="4" fill="#6b21a8" font-family="'JetBrains Mono', monospace" font-size="8" font-weight="800" text-anchor="middle">Aspartato ➔ cAST</text>
    </g>
    """)

    # --- MATRIZ INFERIOR ---
    # Salida desde SLC25A12 hacia L-Glutamato matriz
    svg.append("""
    <line x1="705" y1="543" x2="775" y2="543" stroke="#be185d" stroke-width="2.5" marker-end="url(#arrowPink)"/>
    """)

    # L-Glutamato (matriz)
    svg.append(crear_metabolito(
        x=780, y=515,
        nombre="L-Glutamato",
        carbonos="5 Carbonos",
        detalle="Sustrato de mAST",
        svg_estructura=GLUTAMATO
    ))

    # Entrada de L-Glutamato hacia mAST (vía ascendente despejada)
    svg.append("""
    <path d="M 940 540 L 1070 540 Q 1100 540 1100 440 L 1100 395 Q 1100 375 1240 375" fill="none" stroke="#be185d" stroke-width="2" marker-end="url(#arrowPink)"/>
    <text x="1030" y="530" fill="#9d174d" font-family="'Inter', sans-serif" font-size="9" font-weight="800">+ L-Glutamato</text>
    """)

    # L-Aspartato (matriz)
    svg.append(crear_metabolito(
        x=1150, y=515,
        nombre="L-Aspartato",
        carbonos="4 Carbonos",
        detalle="Exportable a citosol",
        svg_estructura=ASPARTATO
    ))

    # Exportación de L-Aspartato matriz hacia SLC25A12 (vía inferior despejada)
    svg.append("""
    <path d="M 1250 665 L 1250 685 Q 1250 695 1235 695 L 755 695 Q 740 695 740 680 L 740 567 L 705 567" fill="none" stroke="#7c3aed" stroke-width="2.2" marker-end="url(#arrowPurple)"/>
    <!-- Pill indicador estilo Glucólisis -->
    <g transform="translate(980, 695)">
      <rect x="-65" y="-9" width="130" height="18" rx="9" fill="#fdf2f8" stroke="#7c3aed" stroke-width="1.2"/>
      <text x="0" y="4" fill="#6b21a8" font-family="'JetBrains Mono', monospace" font-size="8" font-weight="800" text-anchor="middle">Aspartato ➔ SLC25A12</text>
    </g>
    """)

    # =========================================================================
    # 5. LETRERO DE BALANCE ENERGÉTICO INTEGRADO (ESTILO GLUCÓLISIS / KREBS)
    # =========================================================================
    svg.append(f"""
    <!-- Badge de Balance Energético y Tisular al estilo Glucólisis -->
    <g transform="translate({ANCHO / 2}, 780)">
      <!-- Fondo integrado verde suave con borde esmeralda -->
      <rect x="-510" y="-22" width="1020" height="44" rx="22" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.8" filter="drop-shadow(0 4px 12px rgba(22, 163, 74, 0.12))"/>
      
      <!-- Icono y Rendimiento -->
      <text x="-480" y="6" fill="#15803d" font-family="'Inter', sans-serif" font-size="12" font-weight="900">★ RENDIMIENTO NETO:</text>
      <text x="-295" y="6" fill="#0f172a" font-family="'Inter', sans-serif" font-size="11.5" font-weight="700">1 NADH citosólico ➔ 1 NADH matricial (Complejo I de la CTE: ~2.5 ATP)</text>
      
      <!-- Separador sutil -->
      <line x1="210" y1="-10" x2="210" y2="10" stroke="#86efac" stroke-width="1.5"/>
      
      <!-- Cápsula de Tejidos (estilo píldora de Fase 2 de Glucólisis) -->
      <g transform="translate(340, 0)">
        <rect x="-115" y="-12" width="230" height="24" rx="12" fill="#ffedd5" stroke="#ea580c" stroke-width="1.4"/>
        <text x="0" y="5" fill="#c2410c" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="800" text-anchor="middle">HÍGADO • RIÑÓN • CORAZÓN</text>
      </g>
    </g>
    """)

    return "".join(svg)


def main():
    contenido_svg = generar_svg_lanzadera()
    
    # Escribir archivo SVG puro
    ruta_svg = os.path.join(os.path.dirname(__file__), "Lanzadera_Malato_Aspartato.svg")
    with open(ruta_svg, "w", encoding="utf-8") as f_svg:
        f_svg.write(f'<svg width="{ANCHO}" height="{ALTO}" viewBox="0 0 {ANCHO} {ALTO}" xmlns="http://www.w3.org/2000/svg">\n')
        f_svg.write(CABECERA_HTML.split("<svg")[1].split("</defs>")[0] + "</defs>\n")
        f_svg.write(contenido_svg)
        f_svg.write("\n</svg>")
    
    # Escribir archivo HTML
    html_final = CABECERA_HTML + contenido_svg + PIE_HTML
    ruta_html = os.path.join(os.path.dirname(__file__), "Lanzadera_Malato_Aspartato.html")
    with open(ruta_html, "w", encoding="utf-8") as f_html:
        f_html.write(html_final)
        
    print(f"✅ ¡Lanzadera Malato-Aspartato generada al estilo exacto de Glucólisis!")
    print(f"   - HTML: {ruta_html}")
    print(f"   - SVG:  {ruta_svg}")


if __name__ == "__main__":
    main()
