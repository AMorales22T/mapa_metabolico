# =============================================================================
# MÓDULO DE REVISIÓN: Entorno de Transaminación y Desaminación
# =============================================================================
# Archivo original : 04_NITROGENO_Y_AMINOACIDOS/via_13_transaminacion_y_desaminacion/entorno_aminoacidos.py (líneas 1 a 150 de 150)
# Descripción      : Compartimentos citosólico y mitocondrial para el manejo del grupo amino.
# =============================================================================

#!/usr/bin/env python3
"""
ENTORNO BIOLÓGICO CELULAR PARA EL METABOLISMO DE NITROGENO Y AMINOÁCIDOS (SVG)
=============================================================================
Este módulo provee la arquitectura biológica real donde ocurren:
1. Membrana Plasmática y Torrente Sanguíneo (Arriba):
   - Importación de aminoácidos desde la sangre a través de transportadores específicos (LAT1 / ASCT2).
   - Exportación de transportadores de nitrógeno (Alanina, Glutamina) hacia el hígado.
2. Citosol Real:
   - Reacciones de Transaminación citosólicas (ALT / AST citosólicas).
   - Síntesis de Glutamina (Glutamina Sintetasa) como reserva de amonio atóxica.
   - Citoesqueleto y polirribosomas libres.
3. Mitocondria Real (Abajo / Matriz):
   - Transportador mitocondrial de Glutamato / Aspartato.
   - Desaminación oxidativa en la Matriz por la Glutamato Deshidrogenasa (GLDH).
   - Liberación de NH4+ lista para el Ciclo de la Urea (CPS-1).
"""

DEFS_ENTORNO_AMINO = """
    <!-- Gradiente acuoso citosólico biológico -->
    <linearGradient id="gradCitosolAmino" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#f8fafc" stop-opacity="1" />
      <stop offset="5%" stop-color="#f0fdfa" stop-opacity="0.85" />
      <stop offset="50%" stop-color="#f8fafc" stop-opacity="0.6" />
      <stop offset="90%" stop-color="#f0fdfa" stop-opacity="0.75" />
      <stop offset="100%" stop-color="#f8fafc" stop-opacity="1" />
    </linearGradient>

    <!-- Gradiente del medio extracelular vascular / intersticial (arriba) -->
    <linearGradient id="gradVascularAmino" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#7f1d1d" stop-opacity="0.9" />
      <stop offset="70%" stop-color="#991b1b" stop-opacity="0.85" />
      <stop offset="100%" stop-color="#b91c1c" stop-opacity="0.75" />
    </linearGradient>

    <!-- Gradiente de la Matriz Mitocondrial (abajo, ámbar cálido) -->
    <radialGradient id="gradMitocondriaAmino" cx="50%" cy="100%" r="90%">
      <stop offset="0%" stop-color="#fef3c7" stop-opacity="0.95" />
      <stop offset="50%" stop-color="#fffbeb" stop-opacity="0.9" />
      <stop offset="100%" stop-color="#fef9c3" stop-opacity="0.85" />
    </radialGradient>

    <!-- Marcador de flecha verde azulada (Nitrógeno / Aminoácidos) -->
    <marker id="arrowTeal" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
      <path d="M 0 0 L 6 3 L 0 6 Z" fill="#0d9488" />
    </marker>
    <!-- Marcador de flecha azul (Grupos Amino / Nitrógeno) -->
    <marker id="arrowBlueAmino" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
      <path d="M 0 0 L 6 3 L 0 6 Z" fill="#2563eb" />
    </marker>
"""

