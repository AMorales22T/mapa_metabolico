#!/usr/bin/env python3
# Uso: python3 parchear_ascii_encabezado.py archivo1 [archivo2 ...]   (idempotente, solo stdlib)
# Tarjeta de autoria: agranda la franja del ASCII "MAPA METABOLICO" (fuente 16, paso 20), centra las
# 2 pildoras y baja linea, divisores y columnas 56 px; la tarjeta crece de 505 a 561. Sirve sobre original o parcheado.
import re, sys
REP = [('height="505" rx="22"', 'height="561" rx="22"'),
       ('<rect x="0" y="0" width="310" height="24"', '<rect x="0" y="23" width="310" height="24"'),
       ('<text x="155" y="16"', '<text x="155" y="39"'),
       ('<rect x="1330" y="-2" width="490"', '<rect x="1330" y="21" width="490"'),
       ('<text x="1575" y="15"', '<text x="1575" y="38"'),
       ('y1="64" x2="1825" y2="64"', 'y1="120" x2="1825" y2="120"'),
       ('translate(35, 82)', 'translate(35, 138)'), ('translate(565, 82)', 'translate(565, 138)'),
       ('translate(1495, 82)', 'translate(1495, 138)'),
       ('y1="80" x2="535" y2="480"', 'y1="136" x2="535" y2="536"'),
       ('y1="80" x2="1470" y2="480"', 'y1="136" x2="1470" y2="536"')]
def patch(s):
    a = s.find('id="bloque_autoria"'); e = s.find('translate(1495, 82)', a)
    if a < 0 or e < 0: return s, 'sin bloque / ya parcheado'
    seg = s[a:e + len('translate(1495, 82)')]
    for o, n in REP:
        assert seg.count(o) == 1, f'esperaba 1 coincidencia de {o!r}, hay {seg.count(o)}'
        seg = seg.replace(o, n)
    def txt(m):
        t = re.sub(r'font-size="[\d.]+"', 'font-size="16"', m.group(0))
        t = re.sub(r'font-weight="\d+"', 'font-weight="700"', t)
        t = re.sub(r'line-height: [\d.]+px', 'line-height: 20px', t)
        return re.sub(r'(<text x="340" y=")[-\d.]+', r'\g<1>10', t)
    seg, n1 = re.subn(r'<text x="340" y="[-\d.]+"[^>]*>', txt, seg, count=1)
    ys = iter(['10', '30', '50', '70'])
    seg, n2 = re.subn(r'(<tspan x="340" y=")[-\d.]+', lambda m: m.group(1) + next(ys), seg)
    assert (n1, n2) == (1, 4), (n1, n2)
    return s[:a] + seg + s[e + len('translate(1495, 82)'):], 'parcheado'
def fix_font(s):
    # El SVG trae <style>text{font-family:Inter}</style>, que gana al atributo font-family: el ASCII salia proporcional.
    # El style en linea si gana; ligaduras fuera para que JetBrains Mono no fusione |_| , \\/ , etc.
    css = ("style=\"font-family: 'JetBrains Mono', 'DejaVu Sans Mono', Menlo, Consolas, monospace; "
           "font-variant-ligatures: none; font-feature-settings: 'liga' 0, 'calt' 0; white-space: pre; line-height: 20px;\"")
    return re.sub(r'(<text x="340" y="10"[^>]*?)style="white-space: pre; line-height: 20px;"', lambda m: m.group(1) + css, s, count=1)
for f in sys.argv[1:]:
    s = open(f, encoding='utf8').read(); n, msg = patch(s); n = fix_font(n)
    if n != s: open(f, 'w', encoding='utf8').write(n)
    print(msg, f)
