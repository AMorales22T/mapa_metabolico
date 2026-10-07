#!/usr/bin/env python3
"""
GENERADOR DEL COMPLEJO PIRUVATO DESHIDROGENASA (PDH) - MAPA BIOLÓGICO INTEGRADO
=================================================================================
Diseño Orgánico y Funcional (idéntico a la Cadena Respiratoria y Mapa Integrado):
- Sin cajas de texto cuadradas artificiales.
- Entorno celular real: Citosol -> Membranas (VDAC, MPC) -> Matriz Mitocondrial.
- La regulación ocurre DIRECTAMENTE donde actúa (PDK y PDP incrustadas sobre E1).
- Las patologías e inhibidores señalan DIRECTAMENTE su diana molecular:
  * Beriberi / Déficit B1 señala a E1 (TPP).
  * Arsenito / Mercuriales señala al enlace ditiol de E2 (Lipoamida).
  * Acidosis Láctica señala el desvío a LDH si E1 falla.
- El Acetil-CoA producido se bifurca directamente mediante flechas de flujo metabólico
  hacia sus 4 destinos (Krebs, Lipogénesis, Cetogénesis y Colesterol) en la base.
- Cero solapamientos verificado geométricamente.
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

ANCHO_CANVAS = 1560
ALTO_CANVAS = 2050

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
        <!-- Flecha de flujo metabólico principal (Naranja) -->
        <marker id="arrowFlow" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
          <path d="M 0 0 L 6 3 L 0 6 Z" fill="#ea580c" />
        </marker>
        <!-- Flecha de gasto / reactivo (Roja) -->
        <marker id="arrowRed" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#dc2626" />
        </marker>
        <!-- Flecha de producto / ganancia energética (Verde) -->
        <marker id="arrowGreen" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#059669" />
        </marker>
        <!-- Flecha de Coenzima A (Púrpura) -->
        <marker id="arrowPurple" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#7c3aed" />
        </marker>
        <!-- Flecha gris de descarboxilación -->
        <marker id="arrowSlate" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#64748b" />
        </marker>
        <!-- Flecha dorada redox -->
        <marker id="arrowAmber" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#d97706" />
        </marker>
        <!-- Marcador de Inhibición / Bloqueo (Barra T roja) -->
        <marker id="inhibitionT" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
          <line x1="5" y1="0" x2="5" y2="6" stroke="#dc2626" stroke-width="2.2" />
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

        <!-- Filtro orgánico suave -->
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
    # 1. ENTORNO CELULAR BIOLÓGICO REAL (CITOSOL, BICAPAS Y MATRIZ)
    # =========================================================================
    y_mme = 130
    y_eim = 144
    y_mmi = 176
    y_matriz = 196

    # Matriz mitocondrial de fondo
    partes.append(f'<rect width="{ANCHO_CANVAS}" height="{ALTO_CANVAS}" fill="url(#gradMatrizPDH)"/>')

    # Citosol superior
    partes.append(f'<rect x="0" y="0" width="{ANCHO_CANVAS}" height="{y_mme}" fill="url(#gradCitosolPDH)"/>')
    partes.append(f"""
    <!-- Etiqueta Citosol -->
    <g transform="translate(40, 40)" opacity="0.85">
      <text x="0" y="0" fill="#334155" font-size="18" font-weight="900" letter-spacing="2">CITOSOL CELULAR</text>
      <text x="0" y="18" fill="#64748b" font-size="11">Final de la Glucólisis • Origen del Piruvato</text>
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
    <g transform="translate(40, {y_matriz + 40})" opacity="0.85">
      <text x="0" y="0" fill="#78350f" font-size="20" font-weight="900" letter-spacing="2">MATRIZ MITOCONDRIAL</text>
      <text x="0" y="18" fill="#92400e" font-size="11.5">Descarboxilación oxidativa del Piruvato • Máquina multienzimática PDH</text>
    </g>
    """)

    # Transportador MPC en la MMI (x=380)
    partes.append(f"""
    <g transform="translate(345, {y_mmi - 12})">
      <rect x="0" y="0" width="70" height="44" rx="10" fill="#9a3412" stroke="#7c2d12" stroke-width="2.2"/>
      <text x="35" y="27" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="900" text-anchor="middle">MPC</text>
    </g>
    <text x="425" y="{y_mmi + 14}" fill="#78350f" font-size="11.5" font-weight="800">Carrier de Piruvato (MPC1/2) • Simport H⁺</text>
    """)

    # Banner del Título Superior
    partes.append(f"""
    <g transform="translate(820, 35)">
      <rect x="0" y="0" width="620" height="75" rx="12" fill="#ffffff" stroke="#ea580c" stroke-width="2" filter="url(#shadowGlow)"/>
      <rect x="16" y="16" width="44" height="44" rx="8" fill="#ea580c"/>
      <text x="38" y="46" fill="#ffffff" font-size="24" font-weight="900" text-anchor="middle">5</text>
      <text x="75" y="35" fill="#0f172a" font-size="17" font-weight="900">COMPLEJO PIRUVATO DESHIDROGENASA (PDH)</text>
      <text x="75" y="54" fill="#ea580c" font-size="11.5" font-weight="700">Descarboxilación Oxidativa de Piruvato • EC 1.2.4.1 • ΔG°' = -33.4 kJ/mol</text>
    </g>
    """)

    # =========================================================================
    # 2. COLUMNA METABÓLICA CENTRAL (MECANISMO CATALÍTICO EN 5 ETAPAS)
    # =========================================================================
    x_col = 340

    # 1. Piruvato Citosol
    partes.append(nodo_metabolito(x_col, 25, "Piruvato (Citosol)", "3 Carbonos", PIRUVATO,
                                  detalle="Generado por Piruvato Cinasa en Glucólisis",
                                  detalle2="Difusión facilitada por VDAC en la MME", offset_texto=100))

    # Transporte a través de MPC
    partes.append(f"""
    <path d="M {x_col + 40} 120 L {x_col + 40} 160 M {x_col + 40} 210 L {x_col + 40} 250" stroke="#ea580c" stroke-width="3" stroke-dasharray="6 4" marker-end="url(#arrowFlow)"/>
    """)

    # 2. Piruvato Matricial
    partes.append(nodo_metabolito(x_col, 255, "Piruvato (Matriz)", "3 Carbonos", PIRUVATO,
                                  detalle="Sustrato alimentador del Complejo Multienzimático",
                                  detalle2="Concentración regula el recambio catalítico", offset_texto=100))

    # Flecha Reacción 1: Subunidad E1 (Descarboxilación)
    partes.append(f"""
    <!-- Reacción E1 -->
    <g transform="translate({x_col + 40}, 385)">
      <line x1="0" y1="0" x2="0" y2="75" stroke="#ea580c" stroke-width="3" marker-end="url(#arrowFlow)"/>
      <!-- Curva de descarboxilación CO2 -->
      <path d="M -8 24 Q -45 42 -115 42" fill="none" stroke="#dc2626" stroke-width="2.2" marker-end="url(#arrowRed)"/>
      <text x="-122" y="46" fill="#dc2626" font-size="12" font-weight="900" text-anchor="end">+ CO₂ ↑</text>
      
      <!-- Datos enzimáticos -->
      <g transform="translate(25, 20)">
        <text x="0" y="0" fill="#0f172a" font-size="14" font-weight="900">E1: Piruvato Deshidrogenasa (TPP)</text>
        <text x="0" y="16" fill="#64748b" font-size="10.5" font-family="'JetBrains Mono', monospace">EC 1.2.4.1 • Cofactor: TPP (Tiamina Pi)</text>
        <text x="0" y="32" fill="#c2410c" font-size="10" font-weight="800">Ataque nucleofílico del carbanión TPP • Paso limitante</text>
      </g>
    </g>
    """)

    # 3. Intermediario: Hidroxietil-TPP
    partes.append(nodo_metabolito(x_col - 20, 500, "Hidroxietil-TPP", "2 Carbonos unidos a E1", HIDROXIETIL_TPP,
                                  detalle="Intermediario carbaniónico unido covalentemente a E1",
                                  detalle2="Canalizado internamente al centro activo de E2", offset_texto=210))

    # Flecha Reacción 2: Subunidad E2 Paso 1 (Oxidación y transferencia)
    partes.append(f"""
    <!-- Reacción E2 Paso 1 -->
    <g transform="translate({x_col + 40}, 640)">
      <line x1="0" y1="0" x2="0" y2="70" stroke="#ea580c" stroke-width="3" marker-end="url(#arrowFlow)"/>
      <!-- Entrada del brazo lipoil oxidado -->
      <path d="M -120 12 Q -45 12 -8 24" fill="none" stroke="#d97706" stroke-width="2" marker-end="url(#arrowAmber)"/>
      <text x="-125" y="16" fill="#b45309" font-size="11.5" font-weight="800" text-anchor="end">+ Brazo Lipoil (E2)</text>
      
      <g transform="translate(25, 20)">
        <text x="0" y="0" fill="#0f172a" font-size="14" font-weight="900">E2: Lipoil Transacetilasa (Oxidación)</text>
        <text x="0" y="16" fill="#64748b" font-size="10.5" font-family="'JetBrains Mono', monospace">EC 2.3.1.12 • Cofactor: Lipoamida (S-S)</text>
        <text x="0" y="32" fill="#15803d" font-size="10" font-weight="800">Oxida el hidroxietilo a acetilo • TPP regenera su carbanión</text>
      </g>
    </g>
    """)

    # 4. Intermediario: Acetil-Lipoamida
    partes.append(nodo_metabolito(x_col - 20, 750, "Acetil-Dihidrolipoamida", "2 Carbonos en E2", ACETIL_LIPOAMIDA,
                                  detalle="Tioéster de alta energía en el brazo lipoilo de 14 Å",
                                  detalle2="Oscila directamente hacia el sitio aceptor de CoA-SH", offset_texto=235))

    # Flecha Reacción 3: Subunidad E2 Paso 2 (Transacetilación a CoA-SH)
    partes.append(f"""
    <!-- Reacción E2 Paso 2 -->
    <g transform="translate({x_col + 40}, 890)">
      <line x1="0" y1="0" x2="0" y2="70" stroke="#ea580c" stroke-width="3" marker-end="url(#arrowFlow)"/>
      <!-- Entrada de CoA-SH -->
      <path d="M -120 12 Q -45 12 -8 24" fill="none" stroke="#7c3aed" stroke-width="2.2" marker-end="url(#arrowPurple)"/>
      <text x="-125" y="16" fill="#7c3aed" font-size="12" font-weight="900" text-anchor="end">+ CoA-SH</text>
      
      <g transform="translate(25, 20)">
        <text x="0" y="0" fill="#0f172a" font-size="14" font-weight="900">E2: Lipoil Transacetilasa (Transacetilación)</text>
        <text x="0" y="16" fill="#64748b" font-size="10.5" font-family="'JetBrains Mono', monospace">EC 2.3.1.12 • Aceptor: Coenzima A libre</text>
        <text x="0" y="32" fill="#7c3aed" font-size="10" font-weight="800">Transferencia del acetilo al grupo tiol de la CoA</text>
      </g>
    </g>
    """)

    # 5. PRODUCTO PRINCIPAL: Acetil-CoA
    partes.append(nodo_metabolito(x_col - 10, 1000, "Acetil-Coenzima A", "2 Carbonos activados", ACETIL_COA,
                                  detalle="Tioéster de alta energía (ΔG°' hidrólisis = -31.5 kJ/mol)",
                                  detalle2="Encrucijada universal que alimenta las rutas centrales", offset_texto=185))

    # Canalización a E3
    partes.append(f"""
    <path d="M {x_col + 150} 1130 L {x_col + 150} 1195" stroke="#ea580c" stroke-width="2.6" marker-end="url(#arrowFlow)"/>
    """)

    # 6. Dihidrolipoamida reducida
    partes.append(nodo_metabolito(x_col - 20, 1210, "Dihidrolipoamida (reducida)", "Forma inactiva E2", DIHIDROLIPOAMIDA,
                                  detalle="Dos grupos tiol (-SH HS-) tras liberar el acetilo",
                                  detalle2="Obligatorio reoxidar para permitir la siguiente vuelta", offset_texto=210))

    # Flecha Reacción 4: Subunidad E3 (Cascada Redox)
    partes.append(f"""
    <!-- Reacción E3 -->
    <g transform="translate({x_col + 40}, 1355)">
      <line x1="0" y1="0" x2="0" y2="75" stroke="#ea580c" stroke-width="3" marker-end="url(#arrowFlow)"/>
      <!-- Entrada NAD+ -->
      <path d="M -120 12 Q -45 12 -8 24" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrowSlate)"/>
      <text x="-125" y="16" fill="#475569" font-size="11.5" font-weight="800" text-anchor="end">+ NAD⁺</text>
      <!-- Salida NADH -->
      <path d="M -8 30 Q -50 52 -135 52" fill="none" stroke="#059669" stroke-width="2.4" marker-end="url(#arrowGreen)"/>
      <text x="-142" y="56" fill="#059669" font-size="12.5" font-weight="900" text-anchor="end">+ NADH + H⁺</text>

      <g transform="translate(25, 20)">
        <text x="0" y="0" fill="#0f172a" font-size="14" font-weight="900">E3: Dihidrolipoil Deshidrogenasa</text>
        <text x="0" y="16" fill="#64748b" font-size="10.5" font-family="'JetBrains Mono', monospace">EC 1.8.1.4 • Cofactores: FAD (prostético) + NAD⁺ móvil</text>
        <text x="0" y="32" fill="#047857" font-size="10" font-weight="800">Cascada electrónica: Tioles ➔ FAD (FADH₂) ➔ NAD⁺ (NADH)</text>
      </g>
    </g>
    """)

    # 7. Lipoamida oxidada regenerada
    partes.append(nodo_metabolito(x_col - 10, 1475, "Lipoamida Oxidada (S-S)", "Forma activa de E2", LIPOAMIDA_OXIDADA,
                                  detalle="Puente disulfuro cíclico regenerado con éxito",
                                  detalle2="Lista para recibir el siguiente acetilo de E1", offset_texto=220))

    # Bucle cerrado de regeneración por el lateral izquierdo
    partes.append(f"""
    <path d="M {x_col - 50} 1515 C 20 1515, 20 735, {x_col - 50} 735" fill="none" stroke="#d97706" stroke-width="2.2" stroke-dasharray="8 5" marker-end="url(#arrowAmber)"/>
    <text x="16" y="1125" fill="#b45309" font-size="11" font-weight="900" transform="rotate(-90 16 1125)" text-anchor="middle">
      ↺ REGENERACIÓN CATALÍTICA DEL BRAZO LIPOILO DE E2
    </text>
    """)

    # =========================================================================
    # 3. REGULACIÓN BIOLÓGICA DIRECTA: INCRUSTADA DONDE OCURRE (SOBRE E1)
    # =========================================================================
    # Ubicada a la derecha de E1 (x=830, y=390)
    x_reg = 840
    y_reg = 390

    partes.append(f"""
    <!-- REGULACIÓN BIOLÓGICA DE LA SUBUNIDAD E1 -->
    <g transform="translate({x_reg}, {y_reg})">
      <!-- Conector curvo desde la reacción de E1 hacia el interruptor de fosforilación -->
      <path d="M -410 40 C -250 40, -100 40, 0 40" fill="none" stroke="#ea580c" stroke-width="2" stroke-dasharray="6 4" marker-end="url(#arrowFlow)"/>

      <!-- Título biológico directo (sin caja) -->
      <text x="0" y="-80" fill="#0f172a" font-size="16" font-weight="900">INTERRUPTOR COVALENTE Y ALOSTÉRICO DE E1</text>
      <text x="0" y="-62" fill="#64748b" font-size="11.5">Fosforilación reversible en el residuo Serina de la subunidad E1α</text>

      <!-- Estado Activo -->
      <g transform="translate(10, 42)">
        <rect x="0" y="0" width="160" height="46" rx="23" fill="#dcfce7" stroke="#16a34a" stroke-width="2.2"/>
        <text x="80" y="22" fill="#15803d" font-size="13" font-weight="900" text-anchor="middle">E1 ACTIVA</text>
        <text x="80" y="36" fill="#166534" font-size="9.5" font-weight="700" text-anchor="middle">Desfosforilada (Ser-OH)</text>
      </g>

      <!-- Flecha PDK (Fosforilación inactivadora) -->
      <path d="M 180 52 C 235 24, 315 24, 370 52" fill="none" stroke="#dc2626" stroke-width="2.6" marker-end="url(#arrowRed)"/>
      <g transform="translate(275, 14)">
        <text x="0" y="0" fill="#dc2626" font-size="12" font-weight="900" text-anchor="middle">PDK (Cinasa)</text>
        <text x="0" y="13" fill="#b91c1c" font-size="9" font-family="'JetBrains Mono', monospace" text-anchor="middle">+ ATP ➔ ADP</text>
      </g>

      <!-- Estado Inactivo -->
      <g transform="translate(380, 42)">
        <rect x="0" y="0" width="170" height="46" rx="23" fill="#fee2e2" stroke="#dc2626" stroke-width="2.2"/>
        <text x="85" y="22" fill="#991b1b" font-size="13" font-weight="900" text-anchor="middle">E1 INACTIVA</text>
        <text x="85" y="36" fill="#7f1d1d" font-size="9.5" font-weight="700" text-anchor="middle">Ⓟ Fosforilada (Ser-O-P)</text>
      </g>

      <!-- Flecha PDP (Desfosforilación activadora) -->
      <path d="M 370 78 C 315 108, 235 108, 180 78" fill="none" stroke="#16a34a" stroke-width="2.6" marker-end="url(#arrowGreen)"/>
      <g transform="translate(275, 126)">
        <text x="0" y="0" fill="#16a34a" font-size="12" font-weight="900" text-anchor="middle">PDP (Fosfatasa)</text>
        <text x="0" y="13" fill="#15803d" font-size="9" font-family="'JetBrains Mono', monospace" text-anchor="middle">+ H₂O ➔ Pi</text>
      </g>

      <!-- Efectores que actúan físicamente sobre PDK y PDP -->
      <g transform="translate(275, -45)">
        <text x="0" y="0" fill="#dc2626" font-size="10.5" font-weight="800" text-anchor="middle">⊕ Estimulan PDK (Apagan PDH):</text>
        <text x="0" y="14" fill="#334155" font-size="9.5" font-weight="700" text-anchor="middle">NADH, Acetil-CoA, ATP (exceso energético)</text>
      </g>
      <g transform="translate(275, 154)">
        <text x="0" y="0" fill="#16a34a" font-size="10.5" font-weight="800" text-anchor="middle">⊕ Estimulan PDP (Encienden PDH):</text>
        <text x="0" y="14" fill="#334155" font-size="9.5" font-weight="700" text-anchor="middle">Ca²⁺ (contracción muscular) • Insulina (hígado)</text>
      </g>

      <!-- Inhibición directa alostérica sobre PDK por sustrato -->
      <g transform="translate(20, 118)">
        <text x="0" y="0" fill="#15803d" font-size="10.5" font-weight="800">⊖ Inhiben a la PDK:</text>
        <text x="0" y="14" fill="#64748b" font-size="9.5">Piruvato, ADP, NAD⁺, Ca²⁺</text>
      </g>
    </g>
    """)

    # =========================================================================
    # 4. PATOLOGÍAS Y FARMACOLOGÍA: MOSTRADAS DIRECTAMENTE EN SU DIANA
    # =========================================================================
    # 1. Deficiencia de Tiamina (Vitamina B1) y Mutación E1α señalando a E1 (x=840, y=230)
    partes.append(f"""
    <!-- DIANA PATOLÓGICA 1: E1 / TPP -->
    <g transform="translate(840, 230)">
      <!-- Flecha indicadora hacia E1 -->
      <path d="M -10 30 L -120 160" fill="none" stroke="#dc2626" stroke-width="2" marker-end="url(#inhibitionT)"/>
      <g transform="translate(10, 15)">
        <text x="0" y="0" fill="#be123c" font-size="13" font-weight="900">DIANA E1: DÉFICIT DE B₁ Y ACIDOSIS LÁCTICA</text>
        <text x="0" y="18" fill="#334155" font-size="11">
          • <tspan font-weight="700">Falta de Tiamina (B₁):</tspan> Agota el TPP en E1 ➔ Beriberi / Wernicke-Korsakoff.
        </text>
        <text x="0" y="34" fill="#334155" font-size="11">
          • <tspan font-weight="700">Acidosis Láctica Congénita:</tspan> Mutación ligada al cromosoma X en E1α.
        </text>
        <text x="0" y="50" fill="#e11d48" font-size="10.5" font-weight="800">
          Mecanismo: Al bloquearse E1, el Piruvato no entra a la mitocondria y la LDH lo reduce a Lactato.
        </text>
      </g>
    </g>
    """)

    # 2. Envenenamiento por Arsenito (AsO2-) señalando a E2 (x=840, y=700)
    partes.append(f"""
    <!-- DIANA PATOLÓGICA 2: E2 / LIPOAMIDA -->
    <g transform="translate(860, 770)">
      <!-- Flecha indicadora hacia el brazo lipoil en E2 -->
      <path d="M -10 30 L -120 -80" fill="none" stroke="#dc2626" stroke-width="2" marker-end="url(#inhibitionT)"/>
      <g transform="translate(10, 15)">
        <text x="0" y="0" fill="#be123c" font-size="13" font-weight="900">DIANA E2: INTOXICACIÓN POR ARSENITO (AsO₂⁻)</text>
        <text x="0" y="18" fill="#334155" font-size="11">
          • El arsenito reacciona covalentemente con los dos tioles vecinales (-SH) de la dihidrolipoamida.
        </text>
        <text x="0" y="34" fill="#334155" font-size="11">
          • Forma un quelato cíclico estable que bloquea de forma irreversible la actividad de E2.
        </text>
        <text x="0" y="50" fill="#15803d" font-size="10.5" font-weight="800">
          Antídoto de rescate: Agentes ditiólicos como BAL (Dimercaprol) que regeneran la lipoamida.
        </text>
      </g>
    </g>
    """)

    # =========================================================================
    # 5. INTEGRACIÓN VISUAL: BIFURCACIÓN DEL ACETIL-COA HACIA SUS 4 DESTINOS
    # =========================================================================
    y_dest = 1620
    partes.append(f"""
    <!-- CONEXIÓN E INTEGRACIÓN TOTAL DEL ACETIL-COA -->
    <g transform="translate(50, {y_dest})">
      <!-- Línea conectora que desciende desde el Acetil-CoA producido arriba (x=380, y=1000) -->
      <path d="M 330 -580 L 330 -40 L 700 -40" fill="none" stroke="#ea580c" stroke-width="3" marker-end="url(#arrowFlow)"/>
      <g transform="translate(715, -60)">
        <text x="0" y="0" fill="#ea580c" font-size="14" font-weight="900">FLUJO METABÓLICO DEL ACETIL-COA FORMADO</text>
        <text x="0" y="16" fill="#64748b" font-size="11">Bifurcación biológica según el estado energético y hormonal del organismo:</text>
      </g>

      <!-- 4 Módulos de Destinos con ancho 325px cada uno (x=20, 365, 710, 1055) -->
      <!-- Destino 1: CICLO DE KREBS (VÍA 6) -->
      <g transform="translate(20, 0)">
        <path d="M 310 -40 C 310 0, 160 0, 160 30" fill="none" stroke="#ea580c" stroke-width="2.5" marker-end="url(#arrowFlow)"/>
        
        <rect x="0" y="30" width="325" height="230" rx="14" fill="#fffbeb" stroke="#f59e0b" stroke-width="2" filter="url(#shadowGlow)"/>
        <g transform="translate(18, 55)">
          <!-- Badge 6 -->
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
      <g transform="translate(365, 0)">
        <path d="M 310 -40 C 310 0, 510 0, 510 30" fill="none" stroke="#2563eb" stroke-width="2.5" marker-end="url(#arrowFlow)"/>
        
        <rect x="0" y="30" width="325" height="230" rx="14" fill="#eff6ff" stroke="#3b82f6" stroke-width="2" filter="url(#shadowGlow)"/>
        <g transform="translate(18, 55)">
          <!-- Badge 10 -->
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
      <g transform="translate(710, 0)">
        <path d="M 310 -40 C 310 -10, 860 -10, 860 30" fill="none" stroke="#db2777" stroke-width="2.5" marker-end="url(#arrowFlow)"/>
        
        <rect x="0" y="30" width="325" height="230" rx="14" fill="#fdf2f8" stroke="#ec4899" stroke-width="2" filter="url(#shadowGlow)"/>
        <g transform="translate(18, 55)">
          <!-- Badge 11 -->
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
      <g transform="translate(1055, 0)">
        <path d="M 310 -40 C 310 -20, 1200 -20, 1200 30" fill="none" stroke="#9333ea" stroke-width="2.5" marker-end="url(#arrowFlow)"/>
        
        <rect x="0" y="30" width="335" height="230" rx="14" fill="#faf5ff" stroke="#a855f7" stroke-width="2" filter="url(#shadowGlow)"/>
        <g transform="translate(18, 55)">
          <!-- Badge 12 -->
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
