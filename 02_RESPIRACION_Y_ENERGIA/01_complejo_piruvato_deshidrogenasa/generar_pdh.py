#!/usr/bin/env python3
"""
GENERADOR DEL COMPLEJO PIRUVATO DESHIDROGENASA (PDH) - MAPA INDIVIDUAL
========================================================================
Vía 5 del Mapa Metabólico Integrado.
Contenido editorial y científico:
1. Transporte mitocondrial: MPC (MPC1/MPC2) a través de la MMI desde el citosol.
2. Reacción global de descarboxilación oxidativa:
   Piruvato + CoA-SH + NAD⁺ ➔ Acetil-CoA + CO₂ + NADH + H⁺  (ΔG°' = -33.4 kJ/mol)
3. Ciclo catalítico en 5 etapas de las 3 subunidades:
   - E1 (Piruvato deshidrogenasa / carboxilasa, TPP): Descarboxilación a Hidroxietil-TPP.
   - E2 (Dihidrolipoil transacetilasa, Lipoamida): Transferencia del acetilo y formación de Acetil-CoA.
   - E3 (Dihidrolipoil deshidrogenasa, FAD, NAD⁺): Reoxidación del puente disulfuro de lipoamida y reducción de NAD⁺ a NADH.
4. Regulación bioquímica de alta fidelidad:
   - Modificación covalente: PDK (PDH cinasa, inactiva E1 por fosforilación) vs PDP (PDH fosfatasa, activa E1 por desfosforilación estimulada por Ca²⁺ e insulina).
   - Efectores alostéricos:
     * Activadores (⊕): Piruvato, ADP, NAD⁺, CoA-SH, Ca²⁺.
     * Inhibidores (⊖): Acetil-CoA, NADH, ATP.
5. Relevancia clínica y nutricional:
   - Beriberi / Síndrome de Wernicke-Korsakoff (deficiencia de Tiamina/B1).
   - Envenenamiento por Arsénico/Arsenito (bloqueo irreversible de los tioles vecinales de la lipoamida).
   - Acidosis láctica congénita por déficit de E1.
"""

import os
from estructuras_pdh import (
    PIRUVATO,
    HIDROXIETIL_TPP,
    ACETIL_LIPOAMIDA,
    DIHIDROLIPOAMIDA,
    LIPOAMIDA_OXIDADA,
    ACETIL_COA,
    COA_SH
)

ANCHO_CANVAS = 1400
ALTO_CANVAS = 1850

