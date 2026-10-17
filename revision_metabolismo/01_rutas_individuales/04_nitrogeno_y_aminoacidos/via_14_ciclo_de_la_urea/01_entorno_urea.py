# =============================================================================
# MÓDULO DE REVISIÓN: Entorno del Ciclo de la Urea
# =============================================================================
# Archivo original : 04_NITROGENO_Y_AMINOACIDOS/via_14_ciclo_de_la_urea/entorno_urea.py (líneas 1 a 135 de 135)
# Descripción      : Matriz mitocondrial, citosol y transportadores ORNT1 / Citrina.
# =============================================================================

#!/usr/bin/env python3
"""
ENTORNO BIOLÓGICO HEPATOCITARIO - CICLO DE LA UREA (SVG)
========================================================
Compartimentos biológicos alineados con la topología de ciclo limpia:
1. Matriz Mitocondrial (Parte superior, Y=0 a Y=620).
2. Membrana Mitocondrial Interna (MMI, Y=620):
   - Transportador Citrina (SLC25A13) en X=440.
   - Transportador ORNT1 (SLC25A15) en X=700 (alineado al carril de retorno X=730).
3. Citosol Hepatocitario (Parte inferior, Y=620 a Y=2200).
4. Capilar Sanguíneo Hepático centrado abajo (Y=2030).
"""

DEFS_ENTORNO_UREA = """
    <!-- Gradiente de la Matriz Mitocondrial (Ámbar cálido editorial) -->
    <linearGradient id="gradMatrizUrea" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#fef3c7" stop-opacity="0.95" />
      <stop offset="60%" stop-color="#fffbeb" stop-opacity="0.9" />
      <stop offset="100%" stop-color="#fef9c3" stop-opacity="0.8" />
    </linearGradient>

    <!-- Gradiente Citosol Acuoso -->
    <linearGradient id="gradCitosolUrea" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#f8fafc" stop-opacity="1" />
      <stop offset="15%" stop-color="#f0fdfa" stop-opacity="0.85" />
      <stop offset="70%" stop-color="#f8fafc" stop-opacity="0.6" />
      <stop offset="100%" stop-color="#f1f5f9" stop-opacity="1" />
    </linearGradient>

    <!-- Gradiente Vascular Renal / Sanguíneo -->
    <linearGradient id="gradVascularUrea" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#fee2e2" stop-opacity="0.9" />
      <stop offset="100%" stop-color="#fecaca" stop-opacity="0.95" />
    </linearGradient>

    <!-- Marcadores de Flechas Editoriales -->
    <marker id="arrowFlow" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
      <path d="M 0 0 L 6 3 L 0 6 Z" fill="#0d9488" />
    </marker>
    <marker id="arrowOrange" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
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
    <marker id="arrowCobalt" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
      <path d="M 0 0 L 6 3 L 0 6 Z" fill="#2563eb" />
    </marker>
"""

