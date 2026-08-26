# Older UK Credit-Card Customers: Age-Band Analysis

BSc (Hons) Data Scientist — Data Science Professional Practice (M5)

This portfolio hosts the public-data analysis used in the summative report
"Older UK Credit-Card Customers: An Age-Band Analysis of Demand and Repayment
Behaviour". It is provided so the report's findings can be checked and reproduced.

## Repository contents

```
.
├── report/
│   └── Older UK Credit-Card Customers — Final Report.docx   # full summative report
├── figures/
│   ├── figure1_holding_by_age.png        # Figure 1 — credit-card holding by age, 2022 vs 2024
│   ├── figure2_usage_change_by_age.png   # Figure 2 — change in credit-card usage 2022–2024
│   ├── figure3_life_expectancy.png        # Figure 3 — UK cohort life expectancy at 65
│   ├── figure4_holding_use_older.png      # Figure 4 — holding & use among older adults, 2024
│   └── figure5_wage_capacity_scenarios.png # Figure 5 — illustrative wage-equivalent capacity
├── scripts/
│   └── analysis.py                       # loads data, validates reconstruction, runs Spearman test
├── data/
│   └── age_credit_usage_2022_2024.csv   # FCA Financial Lives 2024 age-banded table
├── requirements.txt
└── README.md
```

## Data source

All statistics come from public UK survey publications:

* **FCA Financial Lives 2024 survey** (17,950 UK adults) — credit-card holding and use by age band, and the 2022–2024 change, taken from the FCA's published "Credit and loans" and "Payments" selected findings tables (May 2025). Older repayment evidence comes from the FCA Financial Lives 2017 report.
* **ONS** 2024-based cohort life-expectancy tables (2026).

No employer or customer data is used in any file in this repository. The analysis
is built entirely on publicly published, aggregated survey statistics.

## How to run

```bash
python -m venv venv && source venv/bin/activate   # optional
pip install -r requirements.txt
python scripts/analysis.py
```

The script loads the FCA-derived age-band table, reconstructs the 2022 values from
the FCA-reported percentage-point change (and checks that reconstruction exactly
reproduces the reported change), then runs a Spearman rank-correlation test
between age rank and usage growth. Expected output:

```
Validation passed: all reconstructed 2022 values reproduce FCA changes exactly.
Spearman rho = 0.873, p = 0.010
Average usage growth (55+): 5.67pp
Average usage growth (18-54): 0.50pp
```

These are the figures cited in the report (rho = 0.873, p = 0.010).

## Notes on scope and limitations

* The oldest FCA age band is 75+. There is no published clean 80+ or 85+
  credit-card segment, so the analysis does not extrapolate one. The workplace
  process focuses on customers aged around 80+, which is a genuine limitation
  discussed in the report.
* The operational figures in Part 2 (approximately 2,000 affected customers per
  month and a 15-minute additional interaction) are student-supplied business
  context, not audited operational data. The 2026 National Living Wage is used
  only as a benchmark wage rate.
* Public survey data identifies population-level patterns. It does not predict
  whether any individual older customer can afford or repay credit — that
  remains an affordability and creditworthiness assessment under FCA rules.
