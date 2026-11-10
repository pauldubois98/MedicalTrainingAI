#!/usr/bin/env python3
"""Builds all course materials.

  1. figures/*.svg            (figures.py)
  2. demos/rag_corpus.js      (make_corpus.py, from knowledge_base/*.md)
  3. slides.html              (pandoc + reveal.js)
  4. handouts: workshops/*.md, knowledge_base/*.md  →  .html (+ .pdf with --pdf, via headless Chrome)
  5. with --site: _site/ (what GitHub Pages serves)

Every resource exists in English (name.ext) and French (name-fr.ext): slides-fr.md → slides-fr.html,
figures/*-fr.svg, demos/*-fr.html, demos/rag_corpus-fr.js, workshops/*-fr.md, knowledge_base/*-fr.md,
index-fr.md.

reveal.js is downloaded into vendor/ on the first run.

Usage:  python3 build.py [--pdf] [--site]
Presenting: S = speaker notes, F = full screen, Esc = overview.
"""

import glob
import io
import os
import shutil
import subprocess
import sys
import tarfile
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
REVEAL_VERSION = "5.1.0"
HANDOUTS = ["workshops/*.md", "knowledge_base/*.md"]


def fetch_reveal():
    dest = os.path.join(HERE, "vendor", "reveal.js")
    if os.path.isdir(os.path.join(dest, "dist")):
        return
    url = f"https://github.com/hakimel/reveal.js/archive/refs/tags/{REVEAL_VERSION}.tar.gz"
    print("↓", url)
    data = urllib.request.urlopen(url).read()
    prefix = f"reveal.js-{REVEAL_VERSION}/"
    with tarfile.open(fileobj=io.BytesIO(data)) as tar:
        for m in tar.getmembers():
            rel = m.name[len(prefix):]
            if m.isfile() and rel.split("/")[0] in ("dist", "plugin"):
                out = os.path.join(dest, rel)
                os.makedirs(os.path.dirname(out), exist_ok=True)
                with tar.extractfile(m) as src, open(out, "wb") as f:
                    f.write(src.read())
    print("→ vendor/reveal.js", REVEAL_VERSION)


def lang_of(path):
    return "fr" if path[:-3].endswith("-fr") else "en"


def slides(name):
    with open(os.path.join(HERE, name + ".md"), encoding="utf-8") as f:
        md = f.read()
    subprocess.run(
        ["pandoc", "-f", "markdown", "-t", "revealjs", "-s", "--slide-level=2",
         "-o", os.path.join(HERE, name + ".html"),
         "-V", "revealjs-url=vendor/reveal.js",
         "-V", "theme=white",
         "-V", "width=1280", "-V", "height=720", "-V", "margin=0.04",
         "-V", "transition=fade", "-V", "slideNumber=true", "-V", "hash=true",
         "-V", "center=false",
         "--css", "theme.css"],
        input=md, text=True, check=True, cwd=HERE)
    print(f"→ {name}.html")


def chrome():
    for c in ["google-chrome", "chromium", "chromium-browser"]:
        if shutil.which(c):
            return c
    return None


def handouts(pdf):
    browser = chrome() if pdf else None
    if pdf and not browser:
        print("! no Chrome/Chromium found: PDFs skipped")
    for pattern in HANDOUTS:
        for md in sorted(glob.glob(os.path.join(HERE, pattern))):
            html = md[:-3] + ".html"
            css = os.path.relpath(os.path.join(HERE, "handout.css"), os.path.dirname(md))
            subprocess.run(["pandoc", md, "-s", "-o", html, "--css", css, "--embed-resources",
                            "--metadata", f"lang={lang_of(md)}"], check=True, cwd=os.path.dirname(md))
            print("→", os.path.relpath(html, HERE))
            if browser:
                out = md[:-3] + ".pdf"
                subprocess.run([browser, "--headless", "--disable-gpu", "--no-pdf-header-footer",
                                f"--print-to-pdf={out}", "file://" + html],
                               check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                print("→", os.path.relpath(out, HERE))


SITE_FILES = ["slides.html", "slides-fr.html", "theme.css", "figures", "demos", "vendor/reveal.js/dist",
              "vendor/reveal.js/plugin"]


def site():
    out = os.path.join(HERE, "_site")
    shutil.rmtree(out, ignore_errors=True)
    for item in SITE_FILES:
        src = os.path.join(HERE, item)
        if os.path.isdir(src):
            shutil.copytree(src, os.path.join(out, item))
        else:
            os.makedirs(os.path.dirname(os.path.join(out, item)), exist_ok=True)
            shutil.copy2(src, os.path.join(out, item))
    for pattern in HANDOUTS:
        for md in glob.glob(os.path.join(HERE, pattern)):
            for ext in (".html", ".pdf"):
                f = md[:-3] + ext
                if os.path.exists(f):
                    dst = os.path.join(out, os.path.relpath(f, HERE))
                    os.makedirs(os.path.dirname(dst), exist_ok=True)
                    shutil.copy2(f, dst)
    for name in ("index", "index-fr"):
        subprocess.run(["pandoc", name + ".md", "-s", "-o", os.path.join(out, name + ".html"),
                        "--css", "handout.css", "--embed-resources", "--metadata", f"lang={lang_of(name + '.md')}"],
                       check=True, cwd=HERE)
    print("→ _site/")


def main():
    fetch_reveal()
    subprocess.run([sys.executable, os.path.join(HERE, "figures.py")], check=True)
    subprocess.run([sys.executable, os.path.join(HERE, "make_corpus.py")], check=True)
    slides("slides")
    slides("slides-fr")
    handouts(pdf="--pdf" in sys.argv)
    if "--site" in sys.argv:
        site()


if __name__ == "__main__":
    main()
