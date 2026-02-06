# New Visions Early Warning Analytics Dashboard

A data-driven early warning system for identifying students at risk of dropping out, built with interactive visualizations and actionable insights.

![Dashboard Preview](https://img.shields.io/badge/Students-1000-blue) ![Risk Levels](https://img.shields.io/badge/Risk%20Levels-4-orange) ![Status](https://img.shields.io/badge/Status-Active-green)

## 🎯 Overview

This dashboard helps educators identify and support struggling students before it's too late. It tracks **1,000 students** across 4 years (2021-2024) using three key metrics:

- **Attendance Index** — Year-over-year attendance change
- **Math Stability** — Year-over-year math grade trend  
- **English Stability** — Year-over-year English grade trend

## 🚨 Risk Levels

| Level | Name | Criteria | Action |
|-------|------|----------|--------|
| 🔴 **3** | Critical Risk | All 3 metrics declining >5% | Immediate multi-disciplinary review |
| 🟠 **2** | Intervention Needed | 2 metrics declining >5% | Parent conference + academic support |
| 🟡 **1** | Early Warning | 1 metric declining >5% | Targeted tutoring/check-ins |
| 🟣 **--** | Stable but Struggling | Est. levels <70% despite stable YoY | Recovery intervention needed |
| 🟢 **0** | On Track | No risk factors | Continue monitoring |

## ✨ Key Features

### 📊 Estimated Absolute Levels (NEW)
The dashboard calculates **cumulative decline** to estimate where students actually are—not just whether they're improving or declining year-over-year.

**Example:** A student might show Risk 0 (stable) but have:
- 41% estimated attendance
- 49% estimated math
- 49% estimated English

Without this feature, they'd appear "fine" when they actually need urgent help.

### 📈 Interactive Charts
- Year-over-year trend analysis
- Risk distribution by cohort
- Attendance vs. Math scatter plot
- Dropout conversion rates by risk level

### 🔍 Filtering & Search
- Filter by year, grade, risk level
- Search individual student IDs
- Toggle between table and chart views

### 🎯 Action Recommendations
Automatic intervention suggestions based on risk level and specific drivers.

## 📋 Case Studies

### Student 1002 — "Stable but Struggling"
| Year | Grade | Risk | Est. Attendance | Est. Math | Est. English |
|------|-------|------|-----------------|-----------|--------------|
| 2021 | 9 | 0 | 90% | 75% | 75% |
| 2022 | 10 | 3 | 69% | 61% | 61% |
| 2023 | 11 | 3 | 40% | 49% | 49% |
| 2024 | 12 | **0** | **41%** | **49%** | **49%** |

**Insight:** Shows Risk 0 in senior year but has catastrophic estimated levels. The "Stable but Struggling" feature catches students like this.

### Student 1007 — True Recovery
| Year | Grade | Risk | Est. Attendance | Est. Math | Est. English |
|------|-------|------|-----------------|-----------|--------------|
| 2021 | 9 | 0 | 90% | 75% | 75% |
| 2022 | 10 | 0 | 90% | 77% | 77% |
| 2023 | 11 | 3 | 78% | 60% | 61% |
| 2024 | 12 | 0 | 78% | 63% | 63% |

**Insight:** Had one bad year but recovered to acceptable levels. This is what genuine recovery looks like.

## 🧮 Methodology

**Risk Assessment:**
- Students flagged when any metric declines >5% year-over-year
- Risk level = count of declining metrics (0-3)

**Estimated Levels:**
- Baseline assumptions: 90% attendance, 75% math, 75% English (Grade 9)
- Each year: Previous estimate + year-over-year change
- "Struggling" threshold: <70% in any metric

## 🚀 Quick Start

1. Download `index.html`
2. Open in any modern browser
3. Use filters to explore the data
4. Click "Table View" for detailed student records

## 📁 File Structure

```
student-risk-dashboard/
├── index.html          # Main dashboard (self-contained)
└── README.md           # This file
```

## 🛠️ Technical Details

- **Pure HTML/CSS/JavaScript** — No build process required
- **Chart.js 4.4.0** — For visualizations
- **Self-contained** — All data embedded in the HTML file
- **Responsive** — Works on desktop and tablet

## 📊 Key Findings

| Metric | Value |
|--------|-------|
| Total Students | 1,000 |
| Dropout Rate | 7.1% (71 students) |
| Critical Risk Dropout Rate | 55.9% |
| On Track Dropout Rate | 4.6% |
| 2021 Cohort Graduation Rate | 83.6% |

**Key Insight:** Students at Risk Level 3 drop out at **12x the rate** of Risk Level 0 students.

## 📝 License

This project is for educational purposes. Student data is synthetic/anonymized.

## 🙏 Acknowledgments

Built for New Visions for Public Schools to support student success through data-driven intervention.

---

**Live Demo:** [View Dashboard](https://ashseconomist.github.io/student-risk-dashboard/)


