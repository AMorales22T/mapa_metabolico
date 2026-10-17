# =============================================================================
# MÓDULO DE REVISIÓN: Generador de Reporte por Consola y SVG de Depuración
# =============================================================================
# Archivo original : scripts_generacion/detectar_solapamientos.py (líneas 512 a 552 de 552)
# Descripción      : Imprime la lista numerada de colisiones y genera solapamientos_debug.svg con recuadros de alerta.
# =============================================================================


def escribir_debug(ruta_svg, problemas, salida):
    with open(ruta_svg, encoding="utf-8") as f:
        s = f.read()
    marcas = []
    colores = {"TEXTO-TEXTO": "#ff0000", "FLECHA-TEXTO": "#ff00ff", "TEXTO-ESTRUCTURA": "#ff8800",
               "FLECHA-ESTRUCTURA": "#0088ff", "FUERA-LIENZO": "#000000"}
    for n, (tipo, b, _) in enumerate(problemas, 1):
        c = colores.get(tipo, "#ff0000")
        marcas.append(f'<rect x="{b[0]:.0f}" y="{b[1]:.0f}" width="{b[2]-b[0]:.0f}" height="{b[3]-b[1]:.0f}" '
                      f'fill="{c}" fill-opacity="0.15" stroke="{c}" stroke-width="3"/>'
                      f'<text x="{b[0]:.0f}" y="{b[1]-3:.0f}" fill="{c}" font-size="16" font-weight="900">{n}</text>')
    s = s.replace("</svg>", "<g id='debug_solapamientos'>" + "".join(marcas) + "</g></svg>")
    with open(salida, "w", encoding="utf-8") as f:
        f.write(s)


if __name__ == "__main__":
    default_svg = "prueba_visual_integrada.svg"
    if not os.path.exists(default_svg):
        dir_s = os.path.dirname(os.path.abspath(__file__))
        cand = os.path.join(os.path.dirname(dir_s), "versiones_html", "prueba_visual_integrada.svg")
        if os.path.exists(cand):
            default_svg = cand
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    ruta = args[0] if args else default_svg
    problemas, _ = analizar(ruta)
    resumen = {}
    for tipo, b, msg in problemas:
        resumen[tipo] = resumen.get(tipo, 0) + 1
    maxn = 9999
    if "--max" in sys.argv:
        maxn = int(sys.argv[sys.argv.index("--max") + 1])
    for n, (tipo, b, msg) in enumerate(problemas[:maxn], 1):
        print(f"{n:3d}. [{tipo:17s}] ({b[0]:.0f},{b[1]:.0f}) {msg}")
    print("\nRESUMEN:", ", ".join(f"{k}={v}" for k, v in sorted(resumen.items())) or "sin solapamientos ✓")
    print("TOTAL:", len(problemas))
    if "--debug" in sys.argv:
        escribir_debug(ruta, problemas, "solapamientos_debug.svg")
        print("→ solapamientos_debug.svg generado")
    sys.exit(1 if problemas else 0)