def generar_entorno_aminoacidos_svg(ancho=1000, alto=2200, y_mitocondria=1480):
    """
    Construye la envoltura celular biológica sin carteles tipo 'CITOSOL',
    con membrana plasmática superior, capilar sanguíneo, transportador de aminoácidos
    y mitocondria inferior espaciosa.
    """
    return f"""
    <!-- ================================================================= -->
    <!-- CAPA 1: FONDO ACUOSO CITOSÓLICO                                   -->
    <!-- ================================================================= -->
    <rect x="0" y="0" width="{ancho}" height="{alto}" fill="url(#gradCitosolAmino)" />

    <!-- ================================================================= -->
    <!-- CAPA 2: ESTRUCTURAS DEL CITOPLASMA (CITOESQUELETO Y VESÍCULAS)    -->
    <!-- ================================================================= -->
    <g opacity="0.32" stroke="#94a3b8" fill="none">
      <path d="M 40 220 Q 250 170 500 240 T 960 210" stroke-width="1.6" stroke-dasharray="8 6" />
      <path d="M 50 510 Q 320 580 620 530 T 950 550" stroke-width="1.5" stroke-dasharray="7 6" />
      <path d="M 40 850 Q 300 790 600 860 T 960 820" stroke-width="1.5" stroke-dasharray="8 5" />
      <path d="M 60 1180 Q 350 1240 680 1190 T 950 1220" stroke-width="1.4" stroke-dasharray="6 6" />
    </g>

    <!-- Polirribosomas celulares flotando en el citosol -->
    <g fill="#94a3b8" opacity="0.25">
      <circle cx="120" cy="180" r="2.5"/><circle cx="126" cy="182" r="2"/><circle cx="124" cy="188" r="2.3"/><circle cx="118" cy="187" r="2.1"/>
      <circle cx="860" cy="310" r="2.5"/><circle cx="867" cy="312" r="2"/><circle cx="864" cy="318" r="2.3"/><circle cx="858" cy="317" r="2.1"/>
      <circle cx="140" cy="740" r="2.5"/><circle cx="146" cy="743" r="2.2"/><circle cx="143" cy="748" r="2"/><circle cx="138" cy="746" r="2.3"/>
      <circle cx="880" cy="980" r="2.5"/><circle cx="887" cy="983" r="2"/><circle cx="883" cy="988" r="2.2"/><circle cx="877" cy="986" r="2.1"/>
    </g>

    <!-- Vesículas citosólicas translúcidas -->
    <g opacity="0.3">
      <circle cx="150" cy="420" r="24" fill="#ccfbf1" stroke="#14b8a6" stroke-width="1.8" stroke-dasharray="4 2"/>
      <circle cx="870" cy="650" r="22" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8" stroke-dasharray="4 2"/>
      <circle cx="160" cy="1050" r="26" fill="#ccfbf1" stroke="#14b8a6" stroke-width="1.8" stroke-dasharray="4 2"/>
    </g>

    <!-- ================================================================= -->
    <!-- CAPA 3: MEDIO EXTRACELULAR / TORRENTE SANGUÍNEO Y MEMBRANA PLASMÁTICA -->
    <!-- ================================================================= -->
    <path d="M 0 0 L {ancho} 0 L {ancho} 55 Q 500 78 0 55 Z" fill="url(#gradVascularAmino)" />
    
    <!-- Glóbulos rojos flotando en capilar superior -->
    <g opacity="0.85">
      <g transform="translate(180, 26) rotate(-10)">
        <ellipse cx="0" cy="0" rx="20" ry="12" fill="#ef4444" stroke="#7f1d1d" stroke-width="1.5"/>
        <ellipse cx="0" cy="0" rx="10" ry="5" fill="#7f1d1d" opacity="0.6"/>
      </g>
      <g transform="translate(820, 24) rotate(14)">
        <ellipse cx="0" cy="0" rx="22" ry="13" fill="#ef4444" stroke="#7f1d1d" stroke-width="1.5"/>
        <ellipse cx="0" cy="0" rx="11" ry="6" fill="#7f1d1d" opacity="0.6"/>
      </g>
    </g>

    <!-- Bicapa fosfolipídica plasmática -->
    <path d="M 0 55 Q 500 78 {ancho} 55" fill="none" stroke="#0284c7" stroke-width="8" stroke-linecap="round"/>
    <path d="M 0 63 Q 500 86 {ancho} 63" fill="none" stroke="#38bdf8" stroke-width="3" stroke-linecap="round"/>

    <!-- Transportador de Aminoácidos en la membrana (LAT-1 / Sistema A) -->
    <g transform="translate(240, 42)">
      <path d="M 0 5 C 10 -10, 26 -10, 32 5 C 36 18, 32 36, 23 42 C 10 45, 2 35, 0 22 Z" fill="#0d9488" stroke="#0f766e" stroke-width="2"/>
      <path d="M 76 5 C 66 -10, 50 -10, 44 5 C 40 18, 44 36, 53 42 C 66 45, 74 35, 76 22 Z" fill="#0d9488" stroke="#0f766e" stroke-width="2"/>
      <ellipse cx="38" cy="20" rx="9" ry="17" fill="#ccfbf1" stroke="#14b8a6" stroke-width="1.6"/>
      <text x="38" y="47" fill="#0f766e" font-size="9.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">LAT-1 / ASCT2</text>
      <!-- Aminoácido entrando -->
      <line x1="38" y1="-18" x2="38" y2="8" stroke="#0d9488" stroke-width="2.2" marker-end="url(#arrowTeal)"/>
      <line x1="38" y1="32" x2="38" y2="58" stroke="#0d9488" stroke-width="2.4" marker-end="url(#arrowTeal)"/>
    </g>
    <text x="340" y="32" fill="#fecaca" font-size="11" font-weight="800" font-family="'Inter', sans-serif">TORRENTE SANGUÍNEO • AMINOÁCIDOS DIETARIOS Y MUSCULARES</text>

    <!-- ================================================================= -->
    <!-- CAPA 4: MITOCONDRIA BIOLÓGICA REAL (ABAJO)                        -->
    <!-- ================================================================= -->
    <g transform="translate(0, {y_mitocondria})">
      <!-- MME Membrana Mitocondrial Externa Lisa (Ámbar) -->
      <path d="M 0 50 Q 250 15 500 35 T {ancho} 25 L {ancho} {alto - y_mitocondria} L 0 {alto - y_mitocondria} Z" fill="url(#gradMitocondriaAmino)" stroke="#b45309" stroke-width="3.5"/>
      
      <!-- Espacio Intermembrana (EIM) -->
      <path d="M 0 65 Q 250 30 500 50 T {ancho} 40" fill="none" stroke="#78350f" stroke-width="2" stroke-dasharray="6 3"/>

      <!-- Crestas Mitocondriales Profundas -->
      <path d="M 60 130 C 130 80, 160 150, 230 100 C 280 150, 240 180, 130 170 Z" fill="#fef3c7" stroke="#b45309" stroke-width="2.5" opacity="0.85"/>
      <path d="M 720 120 C 790 70, 840 140, 910 90 C 970 140, 930 180, 800 165 Z" fill="#fef3c7" stroke="#b45309" stroke-width="2.5" opacity="0.85"/>

      <!-- Transportador Mitocondrial de Glutamato (Carrier AGC / GC) -->
      <g transform="translate(465, 20)">
        <rect x="0" y="0" width="70" height="28" rx="8" fill="#b45309" stroke="#78350f" stroke-width="2"/>
        <text x="35" y="18" fill="#ffffff" font-size="10.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">AGC / GC1</text>
      </g>
      <text x="550" y="38" fill="#78350f" font-size="11" font-weight="800" font-family="'Inter', sans-serif">Carrier de Glutamato / Aspartato (MMI)</text>

      <!-- Título biológico de la matriz (Despejado lateralmente) -->
      <g transform="translate(240, 75)">
        <text x="0" y="0" fill="#78350f" font-size="18" font-weight="900" font-family="'Inter', sans-serif" letter-spacing="3">MATRIZ MITOCONDRIAL</text>
        <text x="0" y="18" fill="#92400e" font-size="11.5" font-weight="700" font-family="'Inter', sans-serif">Desaminación Oxidativa • Destino Urea</text>
      </g>
    </g>
    """
