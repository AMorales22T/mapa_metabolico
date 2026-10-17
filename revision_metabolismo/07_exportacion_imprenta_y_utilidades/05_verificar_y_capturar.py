# =============================================================================
# MÓDULO DE REVISIÓN: Verificador y Generador de Capturas
# =============================================================================
# Archivo original : scripts_generacion/verificar_y_capturar.py (líneas 1 a 78 de 78)
# Descripción      : Automatiza la comprobación visual y renderizado de vistas previas.
# =============================================================================

#!/usr/bin/env python3
"""
SCRIPT DE VERIFICACIÓN Y CAPTURA HEADLESS PARA PRUEBA_VISUAL_INTERACTIVA.HTML
============================================================================
1. Comprueba consola del navegador para certificar cero errores de JavaScript.
2. Genera las 4 capturas solicitadas:
   - captura_vista_inicial.png
   - captura_via_resaltada.png (con Vía 6: Ciclo de Krebs centrada y resaltada)
   - captura_busqueda.png (con búsqueda activa de "Glucosa-6-Fosfato" y pulso)
   - captura_modo_ayuno.png (con Modo Ayuno activo y rótulo visible)
"""
import os
import subprocess
import sys

DIR_SCRIPT = os.path.dirname(os.path.abspath(__file__))
DIR_BASE = os.path.dirname(DIR_SCRIPT) if os.path.basename(DIR_SCRIPT) == "scripts_generacion" else DIR_SCRIPT
DIR_HTML = os.path.join(DIR_BASE, "versiones_html")
DIR_CAPTURAS = os.path.join(DIR_BASE, "capturas_y_pruebas")

RUTA_HTML = os.path.join(DIR_HTML, "prueba_visual_interactiva.html")
BRAVE_BIN = "/opt/brave-bin/brave"

capturas = [
    ("captura_vista_inicial.png", "", "Vista inicial estándar"),
    ("captura_via_resaltada.png", "?via=6", "Vía 6 (Ciclo de Krebs) resaltada y centrada"),
    ("captura_busqueda.png", "?search=Glucosa-6-Fosfato", "Búsqueda activa de 'Glucosa-6-Fosfato' con pulso"),
    ("captura_modo_ayuno.png", "?state=ayuno", "Modo metabólico de Ayuno activo")
]

print("=== INICIANDO VERIFICACIÓN HEADLESS Y GENERACIÓN DE CAPTURAS ===")
todos_errores = []

for nombre_archivo, url_params, descripcion in capturas:
    out_path = os.path.join(DIR_CAPTURAS, nombre_archivo)
    url = f"file://{RUTA_HTML}{url_params}"
    
    print(f"\nGenerando {nombre_archivo} ({descripcion})...")
    cmd = [
        BRAVE_BIN,
        "--headless=new",
        "--no-sandbox",
        "--disable-gpu",
        "--window-size=1920,1080",
        "--enable-logging=stderr",
        "--v=1",
        "--virtual-time-budget=3000",
        f"--screenshot={out_path}",
        url
    ]
    
    p = subprocess.run(cmd, capture_output=True, text=True)
    
    if os.path.exists(out_path) and os.path.getsize(out_path) > 10000:
        print(f"   ✓ Captura guardada: {out_path} ({os.path.getsize(out_path):,} bytes)")
    else:
        print(f"   ✗ Error: No se pudo generar {out_path}")
        sys.exit(1)
        
    # Analizar stderr en busca de errores JS
    lineas_stderr = p.stderr.splitlines()
    errores_js = [l for l in lineas_stderr if any(err in l for err in ["Uncaught", "TypeError", "ReferenceError", "SyntaxError", "RangeError"])]
    if errores_js:
        print(f"   ✗ Errores JS detectados en consola ({url_params}):")
        for err in errores_js:
            print(f"     {err}")
        todos_errores.extend(errores_js)
    else:
        print("   ✓ Consola limpia: CERO errores de JavaScript detectados.")

print("\n=== RESUMEN DE VERIFICACIÓN ===")
if not todos_errores:
    print("✓ TODAS LAS PRUEBAS PASARON EXITOSAMENTE:")
    print("  - Consola del navegador sin errores ni excepciones.")
    print("  - 4 capturas en alta resolución (1920x1080) generadas y verificadas.")
else:
    print(f"✗ Se detectaron {len(todos_errores)} errores en consola.")
    sys.exit(1)
