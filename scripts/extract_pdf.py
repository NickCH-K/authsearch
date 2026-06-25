#!/usr/bin/env python3
"""Extract text from a PDF into scratch/<name>.txt. Usage: python3 scripts/extract_pdf.py file.pdf"""
import os
import sys

from pypdf import PdfReader

for f in sys.argv[1:]:
    r = PdfReader(f)
    base = os.path.splitext(os.path.basename(f))[0].replace(" ", "_")
    out = os.path.join(os.path.dirname(__file__), "..", "scratch", base + ".txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w") as o:
        for pg in r.pages:
            o.write(pg.extract_text() or "")
            o.write("\n")
    print(out, len(r.pages), "pages")
