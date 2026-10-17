# =============================================================================
# MÓDULO DE REVISIÓN: Encabezado Python e Inyección de Plantilla
# =============================================================================
# Archivo original : 07_AMPLIACION_TEMARIO/interactividad_html.py (líneas 1 a 40 de 1638)
# Descripción      : Importación de datos estequiométricos y firma de construir_html_mapa_ampliado.
# =============================================================================

"""
MÓDULO DE INTERACTIVIDAD PARA VISORES METABÓLICOS HTML (MOTOR DE ESTUDIO CIENTÍFICO)
====================================================================================
Genera interfaces interactivas de alta fidelidad con:
- Clic para resaltar/atenuar vías (distingue clic de arrastre <= 4px)
- Índice lateral desplegable (25 vías) con zoom animado centrado vectorial (CTM / getBBox)
- Buscador global sin acentos ni mayúsculas con pulso animado y navegación
- Ficha flotante / Tooltip para metabolitos (m_*) y enzimas (rx_*)
- Selector de Estados Metabólicos (Normal, Posprandial, Ayuno)
- Soporte táctil completo (arrastre 1 dedo, zoom pellizco 2 dedos)
- Atajos de teclado ('/' busca, 'Esc' limpia, 'F' ajusta)
- Menú de navegación entre vistas y descarga PDF
- Optimización print sin elementos UI
"""
import json
import os
import sys

DIR_INTERACT = os.path.dirname(os.path.abspath(__file__))
DIR_ROOT = os.path.dirname(DIR_INTERACT)
sys.path.append(os.path.join(DIR_ROOT, "06_REGULACION_Y_LEYENDA"))

try:
    import reacciones_estequiometria as re_est
    TABLA_REACCIONES_DATA = re_est.REACCIONES_ESTEQUIOMETRIA
except Exception:
    TABLA_REACCIONES_DATA = {}

def construir_html_mapa_ampliado(svg_final, w_canvas=7320, h_canvas=5490, vb_x=-760, vb_y=-250):
    """
    Empaqueta el SVG ampliado de 25 vías en un visor interactivo de estudio completo.
    """
    html_plantilla = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Mapa Metabólico Integrado — Herramienta Interactiva Ampliada (25 Vías)</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@600;700;800&display=swap" rel="stylesheet">
