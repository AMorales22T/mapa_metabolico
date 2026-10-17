# =============================================================================
# MÓDULO DE REVISIÓN: Orquestador y Generador de la Capa SVG de Conexiones
# =============================================================================
# Archivo original : scripts_generacion/conectar_rutas.py (líneas 671 a 850 de 850)
# Descripción      : Trazado secuencial con memoria acumulativa (marcar_ruta) e inyección de la capa en el SVG/HTML.
# =============================================================================

# ===========================================================================
# 6. ORQUESTACIÓN
# ===========================================================================
def caja_endpoint(ep, cajas):
    if "rect" in ep:
        return ep["rect"]
    if ep["id"] not in cajas:
        raise KeyError(f"id '{ep['id']}' no encontrado en el SVG")
    return cajas[ep["id"]]


def trazar_tramo(rj, b_src, lado_src, b_dst, lado_dst):
    ini = anillo(rj, b_src, lado_src)
    met = anillo(rj, b_dst, lado_dst)
    # El origen/destino propios no deben bloquear su anillo
    camino, coste, exp = astar(rj, ini, met, b_dst)
    if camino is None:
        return None, None, exp
    pts = simplificar([rj.centro(i) for i in camino])
    p_ini = punto_en_borde(b_src, pts[0], 2)
    p_fin = punto_en_borde(b_dst, pts[-1], 3)
    p_ini = alinear_stub(b_src, p_ini, pts[0])
    p_fin = alinear_stub(b_dst, p_fin, pts[-1])
    pts = simplificar([p_ini] + pts + [p_fin])
    return pts, coste, exp


def marcar_ruta(rj, pts):
    for p, q in zip(pts[:-1], pts[1:]):
        rj.segmento(p, q, RUTA, 1, RUTA_HALO)


def color_oscuro(hexc, f=0.72):
    r, g, b = (int(hexc[i:i + 2], 16) for i in (1, 3, 5))
    return "#%02x%02x%02x" % (int(r * f), int(g * f), int(b * f))


