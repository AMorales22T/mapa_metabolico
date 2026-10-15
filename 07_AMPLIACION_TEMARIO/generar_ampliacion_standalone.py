#!/usr/bin/env python3
"""
GENERADOR DE LA AMPLIACIÓN STANDALONE (VÍAS 18 A 25) SIN EL MAPA METABÓLICO CENTRAL
=====================================================================================
Presenta de manera independiente las 8 rutas y modelos biológicos ampliados:
- Columna 1 (Órganos Periféricos):
    • Vía 18: Digestión y transporte de lípidos dietarios (micela, enterocito, linfa)
    • Vía 19: Tejido adiposo (cascada lipolítica ATGL/HSL/MGL con estructuras químicas)
    • Vía 20: Músculo esquelético y sarcómero en contracción (Cori y Cahill)
    • Vía 21: Cerebro y sistema nervioso (BHE, neurona mielinizada, GLUT1/3, cetonas)
    • Correlaciones clínicas y farmacológicas (Orlistat, Estatinas, Ezetimiba, Fibratos, PKU)
    • Balance energético comparativo (ATP/C de glucosa, palmitato, cetonas)
- Columna 2 (Metabolismo Lipídico, Nitrogenado y Flujos):
    • Vía 22: Lipoproteínas plasmáticas y transporte reverso (VLDL, LDL, LDLR, HDL, SR-B1)
    • Vía 23: Biosíntesis de TAG y fosfolípidos (Vía de Kennedy)
    • Vía 24: Biosíntesis de aminoácidos no esenciales (10 aminoácidos)
    • Vía 25: Conmutador de flujos energéticos intertisulares
- Eje Vascular Central:
    • Capilares continuos y conductos de intercambio intertisular (quilomicrones, albúmina, glicerol, lactato, alanina).
- Motor Interactivo Completo:
    • Clic en ruta resalta y atenúa las demás (<= 4px threshold).
    • Índice lateral plegable con las 8 vías.
    • Buscador instantáneo con pulso animado.
    • Fichas flotantes (tooltips) para metabolitos y enzimas.
    • Selector de estados (Normal, Posprandial, Ayuno, Ejercicio).
"""

import base64
import os
import re
import shutil
import subprocess
import sys

DIR_SCRIPT = os.path.dirname(os.path.abspath(__file__))
DIR_BASE = os.path.dirname(DIR_SCRIPT)
DIR_HTML = os.path.join(DIR_BASE, "versiones_html")
DIR_IMPRESION = os.path.join(DIR_BASE, "versiones_impresion")

sys.path.append(DIR_SCRIPT)
import estructuras_ampliacion as ea
import generar_ampliacion as ga

sys.path.append(os.path.join(DIR_BASE, "04_NITROGENO_Y_AMINOACIDOS", "via_13_transaminacion_y_desaminacion"))
import estructuras_aminoacidos as eaa

sys.path.append(os.path.join(DIR_BASE, "04_NITROGENO_Y_AMINOACIDOS", "via_12b_destinos_esqueletos_carbonados"))
import estructuras_destinos_aa as eda

RUTA_OUT_HTML = os.path.join(DIR_SCRIPT, "ampliacion_rutas_18_25_interactiva.html")
RUTA_OUT_SVG = os.path.join(DIR_SCRIPT, "ampliacion_rutas_18_25_interactiva.svg")
RUTA_OUT_PDF = os.path.join(DIR_SCRIPT, "ampliacion_rutas_18_25_interactiva.pdf")
RUTA_COPIA_HTML = os.path.join(DIR_HTML, "ampliacion_rutas_18_25_interactiva.html")


