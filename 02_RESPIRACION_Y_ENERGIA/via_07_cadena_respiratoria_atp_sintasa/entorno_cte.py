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
def _fila_fosfolipidos(ancho, y_centro, hacia_abajo=True, paso=30, color="#d97706"):
    """
    Genera una fila de cabezas polares con sus dos colas de ácido graso
    (el patrón clásico de la bicapa lipídica esquemática).
    """
    piezas = []
    signo = 1 if hacia_abajo else -1
    for x in range(18, ancho - 10, paso):
        piezas.append(f'<circle cx="{x}" cy="{y_centro}" r="4.2" fill="{color}" opacity="0.85"/>')
        piezas.append(
            f'<path d="M {x - 2.2} {y_centro + signo * 5} q -2.4 {signo * 8} 1.3 {signo * 15}" '
            f'fill="none" stroke="{color}" stroke-width="1" opacity="0.45"/>'
        )
        piezas.append(
            f'<path d="M {x + 2.2} {y_centro + signo * 5} q 2.4 {signo * 8} -1.3 {signo * 15}" '
            f'fill="none" stroke="{color}" stroke-width="1" opacity="0.45"/>'
        )
    return "\n    ".join(piezas)


def _nube_protones(ancho, y_ini, y_fin, columnas_excluidas=()):
    """
    Campo de protones H⁺ distribuido en el Espacio Intermembrana.
    Se saltan las columnas indicadas para no chocar con los dominios solubles
    del Complejo III ni con las flechas de retorno de la ATP sintasa.
    """
    piezas = []
    filas = list(range(y_ini, y_fin, 55))
    for i, yy in enumerate(filas):
        fraccion = i / max(len(filas) - 1, 1)
        opacidad = round(0.32 + 0.30 * fraccion, 2)
        for xx in range(45, ancho - 30, 70):
            if any(abs(xx - prohibida) < 34 for prohibida in columnas_excluidas):
                continue
            piezas.append(
                f'<text x="{xx}" y="{yy}" font-family="\'Inter\', sans-serif" '
                f'font-size="10" font-weight="900" fill="#ea580c" opacity="{opacidad}">H⁺</text>'
            )
    return "\n    ".join(piezas)


