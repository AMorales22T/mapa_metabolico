#!/usr/bin/env python3
"""
GENERADOR VECTORIAL EDITORIAL: CICLO DE LA UREA EN ENTORNO BIOLÓGICO REAL
========================================================================
Diseñado en concordancia 100% estricta con el estilo editorial de:
- 01_CARBOHIDRATOS/01_glucolisis/generar_glucolisis.py
- 02_RESPIRACION_Y_ENERGIA/02_ciclo_de_krebs/generar_ciclo_krebs.py
- 04_NITROGENO_Y_AMINOACIDOS/01_transaminacion_y_desaminacion/generar_transaminacion_y_desaminacion.py

Topología con separación espacial milimétrica (cero colisiones visuales):
1. Carril Izquierdo (Biciclo de Krebs): Fumarato liberado por ASL se reconvierte en Malato y
   Oxalacetato para regenerar el L-Aspartato donador del ciclo.
2. Carril Central (Flujo Metabólico de la Urea):
   - Mitocondria: Síntesis de Carbamoil-P (CPS-1) y Citrulina (OTC).
   - Cruce MMI: Translocador Citrina (SLC25A13) hacia el citosol.
   - Citosol: Condensación con Aspartato (ASS) ➔ Argininosuccinato ➔ Escisión a Arginina (ASL)
     ➔ Hidrólisis por Arginasa (ARG1) ➔ Excreción de UREA hacia el torrente hepático.
3. Carril Derecho (Lanzadera de Ornitina en X=730):
   - Ornitina regenerada asciende limpia por el carril X=730 cruzando el transportador ORNT1
     (SLC25A15) hacia la matriz mitocondrial para cerrar el ciclo en la OTC.
4. 100% átomos de carbono como texto explícito (C, CH, CH₂, COO⁻). CERO puntos negros.
5. Paneles educativos alineados al margen derecho (X=835) sin tocar el flujo central.
"""

import os
import sys

DIR_ACTUAL = os.path.dirname(os.path.abspath(__file__))
sys.path.append(DIR_ACTUAL)

from estructuras_urea import (
    IONES_INICIALES,
    CARBAMOIL_FOSFATO,
    ORNITINA,
    CITRULINA,
    ASPARTATO,
    ARGININOSUCCINATO,
    FUMARATO,
    ARGININA,
    UREA
)
from entorno_urea import DEFS_ENTORNO_UREA, generar_entorno_urea_svg

ANCHO_CANVAS = 1000
ALTO_CANVAS = 2120

# =============================================================================
# 1. PLANTILLA BASE HTML
# =============================================================================
CABECERA_HTML = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ciclo de la Urea en Entorno Hepatocitario Real</title>
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
    svg text {{ stroke: none; }}
  </style>
</head>
<body>
  <div class="lienzo-svg">
    <svg width="{ANCHO_CANVAS}" height="{ALTO_CANVAS}" viewBox="0 0 {ANCHO_CANVAS} {ALTO_CANVAS}" xmlns="http://www.w3.org/2000/svg">
      <defs>
        {DEFS_ENTORNO_UREA}
      </defs>
"""

PIE_HTML = """
    </svg>
  </div>
