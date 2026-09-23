#!/usr/bin/env python3
"""
ENTORNO BIOLÓGICO DE LA MEMBRANA MITOCONDRIAL INTERNA (SVG)
===========================================================
Dibujo de fondo para el mapa de la Cadena Transportadora de Electrones y la
ATP Sintasa. Reutiliza el lenguaje visual del entorno mitocondrial del Ciclo
de Krebs, pero con la bicapa lipídica de la MMI en horizontal y muy visible,
para poder incrustar sobre ella los cinco complejos respiratorios.

Compartimentos (de arriba a abajo):
1. Citosol (lanzaderas que introducen el NADH glucolítico).
2. Membrana Mitocondrial Externa (MME) con la porina VDAC.
3. Espacio Intermembrana (EIM): pH bajo, gradiente de H⁺ acumulado.
4. Membrana Mitocondrial Interna (MMI): bicapa lipídica atravesada por los complejos.
5. Matriz Mitocondrial: pH alto, ADNmt, mitorribosomas y gránulos densos.

NOTA: este módulo sólo usa los marcadores (markers) definidos por el generador
principal: arrowFlow, arrowRed, arrowSlate, arrowGreen, arrowBlue, arrowAmber.
"""


# =============================================================================
# RECURSOS GRÁFICOS (GRADIENTES) DEL ENTORNO MITOCONDRIAL
# =============================================================================
DEFS_ENTORNO_CTE = """
    <!-- Gradiente del citosol (arriba) -->
    <linearGradient id="cteGradCitosol" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#f8fafc" stop-opacity="1" />
      <stop offset="100%" stop-color="#e2e8f0" stop-opacity="0.95" />
    </linearGradient>

    <!-- Gradiente del Espacio Intermembrana (EIM): cálido y ácido, rico en H⁺ -->
    <linearGradient id="cteGradEIM" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#ffedd5" stop-opacity="0.55" />
      <stop offset="70%" stop-color="#fed7aa" stop-opacity="0.75" />
      <stop offset="100%" stop-color="#fdba74" stop-opacity="0.85" />
    </linearGradient>

    <!-- Gradiente de la Matriz Mitocondrial (ámbar cálido y luminoso) -->
    <radialGradient id="cteGradMatriz" cx="50%" cy="35%" r="85%">
      <stop offset="0%" stop-color="#fffbeb" stop-opacity="1" />
      <stop offset="45%" stop-color="#fef3c7" stop-opacity="0.96" />
      <stop offset="85%" stop-color="#fef9c3" stop-opacity="0.92" />
      <stop offset="100%" stop-color="#fef08a" stop-opacity="0.88" />
    </radialGradient>

    <!-- Gradiente del interior de la bicapa lipídica -->
    <linearGradient id="cteGradBicapa" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#fde68a" stop-opacity="0.95" />
      <stop offset="50%" stop-color="#fef3c7" stop-opacity="0.9" />
      <stop offset="100%" stop-color="#fde68a" stop-opacity="0.95" />
    </linearGradient>

    <!-- Gradiente de las crestas mitocondriales -->
    <linearGradient id="cteGradCresta" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fde68a" stop-opacity="0.95" />
      <stop offset="100%" stop-color="#fef3c7" stop-opacity="0.8" />
    </linearGradient>
"""


# =============================================================================
# HERRAMIENTAS DE DIBUJO
# =============================================================================
def _fila_fosfolipidos(ancho, y_centro, hacia_abajo=True, paso=38, color="#d97706"):
    """
    Genera una fila de cabezas polares con sus dos colas de ácido graso
    (el patrón clásico de la bicapa lipídica esquemática).
    """
    piezas = []
    signo = 1 if hacia_abajo else -1
    for x in range(22, ancho - 12, paso):
        piezas.append(f'<circle cx="{x}" cy="{y_centro}" r="4.6" fill="{color}" opacity="0.85"/>')
        piezas.append(
            f'<path d="M {x - 2.4} {y_centro + signo * 5} q -2.6 {signo * 8} 1.4 {signo * 15}" '
            f'fill="none" stroke="{color}" stroke-width="1.1" opacity="0.45"/>'
        )
        piezas.append(
            f'<path d="M {x + 2.4} {y_centro + signo * 5} q 2.6 {signo * 8} -1.4 {signo * 15}" '
            f'fill="none" stroke="{color}" stroke-width="1.1" opacity="0.45"/>'
        )
    return "\n    ".join(piezas)


