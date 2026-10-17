# =============================================================================
# MÓDULO DE REVISIÓN: Entorno Celular de Beta-Oxidación Mitocondrial
# =============================================================================
# Archivo original : 03_LIPIDOS/via_09_beta_oxidacion/entorno_beta_oxidacion.py (líneas 1 a 188 de 188)
# Descripción      : Compartimentos celulares para Beta-Oxidación Mitocondrial.
# =============================================================================

#!/usr/bin/env python3
"""
ENTORNO BIOLÓGICO Y MITOCONDRIAL - BETA-OXIDACIÓN DE ÁCIDOS GRASOS
==================================================================
Diseña el escenario compartimental realista idéntico a Glucolisis y Ciclo de Krebs:
1. CITOSOL CELULAR (Arriba): Microfilamentos, gota lipídica con triacilgliceroles, ribosomas.
2. ENVOLTURA MITOCONDRIAL (Medio):
   - MME: Membrana externa con CPT-I (inhibido alostéricamente por Malonil-CoA).
   - EIM: Espacio Intermembrana con gradiente de H+ y tránsito de Palmitoilcarnitina.
   - MMI: Bicapa lipídica de fosfolípidos con CACT (antiporte) y CPT-II matricial.
3. MATRIZ MITOCONDRIAL (Abajo):
   - Fondo cálido ámbar con crestas mitocondriales laterales onduladas.
   - Ribosomas 55S y gránulos densos de Ca2+/Mg2+.
"""

DEFS_ENTORNO_BETA_OX = """
    <!-- Gradiente del Citosol Celular -->
    <linearGradient id="boGradCitosol" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#f8fafc" stop-opacity="1" />
      <stop offset="100%" stop-color="#f0fdf4" stop-opacity="0.85" />
    </linearGradient>

    <!-- Gradiente de Gota Lipídica Citosólica (Almacén TAG) -->
    <radialGradient id="boGradGotaLipidica" cx="40%" cy="40%" r="60%">
      <stop offset="0%" stop-color="#fef08a" stop-opacity="0.9" />
      <stop offset="70%" stop-color="#f59e0b" stop-opacity="0.6" />
      <stop offset="100%" stop-color="#d97706" stop-opacity="0.8" />
    </radialGradient>

    <!-- Gradiente del Espacio Intermembrana (EIM) -->
    <linearGradient id="boGradEIM" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#fed7aa" stop-opacity="0.75" />
      <stop offset="100%" stop-color="#ffedd5" stop-opacity="0.9" />
    </linearGradient>

    <!-- Gradiente de la Matriz Mitocondrial (ámbar cálido luminoso) -->
    <radialGradient id="boGradMatriz" cx="50%" cy="50%" r="75%">
      <stop offset="0%" stop-color="#fffbeb" stop-opacity="1" />
      <stop offset="45%" stop-color="#fef3c7" stop-opacity="0.95" />
      <stop offset="85%" stop-color="#fef9c3" stop-opacity="0.9" />
      <stop offset="100%" stop-color="#fef08a" stop-opacity="0.85" />
    </radialGradient>

    <!-- Gradiente de Cresta Mitocondrial -->
    <linearGradient id="boGradCresta" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fde68a" stop-opacity="0.95" />
      <stop offset="100%" stop-color="#fef3c7" stop-opacity="0.8" />
    </linearGradient>

    <!-- Gradiente de Bicapa Lipídica MMI -->
    <linearGradient id="boGradBicapa" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#fed7aa" stop-opacity="0.95" />
      <stop offset="50%" stop-color="#ffedd5" stop-opacity="0.9" />
      <stop offset="100%" stop-color="#fed7aa" stop-opacity="0.95" />
    </linearGradient>
"""

