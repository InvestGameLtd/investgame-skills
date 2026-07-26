"""InvestGame brand constants for programmatic builds (PowerPoint / Excel).

Import these instead of re-typing hex codes - referring to colours by name is
how you keep a deck on-brand and avoid silent drift. Hex values are stored
WITHOUT the leading '#'; python-pptx wants RGBColor(0x..), pptxgenjs wants the
bare 6-char string.

Two skins share one teal/navy core:
  IG_DARK   - Dark Navy deck   (slide 13.33in x 7.5in / 16:9)
  IG_WHITE  - Warm White deck   (slide 13.33in x 7.5in / 16:9)
Both carry the InvestGame logo. See references/pptx-and-pdf.md for the
copy-the-template workflow.
"""

# --- Shared brand core --------------------------------------------------------
IG = {
    "teal": "61BFB3",  # PRIMARY brand teal - both skins
    "teal_bright": "1ECABA",
    "teal_deep": "00928A",
    "blue": "6189D6",
    "blue_deep": "2D5BA8",
    "white": "FFFFFF",
}

# --- Dark Navy skin -----------------------------------------------------------
IG_DARK = {
    "navy": "0E1F33",  # primary dark bg + body text on light
    "navy_2": "142A44",
    "teal": "61BFB3",
    "teal_2": "1ECABA",  # big numerals on dark
    "teal_dark": "00928A",  # chips, emphasis, positive delta
    "blue": "6189D6",
    "blue_dark": "2D5BA8",
    "slate": "8A95A4",
    "gray": "8FA1B5",  # labels, captions, footer
    "light": "F5F7FA",
    "rule": "E1E6EC",
    "ink_soft": "45596F",  # secondary body text on light
    "tint_teal": "E1F4F1",  # teal-tinted row / highlight
}

# --- Warm White skin ----------------------------------------------------------
IG_WHITE = {
    "bg": "F4F3EE",  # warm off-white page
    "bg_soft": "EEEDE6",
    "card": "FFFFFF",
    "text": "0B1A2A",  # warm navy body text
    "text_muted": "5F6B7A",
    "text_soft": "8E99A6",
    "accent": "61BFB3",  # primary teal
    "accent_deep": "3D9B8F",  # kickers, footnote marks
    "accent_soft": "E6F4F2",  # teal-tinted callout / row
    "warn": "C07B5A",  # rust caution / negative
    "warn_soft": "F5E6DD",
    "border": "E0DFD9",
    "border_strong": "C7C6C0",
}

# --- Chart series order (apply 1..n in this sequence) -------------------------
# Positive delta = teal_deep. Negative / caution = warn (rust). Never green;
# never red except the rust caution tone. See references/charts.md.
CHART_COLORS = ["61BFB3", "6189D6", "00928A", "2D5BA8", "8A95A4", "1ECABA", "8FA1B5"]

POSITIVE = "00928A"  # teal-deep - "up"
NEGATIVE = "C07B5A"  # rust - "down" / caution

# --- Typography ---------------------------------------------------------------
# Dark Navy skin:   Helvetica Neue (Arial fallback) throughout.
# Warm White skin:  Space Grotesk -> headings/cover; Inter -> body;
#                   JetBrains Mono -> numeric columns. PowerPoint fallbacks:
#                   Space Grotesk -> Arial Bold; Inter -> Arial / Aptos;
#                   JetBrains Mono -> Consolas. See references/typography.md.
FONTS_DARK = {"display": "Helvetica Neue", "body": "Helvetica Neue", "fallback": "Arial"}
FONTS_WHITE = {"display": "Space Grotesk", "body": "Inter", "mono": "JetBrains Mono"}


def hex_to_rgbcolor(hex6):
    """'61BFB3' -> RGBColor for python-pptx. Usage:
    from pptx.dml.color import RGBColor
    RGBColor(*hex_to_rgbcolor(IG['teal']))
    """
    return tuple(int(hex6[i : i + 2], 16) for i in (0, 2, 4))
