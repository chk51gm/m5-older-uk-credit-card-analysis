# M5 Data Science Professional Practice — Older UK Credit-Card Customers

BSc (Hons) Data Scientist, M5.

This repo has the data and script behind the age-band analysis in my M5 report
(older UK adults and credit-card use). Everything here is public FCA/ONS survey
data — nothing from work, no customer data.

## Files

- `data/age_credit_usage_2022_2024.csv` — FCA Financial Lives age-band table (holding/usage by age, 2024 + change since 2022)
- `scripts/analysis.py` — loads the csv, works out 2022 values from the change, runs the Spearman test
- `figures/` — the charts used in the report
- `report/` — final report (docx + pdf)

## Sources

- FCA Financial Lives 2024 survey: [Credit & Loans](https://www.fca.org.uk/publication/financial-lives/fls-2024-credit-loans.pdf), [Payments](https://www.fca.org.uk/publication/financial-lives/fls-2024-payments.pdf), [Key findings](https://www.fca.org.uk/publication/financial-lives/financial-lives-survey-2024-key-findings.pdf)
- FCA Financial Lives 2022: [Key findings](https://www.fca.org.uk/publication/financial-lives/financial-lives-survey-2022-key-findings.pdf)
- FCA Financial Lives 2017: [report](https://www.fca.org.uk/publication/research/financial-lives-survey-2017.pdf)
- ONS cohort life expectancy tables: [link](https://www.ons.gov.uk/peoplepopulationandcommunity/birthsdeathsandmarriages/lifeexpectancies/bulletins/pastandprojecteddatafromtheperiodandcohortlifetables/2024baseduk1981to2074)

## Running it

```
pip install -r requirements.txt
python scripts/analysis.py
```

Should print the reconstructed 2022 values plus the Spearman result (rho 0.873, p 0.010), which is what's quoted in the report.

## Limitations

FCA's oldest published band is 75+, so there's no clean 80+ split — I didn't
try to extrapolate one, even though the workplace process this evaluates is
really about 80+ customers. The 2,000/month and 15-min figures in Part 2 are
just my own assumptions for the evaluation, not real operational numbers.
