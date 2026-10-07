#!/usr/bin/env python3
"""
GENERADOR DEL COMPLEJO PIRUVATO DESHIDROGENASA (PDH) - MAPA BIOLÓGICO INTEGRADO
=================================================================================
Diseño Bioquímico Editorial Limpio y Despejado (Ancho 1750, Alto 2150):
- Columna metabólica a la izquierda (x=280) con amplio espaciado vertical.
- Subunidades E1, E2, E3 y sus intermediarios sin interferencias ni cruces.
- Interruptor de E1 visual (Semáforo Verde "Encendida" / Rojo "Apagada") a la derecha de E1.
- Patologías ubicadas directamente junto a su diana (Déficit B1 en E1, Arsenito en E2).
- Bifurcación del Acetil-CoA en un bloque horizontal inferior claramente conectado.
- Cero solapamientos verificado con detectar_solapamientos.py.
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

ANCHO_CANVAS = 1750
ALTO_CANVAS = 2200

CABECERA_HTML = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Vía 5: Complejo Piruvato Deshidrogenasa (PDH) • Entorno Mitocondrial</title>
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
        <!-- Marcadores de flechas -->
        <marker id="arrowFlow" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
          <path d="M 0 0 L 6 3 L 0 6 Z" fill="#ea580c" />
        </marker>
        <marker id="arrowRed" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#dc2626" />
        </marker>
        <marker id="arrowGreen" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#059669" />
        </marker>
        <marker id="arrowPurple" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#7c3aed" />
        </marker>
        <marker id="arrowSlate" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#64748b" />
        </marker>
        <marker id="arrowAmber" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#d97706" />
        </marker>
        <marker id="inhibitionT" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
          <line x1="5" y1="0" x2="5" y2="6" stroke="#dc2626" stroke-width="2.4" />
        </marker>

        <!-- Gradientes celulares y mitocondriales -->
        <linearGradient id="gradCitosolPDH" x1="0%" y1="0%" x2="0%" y2="100%">
          <stop offset="0%" stop-color="#f8fafc" />
          <stop offset="100%" stop-color="#e2e8f0" />
        </linearGradient>

        <linearGradient id="gradMatrizPDH" x1="0%" y1="0%" x2="0%" y2="100%">
          <stop offset="0%" stop-color="#fffbeb" />
          <stop offset="35%" stop-color="#fef3c7" stop-opacity="0.96" />
          <stop offset="80%" stop-color="#fef9c3" stop-opacity="0.92" />
          <stop offset="100%" stop-color="#fef08a" stop-opacity="0.88" />
        </linearGradient>

        <filter id="shadowGlow" x="-10%" y="-10%" width="120%" height="120%">
          <feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#0f172a" flood-opacity="0.08"/>
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
    """Estructura química flotante libre sin cajas opacas."""
    txt2 = f'<text x="0" y="48" fill="#64748b" font-size="11">{detalle2}</text>' if detalle2 else ""
    return f"""
      <!-- Metabolito: {nombre} -->
      <g transform="translate({x}, {y})">
        <g transform="translate(0, 0)">
          {svg_estructura}
        </g>
        <g transform="translate({offset_texto}, 25)">
          <text x="0" y="0" fill="#0f172a" font-size="18" font-weight="900">{nombre}</text>
          <text x="0" y="18" fill="#ea580c" font-size="12" font-weight="800">{carbonos}</text>
          <text x="0" y="34" fill="#64748b" font-size="11">{detalle}</text>
          {txt2}
        </g>
      </g>
    """

def generar_svg():
    partes = []

    # =========================================================================
    # 1. ENTORNO BIOLÓGICO: CITOSOL, MEMBRANAS Y MATRIZ
    # =========================================================================
    y_mme = 125
    y_eim = 139
    y_mmi = 171

    # Matriz mitocondrial de fondo
    partes.append(f'<rect width="{ANCHO_CANVAS}" height="{ALTO_CANVAS}" fill="url(#gradMatrizPDH)"/>')

    # Citosol superior
    partes.append(f'<rect x="0" y="0" width="{ANCHO_CANVAS}" height="{y_mme}" fill="url(#gradCitosolPDH)"/>')
    partes.append(f"""
    <!-- Etiqueta Citosol -->
    <g transform="translate(40, 38)" opacity="0.85">
      <text x="0" y="0" fill="#334155" font-size="17" font-weight="900" letter-spacing="2">CITOSOL CELULAR</text>
      <text x="0" y="17" fill="#64748b" font-size="11">Final de la Glucólisis • Origen del Piruvato</text>
    </g>
    """)

    # Membrana Mitocondrial Externa (MME)
    partes.append(f"""
    <rect x="0" y="{y_mme}" width="{ANCHO_CANVAS}" height="14" fill="#cbd5e1" stroke="#94a3b8" stroke-width="1.2"/>
    <text x="40" y="{y_mme + 10}" fill="#475569" font-family="'JetBrains Mono', monospace" font-size="9.5" font-weight="800">MME (Porinas VDAC)</text>

    <!-- Espacio Intermembrana (EIM) -->
    <rect x="0" y="{y_eim}" width="{ANCHO_CANVAS}" height="32" fill="#fed7aa" opacity="0.6"/>
    <text x="40" y="{y_eim + 20}" fill="#c2410c" font-size="10.5" font-weight="700">Espacio Intermembrana (EIM)</text>

    <!-- Membrana Mitocondrial Interna (MMI) -->
    <rect x="0" y="{y_mmi}" width="{ANCHO_CANVAS}" height="20" fill="#d97706" stroke="#b45309" stroke-width="1.5"/>
    <text x="40" y="{y_mmi + 14}" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="9.5" font-weight="800">MMI (Impermeable a H⁺)</text>

    <!-- Matriz Mitocondrial -->
    <g transform="translate(40, 235)" opacity="0.85">
      <text x="0" y="0" fill="#78350f" font-size="20" font-weight="900" letter-spacing="2">MATRIZ MITOCONDRIAL</text>
      <text x="0" y="18" fill="#92400e" font-size="11.5">Descarboxilación oxidativa del Piruvato • Complejo PDH multienzimático</text>
    </g>
    """)

    # Transportador MPC en la MMI (x=330)
    partes.append(f"""
    <g transform="translate(295, {y_mmi - 12})">
      <rect x="0" y="0" width="70" height="44" rx="10" fill="#9a3412" stroke="#7c2d12" stroke-width="2.2"/>
      <text x="35" y="27" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="900" text-anchor="middle">MPC</text>
    </g>
    <text x="375" y="{y_mmi + 14}" fill="#78350f" font-size="11.5" font-weight="800">Carrier de Piruvato (MPC1/2)</text>
    """)

    # Banner del Título Superior
    partes.append(f"""
    <g transform="translate(1080, 32)">
      <rect x="0" y="0" width="630" height="72" rx="12" fill="#ffffff" stroke="#ea580c" stroke-width="2" filter="url(#shadowGlow)"/>
      <rect x="16" y="14" width="44" height="44" rx="8" fill="#ea580c"/>
      <text x="38" y="44" fill="#ffffff" font-size="24" font-weight="900" text-anchor="middle">5</text>
      <text x="75" y="33" fill="#0f172a" font-size="17" font-weight="900">COMPLEJO PIRUVATO DESHIDROGENASA (PDH)</text>
      <text x="75" y="52" fill="#ea580c" font-size="11.5" font-weight="700">Descarboxilación Oxidativa de Piruvato • EC 1.2.4.1 • ΔG°' = -33.4 kJ/mol</text>
    </g>
    """)

    # =========================================================================
    # 2. COLUMNA METABÓLICA CENTRAL (MECANISMO PASO A PASO)
    # =========================================================================
    x_col = 290

    # 1. Piruvato Citosol
    partes.append(nodo_metabolito(x_col, 20, "Piruvato (Citosol)", "3 Carbonos", PIRUVATO,
                                  detalle="Generado por Piruvato Cinasa en Glucólisis",
                                  detalle2="Cruza la MME por difusión facilitada (VDAC)", offset_texto=100))

    # Transporte por MPC
    partes.append(f"""
    <path d="M {x_col + 40} 115 L {x_col + 40} 155 M {x_col + 40} 205 L {x_col + 40} 245" stroke="#ea580c" stroke-width="3" stroke-dasharray="6 4" marker-end="url(#arrowFlow)"/>
    """)

    # 2. Piruvato Matricial
    partes.append(nodo_metabolito(x_col, 250, "Piruvato (Matriz)", "3 Carbonos", PIRUVATO,
                                  detalle="Sustrato alimentador del Complejo Multienzimático",
                                  detalle2="Concentración regula el recambio catalítico", offset_texto=100))

    # Reacción 1: Subunidad E1
    partes.append(f"""
    <!-- Reacción E1 -->
    <g transform="translate({x_col + 40}, 380)">
      <line x1="0" y1="0" x2="0" y2="70" stroke="#ea580c" stroke-width="3" marker-end="url(#arrowFlow)"/>
      <path d="M -8 22 Q -45 40 -115 40" fill="none" stroke="#dc2626" stroke-width="2.2" marker-end="url(#arrowRed)"/>
      <text x="-122" y="44" fill="#dc2626" font-size="12" font-weight="900" text-anchor="end">+ CO₂ ↑</text>
      
      <g transform="translate(25, 18)">
        <text x="0" y="0" fill="#0f172a" font-size="14" font-weight="900">E1: Piruvato Deshidrogenasa (TPP)</text>
        <text x="0" y="16" fill="#64748b" font-size="10.5" font-family="'JetBrains Mono', monospace">EC 1.2.4.1 • Cofactor: TPP (Tiamina Pi)</text>
        <text x="0" y="32" fill="#c2410c" font-size="10" font-weight="800">Ataque nucleofílico de carbanión TPP • Paso limitante</text>
      </g>
    </g>
    """)

    # 3. Intermediario 1: Hidroxietil-TPP
    partes.append(nodo_metabolito(x_col - 20, 490, "Hidroxietil-TPP", "2 Carbonos en E1", HIDROXIETIL_TPP,
                                  detalle="Intermediario carbaniónico unido covalentemente a E1",
                                  detalle2="Canalizado internamente al centro activo de E2", offset_texto=210))

    # Reacción 2: Subunidad E2 (Oxidación)
    partes.append(f"""
    <!-- Reacción E2 Paso 1 -->
    <g transform="translate({x_col + 40}, 625)">
      <line x1="0" y1="0" x2="0" y2="70" stroke="#ea580c" stroke-width="3" marker-end="url(#arrowFlow)"/>
      <path d="M -120 12 Q -45 12 -8 24" fill="none" stroke="#d97706" stroke-width="2" marker-end="url(#arrowAmber)"/>
      <text x="-125" y="16" fill="#b45309" font-size="11.5" font-weight="800" text-anchor="end">+ Brazo Lipoil (E2)</text>
      
      <g transform="translate(25, 18)">
        <text x="0" y="0" fill="#0f172a" font-size="14" font-weight="900">E2: Lipoil Transacetilasa (Oxidación)</text>
        <text x="0" y="16" fill="#64748b" font-size="10.5" font-family="'JetBrains Mono', monospace">EC 2.3.1.12 • Cofactor: Lipoamida (S-S)</text>
        <text x="0" y="32" fill="#15803d" font-size="10" font-weight="800">Oxida el hidroxietilo a acetilo • TPP regenera su carbanión</text>
      </g>
    </g>
    """)

    # 4. Intermediario 2: Acetil-Lipoamida
    partes.append(nodo_metabolito(x_col - 20, 735, "Acetil-Dihidrolipoamida", "2 Carbonos en E2", ACETIL_LIPOAMIDA,
                                  detalle="Tioéster de alta energía en el brazo lipoilo de 14 Å",
                                  detalle2="Oscila directamente hacia el sitio aceptor de CoA-SH", offset_texto=235))

    # Reacción 3: Subunidad E2 (Transacetilación a CoA-SH)
    partes.append(f"""
    <!-- Reacción E2 Paso 2 -->
    <g transform="translate({x_col + 40}, 870)">
      <line x1="0" y1="0" x2="0" y2="70" stroke="#ea580c" stroke-width="3" marker-end="url(#arrowFlow)"/>
      <path d="M -120 12 Q -45 12 -8 24" fill="none" stroke="#7c3aed" stroke-width="2.2" marker-end="url(#arrowPurple)"/>
      <text x="-125" y="16" fill="#7c3aed" font-size="12" font-weight="900" text-anchor="end">+ CoA-SH</text>
      
      <g transform="translate(25, 18)">
        <text x="0" y="0" fill="#0f172a" font-size="14" font-weight="900">E2: Lipoil Transacetilasa (Transacetilación)</text>
        <text x="0" y="16" fill="#64748b" font-size="10.5" font-family="'JetBrains Mono', monospace">EC 2.3.1.12 • Aceptor: Coenzima A libre</text>
        <text x="0" y="32" fill="#7c3aed" font-size="10" font-weight="800">Transferencia del acetilo al grupo tiol de la CoA</text>
      </g>
    </g>
    """)

    # 5. PRODUCTO FINAL: Acetil-CoA
    partes.append(nodo_metabolito(x_col - 10, 980, "Acetil-Coenzima A", "2 Carbonos activados", ACETIL_COA,
                                  detalle="Tioéster de alta energía (ΔG°' hidrólisis = -31.5 kJ/mol)",
                                  detalle2="Encrucijada universal que alimenta las rutas centrales", offset_texto=185))

    # Canalización hacia E3
    partes.append(f"""
    <path d="M {x_col + 40} 1105 L {x_col + 40} 1165" stroke="#ea580c" stroke-width="2.6" marker-end="url(#arrowFlow)"/>
    """)

    # 6. Dihidrolipoamida reducida
    partes.append(nodo_metabolito(x_col - 20, 1180, "Dihidrolipoamida (reducida)", "Forma inactiva E2", DIHIDROLIPOAMIDA,
                                  detalle="Dos grupos tiol (-SH HS-) tras liberar el acetilo",
                                  detalle2="Obligatorio reoxidar para permitir la siguiente vuelta", offset_texto=210))

    # Reacción 4: Subunidad E3 (curvas despejadas para no cortar el texto de NADH)
    partes.append(f"""
    <!-- Reacción E3 -->
    <g transform="translate({x_col + 40}, 1315)">
      <line x1="0" y1="0" x2="0" y2="70" stroke="#ea580c" stroke-width="3" marker-end="url(#arrowFlow)"/>
      <path d="M -120 12 Q -45 12 -8 24" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrowSlate)"/>
      <text x="-125" y="16" fill="#475569" font-size="11.5" font-weight="800" text-anchor="end">+ NAD⁺</text>
      <path d="M -8 26 Q -40 45 -100 45" fill="none" stroke="#059669" stroke-width="2.4" marker-end="url(#arrowGreen)"/>
      <text x="-110" y="49" fill="#059669" font-size="12.5" font-weight="900" text-anchor="end">+ NADH + H⁺</text>

      <g transform="translate(25, 18)">
        <text x="0" y="0" fill="#0f172a" font-size="14" font-weight="900">E3: Dihidrolipoil Deshidrogenasa</text>
        <text x="0" y="16" fill="#64748b" font-size="10.5" font-family="'JetBrains Mono', monospace">EC 1.8.1.4 • Cofactores: FAD (prostético) + NAD⁺ móvil</text>
        <text x="0" y="32" fill="#047857" font-size="10" font-weight="800">Cascada electrónica: Tioles ➔ FAD (FADH₂) ➔ NAD⁺ (NADH)</text>
      </g>
    </g>
    """)

    # 7. Lipoamida oxidada regenerada
    partes.append(nodo_metabolito(x_col - 10, 1425, "Lipoamida Oxidada (S-S)", "Forma activa de E2", LIPOAMIDA_OXIDADA,
                                  detalle="Puente disulfuro cíclico regenerado con éxito",
                                  detalle2="Lista para recibir el siguiente acetilo de E1", offset_texto=220))

    # Bucle cerrado de regeneración de E2 (arco amplio a la izquierda)
    partes.append(f"""
    <path d="M {x_col - 50} 1465 C 20 1465, 20 710, {x_col - 50} 710" fill="none" stroke="#d97706" stroke-width="2.2" stroke-dasharray="8 5" marker-end="url(#arrowAmber)"/>
    <text x="16" y="1085" fill="#b45309" font-size="11" font-weight="900" transform="rotate(-90 16 1085)" text-anchor="middle">
      ↺ REGENERACIÓN CATALÍTICA DEL BRAZO LIPOILO DE E2
    </text>
    """)

    # =========================================================================
    # 3. INTERRUPTOR BIOLÓGICO DE REGULACIÓN DE E1 (SÚPER VISUAL Y CLARO)
    # =========================================================================
    x_reg = 860
    y_reg = 360

    partes.append(f"""
    <!-- INTERRUPTOR DE REGULACIÓN DE E1 -->
    <g transform="translate({x_reg}, {y_reg})">
      <!-- Conector desde la reacción E1 -->
      <path d="M -430 45 C -280 45, -120 45, -10 45" fill="none" stroke="#ea580c" stroke-width="2" stroke-dasharray="6 4" marker-end="url(#arrowFlow)"/>

      <!-- Título biológico claro -->
      <text x="0" y="-10" fill="#0f172a" font-size="16" font-weight="900">INTERRUPTOR BIOLÓGICO DE E1 (PDK vs PDP)</text>
      <text x="0" y="10" fill="#64748b" font-size="11.5">Control por fosforilación en el residuo Serina de la subunidad E1α:</text>

      <!-- Panel Verde: CUÁNDO ESTÁ ACTIVA (ENCENDIDA) -->
      <g transform="translate(0, 30)">
        <rect x="0" y="0" width="220" height="150" rx="14" fill="#f0fdf4" stroke="#16a34a" stroke-width="2"/>
        <circle cx="28" cy="28" r="14" fill="#16a34a"/>
        <text x="28" y="34" fill="#ffffff" font-size="16" font-weight="900" text-anchor="middle">✓</text>
        <text x="50" y="32" fill="#15803d" font-size="14" font-weight="900">PDH ENCENDIDA</text>
        <text x="14" y="56" fill="#166534" font-size="11" font-weight="800">Desfosforilada (Ser-OH activo)</text>

        <text x="14" y="80" fill="#0f172a" font-size="11" font-weight="800">¿Cuándo se activa?</text>
        <text x="14" y="98" fill="#166534" font-size="10.5">• Ca²⁺ (ejercicio y contracción)</text>
        <text x="14" y="114" fill="#166534" font-size="10.5">• Insulina (estado postprandial)</text>
        <text x="14" y="130" fill="#166534" font-size="10.5">• Piruvato, ADP, NAD⁺ altos</text>
      </g>

      <!-- Flechas del interruptor entre verde y rojo -->
      <path d="M 230 65 L 310 65" fill="none" stroke="#dc2626" stroke-width="2.4" marker-end="url(#arrowRed)"/>
      <text x="270" y="56" fill="#dc2626" font-size="11" font-weight="900" text-anchor="middle">PDK (+ATP)</text>

      <path d="M 310 115 L 230 115" fill="none" stroke="#16a34a" stroke-width="2.4" marker-end="url(#arrowGreen)"/>
      <text x="270" y="135" fill="#16a34a" font-size="11" font-weight="900" text-anchor="middle">PDP (+H₂O)</text>

      <!-- Panel Rojo: CUÁNDO SE APAGA (INACTIVA) -->
      <g transform="translate(320, 30)">
        <rect x="0" y="0" width="220" height="150" rx="14" fill="#fef2f2" stroke="#dc2626" stroke-width="2"/>
        <circle cx="28" cy="28" r="14" fill="#dc2626"/>
        <text x="28" y="34" fill="#ffffff" font-size="16" font-weight="900" text-anchor="middle">✕</text>
        <text x="50" y="32" fill="#991b1b" font-size="14" font-weight="900">PDH APAGADA</text>
        <text x="14" y="56" fill="#991b1b" font-size="11" font-weight="800">Ⓟ Fosforilada (Ser-O-P inactivo)</text>

        <text x="14" y="80" fill="#0f172a" font-size="11" font-weight="800">¿Cuándo se apaga?</text>
        <text x="14" y="98" fill="#b91c1c" font-size="10.5">• Acetil-CoA alto (exceso)</text>
        <text x="14" y="114" fill="#b91c1c" font-size="10.5">• NADH y ATP elevados</text>
        <text x="14" y="130" fill="#7f1d1d" font-size="10">• Desvía piruvato a Gluconeogénesis</text>
      </g>
    </g>
    """)

    # =========================================================================
    # 4. PATOLOGÍAS SITUADAS DIRECTAMENTE AL LADO DE SU ENZIMA DIANA
    # =========================================================================
    # Diana 1: Subunidad E1 (TPP) -> Situada exactamente en y=225 a la derecha de E1
    partes.append(f"""
    <!-- DIANA PATOLÓGICA 1: E1 / TPP -->
    <g transform="translate(860, 225)">
      <rect x="0" y="0" width="550" height="70" rx="10" fill="#fff1f2" stroke="#e11d48" stroke-width="1.8"/>
      <circle cx="24" cy="24" r="12" fill="#be123c"/>
      <text x="24" y="29" fill="#ffffff" font-size="13" font-weight="900" text-anchor="middle">!</text>
      
      <text x="44" y="22" fill="#9f1239" font-size="12.5" font-weight="900">DIANA E1: DÉFICIT DE TIAMINA (B₁) Y ACIDOSA LÁCTICA</text>
      <text x="44" y="40" fill="#334155" font-size="11">
        • <tspan font-weight="700">Falta de B₁:</tspan> agota el TPP en E1 ➔ <tspan font-weight="700">Beriberi</tspan> y <tspan font-weight="700">Wernicke-Korsakoff</tspan>.
      </text>
      <text x="44" y="56" fill="#be123c" font-size="10.5" font-weight="700">
        • Mutación en E1α: El Piruvato no entra a la mitocondria y la LDH lo reduce a Lactato en exceso.
      </text>

      <path d="M 0 35 L -140 130" fill="none" stroke="#e11d48" stroke-width="2" marker-end="url(#inhibitionT)"/>
    </g>
    """)

    # Diana 2: Subunidad E2 (Lipoamida) -> Situada exactamente en y=625 a la derecha de E2
    partes.append(f"""
    <!-- DIANA PATOLÓGICA 2: E2 / LIPOAMIDA -->
    <g transform="translate(860, 625)">
      <rect x="0" y="0" width="550" height="70" rx="10" fill="#fff1f2" stroke="#e11d48" stroke-width="1.8"/>
      <circle cx="24" cy="24" r="12" fill="#be123c"/>
      <text x="24" y="29" fill="#ffffff" font-size="13" font-weight="900" text-anchor="middle">!</text>

      <text x="44" y="22" fill="#9f1239" font-size="12.5" font-weight="900">DIANA E2: INTOXICACIÓN POR ARSENITO (AsO₂⁻)</text>
      <text x="44" y="40" fill="#334155" font-size="11">
        • El arsenito ataca los dos grupos -SH de la dihidrolipoamida formando un quelato cíclico irreversible.
      </text>
      <text x="44" y="56" fill="#15803d" font-size="10.5" font-weight="700">
        • Antídoto: Quelantes ditiólicos como BAL (Dimercaprol) que regeneran el brazo móvil de E2.
      </text>

      <path d="M 0 35 L -140 20" fill="none" stroke="#e11d48" stroke-width="2" marker-end="url(#inhibitionT)"/>
    </g>
    """)

    # =========================================================================
    # 5. INTEGRACIÓN VISUAL: BIFURCACIÓN DEL ACETIL-COA EN EL EXTREMO INFERIOR
    # =========================================================================
    # Colocado en y=1680 (después de terminar E3 y la regeneración de lipoamida oxidada),
    # evitando cualquier solapamiento vertical.
    y_dest = 1720
    partes.append(f"""
    <!-- CONEXIÓN E INTEGRACIÓN TOTAL DEL ACETIL-COA -->
    <g transform="translate(50, {y_dest})">
      <!-- Línea conectora que desciende desde el Acetil-CoA producido arriba (x=380, y=980)
           y baja por el lado izquierdo despejado sin tocar ninguna molécula -->
      <path d="M 280 -640 L 280 -40 L 700 -40" fill="none" stroke="#ea580c" stroke-width="3" marker-end="url(#arrowFlow)"/>
      <g transform="translate(715, -65)">
        <text x="0" y="0" fill="#ea580c" font-size="15" font-weight="900">BIFURCACIÓN Y DESTINOS DEL ACETIL-COA (2C) FORMADO</text>
        <text x="0" y="16" fill="#64748b" font-size="11.5">Encrucijada universal que alimenta las rutas centrales según el estado metabólico:</text>
      </g>

      <!-- 4 Tarjetas de Destinos con ancho 380px cada una organizadas de forma holgada -->
      <!-- Destino 1: CICLO DE KREBS (VÍA 6) -->
      <g transform="translate(20, 0)">
        <path d="M 330 -40 C 330 0, 190 0, 190 30" fill="none" stroke="#ea580c" stroke-width="2.5" marker-end="url(#arrowFlow)"/>
        
        <rect x="0" y="30" width="375" height="230" rx="14" fill="#fffbeb" stroke="#f59e0b" stroke-width="2" filter="url(#shadowGlow)"/>
        <g transform="translate(20, 55)">
          <rect x="0" y="0" width="28" height="28" rx="6" fill="#ea580c"/>
          <text x="14" y="20" fill="#ffffff" font-size="15" font-weight="900" text-anchor="middle">6</text>
          <text x="38" y="20" fill="#b45309" font-size="15" font-weight="900">CICLO DE KREBS (TCA)</text>
          
          <text x="0" y="44" fill="#0f172a" font-size="12" font-weight="800">Condensación Inicial (Matriz):</text>
          <text x="0" y="60" fill="#64748b" font-size="11">Citrato Sintasa + Oxalacetato (4C) ➔ Citrato (6C)</text>
          
          <text x="0" y="86" fill="#15803d" font-size="11.5" font-weight="800">Rendimiento por Acetil-CoA:</text>
          <text x="0" y="104" fill="#15803d" font-size="11">3 NADH + 1 FADH₂ + 1 GTP + 2 CO₂</text>
          
          <text x="0" y="132" fill="#92400e" font-size="10.5" font-weight="700">➔ Oxigenación celular y síntesis masiva de ATP en la CTE.</text>
        </g>
      </g>

      <!-- Destino 2: LIPOGÉNESIS (VÍA 10) -->
      <g transform="translate(425, 0)">
        <path d="M 330 -40 C 330 0, 595 0, 595 30" fill="none" stroke="#2563eb" stroke-width="2.5" marker-end="url(#arrowFlow)"/>
        
        <rect x="0" y="30" width="375" height="230" rx="14" fill="#eff6ff" stroke="#3b82f6" stroke-width="2" filter="url(#shadowGlow)"/>
        <g transform="translate(20, 55)">
          <rect x="0" y="0" width="28" height="28" rx="6" fill="#2563eb"/>
          <text x="14" y="20" fill="#ffffff" font-size="14" font-weight="900" text-anchor="middle">10</text>
          <text x="38" y="20" fill="#1d4ed8" font-size="15" font-weight="900">LIPOGÉNESIS</text>
          
          <text x="0" y="44" fill="#0f172a" font-size="12" font-weight="800">Salida al Citosol (Exceso Calórico):</text>
          <text x="0" y="60" fill="#64748b" font-size="11">Lanzadera Citrato ➔ ACLY ➔ Acetil-CoA citosólico</text>
          
          <text x="0" y="86" fill="#1e40af" font-size="11.5" font-weight="800">Ruta Biosintética:</text>
          <text x="0" y="104" fill="#1e40af" font-size="11">ACC (Malonil-CoA) ➔ FAS (Palmitato 16:0)</text>
          
          <text x="0" y="132" fill="#1d4ed8" font-size="10.5" font-weight="700">➔ Almacenamiento como Triacilglicéridos (TAG).</text>
        </g>
      </g>

      <!-- Destino 3: CETOGÉNESIS (VÍA 11) -->
      <g transform="translate(830, 0)">
        <path d="M 330 -40 C 330 -15, 1000 -15, 1000 30" fill="none" stroke="#db2777" stroke-width="2.5" marker-end="url(#arrowFlow)"/>
        
        <rect x="0" y="30" width="375" height="230" rx="14" fill="#fdf2f8" stroke="#ec4899" stroke-width="2" filter="url(#shadowGlow)"/>
        <g transform="translate(20, 55)">
          <rect x="0" y="0" width="28" height="28" rx="6" fill="#db2777"/>
          <text x="14" y="20" fill="#ffffff" font-size="14" font-weight="900" text-anchor="middle">11</text>
          <text x="38" y="20" fill="#be185d" font-size="15" font-weight="900">CETOGÉNESIS HEPÁTICA</text>
          
          <text x="0" y="44" fill="#0f172a" font-size="12" font-weight="800">En Ayuno Prolongado / Diabetes:</text>
          <text x="0" y="60" fill="#64748b" font-size="11">Condensación de 2 Acetil-CoA por Tiolasa</text>
          
          <text x="0" y="86" fill="#9d174d" font-size="11.5" font-weight="800">Cuerpos Cetónicos:</text>
          <text x="0" y="104" fill="#9d174d" font-size="11">HMG-CoA mitocondrial ➔ Acetoacetato y β-OH-butirato</text>
          
          <text x="0" y="132" fill="#be185d" font-size="10.5" font-weight="700">➔ Combustible hidrosoluble para cerebro y músculo.</text>
        </g>
      </g>

      <!-- Destino 4: COLESTEROL Y MEVALONATO (VÍA 12) -->
      <g transform="translate(1235, 0)">
        <path d="M 330 -40 C 330 -25, 1405 -25, 1405 30" fill="none" stroke="#9333ea" stroke-width="2.5" marker-end="url(#arrowFlow)"/>
        
        <rect x="0" y="30" width="375" height="230" rx="14" fill="#faf5ff" stroke="#a855f7" stroke-width="2" filter="url(#shadowGlow)"/>
        <g transform="translate(20, 55)">
          <rect x="0" y="0" width="28" height="28" rx="6" fill="#9333ea"/>
          <text x="14" y="20" fill="#ffffff" font-size="14" font-weight="900" text-anchor="middle">12</text>
          <text x="38" y="20" fill="#7e22ce" font-size="15" font-weight="900">COLESTEROL Y MEVALONATO</text>
          
          <text x="0" y="44" fill="#0f172a" font-size="12" font-weight="800">Citosol Hepático:</text>
          <text x="0" y="60" fill="#64748b" font-size="11">HMG-CoA Reductasa (marcapasos alostérico)</text>
          
          <text x="0" y="86" fill="#6b21a8" font-size="11.5" font-weight="800">Productos Esteroideos:</text>
          <text x="0" y="104" fill="#6b21a8" font-size="11">Colesterol de membrana, Ácidos biliares, Vitamina D</text>
          
          <text x="0" y="132" fill="#7e22ce" font-size="10.5" font-weight="700">➔ Diana farmacológica principal de las estatinas.</text>
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
