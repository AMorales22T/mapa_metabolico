# =============================================================================
# MÓDULO DE REVISIÓN: Entorno Celular de Lipogénesis de Novo
# =============================================================================
# Archivo original : 03_LIPIDOS/via_10_lipogenesis/entorno_lipogenesis.py (líneas 1 a 126 de 126)
# Descripción      : Compartimentos celulares para Lipogénesis de Novo.
# =============================================================================

#!/usr/bin/env python3
"""
ENTORNO BIOLÓGICO Y COMPARTIMENTAL - LIPOGÉNESIS (SÍNTESIS DE ÁCIDOS GRASOS)
=============================================================================
Escenario biológico integrado:
1. MATRIZ MITOCONDRIAL (Arriba, y=0 a 220):
   - Origen del Citrato (exceso de Acetil-CoA + Oxalacetato en el Ciclo de Krebs).
   - Fondo ámbar cálido con crestas mitocondriales superiores.
2. MEMBRANA MITOCONDRIAL INTERNA (MMI) Y LANZADERA DEL CITRATO (y=220 a 270):
   - Bicapa fosfolipídica con el transportador de tricarboxilatos (SLC25A1).
3. CITOPLASMA CELULAR / CITOSOL (Medio y Abajo, y=270 a 2100):
   - Escenario principal de la síntesis de ácidos grasos.
   - Microfilamentos, polirribosomas.
   - Complejo de la Ácido Graso Sintasa (FASN) libre en citosol.
   - Destino final hacia esterificación y formación de triacilgliceroles / gota lipídica.
"""

DEFS_ENTORNO_LIPOGENESIS = """
    <!-- Gradiente de la Matriz Mitocondrial (arriba) -->
    <linearGradient id="lipoGradMatriz" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#fffbeb" stop-opacity="1" />
      <stop offset="70%" stop-color="#fef3c7" stop-opacity="0.95" />
      <stop offset="100%" stop-color="#fef08a" stop-opacity="0.9" />
    </linearGradient>

    <!-- Gradiente de Bicapa MMI -->
    <linearGradient id="lipoGradBicapa" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#fed7aa" stop-opacity="0.95" />
      <stop offset="50%" stop-color="#ffedd5" stop-opacity="0.9" />
      <stop offset="100%" stop-color="#fed7aa" stop-opacity="0.95" />
    </linearGradient>

    <!-- Gradiente del Citosol Celular -->
    <linearGradient id="lipoGradCitosol" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#f8fafc" stop-opacity="1" />
      <stop offset="100%" stop-color="#f0fdf4" stop-opacity="0.85" />
    </linearGradient>

    <!-- Gradiente de Gota Lipídica / Reserva TAG -->
    <radialGradient id="lipoGradGota" cx="40%" cy="40%" r="60%">
      <stop offset="0%" stop-color="#fef08a" stop-opacity="0.9" />
      <stop offset="70%" stop-color="#f59e0b" stop-opacity="0.6" />
      <stop offset="100%" stop-color="#d97706" stop-opacity="0.8" />
    </radialGradient>
"""

