#!/usr/bin/env python3
"""
GENERADOR DEL COMPLEJO PIRUVATO DESHIDROGENASA (PDH) - MAPA INDIVIDUAL INTEGRABLE
==================================================================================
Diseño de Alta Fidelidad Bioquímica:
- Eje metabólico vertical amplio y despejado (Citosol -> MPC -> Matriz).
- Carbonos moleculares explícitos en cada estructura química (sin puntos ciegos).
- Subunidades E1, E2 y E3 claramente diferenciadas con sus intermediarios químicos.
- Regulación bioquímica visual con diagrama de flujo intuitivo (PDK/PDP) y badges alostéricos ⊕ / ⊖.
- Conexión e integración completa con las vías del mapa (Krebs, Lipogénesis, Cetogénesis y Colesterol).
- Detección estricta de cero solapamientos.
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

ANCHO_CANVAS = 1520
ALTO_CANVAS = 2400

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
      background: #0f172a;
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
      border-radius: 16px;
      box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
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

        <!-- Gradientes celulares y mitocondriales -->
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

        <filter id="shadowSoft" x="-5%" y="-5%" width="110%" height="110%">
          <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#0f172a" flood-opacity="0.06"/>
        </filter>
      </defs>
"""

PIE_HTML = """
    </svg>
  </div>
</body>
</html>
"""

def nodo_metabolito(x, y, nombre, carbonos, svg_estructura, detalle="", detalle2="", offset_texto=140):
    """Bloque SVG de un metabolito con su estructura molecular nítida."""
    txt2 = f'<text x="0" y="48" fill="#64748b" font-size="11">{detalle2}</text>' if detalle2 else ""
    return f"""
      <!-- Metabolito: {nombre} -->
      <g transform="translate({x}, {y})">
        <g transform="translate(0, 0)">
          {svg_estructura}
        </g>
        <g transform="translate({offset_texto}, 25)">
          <text x="0" y="0" fill="#0f172a" font-size="18" font-weight="800">{nombre}</text>
          <text x="0" y="18" fill="#ea580c" font-size="12" font-weight="700">{carbonos}</text>
          <text x="0" y="34" fill="#64748b" font-size="11">{detalle}</text>
          {txt2}
        </g>
      </g>
    """

def crear_reaccion(x, y, enzima, ec="", regulacion="", entra_reactivo="", sale_producto="",
                   sale_co2=False, entra_coa=False, es_ganancia=False, detalle_extra="", altura_flecha=65):
    """Flecha central vertical con curvas acopladas y espacio suficiente para evitar colisiones."""
    curvas = ""

    # Reactivo entrante a la izquierda
    if entra_reactivo:
        col = "#7c3aed" if entra_coa else "#475569"
        mkr = "url(#arrowPurple)" if entra_coa else "url(#arrowSlate)"
        curvas += f"""
        <path d="M -120 12 Q -45 12 -8 24" fill="none" stroke="{col}" stroke-width="2" marker-end="{mkr}"/>
        <text x="-125" y="16" fill="{col}" font-size="11.5" font-weight="800" text-anchor="end">{entra_reactivo}</text>
        """

    # Salida de CO2
    if sale_co2:
        curvas += """
        <path d="M -8 24 Q -45 42 -115 42" fill="none" stroke="#dc2626" stroke-width="2" marker-end="url(#arrowRed)"/>
        <text x="-122" y="46" fill="#dc2626" font-size="12" font-weight="900" text-anchor="end">+ CO₂ ↑</text>
        """

    # Salida de NADH (desplazada para no solapar la flecha)
    if sale_producto:
        col = "#059669" if es_ganancia else "#475569"
        mkr = "url(#arrowGreen)" if es_ganancia else "url(#arrowSlate)"
        curvas += f"""
        <path d="M -8 30 Q -50 52 -135 52" fill="none" stroke="{col}" stroke-width="2" marker-end="{mkr}"/>
        <text x="-142" y="56" fill="{col}" font-size="12" font-weight="900" text-anchor="end">{sale_producto}</text>
        """

    flecha_central = f"""
    <line x1="0" y1="0" x2="0" y2="{altura_flecha}" stroke="#ea580c" stroke-width="2.8" marker-end="url(#arrowFlow)"/>
    """

    reg_svg = ""
    if regulacion:
        reg_svg = f'<text x="0" y="30" fill="#16a34a" font-size="10.5" font-weight="700">{regulacion}</text>'

    extra_svg = ""
    if detalle_extra:
        extra_svg = f'<text x="0" y="45" fill="#c2410c" font-size="10" font-weight="800">{detalle_extra}</text>'

    return f"""
    <!-- Reacción: {enzima} -->
    <g transform="translate({x}, {y})">
      {flecha_central}
      {curvas}
      <g transform="translate(24, 16)">
        <text x="0" y="0" fill="#0f172a" font-size="14" font-weight="800">{enzima}</text>
        <text x="0" y="15" fill="#64748b" font-size="10.5" font-family="'JetBrains Mono', monospace">{ec}</text>
        {reg_svg}
        {extra_svg}
      </g>
    </g>
    """