def generar_entorno_urea_svg(ancho=1150, alto=2200, y_membrana=620):
    return f"""
    <!-- ================================================================= -->
    <!-- 1. FONDO CITOSÓLICO COMPLETO                                      -->
    <!-- ================================================================= -->
    <rect x="0" y="0" width="{ancho}" height="{alto}" fill="url(#gradCitosolUrea)" />

    <!-- Citoesqueleto y microtúbulos en citosol -->
    <g opacity="0.22" stroke="#94a3b8" fill="none">
      <path d="M 30 850 Q 300 800 650 860 T {ancho - 40} 830" stroke-width="1.6" stroke-dasharray="8 6" />
      <path d="M 40 1200 Q 350 1260 700 1210 T {ancho - 40} 1240" stroke-width="1.5" stroke-dasharray="7 6" />
      <path d="M 30 1650 Q 300 1590 620 1660 T {ancho - 40} 1620" stroke-width="1.5" stroke-dasharray="8 5" />
    </g>

    <!-- ================================================================= -->
    <!-- 2. MATRIZ MITOCONDRIAL (PARTE SUPERIOR: Y=0 a Y={y_membrana})     -->
    <!-- ================================================================= -->
    <path d="M 0 0 L {ancho} 0 L {ancho} {y_membrana} Q 600 {y_membrana + 25} 0 {y_membrana} Z" fill="url(#gradMatrizUrea)" stroke="#b45309" stroke-width="3"/>
    
    <!-- Ribete de membrana externa y crestas decorativas suaves -->
    <path d="M 60 110 C 130 65, 160 135, 230 85" fill="none" stroke="#d97706" stroke-width="2" opacity="0.35"/>
    <path d="M {ancho - 220} 105 C {ancho - 150} 55, {ancho - 120} 125, {ancho - 50} 75" fill="none" stroke="#d97706" stroke-width="2" opacity="0.35"/>

    <!-- Título de la Matriz Mitocondrial (sin recuadros) -->
    <g transform="translate(50, 42)">
      <text x="0" y="0" font-family="'Inter', sans-serif" font-size="14" font-weight="900" fill="#92400e" letter-spacing="2">MATRIZ MITOCONDRIAL</text>
      <text x="0" y="18" font-family="'Inter', sans-serif" font-size="10.5" font-weight="700" fill="#b45309">Fase 1: Fijación de Amonio y Formación de Citrulina</text>
    </g>

    <!-- ================================================================= -->
    <!-- 3. MEMBRANA MITOCONDRIAL INTERNA (MMI) Y TRANSPORTADORES          -->
    <!-- ================================================================= -->
    <g transform="translate(0, {y_membrana})">
      <!-- Bicapa lipídica representada con doble trazo suave -->
      <path d="M 0 0 Q 600 25 {ancho} 0" fill="none" stroke="#ea580c" stroke-width="8" opacity="0.75" stroke-linecap="round"/>
      <path d="M 0 10 Q 600 35 {ancho} 10" fill="none" stroke="#fed7aa" stroke-width="4" opacity="0.9" stroke-linecap="round"/>
      <path d="M 0 20 Q 600 45 {ancho} 20" fill="none" stroke="#ea580c" stroke-width="8" opacity="0.75" stroke-linecap="round"/>

      <!-- Etiqueta de la MMI -->
      <g transform="translate(50, 26)">
        <text x="0" y="0" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#c2410c">MEMBRANA MITOCONDRIAL INTERNA (MMI)</text>
      </g>

      <!-- TRANSPORTADOR 1: CITRINA / SLC25A13 (Salida de Citrulina en X=440) -->
      <g transform="translate(420, -12)">
        <rect x="0" y="0" width="80" height="42" rx="10" fill="#0d9488" stroke="#0f766e" stroke-width="2"/>
        <text x="40" y="18" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#ffffff" text-anchor="middle">SLC25A13</text>
        <text x="40" y="32" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="800" fill="#ccfbf1" text-anchor="middle">Citrina</text>
      </g>

      <!-- TRANSPORTADOR 2: ORNT1 / SLC25A15 (Retorno de Ornitina en X=820) -->
      <g transform="translate(780, -12)">
        <rect x="0" y="0" width="80" height="42" rx="10" fill="#2563eb" stroke="#1d4ed8" stroke-width="2"/>
        <text x="40" y="18" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#ffffff" text-anchor="middle">SLC25A15</text>
        <text x="40" y="32" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="800" fill="#eff6ff" text-anchor="middle">ORNT1</text>
      </g>
    </g>

    <!-- ================================================================= -->
    <!-- 4. CITOSOL HEPATOCITARIO (PARTE INFERIOR)                         -->
    <!-- ================================================================= -->
    <!-- Título del Citosol (sin recuadros) -->
    <g transform="translate(50, {y_membrana + 55})">
      <text x="0" y="0" font-family="'Inter', sans-serif" font-size="14" font-weight="900" fill="#0284c7" letter-spacing="2">CITOSOL HEPATOCITARIO</text>
      <text x="0" y="18" font-family="'Inter', sans-serif" font-size="10.5" font-weight="700" fill="#64748b">Fase 2: Incorporación de Aspartato, Arginina y Excreción</text>
    </g>

    <!-- Lecho Vascular / Torrente Sanguíneo (sin cajas artificiales) -->
    <path d="M 0 {alto - 75} Q {ancho / 2} {alto - 95} {ancho} {alto - 75} L {ancho} {alto} L 0 {alto} Z" fill="url(#gradVascularUrea)" stroke="#dc2626" stroke-width="2.5" opacity="0.9"/>
    <!-- Glóbulos rojos tenues en el capilar -->
    <g opacity="0.6">
      <ellipse cx="{ancho * 0.2}" cy="{alto - 35}" rx="18" ry="10" fill="#ef4444" stroke="#7f1d1d" stroke-width="1.2" transform="rotate(-8, {ancho * 0.2}, {alto - 35})"/>
      <ellipse cx="{ancho * 0.8}" cy="{alto - 40}" rx="20" ry="11" fill="#ef4444" stroke="#7f1d1d" stroke-width="1.2" transform="rotate(12, {ancho * 0.8}, {alto - 40})"/>
    </g>
    <text x="{ancho / 2}" y="{alto - 30}" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#991b1b" text-anchor="middle" letter-spacing="1">TORRENTE SANGUÍNEO • EXCRECIÓN RENAL</text>
    """