def _nube_protones(ancho, y_ini, y_fin):
    """
    Campo de protones H⁺ distribuido en el Espacio Intermembrana.
    La opacidad aumenta hacia la membrana interna (gradiente electroquímico).
    """
    piezas = []
    filas = list(range(y_ini, y_fin, 46))
    for i, yy in enumerate(filas):
        fraccion = i / max(len(filas) - 1, 1)
        opacidad = round(0.30 + 0.35 * fraccion, 2)
        desplazamiento = 0 if i % 2 == 0 else 62
        for col in range(13):
            xx = 46 + desplazamiento + col * 132
            if xx > ancho - 26:
                continue
            piezas.append(
                f'<text x="{xx}" y="{yy}" font-family="\'Inter\', sans-serif" '
                f'font-size="11" font-weight="900" fill="#ea580c" opacity="{opacidad}">H⁺</text>'
            )
    return "\n    ".join(piezas)


# =============================================================================
# DIBUJO COMPLETO DEL ENTORNO
# =============================================================================
def generar_entorno_cte_svg(ancho=1700, alto=2200, y_mme=112, y_eim_ini=132,
                            y_eim_fin=545, y_mmi_ini=545, y_mmi_fin=645):
    """
    Retorna todo el código SVG del fondo celular y mitocondrial.
    Los complejos respiratorios se dibujan DESPUÉS, encima de la bicapa.
    """
    espaciado_eim = y_eim_fin - y_eim_ini

    return f"""
    <!-- ================================================================= -->
    <!-- CAPA 1: MATRIZ MITOCONDRIAL DE FONDO                              -->
    <!-- ================================================================= -->
    <rect x="0" y="0" width="{ancho}" height="{alto}" fill="url(#cteGradMatriz)" />

    <!-- Crestas mitocondriales profundas (invaginaciones de la MMI) -->
    <g fill="url(#cteGradCresta)" stroke="#d97706" stroke-width="2" opacity="0.4">
      <path d="M 0 780 C 70 780, 92 830, 88 900 C 84 970, 50 1000, 0 1010 Z" />
      <path d="M 0 1240 C 76 1230, 96 1290, 90 1360 C 84 1420, 44 1450, 0 1460 Z" />
      <path d="M {ancho} 1180 C {ancho - 78} 1170, {ancho - 98} 1230, {ancho - 92} 1300 C {ancho - 86} 1360, {ancho - 46} 1390, {ancho} 1400 Z" />
    </g>

    <!-- ADN mitocondrial circular (ADNmt) -->
    <g fill="none" stroke="#b45309" stroke-width="1.3" opacity="0.22">
      <path d="M 96 1560 C 130 1530, 176 1554, 166 1600 C 156 1646, 106 1656, 84 1620 Z" stroke-dasharray="4 3"/>
      <path d="M {ancho - 120} 1880 C {ancho - 86} 1850, {ancho - 40} 1874, {ancho - 50} 1920 C {ancho - 60} 1966, {ancho - 110} 1976, {ancho - 132} 1940 Z" stroke-dasharray="4 3"/>
    </g>

    <!-- Mitorribosomas (55S) y gránulos densos de Ca²⁺ / Mg²⁺ -->
    <g fill="#b45309" opacity="0.22">
      <circle cx="250" cy="1500" r="2.8"/><circle cx="258" cy="1503" r="2.2"/><circle cx="254" cy="1509" r="2.5"/>
      <circle cx="1480" cy="1560" r="2.8"/><circle cx="1488" cy="1563" r="2.2"/><circle cx="1484" cy="1569" r="2.5"/>
      <circle cx="860" cy="2080" r="2.8"/><circle cx="868" cy="2083" r="2.2"/><circle cx="864" cy="2089" r="2.5"/>
    </g>
    <g opacity="0.22">
      <ellipse cx="300" cy="1900" rx="9" ry="6" fill="#78350f" stroke="#92400e" stroke-width="1.3"/>
      <ellipse cx="1380" cy="1820" rx="9" ry="6" fill="#78350f" stroke="#92400e" stroke-width="1.3"/>
    </g>

    <!-- ================================================================= -->
    <!-- CAPA 2: CITOSOL, MME Y PORINA VDAC                                -->
    <!-- ================================================================= -->
    <path d="M 0 0 L {ancho} 0 L {ancho} {y_mme} Q {ancho / 2} {y_mme + 6} 0 {y_mme} Z" fill="url(#cteGradCitosol)" />
    <g opacity="0.3" stroke="#94a3b8" fill="none">
      <path d="M 30 24 Q 400 10 900 26 T {ancho - 30} 20" stroke-width="1.5" stroke-dasharray="8 6"/>
      <path d="M 70 52 Q 500 66 1000 48 T {ancho - 70} 56" stroke-width="1.3" stroke-dasharray="6 5"/>
    </g>
    <text x="30" y="26" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900"
          fill="#64748b" letter-spacing="1.4">CITOSOL (NADH GLUCOLÍTICO → LANZADERAS MALATO-ASPARTATO / GLICEROL-3-P)</text>

    <!-- Membrana Mitocondrial Externa (MME) -->
    <path d="M 0 {y_mme} Q {ancho / 2} {y_mme + 6} {ancho} {y_mme}" fill="none" stroke="#78350f" stroke-width="5.5" stroke-linecap="round"/>
    <path d="M 0 {y_mme + 3} Q {ancho / 2} {y_mme + 9} {ancho} {y_mme + 3}" fill="none" stroke="#b45309" stroke-width="2" stroke-linecap="round"/>
    <text x="{ancho - 300}" y="{y_mme - 9}" font-family="'Inter', sans-serif" font-size="9.5"
          font-weight="700" fill="#78350f">Membrana Mitocondrial Externa (MME)</text>

    <!-- Porina VDAC (paso libre de nucleótidos y metabolitos pequeños) -->
    <g transform="translate(300, {y_mme - 12})">
      <rect x="0" y="0" width="38" height="24" rx="6" fill="#f97316" stroke="#c2410c" stroke-width="1.8"/>
      <ellipse cx="19" cy="12" rx="8.5" ry="5.5" fill="#e0f2fe" stroke="#38bdf8" stroke-width="1.2"/>
      <text x="19" y="31" font-family="'JetBrains Mono', monospace" font-size="8"
            font-weight="900" fill="#9a3412" text-anchor="middle">VDAC</text>
    </g>

    <!-- ================================================================= -->
    <!-- CAPA 3: ESPACIO INTERMEMBRANA Y GRADIENTE DE PROTONES             -->
    <!-- ================================================================= -->
    <path d="M 0 {y_mme + 6} Q {ancho / 2} {y_mme + 12} {ancho} {y_mme + 6}
             L {ancho} {y_eim_fin} Q {ancho / 2} {y_eim_fin + 6} 0 {y_eim_fin} Z"
          fill="url(#cteGradEIM)" />

    {_nube_protones(ancho, y_eim_ini + 30, y_eim_fin - 10)}

    <text x="30" y="{y_eim_ini + 26}" font-family="'Inter', sans-serif" font-size="10.5"
          font-weight="900" fill="#9a3412" letter-spacing="1.2">ESPACIO INTERMEMBRANA (EIM) • pH ≈ 6.8 • [H⁺] ALTA</text>

    <!-- Barra lateral del gradiente electroquímico -->
    <g transform="translate(24, {y_eim_ini + 60})">
      <rect x="0" y="0" width="14" height="{espaciado_eim - 120}" rx="7" fill="#fdba74" stroke="#ea580c" stroke-width="1.4"/>
      <text x="26" y="{espaciado_eim / 2 - 60}" font-family="'JetBrains Mono', monospace" font-size="9"
            font-weight="700" fill="#9a3412">Δp = Δψ + ΔpH ≈ 200 mV</text>
    </g>

    <!-- ================================================================= -->
    <!-- CAPA 4: MEMBRANA MITOCONDRIAL INTERNA (BICAPA LIPÍDICA)           -->
    <!-- ================================================================= -->
    <rect x="0" y="{y_mmi_ini}" width="{ancho}" height="{y_mmi_fin - y_mmi_ini}" fill="url(#cteGradBicapa)"/>
    <line x1="0" y1="{(y_mmi_ini + y_mmi_fin) / 2}" x2="{ancho}" y2="{(y_mmi_ini + y_mmi_fin) / 2}"
          stroke="#d97706" stroke-width="1.2" stroke-dasharray="5 4" opacity="0.6"/>
    {_fila_fosfolipidos(ancho, y_mmi_ini + 8, hacia_abajo=True)}
    {_fila_fosfolipidos(ancho, y_mmi_fin - 8, hacia_abajo=False)}
    <text x="{ancho - 320}" y="{y_mmi_fin + 20}" font-family="'Inter', sans-serif" font-size="10"
          font-weight="800" fill="#92400e">Membrana Mitocondrial Interna (MMI) • bicapa impermeable a H⁺</text>

    <!-- ================================================================= -->
    <!-- CAPA 5: MATRIZ MITOCONDRIAL (RÓTULO DE COMPARTIMENTO)             -->
    <!-- ================================================================= -->
    <text x="30" y="{y_mmi_fin + 52}" font-family="'Inter', sans-serif" font-size="10.5"
          font-weight="900" fill="#92400e" letter-spacing="1.2">MATRIZ MITOCONDRIAL • pH ≈ 7.8 • [H⁺] BAJA • ALTA [ATP] / [ADP] BAJA</text>
    """
