import pandas as pd
from config import RAW_PATH, CLEAN_PATH, engine

df = pd.read_csv(RAW_PATH)
print("Shape:", df.shape)
df.info()

# TotalCharges loads as text because some rows are blank
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
blank = df[df["TotalCharges"].isna()]
print("Blank TotalCharges rows:", len(blank))
print(blank[["tenure", "MonthlyCharges"]])   # look at the tenure column

df["TotalCharges"] = df["TotalCharges"].fillna(0)
df["Churn_flag"] = (df["Churn"] == "Yes").astype(int)

print("Duplicates:", df.duplicated().sum())
print("Churn rate:", round(df["Churn_flag"].mean(), 4))

df.to_csv(CLEAN_PATH, index=False)
df.to_sql("customers", engine, if_exists="replace", index=False)
print("Loaded into MySQL.")