def generar_svg():
    return f"""<svg width="{ANCHO_CANVAS}" height="{ALTO_CANVAS}" viewBox="0 0 {ANCHO_CANVAS} {ALTO_CANVAS}" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <!-- Filtros de sombra editorial -->
    <filter id="shadowCard" x="-10%" y="-10%" width="125%" height="125%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#0f172a" flood-opacity="0.06"/>
    </filter>
    <filter id="shadowElevated" x="-10%" y="-10%" width="125%" height="125%">
      <feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="#0f172a" flood-opacity="0.08"/>
    </filter>

    <!-- Marcadores de flechas -->
    <marker id="arrowFlow" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto">
      <path d="M 0 0 L 7 3.5 L 0 7 Z" fill="#ea580c" />
    </marker>
    <marker id="arrowAmber" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
      <path d="M 0 0 L 6 3 L 0 6 Z" fill="#d97706" />
    </marker>
    <marker id="arrowGreen" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
      <path d="M 0 0 L 6 3 L 0 6 Z" fill="#059669" />
    </marker>
    <marker id="arrowBlue" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
      <path d="M 0 0 L 6 3 L 0 6 Z" fill="#2563eb" />
    </marker>
    <marker id="arrowRed" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
      <path d="M 0 0 L 6 3 L 0 6 Z" fill="#dc2626" />
    </marker>
    <marker id="arrowPurple" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
      <path d="M 0 0 L 6 3 L 0 6 Z" fill="#7c3aed" />
    </marker>

    <!-- Gradientes de fondos -->
    <linearGradient id="gradCitosolPDH" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#f8fafc" />
      <stop offset="100%" stop-color="#e2e8f0" />
    </linearGradient>

    <linearGradient id="gradMatrizPDH" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#fffbeb" />
      <stop offset="50%" stop-color="#fef3c7" stop-opacity="0.95" />
      <stop offset="100%" stop-color="#fef9c3" stop-opacity="0.9" />
    </linearGradient>

    <linearGradient id="gradCardE1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fff7ed" />
      <stop offset="100%" stop-color="#ffedd5" />
    </linearGradient>

    <linearGradient id="gradCardE2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fefce8" />
      <stop offset="100%" stop-color="#fef08a" stop-opacity="0.6" />
    </linearGradient>

    <linearGradient id="gradCardE3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f0fdf4" />
      <stop offset="100%" stop-color="#dcfce7" />
    </linearGradient>

    <linearGradient id="gradHeader" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#1e293b" />
      <stop offset="100%" stop-color="#334155" />
    </linearGradient>
  </defs>

  <!-- ================================================================= -->
  <!-- 1. FONDO ESTRUCTURAL: CITOSOL Y MATRIZ MITOCONDRIAL               -->
  <!-- ================================================================= -->
  <!-- Fondo global Matriz -->
  <rect width="{ANCHO_CANVAS}" height="{ALTO_CANVAS}" fill="url(#gradMatrizPDH)"/>

  <!-- Franja superior: Citosol -->
  <rect x="0" y="0" width="{ANCHO_CANVAS}" height="190" fill="url(#gradCitosolPDH)"/>

  <!-- Doble Membrana Mitocondrial y Espacio Intermembrana (EIM) -->
  <!-- MME -->
  <rect x="0" y="190" width="{ANCHO_CANVAS}" height="14" fill="#cbd5e1" stroke="#94a3b8" stroke-width="1.2"/>
  <text x="35" y="201" fill="#475569" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="800">MEMBRANA MITOCONDRIAL EXTERNA (MME)</text>

  <!-- EIM -->
  <rect x="0" y="204" width="{ANCHO_CANVAS}" height="28" fill="#fed7aa" opacity="0.6"/>
  <text x="35" y="222" fill="#c2410c" font-family="'Inter', sans-serif" font-size="10" font-weight="700">Espacio Intermembrana (EIM) • Acumulación de H⁺</text>

  <!-- MMI -->
  <rect x="0" y="232" width="{ANCHO_CANVAS}" height="18" fill="#d97706" stroke="#b45309" stroke-width="1.5"/>
  <text x="35" y="245" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="800">MEMBRANA MITOCONDRIAL INTERNA (MMI) - Impermeable</text>

  <!-- ================================================================= -->
  <!-- 2. BANNER SUPERIOR EDITORIAL INSTITUCIONAL                        -->
  <!-- ================================================================= -->
  <rect x="0" y="0" width="{ANCHO_CANVAS}" height="95" fill="url(#gradHeader)"/>
  
  <g transform="translate(40, 28)">
    <!-- Badge de Vía 5 -->
    <rect x="0" y="0" width="36" height="36" rx="8" fill="#ea580c"/>
    <text x="18" y="25" fill="#ffffff" font-size="19" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">5</text>
    
    <text x="50" y="22" fill="#ffffff" font-family="'Inter', sans-serif" font-size="22" font-weight="800">COMPLEJO PIRUVATO DESHIDROGENASA (PDH)</text>
    <text x="50" y="42" fill="#cbd5e1" font-family="'Inter', sans-serif" font-size="12" font-weight="600">
      Descarboxilación Oxidativa de Piruvato a Acetil-CoA • Puente entre Glucólisis y Ciclo de Krebs • EC 1.2.4.1
    </text>
  </g>

  <!-- Resumen de Balance Energético y Termodinámico -->
  <g transform="translate(1000, 18)">
    <rect x="0" y="0" width="360" height="60" rx="8" fill="#0f172a" fill-opacity="0.4" stroke="#475569" stroke-width="1.2"/>
    <text x="15" y="22" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700">Reacción Neta Global:</text>
    <text x="15" y="38" fill="#f8fafc" font-family="'Inter', sans-serif" font-size="11" font-weight="700">Piruvato + CoA-SH + NAD⁺ ➔ Acetil-CoA + CO₂ + NADH + H⁺</text>
    <text x="15" y="52" fill="#34d399" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="700">ΔG°' = -33.4 kJ/mol (Irreversible)</text>
  </g>

  <!-- ================================================================= -->
  <!-- 3. TRANSPORTE DE PIRUVATO A LA MATRIZ (MPC)                       -->
  <!-- ================================================================= -->
  <!-- Piruvato citosólico -->
  <g transform="translate(130, 105)">
    <text x="0" y="0" fill="#0f172a" font-family="'Inter', sans-serif" font-size="14" font-weight="800">Piruvato (Citosol)</text>
    <text x="0" y="14" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="10">Producto final de la Glucólisis</text>
  </g>
  <g transform="translate(180, 120)">
    {PIRUVATO}
  </g>

  <!-- Flecha a través de VDAC y MPC -->
  <path d="M 220 185 L 220 270" stroke="#ea580c" stroke-width="3" stroke-dasharray="6 4" marker-end="url(#arrowFlow)"/>
  
  <!-- Carrier MPC en la MMI -->
  <g transform="translate(175, 222)">
    <rect x="0" y="0" width="90" height="38" rx="8" fill="#9a3412" stroke="#7c2d12" stroke-width="2"/>
    <text x="45" y="22" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="800" text-anchor="middle">MPC1/2</text>
  </g>
  <text x="275" y="246" fill="#78350f" font-family="'Inter', sans-serif" font-size="11" font-weight="700">Carrier de Piruvato Mitocondrial (Simport H⁺ / Antiport OH⁻)</text>

  <!-- Piruvato en Matriz Mitocondrial -->
  <g transform="translate(140, 290)">
    <rect x="0" y="0" width="220" height="30" rx="6" fill="#fef3c7" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="110" y="20" fill="#92400e" font-family="'Inter', sans-serif" font-size="12" font-weight="800" text-anchor="middle">Piruvato en Matriz Mitocondrial</text>
  </g>

  <!-- ================================================================= -->
  <!-- 4. EL COMPLEJO MULTIENZIMÁTICO CENTRAL (ARQUITECTURA Y CICLO)      -->
  <!-- ================================================================= -->
  <!-- Contenedor central del complejo -->
  <rect x="50" y="340" width="870" height="1060" rx="16" fill="#ffffff" stroke="#f97316" stroke-width="2" filter="url(#shadowElevated)"/>
  
  <g transform="translate(75, 375)">
    <text x="0" y="0" fill="#c2410c" font-family="'Inter', sans-serif" font-size="20" font-weight="900">MÁQUINA MULTIENZIMÁTICA: 3 SUBUNIDADES Y 5 COFACTORES</text>
    <text x="0" y="20" fill="#64748b" font-family="'Inter', sans-serif" font-size="12">
      Canalización de sustratos: los intermediarios nunca abandonan el complejo, evitando reacciones secundarias.
    </text>
  </g>

  <!-- ==== SUBUNIDAD E1 ==== -->
  <g transform="translate(80, 420)">
    <rect x="0" y="0" width="810" height="230" rx="12" fill="url(#gradCardE1)" stroke="#ea580c" stroke-width="1.5"/>
    
    <!-- Título E1 -->
    <rect x="18" y="14" width="70" height="26" rx="6" fill="#ea580c"/>
    <text x="53" y="32" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="900" text-anchor="middle">E1</text>
    <text x="96" y="32" fill="#9a3412" font-family="'Inter', sans-serif" font-size="16" font-weight="800">Piruvato Deshidrogenasa / Carboxilasa</text>
    <text x="440" y="32" fill="#78350f" font-family="'JetBrains Mono', monospace" font-size="12">EC 1.2.4.1 • Cofactor: TPP (Tiamina Pirofosfato)</text>
    
    <!-- Paso 1: Descarboxilación -->
    <g transform="translate(25, 60)">
      <circle cx="10" cy="10" r="10" fill="#c2410c"/>
      <text x="10" y="14" fill="#ffffff" font-size="11" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">1</text>
      <text x="28" y="14" fill="#0f172a" font-family="'Inter', sans-serif" font-size="12" font-weight="800">Descarboxilación limitante de velocidad:</text>
      <text x="28" y="30" fill="#475569" font-family="'Inter', sans-serif" font-size="11">El carbanión de TPP ataca al C2 de Piruvato. Se libera CO₂.</text>
      
      <!-- Liberación de CO2 -->
      <g transform="translate(50, 45)">
        <path d="M 0 10 Q 15 -10 30 10" fill="none" stroke="#dc2626" stroke-width="2" marker-end="url(#arrowRed)"/>
        <text x="40" y="12" fill="#dc2626" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="900">CO₂ ↑</text>
      </g>
    </g>

    <!-- Molécula intermedia: Hidroxietil-TPP -->
    <g transform="translate(360, 65)">
      <text x="40" y="0" fill="#c2410c" font-family="'Inter', sans-serif" font-size="12" font-weight="800">Intermediario: Hidroxietil-TPP</text>
      {HIDROXIETIL_TPP}
    </g>

    <!-- Paso 2: Oxidación y transferencia a E2 -->
    <g transform="translate(25, 140)">
      <circle cx="10" cy="10" r="10" fill="#c2410c"/>
      <text x="10" y="14" fill="#ffffff" font-size="11" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">2</text>
      <text x="28" y="14" fill="#0f172a" font-family="'Inter', sans-serif" font-size="12" font-weight="800">Oxidación del grupo hidroxietilo a grupo acetilo:</text>
      <text x="28" y="30" fill="#475569" font-family="'Inter', sans-serif" font-size="11">El hidroxietilo se transfiere al puente disulfuro (S-S) de la lipoamida de E2.</text>
      <text x="28" y="46" fill="#059669" font-family="'Inter', sans-serif" font-size="11" font-weight="700">El TPP regenera su carbanión activo listo para el siguiente Piruvato.</text>
    </g>
  </g>

  <!-- Flecha de canalización E1 ➔ E2 -->
  <path d="M 485 650 L 485 680" stroke="#ea580c" stroke-width="3" marker-end="url(#arrowFlow)"/>

  <!-- ==== SUBUNIDAD E2 ==== -->
  <g transform="translate(80, 680)">
    <rect x="0" y="0" width="810" height="340" rx="12" fill="url(#gradCardE2)" stroke="#ca8a04" stroke-width="1.5"/>
    
    <!-- Título E2 -->
    <rect x="18" y="14" width="70" height="26" rx="6" fill="#ca8a04"/>
    <text x="53" y="32" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="900" text-anchor="middle">E2</text>
    <text x="96" y="32" fill="#854d0e" font-family="'Inter', sans-serif" font-size="16" font-weight="800">Dihidrolipoil Transacetilasa</text>
    <text x="350" y="32" fill="#713f12" font-family="'JetBrains Mono', monospace" font-size="12">EC 2.3.1.12 • Cofactores: Lipoamida (brazo móvil de 14 Å) + CoA-SH</text>

    <!-- Brazo oscilante explicación -->
    <g transform="translate(25, 55)">
      <circle cx="10" cy="10" r="10" fill="#a16207"/>
      <text x="10" y="14" fill="#ffffff" font-size="11" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">3</text>
      <text x="28" y="14" fill="#0f172a" font-family="'Inter', sans-serif" font-size="12" font-weight="800">Brazo oscilante de lipoil-lisina (14 Å de alcance):</text>
      <text x="28" y="30" fill="#475569" font-family="'Inter', sans-serif" font-size="11">Lleva el acetilo activado desde el sitio activo de E1 hacia el centro activo de E2.</text>
    </g>

    <!-- Molécula: Acetil-lipoamida -->
    <g transform="translate(40, 100)">
      <text x="10" y="0" fill="#854d0e" font-family="'Inter', sans-serif" font-size="12" font-weight="800">Acetil-Dihidrolipoamida (Tioéster de alta energía)</text>
      <g transform="translate(10, 10)">
        {ACETIL_LIPOAMIDA}
      </g>
    </g>

    <!-- Entrada de CoA-SH y Salida de Acetil-CoA -->
    <g transform="translate(480, 95)">
      <!-- Entrada CoA-SH -->
      <path d="M 0 20 L 50 40" stroke="#7c3aed" stroke-width="2.2" marker-end="url(#arrowPurple)"/>
      <g transform="translate(0, -5)">
        <text x="0" y="12" fill="#7c3aed" font-family="'Inter', sans-serif" font-size="12" font-weight="800">+ Coenzima A libre</text>
        {COA_SH}
      </g>

      <!-- Salida Acetil-CoA -->
      <path d="M 60 70 L 100 100" stroke="#ea580c" stroke-width="2.8" marker-end="url(#arrowFlow)"/>
      <g transform="translate(80, 110)">
        <rect x="-10" y="-12" width="220" height="85" rx="8" fill="#ffffff" stroke="#ea580c" stroke-width="2" filter="url(#shadowCard)"/>
        <text x="0" y="5" fill="#ea580c" font-family="'Inter', sans-serif" font-size="13" font-weight="900">PRODUCTO: Acetil-CoA (2C)</text>
        <g transform="translate(0, 12)">
          {ACETIL_COA}
        </g>
      </g>
    </g>

    <!-- Estado resultante de E2: Lipoamida reducida -->
    <g transform="translate(25, 230)">
      <circle cx="10" cy="10" r="10" fill="#a16207"/>
      <text x="10" y="14" fill="#ffffff" font-size="11" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">4</text>
      <text x="28" y="14" fill="#0f172a" font-family="'Inter', sans-serif" font-size="12" font-weight="800">Lipoamida completamente reducida (Ditiol -SH HS-):</text>
      <text x="28" y="30" fill="#475569" font-family="'Inter', sans-serif" font-size="11">Debe reoxidarse obligatoriamente para poder catalizar otra ronda metabólica.</text>
      <g transform="translate(28, 40)">
        {DIHIDROLIPOAMIDA}
      </g>
    </g>
  </g>

  <!-- Flecha de transferencia E2 ➔ E3 -->
  <path d="M 485 1020 L 485 1050" stroke="#059669" stroke-width="3" marker-end="url(#arrowGreen)"/>

  <!-- ==== SUBUNIDAD E3 ==== -->
  <g transform="translate(80, 1050)">
    <rect x="0" y="0" width="810" height="310" rx="12" fill="url(#gradCardE3)" stroke="#16a34a" stroke-width="1.5"/>
    
    <!-- Título E3 -->
    <rect x="18" y="14" width="70" height="26" rx="6" fill="#16a34a"/>
    <text x="53" y="32" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="900" text-anchor="middle">E3</text>
    <text x="96" y="32" fill="#14532d" font-family="'Inter', sans-serif" font-size="16" font-weight="800">Dihidrolipoil Deshidrogenasa</text>
    <text x="350" y="32" fill="#14532d" font-family="'JetBrains Mono', monospace" font-size="12">EC 1.8.1.4 • Cofactores: FAD (prostético) + NAD⁺ (móvil)</text>

    <!-- Paso 5: Reoxidación y cadena de electrones -->
    <g transform="translate(25, 55)">
      <circle cx="10" cy="10" r="10" fill="#15803d"/>
      <text x="10" y="14" fill="#ffffff" font-size="11" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">5</text>
      <text x="28" y="14" fill="#0f172a" font-family="'Inter', sans-serif" font-size="12" font-weight="800">Cascada Redox de Electrones (Regeneración de Lipoamida y Producción de NADH):</text>
      <text x="28" y="30" fill="#475569" font-family="'Inter', sans-serif" font-size="11">
        2 H⁺ y 2 e⁻ pasan de la Dihidrolipoamida ➔ FAD (formando FADH₂) ➔ NAD⁺ (formando NADH + H⁺).
      </text>
    </g>

    <!-- Cascada visual de cofactores -->
    <g transform="translate(50, 105)">
      <!-- Regeneración Lipoamida -->
      <g transform="translate(0, 0)">
        <text x="0" y="0" fill="#047857" font-family="'Inter', sans-serif" font-size="11" font-weight="800">1. Regenera puente disulfuro en E2:</text>
        <g transform="translate(0, 10)">
          {LIPOAMIDA_OXIDADA}
        </g>
      </g>

      <!-- FAD -> FADH2 intermedio -->
      <g transform="translate(350, 10)">
        <rect x="0" y="0" width="160" height="70" rx="8" fill="#ffffff" stroke="#ca8a04" stroke-width="1.5"/>
        <text x="80" y="24" fill="#a16207" font-family="'Inter', sans-serif" font-size="12" font-weight="800" text-anchor="middle">FAD unido a E3</text>
        <path d="M 30 40 Q 80 55 130 40" fill="none" stroke="#ca8a04" stroke-width="2" marker-end="url(#arrowAmber)"/>
        <text x="80" y="58" fill="#15803d" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="800" text-anchor="middle">FADH₂ (Intermediario)</text>
      </g>

      <!-- Producción final de NADH + H+ -->
      <g transform="translate(540, 0)">
        <path d="M 0 45 L 30 45" stroke="#16a34a" stroke-width="2.5" marker-end="url(#arrowGreen)"/>
        
        <rect x="40" y="0" width="180" height="85" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2" filter="url(#shadowCard)"/>
        <text x="130" y="22" fill="#15803d" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="800" text-anchor="middle">GANANCIA ENERGÉTICA</text>
        <text x="130" y="46" fill="#047857" font-family="'Inter', sans-serif" font-size="16" font-weight="900" text-anchor="middle">+ NADH + H⁺</text>
        <text x="130" y="68" fill="#64748b" font-family="'Inter', sans-serif" font-size="10" text-anchor="middle">➔ CTE Complejo I (≈ 2.5 ATP)</text>
      </g>
    </g>

    <!-- Nota de bucle cerrado -->
    <g transform="translate(35, 235)">
      <rect x="0" y="0" width="740" height="50" rx="6" fill="#f0fdf4" stroke="#86efac" stroke-width="1"/>
      <text x="15" y="22" fill="#166534" font-family="'Inter', sans-serif" font-size="11" font-weight="800">
        ↺ Bucle Catalítico Completo: E1, E2 y E3 retornan intactos a su conformación basal.
      </text>
      <text x="15" y="38" fill="#15803d" font-family="'Inter', sans-serif" font-size="11">
        Rendimiento por molécula de Glucosa (x2 Piruvatos): +2 Acetil-CoA, +2 NADH, +2 CO₂.
      </text>
    </g>
  </g>

  <!-- ================================================================= -->
  <!-- 5. PANEL DERECHO: REGULACIÓN ALOSTÉRICA Y COVALENTE (VITAL NOTA)    -->
  <!-- ================================================================= -->
  <g transform="translate(950, 340)">
    <rect x="0" y="0" width="410" height="660" rx="16" fill="#ffffff" stroke="#0284c7" stroke-width="2" filter="url(#shadowElevated)"/>
    
    <!-- Título Regulación -->
    <g transform="translate(25, 35)">
      <text x="0" y="0" fill="#0369a1" font-family="'Inter', sans-serif" font-size="18" font-weight="900">REGULACIÓN DE LA PDH</text>
      <text x="0" y="18" fill="#64748b" font-family="'Inter', sans-serif" font-size="11">Doble nivel de control: Covalente + Alostérico</text>
    </g>

    <!-- Subpanel: Modificación Covalente -->
    <g transform="translate(20, 75)">
      <rect x="0" y="0" width="370" height="255" rx="10" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.2"/>
      <text x="15" y="24" fill="#0f172a" font-family="'Inter', sans-serif" font-size="13" font-weight="800">1. Control por Modificación Covalente</text>
      
      <!-- Esquema PDK vs PDP -->
      <!-- PDH Activa (no fosforilada) -->
      <g transform="translate(30, 45)">
        <rect x="0" y="0" width="130" height="42" rx="8" fill="#dcfce7" stroke="#16a34a" stroke-width="1.8"/>
        <text x="65" y="20" fill="#15803d" font-family="'Inter', sans-serif" font-size="11" font-weight="800" text-anchor="middle">PDH ACTIVA</text>
        <text x="65" y="34" fill="#166534" font-family="'JetBrains Mono', monospace" font-size="9" text-anchor="middle">Desfosforilada</text>
      </g>

      <!-- Flecha hacia Inactiva (Kinasa) -->
      <path d="M 170 55 C 210 35, 230 35, 230 65" fill="none" stroke="#dc2626" stroke-width="2" marker-end="url(#arrowRed)"/>
      <text x="210" y="25" fill="#dc2626" font-family="'Inter', sans-serif" font-size="10" font-weight="800" text-anchor="middle">PDK (Cinasa)</text>
      <text x="210" y="37" fill="#b91c1c" font-family="'JetBrains Mono', monospace" font-size="8" text-anchor="middle">+ ATP ➔ ADP</text>

      <!-- PDH Inactiva (fosforilada) -->
      <g transform="translate(210, 85)">
        <rect x="0" y="0" width="130" height="42" rx="8" fill="#fee2e2" stroke="#dc2626" stroke-width="1.8"/>
        <text x="65" y="20" fill="#b91c1c" font-family="'Inter', sans-serif" font-size="11" font-weight="800" text-anchor="middle">PDH INACTIVA</text>
        <text x="65" y="34" fill="#991b1b" font-family="'JetBrains Mono', monospace" font-size="9" text-anchor="middle">Ⓟ Fosforilada (E1-Ser)</text>
      </g>

      <!-- Flecha hacia Activa (Fosfatasa) -->
      <path d="M 210 115 C 170 145, 150 145, 120 100" fill="none" stroke="#16a34a" stroke-width="2" marker-end="url(#arrowGreen)"/>
      <text x="150" y="160" fill="#16a34a" font-family="'Inter', sans-serif" font-size="10" font-weight="800" text-anchor="middle">PDP (Fosfatasa)</text>
      <text x="150" y="172" fill="#15803d" font-family="'JetBrains Mono', monospace" font-size="8" text-anchor="middle">+ H₂O ➔ Pi</text>

      <!-- Moduladores de PDK y PDP -->
      <g transform="translate(15, 190)">
        <text x="0" y="12" fill="#b91c1c" font-family="'Inter', sans-serif" font-size="10" font-weight="800">PDK estimulada por:</text>
        <text x="110" y="12" fill="#334155" font-family="'Inter', sans-serif" font-size="10">NADH, Acetil-CoA, ATP (exceso energético)</text>
        <text x="0" y="26" fill="#15803d" font-family="'Inter', sans-serif" font-size="10" font-weight="800">PDK inhibida por:</text>
        <text x="110" y="26" fill="#334155" font-family="'Inter', sans-serif" font-size="10">Piruvato, ADP, NAD⁺, Ca²⁺</text>
        <text x="0" y="42" fill="#0284c7" font-family="'Inter', sans-serif" font-size="10" font-weight="800">PDP estimulada por:</text>
        <text x="110" y="42" fill="#334155" font-family="'Inter', sans-serif" font-size="10">Ca²⁺ (ejercicio/contracción), Insulina (hígado)</text>
      </g>
    </g>

    <!-- Subpanel: Efectores Alostéricos Directos -->
    <g transform="translate(20, 345)">
      <rect x="0" y="0" width="370" height="295" rx="10" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.2"/>
      <text x="15" y="24" fill="#0f172a" font-family="'Inter', sans-serif" font-size="13" font-weight="800">2. Efectores Alostéricos Directos</text>
      
      <!-- Activadores -->
      <g transform="translate(15, 45)">
        <rect x="0" y="0" width="340" height="105" rx="8" fill="#f0fdf4" stroke="#86efac" stroke-width="1.2"/>
        <text x="12" y="22" fill="#166534" font-family="'Inter', sans-serif" font-size="12" font-weight="900">⊕ ACTIVADORES ALOSTÉRICOS</text>
        <text x="12" y="42" fill="#15803d" font-family="'Inter', sans-serif" font-size="11" font-weight="700">• Piruvato:</text>
        <text x="80" y="42" fill="#334155" font-family="'Inter', sans-serif" font-size="11">Sustrato abundante; fuerza el flujo hacia Krebs.</text>
        <text x="12" y="60" fill="#15803d" font-family="'Inter', sans-serif" font-size="11" font-weight="700">• ADP y NAD⁺:</text>
        <text x="100" y="60" fill="#334155" font-family="'Inter', sans-serif" font-size="11">Baja carga energética celular.</text>
        <text x="12" y="78" fill="#15803d" font-family="'Inter', sans-serif" font-size="11" font-weight="700">• CoA-SH libre:</text>
        <text x="95" y="78" fill="#334155" font-family="'Inter', sans-serif" font-size="11">Disponibilidad de aceptor tioéster.</text>
        <text x="12" y="96" fill="#15803d" font-family="'Inter', sans-serif" font-size="11" font-weight="700">• Ca²⁺:</text>
        <text x="50" y="96" fill="#334155" font-family="'Inter', sans-serif" font-size="11">Señal de trabajo muscular y demanda de ATP.</text>
      </g>

      <!-- Inhibidores -->
      <g transform="translate(15, 165)">
        <rect x="0" y="0" width="340" height="115" rx="8" fill="#fef2f2" stroke="#fca5a5" stroke-width="1.2"/>
        <text x="12" y="22" fill="#991b1b" font-family="'Inter', sans-serif" font-size="12" font-weight="900">⊖ INHIBIDORES POR PRODUCTO</text>
        <text x="12" y="42" fill="#b91c1c" font-family="'Inter', sans-serif" font-size="11" font-weight="700">• Acetil-CoA:</text>
        <text x="90" y="42" fill="#334155" font-family="'Inter', sans-serif" font-size="11">Inhibición competitiva sobre E2.</text>
        <text x="12" y="60" fill="#b91c1c" font-family="'Inter', sans-serif" font-size="11" font-weight="700">• NADH:</text>
        <text x="65" y="60" fill="#334155" font-family="'Inter', sans-serif" font-size="11">Inhibición por producto redox sobre E3.</text>
        <text x="12" y="78" fill="#b91c1c" font-family="'Inter', sans-serif" font-size="11" font-weight="700">• ATP:</text>
        <text x="55" y="78" fill="#334155" font-family="'Inter', sans-serif" font-size="11">Alta carga energética celular.</text>
        <text x="12" y="98" fill="#7f1d1d" font-family="'Inter', sans-serif" font-size="10" font-weight="600">
          * Desvía el piruvato hacia Gluconeogénesis (vía Piruvato Carboxilasa).
        </text>
      </g>
    </g>
  </g>

  <!-- ================================================================= -->
  <!-- 6. PANEL INFERIOR DERECHO: PATOLOGÍAS Y FARMACOLOGÍA               -->
  <!-- ================================================================= -->
  <g transform="translate(950, 1020)">
    <rect x="0" y="0" width="410" height="380" rx="16" fill="#ffffff" stroke="#e11d48" stroke-width="2" filter="url(#shadowElevated)"/>
    
    <!-- Título Correlación Clínica -->
    <g transform="translate(25, 30)">
      <text x="0" y="0" fill="#be123c" font-family="'Inter', sans-serif" font-size="16" font-weight="900">CORRELACIÓN CLÍNICA Y FARMACOLÓGICA</text>
      <text x="0" y="16" fill="#64748b" font-family="'Inter', sans-serif" font-size="11">Impacto de la inhibición patológica de la PDH</text>
    </g>

    <!-- 1. Beriberi / Déficit B1 -->
    <g transform="translate(20, 60)">
      <rect x="0" y="0" width="370" height="85" rx="8" fill="#fff1f2" stroke="#fecdd3" stroke-width="1"/>
      <text x="12" y="20" fill="#9f1239" font-family="'Inter', sans-serif" font-size="12" font-weight="800">1. Déficit de Tiamina (Vitamina B1) / Beriberi</text>
      <text x="12" y="38" fill="#334155" font-family="'Inter', sans-serif" font-size="11">
        • La falta de TPP paraliza E1 en cerebro y miocardio.
      </text>
      <text x="12" y="54" fill="#334155" font-family="'Inter', sans-serif" font-size="11">
        • Provoca el <tspan font-weight="700">Síndrome de Wernicke-Korsakoff</tspan> en pacientes alcohólicos.
      </text>
      <text x="12" y="70" fill="#e11d48" font-family="'Inter', sans-serif" font-size="10" font-weight="700">
        Acumulación masiva de piruvato y lactato sanguíneo.
      </text>
    </g>

    <!-- 2. Intoxicación por Arsénico -->
    <g transform="translate(20, 155)">
      <rect x="0" y="0" width="370" height="95" rx="8" fill="#fff1f2" stroke="#fecdd3" stroke-width="1"/>
      <text x="12" y="20" fill="#9f1239" font-family="'Inter', sans-serif" font-size="12" font-weight="800">2. Envenenamiento por Arsenito (AsO₂⁻)</text>
      <text x="12" y="38" fill="#334155" font-family="'Inter', sans-serif" font-size="11">
        • El arsenito se une covalentemente a los dos grupos -SH
      </text>
      <text x="12" y="54" fill="#334155" font-family="'Inter', sans-serif" font-size="11">
        vecinales de la dihidrolipoamida de E2 formando un quelato cíclico estable.
      </text>
      <text x="12" y="70" fill="#334155" font-family="'Inter', sans-serif" font-size="11">
        • Bloqueo irreversible que detiene tanto PDH como α-KGDH.
      </text>
      <text x="12" y="86" fill="#be123c" font-family="'Inter', sans-serif" font-size="10" font-weight="700">
        Tratamiento: Quelantes ditiólicos como BAL (Dimercaprol).
      </text>
    </g>

    <!-- 3. Acidosis Láctica Congénita -->
    <g transform="translate(20, 260)">
      <rect x="0" y="0" width="370" height="85" rx="8" fill="#fff1f2" stroke="#fecdd3" stroke-width="1"/>
      <text x="12" y="20" fill="#9f1239" font-family="'Inter', sans-serif" font-size="12" font-weight="800">3. Acidosis Láctica Congénita (Mutación E1)</text>
      <text x="12" y="38" fill="#334155" font-family="'Inter', sans-serif" font-size="11">
        • Mutaciones ligadas al cromosoma X en la subunidad E1α.
      </text>
      <text x="12" y="54" fill="#334155" font-family="'Inter', sans-serif" font-size="11">
        • El piruvato se deriva obligatoriamente a lactato por LDH.
      </text>
      <text x="12" y="70" fill="#e11d48" font-family="'Inter', sans-serif" font-size="10" font-weight="700">
        Manejo terapéutico: Dieta cetogénica (fuente de Acetil-CoA no glucídica).
      </text>
    </g>
  </g>

  <!-- ================================================================= -->
  <!-- 7. CONEXIÓN Y DESTINOS DEL ACETIL-COA FORMADO (INTEGRACIÓN)       -->
  <!-- ================================================================= -->
  <g transform="translate(50, 1420)">
    <rect x="0" y="0" width="1310" height="380" rx="16" fill="#ffffff" stroke="#475569" stroke-width="2" filter="url(#shadowElevated)"/>
    
    <g transform="translate(30, 35)">
      <text x="0" y="0" fill="#0f172a" font-family="'Inter', sans-serif" font-size="18" font-weight="900">INTEGRACIÓN METABÓLICA: DESTINOS DEL ACETIL-COA GENERADO</text>
      <text x="0" y="20" fill="#64748b" font-family="'Inter', sans-serif" font-size="12">
        El Acetil-CoA es la encrucijada central del metabolismo intermediario, conectando la PDH con las demás vías del mapa:
      </text>
    </g>

    <!-- Destino 1: Ciclo de Krebs (Vía 6) -->
    <g transform="translate(30, 80)">
      <rect x="0" y="0" width="290" height="260" rx="12" fill="#fffbeb" stroke="#f59e0b" stroke-width="1.5"/>
      <g transform="translate(15, 25)">
        <!-- Badge 6 -->
        <rect x="0" y="0" width="26" height="26" rx="6" fill="#ea580c"/>
        <text x="13" y="18" fill="#ffffff" font-size="14" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">6</text>
        <text x="36" y="18" fill="#b45309" font-family="'Inter', sans-serif" font-size="14" font-weight="800">CICLO DE KREBS (TCA)</text>
      </g>
      <g transform="translate(15, 65)">
        <text x="0" y="14" fill="#0f172a" font-family="'Inter', sans-serif" font-size="12" font-weight="700">Condensación con Oxalacetato:</text>
        <text x="0" y="32" fill="#475569" font-family="'Inter', sans-serif" font-size="11">Citrato Sintasa ➔ Citrato (6C).</text>
        <text x="0" y="55" fill="#0f172a" font-family="'Inter', sans-serif" font-size="12" font-weight="700">Rendimiento por Acetil-CoA:</text>
        <text x="0" y="73" fill="#15803d" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700">• 3 NADH + H⁺</text>
        <text x="0" y="90" fill="#15803d" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700">• 1 FADH₂</text>
        <text x="0" y="107" fill="#15803d" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700">• 1 GTP / ATP</text>
        <text x="0" y="124" fill="#dc2626" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700">• 2 CO₂</text>
        <text x="0" y="150" fill="#b45309" font-family="'Inter', sans-serif" font-size="11" font-weight="800">Oxidación completa final a CO₂.</text>
      </g>
    </g>

    <!-- Destino 2: Lipogénesis (Vía 10) -->
    <g transform="translate(345, 80)">
      <rect x="0" y="0" width="290" height="260" rx="12" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5"/>
      <g transform="translate(15, 25)">
        <!-- Badge 10 -->
        <rect x="0" y="0" width="30" height="26" rx="6" fill="#2563eb"/>
        <text x="15" y="18" fill="#ffffff" font-size="13" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">10</text>
        <text x="38" y="18" fill="#1d4ed8" font-family="'Inter', sans-serif" font-size="14" font-weight="800">SÍNTESIS LIPÍDICA</text>
      </g>
      <g transform="translate(15, 65)">
        <text x="0" y="14" fill="#0f172a" font-family="'Inter', sans-serif" font-size="12" font-weight="700">Lanzadera de Citrato al Citosol:</text>
        <text x="0" y="32" fill="#475569" font-family="'Inter', sans-serif" font-size="11">El exceso de energía satura Krebs.</text>
        <text x="0" y="55" fill="#0f172a" font-family="'Inter', sans-serif" font-size="12" font-weight="700">Ruta citoplasmática:</text>
        <text x="0" y="73" fill="#1e40af" font-family="'Inter', sans-serif" font-size="11">• ATP-Citrato Liasa (ACLY)</text>
        <text x="0" y="90" fill="#1e40af" font-family="'Inter', sans-serif" font-size="11">• Acetil-CoA Carboxilasa (ACC)</text>
        <text x="0" y="107" fill="#1e40af" font-family="'Inter', sans-serif" font-size="11">• Complejo FAS (Ácido Palmítico)</text>
        <text x="0" y="150" fill="#1d4ed8" font-family="'Inter', sans-serif" font-size="11" font-weight="800">Almacenamiento como Triacilglicéridos.</text>
      </g>
    </g>

    <!-- Destino 3: Cetogénesis (Vía 11) -->
    <g transform="translate(660, 80)">
      <rect x="0" y="0" width="290" height="260" rx="12" fill="#fdf2f8" stroke="#ec4899" stroke-width="1.5"/>
      <g transform="translate(15, 25)">
        <!-- Badge 11 -->
        <rect x="0" y="0" width="30" height="26" rx="6" fill="#db2777"/>
        <text x="15" y="18" fill="#ffffff" font-size="13" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">11</text>
        <text x="38" y="18" fill="#be185d" font-family="'Inter', sans-serif" font-size="14" font-weight="800">CETOGÉNESIS HEPÁTICA</text>
      </g>
      <g transform="translate(15, 65)">
        <text x="0" y="14" fill="#0f172a" font-family="'Inter', sans-serif" font-size="12" font-weight="700">En ayuno prolongado / Diabetes:</text>
        <text x="0" y="32" fill="#475569" font-family="'Inter', sans-serif" font-size="11">Condensación de 2 Acetil-CoA.</text>
        <text x="0" y="55" fill="#0f172a" font-family="'Inter', sans-serif" font-size="12" font-weight="700">Formación de Cuerpos Cetónicos:</text>
        <text x="0" y="73" fill="#9d174d" font-family="'Inter', sans-serif" font-size="11">• Acetoacetil-CoA (Tiolasa)</text>
        <text x="0" y="90" fill="#9d174d" font-family="'Inter', sans-serif" font-size="11">• HMG-CoA mitocondrial</text>
        <text x="0" y="107" fill="#9d174d" font-family="'Inter', sans-serif" font-size="11">• Acetoacetato y β-Hidroxibutirato</text>
        <text x="0" y="150" fill="#be185d" font-family="'Inter', sans-serif" font-size="11" font-weight="800">Combustible para cerebro y músculo.</text>
      </g>
    </g>

    <!-- Destino 4: Colesterol y Mevalonato (Vía 12) -->
    <g transform="translate(975, 80)">
      <rect x="0" y="0" width="300" height="260" rx="12" fill="#faf5ff" stroke="#a855f7" stroke-width="1.5"/>
      <g transform="translate(15, 25)">
        <!-- Badge 12 -->
        <rect x="0" y="0" width="30" height="26" rx="6" fill="#9333ea"/>
        <text x="15" y="18" fill="#ffffff" font-size="13" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">12</text>
        <text x="38" y="18" fill="#7e22ce" font-family="'Inter', sans-serif" font-size="14" font-weight="800">COLESTEROL Y MEVALONATO</text>
      </g>
      <g transform="translate(15, 65)">
        <text x="0" y="14" fill="#0f172a" font-family="'Inter', sans-serif" font-size="12" font-weight="700">Vía citosólica del Mevalonato:</text>
        <text x="0" y="32" fill="#475569" font-family="'Inter', sans-serif" font-size="11">HMG-CoA Reductasa (marcapasos).</text>
        <text x="0" y="55" fill="#0f172a" font-family="'Inter', sans-serif" font-size="12" font-weight="700">Productos esteroideos:</text>
        <text x="0" y="73" fill="#6b21a8" font-family="'Inter', sans-serif" font-size="11">• Colesterol de membrana</text>
        <text x="0" y="90" fill="#6b21a8" font-family="'Inter', sans-serif" font-size="11">• Sales y ácidos biliares</text>
        <text x="0" y="107" fill="#6b21a8" font-family="'Inter', sans-serif" font-size="11">• Hormonas esteroideas y Vitamina D</text>
        <text x="0" y="150" fill="#7e22ce" font-family="'Inter', sans-serif" font-size="11" font-weight="800">Diana de estatinas farmacológicas.</text>
      </g>
    </g>
  </g>
</svg>"""

