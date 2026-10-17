# =============================================================================
# MÓDULO DE REVISIÓN: Ensamblador Final del Póster Vectorial Ampliado
# =============================================================================
# Archivo original : 07_AMPLIACION_TEMARIO/generar_ampliacion.py (líneas 771 a 925 de 925)
# Descripción      : Une el mapa central con las bandas laterales, aplica correcciones y exporta SVG, HTML, PDF 120x84 cm y PNG.
# =============================================================================

# =============================================================================
# ENSAMBLAJE FINAL DEL PÓSTER VECTORIAL COMPLETO
# =============================================================================

def ensamblar_mapa_ampliado():
    print(f"1. Leyendo mapa central original: {RUTA_ORIGINAL_HTML}")
    with open(RUTA_ORIGINAL_HTML, "r", encoding="utf-8") as f:
        html_orig = f.read()

    svg_start = html_orig.find("<svg")
    if svg_start == -1:
        raise ValueError("No se encontró la etiqueta <svg en el archivo original")
    svg_tag_end = html_orig.find(">", svg_start) + 1
    svg_close = html_orig.rfind("</svg>")
    inner_svg_orig = html_orig[svg_tag_end:svg_close]

    print(f"   ✓ Mapa original extraído ({len(inner_svg_orig):,} caracteres)")

    # Actualizar la leyenda central para incluir las nuevas vías y 'CÓDIGO DE COLORES:'
    inner_svg_orig = actualizar_bloque_leyenda_central(inner_svg_orig)
    print("   ✓ Leyenda institucional actualizada con Vías 18–25 y rótulo corregido")

    css_fonts = cargar_fuentes_base64()

    W_CANVAS = 7320
    H_CANVAS = 5120
    VB_X = -760
    VB_Y = 0

    fondo_izq = construir_fondo_izquierdo()
    fondo_der = construir_fondo_derecho()
    banda_izq = construir_banda_izquierda()
    banda_der = construir_banda_derecha()

    svg_final = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W_CANVAS}" height="{H_CANVAS}" viewBox="{VB_X} {VB_Y} {W_CANVAS} {H_CANVAS}">
    <style>
      {css_fonts}
      text {{ font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }}
    </style>
    <defs>
      <linearGradient id="print_gradPlasma" x1="0" y1="350" x2="0" y2="431.5" gradientUnits="userSpaceOnUse">
        <stop offset="0%" stop-color="#450a0a" stop-opacity="0.95"/>
        <stop offset="65%" stop-color="#7f1d1d" stop-opacity="0.9"/>
        <stop offset="100%" stop-color="#991b1b" stop-opacity="0.85"/>
      </linearGradient>

      <marker id="arrowOrange" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto">
        <path d="M0,0 L9,4.5 L0,9 Z" fill="#ea580c"/>
      </marker>
      <marker id="arrowTeal" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto">
        <path d="M0,0 L9,4.5 L0,9 Z" fill="#0d9488"/>
      </marker>
    </defs>

    <!-- 1. Fondo base del lienzo completo -->
    <g id="print_fondo_base">
      <rect x="{VB_X}" y="{VB_Y}" width="{W_CANVAS}" height="{H_CANVAS}" fill="#f1f5f9" />
    </g>

    <!-- 2. Extensiones laterales biológicas continuas (con torrente vascular a Y=350..418) -->
    {fondo_izq}
    {fondo_der}

    <!-- 3. Contenido íntegro del mapa central original con leyenda actualizada -->
    {inner_svg_orig}

    <!-- 4. Contenidos de ampliación temática en las bandas laterales -->
    {banda_izq}
    {banda_der}
