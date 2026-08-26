"""
M5 report analysis: older UK credit-card customers, age-band analysis.
Loads the FCA age-band table, works out the 2022 values from the reported change,
runs a Spearman test (usage growth vs age rank).
"""

import pandas as pd
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

print()
print(df.to_string(index=False))
