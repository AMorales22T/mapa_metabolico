# =============================================================================
# MÓDULO DE REVISIÓN: Entorno Celular de Cetogénesis y Cetólisis
# =============================================================================
# Archivo original : 03_LIPIDOS/via_11_cetogenesis_y_cetolisis/entorno_ceto.py (líneas 1 a 174 de 174)
# Descripción      : Compartimentos celulares para Cetogénesis y Cetólisis.
# =============================================================================

#!/usr/bin/env python3
"""
ENTORNO BIOLÓGICO Y ANATOMÍA COMPARTIMENTADA - CETOGÉNESIS (ESTILO GLUCÓLISIS Y LANZADERA)
========================================================================================
Aplica estrictamente las directrices de las skills:
- scientific-schematics: Claridad fisiológica, sin textos de bloque estorbando, Okabe-Ito, contraste.
- excalidraw-diagram: Multi-Zoom Architecture (Lupa circular cónica para Cetólisis extrahepática).
- Estilo del proyecto: Fondo orgánico con gradientes acuosos, bicapa de fosfolípidos con cabezas polares,
  transportador transmembrana proteico MCT real con poro acuoso y lóbulos proteicos,
  microfilamentos sutiles de citoesqueleto y lupa de aumento científico.
"""

DEFS_ENTORNO_CETO_ORGANICO = """
    <!-- Gradiente del Citosol Celular Hepático (arriba) -->
    <linearGradient id="gradCitosolCeto" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#f8fafc" stop-opacity="1" />
      <stop offset="60%" stop-color="#f0fdf4" stop-opacity="0.6" />
      <stop offset="100%" stop-color="#f8fafc" stop-opacity="0.9" />
    </linearGradient>

    <!-- Gradiente de la Matriz Mitocondrial Hepática (Cálido y Luminoso) -->
    <radialGradient id="gradMatrizCeto" cx="50%" cy="30%" r="85%">
      <stop offset="0%" stop-color="#fffbeb" stop-opacity="1" />
      <stop offset="50%" stop-color="#fef3c7" stop-opacity="0.95" />
      <stop offset="85%" stop-color="#fef9c3" stop-opacity="0.9" />
      <stop offset="100%" stop-color="#fef08a" stop-opacity="0.85" />
    </radialGradient>

    <!-- Gradiente del Espacio Intermembrana / Membrana Plasmática -->
    <linearGradient id="gradBicapaCeto" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#fed7aa" stop-opacity="0.9" />
      <stop offset="50%" stop-color="#ffedd5" stop-opacity="0.95" />
      <stop offset="100%" stop-color="#fed7aa" stop-opacity="0.9" />
    </linearGradient>

    <!-- Gradiente del Capilar Sanguíneo en la Lupa -->
    <linearGradient id="gradCapilarZoom" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#ffe4e6" stop-opacity="0.9" />
      <stop offset="100%" stop-color="#fecdd3" stop-opacity="0.7" />
    </linearGradient>

    <!-- Gradiente Mitocondrial de la Célula Extrahepática en la Lupa -->
    <radialGradient id="gradExtraZoom" cx="50%" cy="50%" r="70%">
      <stop offset="0%" stop-color="#f0f9ff" stop-opacity="1" />
      <stop offset="70%" stop-color="#e0f2fe" stop-opacity="0.9" />
      <stop offset="100%" stop-color="#bae6fd" stop-opacity="0.8" />
    </radialGradient>
"""

