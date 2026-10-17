# =============================================================================
# MÓDULO DE REVISIÓN: Entorno de Catabolismo de Nucleótidos
# =============================================================================
# Archivo original : 05_NUCLEOTIDOS_Y_OTRAS/via_16_degradacion_y_acido_urico/entorno_degradacion.py (líneas 1 a 49 de 49)
# Descripción      : Citosol y excreción vascular hacia riñón.
# =============================================================================

#!/usr/bin/env python3
"""
ENTORNO BIOLÓGICO CELULAR (SVG) - CATABOLISMO DE NUCLEÓTIDOS Y EXCRECIÓN DE URATO
================================================================================
Fondo orgánico para la degradación de Purinas y Pirimidinas:
1. Fondo celular citosólico (#f8fafc -> #fef2f2 en la zona de acumulación de urato)
2. Citoesqueleto y perfil vascular/capilar inferior para la excreción de ácido úrico
3. Transportador URAT1 y filtración tubular renal sugerida
"""

DEFS_ENTORNO_DEGRADACION = """
    <!-- Gradiente de citosol a polo de excreción vascular de urato -->
    <linearGradient id="gradCitosolDeg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#f8fafc" stop-opacity="1" />
      <stop offset="60%" stop-color="#faf5ff" stop-opacity="0.8" />
      <stop offset="85%" stop-color="#fff1f2" stop-opacity="0.9" />
      <stop offset="100%" stop-color="#f8fafc" stop-opacity="1" />
    </linearGradient>

    <!-- Gradiente del lecho vascular / túbulo renal inferior -->
    <linearGradient id="gradCapilarRenal" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#fee2e2" stop-opacity="0.7" />
      <stop offset="50%" stop-color="#fecdd3" stop-opacity="0.85" />
      <stop offset="100%" stop-color="#fee2e2" stop-opacity="0.7" />
    </linearGradient>
"""

def generar_entorno_degradacion_svg(ancho=1400, alto=2200):
    """Genera la capa de fondo biológico sin cajas artificiales."""
    ancho_vasc = ancho - 80
    return f"""
    <!-- Fondo citosólico -->
    <rect x="0" y="0" width="{ancho}" height="{alto}" fill="url(#gradCitosolDeg)" />

    <!-- Red de microfilamentos citoplasmáticos -->
    <g opacity="0.25" stroke="#94a3b8" stroke-width="1.2" fill="none">
      <path d="M 60,180 Q 280,140 520,260 T 1220,240" />
      <path d="M 80,720 Q 360,660 680,780 T 1300,740" />
      <path d="M 40,1320 Q 320,1380 620,1260 T 1280,1400" />
    </g>

    <!-- Polo vascular inferior / túbulo proximal renal (excreción de urato) -->
    <g transform="translate(40, 1850)">
      <rect x="0" y="0" width="{ancho_vasc}" height="130" rx="14" fill="url(#gradCapilarRenal)" opacity="0.45"/>
      <path d="M 10,20 Q {ancho_vasc/2},-15 {ancho_vasc - 10},20" fill="none" stroke="#e11d48" stroke-width="2" opacity="0.4"/>
      <path d="M 10,110 Q {ancho_vasc/2},145 {ancho_vasc - 10},110" fill="none" stroke="#e11d48" stroke-width="2" opacity="0.4"/>
      <text x="{ancho_vasc/2}" y="125" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#be123c" text-anchor="middle" opacity="0.7">COMPARTIMENTO VASCULAR Y FILTRACIÓN RENAL (Túbulo contorneado proximal · URAT1)</text>
    </g>
    """
