# =============================================================================
# MÓDULO DE REVISIÓN: Entorno de Esqueletos Carbonados
# =============================================================================
# Archivo original : 04_NITROGENO_Y_AMINOACIDOS/via_12b_destinos_esqueletos_carbonados/entorno_destinos_aa.py (líneas 1 a 126 de 126)
# Descripción      : Lienzo para la convergencia de los 20 aminoácidos hacia el Ciclo de Krebs.
# =============================================================================

#!/usr/bin/env python3
"""
ENTORNO BIOLÓGICO CELULAR (SVG) - DESTINOS DE LOS ESQUELETOS CARBONADOS DE AMINOÁCIDOS
====================================================================================
Entorno bicompartimental continuo:
1. Citosol Hepatocitario / Celular (Zona Superior, Y=0 a Y=540)
2. Membrana Mitocondrial Ondulada Continua (Y=540 a Y=590)
3. Matriz Mitocondrial (Zona Inferior, Y=590 a Y=2240)
"""

DEFS_ENTORNO_DESTINOS_AA = """
    <!-- Gradiente de Fondo Citosol Acuoso -->
    <linearGradient id="gradCitosolAA" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#f8fafc" stop-opacity="1" />
      <stop offset="40%" stop-color="#f0fdf4" stop-opacity="0.85" />
      <stop offset="85%" stop-color="#f8fafc" stop-opacity="0.7" />
      <stop offset="100%" stop-color="#f1f5f9" stop-opacity="1" />
    </linearGradient>

    <!-- Gradiente de la Matriz Mitocondrial (Ámbar cálido editorial) -->
    <linearGradient id="gradMatrizAA" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#fffbeb" stop-opacity="0.95" />
      <stop offset="40%" stop-color="#fef3c7" stop-opacity="0.9" />
      <stop offset="80%" stop-color="#fef9c3" stop-opacity="0.85" />
      <stop offset="100%" stop-color="#fffbeb" stop-opacity="0.95" />
    </linearGradient>

    <!-- Gradiente de la Doble Membrana Mitocondrial -->
    <linearGradient id="gradMembranaMito" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#fb923c" stop-opacity="0.8" />
      <stop offset="50%" stop-color="#fed7aa" stop-opacity="0.5" />
      <stop offset="100%" stop-color="#ea580c" stop-opacity="0.85" />
    </linearGradient>

    <!-- Marcadores de Flechas Editoriales -->
    <marker id="arrowFlowAA" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
      <path d="M 0 0 L 6 3 L 0 6 Z" fill="#0284c7" />
    </marker>
    <marker id="arrowGreenAA" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
      <path d="M 0 0 L 6 3 L 0 6 Z" fill="#16a34a" />
    </marker>
    <marker id="arrowAmberAA" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
      <path d="M 0 0 L 6 3 L 0 6 Z" fill="#d97706" />
    </marker>
    <marker id="arrowRubyAA" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
      <path d="M 0 0 L 6 3 L 0 6 Z" fill="#e11d48" />
    </marker>
    <marker id="arrowPurpleAA" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
      <path d="M 0 0 L 6 3 L 0 6 Z" fill="#9333ea" />
    </marker>
    <marker id="arrowKrebsAA" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
      <path d="M 0 0 L 6 3 L 0 6 Z" fill="#7c3aed" />
    </marker>
    <marker id="arrowSlateAA" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
      <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#64748b" />
    </marker>
"""

