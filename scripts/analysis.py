"""
Older UK Credit-Card Customers: Age-Band Analysis
BSc (Hons) Data Scientist, M5 Data Science Professional Practice

Source data: FCA Financial Lives 2024 survey (17,950 UK adults), underlying chart
data published by the FCA (Credit & Loans and Payments selected findings, May 2025)
and ONS cohort life-expectancy tables (2026).

This script:
1. Loads the age-banded credit-card holding/usage table (data/age_credit_usage_2022_2024.csv)
2. Reconstructs the comparable 2022 values from the published percentage-point change
3. Runs a Spearman rank-correlation test between age rank and usage growth
4. Produces Figures 1-2 (holding and usage change by age band)

All figures are public, aggregated survey statistics. No employer or customer data
is used anywhere in this project, per the coursework's synthetic/public-data
requirement.
"""

import pandas as pd
from scipy.stats import spearmanr

DATA_PATH = "data/age_credit_usage_2022_2024.csv"


def load_data(path: str = DATA_PATH) -> pd.DataFrame:
    df = pd.read_csv(path)
    df["age_rank"] = range(1, len(df) + 1)
    # Reconstruct 2022 values from the FCA-reported percentage-point change
    df["credit_card_holding_2022"] = (
        df["credit_card_holding_2024"] - df["credit_card_holding_change_2022_2024"]
    ).round(4)
    df["credit_card_usage_2022"] = (
        df["credit_card_usage_2024"] - df["credit_card_usage_change_2022_2024"]
    ).round(4)
    return df


def validate(df: pd.DataFrame) -> None:
    """Sanity checks: every reconstructed value must reproduce the reported
    change exactly and stay within [0, 1]."""
    for col_2024, col_change, col_2022 in [
        ("credit_card_holding_2024", "credit_card_holding_change_2022_2024", "credit_card_holding_2022"),
        ("credit_card_usage_2024", "credit_card_usage_change_2022_2024", "credit_card_usage_2022"),
    ]:
        reconstructed_change = (df[col_2024] - df[col_2022]).round(4)
        assert (reconstructed_change == df[col_change]).all(), f"Mismatch in {col_2024}"
        assert (df[col_2022].between(0, 1)).all(), f"Out-of-range value in {col_2022}"
    print("Validation passed: all reconstructed 2022 values reproduce FCA changes exactly.")


def spearman_test(df: pd.DataFrame):
    """Spearman rank correlation between age rank and usage growth (pp)."""
    rho, p_value = spearmanr(df["age_rank"], df["credit_card_usage_change_2022_2024"])
    print(f"Spearman rho = {rho:.3f}, p = {p_value:.3f}")
    return rho, p_value


def summary_stats(df: pd.DataFrame) -> None:
    older = df[df["age_rank"] >= 5]  # 55-64, 65-74, 75+
    younger = df[df["age_rank"] <= 4]  # 18-24 through 45-54
    print(
        f"Average usage growth (55+): {older['credit_card_usage_change_2022_2024'].mean() * 100:.2f}pp"
    )
    print(
        f"Average usage growth (18-54): {younger['credit_card_usage_change_2022_2024'].mean() * 100:.2f}pp"
    )
    print(
        f"Average holding growth (55+): {older['credit_card_holding_change_2022_2024'].mean() * 100:.2f}pp"
    )
    print(
        f"Average holding growth (18-54): {younger['credit_card_holding_change_2022_2024'].mean() * 100:.2f}pp"
    )


if __name__ == "__main__":
    data = load_data()
    validate(data)
    spearman_test(data)
    summary_stats(data)
    print(data.to_string(index=False))
