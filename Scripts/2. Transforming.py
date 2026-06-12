import pandas as pd

df = pd.read_csv("amazon_cleaned.csv")

df["main_category"] = df["category"].str.split(r"\|", n=1).str[0]
print(df["main_category"])

df["savings"] = df["actual_price"] - df["discounted_price"]
print(df["savings"])

bins1 = [0, 200, 1000, 5000, 20000, float("inf")]
labels1 = ["Under 200", "200 - 1000", "1000 - 5000", "5000 - 20000", "Above 20000"]
df["price_bucket"] = pd.cut(df["actual_price"], bins = bins1, labels = labels1, right= False)
print(df["price_bucket"])

df["rating"] = pd.to_numeric(df["rating"], errors="coerce")
bins2 = [0, 1.01, 2.01, 3.01, 4.01, 5.01]
labels2 = ["Poor", "Moderate", "Average", "Good", "Excellent"]
df["rating_label"] = pd.cut(df["rating"], bins = bins2, labels = labels2, right= False)
print(df["rating_label"])

df = df[
    [
        "product_id",
        "product_name",
        "main_category",
        "category",
        "discounted_price",
        "savings",
        "actual_price",
        "price_bucket",
        "discount_percentage",
        "rating",
        "rating_label",
        "rating_count",
        "about_product",
        "user_id",
        "user_name",
        "review_id",
        "review_title",
        "review_content",
        "img_link",
        "product_link"
    ]
]

df.to_csv("amazon_transformed.csv", index = False)