</body>
</html>
"""

# =============================================================================
# 2. FUNCIONES GENERADORAS DE ELEMENTOS (ESTILO GLUCÓLISIS Y KREBS)
# =============================================================================

def crear_metabolito(x, y, nombre, carbonos, detalle="", detalle2="", svg_estructura="", offset_texto=135, texto_arriba=False):
    """Construye el bloque SVG de un metabolito libre con su estructura y textos jerárquicos."""
    txt2 = f'<text x="0" y="44" fill="#0d9488" font-size="10" font-weight="700" font-family="\'Inter\', sans-serif">{detalle2}</text>' if detalle2 else ""
    offset_y_est = 60 if detalle2 else 46
    
    if texto_arriba:
        return f"""
        <!-- Metabolito: {nombre} -->
        <g transform="translate({x}, {y})">
          <g transform="translate(0, 0)">
            <text x="0" y="0" fill="#0f172a" font-size="15.5" font-weight="800" font-family="'Inter', sans-serif">{nombre}</text>
            <text x="0" y="16" fill="#ea580c" font-size="11.5" font-weight="700" font-family="'JetBrains Mono', monospace">{carbonos}</text>
            <text x="0" y="30" fill="#64748b" font-size="10" font-family="'Inter', sans-serif">{detalle}</text>
            {txt2}
          </g>
          <g transform="translate(0, {offset_y_est})">
            {svg_estructura}
          </g>
        </g>
        """

    return f"""
      <!-- Metabolito: {nombre} -->
      <g transform="translate({x}, {y})">
        <g transform="translate(0, 0)">
          {svg_estructura}
        </g>
        <g transform="translate({offset_texto}, 25)">
          <text x="0" y="0" fill="#0f172a" font-size="15.5" font-weight="800" font-family="'Inter', sans-serif">{nombre}</text>
          <text x="0" y="18" fill="#ea580c" font-size="11.5" font-weight="700" font-family="'JetBrains Mono', monospace">{carbonos}</text>
          <text x="0" y="33" fill="#64748b" font-size="10.5" font-family="'Inter', sans-serif">{detalle}</text>
          {txt2}
        </g>
      </g>
    """

# =============================================================================
# 3. CONSTRUCCIÓN INTEGRADA DEL CICLO COMPLETO
# =============================================================================
def construir_ciclo_urea_svg():
    partes = []

    # 1. Fondo biológico hepatocitario (con MMI en Y=620)
    partes.append(generar_entorno_urea_svg(ancho=ANCHO_CANVAS, alto=ALTO_CANVAS, y_membrana=620))

    # =========================================================================
    # FASE 1: MATRIZ MITOCONDRIAL (Y = 80 a Y = 580)
    # =========================================================================
    
    # 0. Iones Iniciales: NH4+ + HCO3- (X=140, Y=75)
    partes.append(crear_metabolito(
        x=140, y=75,
        nombre="Sustratos Iniciales de Nitrógeno",
        carbonos="NH₄⁺ (Amonio libre) + HCO₃⁻ (Bicarbonato)",
        detalle="Amonio aportado por GLDH mitocondrial",
        svg_estructura=IONES_INICIALES,
        offset_texto=190
    ))

    # Reacción 1: CPS-1 (Carbamoil Fosfato Sintetasa I)
    partes.append("""
    <g transform="translate(250, 140)">
      <!-- Flecha vertical descendente -->
      <line x1="0" y1="0" x2="0" y2="65" stroke="#0d9488" stroke-width="2.6" marker-end="url(#arrowFlow)"/>

      <!-- Entrada de 2 ATP -->
      <path d="M -80 10 Q -30 10 -5 20" fill="none" stroke="#dc2626" stroke-width="1.8" marker-end="url(#arrowRed)"/>
      <text x="-85" y="13" fill="#dc2626" font-family="'Inter', sans-serif" font-size="11" font-weight="800" text-anchor="end">- 2 ATP</text>

      <!-- Salida de 2 ADP + Pi -->
      <path d="M -5 45 Q -30 55 -80 55" fill="none" stroke="#475569" stroke-width="1.8" marker-end="url(#arrowSlate)"/>
      <text x="-85" y="59" fill="#475569" font-family="'Inter', sans-serif" font-size="11" font-weight="800" text-anchor="end">+ 2 ADP + Pi</text>

      <!-- Metadatos de CPS-1 -->
      <g transform="translate(20, 18)">
        <text x="0" y="0" fill="#0f172a" font-family="'Inter', sans-serif" font-size="12.5" font-weight="900">Carbamoil Fosfato Sintetasa I (CPS-1)</text>
        <text x="0" y="14" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="10">EC 6.3.4.16 (Mitocondrial)</text>
        <text x="0" y="27" fill="#16a34a" font-family="'Inter', sans-serif" font-size="10" font-weight="800">⊕ N-Acetilglutamato (NAG) obligado</text>
      </g>
    </g>
    """)

    # 1. Carbamoil Fosfato (1C) (X=140, Y=220)
    partes.append(crear_metabolito(
        x=140, y=220,
        nombre="Carbamoil Fosfato",
        carbonos="1 Carbono [1C] (Anhidro fosfato)",
        detalle="Enlace fosfato de alta energía",
        detalle2="Aporta 1ᵉʳ nitrógeno de urea ➔",
        svg_estructura=CARBAMOIL_FOSFATO,
        offset_texto=150
    ))

    # 2. Ornitina en Matriz Mitocondrial (Ubicada en X=650, Y=85)
    partes.append(crear_metabolito(
        x=650, y=85,
        nombre="L-Ornitina (Matriz)",
        carbonos="5 Carbonos [5C]",
        detalle="Aceptor de carbamoilo",
        detalle2="Regenerada por ORNT1 ↻",
        svg_estructura=ORNITINA,
        texto_arriba=True
    ))

    # Reacción 2: Ornitina Transcarbamilasa (OTC)
    # Canaliza Carbamoil-P desde la izquierda (X=290, Y=250) y Ornitina desde arriba-derecha (X=650, Y=300)
    partes.append("""
    <g transform="translate(460, 315)">
      <!-- Flecha diagonal desde Carbamoil-P hacia OTC -->
      <path d="M -160 -30 Q -70 -10 -5 10" fill="none" stroke="#0d9488" stroke-width="2.6" marker-end="url(#arrowFlow)"/>

      <!-- Flecha diagonal descendente desde Ornitina (mito) hacia OTC -->
      <path d="M 205 -10 Q 105 -5 5 10" fill="none" stroke="#0d9488" stroke-width="2.6" marker-end="url(#arrowFlow)"/>

      <!-- Flecha vertical resultante hacia Citrulina -->
      <line x1="0" y1="12" x2="0" y2="75" stroke="#0d9488" stroke-width="2.8" marker-end="url(#arrowFlow)"/>

      <!-- Salida de Pi libre -->
      <path d="M -4 42 Q -35 52 -75 52" fill="none" stroke="#475569" stroke-width="1.8" marker-end="url(#arrowSlate)"/>
      <text x="-80" y="56" fill="#475569" font-family="'Inter', sans-serif" font-size="11" font-weight="800" text-anchor="end">+ Pi (Fosfato libre)</text>

      <!-- Metadatos de la OTC -->
      <g transform="translate(20, 32)">
        <text x="0" y="0" fill="#0f172a" font-family="'Inter', sans-serif" font-size="12.5" font-weight="900">Ornitina Transcarbamilasa (OTC)</text>
        <text x="0" y="14" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="10">EC 2.1.3.3 (Mitocondrial)</text>
        <text x="0" y="27" fill="#0f766e" font-family="'Inter', sans-serif" font-size="9.5" font-weight="700">Formación de enlace ureido</text>
      </g>
    </g>
    """)

    # 3. L-Citrulina en Matriz Mitocondrial (X=380, Y=405)
    partes.append(crear_metabolito(
        x=380, y=405,
        nombre="L-Citrulina (Matriz)",
        carbonos="6 Carbonos [6C] (Derivado ureido)",
        detalle="1ᵉʳ nitrógeno fijado",
        detalle2="Exportación a citosol ➔",
        svg_estructura=CITRULINA,
        offset_texto=135
    ))

    # =========================================================================
    # FASE 2: TRANSLOCACIÓN A TRAVÉS DE LA MEMBRANA MITOCONDRIAL (Y = 580 a 720)
    # =========================================================================

    # A. Salida de Citrulina a través de SLC25A13 (Citrina) en X=460
    partes.append("""
    <g id="translocacion_citrulina">
      <path d="M 460 600 L 460 720" stroke="#0d9488" stroke-width="3" marker-end="url(#arrowFlow)" fill="none"/>
      <text x="400" y="660" fill="#0f766e" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" text-anchor="end">Exportación de Citrulina ➔</text>
    </g>
    """)

    # B. Retorno ascendente de Ornitina a través de SLC25A15 (ORNT1) en X=820
    partes.append("""
    <g id="translocacion_ornitina">
      <!-- Retorno cerrado: Ornitina citosólica (755, 1680) ➔ carril X=820 ➔ cruza ORNT1 ➔ Ornitina matriz (755, 180) -->
      <path d="M 755 1680 L 820 1680 L 820 180 L 755 180" fill="none" stroke="#2563eb" stroke-width="2.6" stroke-dasharray="8 5" marker-end="url(#arrowCobalt)"/>
      <text x="832" y="1145" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="800" fill="#1d4ed8">↑ RETORNO ORNT1</text>
    </g>
    """)

    # =========================================================================
    # FASE 3: CITOSOL HEPATOCITARIO (Y = 730 a Y = 2100)
    # =========================================================================

    # 4. L-Citrulina en Citosol (X=380, Y=730)
    partes.append(crear_metabolito(
        x=380, y=730,
        nombre="L-Citrulina (Citosol)",
        carbonos="6 Carbonos [6C]",
        detalle="Recibida por SLC25A13",
        detalle2="Sustrato para condensación",
        svg_estructura=CITRULINA,
        offset_texto=135
    ))

    # Donador de Nitrógeno Lateral: L-Aspartato (X=110, Y=820)
    partes.append(crear_metabolito(
        x=110, y=820,
        nombre="L-Aspartato",
        carbonos="4 Carbonos [4C]",
        detalle="Aportado por AST (Transaminación)",
        detalle2="Dona 2º nitrógeno de urea ➔",
        svg_estructura=ASPARTATO,
        offset_texto=0,
        texto_arriba=True
    ))

    # Reacción 3: Argininosuccinato Sintetasa (ASS)
    partes.append("""
    <g transform="translate(460, 930)">
      <!-- Entrada horizontal de Aspartato desde la izquierda -->
      <path d="M -210 45 Q -90 45 -5 18" fill="none" stroke="#2563eb" stroke-width="2.4" marker-end="url(#arrowCobalt)"/>

      <!-- Flecha principal descendente -->
      <line x1="0" y1="0" x2="0" y2="70" stroke="#0d9488" stroke-width="2.8" marker-end="url(#arrowFlow)"/>

      <!-- Entrada de ATP (a la derecha) -->
      <path d="M 60 10 Q 25 10 5 20" fill="none" stroke="#dc2626" stroke-width="1.8" marker-end="url(#arrowRed)"/>
      <text x="65" y="14" fill="#dc2626" font-family="'Inter', sans-serif" font-size="11" font-weight="800">- 1 ATP</text>

      <!-- Salida de AMP + PPi (a la derecha) -->
      <path d="M 5 45 Q 25 58 65 58" fill="none" stroke="#475569" stroke-width="1.8" marker-end="url(#arrowSlate)"/>
      <text x="70" y="62" fill="#475569" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800">+ AMP + PPi (➔ 2 Pi)</text>

      <!-- Metadatos de la ASS -->
      <g transform="translate(20, 26)">
        <text x="0" y="0" fill="#0f172a" font-family="'Inter', sans-serif" font-size="12.5" font-weight="900">Argininosuccinato Sintetasa (ASS)</text>
        <text x="0" y="14" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="10">EC 6.3.4.5 (Citosólica)</text>
        <text x="0" y="27" fill="#15803d" font-family="'Inter', sans-serif" font-size="9.5" font-weight="700">Intermedio Citrulil-AMP activado</text>
      </g>
    </g>
    """)

    # 5. L-Argininosuccinato (10C) - Intermediario que une ambos nitrógenos
    partes.append(crear_metabolito(
        x=340, y=1000,
        nombre="L-Argininosuccinato",
        carbonos="10 Carbonos [10C]",
        detalle="Condensado Citrulina-Asp",
        detalle2="Escisión trans por ASL",
        svg_estructura=ARGININOSUCCINATO,
        offset_texto=175
    ))

    # Reacción 4: Argininosuccinato Liasa (ASL)
    partes.append("""
    <g transform="translate(460, 1270)">
      <!-- Flecha vertical hacia Arginina -->
      <line x1="0" y1="0" x2="0" y2="70" stroke="#0d9488" stroke-width="2.8" marker-end="url(#arrowFlow)"/>

      <!-- Salida lateral hacia la IZQUIERDA de FUMARATO -->
      <path d="M -5 32 Q -110 32 -195 32" fill="none" stroke="#ea580c" stroke-width="2.4" marker-end="url(#arrowOrange)"/>
      <text x="-90" y="22" fill="#c2410c" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" text-anchor="middle">⮜ + Fumarato (4C)</text>

      <!-- Metadatos de la ASL (a la derecha) -->
      <g transform="translate(20, 24)">
        <text x="0" y="0" fill="#0f172a" font-family="'Inter', sans-serif" font-size="12.5" font-weight="900">Argininosuccinato Liasa (ASL)</text>
        <text x="0" y="14" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="10">EC 4.3.2.1 (Eliminación trans)</text>
        <text x="0" y="27" fill="#be185d" font-family="'Inter', sans-serif" font-size="9.5" font-weight="700">Escisión del esqueleto de 4C</text>
      </g>
    </g>
    """)

    # Fumarato libre resultante (X=110, Y=1230)
    partes.append(crear_metabolito(
        x=110, y=1230,
        nombre="Fumarato",
        carbonos="4 Carbonos [4C] (trans-Dicarboxilato)",
        detalle="Subproducto de la escisión",
        detalle2="Conexión al Ciclo de Krebs (Biciclo)",
        svg_estructura=FUMARATO,
        offset_texto=0,
        texto_arriba=True
    ))

    # Conexión ascendente del Biciclo de Krebs (Fumarato ➔ Aspartato en el carril izquierdo)
    partes.append("""
    <g id="biciclo_krebs_carril_izquierdo">
      <!-- Línea ascendente desde Fumarato (Y=1220) hacia Aspartato (Y=1000) -->
      <path d="M 185 1220 L 185 1020" stroke="#ea580c" stroke-width="2.4" stroke-dasharray="6 4" marker-end="url(#arrowOrange)" fill="none"/>
      <text x="185" y="1125" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="800" fill="#c2410c" text-anchor="middle">↑ FUMARATO ➔ ASPARTATO</text>
    </g>
    """)

    # 6. L-Arginina (6C) (X=380, Y=1350)
    partes.append(crear_metabolito(
        x=380, y=1350,
        nombre="L-Arginina",
        carbonos="6 Carbonos [6C] (Aminoácido)",
        detalle="Grupo guanidino cargado",
        detalle2="Sustrato de la Arginasa",
        svg_estructura=ARGININA,
        offset_texto=135
    ))

    # Reacción 5: Arginasa 1 (ARG1) - Bifurcación hacia Ornitina y Urea
    partes.append("""
    <g transform="translate(460, 1560)">
      <!-- Flecha curva que gira hacia la derecha hacia Ornitina citosólica (X=650) -->
      <path d="M 0 0 L 0 35 Q 0 100 55 100 L 185 100" fill="none" stroke="#0d9488" stroke-width="2.8" marker-end="url(#arrowFlow)"/>

      <!-- Entrada de Agua (+ H2O) para la hidrólisis -->
      <path d="M -60 15 Q -20 15 -5 30" fill="none" stroke="#0284c7" stroke-width="2" marker-end="url(#arrowBlue)"/>
      <text x="-65" y="19" fill="#0284c7" font-family="'Inter', sans-serif" font-size="11" font-weight="900" text-anchor="end">+ H₂O</text>

      <!-- Salida descendente hacia la UREA (Excreción en X=460) -->
      <path d="M 0 45 L 0 260" fill="none" stroke="#dc2626" stroke-width="2.6" marker-end="url(#arrowRed)"/>
      <text x="-15" y="160" fill="#dc2626" font-family="'Inter', sans-serif" font-size="11" font-weight="900" text-anchor="end">Salida de UREA ➔</text>

      <!-- Metadatos de la Arginasa -->
      <g transform="translate(60, 36)">
        <text x="0" y="0" fill="#0f172a" font-family="'Inter', sans-serif" font-size="12.5" font-weight="900">Arginasa 1 (ARG1)</text>
        <text x="0" y="14" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="10">EC 3.5.3.1 (Mn²⁺)</text>
        <text x="0" y="27" fill="#15803d" font-family="'Inter', sans-serif" font-size="9.5" font-weight="700">Hidrólisis terminal</text>
      </g>
    </g>
    """)

    # 7. L-Ornitina Citosólica (Regenerada, X=650, Y=1560)
    partes.append(crear_metabolito(
        x=650, y=1560,
        nombre="L-Ornitina (Citosol)",
        carbonos="5 Carbonos [5C]",
        detalle="Regenerada tras hidrólisis",
        detalle2="Retorno vía ORNT1 ↻",
        svg_estructura=ORNITINA,
        texto_arriba=True
    ))

    # 8. UREA (Producto Final de Excreción, X=416, Y=1830)
    partes.append(crear_metabolito(
        x=416, y=1830,
        nombre="UREA (Carbamida)",
        carbonos="1 Carbono [1C] (Diamida)",
        detalle="Compuesto neutro y no tóxico",
        detalle2="Contiene ambos nitrógenos de desecho",
        svg_estructura=UREA,
        offset_texto=100
    ))

    # Canalización final de Urea hacia el capilar sanguíneo (Y=1920 a Y=2040 en X=460)
    partes.append("""
    <g id="canalizacion_urea_capilar">
      <path d="M 460 1920 L 460 2040" fill="none" stroke="#dc2626" stroke-width="2.8" marker-end="url(#arrowRed)"/>
      <text x="475" y="1980" fill="#991b1b" font-family="'Inter', sans-serif" font-size="11.5" font-weight="900">➔ Excreción hacia Torrente Sanguíneo y Riñón</text>
    </g>
    """)

    return "".join(partes)

# =============================================================================
# 5. FUNCIÓN PRINCIPAL DE EJECUCIÓN
# =============================================================================
def main():
    contenido_svg = construir_ciclo_urea_svg()

    # SVG Puro
    svg_completo = f"""<svg width="{ANCHO_CANVAS}" height="{ALTO_CANVAS}" viewBox="0 0 {ANCHO_CANVAS} {ALTO_CANVAS}" xmlns="http://www.w3.org/2000/svg">
      <defs>
        {DEFS_ENTORNO_UREA}
      </defs>
      {contenido_svg}
    </svg>"""

    ruta_svg = os.path.join(DIR_ACTUAL, "Ciclo_de_la_Urea.svg")
    with open(ruta_svg, "w", encoding="utf-8") as f:
        f.write(svg_completo)

    # HTML Integrado
    html_completo = CABECERA_HTML + contenido_svg + PIE_HTML
    ruta_html = os.path.join(DIR_ACTUAL, "Ciclo_de_la_Urea.html")
    with open(ruta_html, "w", encoding="utf-8") as f:
        f.write(html_completo)

    print(f"✅ Archivo SVG generado con éxito en: {ruta_svg}")
    print(f"✅ Archivo HTML generado con éxito en: {ruta_html}")

if __name__ == "__main__":
    main()
