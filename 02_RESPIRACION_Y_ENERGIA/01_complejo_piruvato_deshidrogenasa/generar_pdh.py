#!/usr/bin/env python3
"""
GENERADOR DEL COMPLEJO PIRUVATO DESHIDROGENASA (PDH) - FORMATO EDITORIAL METABÓLICO
=====================================================================================
Diseñado bajo la misma arquitectura visual y estructural de todas las rutas del mapa:
- Formato de columna metabólica vertical en entorno biológico real (Citosol -> MME -> EIM -> MMI -> Matriz).
- Nodos de metabolitos libres con fórmulas moleculares vectoriales sin cajas delimitadoras.
- Flechas centrales de reacción metabólica con curvas de energía Bézier (+ CoA-SH, + NAD⁺, CO₂ ↑, + NADH + H⁺).
- Detalle molecular de las 3 enzimas (E1, E2, E3) acopladas paso a paso a lo largo de la columna.
- Panel lateral derecho con regulación alostérica/covalente (PDK vs PDP), control hormonal y correlación clínica.
- Conexión de salida al pie hacia las rutas integradas (Ciclo de Krebs, Lipogénesis, Cetogénesis y Colesterol).
"""

import os
from estructuras_pdh import (
    PIRUVATO,
    HIDROXIETIL_TPP,
    ACETIL_LIPOAMIDA,
    DIHIDROLIPOAMIDA,
    LIPOAMIDA_OXIDADA,
    ACETIL_COA
)

ANCHO_CANVAS = 1250
ALTO_CANVAS = 2250

CABECERA_HTML = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Complejo Piruvato Deshidrogenasa (PDH) • Vía 5</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;600;700;800&display=swap" rel="stylesheet">
  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: 'Inter', sans-serif;
      background: #e2e8f0;
      color: #0f172a;
      padding: 30px 15px;
      display: flex;
      flex-direction: column;
      align-items: center;
    }}
    .lienzo-svg {{
      width: {ANCHO_CANVAS}px;
      background: #ffffff;
      border: 1px solid #cbd5e1;
      border-radius: 12px;
      box-shadow: 0 20px 45px rgba(0, 0, 0, 0.14);
      overflow: hidden;
    }}
    svg {{ display: block; width: 100%; height: auto; }}
  </style>
</head>
<body>
  <div class="lienzo-svg">
    <svg width="{ANCHO_CANVAS}" height="{ALTO_CANVAS}" viewBox="0 0 {ANCHO_CANVAS} {ALTO_CANVAS}" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <!-- Flecha de flujo metabólico principal (Naranja) -->
        <marker id="arrowFlow" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
          <path d="M 0 0 L 6 3 L 0 6 Z" fill="#ea580c" />
        </marker>
        <!-- Flecha de gasto / reactivo (Roja) -->
        <marker id="arrowRed" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#dc2626" />
        </marker>
        <!-- Flecha de producto / energía (Verde esmeralda) -->
        <marker id="arrowGreen" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#059669" />
        </marker>
        <!-- Flecha de Coenzima A (Púrpura) -->
        <marker id="arrowPurple" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#7c3aed" />
        </marker>
        <!-- Flecha gris de subproducto (CO2) -->
        <marker id="arrowSlate" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#64748b" />
        </marker>
        <!-- Flecha dorada para cofactores redox -->
        <marker id="arrowAmber" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#d97706" />
        </marker>

        <!-- Gradientes celulares y mitocondriales idénticos a Krebs -->
        <linearGradient id="gradCitosolPDH" x1="0%" y1="0%" x2="0%" y2="100%">
          <stop offset="0%" stop-color="#f8fafc" />
          <stop offset="100%" stop-color="#e2e8f0" />
        </linearGradient>

        <linearGradient id="gradMatrizPDH" x1="0%" y1="0%" x2="0%" y2="100%">
          <stop offset="0%" stop-color="#fffbeb" />
          <stop offset="45%" stop-color="#fef3c7" stop-opacity="0.95" />
          <stop offset="85%" stop-color="#fef9c3" stop-opacity="0.9" />
          <stop offset="100%" stop-color="#fef08a" stop-opacity="0.85" />
        </linearGradient>

        <filter id="shadowBox" x="-5%" y="-5%" width="110%" height="110%">
          <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#0f172a" flood-opacity="0.08"/>
        </filter>
      </defs>
"""

PIE_HTML = """
    </svg>
  </div>
