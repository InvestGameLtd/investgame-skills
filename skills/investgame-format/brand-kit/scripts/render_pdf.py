#!/usr/bin/env python3
"""Render an InvestGame HTML deck to PDF at the exact slide canvas.

The templates set `@page { size: <W>px <H>px; margin: 0 }` and a print
stylesheet, so the renderer just needs to honour CSS page size. Two backends are
tried in order: Playwright (best fidelity, `preferCSSPageSize`), then headless
Chrome/Chromium (`--print-to-pdf`).

Usage:
    python render_pdf.py input.html [output.pdf]

Notes:
- Charts drawn with Chart.js need a moment to paint; a short wait is built in.
- If neither backend is installed: `pip install playwright && playwright install
  chromium`, or install Google Chrome / Chromium.
"""

import shutil
import subprocess
import sys
from pathlib import Path


def render_with_playwright(html: Path, pdf: Path) -> bool:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        return False
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(html.resolve().as_uri())
        page.emulate_media(media="print")
        page.wait_for_timeout(900)  # let Chart.js finish painting
        page.pdf(path=str(pdf), prefer_css_page_size=True, print_background=True)
        browser.close()
    return True


def render_with_chrome(html: Path, pdf: Path) -> bool:
    candidates = [
        "google-chrome",
        "google-chrome-stable",
        "chromium",
        "chromium-browser",
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Chromium.app/Contents/MacOS/Chromium",
    ]
    chrome = next((c for c in candidates if shutil.which(c) or Path(c).exists()), None)
    if not chrome:
        return False
    subprocess.run(
        [
            chrome,
            "--headless=new",
            "--disable-gpu",
            "--no-pdf-header-footer",
            f"--print-to-pdf={pdf}",
            "--virtual-time-budget=2000",
            html.resolve().as_uri(),
        ],
        check=True,
    )
    return True


def main():
    if len(sys.argv) < 2:
        print("Usage: python render_pdf.py input.html [output.pdf]")
        sys.exit(1)
    html = Path(sys.argv[1])
    pdf = Path(sys.argv[2]) if len(sys.argv) > 2 else html.with_suffix(".pdf")
    if render_with_playwright(html, pdf) or render_with_chrome(html, pdf):
        print(f"Rendered {pdf}")
        return
    print(
        "No renderer found. Install Playwright (pip install playwright && "
        "playwright install chromium) or Google Chrome / Chromium."
    )
    sys.exit(1)


if __name__ == "__main__":
    main()
