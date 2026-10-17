# =============================================================================
# MÓDULO DE REVISIÓN: Vía 19: Tejido Adiposo y Cascada Lipolítica Secuencial
# =============================================================================
# Archivo original : 07_AMPLIACION_TEMARIO/generar_ampliacion.py (líneas 330 a 425 de 925)
# Descripción      : Gota lipídica con perilipina-1, hidrólisis secuencial TAG -> ATGL -> DAG -> HSL -> 2-MAG -> MGL -> Glicerol + 3 AG.
# =============================================================================

    # -------------------------------------------------------------------------
    # VÍA 19: TEJIDO ADIPOSO (CASCADA LIPOLÍTICA COMPLETA CON ESTRUCTURAS)
    # -------------------------------------------------------------------------
    p.append('<g id="ruta_tejido_adiposo" class="ruta-metabolica">')
    p.append(encabezado_via(-710, 1290, 19, "TEJIDO ADIPOSO: CASCADA LIPOLÍTICA COMPLETA", "Gota lipídica • ATGL ➔ HSL ➔ MGL con estructuras químicas completas", color="#ea580c"))

    # Contenedor del adipocito
    p.append("""
    <g transform="translate(-690, 1340)">
      <!-- Membrana celular adipocitaria -->
      <rect x="0" y="0" width="620" height="960" rx="16" fill="#fffbeb" stroke="#d97706" stroke-width="3" opacity="0.95"/>
      <text x="310" y="30" font-family="'Inter', sans-serif" font-size="13.5" font-weight="900" fill="#78350f" text-anchor="middle">ADIPOCITO UNILOCULAR: GOTA LIPÍDICA Y LIPÓLISIS SECUENCIAL</text>
      
      <!-- Control hormonal nítido -->
      <g transform="translate(30, 45)">
        <rect x="0" y="0" width="260" height="38" rx="6" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.8"/>
        <text x="130" y="17" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#15803d" text-anchor="middle">[+ INSULINA]</text>
        <text x="130" y="30" font-family="'Inter', sans-serif" font-size="8.5" font-weight="800" fill="#166534" text-anchor="middle">↑ Síntesis TAG / Inhibe ATGL y HSL</text>
      </g>
      <g transform="translate(330, 45)">
        <rect x="0" y="0" width="260" height="38" rx="6" fill="#fef2f2" stroke="#dc2626" stroke-width="1.8"/>
        <text x="130" y="17" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#b91c1c" text-anchor="middle">[+ GLUCAGÓN / ADRENALINA]</text>
        <text x="130" y="30" font-family="'Inter', sans-serif" font-size="8.5" font-weight="800" fill="#991b1b" text-anchor="middle">PKA fosforila Perilipina-1 (PLIN1) y HSL</text>
      </g>
    </g>
    """)

    # PASO 1: TRIACILGLICEROL ➔ ATGL ➔ DAG + 1º AG
    p.append(nodo_libre(-660, 1450, "Triacilglicerol de Reserva", "TAG", ea.TRIACILGLICEROL, "m_adipo_tag", dx=190, dy=20, detalle="Almacenado en gota lipídica con PLIN1"))
    p.append(reaccion_flecha(-520, 1560, 60, "ATGL (Lipasa Adiposa de TAG)", entra="+ H₂O", sale="+ 1º AG libre", ec="EC 3.1.1.3 (+ CGI-58)", color="#ea580c", id_rx="rx_atgl"))

    # PASO 2: 1,2-DIACILGLICEROL ➔ HSL ➔ 2-MAG + 2º AG
    p.append(nodo_libre(-660, 1670, "1,2-Diacilglicerol (DAG)", "DAG", ea.DIACILGLICEROL, "m_adipo_dag", dx=190, dy=20, detalle="Sustrato de HSL fosforilada por PKA"))
    p.append(reaccion_flecha(-520, 1780, 60, "HSL (Lipasa Sensible a Hormonas)", entra="+ H₂O", sale="+ 2º AG libre", ec="EC 3.1.1.79 (PKA / Glucagón)", color="#ea580c", id_rx="rx_hsl"))

    # PASO 3: 2-MONOACILGLICEROL ➔ MGL ➔ GLICEROL LIBRE + 3º AG
    p.append(nodo_libre(-660, 1890, "2-Monoacilglicerol (2-MAG)", "MAG", ea.MONOACILGLICEROL_2, "m_adipo_mag", dx=190, dy=20, detalle="Sustrato final de MGL citosólica"))
    p.append(reaccion_flecha(-520, 2000, 60, "MGL (Monoacilglicerol Lipasa)", entra="+ H₂O", sale="+ 3º AG libre", ec="EC 3.1.1.23", color="#ea580c", id_rx="rx_mgl"))

    # PRODUCTO FINAL: GLICEROL LIBRE
    p.append(nodo_libre(-660, 2110, "Glicerol Libre", "3C", ea.GLICEROL_ESTRUCTURA, "m_adipo_glicerol", dx=190, dy=20, detalle="El adipocito carece de Glicerol Quinasa"))

    # =========================================================================
    # CONEXIONES VASCULARES Y COLECTORES CON LÍNEAS Y FLECHAS PUNTEADAS (0 SOLAPAMIENTOS)
    # =========================================================================
    p.append("""
    <!-- 1. POOL COLECTOR DE LOS 3 ÁCIDOS GRASOS LIBRES -->
    <g id="colector_3ag_adipocito">
      <!-- Convergencia de los 3 cortes enzimáticos (ATGL, HSL, MGL) hacia el Pool con flechas punteadas -->
      <path d="M -580 1590 C -450 1590, -360 1700, -280 1700" fill="none" stroke="#ea580c" stroke-width="2" stroke-dasharray="6 4" marker-end="url(#arrowOrange)"/>
      <path d="M -580 1810 C -450 1810, -360 1726, -280 1726" fill="none" stroke="#ea580c" stroke-width="2" stroke-dasharray="6 4" marker-end="url(#arrowOrange)"/>
      <path d="M -580 2030 C -450 2030, -360 1750, -280 1750" fill="none" stroke="#ea580c" stroke-width="2" stroke-dasharray="6 4" marker-end="url(#arrowOrange)"/>

      <!-- Caja del Pool de 3 AG libres -->
      <rect x="-280" y="1680" width="190" height="92" rx="10" fill="#fff7ed" stroke="#ea580c" stroke-width="2"/>
      <text x="-185" y="1703" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#c2410c" text-anchor="middle">POOL: 3 AG LIBRES</text>
      <text x="-185" y="1720" font-family="'Inter', sans-serif" font-size="9" font-weight="700" fill="#ea580c" text-anchor="middle">3 (R-COO⁻) de ATGL/HSL/MGL</text>
      <line x1="-270" y1="1728" x2="-100" y2="1728" stroke="#fed7aa" stroke-width="1"/>
      <text x="-185" y="1744" font-family="'Inter', sans-serif" font-size="9" font-weight="800" fill="#0f172a" text-anchor="middle">Transportador CD36 / FATP</text>
      <text x="-185" y="1760" font-family="'Inter', sans-serif" font-size="8.5" font-weight="700" fill="#64748b" text-anchor="middle">+ Albúmina Sérica en Sangre</text>
    </g>

    <!-- Salida y transporte vascular de 3 AG + Albúmina con línea y flechas punteadas ascendentes -->
    <g id="salida_vascular_adipocito">
      <path d="M -90 1726 L -40 1726 L -40 425" fill="none" stroke="#ea580c" stroke-width="2.8" stroke-dasharray="8 5" marker-end="url(#arrowOrange)"/>
      <g transform="translate(-40, 1080)">
        <rect x="-85" y="-14" width="170" height="28" rx="6" fill="#fff7ed" stroke="#ea580c" stroke-width="1.6"/>
        <text x="0" y="4" font-family="'Inter', sans-serif" font-size="9" font-weight="900" fill="#c2410c" text-anchor="middle">3 AG + Albúmina ➔ Sangre</text>
      </g>
    </g>

    <!-- 2. COLECTOR Y SALIDA DE GLICEROL LIBRE POR AQUAPORINA-7 -->
    <g id="colector_glicerol_adipocito">
      <!-- Flecha punteada desde la molécula de Glicerol hacia el colector -->
      <path d="M -340 2120 L -280 2120" fill="none" stroke="#0284c7" stroke-width="2" stroke-dasharray="6 4" marker-end="url(#arrowBlue)"/>

      <!-- Caja de salida de Glicerol -->
      <rect x="-280" y="2080" width="190" height="80" rx="10" fill="#f0f9ff" stroke="#0284c7" stroke-width="2"/>
      <text x="-185" y="2102" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#0369a1" text-anchor="middle">GLICEROL LIBRE</text>
      <text x="-185" y="2118" font-family="'Inter', sans-serif" font-size="9" font-weight="700" fill="#0284c7" text-anchor="middle">El adipocito carece de GK</text>
      <line x1="-270" y1="2126" x2="-100" y2="2126" stroke="#bae6fd" stroke-width="1"/>
      <text x="-185" y="2142" font-family="'Inter', sans-serif" font-size="9" font-weight="800" fill="#0f172a" text-anchor="middle">Aquaporina-7 (AQP7)</text>
      <text x="-185" y="2154" font-family="'Inter', sans-serif" font-size="8.5" font-weight="700" fill="#64748b" text-anchor="middle">➔ Sangre a Hígado (GNG)</text>
    </g>

    <!-- Salida y transporte vascular de Glicerol con línea y flechas punteadas ascendentes -->
    <g id="salida_vascular_glicerol">
      <path d="M -90 2120 L -15 2120 L -15 425" fill="none" stroke="#0284c7" stroke-width="2.6" stroke-dasharray="8 5" marker-end="url(#arrowBlue)"/>
      <g transform="translate(-15, 1220)">
        <rect x="-80" y="-14" width="160" height="28" rx="6" fill="#f0f9ff" stroke="#0284c7" stroke-width="1.6"/>
        <text x="0" y="4" font-family="'Inter', sans-serif" font-size="9" font-weight="900" fill="#0369a1" text-anchor="middle">Glicerol ➔ Hígado (GNG)</text>
      </g>
    </g>
    """)
    p.append('</g>')

