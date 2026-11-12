import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from config import CLEAN_PATH

df = pd.read_csv(CLEAN_PATH)

sns.set_theme(style="whitegrid")

print("Dataset Shape:", df.shape)
print(df.info())
print(df.isnull().sum())

#Univariate analysis – Churn distribution

plt.figure(figsize=(7, 5))

sns.countplot(data=df, x="Churn")

plt.title("Customer Churn Distribution")
plt.xlabel("Churn")
plt.ylabel("Number of Customers")

plt.savefig("../images/churn_distribution.png")
plt.show()

#Bivariate analysis – Churn vs Contract
plt.figure(figsize=(9, 5))

sns.countplot(
    data=df,
    x="Contract",
    hue="Churn"
)

plt.title("Customer Churn by Contract Type")
plt.xlabel("Contract Type")
plt.ylabel("Number of Customers")

plt.savefig("../images/churn_by_contract.png")
plt.show()

#Tenure distribution
plt.figure(figsize=(9, 5))

sns.histplot(
    data=df,
    x="tenure",
    hue="Churn",
    bins=30,
    kde=True
)

plt.title("Customer Tenure Distribution by Churn")
plt.xlabel("Tenure (Months)")
plt.ylabel("Customer Count")

plt.savefig("../images/tenure_distribution.png")
plt.show()

#Monthly charges vs churn
plt.figure(figsize=(8, 5))

sns.boxplot(
    data=df,
    x="Churn",
    y="MonthlyCharges"
)

plt.title("Monthly Charges vs Customer Churn")
plt.xlabel("Churn")
plt.ylabel("Monthly Charges")

plt.savefig("../images/monthly_charges.png")
plt.show()

#corr analysis
numerical_df = df[
    [
        "SeniorCitizen",
        "tenure",
        "MonthlyCharges",
        "TotalCharges",
        "Churn_flag"
    ]
]

correlation = numerical_df.corr()

print(correlation)

plt.figure(figsize=(8, 6))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Heatmap")

plt.savefig("../images/correlation_heatmap.png")
plt.show()

#final validation
print("Missing values:")
print(df.isnull().sum())

print("\nChurn distribution:")
print(df["Churn"].value_counts(normalize=True) * 100)

print("\nNumerical summary:")
print(df.describe())