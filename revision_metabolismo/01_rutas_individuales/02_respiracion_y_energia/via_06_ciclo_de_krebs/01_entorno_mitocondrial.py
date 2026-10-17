# =============================================================================
# MÓDULO DE REVISIÓN: Entorno de la Matriz Mitocondrial
# =============================================================================
# Archivo original : 02_RESPIRACION_Y_ENERGIA/via_06_ciclo_de_krebs/entorno_mitocondrial.py (líneas 1 a 190 de 190)
# Descripción      : Doble membrana mitocondrial y espacio intermembrana para el Ciclo de Krebs.
# =============================================================================

#!/usr/bin/env python3
"""
DIBUJO DEL ENTORNO BIOLÓGICO MITOCONDRIAL (SVG) - COLUMNA VERTICAL EDITORIAL
=============================================================================
Formato vertical estricto (a juego con Glucólisis):
1. Arriba: Citosol celular con microfilamentos, VDAC (MME), EIM con gradiente H⁺ y MPC (MMI).
2. Centro y Fondo: Matriz Mitocondrial en gradiente ámbar cálido (#fffbeb / #fef3c7),
   con crestas laterales profundas, ADNmt circular y mitorribosomas.
3. Lateral derecho: Lupa de Aumento Molecular Científica del Complejo II (SDH) en la MMI.
"""

DEFS_ENTORNO_MITOCONDRIAL = """
    <!-- Gradiente del Citosol (arriba) -->
    <linearGradient id="gradCitosol" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#f8fafc" stop-opacity="1" />
      <stop offset="100%" stop-color="#e2e8f0" stop-opacity="0.95" />
    </linearGradient>

    <!-- Gradiente del Espacio Intermembrana (EIM) -->
    <linearGradient id="gradEIM" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#fed7aa" stop-opacity="0.75" />
      <stop offset="100%" stop-color="#ffedd5" stop-opacity="0.9" />
    </linearGradient>

    <!-- Gradiente de la Matriz Mitocondrial (ámbar cálido y luminoso) -->
    <radialGradient id="gradMatrizMitocondrial" cx="50%" cy="50%" r="70%">
      <stop offset="0%" stop-color="#fffbeb" stop-opacity="1" />
      <stop offset="45%" stop-color="#fef3c7" stop-opacity="0.95" />
      <stop offset="85%" stop-color="#fef9c3" stop-opacity="0.9" />
      <stop offset="100%" stop-color="#fef08a" stop-opacity="0.85" />
    </radialGradient>

    <!-- Gradiente de Cresta Mitocondrial -->
    <linearGradient id="gradCresta" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fde68a" stop-opacity="0.95" />
      <stop offset="100%" stop-color="#fef3c7" stop-opacity="0.8" />
    </linearGradient>
"""

