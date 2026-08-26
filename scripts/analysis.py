"""
M5 report analysis: older UK credit-card customers, age-band analysis.
Loads the FCA age-band table, works out the 2022 values from the reported change,
runs a Spearman test (usage growth vs age rank), and saves the two report figures.
"""

import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import spearmanr

df = pd.read_csv("data/age_credit_usage_2022_2024.csv")

# seven standard FCA age bands, lowest to highest
df["age_rank"] = range(1, len(df) + 1)

# 2022 values aren't printed separately in the FCA tables, only the 2024 value
# and the change since 2022 — so just subtract the change off the 2024 figure
df["holding_2022"] = (df["credit_card_holding_2024"] - df["credit_card_holding_change_2022_2024"]).round(4)
df["usage_2022"] = (df["credit_card_usage_2024"] - df["credit_card_usage_change_2022_2024"]).round(4)

# quick sanity check: the reconstructed 2022 figures have to fall between 0 and 1
assert (df["holding_2022"].between(0, 1)).all()
assert (df["usage_2022"].between(0, 1)).all()

# Spearman: does usage growth rise with age band?
rho, p = spearmanr(df["age_rank"], df["credit_card_usage_change_2022_2024"])
print(f"Spearman rho = {rho:.3f}, p = {p:.3f}")

older = df[df["age_rank"] >= 5]    # 55 and over
younger = df[df["age_rank"] <= 4] # under 55
print(f"Mean usage change (55+): {older['credit_card_usage_change_2022_2024'].mean()*100:.2f}pp")
print(f"Mean usage change (<55): {younger['credit_card_usage_change_2022_2024'].mean()*100:.2f}pp")

# Figure 1 — holding by age, 2022 vs 2024
x = range(len(df))
w = 0.4
plt.figure(figsize=(8, 4))
plt.bar([i - w/2 for i in x], df["holding_2022"]*100, width=w, label="2022")
plt.bar([i + w/2 for i in x], df["credit_card_holding_2024"]*100, width=w, label="2024")
plt.xticks(list(x), df["age_band"])
plt.ylabel("Adults holding a credit card (%)")
plt.title("Credit-card holding by age: 2022 vs 2024")
plt.legend()
plt.tight_layout()
plt.savefig("figures/figure1_holding_by_age.png")
plt.close()

# Figure 2 — usage change 2022 to 2024 by age band
plt.figure(figsize=(8, 4))
plt.bar(list(x), df["credit_card_usage_change_2022_2024"]*100)
plt.axhline(0, color="grey", linewidth=0.8)
plt.xticks(list(x), df["age_band"])
plt.ylabel("Change in credit-card usage (pp)")
plt.title("Change in credit-card usage by age, 2022 to 2024")
plt.tight_layout()
plt.savefig("figures/figure2_usage_change_by_age.png")
plt.close()

print("\nFigures saved to figures/")
print()
print(df.to_string(index=False))