def construir_panel_clinico_y_balance():
    """Genera las fichas clínicas y de balance energético para completar la Columna 1 bajo Vía 21."""
    p = []
    p.append("""
    <g id="panel_correlaciones_clinicas" transform="translate(-690, 3440)">
      <rect x="0" y="0" width="620" height="740" rx="14" fill="#ffffff" stroke="#0284c7" stroke-width="2.2" opacity="0.98"/>
      
      <!-- Cabecera del panel -->
      <path d="M 0 14 C 0 6.2 6.2 0 14 0 L 606 0 C 613.8 0 620 6.2 620 14 L 620 42 L 0 42 Z" fill="#0284c7"/>
      <text x="310" y="27" font-family="'Inter', sans-serif" font-size="13" font-weight="900" fill="#ffffff" text-anchor="middle" letter-spacing="0.5">FARMACOLOGÍA Y CORRELACIONES CLÍNICAS (VÍAS 18–25)</text>

      <!-- Ficha 1: Digestión y Absorción Lipídica -->
      <g transform="translate(20, 56)">
        <rect x="0" y="0" width="580" height="96" rx="8" fill="#f0fdfa" stroke="#0d9488" stroke-width="1.6"/>
        <text x="16" y="22" font-family="'Inter', sans-serif" font-size="11.5" font-weight="900" fill="#0f766e">1. ORLISTAT (Inhibidor de Lipasa Pancreática — Vía 18)</text>
        <text x="16" y="42" font-family="'Inter', sans-serif" font-size="10" font-weight="700" fill="#0f172a">• Mecanismo: Se une covalentemente al residuo de serina activo de la Lipasa Pancreática y Gástrica.</text>
        <text x="16" y="60" font-family="'Inter', sans-serif" font-size="10" font-weight="700" fill="#0f172a">• Efecto clínico: Reduce la hidrólisis y absorción de TAG de la dieta en ~30%. Provoca esteatorrea transitoria.</text>
        <text x="16" y="80" font-family="'Inter', sans-serif" font-size="9.5" font-weight="800" fill="#0d9488">• Indicación: Coadyuvante en el manejo de la obesidad y síndrome metabólico con dieta hipocalórica.</text>
      </g>

      <!-- Ficha 2: Estatinas y Regulación de LDLR -->
      <g transform="translate(20, 164)">
        <rect x="0" y="0" width="580" height="110" rx="8" fill="#eff6ff" stroke="#2563eb" stroke-width="1.6"/>
        <text x="16" y="22" font-family="'Inter', sans-serif" font-size="11.5" font-weight="900" fill="#1d4ed8">2. ESTATINAS Y EZETIMIBA (Control de Lipoproteínas — Vía 22)</text>
        <text x="16" y="42" font-family="'Inter', sans-serif" font-size="10" font-weight="700" fill="#0f172a">• Estatinas (Atorvastatina, Rosuvastatina): Inhibidores competitivos de HMG-CoA Reductasa (EC 1.1.1.34).</text>
        <text x="16" y="60" font-family="'Inter', sans-serif" font-size="10" font-weight="700" fill="#0f172a">• Cascada reguladora: ↓ Colesterol hepático ➔ Activación de SREBP-2 ➔ ↑ Expresión masiva de receptores LDLR.</text>
        <text x="16" y="78" font-family="'Inter', sans-serif" font-size="10" font-weight="700" fill="#0f172a">• Ezetimiba: Bloquea selectivamente el transportador NPC1L1 en el borde en cepillo del enterocito.</text>
        <text x="16" y="98" font-family="'Inter', sans-serif" font-size="9.5" font-weight="800" fill="#1d4ed8">• Hipercolesterolemia Familiar: Mutación en gen LDLR (19p13) o ApoB-100 ➔ Aterosclerosis prematura grave.</text>
      </g>

      <!-- Ficha 3: Fibratos y PPAR-alfa -->
      <g transform="translate(20, 286)">
        <rect x="0" y="0" width="580" height="96" rx="8" fill="#fdf4ff" stroke="#a855f7" stroke-width="1.6"/>
        <text x="16" y="22" font-family="'Inter', sans-serif" font-size="11.5" font-weight="900" fill="#7e22ce">3. FIBRATOS (Agonistas de PPAR-α — Vías 19, 22 y β-oxidación)</text>
        <text x="16" y="42" font-family="'Inter', sans-serif" font-size="10" font-weight="700" fill="#0f172a">• Fármacos: Fenofibrato, Gemfibrozilo. Activan el receptor nuclear PPAR-α hepático y muscular.</text>
        <text x="16" y="60" font-family="'Inter', sans-serif" font-size="10" font-weight="700" fill="#0f172a">• Acciones genómicas: ↑ Expresión de Lipoproteína Lipasa (LPL), ↑ ApoA-I / ApoA-II (↑ HDL), ↓ ApoC-III.</text>
        <text x="16" y="80" font-family="'Inter', sans-serif" font-size="9.5" font-weight="800" fill="#7e22ce">• Resultado: Reducción drástica de TAG plasmáticos (30-50%) y aumento moderado de HDL protectora.</text>
      </g>

      <!-- Ficha 4: Patología Molecular de Aminoácidos -->
      <g transform="translate(20, 394)">
        <rect x="0" y="0" width="580" height="110" rx="8" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.6"/>
        <text x="16" y="22" font-family="'Inter', sans-serif" font-size="11.5" font-weight="900" fill="#15803d">4. ERRORES CONGÉNITOS DEL METABOLISMO (Vías 20 y 24)</text>
        <text x="16" y="42" font-family="'Inter', sans-serif" font-size="10" font-weight="700" fill="#0f172a">• Fenilcetonuria (PKU): Déficit de Fenilalanina Hidroxilasa (PAH) o cofactor BH₄. Tirosina se vuelve esencial.</text>
        <text x="16" y="60" font-family="'Inter', sans-serif" font-size="10" font-weight="700" fill="#0f172a">• Toxicidad PKU: Fenilpiruvato y fenil-lactato saturan transportadores LAT1 en la BHE ➔ Daño neuronal.</text>
        <text x="16" y="78" font-family="'Inter', sans-serif" font-size="10" font-weight="700" fill="#0f172a">• Déficit de Lipina-1 (PAP / Vía 23): Provoca rabdomiólisis recurrente desencadenada por ayuno o fiebre.</text>
        <text x="16" y="98" font-family="'Inter', sans-serif" font-size="9.5" font-weight="800" fill="#15803d">• Enfermedad de Jarabe de Arce (MSUD): Bloqueo del complejo BCKDH ➔ Toxicidad de Leu, Ile, Val.</text>
      </g>

      <!-- Ficha 5: Cetoacidosis Diabética -->
      <g transform="translate(20, 516)">
        <rect x="0" y="0" width="580" height="96" rx="8" fill="#fff7ed" stroke="#ea580c" stroke-width="1.6"/>
        <text x="16" y="22" font-family="'Inter', sans-serif" font-size="11.5" font-weight="900" fill="#c2410c">5. CETOACIDOSIS DIABÉTICA (CAD — Desequilibrio Vías 19, 21 y 25)</text>
        <text x="16" y="42" font-family="'Inter', sans-serif" font-size="10" font-weight="700" fill="#0f172a">• Déficit absoluto de insulina ➔ Desinhibición masiva de ATGL y HSL en tejido adiposo (lipólisis desbocada).</text>
        <text x="16" y="60" font-family="'Inter', sans-serif" font-size="10" font-weight="700" fill="#0f172a">• Inundación hepática de AG libres ➔ Cetogénesis extrema ➔ Acetoacetato y β-Hidroxibutirato en plasma.</text>
        <text x="16" y="80" font-family="'Inter', sans-serif" font-size="9.5" font-weight="800" fill="#c2410c">• Consecuencia: Acidosis metabólica con anion gap elevado, respiración de Kussmaul y aliento a acetona.</text>
      </g>

      <!-- Ficha 6: Encefalopatía Hepática -->
      <g transform="translate(20, 624)">
        <rect x="0" y="0" width="580" height="96" rx="8" fill="#fef2f2" stroke="#dc2626" stroke-width="1.6"/>
        <text x="16" y="22" font-family="'Inter', sans-serif" font-size="11.5" font-weight="900" fill="#b91c1c">6. AMONIO Y TOXICIDAD NEURONAL (Vías 20, 21 y Ciclo de la Urea)</text>
        <text x="16" y="42" font-family="'Inter', sans-serif" font-size="10" font-weight="700" fill="#0f172a">• Fallo hepático grave ➔ Amonio (NH₄⁺) atraviesa libremente la BHE hacia los astrocitos cerebrales.</text>
        <text x="16" y="60" font-family="'Inter', sans-serif" font-size="10" font-weight="700" fill="#0f172a">• Astrocitos: Glutamina Sintetasa capta NH₄⁺ ➔ Acumulación osmótica de Glutamina ➔ Edema cerebral.</text>
        <text x="16" y="80" font-family="'Inter', sans-serif" font-size="9.5" font-weight="800" fill="#b91c1c">• Músculo esquelético: Actúa como salvamento temporal incorporando NH₄⁺ a Alanina (Cahill) y Glutamina.</text>
      </g>
    </g>
    """)

    # Panel de Balance Energético Comparativo
    p.append("""
    <g id="panel_balance_energetico_comparativo" transform="translate(-690, 4200)">
      <rect x="0" y="0" width="620" height="670" rx="14" fill="#ffffff" stroke="#16a34a" stroke-width="2.2" opacity="0.98"/>
      <path d="M 0 14 C 0 6.2 6.2 0 14 0 L 606 0 C 613.8 0 620 6.2 620 14 L 620 42 L 0 42 Z" fill="#16a34a"/>
      <text x="310" y="27" font-family="'Inter', sans-serif" font-size="13" font-weight="900" fill="#ffffff" text-anchor="middle" letter-spacing="0.5">BALANCE ENERGÉTICO COMPARATIVO Y RENDIMIENTO EN ATP</text>

      <!-- Tabla Comparativa -->
      <g transform="translate(20, 56)">
        <rect x="0" y="0" width="580" height="42" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.2"/>
        <text x="15" y="26" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#0f172a">COMBUSTIBLE</text>
        <text x="210" y="26" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#0f172a" text-anchor="middle">CARBONOS</text>
        <text x="350" y="26" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#0f172a" text-anchor="middle">ATP NETO / MOL</text>
        <text x="490" y="26" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#0f172a" text-anchor="middle">ATP / CARBONO</text>
      </g>

      <!-- Fila 1: Glucosa aerobia -->
      <g transform="translate(20, 108)">
        <rect x="0" y="0" width="580" height="40" rx="6" fill="#eff6ff" stroke="#bfdbfe" stroke-width="1"/>
        <text x="15" y="25" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#1d4ed8">Glucosa (Oxidación completa)</text>
        <text x="210" y="25" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#334155" text-anchor="middle">6 C</text>
        <text x="350" y="25" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#1d4ed8" text-anchor="middle">30 – 32 ATP</text>
        <text x="490" y="25" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#059669" text-anchor="middle">5.0 – 5.3 ATP/C</text>
      </g>

      <!-- Fila 2: Glucosa anaerobia (Cori) -->
      <g transform="translate(20, 156)">
        <rect x="0" y="0" width="580" height="40" rx="6" fill="#fff1f2" stroke="#fecdd3" stroke-width="1"/>
        <text x="15" y="25" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#be123c">Glucosa anaerobia (➔ Lactato)</text>
        <text x="210" y="25" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#334155" text-anchor="middle">6 C</text>
        <text x="350" y="25" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#be123c" text-anchor="middle">2 ATP (Rápido)</text>
        <text x="490" y="25" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#e11d48" text-anchor="middle">0.33 ATP/C</text>
      </g>

      <!-- Fila 3: Ácido Palmitato -->
      <g transform="translate(20, 204)">
        <rect x="0" y="0" width="580" height="40" rx="6" fill="#fffbeb" stroke="#fde68a" stroke-width="1"/>
        <text x="15" y="25" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#b45309">Ácido Palmitato (16:0)</text>
        <text x="210" y="25" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#334155" text-anchor="middle">16 C</text>
        <text x="350" y="25" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#b45309" text-anchor="middle">106 ATP</text>
        <text x="490" y="25" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#059669" text-anchor="middle">6.63 ATP/C ★</text>
      </g>

      <!-- Fila 4: Triacilglicerol completo -->
      <g transform="translate(20, 252)">
        <rect x="0" y="0" width="580" height="40" rx="6" fill="#fff7ed" stroke="#fed7aa" stroke-width="1"/>
        <text x="15" y="25" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#c2410c">Trioleína (TAG: 3x 18:1 + Glicerol)</text>
        <text x="210" y="25" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#334155" text-anchor="middle">57 C</text>
        <text x="350" y="25" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#c2410c" text-anchor="middle">~360 ATP</text>
        <text x="490" y="25" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#059669" text-anchor="middle">6.32 ATP/C</text>
      </g>

      <!-- Fila 5: Cuerpos cetónicos -->
      <g transform="translate(20, 300)">
        <rect x="0" y="0" width="580" height="40" rx="6" fill="#f5f3ff" stroke="#ddd6fe" stroke-width="1"/>
        <text x="15" y="25" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#6d28d9">D-β-Hidroxibutirato</text>
        <text x="210" y="25" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#334155" text-anchor="middle">4 C</text>
        <text x="350" y="25" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#6d28d9" text-anchor="middle">21.5 ATP</text>
        <text x="490" y="25" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#059669" text-anchor="middle">5.38 ATP/C</text>
      </g>

      <!-- Fila 6: Acetoacetato -->
      <g transform="translate(20, 348)">
        <rect x="0" y="0" width="580" height="40" rx="6" fill="#f5f3ff" stroke="#ddd6fe" stroke-width="1"/>
        <text x="15" y="25" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#6d28d9">Acetoacetato</text>
        <text x="210" y="25" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#334155" text-anchor="middle">4 C</text>
        <text x="350" y="25" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#6d28d9" text-anchor="middle">19 ATP</text>
        <text x="490" y="25" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#059669" text-anchor="middle">4.75 ATP/C</text>
      </g>

      <!-- Conclusiones Bioquímicas de Integración -->
      <g transform="translate(20, 404)">
        <rect x="0" y="0" width="580" height="246" rx="8" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1.4"/>
        <text x="20" y="28" font-family="'Inter', sans-serif" font-size="11.5" font-weight="900" fill="#0f172a">CLAVES FISIOLÓGICAS DE INTEGRACIÓN ENERGÉTICA:</text>
        <text x="20" y="52" font-family="'Inter', sans-serif" font-size="10" font-weight="700" fill="#334155">1. Los Ácidos Grasos son el reservorio más eficiente (9 kcal/g vs 4 kcal/g de carbohidratos):</text>
        <text x="35" y="70" font-family="'Inter', sans-serif" font-size="9.5" font-weight="600" fill="#64748b">• Su estado químico es más reducido (–CH₂– vs –CHOH–) y se almacenan anhidros en la gota lipídica.</text>
        <text x="35" y="88" font-family="'Inter', sans-serif" font-size="9.5" font-weight="600" fill="#64748b">• El glucógeno retiene ~2 g de agua por cada gramo de polisacárido, aumentando la masa corporal.</text>
        <text x="20" y="114" font-family="'Inter', sans-serif" font-size="10" font-weight="700" fill="#334155">2. El Cerebro no oxida Ácidos Grasos debido a la BHE y a la lentitud de la β-oxidación axonal:</text>
        <text x="35" y="132" font-family="'Inter', sans-serif" font-size="9.5" font-weight="600" fill="#64748b">• Consume ~120 g/día de Glucosa. En ayuno adapta su maquinaria a β-Hidroxibutirato (MCT1/2).</text>
        <text x="20" y="158" font-family="'Inter', sans-serif" font-size="10" font-weight="700" fill="#334155">3. El Eritrocito carece de mitocondrias:</text>
        <text x="35" y="176" font-family="'Inter', sans-serif" font-size="9.5" font-weight="600" fill="#64748b">• Su único destino catabólico es Glucólisis anaerobia a Lactato (Ciclo de Cori) y Vía de Pentosas (NADPH).</text>
        <text x="20" y="202" font-family="'Inter', sans-serif" font-size="10" font-weight="700" fill="#334155">4. El Hígado es generoso con el organismo y austero consigo mismo:</text>
        <text x="35" y="220" font-family="'Inter', sans-serif" font-size="9.5" font-weight="600" fill="#64748b">• Produce Cuerpos Cetónicos para el cerebro y músculo, pero carece de Tioforasa (no puede consumirlos).</text>
      </g>
    </g>
    """)
    return "\n".join(p)