def generar_html(svg_str):
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Vía 5: Complejo Piruvato Deshidrogenasa (PDH) - Mapa Individual</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&family=JetBrains+Mono:wght@600;700;800&display=swap" rel="stylesheet">
  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      background: #0f172a;
      color: #f8fafc;
      font-family: 'Inter', system-ui, sans-serif;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 24px;
    }}
    .header-panel {{
      width: 100%;
      max-width: {ANCHO_CANVAS}px;
      margin-bottom: 16px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: #1e293b;
      padding: 16px 24px;
      border-radius: 12px;
      border: 1px solid #334155;
    }}
    .header-title h1 {{
      font-size: 20px;
      font-weight: 800;
      color: #f8fafc;
    }}
    .header-title p {{
      font-size: 13px;
      color: #94a3b8;
      margin-top: 4px;
    }}
    .btn-group {{
      display: flex;
      gap: 12px;
    }}
    .btn {{
      background: #ea580c;
      color: #ffffff;
      padding: 8px 16px;
      border-radius: 8px;
      text-decoration: none;
      font-size: 13px;
      font-weight: 700;
      transition: background 0.2s;
    }}
    .btn:hover {{
      background: #c2410c;
    }}
    .btn-secondary {{
      background: #334155;
      color: #e2e8f0;
    }}
    .btn-secondary:hover {{
      background: #475569;
    }}
    .canvas-container {{
      background: #ffffff;
      border-radius: 16px;
      box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.4);
      overflow: hidden;
      max-width: 100%;
      border: 1px solid #334155;
    }}
  </style>
</head>
<body>
  <div class="header-panel">
    <div class="header-title">
      <h1>Complejo Piruvato Deshidrogenasa (PDH) • Vía 5</h1>
      <p>Visualización Individual de Alta Resolución • Diseñada para Integración Total</p>
    </div>
    <div class="btn-group">
      <a href="../../prueba_visual_integrada.html" class="btn btn-secondary">← Volver al Mapa Integrado</a>
      <a href="Piruvato_Deshidrogenasa.svg" download class="btn">Descargar SVG</a>
    </div>
  </div>

  <div class="canvas-container">
    {svg_str}
  </div>
</body>
</html>
"""

def main():
    carpeta_actual = os.path.dirname(os.path.abspath(__file__))
    svg_content = generar_svg()
    
    # 1. Guardar SVG
    svg_path = os.path.join(carpeta_actual, "Piruvato_Deshidrogenasa.svg")
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f" SVG generado con éxito en: {svg_path}")

    # 2. Guardar HTML visor
    html_content = generar_html(svg_content)
    html_path = os.path.join(carpeta_actual, "Piruvato_Deshidrogenasa.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f" HTML generado con éxito en: {html_path}")

if __name__ == "__main__":
    main()
