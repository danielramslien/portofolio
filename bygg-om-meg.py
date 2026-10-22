#!/usr/bin/env python3
"""Lager undersidene om-meg.html og attester.html fra index.html.

Undersidene bruker samme kode, stil og innhold som forsiden, men viser bare
sin egen seksjon og Kontakt. Kjør dette skriptet etter hver endring i index.html:

    python3 bygg-om-meg.py
"""
import pathlib
root = pathlib.Path(__file__).parent
src = (root / 'index.html').read_text(encoding='utf-8')
PAGES = {
    'om-meg.html':   ('about', 'om-meg',   'Om meg · Daniel Ramslien'),
    'attester.html': ('refs',  'attester', 'Attester · Daniel Ramslien'),
}
for fname, (page, anchor, title) in PAGES.items():
    s = src.replace('<html lang="no" data-page="home">', f'<html lang="no" data-page="{page}">', 1)
    for sec in ('top', 'arbeid', 'verktoy', 'anbefalinger', 'resultater'):
        s = s.replace(f'href="#{sec}"', f'href="index.html#{sec}"')
    s = s.replace('<a class="skip" href="index.html#arbeid"', f'<a class="skip" href="#{anchor}"', 1)
    s = s.replace('<title>Daniel Ramslien Portefølje</title>', f'<title>{title}</title>', 1)
    s = s.replace('<meta property="og:url" content="https://portofolio-8jx.pages.dev/">', f'<meta property="og:url" content="https://portofolio-8jx.pages.dev/{fname[:-5]}">', 1)
    if page == 'refs':
        old = 'id="kontakt-tittel" data-i18n-html="contact.title">La oss ta en prat</h2>'
        assert old in s
        s = s.replace(old, 'id="kontakt-tittel" data-i18n="nav.contact">Kontakt</h2>', 1)
    (root / fname).write_text(s, encoding='utf-8')
    print(fname, 'oppdatert')