def construir_eje_vascular_intertisular():
    """Genera el canal vascular y conectores de flujo intertisular entre la Columna 1 y 2."""
    return """
    <!-- EJE VASCULAR CENTRAL Y CANAL DE TRANSPORTE INTERTISULAR (X = 720 .. 860) -->
    <g id="eje_vascular_central">
      <!-- Columna vascular vertical de fondo -->
      <rect x="730" y="440" width="120" height="4480" rx="10" fill="#fff1f2" stroke="#fda4af" stroke-width="1.8"/>
      
      <!-- Torrente de sangre central -->
      <rect x="760" y="450" width="60" height="4460" rx="8" fill="url(#gradEjeVascular)" opacity="0.92"/>
      
      <!-- Rótulo vertical -->
      <g transform="translate(795, 520) rotate(90)">
        <text x="0" y="0" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#ffffff" letter-spacing="3" text-anchor="start">TORRENTE SANGUÍNEO Y TRANSPORTE INTERTISULAR</text>
      </g>
      <g transform="translate(795, 2600) rotate(90)">
        <text x="0" y="0" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#ffffff" letter-spacing="3" text-anchor="start">INTERCAMBIO DE COMBUSTIBLES Y METABOLITOS</text>
      </g>

      <!-- Eritrocitos viajando por el torrente central -->
      <g opacity="0.85">
        <g transform="translate(790, 800) rotate(15)">
          <ellipse cx="0" cy="0" rx="18" ry="11" fill="url(#gradEritrocito)" stroke="#7f1d1d" stroke-width="1.4" />
          <ellipse cx="0" cy="0" rx="9" ry="5.5" fill="url(#gradEritrocitoCentro)" opacity="0.75" />
        </g>
        <g transform="translate(790, 1400) rotate(-20)">
          <ellipse cx="0" cy="0" rx="18" ry="11" fill="url(#gradEritrocito)" stroke="#7f1d1d" stroke-width="1.4" />
          <ellipse cx="0" cy="0" rx="9" ry="5.5" fill="url(#gradEritrocitoCentro)" opacity="0.75" />
        </g>
        <g transform="translate(790, 2100) rotate(25)">
          <ellipse cx="0" cy="0" rx="18" ry="11" fill="url(#gradEritrocito)" stroke="#7f1d1d" stroke-width="1.4" />
          <ellipse cx="0" cy="0" rx="9" ry="5.5" fill="url(#gradEritrocitoCentro)" opacity="0.75" />
        </g>
        <g transform="translate(790, 2900) rotate(-10)">
          <ellipse cx="0" cy="0" rx="18" ry="11" fill="url(#gradEritrocito)" stroke="#7f1d1d" stroke-width="1.4" />
          <ellipse cx="0" cy="0" rx="9" ry="5.5" fill="url(#gradEritrocitoCentro)" opacity="0.75" />
        </g>
        <g transform="translate(790, 3800) rotate(12)">
          <ellipse cx="0" cy="0" rx="18" ry="11" fill="url(#gradEritrocito)" stroke="#7f1d1d" stroke-width="1.4" />
          <ellipse cx="0" cy="0" rx="9" ry="5.5" fill="url(#gradEritrocitoCentro)" opacity="0.75" />
        </g>
        <g transform="translate(790, 4600) rotate(-18)">
          <ellipse cx="0" cy="0" rx="18" ry="11" fill="url(#gradEritrocito)" stroke="#7f1d1d" stroke-width="1.4" />
          <ellipse cx="0" cy="0" rx="9" ry="5.5" fill="url(#gradEritrocitoCentro)" opacity="0.75" />
        </g>
      </g>

      <!-- Flechas de interconexión funcional -->
      <!-- 1. Linfa / Quilomicrones (de Col 1 Vía 18 a Torrente) -->
      <path d="M 680 1170 L 760 1170" fill="none" stroke="#16a34a" stroke-width="3" stroke-dasharray="6 4" marker-end="url(#arrowGreen)"/>
      
      <!-- 2. AG libres + Albúmina (de Col 1 Vía 19 a Torrente) -->
      <path d="M 700 1726 L 760 1726" fill="none" stroke="#ea580c" stroke-width="3" stroke-dasharray="8 5" marker-end="url(#arrowOrange)"/>
      
      <!-- 3. Glicerol (de Col 1 Vía 19 a Torrente hacia Kennedy Vía 23) -->
      <path d="M 725 2120 C 760 2120, 780 1600, 890 1240" fill="none" stroke="#0284c7" stroke-width="2.8" stroke-dasharray="8 5" marker-end="url(#arrowBlue)"/>
      
      <!-- 4. Lactato / Alanina (de Col 1 Vía 20 a Torrente hacia Vía 24/25) -->
      <path d="M 680 2740 C 750 2740, 770 2900, 890 3100" fill="none" stroke="#e11d48" stroke-width="3" stroke-dasharray="8 5" marker-end="url(#arrowRose)"/>
      
      <!-- 5. VLDL / LDL (de Col 2 Vía 22 a Tejidos en Col 1) -->
      <path d="M 890 610 L 820 610" fill="none" stroke="#2563eb" stroke-width="3" marker-end="url(#arrowBlue)"/>
      
      <!-- 6. HDL Transporte reverso (a Hígado) -->
      <path d="M 820 970 L 890 970" fill="none" stroke="#059669" stroke-width="3" marker-end="url(#arrowGreen)"/>
    </g>
    """


