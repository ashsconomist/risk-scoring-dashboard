# Risk Scoring & Threshold Detection Dashboard

An interactive analytics dashboard applying multi-metric threshold 
detection to classify records into risk tiers and surface actionable 
patterns for operational decision-making.

![Records](https://img.shields.io/badge/Records-1000-blue) 
![Risk Levels](https://img.shields.io/badge/Risk%20Levels-4-orange) 
![Status](https://img.shields.io/badge/Status-Active-green)

## Overview

This dashboard tracks 1,000 records across 4 time periods (2021–2024) 
using three longitudinal performance metrics:

- **Metric A** — Year-over-year change, dimension 1
- **Metric B** — Year-over-year trend, dimension 2
- **Metric C** — Year-over-year trend, dimension 3

The scoring engine flags records when any metric declines beyond a 
configurable threshold and assigns a Risk Score of 0–3 based on how 
many metrics are declining simultaneously.

## Risk Tiers

| Score | Name | Criteria | Recommended Action |
|-------|------|----------|--------------------|
| 🔴 **3** | Critical | All 3 metrics declining >5% | Immediate multi-factor review |
| 🟠 **2** | Intervention Needed | 2 metrics declining >5% | Targeted intervention |
| 🟡 **1** | Early Warning | 1 metric declining >5% | Monitoring + check-in |
| 🟣 **--** | Stable but Struggling | Estimated absolute levels <70% despite stable YoY | Recovery-level response |
| 🟢 **0** | On Track | No risk factors | Continue monitoring |

## Key Features

### Estimated Absolute Levels
The dashboard calculates cumulative decline to estimate where records 
actually stand — not just whether they are improving or declining 
year-over-year.

**Example:** A record may show Risk 0 (stable year-over-year) but have 
estimated absolute levels of 41% / 49% / 49% across its three metrics. 
Without this feature, it would appear healthy when it actually requires 
urgent attention. This is the "Stable but Struggling" insight.

### Interactive Charts
- Year-over-year trend analysis
- Risk distribution by cohort
- Scatter plot: Metric A vs. Metric B
- Attrition/conversion rates by risk tier

### Filtering & Search
- Filter by time period, segment, and risk level
- Search by individual record ID
- Toggle between table and chart views

### Automated Recommendations
Intervention logic triggered by risk score and specific metric drivers.

## Methodology

**Risk Scoring:**
- Records flagged when any metric declines >5% year-over-year
- Risk score = count of declining metrics (0–3)

**Estimated Absolute Levels:**
- Baseline set at initialization (Period 1)
- Each subsequent period: prior estimate + observed change
- "Struggling" threshold: estimated level <70% in any metric

**Background:** This threshold-based detection methodology is adapted 
from longitudinal administrative data analysis work, demonstrating how 
analytical frameworks from labor economics translate directly into 
operational decision-support tools across industries.

## Key Findings (Sample Dataset, n=1,000)

| Metric | Value |
|--------|-------|
| Total Records | 1,000 |
| Attrition Rate | 7.1% |
| Critical Risk Attrition Rate | 55.9% |
| On Track Attrition Rate | 4.6% |
| Cohort Retention Rate | 83.6% |

**Key Insight:** Records at Risk Level 3 attrite at 12x the rate of 
Risk Level 0 records.

## Quick Start

1. Download `index.html`
2. Open in any modern browser — no build process required
3. Use filters to explore the data
4. Toggle between Table View and Charts View

## File Structure
```
risk-scoring-dashboard/
├── index.html    # Self-contained dashboard
└── README.md     # This file
```

## Technical Stack

- Pure HTML / CSS / JavaScript — no dependencies or build tools
- Chart.js 4.4.0 for visualizations
- All data embedded in the HTML file
- LLM-assisted development (ChatGPT, Claude) for scoring logic 
  and dashboard architecture
- Responsive layout for desktop and tablet

## Live Demo

[View Dashboard](https://ashsconomist.github.io/student-risk-dashboard/)

## License

Synthetic/anonymized data. For portfolio and demonstration purposes.