def generar_entorno_destinos_aa_svg(ancho=1920, alto=2240, y_membrana=560):
    return f"""
    <!-- 1. FONDO CITOSÓLICO ACUOSO -->
    <rect x="0" y="0" width="{ancho}" height="{y_membrana}" fill="url(#gradCitosolAA)" />

    <!-- Filamentos sutiles en citosol (despejados) -->
    <g opacity="0.12" stroke="#94a3b8" fill="none">
      <path d="M 30 110 Q 450 80 950 120 T {ancho - 50} 100" stroke-width="1.8" stroke-dasharray="10 8" />
    </g>

    <!-- Rótulo Citosol (Esquina superior derecha despejada) -->
    <g opacity="0.8" transform="translate({ancho - 300}, 45)">
      <text x="0" y="0" font-family="'Inter', sans-serif" font-size="14" font-weight="900" fill="#0284c7" letter-spacing="1">CITOSOL CELULAR</text>
      <text x="0" y="16" font-family="'Inter', sans-serif" font-size="10" font-weight="600" fill="#64748b">Fase citoplasmática y transaminaciones</text>
    </g>

    <!-- 2. MEMBRANA MITOCONDRIAL ONDULADA -->
    <g class="membrana-mitocondrial">
      <!-- Espacio Intermembrana ondulado -->
      <path d="M 0 {y_membrana} 
               Q 450 {y_membrana - 15} 950 {y_membrana + 5} 
               T 1550 {y_membrana - 8} 
               T {ancho} {y_membrana} 
               L {ancho} {y_membrana + 34} 
               Q 1550 {y_membrana + 26} 950 {y_membrana + 39} 
               T 450 {y_membrana + 19} 
               T 0 {y_membrana + 34} Z" 
            fill="url(#gradMembranaMito)" opacity="0.65" />

      <!-- MME: Membrana Externa -->
      <path d="M 0 {y_membrana} 
               Q 450 {y_membrana - 15} 950 {y_membrana + 5} 
               T 1550 {y_membrana - 8} 
               T {ancho} {y_membrana}" 
            stroke="#ea580c" stroke-width="2.5" fill="none" opacity="0.85" />

      <!-- MMI: Membrana Interna -->
      <path d="M 0 {y_membrana + 34} 
               Q 450 {y_membrana + 19} 950 {y_membrana + 39} 
               T 1550 {y_membrana + 26} 
               T {ancho} {y_membrana + 34}" 
            stroke="#c2410c" stroke-width="2.5" fill="none" opacity="0.95" />

      <!-- Transportador MPC en X=210 -->
      <g transform="translate(190, {y_membrana + 4})">
        <ellipse cx="20" cy="13" rx="22" ry="14" fill="#ffedd5" stroke="#ea580c" stroke-width="2" />
        <text x="20" y="17" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#9a3412" text-anchor="middle">MPC</text>
      </g>

      <!-- Transportador AGC1 / GC1 en X=1720 -->
      <g transform="translate(1700, {y_membrana + 4})">
        <ellipse cx="26" cy="13" rx="24" ry="14" fill="#ede9fe" stroke="#7c3aed" stroke-width="2" />
        <text x="26" y="17" font-family="'Inter', sans-serif" font-size="8.5" font-weight="900" fill="#5b21b6" text-anchor="middle">AGC1</text>
      </g>

      <!-- Rótulo Membrana Mitocondrial en X=440 (zona central libre) -->
      <text x="440" y="{y_membrana + 22}" font-family="'Inter', sans-serif" font-size="10" font-weight="800" fill="#9a3412" letter-spacing="1">DOBLE MEMBRANA MITOCONDRIAL (MME / MMI)</text>
    </g>

    <!-- 3. MATRIZ MITOCONDRIAL -->
    <rect x="0" y="{y_membrana + 34}" width="{ancho}" height="{alto - (y_membrana + 34)}" fill="url(#gradMatrizAA)" />

    <!-- Rótulo Matriz Mitocondrial en zona central libre (X=440, Y=625) -->
    <g opacity="0.8" transform="translate(440, {y_membrana + 65})">
      <text x="0" y="0" font-family="'Inter', sans-serif" font-size="14" font-weight="900" fill="#b45309" letter-spacing="1">MATRIZ MITOCONDRIAL</text>
      <text x="0" y="16" font-family="'Inter', sans-serif" font-size="10" font-weight="600" fill="#78350f">Ciclo de Krebs, Complejo BCKDH y Vía Propionato</text>
    </g>
    """