def generar_ampliacion_standalone():
    print("1. Generando contenidos vectoriales de Vías 18 a 25...")
    banda_izq_orig = ga.construir_banda_izquierda()
    banda_der_orig = ga.construir_banda_derecha()
    panel_clinico = construir_panel_clinico_y_balance()
    eje_vascular = construir_eje_vascular_intertisular()

    # Dimensiones óptimas del póster de 2 columnas
    W_CANVAS = 1720
    H_CANVAS = 5020
    VB_X = 0
    VB_Y = 0

    # Desplazamientos geométricos precisos
    # Banda izquierda: X original [-710, -80] con transform="translate(740, 0)" aterriza en [30, 660]
    # Banda derecha: X original [5850, 6510] con transform="translate(-4980, 0)" aterriza en [870, 1530]
    
    css_fonts = ga.cargar_fuentes_base64()

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W_CANVAS}" height="{H_CANVAS}" viewBox="{VB_X} {VB_Y} {W_CANVAS} {H_CANVAS}">
    <style>
      {css_fonts}
      text {{ font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }}
    </style>
    <defs>
      <linearGradient id="gradEjeVascular" x1="0" y1="0" x2="1" y2="0">
        <stop offset="0%" stop-color="#450a0a" stop-opacity="0.95"/>
        <stop offset="50%" stop-color="#991b1b" stop-opacity="0.9"/>
        <stop offset="100%" stop-color="#450a0a" stop-opacity="0.95"/>
      </linearGradient>

      <linearGradient id="gradEritrocito" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0%" stop-color="#dc2626"/>
        <stop offset="100%" stop-color="#991b1b"/>
      </linearGradient>
      <linearGradient id="gradEritrocitoCentro" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0%" stop-color="#f87171"/>
        <stop offset="100%" stop-color="#ef4444"/>
      </linearGradient>

      <marker id="arrowOrange" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto">
        <path d="M0,0 L9,4.5 L0,9 Z" fill="#ea580c"/>
      </marker>
      <marker id="arrowTeal" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto">
        <path d="M0,0 L9,4.5 L0,9 Z" fill="#0d9488"/>
      </marker>
      <marker id="arrowBlue" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto">
        <path d="M0,0 L9,4.5 L0,9 Z" fill="#0284c7"/>
      </marker>
      <marker id="arrowGreen" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto">
        <path d="M0,0 L9,4.5 L0,9 Z" fill="#16a34a"/>
      </marker>
      <marker id="arrowRose" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto">
        <path d="M0,0 L9,4.5 L0,9 Z" fill="#e11d48"/>
      </marker>
    </defs>

    <!-- 1. Fondo general del póster -->
    <rect x="0" y="0" width="{W_CANVAS}" height="{H_CANVAS}" fill="#f8fafc" />

    <!-- 2. Cabecera institucional -->
    <g id="header_standalone">
      <rect x="25" y="20" width="1670" height="195" rx="14" fill="#0f172a" stroke="#0284c7" stroke-width="2.5"/>
      <rect x="35" y="30" width="1650" height="6" fill="#38bdf8" rx="3"/>
      
      <text x="860" y="85" fill="#f8fafc" font-size="34" font-weight="900" font-family="'Inter', sans-serif" letter-spacing="2" text-anchor="middle">METABOLISMO INTERMEDIARIO · VÍAS DE AMPLIACIÓN (18–25)</text>
      <text x="860" y="125" fill="#38bdf8" font-size="16" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Digestión Lipídica • Cascada Lipolítica Adiposa con Estructuras • Sarcómero Muscular • Combustibles del SNC • Lipoproteínas • Vía de Kennedy • Aminoácidos • Conmutador Nutricional</text>
      <text x="860" y="160" fill="#94a3b8" font-size="12.5" font-weight="700" font-family="'Inter', sans-serif" text-anchor="middle">Versión de Estudio Especializada sin el Mapa Central Integrado • Bioquímica Humana y Fisiología Celular • Resolución Vectorial Ultra-HD</text>
      
      <!-- Sub-cabeceras de columnas -->
      <g transform="translate(45, 230)">
        <rect x="0" y="0" width="670" height="42" rx="8" fill="#1e293b" stroke="#0d9488" stroke-width="1.8"/>
        <text x="335" y="26" font-family="'Inter', sans-serif" font-size="13" font-weight="900" fill="#2dd4bf" text-anchor="middle">COLUMNA 1: FISIOLOGÍA DE ÓRGANOS Y CASCADAS SECUENCIALES (18–21)</text>
      </g>
      <g transform="translate(1005, 230)">
        <rect x="0" y="0" width="670" height="42" rx="8" fill="#1e293b" stroke="#3b82f6" stroke-width="1.8"/>
        <text x="335" y="26" font-family="'Inter', sans-serif" font-size="13" font-weight="900" fill="#60a5fa" text-anchor="middle">COLUMNA 2: LIPOPROTEÍNAS, KENNEDY, AMINOÁCIDOS Y CONMUTADOR (22–25)</text>
      </g>
    </g>

    <!-- 3. Fondos suaves de las columnas de trabajo -->
    <rect x="35" y="285" width="690" height="4630" rx="14" fill="#ffffff" stroke="#e2e8f0" stroke-width="2"/>
    <rect x="995" y="285" width="690" height="4630" rx="14" fill="#ffffff" stroke="#e2e8f0" stroke-width="2"/>

    <!-- 4. Eje vascular central continuo con eritrocitos e interconexiones -->
    {eje_vascular}

    <!-- 5. Columna 1: Vías 18, 19, 20, 21 + Panel Clínico y Balance -->
    <g id="columna_1_organos" transform="translate(745, -170)">
      {banda_izq_orig}
      {panel_clinico}
    </g>

    <!-- 6. Columna 2: Vías 22, 23, 24, 25 -->
    <g id="columna_2_flujos" transform="translate(-4845, -170)">
      {banda_der_orig}
    </g>

    <!-- 7. Pie institucional del póster -->
    <g id="pie_standalone">
      <rect x="25" y="4935" width="1670" height="65" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
      <text x="55" y="4973" fill="#0f172a" font-size="13" font-weight="900" font-family="'Inter', sans-serif">METABOLISMO INTERMEDIARIO · VÍAS 18 A 25</text>
      <text x="345" y="4973" fill="#64748b" font-size="11.5" font-weight="700" font-family="'Inter', sans-serif">Herramienta Didáctica Independiente • Edición Complementaria</text>
      <text x="1660" y="4973" fill="#64748b" font-size="11.5" font-weight="700" font-family="'Inter', sans-serif" text-anchor="end">Bioquímica Universitaria • Medicina y Ciencias Biomédicas</text>
    </g>
  </svg>"""

    print(f"2. Escribiendo SVG en: {RUTA_OUT_SVG}")
    with open(RUTA_OUT_SVG, "w", encoding="utf-8") as f:
        f.write(svg_content)

    print("3. Empaquetando en Visor HTML Interactivo Especializado (Vías 18 a 25)...")
    # Generar visor interactivo especializado para Vías 18 a 25
    html_standalone = ga.construir_html_mapa_ampliado(
        svg_final=svg_content,
        w_canvas=W_CANVAS,
        h_canvas=H_CANVAS,
        vb_x=VB_X,
        vb_y=VB_Y
    )

    # Ajustar el título y subtítulo en el HTML para reflejar la versión independiente
    html_standalone = html_standalone.replace(
        "Mapa Metabólico Integrado — Herramienta Interactiva Ampliada (25 Vías)",
        "Metabolismo Intermediario — Ampliación Standalone (Vías 18 a 25)"
    )
    html_standalone = html_standalone.replace(
        "Mapa Metabólico Integrado — Versión Ampliada (1200 × 900 mm)",
        "Ampliación del Temario — Vías 18 a 25 (Sin Mapa Central Integrado)"
    )
    html_standalone = html_standalone.replace(
        "25 rutas integradas • Clic para centrar y resaltar",
        "8 vías ampliadas • Clic para centrar y resaltar"
    )

    ruta_copia_html_num = os.path.join(DIR_HTML, "02_ampliacion_rutas_18_25.html")
    print(f"4. Guardando HTML en:")
    print(f"   - {ruta_copia_html_num} (Entregable numerado standalone)")
    print(f"   - {RUTA_OUT_HTML}")
    print(f"   - {RUTA_COPIA_HTML}")
    with open(RUTA_OUT_HTML, "w", encoding="utf-8") as f:
        f.write(html_standalone)
    with open(RUTA_COPIA_HTML, "w", encoding="utf-8") as f:
        f.write(html_standalone)
    with open(ruta_copia_html_num, "w", encoding="utf-8") as f:
        f.write(html_standalone)

    # Generación de PDF con rsvg-convert si está disponible
    rsvg = shutil.which("rsvg-convert")
    if rsvg:
        print("5. Generando PDF vectorial de la ampliación standalone...")
        cmd_pdf = [
            rsvg, "-f", "pdf",
            "-o", RUTA_OUT_PDF,
            RUTA_OUT_SVG
        ]
        subprocess.run(cmd_pdf, check=True)
        print(f"   ✓ PDF generado: {RUTA_OUT_PDF}")
        ruta_copia_pdf_num = os.path.join(DIR_BASE, "versiones_impresion", "02_ampliacion_rutas_18_25.pdf")
        shutil.copy2(RUTA_OUT_PDF, ruta_copia_pdf_num)
        print(f"   ✓ Copia PDF guardada en: {ruta_copia_pdf_num}")

    print("\n=======================================================")
    print("¡AMPLIACIÓN STANDALONE (VÍAS 18 A 25) GENERADA CON ÉXITO!")
    print("=======================================================")


if __name__ == "__main__":
    generar_ampliacion_standalone()
