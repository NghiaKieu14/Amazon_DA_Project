import pandas as pd

df = pd.read_csv("amazon_raw.csv")

print(df.dtypes)
print(df.head())
print(df.shape)
print(df.isnull().sum())

df["discounted_price"] = df["discounted_price"].str.replace("₹", "", regex=False).str.replace(",", "", regex=False).astype(float)
print(df["discounted_price"])

df["actual_price"] = df["actual_price"].str.replace("₹", "", regex=False).str.replace(",", "", regex=False).astype(float)
print(df["actual_price"])

df["discount_percentage"] = df["discount_percentage"].str.replace("%", "", regex=False).astype(float)
print(df["discount_percentage"])

df["rating_count"] = df["rating_count"].str.replace(",", "", regex=False).astype(float)
df["rating_count"] = df["rating_count"].fillna(df["rating_count"].median())
print(df["rating_count"])

print(df.isnull().sum())
df.to_csv("amazon_cleaned.csv", index=False)