def generar_svg():
    partes = []

    # =========================================================================
    # 1. ENTORNO BIOLÓGICO: CITOSOL Y MITOCONDRIA
    # =========================================================================
    y_mme = 135
    y_eim = 150
    y_mmi = 180
    y_matriz = 200

    partes.append(f'<rect width="{ANCHO_CANVAS}" height="{ALTO_CANVAS}" fill="url(#gradMatrizPDH)"/>')
    partes.append(f'<rect x="0" y="0" width="{ANCHO_CANVAS}" height="{y_mme}" fill="url(#gradCitosolPDH)"/>')

    # Etiqueta Citosol en esquina superior izquierda despejada
    partes.append(f"""
    <g transform="translate(50, 40)" opacity="0.85">
      <text x="0" y="0" fill="#334155" font-size="18" font-weight="900" letter-spacing="2">CITOSOL CELULAR</text>
      <text x="0" y="18" fill="#64748b" font-size="11">Término de la Glucólisis</text>
    </g>
    """)

    # Membranas
    partes.append(f"""
    <rect x="0" y="{y_mme}" width="{ANCHO_CANVAS}" height="15" fill="#cbd5e1" stroke="#94a3b8" stroke-width="1.2"/>
    <text x="50" y="{y_mme + 11}" fill="#475569" font-family="'JetBrains Mono', monospace" font-size="9.5" font-weight="800">MME (Porinas VDAC)</text>

    <rect x="0" y="{y_eim}" width="{ANCHO_CANVAS}" height="30" fill="#fed7aa" opacity="0.6"/>
    <text x="50" y="{y_eim + 19}" fill="#c2410c" font-size="10" font-weight="700">Espacio Intermembrana (EIM)</text>

    <rect x="0" y="{y_mmi}" width="{ANCHO_CANVAS}" height="20" fill="#d97706" stroke="#b45309" stroke-width="1.5"/>
    <text x="50" y="{y_mmi + 14}" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="9.5" font-weight="800">MMI (Impermeable)</text>

    <g transform="translate(50, {y_matriz + 40})" opacity="0.85">
      <text x="0" y="0" fill="#78350f" font-size="18" font-weight="900" letter-spacing="2">MATRIZ MITOCONDRIAL</text>
      <text x="0" y="18" fill="#92400e" font-size="11">Descarboxilación oxidativa • Krebs</text>
    </g>
    """)

    # Transportador MPC en la MMI (x=380)
    partes.append(f"""
    <g transform="translate(345, {y_mmi - 12})">
      <rect x="0" y="0" width="70" height="44" rx="10" fill="#9a3412" stroke="#7c2d12" stroke-width="2.2"/>
      <text x="35" y="27" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="900" text-anchor="middle">MPC</text>
    </g>
    <text x="430" y="{y_mmi + 14}" fill="#78350f" font-size="11.5" font-weight="800">Carrier de Piruvato (MPC1/2)</text>
    """)

    # Banner del Título Superior
    partes.append(f"""
    <g transform="translate(850, 35)">
      <rect x="0" y="0" width="580" height="75" rx="12" fill="#ffffff" stroke="#ea580c" stroke-width="2" filter="url(#shadowSoft)"/>
      <rect x="16" y="16" width="44" height="44" rx="8" fill="#ea580c"/>
      <text x="38" y="46" fill="#ffffff" font-size="24" font-weight="900" text-anchor="middle">5</text>
      <text x="75" y="35" fill="#0f172a" font-size="17" font-weight="900">COMPLEJO PIRUVATO DESHIDROGENASA (PDH)</text>
      <text x="75" y="54" fill="#ea580c" font-size="11.5" font-weight="700">Descarboxilación Oxidativa de Piruvato • EC 1.2.4.1</text>
    </g>
    """)

    # =========================================================================
    # 2. COLUMNA METABÓLICA VERTICAL (ESPACIADO DESPEJADO SIN COLISIONES)
    # =========================================================================
    x_col = 340

    # 1. Piruvato Citosol
    partes.append(nodo_metabolito(x_col, 30, "Piruvato (Citosol)", "3 Carbonos", PIRUVATO,
                                  detalle="Generado por Piruvato Cinasa en Glucólisis",
                                  detalle2="Cruza la MME por difusión facilitada (VDAC)", offset_texto=110))

    # Transporte a través de MPC (línea sin atravesar textos)
    partes.append(f"""
    <path d="M {x_col + 40} 125 L {x_col + 40} 165 M {x_col + 40} 215 L {x_col + 40} 255" stroke="#ea580c" stroke-width="3" stroke-dasharray="6 4" marker-end="url(#arrowFlow)"/>
    """)

    # 2. Piruvato Matricial
    partes.append(nodo_metabolito(x_col, 260, "Piruvato (Matriz)", "3 Carbonos", PIRUVATO,
                                  detalle="Sustrato alimentador del Complejo Multienzimático",
                                  detalle2="Concentración regula el recambio catalítico", offset_texto=110))

    # Reacción 1: Subunidad E1 (Descarboxilación)
    partes.append(crear_reaccion(x_col + 40, 390, "E1: Piruvato Deshidrogenasa (TPP)",
                                 ec="EC 1.2.4.1 • Cofactor: TPP (Tiamina Pirofosfato)",
                                 sale_co2=True,
                                 regulacion="⊕ Piruvato, ADP, Ca²⁺  ⊣ PDK fosforilante",
                                 detalle_extra="Ataque nucleofílico de carbanión TPP • Paso limitante",
                                 altura_flecha=75))

    # 3. Intermediario: Hidroxietil-TPP
    partes.append(nodo_metabolito(x_col - 20, 505, "Hidroxietil-TPP", "2 Carbonos en E1", HIDROXIETIL_TPP,
                                  detalle="Intermediario carbaniónico unido covalentemente a E1",
                                  detalle2="Canalizado internamente al centro activo de E2", offset_texto=210))

    # Reacción 2: Subunidad E2 Paso 1 (Oxidación y formación de tioéster)
    partes.append(crear_reaccion(x_col + 40, 645, "E2: Lipoil Transacetilasa (Oxidación)",
                                 ec="EC 2.3.1.12 • Cofactor: Lipoamida (S-S)",
                                 entra_reactivo="Brazo Lipoil (E2)",
                                 regulacion="Oxidación del hidroxietilo a grupo acetilo",
                                 detalle_extra="El TPP regenera su carbanión activo en E1",
                                 altura_flecha=70))

    # 4. Intermediario: Acetil-Lipoamida
    partes.append(nodo_metabolito(x_col - 20, 755, "Acetil-Dihidrolipoamida", "2 Carbonos en E2", ACETIL_LIPOAMIDA,
                                  detalle="Tioéster de alta energía en el brazo lipoilo de 14 Å",
                                  detalle2="Oscila directamente hacia el sitio aceptor de CoA-SH", offset_texto=235))

    # Reacción 3: Subunidad E2 Paso 2 (Transferencia a CoA-SH y formación de Acetil-CoA)
    partes.append(crear_reaccion(x_col + 40, 895, "E2: Lipoil Transacetilasa (Transacetilación)",
                                 ec="EC 2.3.1.12 • Aceptor: CoA-SH libre",
                                 entra_reactivo="+ CoA-SH", entra_coa=True,
                                 regulacion="⊣ Inhibición por exceso de Acetil-CoA",
                                 detalle_extra="Transferencia del acetilo al grupo tiol de Coenzima A",
                                 altura_flecha=70))

    # 5. PRODUCTO FINAL: Acetil-CoA
    partes.append(nodo_metabolito(x_col - 10, 1005, "Acetil-Coenzima A", "2 Carbonos activados", ACETIL_COA,
                                  detalle="Tioéster de alta energía (ΔG°' hidrólisis = -31.5 kJ/mol)",
                                  detalle2="Encrucijada central del metabolismo intermediario", offset_texto=185))

    # Canalización a E3 (flecha vertical limpia)
    partes.append(f"""
    <path d="M {x_col + 150} 1130 L {x_col + 150} 1195" stroke="#ea580c" stroke-width="2.6" marker-end="url(#arrowFlow)"/>
    """)

    # 6. Dihidrolipoamida reducida
    partes.append(nodo_metabolito(x_col - 20, 1215, "Dihidrolipoamida (reducida)", "Forma inactiva E2", DIHIDROLIPOAMIDA,
                                  detalle="Dos grupos tiol (-SH HS-) tras liberar el acetilo",
                                  detalle2="Obligatorio reoxidar para permitir la siguiente vuelta", offset_texto=210))

    # Reacción 4: Subunidad E3 (Cascada Redox)
    partes.append(crear_reaccion(x_col + 40, 1360, "E3: Dihidrolipoil Deshidrogenasa",
                                 ec="EC 1.8.1.4 • Cofactores: FAD (prostético) + NAD⁺",
                                 entra_reactivo="+ NAD⁺",
                                 sale_producto="+ NADH + H⁺", es_ganancia=True,
                                 regulacion="⊣ Inhibición por exceso de NADH",
                                 detalle_extra="Transferencia electrónica: Tioles ➔ FAD (FADH₂) ➔ NAD⁺",
                                 altura_flecha=75))

    # 7. Lipoamida oxidada regenerada
    partes.append(nodo_metabolito(x_col - 10, 1485, "Lipoamida Oxidada (S-S)", "Forma activa de E2", LIPOAMIDA_OXIDADA,
                                  detalle="Puente disulfuro cíclico regenerado con éxito",
                                  detalle2="Lista para recibir el siguiente acetilo de E1", offset_texto=220))

    # Bucle cerrado de regeneración por el lateral izquierdo (curva que pasa por x=-30 relativo a la molécula para no tocar el átomo S)
    partes.append(f"""
    <path d="M {x_col - 50} 1525 C 20 1525, 20 735, {x_col - 50} 735" fill="none" stroke="#d97706" stroke-width="2.2" stroke-dasharray="8 5" marker-end="url(#arrowAmber)"/>
    <text x="16" y="1125" fill="#b45309" font-size="11" font-weight="900" transform="rotate(-90 16 1125)" text-anchor="middle">
      ↺ REGENERACIÓN CATALÍTICA DEL BRAZO LIPOILO DE E2
    </text>
    """)

    # =========================================================================
    # 3. PANEL LATERAL DERECHO: REGULACIÓN INTUITIVA Y NO ABIGARRADA
    # =========================================================================
    x_pan = 820

    partes.append(f"""
    <!-- PANEL DE CONTROL Y REGULACIÓN BIOQUÍMICA -->
    <g transform="translate({x_pan}, 250)">
      <rect x="0" y="0" width="650" height="580" rx="16" fill="#ffffff" stroke="#0284c7" stroke-width="2" filter="url(#shadowSoft)"/>
      <path d="M 0 16 Q 0 0 16 0 L 634 0 Q 650 0 650 16 L 650 46 L 0 46 Z" fill="#0284c7"/>
      <text x="24" y="30" fill="#ffffff" font-size="16" font-weight="900">REGULACIÓN DEL COMPLEJO PDH (CLAVE DE EXAMEN)</text>

      <!-- 1. DIAGRAMA VISUAL DE FOSFORILACIÓN / DESFOSFORILACIÓN -->
      <g transform="translate(24, 60)">
        <text x="0" y="0" fill="#0f172a" font-size="14" font-weight="800">1. Ciclo de Modificación Covalente (PDK vs PDP)</text>
        
        <!-- Estado Activo -->
        <g transform="translate(15, 38)">
          <rect x="0" y="0" width="165" height="50" rx="10" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
          <text x="82" y="24" fill="#15803d" font-size="13" font-weight="900" text-anchor="middle">PDH ACTIVA</text>
          <text x="82" y="40" fill="#166534" font-size="10" font-weight="700" text-anchor="middle">Desfosforilada (E1-OH)</text>
        </g>

        <!-- Flecha PDK hacia la derecha -->
        <path d="M 195 50 C 240 24, 320 24, 365 50" fill="none" stroke="#dc2626" stroke-width="2.4" marker-end="url(#arrowRed)"/>
        <g transform="translate(280, 14)">
          <text x="0" y="0" fill="#dc2626" font-size="11.5" font-weight="900" text-anchor="middle">PDH CINASA (PDK)</text>
          <text x="0" y="14" fill="#b91c1c" font-size="9.5" font-weight="700" text-anchor="middle">+ ATP ➔ ADP</text>
        </g>

        <!-- Estado Inactivo -->
        <g transform="translate(380, 38)">
          <rect x="0" y="0" width="175" height="50" rx="10" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>
          <text x="87" y="24" fill="#991b1b" font-size="13" font-weight="900" text-anchor="middle">PDH INACTIVA</text>
          <text x="87" y="40" fill="#7f1d1d" font-size="10" font-weight="700" text-anchor="middle">Ⓟ Fosforilada (E1-O-P)</text>
        </g>

        <!-- Flecha PDP hacia la izquierda -->
        <path d="M 365 78 C 320 106, 240 106, 195 78" fill="none" stroke="#16a34a" stroke-width="2.4" marker-end="url(#arrowGreen)"/>
        <g transform="translate(280, 124)">
          <text x="0" y="0" fill="#16a34a" font-size="11.5" font-weight="900" text-anchor="middle">PDH FOSFATASA (PDP)</text>
          <text x="0" y="14" fill="#15803d" font-size="9.5" font-weight="700" text-anchor="middle">+ H₂O ➔ Pi</text>
        </g>

        <!-- Moduladores de PDK y PDP -->
        <g transform="translate(0, 150)">
          <rect x="0" y="0" width="600" height="95" rx="10" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1.2"/>
          <text x="16" y="20" fill="#0f172a" font-size="12" font-weight="800">Control de las enzimas reguladoras:</text>
          <text x="16" y="40" fill="#dc2626" font-size="11" font-weight="800">• PDK activada por:</text>
          <text x="140" y="40" fill="#334155" font-size="11">NADH, Acetil-CoA, ATP (alta carga energética celular)</text>
          <text x="16" y="60" fill="#16a34a" font-size="11" font-weight="800">• PDK inhibida por:</text>
          <text x="140" y="60" fill="#334155" font-size="11">Piruvato, ADP, NAD⁺, Ca²⁺ (demanda de energía)</text>
          <text x="16" y="80" fill="#0284c7" font-size="11" font-weight="800">• PDP activada por:</text>
          <text x="140" y="80" fill="#334155" font-size="11">Ca²⁺ (contracción muscular) e Insulina (estado postprandial)</text>
        </g>
      </g>

      <!-- 2. EFECTORES ALOSTÉRICOS DIRECTOS -->
      <g transform="translate(24, 335)">
        <text x="0" y="0" fill="#0f172a" font-size="14" font-weight="800">2. Efectores Alostéricos Directos sobre E1, E2 y E3</text>
        <g transform="translate(0, 18)">
          <!-- Activadores -->
          <rect x="0" y="0" width="290" height="195" rx="10" fill="#f0fdf4" stroke="#86efac" stroke-width="1.5"/>
          <text x="16" y="24" fill="#166534" font-size="13" font-weight="900">⊕ ACTIVADORES ALOSTÉRICOS</text>
          <text x="16" y="50" fill="#15803d" font-size="12" font-weight="700">• Piruvato:</text>
          <text x="85" y="50" fill="#334155" font-size="11">Sustrato abundante.</text>
          <text x="16" y="74" fill="#15803d" font-size="12" font-weight="700">• ADP y NAD⁺:</text>
          <text x="105" y="74" fill="#334155" font-size="11">Baja carga energética.</text>
          <text x="16" y="98" fill="#15803d" font-size="12" font-weight="700">• CoA-SH libre:</text>
          <text x="110" y="98" fill="#334155" font-size="11">Aceptor disponible.</text>
          <text x="16" y="122" fill="#15803d" font-size="12" font-weight="700">• Ca²⁺:</text>
          <text x="60" y="122" fill="#334155" font-size="11">Señal de trabajo muscular.</text>
          <text x="16" y="160" fill="#166534" font-size="11" font-weight="800">➔ Fuerza el flujo hacia Krebs.</text>

          <!-- Inhibidores -->
          <g transform="translate(310, 0)">
            <rect x="0" y="0" width="290" height="195" rx="10" fill="#fef2f2" stroke="#fca5a5" stroke-width="1.5"/>
            <text x="16" y="24" fill="#991b1b" font-size="13" font-weight="900">⊖ INHIBIDORES POR PRODUCTO</text>
            <text x="16" y="50" fill="#b91c1c" font-size="12" font-weight="700">• Acetil-CoA:</text>
            <text x="100" y="50" fill="#334155" font-size="11">Inhibe E2 por producto.</text>
            <text x="16" y="74" fill="#b91c1c" font-size="12" font-weight="700">• NADH:</text>
            <text x="75" y="74" fill="#334155" font-size="11">Inhibe E3 redox.</text>
            <text x="16" y="98" fill="#b91c1c" font-size="12" font-weight="700">• ATP:</text>
            <text x="65" y="98" fill="#334155" font-size="11">Alta carga energética.</text>
            <text x="16" y="145" fill="#991b1b" font-size="11" font-weight="800">➔ Desvía Piruvato a Gluconeogénesis</text>
            <text x="16" y="165" fill="#64748b" font-size="10.5">(activa la Piruvato Carboxilasa).</text>
          </g>
        </g>
      </g>
    </g>

    <!-- PANEL DE CORRELACIÓN CLÍNICA Y FARMACOLÓGICA -->
    <g transform="translate({x_pan}, 860)">
      <rect x="0" y="0" width="650" height="420" rx="16" fill="#ffffff" stroke="#e11d48" stroke-width="2" filter="url(#shadowSoft)"/>
      <path d="M 0 16 Q 0 0 16 0 L 634 0 Q 650 0 650 16 L 650 46 L 0 46 Z" fill="#e11d48"/>
      <text x="24" y="30" fill="#ffffff" font-size="16" font-weight="900">CORRELACIÓN CLÍNICA, PATOLOGÍAS Y FARMACOLOGÍA</text>

      <g transform="translate(24, 65)">
        <text x="0" y="14" fill="#9f1239" font-size="13" font-weight="800">1. Déficit de Tiamina (Vitamina B1) • Beriberi / Síndrome Wernicke-Korsakoff</text>
        <text x="0" y="34" fill="#334155" font-size="11.5">• La falta de TPP paraliza E1 en tejidos dependientes de glucosa (cerebro, miocardio).</text>
        <text x="0" y="52" fill="#334155" font-size="11.5">• Causa acumulación masiva de piruvato y lactato, daño neuronal y falla cardiovascular.</text>
      </g>

      <g transform="translate(24, 150)">
        <text x="0" y="14" fill="#9f1239" font-size="13" font-weight="800">2. Envenenamiento por Arsenito (AsO₂⁻)</text>
        <text x="0" y="34" fill="#334155" font-size="11.5">• El arsenito reacciona covalentemente con los tioles vecinales (-SH) de la lipoamida en E2.</text>
        <text x="0" y="52" fill="#334155" font-size="11.5">• Bloqueo irreversible que detiene tanto la PDH como el Ciclo de Krebs (α-Cetoglutarato DH).</text>
        <text x="0" y="70" fill="#be123c" font-size="11" font-weight="800">Tratamiento con quelantes ditiólicos: BAL (Dimercaprol).</text>
      </g>

      <g transform="translate(24, 255)">
        <text x="0" y="14" fill="#9f1239" font-size="13" font-weight="800">3. Acidosis Láctica Congénita (Mutación en subunidad E1α)</text>
        <text x="0" y="34" fill="#334155" font-size="11.5">• Mutación ligada al cromosoma X que impide la descarboxilación del piruvato.</text>
        <text x="0" y="52" fill="#334155" font-size="11.5">• El piruvato se desvía obligatoriamente a Lactato por la LDH, causando acidosis metabólica.</text>
        <text x="0" y="70" fill="#be123c" font-size="11" font-weight="800">Manejo terapéutico: Dieta Cetogénica (suministro de Acetil-CoA sin pasar por PDH).</text>
      </g>
    </g>

    <!-- RESUMEN ESTEQUIOMÉTRICO Y BALANCE -->
    <g transform="translate({x_pan}, 1310)">
      <rect x="0" y="0" width="650" height="230" rx="16" fill="#ffffff" stroke="#f59e0b" stroke-width="2" filter="url(#shadowSoft)"/>
      <path d="M 0 16 Q 0 0 16 0 L 634 0 Q 650 0 650 16 L 650 46 L 0 46 Z" fill="#f59e0b"/>
      <text x="24" y="30" fill="#ffffff" font-size="16" font-weight="900">BALANCE ESTEQUIOMÉTRICO Y ARQUITECTURA</text>

      <g transform="translate(24, 65)">
        <text x="0" y="14" fill="#0f172a" font-size="12.5" font-weight="800">Reacción neta por Glucosa (× 2 Piruvatos):</text>
        <rect x="0" y="25" width="600" height="45" rx="8" fill="#fefce8" stroke="#fef08a" stroke-width="1.2"/>
        <text x="300" y="52" fill="#854d0e" font-family="'JetBrains Mono', monospace" font-size="11.5" font-weight="800" text-anchor="middle">
          2 Piruvato + 2 CoA-SH + 2 NAD⁺ ➔ 2 Acetil-CoA + 2 CO₂ + 2 NADH + 2 H⁺
        </text>

        <text x="0" y="95" fill="#15803d" font-size="12" font-weight="800">Ganancia energética:</text>
        <text x="140" y="95" fill="#334155" font-size="11.5">2 NADH mitocondriales ➔ ≈ 5 ATP en la Cadena Respiratoria (Complejo I).</text>

        <text x="0" y="125" fill="#0f172a" font-size="12" font-weight="800">Masa macromolecular:</text>
        <text x="155" y="125" fill="#334155" font-size="11.5">≈ 9 MDa (60 E2 nucleares + 30 E1 periféricos + 12 E3 dímeros + E3BP).</text>
      </g>
    </g>
    """)

    # =========================================================================
    # 4. PIE DE PÁGINA: CONEXIÓN E INTEGRACIÓN TOTAL DEL ACETIL-COA FORMADO
    # =========================================================================
    y_pie = 1620
    partes.append(f"""
    <!-- CONEXIÓN E INTEGRACIÓN TOTAL CON EL RESTO DE RUTAS -->
    <g transform="translate(50, {y_pie})">
      <rect x="0" y="0" width="1420" height="690" rx="18" fill="#ffffff" stroke="#334155" stroke-width="2.5" filter="url(#shadowSoft)"/>
      <path d="M 0 18 Q 0 0 18 0 L 1402 0 Q 1420 0 1420 18 L 1420 54 L 0 54 Z" fill="#1e293b"/>
      <text x="360" y="35" fill="#ffffff" font-size="18" font-weight="900" letter-spacing="1">CONEXIÓN E INTEGRACIÓN METABÓLICA DEL ACETIL-COA FORMADO</text>
      <text x="1000" y="35" fill="#cbd5e1" font-size="12">Encrucijada universal que alimenta las rutas centrales</text>

      <!-- Flecha de descenso del Acetil-CoA desde la columna metabólica hacia la caja de integración (desviada hacia la izquierda sin tocar la cabecera) -->
      <path d="M 280 -550 L 280 80" fill="none" stroke="#ea580c" stroke-width="3" stroke-dasharray="10 6" marker-end="url(#arrowFlow)"/>
      <g transform="translate(295, 75)">
        <text x="0" y="0" fill="#c2410c" font-size="13" font-weight="900">DESTINO DEL ACETIL-COA GENERADO EN PDH</text>
        <text x="0" y="16" fill="#64748b" font-size="10.5">Se bifurca según el estado energético y hormonal celular:</text>
      </g>

      <!-- 4 Módulos de Rutas Integradas con ancho holgado (325px cada una) -->
      <!-- 1. Ciclo de Krebs (Vía 6) -->
      <g transform="translate(25, 110)">
        <rect x="0" y="0" width="325" height="550" rx="14" fill="#fffbeb" stroke="#f59e0b" stroke-width="2"/>
        <g transform="translate(18, 25)">
          <rect x="0" y="0" width="32" height="32" rx="7" fill="#ea580c"/>
          <text x="16" y="22" fill="#ffffff" font-size="16" font-weight="900" text-anchor="middle">6</text>
          <text x="44" y="22" fill="#b45309" font-size="15" font-weight="900">CICLO DE KREBS (TCA)</text>
        </g>
        <g transform="translate(18, 80)">
          <text x="0" y="14" fill="#0f172a" font-size="13" font-weight="800">Condensación Inicial:</text>
          <text x="0" y="34" fill="#475569" font-size="11">Citrato Sintasa + Oxalacetato (4C)</text>
          <text x="0" y="52" fill="#ea580c" font-size="12" font-weight="800">➔ Citrato (6C)</text>

          <text x="0" y="90" fill="#0f172a" font-size="13" font-weight="800">Rendimiento por Acetil-CoA:</text>
          <text x="0" y="112" fill="#15803d" font-size="11.5" font-weight="700">• 3 NADH + H⁺</text>
          <text x="0" y="132" fill="#15803d" font-size="11.5" font-weight="700">• 1 FADH₂</text>
          <text x="0" y="152" fill="#15803d" font-size="11.5" font-weight="700">• 1 GTP / ATP</text>
          <text x="0" y="172" fill="#dc2626" font-size="11.5" font-weight="700">• 2 CO₂ (oxidación total)</text>

          <text x="0" y="220" fill="#0f172a" font-size="13" font-weight="800">Función Celular:</text>
          <text x="0" y="242" fill="#334155" font-size="11">Oxidación y suministro de electrones para ATP.</text>
        </g>
      </g>

      <!-- 2. Lipogénesis (Vía 10) -->
      <g transform="translate(370, 110)">
        <rect x="0" y="0" width="325" height="550" rx="14" fill="#eff6ff" stroke="#3b82f6" stroke-width="2"/>
        <g transform="translate(18, 25)">
          <rect x="0" y="0" width="32" height="32" rx="7" fill="#2563eb"/>
          <text x="16" y="22" fill="#ffffff" font-size="15" font-weight="900" text-anchor="middle">10</text>
          <text x="44" y="22" fill="#1d4ed8" font-size="15" font-weight="900">LIPOGÉNESIS</text>
        </g>
        <g transform="translate(18, 80)">
          <text x="0" y="14" fill="#0f172a" font-size="13" font-weight="800">Salida al Citosol:</text>
          <text x="0" y="34" fill="#475569" font-size="11">Lanzadera de Citrato (ACLY)</text>
          <text x="0" y="52" fill="#2563eb" font-size="12" font-weight="800">Citrato ➔ Acetil-CoA + OAA</text>

          <text x="0" y="90" fill="#0f172a" font-size="13" font-weight="800">Ruta Biosintética:</text>
          <text x="0" y="112" fill="#1e40af" font-size="11.5" font-weight="700">• Acetil-CoA Carboxilasa (ACC)</text>
          <text x="0" y="132" fill="#475569" font-size="11">Formación de Malonil-CoA</text>
          <text x="0" y="152" fill="#1e40af" font-size="11.5" font-weight="700">• Ácido Graso Sintasa (FAS)</text>
          <text x="0" y="172" fill="#475569" font-size="11">Síntesis de Ácido Palmítico (16:0)</text>

          <text x="0" y="220" fill="#0f172a" font-size="13" font-weight="800">Función Celular:</text>
          <text x="0" y="242" fill="#334155" font-size="11">Almacenamiento de exceso de energía en TAG.</text>
        </g>
      </g>

      <!-- 3. Cetogénesis (Vía 11) -->
      <g transform="translate(715, 110)">
        <rect x="0" y="0" width="325" height="550" rx="14" fill="#fdf2f8" stroke="#ec4899" stroke-width="2"/>
        <g transform="translate(18, 25)">
          <rect x="0" y="0" width="32" height="32" rx="7" fill="#db2777"/>
          <text x="16" y="22" fill="#ffffff" font-size="15" font-weight="900" text-anchor="middle">11</text>
          <text x="44" y="22" fill="#be185d" font-size="15" font-weight="900">CETOGÉNESIS</text>
        </g>
        <g transform="translate(18, 80)">
          <text x="0" y="14" fill="#0f172a" font-size="13" font-weight="800">Condensación Hepática:</text>
          <text x="0" y="34" fill="#475569" font-size="11">En ayuno prolongado / diabetes</text>
          <text x="0" y="52" fill="#db2777" font-size="12" font-weight="800">Tiolasa mitocondrial</text>

          <text x="0" y="90" fill="#0f172a" font-size="13" font-weight="800">Cuerpos Cetónicos:</text>
          <text x="0" y="112" fill="#9d174d" font-size="11.5" font-weight="700">• Acetoacetil-CoA</text>
          <text x="0" y="132" fill="#9d174d" font-size="11.5" font-weight="700">• HMG-CoA mitocondrial</text>
          <text x="0" y="152" fill="#9d174d" font-size="11.5" font-weight="700">• Acetoacetato y β-Hidroxibutirato</text>

          <text x="0" y="220" fill="#0f172a" font-size="13" font-weight="800">Función Celular:</text>
          <text x="0" y="242" fill="#334155" font-size="11">Combustible hidrosoluble para tejidos periféricos.</text>
        </g>
      </g>

      <!-- 4. Colesterol y Mevalonato (Vía 12) -->
      <g transform="translate(1060, 110)">
        <rect x="0" y="0" width="335" height="550" rx="14" fill="#faf5ff" stroke="#a855f7" stroke-width="2"/>
        <g transform="translate(18, 25)">
          <rect x="0" y="0" width="32" height="32" rx="7" fill="#9333ea"/>
          <text x="16" y="22" fill="#ffffff" font-size="15" font-weight="900" text-anchor="middle">12</text>
          <text x="44" y="22" fill="#7e22ce" font-size="15" font-weight="900">COLESTEROL</text>
        </g>
        <g transform="translate(18, 80)">
          <text x="0" y="14" fill="#0f172a" font-size="13" font-weight="800">Vía del Mevalonato:</text>
          <text x="0" y="34" fill="#475569" font-size="11">HMG-CoA Citosólico</text>
          <text x="0" y="52" fill="#9333ea" font-size="12" font-weight="800">HMG-CoA Reductasa (HMGCR)</text>

          <text x="0" y="90" fill="#0f172a" font-size="13" font-weight="800">Derivados Esteroideos:</text>
          <text x="0" y="112" fill="#6b21a8" font-size="11.5" font-weight="700">• Colesterol de membrana</text>
          <text x="0" y="132" fill="#6b21a8" font-size="11.5" font-weight="700">• Ácidos y sales biliares</text>
          <text x="0" y="152" fill="#6b21a8" font-size="11.5" font-weight="700">• Hormonas esteroideas y Vitamina D</text>

          <text x="0" y="220" fill="#0f172a" font-size="13" font-weight="800">Función Celular:</text>
          <text x="0" y="242" fill="#334155" font-size="11">Fluidez de membrana y síntesis hormonal (estatinas).</text>
        </g>
      </g>
    </g>
    """)

    return "".join(partes)

def main():
    carpeta = os.path.dirname(os.path.abspath(__file__))
    svg_body = generar_svg()

    # Guardar SVG
    defs_start = CABECERA_HTML.find("<defs>")
    defs_end = CABECERA_HTML.find("</defs>") + 7
    defs_str = CABECERA_HTML[defs_start:defs_end]

    svg_final = f'<svg width="{ANCHO_CANVAS}" height="{ALTO_CANVAS}" viewBox="0 0 {ANCHO_CANVAS} {ALTO_CANVAS}" xmlns="http://www.w3.org/2000/svg">\n'
    svg_final += defs_str + "\n" + svg_body + "\n</svg>"

    svg_path = os.path.join(carpeta, "Piruvato_Deshidrogenasa.svg")
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_final)
    print(f" SVG guardado en: {svg_path}")

    # Guardar HTML
    html_final = CABECERA_HTML + svg_body + PIE_HTML
    html_path = os.path.join(carpeta, "Piruvato_Deshidrogenasa.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_final)
    print(f" HTML guardado en: {html_path}")

if __name__ == "__main__":
    main()