def generar_capa(svg_str, celda=12, verbose=True):
    root = ET.fromstring(svg_str)
    ancho, alto = _num(root.get("width")), _num(root.get("height"))
    t0 = time.time()
    elems = leer_svg(root)
    cajas = cajas_por_id(elems)
    rj = construir_rejilla(elems, cajas, ancho, alto, celda)
    if verbose:
        print(f"· {len(elems)} elementos leídos, rejilla {rj.W}×{rj.H} (celda {celda}px) "
              f"en {time.time() - t0:.1f}s")

    colores = sorted({c["color"] for c in CONEXIONES})
    defs = ["<defs>"]
    for col in colores:
        defs.append(f'<marker id="cxFlecha{col[1:]}" markerWidth="7" markerHeight="7" refX="5.5" refY="3.5" '
                    f'orient="auto" markerUnits="strokeWidth"><path d="M 0 0 L 7 3.5 L 0 7 Z" fill="{col}"/></marker>')
    defs.append("</defs>")

    trazos, rotulos, informe = [], [], []
    for cx in CONEXIONES:
        t1 = time.time()
        try:
            b_src = caja_endpoint(cx["src"], cajas)
            b_dst = caja_endpoint(cx["dst"], cajas)
        except KeyError as err:
            informe.append((cx["id"], "OMITIDA", str(err)))
            continue
        tramos = []
        if cx.get("via"):
            v = cx["via"]
            pa, _, _ = trazar_tramo(rj, b_src, cx["src"].get("lado"), v, cx["via_in"])
            if pa:
                marcar_ruta(rj, pa)
            pb, _, _ = trazar_tramo(rj, v, cx["via_out"], b_dst, cx["dst"].get("lado"))
            if pa is None or pb is None:
                informe.append((cx["id"], "SIN RUTA", ""))
                continue
            tramos = [(pa, False), (pb, True)]
        else:
            p, _, _ = trazar_tramo(rj, b_src, cx["src"].get("lado"), b_dst, cx["dst"].get("lado"))
            if p is None:
                informe.append((cx["id"], "SIN RUTA", ""))
                continue
            tramos = [(p, True)]

        # Diagnóstico: obstáculos atravesados (antes de marcar la ruta propia)
        cruces_duros = cruces_trazo = 0
        for pts, _ in tramos:
            for p, q in zip(pts[1:-2], pts[2:-1]):
                n = max(1, int(math.dist(p, q) / rj.c))
                for k in range(n + 1):
                    x, y = p[0] + (q[0] - p[0]) * k / n, p[1] + (q[1] - p[1]) * k / n
                    cval = rj.coste[rj.idx(*rj.celda_de(x, y))]
                    if cval >= DURO:
                        cruces_duros += 1
                    elif cval >= TRAZO:
                        cruces_trazo += 1

        # Rótulo en el tramo más largo
        todos = [pt for pts, _ in tramos for pt in pts]
        mejor_tramo = max((pts for pts, _ in tramos), key=lambda P: sum(math.dist(a, b) for a, b in zip(P, P[1:])))
        rot = colocar_rotulo(rj, mejor_tramo, cx["rotulo"]) if cx.get("rotulo") else None
        for pts, _ in tramos:
            marcar_ruta(rj, pts)
        if rot:
            rj.caja(rot[3], DURO)

        col = cx["color"]
        g = [f'<g id="cx_{cx["id"]}" class="conexion-inter-ruta">']
        for pts, con_flecha in tramos:
            pts_d = recortar_final(pts, 2) if con_flecha else pts
            mk = f' marker-end="url(#cxFlecha{col[1:]})"' if con_flecha else ""
            g.append(f'<path d="{path_redondeado(pts_d)}" fill="none" stroke="#ffffff" stroke-width="6" '
                     f'stroke-linecap="round" stroke-linejoin="round" opacity="0.55"/>')
            g.append(f'<path d="{path_redondeado(pts_d)}" fill="none" stroke="{col}" stroke-width="2.6" '
                     f'stroke-dasharray="10 6" stroke-linecap="round" stroke-linejoin="round"{mk}/>')
        g.append("</g>")
        trazos.append("".join(g))
        if rot:
            x, y, anc, _ = rot
            rotulos.append(
                f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anc}" fill="{color_oscuro(col)}" '
                f'font-size="{FS_ROTULO}" font-weight="800" font-family="\'Inter\', sans-serif" '
                f'stroke="#ffffff" stroke-width="3.2" stroke-linejoin="round" paint-order="stroke">'
                f'{cx["rotulo"]}</text>')
        largo = sum(math.dist(a, b) for pts, _ in tramos for a, b in zip(pts, pts[1:]))
        informe.append((cx["id"], "OK", f"{largo:6.0f}px  cruces flecha≈{cruces_trazo:2d}  "
                        f"obstáculos={cruces_duros}  rótulo={'sí' if rot else 'NO'}  ({time.time() - t1:.1f}s)"))
        if verbose:
            print(f"  ✓ {cx['id']:<22s} {informe[-1][2]}")
        del todos

    capa = ('\n<!-- ================= CAPA DE CONEXIONES ENTRE RUTAS (conectar_rutas.py) ================= -->\n'
            '<g id="capa_conexiones_inter_ruta">' + "".join(defs) +
            '<g id="cx_trazos">' + "\n".join(trazos) + "</g>" +
            '<g id="cx_rotulos">' + "\n".join(rotulos) + "</g></g>\n")
    return capa, informe


def insertar_capa(svg_str, capa):
    k = svg_str.rfind("</svg>")
    return svg_str[:k] + capa + svg_str[k:]


def main():
    celda = 12
    if "--celda" in sys.argv:
        celda = int(sys.argv[sys.argv.index("--celda") + 1])

    import generar_prueba_visual_integrada as gen
    print("Generando mapa base (sin modificaciones)…")
    html_base, svg_base = gen.construir_mapa_organico()

    capa, informe = generar_capa(svg_base, celda)
    svg_nuevo = insertar_capa(svg_base, capa)
    html_nuevo = html_base.replace(svg_base, svg_nuevo, 1)

    salida = DIR_HTML
    if "--salida" in sys.argv:
        salida = sys.argv[sys.argv.index("--salida") + 1]
    r_svg = os.path.join(salida, "prueba_visual_integrada_conectada.svg")
    r_html = os.path.join(salida, "prueba_visual_integrada_conectada.html")
    with open(r_svg, "w", encoding="utf-8") as f:
        f.write(svg_nuevo)
    with open(r_html, "w", encoding="utf-8") as f:
        f.write(html_nuevo)

    print("\nRESUMEN DE CONEXIONES")
    ok = sum(1 for _, est, _ in informe if est == "OK")
    for cid, est, msg in informe:
        if est != "OK":
            print(f"  ✗ {cid:<22s} {est} {msg}")
    print(f"  {ok}/{len(CONEXIONES)} conexiones trazadas")
    print(f"\nSVG : {r_svg}\nHTML: {r_html}")

    if "--sin-png" not in sys.argv and shutil.which("rsvg-convert"):
        r_png = os.path.join(DIR_PREVIEWS, "prueba_visual_integrada_conectada_preview.png")
        subprocess.run(["rsvg-convert", "-w", "2900", "-o", r_png, r_svg], check=False)
        print(f"PNG : {r_png}")


if __name__ == "__main__":
    main()
