# EN6: The Signal Inflation Hypothesis
## Why Engagement Signals Lose Value and What Replaces Them

> Status: Outline v0.1 (2026-04-10)
> Target: ICWSM 2027 / arXiv pre-print

---

## Abstract (Draft)

The "like" button, introduced by Facebook in 2009, became the universal unit of social media engagement. Yet engagement rates have collapsed across every major platform — Instagram from 1.22% to 0.36%, Facebook organic reach from 16% to under 1.5%. We propose the **Signal Inflation Hypothesis**: engagement signals follow a predictable devaluation cycle analogous to monetary inflation. Drawing on Spence's (1973) signaling theory, we argue that as the production cost of a signal approaches zero (through habituation, reciprocal norms, algorithmic optimization, and bot manipulation), its informational value collapses. We identify a four-phase devaluation cycle — *genuine, inflated, toxic, deprecated* — and show that Instagram Stories, Snapchat's ephemeral messaging, and BeReal's design each represent market responses that restore signal cost through structurally different mechanisms. Using publicly available engagement data from 2012–2025, we demonstrate that signal devaluation precedes and predicts platform-level senescence (declining DAU/MAU ratios). We conclude with a **Signal Cost Spectrum** framework that predicts the next generation of engagement signals will operate at the identity level — not "I saw this" but "this changed who I am" — and discuss design implications for platforms seeking to escape the inflation trap.

---

## 1. Introduction

### 1.1 The Universal Decline

Every major social media platform has experienced systematic engagement decline:
- Instagram: 1.22% → 0.36% average engagement rate (2015–2025)
- Facebook: 16% → <1.5% organic reach per post (2012–2023)
- Twitter: Average impressions per tweet declining year-over-year since 2018
- YouTube: Comment rate per view declining despite view count growth

The standard explanations — algorithmic changes, content saturation, platform maturity — describe *correlates* but not *mechanisms*. Why do platforms systematically devalue their own engagement signals?

### 1.2 The Puzzle

Instagram's decision to hide like counts (2019 experiment, 2021 global rollout) is a paradox: why would a platform deliberately obscure the metric that defined its product? YouTube's removal of public dislike counts (2021) is similarly counterintuitive. These are not isolated decisions — they represent a pattern of **signal deprecation** by the very platforms that introduced and optimized for these signals.

### 1.3 Our Contribution

We propose that engagement signal devaluation is not a bug but a predictable consequence of signal economics. Using Spence's (1973) signaling theory as our theoretical backbone, we develop the **Signal Inflation Hypothesis**: engagement signals follow a devaluation cycle isomorphic to monetary inflation. We present:

1. A **four-phase devaluation cycle** (genuine → inflated → toxic → deprecated)
2. **Empirical evidence** from 10+ years of cross-platform engagement data
3. A **Signal Cost Spectrum** framework predicting the evolution of engagement signals
4. **Design implications** for platforms seeking to escape the inflation trap

### 1.4 Connection to Prior Work

This paper provides the micro-level mechanism for the macro-level senescence described in [EN1: Social Media Senescence]. While EN1 identifies *that* platforms age, EN6 explains *how* they age at the feature level — through the devaluation of their core engagement signals. EN6 also extends [EN5: Signal Cost Theory] from the AI/human interaction context to the engagement signal context.

---

## 2. Theory: Signal Inflation

### 2.1 Spence Signaling Theory (Foundation)

Spence (1973): A signal is valuable *because it is costly to produce*. In labor markets, education signals ability because education is costly. If education became free and effortless, it would lose signaling value.

Application to social media:
- A "like" is a signal of attention/approval
- Its value depends on the cost of producing it
- When production cost → 0, signal value → 0

### 2.2 The Inflation Mechanism

Monetary inflation: money supply ↑ → purchasing power ↓ → hyperinflation → new currency.
Signal inflation: signal supply ↑ → informational value ↓ → toxification → new signal.

The parallel is structural, not metaphorical:

| Monetary Inflation | Signal Inflation |
|---|---|
| Central bank prints money | Platform optimizes for engagement (more likes per session) |
| Purchasing power declines | Each like means less ("everyone likes everything") |
| Inflation expectations form | Users expect likes; absence = negative signal |
| Hyperinflation → currency collapse | Signal toxification → mental health harm → platform deprecation |
| New currency introduced | New engagement signal introduced (Stories DM, ✦ Keep) |

### 2.3 Gresham's Law of Social Signals

