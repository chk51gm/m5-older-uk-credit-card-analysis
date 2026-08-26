# M5 — Older UK credit-card customers

BSc (Hons) Data Scientist, M5.

Data and script behind the age-band analysis in my M5 report (older UK adults and
credit-card use). All public FCA/ONS survey data — nothing from work, no
customer data.

## Files

- `data/age_credit_usage_2022_2024.csv` — FCA Financial Lives age-band table
- `scripts/analysis.py` — loads the csv, works out 2022 values from the change, runs the Spearman test, makes the two charts
- `figures/figure1_holding_by_age.png` — Figure 1 (holding by age, 2022 vs 2024)
- `figures/figure2_usage_change_by_age.png` — Figure 2 (usage change 2022–2024 by age)

## Sources

- FCA Financial Lives 2024: [Credit & Loans](https://www.fca.org.uk/publication/financial-lives/fls-2024-credit-loans.pdf), [Payments](https://www.fca.org.uk/publication/financial-lives/fls-2024-payments.pdf), [Key findings](https://www.fca.org.uk/publication/financial-lives/financial-lives-survey-2024-key-findings.pdf)
- FCA Financial Lives 2022: [Key findings](https://www.fca.org.uk/publication/financial-lives/financial-lives-survey-2022-key-findings.pdf)
- FCA Financial Lives 2017: [report](https://www.fca.org.uk/publication/research/financial-lives-survey-2017.pdf)
- ONS cohort life expectancy: [tables](https://www.ons.gov.uk/peoplepopulationandcommunity/birthsdeathsandmarriages/lifeexpectancies/bulletins/pastandprojecteddatafromtheperiodandcohortlifetables/2024baseduk1981to2074)

## Running it

```
pip install pandas scipy matplotlib
python scripts/analysis.py
```

Prints the reconstructed 2022 values plus the Spearman result (rho 0.873, p 0.010),
which is what's quoted in the report, and saves the two figures to `figures/`.

## Notes

FCA's oldest published band is 75+, so there's no clean 80+ split — I didn't try
to extrapolate one. The 2,000/month and 15-min figures in Part 2 are just my own
assumptions for the evaluation, not real operational numbers.