# =============================================================================
# DIBUJO COMPLETO DEL ENTORNO
# =============================================================================
def generar_entorno_cte_svg(ancho=1150, alto=1740, y_mme=90, y_eim_ini=104,
                            y_eim_fin=330, y_mmi_ini=330, y_mmi_fin=430):
    """
    Retorna todo el código SVG del fondo celular y mitocondrial.
    Los complejos respiratorios se dibujan DESPUÉS, encima de la bicapa.

    Columnas de H⁺ excluidas para no chocar con:
      115, 185, 255, 325 -> cartel del acoplamiento quimiosmótico
      535                -> dominio soluble del Complejo III
      1025, 1095         -> flecha de retorno de H⁺ por la ATP sintasa
    """
    columnas_prohibidas = (115, 185, 255, 325, 535, 1025, 1095)

    return f"""
    <!-- ================================================================= -->
    <!-- CAPA 1: MATRIZ MITOCONDRIAL DE FONDO                              -->
    <!-- ================================================================= -->
    <rect x="0" y="0" width="{ancho}" height="{alto}" fill="url(#cteGradMatriz)" />

    <!-- Crestas mitocondriales (invaginaciones de la MMI, sólo en el margen libre) -->
    <g fill="url(#cteGradCresta)" stroke="#d97706" stroke-width="1.8" opacity="0.4">
      <path d="M 0 470 C 70 470, 92 510, 88 560 C 84 600, 50 620, 0 628 Z" />
      <path d="M {ancho} 500 C {ancho - 70} 500, {ancho - 92} 540, {ancho - 88} 590 C {ancho - 84} 630, {ancho - 50} 650, {ancho} 658 Z" />
      <path d="M 0 690 C 60 690, 80 715, 76 745 C 72 765, 40 775, 0 780 Z" />
    </g>

    <!-- ADN mitocondrial circular (ADNmt) y mitorribosomas -->
    <g fill="none" stroke="#b45309" stroke-width="1.2" opacity="0.22">
      <path d="M {ancho - 130} 560 C {ancho - 100} 534, {ancho - 60} 554, {ancho - 70} 592 C {ancho - 80} 630, {ancho - 122} 638, {ancho - 142} 606 Z" stroke-dasharray="4 3"/>
    </g>
    <g fill="#b45309" opacity="0.22">
      <circle cx="1235" cy="470" r="0"/>
      <circle cx="1090" cy="700" r="2.6"/><circle cx="1098" cy="703" r="2"/><circle cx="1094" cy="709" r="2.3"/>
      <circle cx="35" cy="720" r="2.6"/><circle cx="43" cy="723" r="2"/><circle cx="39" cy="729" r="2.3"/>
    </g>
    <g opacity="0.22">
      <ellipse cx="120" cy="700" rx="8" ry="5.5" fill="#78350f" stroke="#92400e" stroke-width="1.2"/>
      <ellipse cx="1060" cy="620" rx="8" ry="5.5" fill="#78350f" stroke="#92400e" stroke-width="1.2"/>
    </g>

    <!-- ================================================================= -->
    <!-- CAPA 2: CITOSOL, MME Y PORINA VDAC                                -->
    <!-- ================================================================= -->
    <path d="M 0 0 L {ancho} 0 L {ancho} {y_mme} Q {ancho / 2} {y_mme + 6} 0 {y_mme} Z" fill="url(#cteGradCitosol)" />
    <g opacity="0.28" stroke="#94a3b8" fill="none">
      <path d="M 20 22 Q 380 10 760 24 T {ancho - 20} 18" stroke-width="1.4" stroke-dasharray="8 6"/>
      <path d="M 40 50 Q 400 62 800 46 T {ancho - 40} 54" stroke-width="1.2" stroke-dasharray="6 5"/>
    </g>
    <text x="20" y="24" font-family="'Inter', sans-serif" font-size="9.5" font-weight="900"
          fill="#64748b" letter-spacing="1.2">CITOSOL • Lanzaderas malato-aspartato y glicerol-3-P</text>

    <!-- Membrana Mitocondrial Externa (MME) -->
    <path d="M 0 {y_mme} Q {ancho / 2} {y_mme + 6} {ancho} {y_mme}" fill="none" stroke="#78350f" stroke-width="5" stroke-linecap="round"/>
    <path d="M 0 {y_mme + 3} Q {ancho / 2} {y_mme + 9} {ancho} {y_mme + 3}" fill="none" stroke="#b45309" stroke-width="1.8" stroke-linecap="round"/>
    <text x="{ancho - 20}" y="{y_mme - 8}" font-family="'Inter', sans-serif" font-size="9"
          font-weight="700" fill="#78350f" text-anchor="end">Membrana Mitocondrial Externa (MME)</text>

    <!-- Porina VDAC (paso libre de nucleótidos y metabolitos pequeños) -->
    <g transform="translate(760, {y_mme - 11})">
      <rect x="0" y="0" width="34" height="22" rx="6" fill="#f97316" stroke="#c2410c" stroke-width="1.6"/>
      <ellipse cx="17" cy="11" rx="7.5" ry="5" fill="#e0f2fe" stroke="#38bdf8" stroke-width="1.1"/>
      <text x="17" y="29" font-family="'JetBrains Mono', monospace" font-size="7.5"
            font-weight="900" fill="#9a3412" text-anchor="middle">VDAC</text>
    </g>

    <!-- ================================================================= -->
    <!-- CAPA 3: ESPACIO INTERMEMBRANA Y GRADIENTE DE PROTONES             -->
    <!-- ================================================================= -->
    <path d="M 0 {y_mme + 6} Q {ancho / 2} {y_mme + 12} {ancho} {y_mme + 6}
             L {ancho} {y_eim_fin} Q {ancho / 2} {y_eim_fin + 6} 0 {y_eim_fin} Z"
          fill="url(#cteGradEIM)" />

    {_nube_protones(ancho, y_eim_ini + 66, y_eim_fin - 20, columnas_prohibidas)}

    <text x="20" y="{y_eim_ini + 22}" font-family="'Inter', sans-serif" font-size="9.5"
          font-weight="900" fill="#9a3412" letter-spacing="1">ESPACIO INTERMEMBRANA (EIM) • pH ≈ 6.8 • [H⁺] ALTA</text>

    <!-- Barra lateral del gradiente electroquímico -->
    <g transform="translate(18, {y_eim_ini + 40})">
      <rect x="0" y="0" width="11" height="{y_eim_fin - y_eim_ini - 60}" rx="5.5" fill="#fdba74" stroke="#ea580c" stroke-width="1.2"/>
      <text x="18" y="16" font-family="'JetBrains Mono', monospace" font-size="8"
            font-weight="700" fill="#9a3412">Δp ≈ 200 mV</text>
    </g>

    <!-- ================================================================= -->
    <!-- CAPA 4: MEMBRANA MITOCONDRIAL INTERNA (BICAPA LIPÍDICA)           -->
    <!-- ================================================================= -->
    <rect x="0" y="{y_mmi_ini}" width="{ancho}" height="{y_mmi_fin - y_mmi_ini}" fill="url(#cteGradBicapa)"/>
    <line x1="0" y1="{(y_mmi_ini + y_mmi_fin) / 2}" x2="{ancho}" y2="{(y_mmi_ini + y_mmi_fin) / 2}"
          stroke="#d97706" stroke-width="1.1" stroke-dasharray="5 4" opacity="0.6"/>
    {_fila_fosfolipidos(ancho, y_mmi_ini + 8, hacia_abajo=True)}
    {_fila_fosfolipidos(ancho, y_mmi_fin - 8, hacia_abajo=False)}
    <text x="520" y="{y_mmi_fin + 35}" font-family="'Inter', sans-serif" font-size="9"
          font-weight="800" fill="#92400e" text-anchor="middle">Membrana Mitocondrial Interna (MMI) • bicapa impermeable a H⁺</text>

    <!-- ================================================================= -->
    <!-- CAPA 5: MATRIZ MITOCONDRIAL (RÓTULO DE COMPARTIMENTO)             -->
    <!-- ================================================================= -->
    <text x="520" y="{y_mmi_fin + 54}" font-family="'Inter', sans-serif" font-size="9"
          font-weight="900" fill="#92400e" letter-spacing="1" text-anchor="middle">MATRIZ MITOCONDRIAL • pH ≈ 7.8 • [H⁺] BAJA</text>
    """
