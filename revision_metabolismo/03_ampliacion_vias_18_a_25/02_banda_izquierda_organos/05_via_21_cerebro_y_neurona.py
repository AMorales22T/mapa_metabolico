# =============================================================================
# MÓDULO DE REVISIÓN: Vía 21: Cerebro, Barrera Hematoencefálica y Neurona
# =============================================================================
# Archivo original : 07_AMPLIACION_TEMARIO/generar_ampliacion.py (líneas 463 a 480 de 925)
# Descripción      : Transporte GLUT-1/GLUT-3 de glucosa en estado normal y adaptación a cuerpos cetónicos (MCT) en ayuno prolongado.
# =============================================================================

    # -------------------------------------------------------------------------
    # VÍA 21: CEREBRO Y SISTEMA NERVIOSO (DIBUJO ANATÓMICO DIDÁCTICO)
    # -------------------------------------------------------------------------
    p.append('<g id="ruta_cerebro_combustibles" class="ruta-metabolica">')
    p.append(encabezado_via(-710, 2920, 21, "CEREBRO Y SISTEMA NERVIOSO: BHE Y NEURONA", "Anatomía del encéfalo • Neurona mielinizada • GLUT1/3 • Cuerpos cetónicos", color="#2563eb"))

    # Dibujo anatómico del cerebro, cerebelo y neurona mielinizada
    p.append(ea.esquema_cerebro_y_neurona_didactico(x=-690, y=2970, w=620, h=420))
    p.append('</g>')

    p.append("</g>")
    return "\n".join(p)


# =============================================================================
# CONTENIDOS METABÓLICOS DE LA BANDA DERECHA
# =============================================================================