"Bad money drives out good money" (Gresham's Law):
When two forms of money circulate, the overvalued (debased) one drives out the undervalued (genuine) one.

Applied to likes:
- Genuine likes (thoughtful engagement) and inflated likes (habitual, bot, reciprocal) circulate on the same platform
- Recipients cannot distinguish genuine from inflated
- Inflated likes drive out the motivation for genuine engagement
- Users who want genuine signals migrate to new channels (DMs, Stories)

### 2.4 The Four-Phase Devaluation Cycle

We propose that all engagement signals pass through four phases:

**Phase 1: Genuine (Signal Value High)**
- Signal is new and costly to produce
- Users make conscious decisions to engage
- Recipient accurately infers sender's attention/approval
- Example: Early Facebook likes (2009–2013)

**Phase 2: Inflated (Signal Value Declining)**
- Production cost decreases through:
  - Habituation (liking becomes muscle memory)
  - Reciprocal norms ("I liked yours, you like mine")
  - Algorithmic optimization (platform nudges more likes per session)
  - Content designed to extract likes (engagement bait)
- Signal-to-noise ratio deteriorates
- Example: Instagram peak like era (2013–2016)

**Phase 3: Toxic (Signal Value Negative)**
- Signal becomes a source of harm:
  - Social comparison (like-count anxiety)
  - Performative behavior (creating content for likes, not expression)
  - Bot/fake engagement (signal pollution)
  - Platform manipulation (suppressing organic reach to sell paid reach)
- The signal's presence is worse than its absence
- Example: Instagram like-count anxiety era (2016–2019)

**Phase 4: Deprecated (Signal Removed or Hidden)**
- Platform acknowledges signal toxification
- Like counts hidden (Instagram 2019/2021), dislike counts hidden (YouTube 2021)
- New signals emerge to fill the vacuum
- Example: Instagram Stories DMs, Close Friends (2019–present)

---

## 3. Historical Analysis: The Like Economy

### 3.1 Phase 1 — Genuine (2009–2013)

- Facebook introduces "Like" button (Feb 2009)
- Initially: conscious endorsement, ~2% of sessions produce a like
- Organic reach of posts: ~16% of followers (2012)
- Signal value high: receiving a like meant genuine attention

### 3.2 Phase 2 — Inflated (2013–2016)

- Facebook's algorithmic feed optimizes for engagement (2013 News Feed redesign)
- Instagram engagement rate peaks at ~1.22% (2015) — already declining from organic era
- "Like for like" (L4L) culture emerges on Instagram
- Engagement bait proliferates ("double tap if you agree!")
- Organic reach begins decline: 16% → 6% (2013–2014)

Key data points:
- Facebook organic reach: 16% (2012) → 6% (2014) → 2% (2016)
- Instagram avg engagement rate: ~4.2% (2013) → 1.22% (2015)
- Bot-generated likes: estimated 8-12% of total interactions (2016)

### 3.3 Phase 3 — Toxic (2016–2019)

- Instagram engagement rate continues decline: 1.22% → 0.7%
- Research links like-count visibility to:
  - Social comparison (Vogel et al., 2014; Appel et al., 2016)
  - Reduced self-esteem (Hawi & Samaha, 2017)
  - Performative authenticity (Duffy & Hund, 2015)
- UK RSPH report "Status of Mind" (2017): Instagram ranked worst for mental health
- Internal Facebook research (leaked 2021): "We make body image issues worse for 1 in 3 teen girls"

The signal is now harmful:
- Receiving few likes → feeling unpopular → stop posting
- Receiving many likes → anxiety about maintaining → performative behavior
- Neither outcome is healthy → signal has become toxic

### 3.4 Phase 4 — Deprecated (2019–Present)

- Instagram hides like counts (test: July 2019, global: May 2021)
- Adam Mosseri: "We want people to worry less about how many likes they get"
- YouTube hides public dislike counts (Nov 2021)
- Twitter/X: likes still visible → continued toxicity (no deprecation yet)

Simultaneously, new signals emerge:
- Instagram Stories DM reply (2016–present): higher-cost signal
- Close Friends (2018): audience restriction → signal value restoration
- BeReal (2020): no likes at all → radical deprecation

---

## 4. Stories as Signal Cost Restoration

### 4.1 The Market Response Hypothesis

Stories did not emerge as a "new feature." Stories emerged because the like economy collapsed, and both platforms and users needed a new signal with restored value.

Evidence:
- Snapchat's original design (2011) had NO likes — by design, not oversight
- Instagram Stories launch (Aug 2016) coincides with peak like toxification
- Stories' key engagement signal is DM reply, which has structurally higher production cost:

| Signal | Production Cost | Informational Value |
|---|---|---|
| Like (tap) | ~0.5 seconds, no cognitive effort | "I scrolled past this" |
| DM reply to Story | ~15 seconds, must compose message | "I want to talk to you about this" |
| Close Friends Story | Same as DM reply + audience selection | "I trust you with this" |

### 4.2 Three Mechanisms of Cost Restoration

**Mechanism 1: Production Cost Increase**
- DM reply requires message composition (vs. single tap)
- Higher cognitive effort → higher signal value

**Mechanism 2: Audience Restriction**
- Close Friends limits recipients → each view is from a trusted person
- Smaller audience → each interaction carries more weight

**Mechanism 3: Failure Cost Reduction**
- 24-hour expiration → low stakes for content creation
- This does NOT reduce signal cost — it reduces content creation barrier
- Critical distinction: Stories lower the barrier to SHARE while maintaining the cost to ENGAGE

### 4.3 The Incompleteness of Stories

Stories restored signal value but introduced a new problem: **nothing accumulates.**

- Content disappears in 24 hours
- Conversations are ephemeral
- No identity is built
- Every day starts from zero

This creates what we call the **Ephemeral Treadmill**: the constant need to produce new content to maintain social presence, with no compounding return.

---

## 5. Hypotheses and Evidence

### H1: Signal Devaluation Cycle

**Statement**: Engagement signals follow a predictable 4-phase devaluation cycle (genuine → inflated → toxic → deprecated).

**Evidence approach**:
- Instagram engagement rate time series (2013–2025): identify structural breaks corresponding to phase transitions
- Facebook organic reach time series (2012–2023): same analysis
- Qualitative markers: reciprocal liking norms, bot prevalence, platform policy changes

**Expected finding**: Phase transitions are identifiable in the data, with 2-3 year phase durations.

### H2: Cost-Restoring Replacement

**Statement**: Features that replace devalued signals have structurally higher production cost.

**Evidence approach**:
- Compare production cost (measured by time, cognitive effort) across signal types
- Like (0.5s, no cognition) < Comment (10s, composition) < DM Reply (15s, composition + intent) < ✦ Keep (identity claim)
- Cross-platform comparison: platforms with higher-cost signals show higher engagement quality

**Expected finding**: Clear monotonic relationship between signal production cost and engagement quality.

### H3: Devaluation Precedes Senescence

**Statement**: Signal devaluation precedes and predicts platform-level senescence (DAU/MAU decline).

**Evidence approach**:
- Lead-lag analysis: engagement rate inflection (signal) vs DAU/MAU inflection (platform)
- Platforms: Facebook (engagement decline 2013 → DAU growth slowdown 2017), Instagram, Snapchat
- Granger causality test on quarterly data

**Expected finding**: Signal devaluation leads platform senescence by 2-4 years.

**Connection to EN1**: This provides the micro-mechanism for EN1's Mechanism #1 (Advertising Ratchet).

### H4: Design-Maintained Signal Cost

**Statement**: Platforms that structurally maintain signal cost show slower engagement decline.

**Evidence approach**:
- Comparative case study:
  - TikTok: algorithm-first, likes exist but algorithm determines distribution → reduced like-seeking behavior
  - BeReal: no likes, no follower counts → radical cost maintenance
  - Twitter/X: likes fully visible, no deprecation → continued toxification
- Compare engagement rate trajectories

**Expected finding**: TikTok and BeReal show flatter engagement decline curves than like-centric platforms.

### H5: Identity-Level Signals (Predictive)

**Statement**: The next generation of engagement signals will operate at the identity level — not "I saw this" but "this changed who I am."

**Evidence approach** (Phase 2, post-Currot launch):
- Compare ✦ Keep recipients' subsequent behavior vs Like recipients
- Measure: relationship depth change, conversation initiation rate, retention
- If ✦ Keep recipients show stronger behavioral response → H5 supported

**Theoretical basis**: Following the Signal Cost Spectrum, the next inflection must be a signal with cost higher than DM reply but lower than explicit relationship declaration. Identity-level signals occupy this space.

---

## 6. The Signal Cost Spectrum (New Framework)

### 6.1 Framework

```
Signal Cost Spectrum:

Cost:  Low ─────────────────────────────────────── High
       │                                              │
       Like  Comment  DM Reply  Ask  ✦ Keep  Relationship
       (★☆)  (★★☆)   (★★★☆)   (★★★★) (★★★★★)  Declaration
       │      │        │         │      │         │
Value: "saw"  "thought" "want to" "want  "this    "we are
              about it   talk"    to     changed   connected"
                                 know    who I
                                 you"    am"
```

### 6.2 Generational Succession

Each "generation" of social media is defined by its dominant engagement signal:

| Generation | Era | Dominant Signal | Cost | Platform |
|---|---|---|---|---|
| 1st | 2004-2012 | Like/Poke | ★☆☆☆☆ | Facebook |
| 2nd | 2012-2016 | Photo Like | ★★☆☆☆ | Instagram |
| 3rd | 2016-present | Story DM Reply | ★★★☆☆ | Instagram Stories, Snapchat |
| 4th | (predicted) | Identity-level | ★★★★★ | ? (Currot ✦ Keep) |

Each transition occurs when the previous signal inflates to the point of toxification.

### 6.3 Design Implication

**The Signal Inflation Trap**: platforms that optimize for engagement quantity (more likes per session) accelerate signal inflation, which accelerates senescence. The way to escape is not to optimize the existing signal but to introduce a structurally higher-cost signal.

---

## 7. Discussion

### 7.1 Implications for Platform Design

1. **Signal cost must be maintained by design.** It is not sufficient to introduce a high-cost signal; the platform must resist the natural tendency to reduce friction (which reduces cost, which reduces value).

2. **Deprecation is a signal of signal failure, not platform failure.** When Instagram hides like counts, it's acknowledging that the signal has inflated past usefulness — not that Instagram is dying.

3. **The next platform will not be built on a better like.** It will be built on a fundamentally different signal — one that is costly by nature, not by design.

### 7.2 Implications for Research

1. **EN1 connection**: Signal inflation provides the micro-mechanism for the macro-level senescence hypothesis. Future work should test the causal chain: advertising optimization → signal inflation → engagement decline → platform senescence.

2. **EN5 connection**: Signal Cost Theory (Spence, 1973) appears to be a unifying framework for both AI/human interaction quality (EN5) and engagement signal evolution (EN6). Future work should develop this into a general theory of social media signal economics.

### 7.3 Limitations

1. Public engagement rate data has measurement issues (platform-reported vs third-party estimates)
2. Causal claims from observational time-series are inherently limited
3. H5 (identity-level signals) is predictive and requires future validation

### 7.4 The Ephemeral Treadmill Problem

Stories solved signal inflation but created a new problem: nothing accumulates. Users are on an "ephemeral treadmill" — constantly producing content that disappears, maintaining social presence without building identity. The next platform must solve both problems: maintain signal cost (avoid inflation) while enabling accumulation (avoid the treadmill).

---

## 8. Conclusion

The like button's decline is not a story of one feature failing. It is a predictable consequence of signal economics: when signals become cheap to produce, they lose value, and markets respond by introducing costlier signals. Instagram Stories, Snapchat's ephemeral messaging, and BeReal's radical signal removal are all market responses to the same underlying dynamic — signal inflation.

Our Signal Cost Spectrum predicts that the next generation of social media will be defined by identity-level signals: engagement acts so costly that they can only mean "this changed who I am." These signals will be rarer than likes but exponentially more valuable — and the platforms built around them will be structurally resistant to the inflation that killed the like.

---

## Data Requirements (Phase 1, Public Data)

| Dataset | Source | Status |
|---|---|---|
| Instagram engagement rate 2013-2025 | Rival IQ, Socialinsider annual reports | TODO |
| Facebook organic reach 2012-2023 | Edgerank Checker, Social@Ogilvy, Locowise | TODO |
| Facebook DAU/MAU/Revenue quarterly | Meta SEC filings | ✅ EN1에서 수집 |
| Snap DAU/Revenue quarterly | Snap SEC filings | ✅ EN1에서 수집 |
| Instagram like-hiding timeline | Instagram blog, press coverage | TODO |
| YouTube dislike-hiding timeline | YouTube blog, press coverage | TODO |
| Pew Research platform attitudes | Pew Research Center | ✅ EN1에서 수집 |
| TikTok engagement comparison | eMarketer, Sensor Tower | TODO |
| BeReal usage/engagement data | App Annie, press reports | TODO |
| Academic studies on like effects | Vogel 2014, Appel 2016, Braghieri 2022 | TODO |
