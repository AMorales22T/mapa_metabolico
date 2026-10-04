#!/usr/bin/env python3
"""
ENTORNO BIOLÓGICO Y COMPARTIMENTAL - COLESTEROL Y VÍA DEL MEVALONATO
====================================================================
Escenario biológico integrado:
1. CITOPLASMA CELULAR / CITOSOL (Arriba y zona media):
   - Condensación de 3 Acetil-CoA a HMG-CoA soluble citosólico.
   - Microfilamentos de citoesqueleto y polirribosomas.
2. MEMBRANA DEL RETÍCULO ENDOPLÁSMICO LISO (REL) (Zona clave marcapasos y ciclación):
   - Bicapa lipídica membranosa del REL.
   - HMG-CoA Reductasa (HMGCR) anclada a la membrana con su dominio catalítico citosólico.
   - Escualeno Monooxigenasa y Ciclación (Escualeno Ciclasa / Lanosterol Sintasa).
3. DESTINOS DEL COLESTEROL (Zona inferior):
   - Transporte vesicular hacia Membrana Plasmática.
   - Esterificación (ACAT) hacia gotas lipídicas intracelulares (Colesteril ésteres).
   - Síntesis de Ácidos Biliares y Hormonas Esteroideas.
"""

DEFS_ENTORNO_COLESTEROL = """
    <!-- Gradiente del Citosol Celular -->
    <linearGradient id="colestGradCitosol" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#f8fafc" stop-opacity="1" />
      <stop offset="100%" stop-color="#fefce8" stop-opacity="0.9" />
    </linearGradient>

    <!-- Gradiente de la Membrana del Retículo Endoplásmico Liso (REL) -->
    <linearGradient id="colestGradREL" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#fed7aa" stop-opacity="0.95" />
      <stop offset="50%" stop-color="#ffedd5" stop-opacity="0.85" />
      <stop offset="100%" stop-color="#fed7aa" stop-opacity="0.95" />
    </linearGradient>

    <!-- Gradiente de la Enzima HMG-CoA Reductasa Anclada -->
    <linearGradient id="colestGradHMGCR" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7" />
      <stop offset="100%" stop-color="#0369a1" />
    </linearGradient>

    <!-- Gradiente de Gota Lipídica de Ésteres de Colesterol -->
    <radialGradient id="colestGradGotaCol" cx="40%" cy="40%" r="60%">
      <stop offset="0%" stop-color="#fef08a" stop-opacity="0.95" />
      <stop offset="70%" stop-color="#eab308" stop-opacity="0.8" />
      <stop offset="100%" stop-color="#ca8a04" stop-opacity="0.9" />
    </radialGradient>
"""

def generar_entorno_colesterol_svg(ancho=1000, alto=2300, y_rel_ini=480, y_rel_fin=530):
    """Genera el fondo biológico compartimental de Citosol y Retículo Endoplásmico Liso."""
    p = []

    # 1. Fondo completo de Citosol
    p.append(f'<rect x="0" y="0" width="{ancho}" height="{alto}" fill="url(#colestGradCitosol)" />')

    # Microfilamentos del citoesqueleto en citosol
    p.append(f"""
    <g opacity="0.32" stroke="#94a3b8" fill="none">
      <path d="M 30 200 Q 300 170 600 220 T {ancho - 30} 190" stroke-width="1.5" stroke-dasharray="8 6"/>
      <path d="M 50 400 Q 350 440 650 380 T {ancho - 50} 420" stroke-width="1.4" stroke-dasharray="6 5"/>
      <path d="M 40 850 Q 280 810 580 870 T {ancho - 40} 830" stroke-width="1.5" stroke-dasharray="8 6"/>
      <path d="M 60 1350 Q 380 1390 700 1330 T {ancho - 60} 1370" stroke-width="1.4" stroke-dasharray="7 5"/>
      <path d="M 30 1850 Q 300 1810 620 1870 T {ancho - 30} 1840" stroke-width="1.5" stroke-dasharray="8 6"/>
    </g>

    <!-- Polirribosomas citosólicos -->
    <g fill="#94a3b8" opacity="0.25">
      <circle cx="80" cy="180" r="2.5"/><circle cx="86" cy="182" r="2"/><circle cx="84" cy="188" r="2.3"/>
      <circle cx="{ancho - 90}" cy="300" r="2.5"/><circle cx="{ancho - 84}" cy="302" r="2"/><circle cx="{ancho - 86}" cy="308" r="2.3"/>
      <circle cx="100" cy="980" r="2.5"/><circle cx="106" cy="982" r="2"/>
      <circle cx="{ancho - 110}" cy="1550" r="2.5"/><circle cx="{ancho - 104}" cy="1552" r="2"/>
    </g>
    """)

    # 2. Título de Compartimento Citosólico
    p.append(f"""
    <text x="35" y="32" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#1e3a8a" letter-spacing="1.5">
      CITOPLASMA CELULAR (CITOSOL) • FASE TEMPRANA Y CONDENSACIÓN DE ACETIL-CoA
    </text>
    """)

    # 3. Franja Ondulada de Membrana del Retículo Endoplásmico Liso (REL)
    p.append(f"""
    <!-- Membrana del REL donde se ancla la HMG-CoA Reductasa y enzimas de ciclación -->
    <g id="membrana_rel">
      <path d="M 0 {y_rel_ini} Q {ancho/3} {y_rel_ini - 15}, {ancho/2} {y_rel_ini} T {ancho} {y_rel_ini}" fill="none" stroke="#ea580c" stroke-width="5" stroke-linecap="round" opacity="0.75"/>
      <path d="M 0 {y_rel_fin} Q {ancho/3} {y_rel_fin - 15}, {ancho/2} {y_rel_fin} T {ancho} {y_rel_fin}" fill="none" stroke="#ea580c" stroke-width="5" stroke-linecap="round" opacity="0.75"/>
      <path d="M 0 {y_rel_ini + 2} Q {ancho/3} {y_rel_ini - 13}, {ancho/2} {y_rel_ini + 2} T {ancho} {y_rel_ini + 2} L {ancho} {y_rel_fin - 2} Q {ancho*2/3} {y_rel_fin - 13}, {ancho/2} {y_rel_fin - 2} T 0 {y_rel_fin - 2} Z" fill="url(#colestGradREL)" opacity="0.6"/>
      
      <text x="{ancho - 35}" y="{y_rel_fin + 22}" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#c2410c" text-anchor="end">
        MEMBRANA DEL RETÍCULO ENDOPLÁSMICO LISO (REL) • ANCLAJE DE HMGCR &amp; CICLASAS
      </text>
    </g>
    """)

    # 4. Fondo inferior: Gota lipídica de Ésteres de Colesterol y Salida de Lipoproteínas
    p.append(f"""
    <!-- Gota lipídica de reserva de Ésteres de Colesterol (CE) -->
    <g transform="translate(130, 2180)" opacity="0.95">
      <circle cx="0" cy="0" r="48" fill="url(#colestGradGotaCol)" stroke="#ca8a04" stroke-width="2.5" stroke-dasharray="6 3"/>
      <text x="0" y="-8" fill="#78350f" font-size="9.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">GOTA LIPÍDICA</text>
      <text x="0" y="6" fill="#854d0e" font-size="8" font-weight="800" font-family="'JetBrains Mono', monospace" text-anchor="middle">ÉSTERES DE COLESTEROL</text>
      <text x="0" y="20" fill="#a16207" font-size="8" font-weight="700" font-family="'Inter', sans-serif" text-anchor="middle">Almacenamiento (ACAT)</text>
    </g>
    """)

    return "\n".join(p)
