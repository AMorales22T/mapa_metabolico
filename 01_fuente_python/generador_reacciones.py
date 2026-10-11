#!/usr/bin/env python3
"""
GENERADOR MODULAR DE REACCIONES METABÓLICAS EN SVG / HTML
=========================================================
Este script muestra cómo Python genera automáticamente las flechas, textos,
estructuras químicas y curvas de energía respetando las medidas del Manual de Estilo.
"""

def generar_metabolito_svg(x, y, nombre, carbonos, detalle="", svg_estructura=""):
    """Genera el bloque visual de un metabolito con su estructura y texto."""
    return f"""
    <!-- Metabolito: {nombre} -->
    <g transform="translate({x}, {y})">
      <!-- Estructura Química -->
      <g transform="translate(80, 0)">
        {svg_estructura}
      </g>
      <!-- Texto descriptivo flotante (Sin cajas) -->
      <g transform="translate(200, 25)">
        <text x="0" y="0" fill="#0f172a" font-size="17" font-weight="800">{nombre}</text>
        <text x="0" y="18" fill="#ea580c" font-size="12" font-weight="700">{carbonos}</text>
        <text x="0" y="32" fill="#64748b" font-size="11">{detalle}</text>
      </g>
    </g>
    """

def generar_paso_reaccion_svg(x, y, enzima, ec="", inhibidor="", activador="", entra_energia="", sale_energia=""):
    """Genera la flecha central de reacción con sus curvas de energía acoplada y enzima."""
    curvas_energia = ""
    
    # Si hay gasto energético (ej. - 1 ATP)
    if entra_energia:
        curvas_energia += f"""
        <!-- Entrada de Energía -->
        <path d="M -90 15 Q -30 12 -5 32" fill="none" stroke="#dc2626" stroke-width="2" marker-end="url(#arrowRed)"/>
        <text x="-95" y="18" fill="#dc2626" font-size="12" font-weight="800" text-anchor="end">{entra_energia}</text>
        """
        
    # Si hay salida energética (ej. + 1 ADP)
    if sale_energia:
        curvas_energia += f"""
        <!-- Salida de Subproducto -->
        <path d="M -5 38 Q -30 58 -90 55" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrowSlate)"/>
        <text x="-95" y="58" fill="#475569" font-size="12" font-weight="700" text-anchor="end">{sale_energia}</text>
        """

    regulacion_txt = ""
    if inhibidor:
        regulacion_txt = f'<text x="0" y="27" fill="#e11d48" font-size="10" font-weight="700">⊣ Inhibida por {inhibidor}</text>'
    elif activador:
        regulacion_txt = f'<text x="0" y="27" fill="#16a34a" font-size="10" font-weight="700">⊕ Activada por {activador}</text>'

    return f"""
    <!-- Reacción Catalizada por: {enzima} -->
    <g transform="translate({x}, {y})">
      <!-- Flecha principal de flujo -->
      <line x1="0" y1="0" x2="0" y2="70" stroke="#ea580c" stroke-width="3" marker-end="url(#arrowFlow)"/>
      
      {curvas_energia}

      <!-- Enzima y Regulación -->
      <g transform="translate(18, 22)">
        <text x="0" y="0" fill="#0f172a" font-size="13" font-weight="800">{enzima}</text>
        <text x="0" y="14" fill="#64748b" font-size="10" font-family="'JetBrains Mono', monospace">{ec}</text>
        {regulacion_txt}
      </g>
    </g>
    """

# Estructura del Anillo de Haworth en código SVG directo
ANILLO_GLUCOSA_SVG = """
<polygon points="50,22 72,36 50,58 16,58 0,36 16,22" fill="#ffffff" stroke="#0f172a" stroke-width="2.5"/>
<circle cx="16" cy="22" r="7" fill="#ffffff"/>
<text x="16" y="26" fill="#dc2626" font-size="14" font-weight="800" text-anchor="middle">O</text>
<line x1="0" y1="36" x2="0" y2="12" stroke="#0f172a" stroke-width="2.2"/>
<text x="0" y="7" fill="#0f172a" font-size="11" font-weight="800" text-anchor="middle">CH₂OH</text>
<line x1="72" y1="36" x2="88" y2="36" stroke="#0f172a" stroke-width="2"/>
<text x="98" y="40" fill="#0f172a" font-size="11" font-weight="700">OH</text>
<line x1="50" y1="58" x2="50" y2="72" stroke="#0f172a" stroke-width="2"/>
<text x="50" y="83" fill="#0f172a" font-size="11" font-weight="700" text-anchor="middle">OH</text>
<line x1="16" y1="58" x2="16" y2="72" stroke="#0f172a" stroke-width="2"/>
<text x="16" y="83" fill="#0f172a" font-size="11" font-weight="700" text-anchor="middle">HO</text>
<line x1="0" y1="36" x2="-14" y2="36" stroke="#0f172a" stroke-width="2"/>
<text x="-24" y="40" fill="#0f172a" font-size="11" font-weight="700">HO</text>
"""

if __name__ == "__main__":
    print("Este módulo contiene las funciones base para generar reacciones en Python.")
    print("Ejemplo de llamada:")
    print("metabolito = generar_metabolito_svg(380, 115, 'D-Glucosa', '6 Carbonos', 'Sustrato libre', ANILLO_GLUCOSA_SVG)")
    print("reaccion = generar_paso_reaccion_svg(460, 215, 'Hexoquinasa', 'EC 2.7.1.1', inhibidor='G-6-P', entra_energia='- 1 ATP', sale_energia='+ 1 ADP')")
