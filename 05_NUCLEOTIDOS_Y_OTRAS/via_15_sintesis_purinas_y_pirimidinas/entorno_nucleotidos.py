#!/usr/bin/env python3
"""
ENTORNO BIOLÓGICO CELULAR (SVG) - METABOLISMO DE NUCLEÓTIDOS
============================================================
Fondo celular orgánico para la biosíntesis de Purinas y Pirimidinas:
1. Fondo acuoso citosólico (#f8fafc -> #faf5ff)
2. Citoesqueleto fino y ribosomas citosólicos
3. Perfil de membrana mitocondrial lateral derecha para albergar la Dihidroorotato Deshidrogenasa (DHODH)
4. Sin cajas divisorias cuadradas artificiales
"""

DEFS_ENTORNO_NUCLEOTIDOS = """
    <!-- Gradiente citosólico con sutil tinte lavanda característico de nucleótidos -->
    <linearGradient id="gradCitosolNuc" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#f8fafc" stop-opacity="1" />
      <stop offset="15%" stop-color="#faf5ff" stop-opacity="0.9" />
      <stop offset="60%" stop-color="#fdf4ff" stop-opacity="0.8" />
      <stop offset="100%" stop-color="#f8fafc" stop-opacity="1" />
    </linearGradient>

    <!-- Gradiente de inserción mitocondrial para DHODH (en membrana interna) -->
    <radialGradient id="gradMitoLateral" cx="100%" cy="45%" r="60%">
      <stop offset="0%" stop-color="#fef3c7" stop-opacity="0.95" />
      <stop offset="70%" stop-color="#fffbeb" stop-opacity="0.7" />
      <stop offset="100%" stop-color="#f8fafc" stop-opacity="0" />
    </radialGradient>
"""

def generar_entorno_nucleotidos_svg(ancho=1150, alto=2200):
    """Genera la capa de fondo biológico celular sin etiquetas invasivas."""
    return f"""
    <!-- Fondo acuoso del citosol -->
    <rect x="0" y="0" width="{ancho}" height="{alto}" fill="url(#gradCitosolNuc)" />

    <!-- Filamentos sutiles de citoesqueleto citoplasmático -->
    <g opacity="0.25" stroke="#a855f7" stroke-width="1.2" fill="none">
      <path d="M 50,150 Q 250,120 480,240 T 950,220" />
      <path d="M 80,680 Q 320,620 620,740 T 1100,700" />
      <path d="M 40,1250 Q 280,1320 580,1210 T 1050,1350" />
      <path d="M 90,1820 Q 350,1750 680,1890 T 1080,1820" />
    </g>

    <!-- Micro-vesículas y ribosomas libres en citoplasma -->
    <g opacity="0.3" fill="#c084fc">
      <circle cx="90" cy="320" r="3" />
      <circle cx="105" cy="335" r="2" />
      <circle cx="1080" cy="450" r="3.5" />
      <circle cx="1060" cy="470" r="2.2" />
      <circle cx="70" cy="1120" r="2.8" />
      <circle cx="1040" cy="1550" r="3.2" />
    </g>

    <!-- Inserción biológica mitocondrial en el flanco derecho (para DHODH en pirimidinas) -->
    <g transform="translate({ancho - 320}, 750)">
      <!-- Sombra matricial suave -->
      <path d="M 0,0 Q 120,-60 220,-40 L 320,-40 L 320,380 L 180,380 Q 80,360 0,300 Z" fill="url(#gradMitoLateral)" />
      <!-- Membrana Mitocondrial Externa (MME) -->
      <path d="M 60,-20 Q 140,-50 320,-30" fill="none" stroke="#b45309" stroke-width="2.5" opacity="0.6"/>
      <!-- Espacio Intermembrana (EIM) -->
      <path d="M 90,15 Q 160,-15 320,5" fill="none" stroke="#d97706" stroke-width="1.8" stroke-dasharray="4 3" opacity="0.5"/>
      <!-- Membrana Mitocondrial Interna (MMI con crestas) -->
      <path d="M 120,50 Q 180,20 220,70 Q 260,120 320,40" fill="none" stroke="#92400e" stroke-width="3" opacity="0.75"/>
      <text x="210" y="25" font-family="'Inter', sans-serif" font-size="9" font-weight="800" fill="#92400e" opacity="0.6">MMI (DHODH)</text>
    </g>
    """