</body>
</html>
"""

def nodo_metabolito(x, y, nombre, carbonos, svg_estructura, detalle="", detalle2="", offset_texto=130):
    """Construye un metabolito libre con su estructura química y textos descriptivos."""
    txt2 = f'<text x="0" y="48" fill="#64748b" font-size="10.5">{detalle2}</text>' if detalle2 else ""
    return f"""
      <!-- Metabolito: {nombre} -->
      <g transform="translate({x}, {y})">
        <g transform="translate(0, 0)">
          {svg_estructura}
        </g>
        <g transform="translate({offset_texto}, 25)">
          <text x="0" y="0" fill="#0f172a" font-size="17" font-weight="800">{nombre}</text>
          <text x="0" y="18" fill="#ea580c" font-size="12" font-weight="700">{carbonos}</text>
          <text x="0" y="34" fill="#64748b" font-size="11">{detalle}</text>
          {txt2}
        </g>
      </g>
    """

def crear_reaccion(x, y, enzima, ec="", regulacion="", entra_reactivo="", sale_producto="",
                   sale_co2=False, entra_coa=False, es_ganancia=False, detalle_extra="", altura_flecha=55):
    """Genera la flecha central de reacción con curvas de reactivos/productos de energía."""
    curvas = ""

    # Entrada de reactivo (ej. + CoA-SH o + NAD+)
    if entra_reactivo:
        col = "#7c3aed" if entra_coa else "#475569"
        mkr = "url(#arrowPurple)" if entra_coa else "url(#arrowSlate)"
        curvas += f"""
        <path d="M -80 10 Q -30 10 -5 20" fill="none" stroke="{col}" stroke-width="1.8" marker-end="{mkr}"/>
        <text x="-85" y="14" fill="{col}" font-size="11" font-weight="800" text-anchor="end">{entra_reactivo}</text>
        """

    # Salida de CO2
    if sale_co2:
        curvas += """
        <path d="M -5 22 Q -30 36 -75 36" fill="none" stroke="#64748b" stroke-width="1.8" marker-end="url(#arrowSlate)"/>
        <text x="-80" y="40" fill="#dc2626" font-size="11" font-weight="900" text-anchor="end">+ CO₂ ↑</text>
        """

    # Salida de ganancia energética (ej. + NADH + H+)
    if sale_producto:
        col = "#059669" if es_ganancia else "#475569"
        mkr = "url(#arrowGreen)" if es_ganancia else "url(#arrowSlate)"
        curvas += f"""
        <path d="M -5 28 Q -30 42 -80 42" fill="none" stroke="{col}" stroke-width="1.8" marker-end="{mkr}"/>
        <text x="-85" y="46" fill="{col}" font-size="11.5" font-weight="900" text-anchor="end">{sale_producto}</text>
        """

    flecha_central = f"""
    <line x1="0" y1="0" x2="0" y2="{altura_flecha}" stroke="#ea580c" stroke-width="2.6" marker-end="url(#arrowFlow)"/>
    """

    reg_svg = ""
    if regulacion:
        reg_svg = f'<text x="0" y="27" fill="#16a34a" font-size="10" font-weight="700">{regulacion}</text>'

    extra_svg = ""
    if detalle_extra:
        extra_svg = f'<text x="0" y="40" fill="#c2410c" font-size="9.5" font-weight="800">{detalle_extra}</text>'

    return f"""
    <!-- Reacción: {enzima} -->
    <g transform="translate({x}, {y})">
      {flecha_central}
      {curvas}
      <g transform="translate(18, 14)">
        <text x="0" y="0" fill="#0f172a" font-size="13" font-weight="800">{enzima}</text>
        <text x="0" y="14" fill="#64748b" font-size="10" font-family="'JetBrains Mono', monospace">{ec}</text>
        {reg_svg}
        {extra_svg}
      </g>
    </g>
    """

def generar_svg():
    partes = []

    # =========================================================================
    # 1. ENTORNO BIOLÓGICO REAL: CITOSOL Y MITOCONDRIA
    # =========================================================================
    y_mme = 130
    y_eim = 144
    y_mmi = 172
    y_matriz = 190

    # Fondo de matriz mitocondrial
    partes.append(f'<rect width="{ANCHO_CANVAS}" height="{ALTO_CANVAS}" fill="url(#gradMatrizPDH)"/>')

    # Citosol superior
    partes.append(f'<rect x="0" y="0" width="{ANCHO_CANVAS}" height="{y_mme}" fill="url(#gradCitosolPDH)"/>')
    partes.append(f"""
    <!-- Etiqueta Citosol -->
    <g transform="translate(50, 45)" opacity="0.85">
      <text x="0" y="0" fill="#334155" font-size="18" font-weight="900" letter-spacing="2">CITOSOL CELULAR</text>
      <text x="0" y="18" fill="#64748b" font-size="11">Término de la Glucólisis • Origen del Piruvato</text>
    </g>
    """)

    # Membranas y EIM
    partes.append(f"""
    <!-- MME -->
    <rect x="0" y="{y_mme}" width="{ANCHO_CANVAS}" height="14" fill="#cbd5e1" stroke="#94a3b8" stroke-width="1.2"/>
    <text x="60" y="{y_mme + 10}" fill="#475569" font-family="'JetBrains Mono', monospace" font-size="9.5" font-weight="800">MEMBRANA MITOCONDRIAL EXTERNA (MME) - Porinas VDAC</text>

    <!-- Espacio Intermembrana (EIM) -->
    <rect x="0" y="{y_eim}" width="{ANCHO_CANVAS}" height="28" fill="#fed7aa" opacity="0.6"/>
    <text x="60" y="{y_eim + 18}" fill="#c2410c" font-size="10" font-weight="700">Espacio Intermembrana (EIM) • Acumulación de H⁺ de la CTE</text>

    <!-- MMI -->
    <rect x="0" y="{y_mmi}" width="{ANCHO_CANVAS}" height="18" fill="#d97706" stroke="#b45309" stroke-width="1.5"/>
    <text x="60" y="{y_mmi + 13}" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="9.5" font-weight="800">MEMBRANA MITOCONDRIAL INTERNA (MMI) - Impermeable • Complejos Respiratorios</text>

    <!-- Matriz Mitocondrial etiqueta -->
    <g transform="translate(50, {y_matriz + 35})" opacity="0.85">
      <text x="0" y="0" fill="#78350f" font-size="18" font-weight="900" letter-spacing="2">MATRIZ MITOCONDRIAL</text>
      <text x="0" y="18" fill="#92400e" font-size="11">Complejo Piruvato Deshidrogenasa • Ciclo de Krebs • Beta-Oxidación</text>
    </g>
    """)

    # Transportador MPC en la MMI
    partes.append(f"""
    <!-- Transportador MPC en la MMI (x=350) -->
    <g transform="translate(315, {y_mmi - 12})">
      <rect x="0" y="0" width="70" height="42" rx="10" fill="#9a3412" stroke="#7c2d12" stroke-width="2.2"/>
      <text x="35" y="26" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="900" text-anchor="middle">MPC</text>
    </g>
    <text x="400" y="{y_mmi + 13}" fill="#78350f" font-size="11" font-weight="800">Carrier de Piruvato (MPC1/MPC2) • Simport H⁺</text>
    """)

    # =========================================================================
    # 2. ENCABEZADO EDITORIAL DE LA VÍA
    # =========================================================================
    partes.append(f"""
    <g transform="translate(750, 40)">
      <rect x="0" y="0" width="450" height="70" rx="10" fill="#ffffff" stroke="#ea580c" stroke-width="2" filter="url(#shadowBox)"/>
      <rect x="15" y="15" width="40" height="40" rx="8" fill="#ea580c"/>
      <text x="35" y="42" fill="#ffffff" font-size="22" font-weight="900" text-anchor="middle">5</text>
      <text x="68" y="32" fill="#0f172a" font-size="16" font-weight="900">PIRUVATO DESHIDROGENASA (PDH)</text>
      <text x="68" y="50" fill="#ea580c" font-size="11" font-weight="700">Descarboxilación Oxidativa de Piruvato • EC 1.2.4.1</text>
    </g>
    """)

    # =========================================================================
    # 3. COLUMNA METABÓLICA CENTRAL (MECANISMO PASO A PASO)
    # =========================================================================
    x_col = 270

    # 1. Piruvato en Citosol
    partes.append(nodo_metabolito(x_col, 50, "Piruvato (Citosol)", "3C", PIRUVATO,
                                  detalle="Generado por Piruvato Cinasa en Glucólisis",
                                  detalle2="Cruza la MME libremente por VDAC", offset_texto=100))

    # Paso a través de la MMI hacia la matriz
    partes.append(f"""
    <path d="M {x_col + 40} 145 L {x_col + 40} 240" stroke="#ea580c" stroke-width="3" stroke-dasharray="6 4" marker-end="url(#arrowFlow)"/>
    """)

    # 2. Piruvato en Matriz Mitocondrial
    partes.append(nodo_metabolito(x_col, 250, "Piruvato (Matriz)", "3C", PIRUVATO,
                                  detalle="Sustrato de entrada a la máquina multienzimática",
                                  detalle2="Concentración regula recambio catalítico", offset_texto=100))

    # Reacción 1: Subunidad E1 (Descarboxilación)
    partes.append(crear_reaccion(x_col + 40, 375, "E1: Piruvato Deshidrogenasa (TPP)",
                                 ec="EC 1.2.4.1 • Cofactor: TPP (Tiamina Pi)",
                                 sale_co2=True,
                                 regulacion="⊕ Piruvato, ADP, Ca²⁺  ⊣ PDK fosforilante",
                                 detalle_extra="Paso limitante • Ataque nucleofílico de carbanión TPP",
                                 altura_flecha=65))

    # 3. Intermediario 1: Hidroxietil-TPP
    partes.append(nodo_metabolito(x_col - 10, 475, "Hidroxietil-TPP", "2C unido a E1", HIDROXIETIL_TPP,
                                  detalle="Intermediario carbaniónico covalente",
                                  detalle2="Canalizado internamente hacia E2", offset_texto=150))

    # Reacción 2: Transferencia a Subunidad E2 (Oxidación y formación de tioéster)
    partes.append(crear_reaccion(x_col + 40, 605, "E2: Lipoil Transacetilasa (Paso 1)",
                                 ec="EC 2.3.1.12 • Cofactor: Lipoamida (S-S)",
                                 entra_reactivo="Brazo Lipoil (E2)",
                                 regulacion="Oxidación del carbanión a acetilo",
                                 detalle_extra="El TPP regenera su carbanión activo para E1",
                                 altura_flecha=60))

    # 4. Intermediario 2: Acetil-Lipoamida
    partes.append(nodo_metabolito(x_col - 20, 700, "Acetil-Dihidrolipoamida", "2C activado", ACETIL_LIPOAMIDA,
                                  detalle="Tioéster de alta energía en el brazo lipoil de 14 Å",
                                  detalle2="Oscila hacia el sitio aceptor de Coenzima A", offset_texto=190))

    # Reacción 3: Transacetilación a CoA-SH (Liberación del producto principal)
    partes.append(crear_reaccion(x_col + 40, 835, "E2: Lipoil Transacetilasa (Paso 2)",
                                 ec="EC 2.3.1.12 • Aceptor: CoA-SH",
                                 entra_reactivo="+ CoA-SH", entra_coa=True,
                                 regulacion="⊣ Inhibición por Acetil-CoA alto",
                                 detalle_extra="Transferencia del grupo acetilo al tiol de CoA",
                                 altura_flecha=60))

    # 5. PRODUCTO FINAL: Acetil-CoA
    partes.append(nodo_metabolito(x_col - 10, 930, "Acetil-Coenzima A", "2C activado", ACETIL_COA,
                                  detalle="Tioéster de alta energía (ΔG°' hidrólisis = -31.5 kJ/mol)",
                                  detalle2="Combustible de Krebs y precursor de Lípidos / Cetonas", offset_texto=170))

    # Reacción 4: Subunidad E3 - Reoxidación de Dihidrolipoamida
    partes.append(f"""
    <!-- Canalización de E2 reducido a E3 -->
    <path d="M {x_col + 40} 1055 L {x_col + 40} 1125" stroke="#ea580c" stroke-width="2.6" marker-end="url(#arrowFlow)"/>
    """)
    partes.append(nodo_metabolito(x_col - 20, 1135, "Dihidrolipoamida (reducida)", "Forma inactiva", DIHIDROLIPOAMIDA,
                                  detalle="Dos grupos tiol (-SH HS-) tras ceder el acetilo",
                                  detalle2="Debe reoxidarse para permitir nuevas vueltas", offset_texto=180))

    # Reacción 5: E3 reoxida lipoamida y genera NADH
    partes.append(crear_reaccion(x_col + 40, 1265, "E3: Dihidrolipoil Deshidrogenasa",
                                 ec="EC 1.8.1.4 • Cofactores: FAD (prostético) + NAD⁺",
                                 entra_reactivo="+ NAD⁺",
                                 sale_producto="+ NADH + H⁺", es_ganancia=True,
                                 regulacion="⊣ Inhibición por NADH alto",
                                 detalle_extra="Cascada: Tioles ➔ FAD (FADH₂) ➔ NAD⁺",
                                 altura_flecha=65))

    # 6. Regeneración de Lipoamida activa
    partes.append(nodo_metabolito(x_col - 10, 1370, "Lipoamida Oxidada (S-S)", "Forma activa de E2", LIPOAMIDA_OXIDADA,
                                  detalle="Puente disulfuro cíclico regenerado con éxito",
                                  detalle2="Lista para recibir el siguiente acetilo de E1", offset_texto=170))

    # Flecha de ciclo cerrado que vuelve hacia arriba
    partes.append(f"""
    <!-- Bucle de retorno de E2 oxidado -->
    <path d="M {x_col - 20} 1410 C 80 1410, 80 680, {x_col - 20} 680" fill="none" stroke="#d97706" stroke-width="2" stroke-dasharray="8 5" marker-end="url(#arrowAmber)"/>
    <text x="65" y="1050" fill="#b45309" font-size="11" font-weight="900" transform="rotate(-90 65 1050)" text-anchor="middle">
      ↺ REGENERACIÓN CATALÍTICA DEL BRAZO LIPOILO DE E2
    </text>
    """)

    # =========================================================================
    # 4. PANEL LATERAL DERECHO: REGULACIÓN METABÓLICA Y CORRELACIÓN CLÍNICA
    # =========================================================================
    x_pan = 680

    # Panel 1: Regulación Alostérica y Modificación Covalente
    partes.append(f"""
    <g transform="translate({x_pan}, 250)">
      <rect x="0" y="0" width="520" height="490" rx="12" fill="#ffffff" stroke="#0284c7" stroke-width="2" filter="url(#shadowBox)"/>
      
      <!-- Cabecera panel -->
      <path d="M 0 12 Q 0 0 12 0 L 508 0 Q 520 0 520 12 L 520 40 L 0 40 Z" fill="#0284c7"/>
      <text x="20" y="26" fill="#ffffff" font-size="14" font-weight="800">REGULACIÓN DEL COMPLEJO PDH (CRUCIAL EXAMEN)</text>
      
      <!-- Modificación Covalente -->
      <g transform="translate(20, 55)">
        <text x="0" y="15" fill="#0f172a" font-size="13" font-weight="800">1. Modificación Covalente (PDK vs PDP)</text>
        <text x="0" y="32" fill="#64748b" font-size="11">La fosforilación de una Serina específica en E1 inactiva el complejo:</text>

        <!-- Esquema PDK / PDP -->
        <g transform="translate(20, 48)">
          <!-- PDH Activa -->
          <rect x="0" y="0" width="130" height="38" rx="8" fill="#dcfce7" stroke="#16a34a" stroke-width="1.6"/>
          <text x="65" y="18" fill="#15803d" font-size="11" font-weight="900" text-anchor="middle">PDH ACTIVA</text>
          <text x="65" y="30" fill="#166534" font-size="9" text-anchor="middle">(Desfosforilada)</text>

          <!-- Flecha a Inactiva (PDK) -->
          <path d="M 140 10 C 185 -5, 205 -5, 250 10" fill="none" stroke="#dc2626" stroke-width="1.8" marker-end="url(#arrowRed)"/>
          <text x="195" y="-8" fill="#dc2626" font-size="10" font-weight="800" text-anchor="middle">PDK (+ATP)</text>

          <!-- PDH Inactiva -->
          <rect x="260" y="0" width="140" height="38" rx="8" fill="#fee2e2" stroke="#dc2626" stroke-width="1.6"/>
          <text x="330" y="18" fill="#991b1b" font-size="11" font-weight="900" text-anchor="middle">PDH INACTIVA</text>
          <text x="330" y="30" fill="#7f1d1d" font-size="9" text-anchor="middle">(Ⓟ Fosforilada)</text>

          <!-- Flecha a Activa (PDP) -->
          <path d="M 250 30 C 205 45, 185 45, 140 30" fill="none" stroke="#16a34a" stroke-width="1.8" marker-end="url(#arrowGreen)"/>
          <text x="195" y="55" fill="#16a34a" font-size="10" font-weight="800" text-anchor="middle">PDP (+H₂O, -Pi)</text>
        </g>
      </g>

      <!-- Moduladores alostéricos de PDK y PDP -->
      <g transform="translate(20, 175)">
        <rect x="0" y="0" width="480" height="110" rx="8" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1"/>
        <text x="12" y="20" fill="#0f172a" font-size="11.5" font-weight="800">Control de las Enzimas Reguladoras:</text>
        <text x="12" y="38" fill="#dc2626" font-size="11" font-weight="700">• PDK (Cinasa):</text>
        <text x="110" y="38" fill="#334155" font-size="11">⊕ Activada por NADH, Acetil-CoA, ATP (exceso energético).</text>
        <text x="110" y="54" fill="#334155" font-size="11">⊖ Inhibida por Piruvato, ADP, NAD⁺, Ca²⁺.</text>
        <text x="12" y="74" fill="#16a34a" font-size="11" font-weight="700">• PDP (Fosfatasa):</text>
        <text x="120" y="74" fill="#334155" font-size="11">⊕ Activada por Ca²⁺ (ejercicio muscular) e Insulina (hígado).</text>
        <text x="120" y="90" fill="#475569" font-size="10.5">Restaura el flujo oxidativo cuando hay demanda de ATP.</text>
      </g>

      <!-- Efectores alostéricos directos -->
      <g transform="translate(20, 300)">
        <text x="0" y="15" fill="#0f172a" font-size="13" font-weight="800">2. Efectores Alostéricos Directos sobre el Complejo</text>
        <g transform="translate(0, 25)">
          <rect x="0" y="0" width="235" height="145" rx="8" fill="#f0fdf4" stroke="#86efac" stroke-width="1.2"/>
          <text x="12" y="22" fill="#166534" font-size="11.5" font-weight="900">⊕ ACTIVADORES DIRECTOS</text>
          <text x="12" y="42" fill="#15803d" font-size="11" font-weight="700">• Piruvato:</text>
          <text x="75" y="42" fill="#334155" font-size="11">Sustrato abundante.</text>
          <text x="12" y="60" fill="#15803d" font-size="11" font-weight="700">• ADP y NAD⁺:</text>
          <text x="95" y="60" fill="#334155" font-size="11">Baja energía celular.</text>
          <text x="12" y="78" fill="#15803d" font-size="11" font-weight="700">• CoA-SH libre:</text>
          <text x="95" y="78" fill="#334155" font-size="11">Aceptor disponible.</text>
          <text x="12" y="96" fill="#15803d" font-size="11" font-weight="700">• Ca²⁺:</text>
          <text x="50" y="96" fill="#334155" font-size="11">Demanda contráctil.</text>
          <text x="12" y="125" fill="#166534" font-size="10" font-weight="700">➔ Fuerza flujo hacia Krebs.</text>
        </g>

        <g transform="translate(245, 25)">
          <rect x="0" y="0" width="235" height="145" rx="8" fill="#fef2f2" stroke="#fca5a5" stroke-width="1.2"/>
          <text x="12" y="22" fill="#991b1b" font-size="11.5" font-weight="900">⊖ INHIBIDORES DIRECTOS</text>
          <text x="12" y="42" fill="#b91c1c" font-size="11" font-weight="700">• Acetil-CoA:</text>
          <text x="90" y="42" fill="#334155" font-size="11">Inhibe E2 por producto.</text>
          <text x="12" y="60" fill="#b91c1c" font-size="11" font-weight="700">• NADH:</text>
          <text x="65" y="60" fill="#334155" font-size="11">Inhibe E3 por producto.</text>
          <text x="12" y="78" fill="#b91c1c" font-size="11" font-weight="700">• ATP:</text>
          <text x="55" y="78" fill="#334155" font-size="11">Alta carga energética.</text>
          <text x="12" y="105" fill="#991b1b" font-size="10" font-weight="700">➔ Desvía piruvato a Gluconeogénesis</text>
          <text x="12" y="122" fill="#475569" font-size="9.5">(vía Piruvato Carboxilasa).</text>
        </g>
      </g>
    </g>
    """)

    # Panel 2: Correlación Clínica y Nutricional
    partes.append(f"""
    <g transform="translate({x_pan}, 760)">
      <rect x="0" y="0" width="520" height="380" rx="12" fill="#ffffff" stroke="#e11d48" stroke-width="2" filter="url(#shadowBox)"/>
      
      <!-- Cabecera panel -->
      <path d="M 0 12 Q 0 0 12 0 L 508 0 Q 520 0 520 12 L 520 40 L 0 40 Z" fill="#e11d48"/>
      <text x="20" y="26" fill="#ffffff" font-size="14" font-weight="800">RELEVANCIA CLÍNICA, TOXICOLOGÍA Y FARMACOLOGÍA</text>

      <!-- 1. Beriberi y Déficit B1 -->
      <g transform="translate(20, 55)">
        <text x="0" y="14" fill="#9f1239" font-size="12" font-weight="800">1. Déficit de Tiamina (Vitamina B1) • Beriberi / Wernicke-Korsakoff</text>
        <text x="0" y="32" fill="#334155" font-size="11">• La falta de TPP paraliza E1 en tejidos altamente dependientes de glucosa (cerebro, miocardio).</text>
        <text x="0" y="48" fill="#334155" font-size="11">• Provoca acumulación masiva de piruvato y lactato, causando ataxia, encefalopatía y falla cardíaca.</text>
      </g>

      <!-- 2. Envenenamiento por Arsénico -->
      <g transform="translate(20, 130)">
        <text x="0" y="14" fill="#9f1239" font-size="12" font-weight="800">2. Envenenamiento por Arsenito (AsO₂⁻)</text>
        <text x="0" y="32" fill="#334155" font-size="11">• El arsenito reacciona covalentemente con los dos grupos -SH vecinales de la dihidrolipoamida de E2.</text>
        <text x="0" y="48" fill="#334155" font-size="11">• Forma un quelato cíclico irreversible que detiene tanto la PDH como la α-Cetoglutarato DH.</text>
        <text x="0" y="64" fill="#be123c" font-size="10.5" font-weight="700">Tratamiento de rescate: Agentes quelantes con ditioles como BAL (Dimercaprol).</text>
      </g>

      <!-- 3. Acidosis Láctica Congénita -->
      <g transform="translate(20, 220)">
        <text x="0" y="14" fill="#9f1239" font-size="12" font-weight="800">3. Acidosis Láctica Congénita (Mutación E1α ligada al X)</text>
        <text x="0" y="32" fill="#334155" font-size="11">• El bloqueo genético de E1 impide la entrada de piruvato a la mitocondria.</text>
        <text x="0" y="48" fill="#334155" font-size="11">• El piruvato citosólico se reduce obligatoriamente a lactato (LDH), produciendo acidosis metabólica severa.</text>
        <text x="0" y="66" fill="#be123c" font-size="10.5" font-weight="700">Estrategia dietética: Dieta Cetogénica rica en grasas para generar Acetil-CoA sin pasar por PDH.</text>
      </g>
    </g>
    """)

    # Panel 3: Arquitectura Multienzimática y Estequiometría
    partes.append(f"""
    <g transform="translate({x_pan}, 1160)">
      <rect x="0" y="0" width="520" height="280" rx="12" fill="#ffffff" stroke="#f59e0b" stroke-width="2" filter="url(#shadowBox)"/>
      <path d="M 0 12 Q 0 0 12 0 L 508 0 Q 520 0 520 12 L 520 40 L 0 40 Z" fill="#f59e0b"/>
      <text x="20" y="26" fill="#ffffff" font-size="14" font-weight="800">ESTRUCTURA CUATERNARIA Y BALANCE ESTEQUIOMÉTRICO</text>

      <g transform="translate(20, 55)">
        <text x="0" y="15" fill="#0f172a" font-size="12" font-weight="800">Estequiometría del Complejo en Mamíferos (Masa ≈ 9 MDa):</text>
        <text x="0" y="35" fill="#334155" font-size="11">• <tspan font-weight="700">Núcleo Central E2:</tspan> 60 copias organizadas en un dodecaedro simétrico (brazo lipoil de 14 Å).</text>
        <text x="0" y="52" fill="#334155" font-size="11">• <tspan font-weight="700">Periferia E1:</tspan> 30 tetrámeros (α₂β₂) unidos al exterior del núcleo.</text>
        <text x="0" y="69" fill="#334155" font-size="11">• <tspan font-weight="700">Periferia E3:</tspan> 12 dímeros acoplados mediante la proteína adaptadora E3BP (Protein X).</text>
        <text x="0" y="86" fill="#334155" font-size="11">• <tspan font-weight="700">Reguladoras:</tspan> Copias integradas de PDK1-4 y PDP1-2.</text>

        <rect x="0" y="105" width="480" height="75" rx="8" fill="#fefce8" stroke="#fef08a" stroke-width="1.2"/>
        <text x="15" y="125" fill="#854d0e" font-size="11.5" font-weight="800">Balance Neto por Molécula de Glucosa (x2 Piruvatos):</text>
        <text x="15" y="145" fill="#0f172a" font-size="12" font-weight="700">2 Piruvato + 2 CoA-SH + 2 NAD⁺ ➔ 2 Acetil-CoA + 2 CO₂ + 2 NADH + 2 H⁺</text>
        <text x="15" y="165" fill="#15803d" font-size="11" font-weight="800">Ganancia respiratoria directa: 2 NADH ➔ ≈ 5 ATP en la Cadena Respiratoria</text>
      </g>
    </g>
    """)

    # =========================================================================
    # 5. PIE DE PÁGINA EDITORIAL: INTEGRACIÓN METABÓLICA Y SALIDA HACIA OTRAS VÍAS
    # =========================================================================
    y_pie = 1520
    partes.append(f"""
    <!-- CONTENEDOR DE DESTINOS INTEGRADOS -->
    <g transform="translate(50, {y_pie})">
      <rect x="0" y="0" width="1150" height="650" rx="16" fill="#ffffff" stroke="#475569" stroke-width="2" filter="url(#shadowBox)"/>
      <path d="M 0 16 Q 0 0 16 0 L 1134 0 Q 1150 0 1150 16 L 1150 50 L 0 50 Z" fill="#1e293b"/>
      <text x="25" y="32" fill="#ffffff" font-size="16" font-weight="900" letter-spacing="1">CONEXIÓN E INTEGRACIÓN METABÓLICA DEL ACETIL-COA FORMADO</text>
      <text x="700" y="32" fill="#94a3b8" font-size="11">Encrucijada metabólica universal que conecta con 4 vías clave</text>

      <!-- Flecha de descenso desde el Acetil-CoA formado arriba hacia los 4 destinos -->
      <path d="M 260 -480 L 260 70" fill="none" stroke="#ea580c" stroke-width="3" stroke-dasharray="10 6" marker-end="url(#arrowFlow)"/>
      <text x="275" y="60" fill="#c2410c" font-size="12" font-weight="900">ACETIL-COA ENTRA A LOS DESTINOS CELULARES</text>

      <!-- 4 Cuadros de Destinos -->
      <!-- Destino 1: Ciclo de Krebs (Vía 6) -->
      <g transform="translate(30, 90)">
        <rect x="0" y="0" width="255" height="520" rx="12" fill="#fffbeb" stroke="#f59e0b" stroke-width="2"/>
        <g transform="translate(15, 25)">
          <rect x="0" y="0" width="30" height="30" rx="6" fill="#ea580c"/>
          <text x="15" y="21" fill="#ffffff" font-size="16" font-weight="900" text-anchor="middle">6</text>
          <text x="40" y="20" fill="#b45309" font-size="14" font-weight="900">CICLO DE KREBS</text>
        </g>
        <g transform="translate(15, 75)">
          <text x="0" y="14" fill="#0f172a" font-size="12" font-weight="800">Condensación Inicial:</text>
          <text x="0" y="32" fill="#475569" font-size="11">Citrato Sintasa + Oxalacetato (4C)</text>
          <text x="0" y="48" fill="#ea580c" font-size="11" font-weight="700">➔ Citrato (6C)</text>

          <text x="0" y="80" fill="#0f172a" font-size="12" font-weight="800">Rendimiento por Acetil-CoA:</text>
          <text x="0" y="102" fill="#15803d" font-size="11" font-weight="700">• 3 NADH + H⁺</text>
          <text x="0" y="122" fill="#15803d" font-size="11" font-weight="700">• 1 FADH₂</text>
          <text x="0" y="142" fill="#15803d" font-size="11" font-weight="700">• 1 GTP / ATP</text>
          <text x="0" y="162" fill="#dc2626" font-size="11" font-weight="700">• 2 CO₂ (oxidación total)</text>

          <text x="0" y="200" fill="#0f172a" font-size="12" font-weight="800">Objetivo Celular:</text>
          <text x="0" y="220" fill="#334155" font-size="11">Generación máxima de ATP en la Cadena de Transporte de Electrones.</text>
        </g>
      </g>

      <!-- Destino 2: Lipogénesis (Vía 10) -->
      <g transform="translate(310, 90)">
        <rect x="0" y="0" width="255" height="520" rx="12" fill="#eff6ff" stroke="#3b82f6" stroke-width="2"/>
        <g transform="translate(15, 25)">
          <rect x="0" y="0" width="30" height="30" rx="6" fill="#2563eb"/>
          <text x="15" y="21" fill="#ffffff" font-size="15" font-weight="900" text-anchor="middle">10</text>
          <text x="40" y="20" fill="#1d4ed8" font-size="14" font-weight="900">LIPOGÉNESIS</text>
        </g>
        <g transform="translate(15, 75)">
          <text x="0" y="14" fill="#0f172a" font-size="12" font-weight="800">Exportación al Citosol:</text>
          <text x="0" y="32" fill="#475569" font-size="11">Vía Lanzadera de Citrato</text>
          <text x="0" y="48" fill="#2563eb" font-size="11" font-weight="700">ATP-Citrato Liasa (ACLY)</text>

          <text x="0" y="80" fill="#0f172a" font-size="12" font-weight="800">Paso Limitante:</text>
          <text x="0" y="102" fill="#1e40af" font-size="11" font-weight="700">• Acetil-CoA Carboxilasa (ACC)</text>
          <text x="0" y="122" fill="#475569" font-size="11">Formación de Malonil-CoA</text>
          <text x="0" y="142" fill="#1e40af" font-size="11" font-weight="700">• Ácido Graso Sintasa (FAS)</text>
          <text x="0" y="162" fill="#475569" font-size="11">Formación de Palmitato (16:0)</text>

          <text x="0" y="200" fill="#0f172a" font-size="12" font-weight="800">Objetivo Celular:</text>
          <text x="0" y="220" fill="#334155" font-size="11">Almacenamiento de exceso calórico en forma de Triacilglicéridos (TAG).</text>
        </g>
      </g>

      <!-- Destino 3: Cetogénesis (Vía 11) -->
      <g transform="translate(590, 90)">
        <rect x="0" y="0" width="255" height="520" rx="12" fill="#fdf2f8" stroke="#ec4899" stroke-width="2"/>
        <g transform="translate(15, 25)">
          <rect x="0" y="0" width="30" height="30" rx="6" fill="#db2777"/>
          <text x="15" y="21" fill="#ffffff" font-size="15" font-weight="900" text-anchor="middle">11</text>
          <text x="40" y="20" fill="#be185d" font-size="14" font-weight="900">CETOGÉNESIS</text>
        </g>
        <g transform="translate(15, 75)">
          <text x="0" y="14" fill="#0f172a" font-size="12" font-weight="800">Matriz Hepática:</text>
          <text x="0" y="32" fill="#475569" font-size="11">Condensación en ayuno o diabetes</text>
          <text x="0" y="48" fill="#db2777" font-size="11" font-weight="700">Tiolasa mitocondrial</text>

          <text x="0" y="80" fill="#0f172a" font-size="12" font-weight="800">Intermediarios Clave:</text>
          <text x="0" y="102" fill="#9d174d" font-size="11" font-weight="700">• Acetoacetil-CoA</text>
          <text x="0" y="122" fill="#9d174d" font-size="11" font-weight="700">• HMG-CoA mitocondrial</text>
          <text x="0" y="142" fill="#9d174d" font-size="11" font-weight="700">• Acetoacetato</text>
          <text x="0" y="162" fill="#9d174d" font-size="11" font-weight="700">• β-Hidroxibutirato</text>

          <text x="0" y="200" fill="#0f172a" font-size="12" font-weight="800">Objetivo Celular:</text>
          <text x="0" y="220" fill="#334155" font-size="11">Exportación de combustible hidrosoluble hacia cerebro y músculo.</text>
        </g>
      </g>

      <!-- Destino 4: Colesterol y Mevalonato (Vía 12) -->
      <g transform="translate(870, 90)">
        <rect x="0" y="0" width="250" height="520" rx="12" fill="#faf5ff" stroke="#a855f7" stroke-width="2"/>
        <g transform="translate(15, 25)">
          <rect x="0" y="0" width="30" height="30" rx="6" fill="#9333ea"/>
          <text x="15" y="21" fill="#ffffff" font-size="15" font-weight="900" text-anchor="middle">12</text>
          <text x="40" y="20" fill="#7e22ce" font-size="14" font-weight="900">COLESTEROL</text>
        </g>
        <g transform="translate(15, 75)">
          <text x="0" y="14" fill="#0f172a" font-size="12" font-weight="800">Citosol Hepático:</text>
          <text x="0" y="32" fill="#475569" font-size="11">Vía del Mevalonato</text>
          <text x="0" y="48" fill="#9333ea" font-size="11" font-weight="700">HMG-CoA Reductasa (HMGCR)</text>

          <text x="0" y="80" fill="#0f172a" font-size="12" font-weight="800">Productos Esteroideos:</text>
          <text x="0" y="102" fill="#6b21a8" font-size="11" font-weight="700">• Colesterol libre y esterificado</text>
          <text x="0" y="122" fill="#6b21a8" font-size="11" font-weight="700">• Sales y Ácidos Biliares</text>
          <text x="0" y="142" fill="#6b21a8" font-size="11" font-weight="700">• Hormonas Esteroideas</text>
          <text x="0" y="162" fill="#6b21a8" font-size="11" font-weight="700">• Vitamina D₃</text>

          <text x="0" y="200" fill="#0f172a" font-size="12" font-weight="800">Objetivo Celular:</text>
          <text x="0" y="220" fill="#334155" font-size="11">Fluidez de biomembranas y señalización endocrina (Diana de Estatinas).</text>
        </g>
      </g>
    </g>
    """)

    return "".join(partes)

def main():
    carpeta = os.path.dirname(os.path.abspath(__file__))
    svg_body = generar_svg()
    
    # 1. Guardar SVG completo
    svg_final = f'<svg width="{ANCHO_CANVAS}" height="{ALTO_CANVAS}" viewBox="0 0 {ANCHO_CANVAS} {ALTO_CANVAS}" xmlns="http://www.w3.org/2000/svg">\n'
    # extraer los defs de CABECERA_HTML
    defs_start = CABECERA_HTML.find("<defs>")
    defs_end = CABECERA_HTML.find("</defs>") + 7
    defs_str = CABECERA_HTML[defs_start:defs_end]
    svg_final += defs_str + "\n" + svg_body + "\n</svg>"

    svg_path = os.path.join(carpeta, "Piruvato_Deshidrogenasa.svg")
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_final)
    print(f" SVG guardado en: {svg_path}")

    # 2. Guardar HTML visor
    html_final = CABECERA_HTML + svg_body + PIE_HTML
    html_path = os.path.join(carpeta, "Piruvato_Deshidrogenasa.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_final)
    print(f" HTML guardado en: {html_path}")

if __name__ == "__main__":
    main()