def generar_entorno_lipogenesis_svg(ancho=1000, alto=2150, y_mmi_ini=220, y_mmi_fin=265):
    """Genera el fondo biológico compartimental."""
    p = []

    # 1. Fondo completo de Citosol (desde 0 hasta alto)
    p.append(f'<rect x="0" y="0" width="{ancho}" height="{alto}" fill="url(#lipoGradCitosol)" />')

    # Microfilamentos del citoesqueleto en citosol
    p.append(f"""
    <g opacity="0.3" stroke="#94a3b8" fill="none">
      <path d="M 30 350 Q 300 320 600 370 T {ancho - 30} 340" stroke-width="1.5" stroke-dasharray="8 6"/>
      <path d="M 50 680 Q 350 720 650 660 T {ancho - 50} 700" stroke-width="1.4" stroke-dasharray="6 5"/>
      <path d="M 40 1100 Q 280 1060 580 1120 T {ancho - 40} 1080" stroke-width="1.5" stroke-dasharray="8 6"/>
      <path d="M 60 1520 Q 380 1560 700 1500 T {ancho - 60} 1540" stroke-width="1.4" stroke-dasharray="7 5"/>
      <path d="M 30 1900 Q 300 1860 620 1920 T {ancho - 30} 1890" stroke-width="1.5" stroke-dasharray="8 6"/>
    </g>

    <!-- Polirribosomas citosólicos -->
    <g fill="#94a3b8" opacity="0.25">
      <circle cx="90" cy="420" r="2.5"/><circle cx="96" cy="422" r="2"/><circle cx="94" cy="428" r="2.3"/>
      <circle cx="{ancho - 90}" cy="560" r="2.5"/><circle cx="{ancho - 84}" cy="562" r="2"/><circle cx="{ancho - 86}" cy="568" r="2.3"/>
      <circle cx="110" cy="1250" r="2.5"/><circle cx="116" cy="1252" r="2"/>
      <circle cx="{ancho - 110}" cy="1720" r="2.5"/><circle cx="{ancho - 104}" cy="1722" r="2"/>
    </g>
    """)

    # 2. Cúpula superior: Matriz Mitocondrial (origen del citrato)
    p.append(f"""
    <!-- Matriz Mitocondrial Superior -->
    <path d="M 0 0 L {ancho} 0 L {ancho} {y_mmi_ini} Q {ancho/2} {y_mmi_ini + 10} 0 {y_mmi_ini} Z" fill="url(#lipoGradMatriz)" />
    
    <!-- Cresta mitocondrial superior decorativa -->
    <g fill="none" stroke="#d97706" stroke-width="1.8" opacity="0.35">
      <path d="M 80 0 C 80 60, 140 90, 140 140 C 140 170, 110 190, 80 190" stroke-dasharray="6 4"/>
      <path d="M {ancho - 80} 0 C {ancho - 80} 60, {ancho - 140} 90, {ancho - 140} 140 C {ancho - 140} 170, {ancho - 110} 190, {ancho - 80} 190" stroke-dasharray="6 4"/>
    </g>

    <text x="35" y="32" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#78350f" letter-spacing="1.5">
      MATRIZ MITOCONDRIAL • ORIGEN DEL CITRATO (EXCESO ENERGÉTICO)
    </text>
    """)

    # 3. Membrana Mitocondrial Interna (MMI) - Bicapa lipídica
    p.append(f"""
    <!-- Bicapa MMI -->
    <path d="M 0 {y_mmi_ini} Q {ancho/2} {y_mmi_ini + 10} {ancho} {y_mmi_ini}" fill="none" stroke="#b45309" stroke-width="7" stroke-linecap="round"/>
    <path d="M 0 {y_mmi_fin} Q {ancho/2} {y_mmi_fin + 10} {ancho} {y_mmi_fin}" fill="none" stroke="#b45309" stroke-width="7" stroke-linecap="round"/>
    <path d="M 0 {y_mmi_ini + 3} Q {ancho/2} {y_mmi_ini + 13} {ancho} {y_mmi_ini + 3} L {ancho} {y_mmi_fin - 3} Q {ancho/2} {y_mmi_fin + 7} 0 {y_mmi_fin - 3} Z" fill="url(#lipoGradBicapa)"/>

    <text x="{ancho - 35}" y="{y_mmi_fin + 20}" font-family="'Inter', sans-serif" font-size="10" font-weight="800" fill="#92400e" text-anchor="end">
      Membrana Mitocondrial Interna (MMI) • Lanzadera del Citrato (SLC25A1)
    </text>
    """)

    # Cabezas de fosfolípidos en la bicapa MMI
    cabezas = []
    for x in range(35, ancho - 35, 40):
        cabezas.append(f'<circle cx="{x}" cy="{y_mmi_ini + 5}" r="3.2" fill="#d97706" opacity="0.85"/>')
        cabezas.append(f'<circle cx="{x}" cy="{y_mmi_fin - 5}" r="3.2" fill="#d97706" opacity="0.85"/>')
    p.append(f'<g>{ "".join(cabezas) }</g>')

    # 4. Rótulo del Citoplasma Celular
    p.append(f"""
    <text x="35" y="{y_mmi_fin + 24}" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#166534" letter-spacing="1.5">
      CITOPLASMA CELULAR (CITOSOL) • SÍNTESIS DE ÁCIDOS GRASOS (FASN)
    </text>
    """)

    # 5. Gota Lipídica / Destino de los Ácidos Grasos al final (abajo a la derecha)
    p.append(f"""
    <!-- Gota Lipídica receptora en citosol (y=1950) -->
    <g transform="translate({ancho - 110}, 1980)" opacity="0.95">
      <ellipse cx="0" cy="0" rx="60" ry="48" fill="url(#lipoGradGota)" stroke="#d97706" stroke-width="2.4" stroke-dasharray="6 3"/>
      <text x="0" y="-12" fill="#78350f" font-size="10.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">GOTA LIPÍDICA</text>
      <text x="0" y="4" fill="#92400e" font-size="9" font-weight="800" font-family="'JetBrains Mono', monospace" text-anchor="middle">TRIACILGLICEROLES</text>
      <text x="0" y="20" fill="#b45309" font-size="8.5" font-weight="700" font-family="'Inter', sans-serif" text-anchor="middle">Esterificación (DGAT)</text>
    </g>
    """)

    return "\n".join(p)