def generar_entorno_organico_svg():
    """Genera la anatomía biológica viva (Matriz mitocondrial arriba, bicapa y transportador MCT, y Lupa de aumento abajo)."""
    return """
    <!-- ================================================================= -->
    <!-- CAPA 1: MATRIZ MITOCONDRIAL HEPÁTICA (ZONA DE CETOGÉNESIS)        -->
    <!-- ================================================================= -->
    <rect x="0" y="0" width="1100" height="980" fill="url(#gradMatrizCeto)" />

    <!-- Crestas Mitocondriales Profundas (Pliegues orgánicos sutiles al fondo) -->
    <g fill="none" stroke="#d97706" stroke-width="2.2" stroke-linecap="round" opacity="0.22">
      <path d="M 60 180 C 180 120, 260 240, 420 170" />
      <path d="M 60 420 C 220 360, 310 490, 480 430" />
      <path d="M 700 160 C 850 110, 930 220, 1060 170" />
      <path d="M 660 380 C 810 320, 920 460, 1050 410" />
      <path d="M 720 620 C 860 570, 940 700, 1050 640" />
    </g>

    <!-- Rótulo de orientación biológica sutil (idéntico a Glucolisis.svg) -->
    <text x="45" y="38" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#78350f" letter-spacing="2">
      HÍGADO • MATRIZ MITOCONDRIAL (SÍNTESIS DE CUERPOS CETÓNICOS)
    </text>


    <!-- ================================================================= -->
    <!-- CAPA 2: MEMBRANA Y CANAL TRANSPORTADOR MCT PROTEICO REAL          -->
    <!-- ================================================================= -->
    <!-- Espacio / Membrana Mitocondrial y Plasmática combinada (y = 980 a 1080) -->
    <rect x="0" y="980" width="1100" height="100" fill="url(#gradCitosolCeto)" />
    
    <!-- Bicapa Fosfolipídica Ondulada (y = 1000) -->
    <path d="M 0 1000 Q 550 1020 1100 1000" fill="none" stroke="#b45309" stroke-width="8" stroke-linecap="round"/>
    <path d="M 0 1008 Q 550 1028 1100 1008" fill="none" stroke="#f59e0b" stroke-width="3" stroke-linecap="round"/>

    <!-- Cabezas de fosfolípidos de la bicapa -->
    <g fill="#b45309" opacity="0.6">
      <circle cx="80" cy="998" r="3.2"/><circle cx="100" cy="999" r="3.2"/><circle cx="120" cy="1000" r="3.2"/>
      <circle cx="240" cy="1005" r="3.2"/><circle cx="260" cy="1006" r="3.2"/><circle cx="280" cy="1007" r="3.2"/>
      <circle cx="480" cy="1009" r="3.2"/><circle cx="500" cy="1009" r="3.2"/><circle cx="520" cy="1008" r="3.2"/>
      <circle cx="680" cy="1006" r="3.2"/><circle cx="700" cy="1005" r="3.2"/><circle cx="720" cy="1004" r="3.2"/>
      <circle cx="920" cy="999" r="3.2"/><circle cx="940" cy="998" r="3.2"/><circle cx="960" cy="997" r="3.2"/>
    </g>

    <!-- Rótulo de membrana discreto y limpio -->
    <text x="350" y="968" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#92400e" letter-spacing="1.5">
      MEMBRANA CELULAR • CARRIERS MCT
    </text>

    <!-- TRANSPORTADOR MCT PROTEICO EMBEBIDO EN LA MEMBRANA (Acetoacetato - Eje x=380) -->
    <g id="ceto-carrier-mct1" data-arrastrable="1" transform="translate(340, 985)">
      <!-- Lóbulo proteico izquierdo -->
      <path d="M 0 5 C 10 -12, 28 -12, 34 5 C 38 18, 34 36, 25 42 C 12 45, 2 35, 0 22 Z" fill="#0284c7" stroke="#0369a1" stroke-width="2.2"/>
      <!-- Lóbulo proteico derecho -->
      <path d="M 80 5 C 70 -12, 52 -12, 46 5 C 42 18, 46 36, 55 42 C 68 45, 78 35, 80 22 Z" fill="#0284c7" stroke="#0369a1" stroke-width="2.2"/>
      <!-- Poro central acuoso -->
      <ellipse cx="40" cy="20" rx="10" ry="18" fill="#e0f2fe" stroke="#38bdf8" stroke-width="1.8"/>
      <!-- Rótulo proteico en el canal -->
      <text x="40" y="24" fill="#0369a1" font-size="9" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">MCT1</text>
    </g>

    <!-- TRANSPORTADOR MCT PROTEICO EMBEBIDO EN LA MEMBRANA (D-β-Hidroxibutirato - Eje x=770) -->
    <g id="ceto-carrier-mct2" data-arrastrable="1" transform="translate(730, 985)">
      <!-- Lóbulo proteico izquierdo -->
      <path d="M 0 5 C 10 -12, 28 -12, 34 5 C 38 18, 34 36, 25 42 C 12 45, 2 35, 0 22 Z" fill="#0284c7" stroke="#0369a1" stroke-width="2.2"/>
      <!-- Lóbulo proteico derecho -->
      <path d="M 80 5 C 70 -12, 52 -12, 46 5 C 42 18, 46 36, 55 42 C 68 45, 78 35, 80 22 Z" fill="#0284c7" stroke="#0369a1" stroke-width="2.2"/>
      <!-- Poro central acuoso -->
      <ellipse cx="40" cy="20" rx="10" ry="18" fill="#e0f2fe" stroke="#38bdf8" stroke-width="1.8"/>
      <!-- Rótulo proteico en el canal -->
      <text x="40" y="24" fill="#0369a1" font-size="9" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">MCT2</text>
    </g>


    <!-- ================================================================= -->
    <!-- CAPA 3: PROYECCIÓN CÓNICA Y LUPA / ZOOM CIENTÍFICO INTERÓRGANO    -->
    <!-- ================================================================= -->
    <!-- Fondo acuoso del medio extracelular y capilar sanguíneo (y = 1080 a 2200) -->
    <rect x="0" y="1080" width="1100" height="1120" fill="url(#gradCitosolCeto)" />

    <!-- Filamentos sutiles de matriz extracelular -->
    <g opacity="0.3" stroke="#94a3b8" fill="none">
      <path d="M 40 1150 Q 300 1110 600 1160 T 1060 1130" stroke-width="1.5" stroke-dasharray="8 6" />
      <path d="M 40 1350 Q 350 1400 700 1340 T 1060 1370" stroke-width="1.4" stroke-dasharray="6 6" />
    </g>

    <!-- Líneas de proyección cónica hacia la Lupa de Cetólisis Extrahepática -->
    <g stroke="#0284c7" stroke-width="1.5" stroke-dasharray="5 4" opacity="0.55">
      <line x1="380" y1="1040" x2="160" y2="1240" />
      <line x1="770" y1="1040" x2="940" y2="1240" />
    </g>

    <!-- VENTANA CIRCULAR / LUPA DE ZOOM CIENTÍFICO (Extrahepático) -->
    <!-- Marco de lente de la Lupa de aumento -->
    <!-- Marco de lente de la Lupa de aumento -->
    <g id="ceto-lupa-extrahepatico" data-arrastrable="1" transform="translate(550, 1750)">
      <!-- Sombra y borde de la lente circular -->
      <circle cx="0" cy="0" r="510" fill="#ffffff" stroke="#0284c7" stroke-width="4.5" />
      <circle cx="0" cy="0" r="504" fill="url(#gradExtraZoom)" stroke="#38bdf8" stroke-width="1.5" />

      <!-- Fondo superior dentro de la lupa: Micro-Capilar Sanguíneo en arco -->
      <path d="M -500 -430 Q 0 -400 500 -430 L 500 -505 Q 0 -475 -500 -505 Z" fill="url(#gradCapilarZoom)" opacity="0.6"/>
      <path d="M -500 -430 Q 0 -400 500 -430" fill="none" stroke="#f43f5e" stroke-width="2.5" stroke-dasharray="6 4"/>
      
      <!-- Glóbulos rojos flotando en el micro-capilar dentro de la lupa -->
      <g fill="#f43f5e" opacity="0.5">
        <ellipse cx="-340" cy="-465" rx="14" ry="9" transform="rotate(-15 -340 -465)"/>
        <ellipse cx="-180" cy="-450" rx="13" ry="8" transform="rotate(10 -180 -450)"/>
        <ellipse cx="220" cy="-455" rx="14" ry="9" transform="rotate(-8 220 -455)"/>
        <ellipse cx="380" cy="-470" rx="13" ry="8" transform="rotate(20 380 -470)"/>
      </g>

      <!-- Rótulo integrado en la cima del lente de aumento -->
      <g transform="translate(0, -475)">
        <rect x="-240" y="-15" width="480" height="30" rx="15" fill="#ffffff" stroke="#0284c7" stroke-width="1.8"/>
        <circle cx="-218" cy="0" r="6" fill="#0284c7"/>
        <text x="-200" y="4.5" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#075985" letter-spacing="1">
          LUPA CIENTÍFICA: TEJIDOS DIANA (CEREBRO / CORAZÓN / MÚSCULO)
        </text>
      </g>
      
      <!-- Subtítulo de especificidad enzimática colocado discretamente bajo el capilar -->
      <text x="0" y="-420" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#0284c7" text-anchor="middle">
        Oxidación mitocondrial periférica dependiente de Tioforasa (SCOT / OXCT1)
      </text>
    </g>
    """
