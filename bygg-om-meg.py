#!/usr/bin/env python3
"""Lager om-meg.html fra index.html.

Om meg-siden bruker samme kode, stil og innhold som forsiden, men viser bare
Om meg og Kontakt. Kjør dette skriptet etter hver endring i index.html:

    python3 bygg-om-meg.py
"""
import re, pathlib
root = pathlib.Path(__file__).parent
s = (root / 'index.html').read_text(encoding='utf-8')
s = s.replace('<html lang="no" data-page="home">', '<html lang="no" data-page="about">', 1)
# Lenker til seksjoner som bare finnes på forsiden
for sec in ('top', 'arbeid', 'verktoy', 'anbefalinger', 'attester', 'resultater'):
    s = s.replace(f'href="#{sec}"', f'href="index.html#{sec}"')
s = s.replace('<a class="skip" href="index.html#arbeid"', '<a class="skip" href="#om-meg"', 1)
s = s.replace('<title>Daniel Ramslien Portefølje</title>', '<title>Om meg · Daniel Ramslien</title>', 1)
s = s.replace('<meta property="og:url" content="https://portofolio-8jx.pages.dev/">', '<meta property="og:url" content="https://portofolio-8jx.pages.dev/om-meg">', 1)
(root / 'om-meg.html').write_text(s, encoding='utf-8')
print('om-meg.html oppdatert')
