# The Signal Inflation Hypothesis

**Why Engagement Signals Lose Value and What Replaces Them**

A working paper on the structural economics of social-media engagement signals — applying Spence's (1973) signaling theory and the monetary-inflation analogy to explain the lifecycle of the Facebook "like" button.

> **Author** · Chanmin Kim · Eliary Inc. · `chanmin@eliary.com`
> **Status** · Working paper, v0.2-preprint (May 2026)
> **License** · Paper + data: CC BY 4.0 · Code: MIT

---

## Abstract

The Facebook "like" button, introduced in 2009, became the universal unit of social media engagement within two years. Sixteen years later, that unit is in collapse. Instagram's average engagement rate fell from 1.22% to 0.36% between 2015 and 2024; Facebook's organic reach dropped from 16% to under 1.5% between 2012 and 2023. In 2019, Instagram began *hiding* like counts — deliberately obscuring the metric it had spent a decade optimizing. Standard accounts invoke algorithmic changes, content saturation, or platform maturity. These describe correlates, not mechanisms. We introduce the **Signal Inflation Hypothesis**: engagement signals follow a devaluation cycle isomorphic to monetary inflation. Drawing on Spence's (1973) signaling theory, we show that as a signal's production cost approaches zero — through habituation, reciprocal norms, algorithmic optimization, and automated manipulation — its informational value collapses. We formalize a four-phase Signal Devaluation Cycle (genuine → inflated → toxic → deprecated), trace the like through all four phases, and demonstrate that signal devaluation precedes platform-level stagnation by 3–5 years across Facebook, Instagram, and Snapchat. We propose a Signal Cost Spectrum mapping engagement signals by production cost, and predict that the next dominant signal will operate at the identity level.

## Key contributions

1. **Signal Inflation** as a formal concept — the structural isomorphism between monetary inflation and engagement-signal devaluation, including a Gresham's-Law analogue for social signals.
2. **Four-Phase Signal Devaluation Cycle** (genuine → inflated → toxic → deprecated) — a general framework applied here to the like button.
3. **Signal Cost Spectrum** — engagement signals mapped by production cost, with a predictive claim about the next generation (identity-level signals).
4. **Lead-lag evidence** — signal devaluation precedes platform-level stagnation by 3–5 years across Facebook, Instagram, and Snapchat.

## Repository contents

```
.
├── paper.md            # paper source (markdown)
├── paper.pdf           # built artifact
├── outline.md          # paper outline + hypothesis structure
├── references.md       # references with annotations
├── data/               # 4 CSVs — Instagram engagement, FB organic reach, like-hiding timeline, platform signal design
├── figures/            # 5 figures + reproducible generate_figures.py
├── CITATION.cff        # citation metadata (GitHub renders → "Cite this repository")
├── LICENSE             # CC BY 4.0 (paper + data) · MIT (code)
└── .zenodo.json        # Zenodo deposit metadata (auto-DOI on release)
```

## Reproducing figures

```bash
cd figures/
python3 generate_figures.py
# Regenerates 5 PNGs from data/*.csv
```

Requires `matplotlib`, `pandas`. No private data dependencies; all sources are public (Rival IQ, Socialinsider, Meta SEC filings, Snap SEC filings, Pew Research, Instagram blog, YouTube blog, academic studies — see `references.md` for source mapping).

## Citation

If you use this work, please cite:

```bibtex
@article{kim2026signalinflation,
  title         = {The Signal Inflation Hypothesis: Why Engagement Signals Lose Value and What Replaces Them},
  author        = {Kim, Chanmin},
  year          = {2026},
  doi           = {10.5281/zenodo.XXXXXXX},
  url           = {https://github.com/eliary-research/signal-inflation-hypothesis},
  note          = {Working paper}
}
```

(GitHub auto-renders citation from `CITATION.cff`; click "Cite this repository" in the sidebar.)

## Related work

This paper is part of a series on social-media signal economics:

- **EN1** *Social Media Senescence* — macro-level platform aging mechanisms; provides the lifecycle frame this paper supplies a micro-mechanism for.
- **EN5** *Signal Cost Theory of AI/Human Interaction* — applies Spence's framework to AI-mediated social signals (preregistered).
- **L1** *AI Trust Funnel* (in preparation) — empirical paper on user trust trajectories with AI-mediated identity signals.

## Disclosures

The author is founder of Eliary Inc., which operates Currot — a product referenced in §5.3 and §7.4 as instantiating identity-level signals. This is a research paper, not a product paper; the framework is general and the specific predictions about identity-level signals are presented as falsifiable hypotheses for future empirical work.

## Contributing

This is a single-author working paper. Issues and discussion welcome via GitHub Issues. Substantive corrections will be acknowledged in subsequent revisions.

## License

- Paper text + data: [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)
- Code (figure generation, analysis scripts): [MIT License](https://opensource.org/licenses/MIT)

See `LICENSE` for full text.