def generar_entorno_mitocondrial_svg(ancho=1150, alto=2450, y_mme=95, y_mmi=155):
    """Genera todo el código SVG del fondo mitocondrial para el lienzo vertical."""
    return f"""
    <!-- ================================================================= -->
    <!-- CAPA 1: MATRIZ MITOCONDRIAL DE FONDO                              -->
    <!-- ================================================================= -->
    <rect x="0" y="0" width="{ancho}" height="{alto}" fill="url(#gradMatrizMitocondrial)" />

    <!-- ================================================================= -->
    <!-- CAPA 2: ULTRAESTRUCTURA DE LA MATRIZ (CRESTAS, ADNmt, RIBOSOMAS)  -->
    <!-- ================================================================= -->

    <!-- Crestas Mitocondriales Laterales (Invaginaciones onduladas) -->
    <g fill="url(#gradCresta)" stroke="#d97706" stroke-width="2" opacity="0.55">
      <!-- Crestas izquierdas -->
      <path d="M 0 360 C 90 360, 110 400, 110 450 C 110 500, 80 530, 0 530 Z" />
      <path d="M 0 850 C 100 850, 120 900, 115 960 C 110 1020, 70 1050, 0 1050 Z" />
      <path d="M 0 1420 C 110 1410, 130 1470, 120 1540 C 110 1600, 60 1630, 0 1640 Z" />
      <path d="M 0 1950 C 90 1950, 120 2000, 110 2060 C 100 2110, 50 2140, 0 2150 Z" />

      <!-- Crestas derechas -->
      <path d="M {ancho} 580 C {ancho - 110} 580, {ancho - 130} 630, {ancho - 120} 690 C {ancho - 110} 750, {ancho - 60} 780, {ancho} 790 Z" />
      <path d="M {ancho} 1220 C {ancho - 120} 1210, {ancho - 140} 1270, {ancho - 130} 1340 C {ancho - 120} 1400, {ancho - 60} 1430, {ancho} 1440 Z" />
      <path d="M {ancho} 1820 C {ancho - 110} 1810, {ancho - 140} 1870, {ancho - 130} 1940 C {ancho - 120} 2000, {ancho - 50} 2030, {ancho} 2040 Z" />

      <!-- Cresta inferior de cierre -->
      <path d="M 250 {alto} C 300 {alto - 70}, 420 {alto - 90}, 500 {alto - 60} C 560 {alto - 30}, 600 {alto}, 600 {alto} Z" />
    </g>

    <!-- Ribosomas Mitocondriales (55S) -->
    <g fill="#b45309" opacity="0.2">
      <circle cx="160" cy="420" r="2.8"/><circle cx="168" cy="422" r="2.2"/><circle cx="164" cy="428" r="2.5"/>
      <circle cx="180" cy="1120" r="2.8"/><circle cx="188" cy="1122" r="2.2"/><circle cx="184" cy="1128" r="2.5"/>
      <circle cx="170" cy="1780" r="2.8"/><circle cx="178" cy="1782" r="2.2"/><circle cx="174" cy="1788" r="2.5"/>
      <circle cx="{ancho - 180}" cy="880" r="2.8"/><circle cx="{ancho - 172}" cy="882" r="2.2"/>
      <circle cx="{ancho - 190}" cy="1620" r="2.8"/><circle cx="{ancho - 182}" cy="1622" r="2.2"/>
    </g>

    <!-- Gránulos densos de Ca²⁺ / Mg²⁺ -->
    <g opacity="0.25">
      <ellipse cx="140" cy="680" rx="8" ry="6" fill="#78350f" stroke="#92400e" stroke-width="1.3"/>
      <ellipse cx="130" cy="1320" rx="8" ry="6" fill="#78350f" stroke="#92400e" stroke-width="1.3"/>
      <ellipse cx="140" cy="1890" rx="8" ry="6" fill="#78350f" stroke="#92400e" stroke-width="1.3"/>
    </g>

    <!-- ADN Mitocondrial (ADNmt circular) -->
    <g fill="none" stroke="#b45309" stroke-width="1.2" opacity="0.2">
      <path d="M 60 1200 C 80 1180, 110 1190, 105 1215 C 100 1240, 70 1250, 55 1230 Z" stroke-dasharray="3 2"/>
      <path d="M {ancho - 90} 1680 C {ancho - 70} 1660, {ancho - 40} 1670, {ancho - 45} 1695 C {ancho - 50} 1720, {ancho - 80} 1730, {ancho - 95} 1710 Z" stroke-dasharray="3 2"/>
    </g>


    <!-- ================================================================= -->
    <!-- CAPA 3: ENVOLTURA MITOCONDRIAL SUPERIOR                           -->
    <!-- ================================================================= -->

    <!-- A) Citosol Celular Superior -->
    <path d="M 0 0 L {ancho} 0 L {ancho} {y_mme} Q {ancho/2} {y_mme + 6} 0 {y_mme} Z" fill="url(#gradCitosol)" />
    
    <!-- Microfilamentos del citoesqueleto en citosol -->
    <g opacity="0.32" stroke="#94a3b8" fill="none">
      <path d="M 30 22 Q 300 8 600 24 T {ancho - 30} 18" stroke-width="1.5" stroke-dasharray="8 6"/>
      <path d="M 60 44 Q 380 58 720 40 T {ancho - 60} 48" stroke-width="1.3" stroke-dasharray="6 5"/>
    </g>
    <text x="35" y="24" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#64748b" letter-spacing="1.5">CITOPLASMA CELULAR (CITOSOL ACUOSO)</text>

    <!-- B) Membrana Mitocondrial Externa (MME) Lisa Ondulada -->
    <path d="M 0 {y_mme} Q {ancho/2} {y_mme + 6} {ancho} {y_mme}" fill="none" stroke="#78350f" stroke-width="6" stroke-linecap="round"/>
    <path d="M 0 {y_mme + 3} Q {ancho/2} {y_mme + 9} {ancho} {y_mme + 3}" fill="none" stroke="#b45309" stroke-width="2.2" stroke-linecap="round"/>
    <text x="{ancho - 290}" y="{y_mme - 8}" font-family="'Inter', sans-serif" font-size="9.5" font-weight="700" fill="#78350f">Membrana Mitocondrial Externa (MME)</text>

    <!-- Porina VDAC en la MME -->
    <g transform="translate(410, {y_mme - 10})">
      <rect x="0" y="0" width="36" height="22" rx="5" fill="#f97316" stroke="#c2410c" stroke-width="1.8"/>
      <ellipse cx="18" cy="11" rx="8" ry="5" fill="#e0f2fe" stroke="#38bdf8" stroke-width="1.2"/>
      <text x="18" y="28" font-family="'JetBrains Mono', monospace" font-size="8" font-weight="900" fill="#9a3412" text-anchor="middle">VDAC</text>
    </g>

    <!-- C) Espacio Intermembrana (EIM) -->
    <path d="M 0 {y_mme + 6} Q {ancho/2} {y_mme + 12} {ancho} {y_mme + 6} L {ancho} {y_mmi} Q {ancho/2} {y_mmi + 6} 0 {y_mmi} Z" fill="url(#gradEIM)" />
    <!-- Protones H+ acumulados en EIM -->
    <g font-family="'Inter', sans-serif" font-size="9.5" font-weight="900" fill="#ea580c" opacity="0.6">
      <text x="320" y="{y_mme + 38}">H⁺</text><text x="440" y="{y_mme + 42}">H⁺</text>
      <text x="560" y="{y_mme + 39}">H⁺</text><text x="680" y="{y_mme + 43}">H⁺</text>
      <text x="860" y="{y_mme + 40}">H⁺</text><text x="980" y="{y_mme + 44}">H⁺</text>
    </g>
    <text x="35" y="{y_mme + 42}" font-family="'Inter', sans-serif" font-size="9.5" font-weight="800" fill="#9a3412" letter-spacing="1">ESPACIO INTERMEMBRANA [GRADIENTE H⁺]</text>

    <!-- D) Membrana Mitocondrial Interna (MMI) Impermeable -->
    <path d="M 0 {y_mmi} Q {ancho/2} {y_mmi + 6} {ancho} {y_mmi}" fill="none" stroke="#b45309" stroke-width="7" stroke-linecap="round"/>
    <path d="M 0 {y_mmi + 4} Q {ancho/2} {y_mmi + 10} {ancho} {y_mmi + 4}" fill="none" stroke="#f59e0b" stroke-width="2.2" stroke-linecap="round"/>
    <text x="{ancho - 360}" y="{y_mmi + 22}" font-family="'Inter', sans-serif" font-size="9.5" font-weight="800" fill="#92400e">Membrana Mitocondrial Interna (MMI)</text>

    <!-- Transportador MPC en la MMI -->
    <g transform="translate(400, {y_mmi - 12})">
      <rect x="0" y="0" width="56" height="28" rx="6" fill="#b45309" stroke="#78350f" stroke-width="2"/>
      <line x1="28" y1="0" x2="28" y2="28" stroke="#78350f" stroke-width="1.6" stroke-dasharray="3 2"/>
      <ellipse cx="28" cy="14" rx="8" ry="7" fill="#fef3c7" stroke="#d97706" stroke-width="1.4"/>
      <text x="28" y="18" font-family="'JetBrains Mono', monospace" font-size="9.5" font-weight="900" fill="#78350f" text-anchor="middle">MPC</text>
    </g>


    <!-- ================================================================= -->
    <!-- CAPA 4: LUPA MOLECULAR CIENTÍFICA (LATERAL DERECHO SUPERIOR)      -->
    <!-- ================================================================= -->
    <g transform="translate({ancho - 180}, 330)">
      <circle cx="0" cy="0" r="95" fill="#ffffff" stroke="#b45309" stroke-width="4" filter="drop-shadow(0 12px 22px rgba(0,0,0,0.16))"/>
      <circle cx="0" cy="0" r="90" fill="#fffbeb" stroke="#fef3c7" stroke-width="1.5" />

      <!-- Bicapa lipídica ampliada de la MMI -->
      <g opacity="0.9">
        <g fill="#b45309">
          <circle cx="-75" cy="-30" r="4.5"/><circle cx="-60" cy="-30" r="4.5"/><circle cx="-45" cy="-30" r="4.5"/>
          <circle cx="45" cy="-30" r="4.5"/><circle cx="60" cy="-30" r="4.5"/><circle cx="75" cy="-30" r="4.5"/>
          <circle cx="-75" cy="8" r="4.5"/><circle cx="-60" cy="8" r="4.5"/><circle cx="-45" cy="8" r="4.5"/>
          <circle cx="45" cy="8" r="4.5"/><circle cx="60" cy="8" r="4.5"/><circle cx="75" cy="8" r="4.5"/>
        </g>
        <g stroke="#d97706" stroke-width="1.2" fill="none">
          <path d="M -75 -25 Q -77 -16 -73 -9"/><path d="M -60 -25 Q -62 -16 -58 -9"/><path d="M -45 -25 Q -47 -16 -43 -9"/>
          <path d="M 45 -25 Q 43 -16 47 -9"/><path d="M 60 -25 Q 58 -16 62 -9"/><path d="M 75 -25 Q 73 -16 77 -9"/>
          <path d="M -75 4 Q -77 -5 -73 -9"/><path d="M -60 4 Q -62 -5 -58 -9"/><path d="M -45 4 Q -47 -5 -43 -9"/>
          <path d="M 45 4 Q 43 -5 47 -9"/><path d="M 60 4 Q 58 -5 62 -9"/><path d="M 75 4 Q 73 -5 77 -9"/>
        </g>
      </g>

      <!-- Subunidades hidrofóbicas transmembrana (SDHC / SDHD con Hemo b) -->
      <path d="M -36 -36 C -32 -40, 32 -40, 36 -36 C 40 -10, 38 10, 34 16 C 18 19, -18 19, -34 16 C -38 10, -40 -10, -36 -36 Z" fill="#0284c7" stroke="#0369a1" stroke-width="1.8"/>
      <text x="0" y="-13" font-family="'Inter', sans-serif" font-size="7.5" font-weight="900" fill="#ffffff" text-anchor="middle">SDHC / SDHD</text>
      <circle cx="0" cy="0" r="5" fill="#dc2626" stroke="#991b1b" stroke-width="1"/>
      <text x="0" y="3" font-family="'JetBrains Mono', monospace" font-size="5" font-weight="900" fill="#ffffff" text-anchor="middle">Hemo b</text>

      <!-- Subunidad hidrofílica SDHB (Centros [Fe-S]) -->
      <ellipse cx="0" cy="30" rx="30" ry="14" fill="#10b981" stroke="#047857" stroke-width="1.8"/>
      <text x="0" y="28" font-family="'Inter', sans-serif" font-size="8" font-weight="900" fill="#ffffff" text-anchor="middle">SDHB [Fe-S]</text>
      <text x="0" y="39" font-family="'JetBrains Mono', monospace" font-size="5.5" font-weight="700" fill="#064e3b" text-anchor="middle">[2Fe-2S]➔[4Fe-4S]➔[3Fe-4S]</text>

      <!-- Subunidad catalítica SDHA (FAD y sitio de Succinato) -->
      <ellipse cx="0" cy="58" rx="36" ry="15" fill="#f59e0b" stroke="#b45309" stroke-width="1.8"/>
      <text x="0" y="56" font-family="'Inter', sans-serif" font-size="8.5" font-weight="900" fill="#78350f" text-anchor="middle">SDHA (Flavoproteína)</text>
      <text x="0" y="66" font-family="'JetBrains Mono', monospace" font-size="6" font-weight="800" fill="#92400e" text-anchor="middle">FAD ➔ FADH₂</text>

      <!-- Reducción de Ubiquinona -->
      <path d="M 32 -6 Q 54 -16 64 -2" fill="none" stroke="#059669" stroke-width="1.8" marker-end="url(#arrowGreen)"/>
      <text x="68" y="-10" font-family="'JetBrains Mono', monospace" font-size="7" font-weight="800" fill="#047857">Q ➔ QH₂</text>

      <!-- Rótulos de la lupa -->
      <rect x="-80" y="-74" width="160" height="20" rx="4" fill="#0f172a" opacity="0.9"/>
      <text x="0" y="-60" font-family="'Inter', sans-serif" font-size="8" font-weight="800" fill="#ffffff" text-anchor="middle" letter-spacing="0.5">COMPLEJO II (SDH) EN MMI</text>
      <text x="0" y="-80" font-family="'JetBrains Mono', monospace" font-size="6.5" font-weight="700" fill="#b45309" text-anchor="middle">ÚNICA ENZIMA INTEGRAL DE MEMBRANA</text>
    </g>
    """