def generar_entorno_beta_oxidacion_svg(ancho=1000, alto=1750, y_mme=450, y_mmi_ini=560, y_mmi_fin=610):
    """Genera todas las capas biológicas subcelulares."""
    p = []

    # =========================================================================
    # CAPA 1: MATRIZ MITOCONDRIAL DE FONDO GENERAL
    # =========================================================================
    p.append(f'<rect x="0" y="0" width="{ancho}" height="{alto}" fill="url(#boGradMatriz)" />')

    # Crestas Mitocondriales Laterales Onduladas (Igual a Ciclo de Krebs)
    p.append(f"""
    <g fill="url(#boGradCresta)" stroke="#d97706" stroke-width="2" opacity="0.45">
      <!-- Crestas izquierdas (en matriz profunda) -->
      <path d="M 0 950 C 80 950, 95 990, 90 1040 C 85 1090, 50 1120, 0 1130 Z" />
      <path d="M 0 1450 C 90 1440, 105 1490, 95 1550 C 85 1600, 45 1630, 0 1640 Z" />

      <!-- Crestas derechas -->
      <path d="M {ancho} 850 C {ancho - 80} 850, {ancho - 95} 900, {ancho - 90} 960 C {ancho - 85} 1010, {ancho - 40} 1040, {ancho} 1050 Z" />
      <path d="M {ancho} 1350 C {ancho - 90} 1340, {ancho - 105} 1390, {ancho - 95} 1450 C {ancho - 85} 1500, {ancho - 45} 1530, {ancho} 1540 Z" />
    </g>
    """)

    # Ribosomas Mitocondriales (55S) y Gránulos densos
    p.append(f"""
    <g fill="#b45309" opacity="0.18">
      <circle cx="120" cy="880" r="2.8"/><circle cx="128" cy="882" r="2.2"/><circle cx="124" cy="888" r="2.5"/>
      <circle cx="140" cy="1320" r="2.8"/><circle cx="148" cy="1322" r="2.2"/><circle cx="144" cy="1328" r="2.5"/>
      <circle cx="{ancho - 120}" cy="980" r="2.8"/><circle cx="{ancho - 112}" cy="982" r="2.2"/>
      <circle cx="{ancho - 130}" cy="1520" r="2.8"/><circle cx="{ancho - 122}" cy="1522" r="2.2"/>
    </g>
    <g opacity="0.2">
      <ellipse cx="110" cy="1200" rx="7" ry="5" fill="#78350f" stroke="#92400e" stroke-width="1.2"/>
      <ellipse cx="{ancho - 110}" cy="1600" rx="7" ry="5" fill="#78350f" stroke="#92400e" stroke-width="1.2"/>
    </g>
    """)

    # =========================================================================
    # CAPA 2: CITOSOL CELULAR SUPERIOR
    # =========================================================================
    p.append(f"""
    <!-- Fondo acuoso del Citosol -->
    <path d="M 0 0 L {ancho} 0 L {ancho} {y_mme} Q {ancho/2} {y_mme + 10} 0 {y_mme} Z" fill="url(#boGradCitosol)"/>

    <!-- Microfilamentos de Citoesqueleto en el Citosol -->
    <g opacity="0.32" stroke="#94a3b8" fill="none">
      <path d="M 30 50 Q 250 25 500 65 T {ancho - 30} 40" stroke-width="1.5" stroke-dasharray="8 6"/>
      <path d="M 50 160 Q 320 190 600 150 T {ancho - 50} 180" stroke-width="1.4" stroke-dasharray="6 5"/>
      <path d="M 40 280 Q 280 240 550 290 T {ancho - 40} 270" stroke-width="1.5" stroke-dasharray="8 6"/>
    </g>

    <!-- Polirribosomas en Citosol -->
    <g fill="#94a3b8" opacity="0.25">
      <circle cx="90" cy="120" r="2.5"/><circle cx="96" cy="122" r="2"/><circle cx="94" cy="128" r="2.3"/>
      <circle cx="{ancho - 90}" cy="140" r="2.5"/><circle cx="{ancho - 84}" cy="142" r="2"/><circle cx="{ancho - 86}" cy="148" r="2.3"/>
      <circle cx="{ancho - 110}" cy="320" r="2.5"/><circle cx="{ancho - 104}" cy="322" r="2"/><circle cx="{ancho - 106}" cy="328" r="2.3"/>
    </g>

    <!-- Gota Lipídica Citosólica (Reserva de Triacilgliceroles que alimenta la vía) -->
    <g transform="translate(75, 75)" opacity="0.9">
      <ellipse cx="0" cy="0" rx="46" ry="38" fill="url(#boGradGotaLipidica)" stroke="#d97706" stroke-width="2.2" stroke-dasharray="6 3"/>
      <text x="0" y="-8" fill="#78350f" font-size="10" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">GOTA LIPÍDICA</text>
      <text x="0" y="6" fill="#92400e" font-size="8.5" font-weight="800" font-family="'JetBrains Mono', monospace" text-anchor="middle">TRIACILGLICEROLES</text>
      <text x="0" y="20" fill="#b45309" font-size="8" font-weight="700" font-family="'Inter', sans-serif" text-anchor="middle">Lipólisis (ATGL/HSL)</text>
      <!-- Flecha saliente de ácido graso libre -->
      <path d="M 40 18 Q 70 25 110 25" fill="none" stroke="#ea580c" stroke-width="2" marker-end="url(#arrowFlow)"/>
      <text x="85" y="15" fill="#ea580c" font-size="9" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">AG Libre</text>
    </g>

    <!-- Título de Zona Citosol -->
    <text x="35" y="32" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#166534" letter-spacing="1.5">
      CITOPLASMA CELULAR (CITOSOL) • ACTIVACIÓN DE ÁCIDOS GRASOS
    </text>
    """)

    # =========================================================================
    # CAPA 3: ENVOLTURA MITOCONDRIAL (MME, EIM, MMI)
    # =========================================================================
    # A) MME
    p.append(f"""
    <!-- Membrana Mitocondrial Externa (MME) Lisa Ondulada -->
    <path d="M 0 {y_mme} Q {ancho/2} {y_mme + 10} {ancho} {y_mme}" fill="none" stroke="#78350f" stroke-width="5" stroke-linecap="round"/>
    <path d="M 0 {y_mme + 2} Q {ancho/2} {y_mme + 12} {ancho} {y_mme + 2}" fill="none" stroke="#b45309" stroke-width="2" stroke-linecap="round"/>
    <text x="{ancho - 35}" y="{y_mme - 10}" font-family="'Inter', sans-serif" font-size="10" font-weight="800" fill="#78350f" text-anchor="end">
      Membrana Mitocondrial Externa (MME) • CPT-I
    </text>
    """)

    # B) EIM
    h_eim = y_mmi_ini - y_mme
    p.append(f"""
    <!-- Espacio Intermembrana (EIM) -->
    <path d="M 0 {y_mme + 4} Q {ancho/2} {y_mme + 14} {ancho} {y_mme + 4} L {ancho} {y_mmi_ini} Q {ancho/2} {y_mmi_ini + 10} 0 {y_mmi_ini} Z" fill="url(#boGradEIM)" />
    
    <!-- Protones acumulados en EIM -->
    <g font-family="'Inter', sans-serif" font-size="9.5" font-weight="900" fill="#ea580c" opacity="0.55">
      <text x="60" y="{y_mme + 30}">H⁺</text><text x="140" y="{y_mme + 32}">H⁺</text>
      <text x="500" y="{y_mme + 30}">H⁺</text><text x="580" y="{y_mme + 32}">H⁺</text>
    </g>
    <text x="{ancho - 35}" y="{y_mme + 30}" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#9a3412" letter-spacing="1" text-anchor="end">
      ESPACIO INTERMEMBRANA [EIM] • Tránsito de Palmitoilcarnitina
    </text>
    """)

    # C) MMI
    h_mmi = y_mmi_fin - y_mmi_ini
    p.append(f"""
    <!-- Membrana Mitocondrial Interna (MMI) - Bicapa Lipídica -->
    <path d="M 0 {y_mmi_ini} Q {ancho/2} {y_mmi_ini + 10} {ancho} {y_mmi_ini}" fill="none" stroke="#b45309" stroke-width="7" stroke-linecap="round"/>
    <path d="M 0 {y_mmi_fin} Q {ancho/2} {y_mmi_fin + 10} {ancho} {y_mmi_fin}" fill="none" stroke="#b45309" stroke-width="7" stroke-linecap="round"/>
    <path d="M 0 {y_mmi_ini + 3} Q {ancho/2} {y_mmi_ini + 13} {ancho} {y_mmi_ini + 3} L {ancho} {y_mmi_fin - 3} Q {ancho/2} {y_mmi_fin + 7} 0 {y_mmi_fin - 3} Z" fill="url(#boGradBicapa)"/>

    <text x="{ancho - 35}" y="{y_mmi_fin + 22}" font-family="'Inter', sans-serif" font-size="10" font-weight="800" fill="#92400e" text-anchor="end">
      Membrana Mitocondrial Interna (MMI) • CACT y CPT-II
    </text>
    """)

    # Cabezas de fosfolípidos en la bicapa MMI
    cabezas = []
    for x in range(35, ancho - 35, 40):
        cabezas.append(f'<circle cx="{x}" cy="{y_mmi_ini + 5}" r="3.2" fill="#d97706" opacity="0.85"/>')
        cabezas.append(f'<circle cx="{x}" cy="{y_mmi_fin - 5}" r="3.2" fill="#d97706" opacity="0.85"/>')
    p.append(f'<g>{ "".join(cabezas) }</g>')

    # Rótulo de la Matriz Mitocondrial
    p.append(f"""
    <text x="35" y="{y_mmi_fin + 65}" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#78350f" letter-spacing="1.5">
      MATRIZ MITOCONDRIAL • ESPIRAL DE LYNEN (β-OXIDACIÓN)
    </text>
    """)

    return "\n".join(p)