</svg>"""

    print("2. Aplicando calibraciones y correcciones biológicas validadas...")
    from correcciones_mapa import aplicar_correcciones_mapa
    svg_final = aplicar_correcciones_mapa(svg_final)

    print(f"   Escribiendo SVG ampliado en: {RUTA_OUT_SVG}")
    with open(RUTA_OUT_SVG, "w", encoding="utf-8") as f:
        f.write(svg_final)

    print("3. Generando visor interactivo enriquecido de 25 vías...")
    html_final = construir_html_mapa_ampliado(svg_final, W_CANVAS, H_CANVAS, VB_X, VB_Y)

    print(f"   Escribiendo HTML visor interactivo en: {RUTA_OUT_HTML}")
    with open(RUTA_OUT_HTML, "w", encoding="utf-8") as f:
        f.write(html_final)

    # Guardar copias directas en versiones_html/
    ruta_copia_html1 = os.path.join(DIR_HTML, "mapa_cartulina_ampliado.html")
    ruta_copia_html2 = os.path.join(DIR_HTML, "mapa_ampliado_interactivo.html")
    ruta_copia_html_num = os.path.join(DIR_HTML, "01_mapa_ampliado_completo_25_vias.html")
    ruta_copia_index = os.path.join(DIR_HTML, "index.html")
    with open(ruta_copia_html1, "w", encoding="utf-8") as f:
        f.write(html_final)
    with open(ruta_copia_html2, "w", encoding="utf-8") as f:
        f.write(html_final)
    with open(ruta_copia_html_num, "w", encoding="utf-8") as f:
        f.write(html_final)
    with open(ruta_copia_index, "w", encoding="utf-8") as f:
        f.write(html_final)
    print(f"   ✓ Copias interactivas guardadas en:")
    print(f"     - {ruta_copia_html_num} (Entregable principal numerado)")
    print(f"     - {ruta_copia_html1}")
    print(f"     - {ruta_copia_html2}")
    print(f"     - {ruta_copia_index}")

    # Exportación con rsvg-convert a PDF y PNG
    rsvg = shutil.which("rsvg-convert")
    if rsvg:
        print("4. Generando PDF imprimible vectorial a tamaño completo (1200 × 840 mm) con rsvg-convert...")
        cmd_pdf = [
            rsvg, "-f", "pdf",
            "-w", "1200mm",
            "-h", "840mm",
            "--page-width", "1200mm",
            "--page-height", "840mm",
            "-o", RUTA_OUT_PDF,
            RUTA_OUT_SVG
        ]
        subprocess.run(cmd_pdf, check=True)
        print(f"   ✓ PDF vectorial generado con éxito: {RUTA_OUT_PDF}")

        # Copia de seguridad en versiones_impresion/
        shutil.copy2(RUTA_OUT_PDF, RUTA_COPIA_PDF)
        ruta_copia_pdf_num = os.path.join(DIR_IMPRESION, "01_mapa_ampliado_completo_120x90cm.pdf")
        shutil.copy2(RUTA_OUT_PDF, ruta_copia_pdf_num)
        ruta_copia_pdf_full = os.path.join(DIR_IMPRESION, "01_mapa_ampliado_completo_tamano_completo.pdf")
        shutil.copy2(RUTA_OUT_PDF, ruta_copia_pdf_full)
        ruta_copia_pdf_84 = os.path.join(DIR_IMPRESION, "01_mapa_ampliado_completo_120x84cm.pdf")
        shutil.copy2(RUTA_OUT_PDF, ruta_copia_pdf_84)
        print(f"   ✓ Copias guardadas en:")
        print(f"     - {ruta_copia_pdf_num} (Entregable principal PDF)")
        print(f"     - {ruta_copia_pdf_full}")
        print(f"     - {ruta_copia_pdf_84}")
        print(f"     - {RUTA_COPIA_PDF}")

        print("5. Generando vista previa PNG en alta resolución (2400 × 1678 px)...")
        cmd_png = [
            rsvg,
            "-w", "2400",
            "-h", "1678",
            "-o", RUTA_OUT_PNG,
            RUTA_OUT_SVG
        ]
        subprocess.run(cmd_png, check=True)
        print(f"   ✓ Vista previa PNG generada con éxito: {RUTA_OUT_PNG}")
    else:
        print("   ⚠ rsvg-convert no encontrado en el sistema; solo se crearon SVG y HTML.")

    print("\n=======================================================")
    print("¡AMPLIACIÓN DEL TEMARIO GENERADA EXITOSAMENTE!")
    print("=======================================================")


if __name__ == "__main__":
    ensamblar_mapa_ampliado()
