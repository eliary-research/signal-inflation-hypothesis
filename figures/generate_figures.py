#!/usr/bin/env python3
"""
EN6: The Signal Inflation Hypothesis — Figure Generation
Generates all figures for the paper from data/ CSV files.

Usage: python generate_figures.py
Output: PNG files in the same directory
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path

# --- Config ---
DATA_DIR = Path(__file__).parent.parent / "data"
FIG_DIR = Path(__file__).parent
plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 11,
    'axes.titlesize': 13,
    'axes.labelsize': 12,
    'figure.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.2,
})

# Phase colors
PHASE_COLORS = {
    'genuine': '#2ecc71',
    'inflated': '#f39c12',
    'toxic': '#e74c3c',
    'deprecated': '#95a5a6',
}


def fig1_devaluation_cycle():
    """Figure 1: The Four-Phase Signal Devaluation Cycle (conceptual diagram)."""
    fig, ax = plt.subplots(figsize=(10, 5))

    # X: time, Y: signal value
    x = np.linspace(0, 10, 500)

    # Signal value curve: starts high, plateaus, declines, crashes, flatlines
    y = np.piecewise(x, [
        x < 2,                    # Phase 1: Genuine (high, slight growth)
        (x >= 2) & (x < 4.5),    # Phase 2: Inflated (gradual decline)
        (x >= 4.5) & (x < 7),    # Phase 3: Toxic (steep decline, goes negative)
        x >= 7                     # Phase 4: Deprecated (flatline near zero)
    ], [
        lambda x: 0.85 + 0.05 * x,
        lambda x: 0.95 - 0.12 * (x - 2),
        lambda x: 0.65 - 0.3 * (x - 4.5),
        lambda x: -0.1 + 0.02 * np.sin(x)
    ])

    # Signal production cost curve (dashed)
    cost = np.piecewise(x, [
        x < 2,
        (x >= 2) & (x < 5),
        (x >= 5) & (x < 7),
        x >= 7
    ], [
        lambda x: 0.7 - 0.05 * x,
        lambda x: 0.6 - 0.15 * (x - 2),
        lambda x: 0.15 - 0.05 * (x - 5),
        lambda x: 0.05
    ])

    # Plot
    ax.plot(x, y, 'k-', linewidth=2.5, label='Signal Informational Value')
    ax.plot(x, cost, 'k--', linewidth=1.5, alpha=0.6, label='Signal Production Cost')

    # Phase backgrounds
    phases = [
        (0, 2, 'genuine', 'Phase 1\nGenuine'),
        (2, 4.5, 'inflated', 'Phase 2\nInflated'),
        (4.5, 7, 'toxic', 'Phase 3\nToxic'),
        (7, 10, 'deprecated', 'Phase 4\nDeprecated'),
    ]
    for x0, x1, phase, label in phases:
        ax.axvspan(x0, x1, alpha=0.15, color=PHASE_COLORS[phase])
        ax.text((x0 + x1) / 2, 1.05, label, ha='center', va='bottom',
                fontsize=10, fontweight='bold', color=PHASE_COLORS[phase])

    # Zero line
    ax.axhline(y=0, color='gray', linewidth=0.5, linestyle='-')

    # Annotations
    ax.annotate('Habituation\nReciprocal norms\nAlgorithmic optimization',
                xy=(3.2, 0.5), fontsize=8, ha='center', alpha=0.7,
                style='italic')
    ax.annotate('Social comparison\nBot manipulation\nPerformative behavior',
                xy=(5.8, 0.0), fontsize=8, ha='center', alpha=0.7,
                style='italic')
    ax.annotate('Counts hidden\nNew signals emerge',
                xy=(8.5, -0.05), fontsize=8, ha='center', alpha=0.7,
                style='italic')

    ax.set_xlim(0, 10)
    ax.set_ylim(-0.3, 1.2)
    ax.set_xlabel('Platform Maturity →')
    ax.set_ylabel('Signal Value / Cost')
    ax.set_title('Figure 1. The Four-Phase Signal Devaluation Cycle')
    ax.legend(loc='upper right', framealpha=0.9)
    ax.set_xticks([])  # Conceptual, no numeric x-axis
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    fig.savefig(FIG_DIR / 'devaluation_cycle.png')
    plt.close()
    print("✓ devaluation_cycle.png")


def fig2_engagement_decline():
    """Figure 2: Instagram Engagement Rate & Facebook Organic Reach Decline."""
    ig = pd.read_csv(DATA_DIR / "instagram_engagement_rate.csv", comment='#')
    fb = pd.read_csv(DATA_DIR / "facebook_organic_reach.csv", comment='#')

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # --- Instagram ---
    colors_ig = [PHASE_COLORS.get(p.split('_')[0], '#333') for p in ig['phase']]
    ax1.plot(ig['year'], ig['engagement_rate_pct'], 'o-', color='#E1306C',
             linewidth=2, markersize=6, zorder=5)

    # Phase backgrounds
    ax1.axvspan(2013, 2015, alpha=0.1, color=PHASE_COLORS['genuine'])
    ax1.axvspan(2015, 2017.5, alpha=0.1, color=PHASE_COLORS['inflated'])
    ax1.axvspan(2017.5, 2020.5, alpha=0.1, color=PHASE_COLORS['toxic'])
    ax1.axvspan(2020.5, 2025, alpha=0.1, color=PHASE_COLORS['deprecated'])

    # Annotations
    ax1.annotate('Stories\nlaunched', xy=(2016, 1.10), xytext=(2016.5, 2.5),
                fontsize=8, ha='center',
                arrowprops=dict(arrowstyle='->', color='gray'))
    ax1.annotate('Like hiding\ntest', xy=(2019, 0.60), xytext=(2019.5, 1.5),
                fontsize=8, ha='center',
                arrowprops=dict(arrowstyle='->', color='gray'))

    ax1.set_xlabel('Year')
    ax1.set_ylabel('Engagement Rate (%)')
    ax1.set_title('(a) Instagram Average Engagement Rate')
    ax1.set_xlim(2012.5, 2025)
    ax1.set_ylim(0, 5)
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    ax1.grid(axis='y', alpha=0.3)

    # --- Facebook ---
    ax2.plot(fb['year'] + fb['month'] / 12, fb['organic_reach_pct'], 's-',
             color='#4267B2', linewidth=2, markersize=5, zorder=5)

    ax2.axvspan(2012, 2013.5, alpha=0.1, color=PHASE_COLORS['genuine'])
    ax2.axvspan(2013.5, 2015.5, alpha=0.1, color=PHASE_COLORS['inflated'])
    ax2.axvspan(2015.5, 2018, alpha=0.1, color=PHASE_COLORS['toxic'])
    ax2.axvspan(2018, 2024, alpha=0.1, color=PHASE_COLORS['deprecated'])

    ax2.annotate("Social@Ogilvy\n'Facebook Zero'", xy=(2014.17, 6.15),
                xytext=(2015.5, 10), fontsize=8, ha='center',
                arrowprops=dict(arrowstyle='->', color='gray'))

    ax2.set_xlabel('Year')
    ax2.set_ylabel('Organic Reach (%)')
    ax2.set_title('(b) Facebook Page Organic Reach')
    ax2.set_xlim(2011.5, 2024)
    ax2.set_ylim(0, 18)
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    ax2.grid(axis='y', alpha=0.3)

    fig.suptitle('Figure 2. Engagement Signal Devaluation: Instagram and Facebook',
                 fontsize=13, fontweight='bold', y=1.02)
    fig.tight_layout()
    fig.savefig(FIG_DIR / 'engagement_decline.png')
    plt.close()
    print("✓ engagement_decline.png")


def fig3_signal_cost_spectrum():
    """Figure 3: The Signal Cost Spectrum."""
    fig, ax = plt.subplots(figsize=(12, 4))

    signals = [
        ('View', 0.5, '#bdc3c7', 'Passive\n(scrolled past)'),
        ('Like', 1.0, '#e74c3c', 'Tap\n(0.5 sec)'),
        ('Comment', 2.0, '#e67e22', 'Compose text\n(~10 sec)'),
        ('Story DM\nReply', 3.0, '#f1c40f', 'Compose +\ninitiate\n(~15 sec)'),
        ('Ask', 4.0, '#2ecc71', 'Formulate\nquestion +\ndirect\n(~30 sec)'),
        ('Keep', 5.0, '#3498db', 'Identity\nclaim\n(reputational\nrisk)'),
    ]

    for label, cost, color, desc in signals:
        # Circle size proportional to informational value
        size = cost * 350
        ax.scatter(cost, 0.5, s=size, c=color, alpha=0.8, edgecolors='white',
                  linewidth=2, zorder=5)
        ax.text(cost, 0.85, label, ha='center', va='bottom', fontsize=11,
               fontweight='bold')
        ax.text(cost, 0.15, desc, ha='center', va='top', fontsize=8,
               alpha=0.7)

    # Arrow
    ax.annotate('', xy=(5.5, 0.5), xytext=(0.0, 0.5),
                arrowprops=dict(arrowstyle='->', lw=1.5, color='gray'))

    # Generation labels
    gen_spans = [
        (0.3, 1.5, 'Gen 1\n(2004-12)', '#e74c3c'),
        (1.5, 2.5, 'Gen 2\n(2012-16)', '#e67e22'),
        (2.5, 3.5, 'Gen 3\n(2016-now)', '#f1c40f'),
        (3.5, 5.5, 'Gen 4\n(predicted)', '#3498db'),
    ]
    for x0, x1, label, color in gen_spans:
        ax.axvspan(x0, x1, ymin=0, ymax=0.08, alpha=0.4, color=color)
        ax.text((x0 + x1) / 2, -0.15, label, ha='center', va='top',
               fontsize=8, color=color, fontweight='bold')

    ax.set_xlim(-0.2, 5.8)
    ax.set_ylim(-0.3, 1.2)
    ax.set_xlabel('Signal Production Cost →', fontsize=12)
    ax.set_title('Figure 3. The Signal Cost Spectrum: Engagement Signal Evolution',
                fontsize=13, fontweight='bold')
    ax.set_yticks([])
    ax.set_xticks([])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)

    fig.tight_layout()
    fig.savefig(FIG_DIR / 'signal_cost_spectrum.png')
    plt.close()
    print("✓ signal_cost_spectrum.png")


def fig4_lead_lag():
    """Figure 4: Signal Devaluation Precedes Platform Senescence."""
    fig, ax = plt.subplots(figsize=(10, 5))

    # Facebook data
    years = np.arange(2012, 2025)

    # Engagement signal (organic reach, normalized 0-1)
    fb_reach = [16, 12, 6.15, 2.6, 2.0, 1.6, 1.3, 1.1, 1.0, 0.9, 0.8, 0.7, 0.7]
    fb_reach_norm = np.array(fb_reach) / max(fb_reach)

    # Platform health (US&CA DAU growth rate, estimated)
    fb_dau_growth = [15, 12, 10, 8, 6, 4, 2, 1, 0.5, 0, -0.5, -1, -1]
    fb_dau_norm = (np.array(fb_dau_growth) - min(fb_dau_growth)) / (max(fb_dau_growth) - min(fb_dau_growth))

    ax.plot(years, fb_reach_norm, 'o-', color='#e74c3c', linewidth=2.5,
            markersize=6, label='Signal Value (Organic Reach)', zorder=5)
    ax.plot(years, fb_dau_norm, 's--', color='#3498db', linewidth=2.5,
            markersize=6, label='Platform Health (US DAU Growth)', zorder=5)

    # Highlight lead-lag
    ax.annotate('Signal inflection\n(~2013)',
                xy=(2013, fb_reach_norm[1]), xytext=(2014.5, 0.85),
                fontsize=9, ha='center',
                arrowprops=dict(arrowstyle='->', color='#e74c3c', lw=1.5))
    ax.annotate('DAU inflection\n(~2017)',
                xy=(2017, fb_dau_norm[5]), xytext=(2018.5, 0.55),
                fontsize=9, ha='center',
                arrowprops=dict(arrowstyle='->', color='#3498db', lw=1.5))

    # Lead-lag arrow
    ax.annotate('', xy=(2017, 0.12), xytext=(2013, 0.12),
                arrowprops=dict(arrowstyle='<->', color='gray', lw=2))
    ax.text(2015, 0.05, '~3-4 year lead', ha='center', fontsize=10,
           color='gray', fontweight='bold')

    ax.set_xlabel('Year')
    ax.set_ylabel('Normalized Value (0-1)')
    ax.set_title('Figure 4. Signal Devaluation Precedes Platform Senescence (Facebook)',
                fontsize=12, fontweight='bold')
    ax.legend(loc='upper right', framealpha=0.9)
    ax.set_xlim(2011.5, 2025)
    ax.set_ylim(-0.05, 1.1)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(axis='y', alpha=0.3)

    fig.tight_layout()
    fig.savefig(FIG_DIR / 'lead_lag_analysis.png')
    plt.close()
    print("✓ lead_lag_analysis.png")


def fig5_deprecation_timeline():
    """Figure 5: Timeline of Engagement Signal Deprecation Events."""
    events = pd.read_csv(DATA_DIR / "like_hiding_timeline.csv", comment='#')
    events['date'] = pd.to_datetime(events['date'])

    fig, ax = plt.subplots(figsize=(14, 4))

    type_colors = {
        'design_choice': '#2ecc71',
        'new_signal': '#3498db',
        'deprecation_test': '#f39c12',
        'deprecation_global': '#e74c3c',
        'signal_addition': '#9b59b6',
    }

    y_positions = {}
    platforms = events['platform'].unique()
    for i, p in enumerate(platforms):
        y_positions[p] = i * 0.8

    for _, row in events.iterrows():
        y = y_positions[row['platform']]
        color = type_colors.get(row['type'], '#333')
        ax.scatter(row['date'], y, s=120, c=color, edgecolors='white',
                  linewidth=1.5, zorder=5)

    # Platform labels
    for platform, y in y_positions.items():
        ax.text(pd.Timestamp('2011-01-01'), y, platform, ha='right', va='center',
               fontsize=9, fontweight='bold')

    # Legend
    handles = [mpatches.Patch(color=c, label=l.replace('_', ' ').title())
               for l, c in type_colors.items()]
    ax.legend(handles=handles, loc='upper left', fontsize=8, ncol=3)

    ax.set_xlim(pd.Timestamp('2010-06-01'), pd.Timestamp('2024-06-01'))
    ax.set_ylim(-0.5, max(y_positions.values()) + 0.5)
    ax.set_yticks([])
    ax.set_title('Figure 5. Timeline of Engagement Signal Deprecation Events (2011-2023)',
                fontsize=12, fontweight='bold')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.grid(axis='x', alpha=0.3)

    fig.tight_layout()
    fig.savefig(FIG_DIR / 'deprecation_timeline.png')
    plt.close()
    print("✓ deprecation_timeline.png")


if __name__ == '__main__':
    print("EN6: Generating figures...")
    print(f"Data dir: {DATA_DIR}")
    print(f"Figure dir: {FIG_DIR}")
    print()
    fig1_devaluation_cycle()
    fig2_engagement_decline()
    fig3_signal_cost_spectrum()
    fig4_lead_lag()
    fig5_deprecation_timeline()
    print()
    print("All figures generated.")
