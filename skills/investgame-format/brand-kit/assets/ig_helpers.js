/* InvestGame brand constants + Chart.js defaults for HTML/PDF decks.
 *
 * Refer to colours by name so artifacts stay on-brand and never drift to a
 * hand-picked hex. Two skins share one teal/navy core. See references/charts.md
 * for chart recipes and references/colors.md for the full palette rationale. */

const IG = {
  // shared brand core
  teal: "#61BFB3", tealBright: "#1ECABA", tealDeep: "#00928A",
  blue: "#6189D6", blueDeep: "#2D5BA8", white: "#FFFFFF",

  // Dark Navy skin
  dark: {
    navy: "#0E1F33", navy2: "#142A44",
    teal: "#61BFB3", teal2: "#1ECABA", tealDark: "#00928A",
    blue: "#6189D6", blueDark: "#2D5BA8",
    slate: "#8A95A4", gray: "#8FA1B5",
    light: "#F5F7FA", rule: "#E1E6EC", inkSoft: "#45596F", tintTeal: "#E1F4F1",
  },

  // Warm White skin
  white_skin: {
    bg: "#F4F3EE", bgSoft: "#EEEDE6", card: "#FFFFFF",
    text: "#0B1A2A", textMuted: "#5F6B7A", textSoft: "#8E99A6",
    accent: "#61BFB3", accentDeep: "#3D9B8F", accentSoft: "#E6F4F2",
    warn: "#C07B5A", warnSoft: "#F5E6DD",
    border: "#E0DFD9", borderStrong: "#C7C6C0",
  },

  // Apply chart series in this order. Positive = tealDeep, negative/caution = rust.
  // Never green; never red except the rust caution tone.
  chartColors: ["#61BFB3", "#6189D6", "#00928A", "#2D5BA8", "#8A95A4", "#1ECABA", "#8FA1B5"],
  positive: "#00928A",
  negative: "#C07B5A",
};

/* Chart.js global defaults. Call once after Chart.js loads, before creating
 * charts. Pass dark:true for the Dark Navy skin. Tooltips and hover are ON by
 * default in Chart.js - keep them, the on-screen deck is meant to be explored.
 * IMPORTANT: every Chart.js chart on a slide that is shown/hidden must call
 * chart.resize() when its slide becomes visible (and on beforeprint) or it
 * renders at 0px on first paint / exports blank to PDF. */
function igChartDefaults(Chart, { dark = false } = {}) {
  const skin = dark ? IG.dark : IG.white_skin;
  const muted = dark ? "rgba(255,255,255,0.6)" : skin.textMuted;
  const grid = dark ? "rgba(255,255,255,0.12)" : "rgba(11,26,42,0.08)";
  Chart.defaults.font.family = "Inter, sans-serif";
  Chart.defaults.font.size = 12;
  Chart.defaults.color = muted;
  Chart.defaults.plugins.legend.labels.boxWidth = 12;
  Chart.defaults.plugins.legend.labels.boxHeight = 12;
  // On-brand, readable hover tooltips.
  Chart.defaults.plugins.tooltip.backgroundColor = dark ? "#0E1F33" : "#0B1A2A";
  Chart.defaults.plugins.tooltip.titleColor = "#FFFFFF";
  Chart.defaults.plugins.tooltip.bodyColor = "#FFFFFF";
  Chart.defaults.plugins.tooltip.borderColor = IG.teal;
  Chart.defaults.plugins.tooltip.borderWidth = 1;
  Chart.defaults.plugins.tooltip.padding = 10;
  Chart.defaults.interaction = { mode: "index", intersect: false };
  Chart.defaults.scale.grid.color = grid;
  Chart.defaults.scale.grid.drawTicks = false;
  Chart.defaults.scale.border.display = false;
  return { muted, grid };
}

if (typeof module !== "undefined") module.exports = { IG, igChartDefaults };
