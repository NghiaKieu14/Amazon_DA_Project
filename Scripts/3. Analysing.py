import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("../Data/amazon_transformed.csv")

plt.figure(figsize=(10, 4.5))
sns.histplot(df["discounted_price"].dropna(), bins=30, kde=True)
plt.title("Figure 1: Distribution of Discounted Price")
plt.xlabel("Discounted Price")
plt.ylabel("Count")

plt.figtext(
    0.5, 0.01,
    "Comment: Most products are priced under ₹2,000 - the market is overwhelmingly budget-focused.",
    ha="center",
    fontsize=10
)

plt.tight_layout()
plt.show()

product_count = df["main_category"].value_counts()

plt.figure(figsize=(10, 4))
sns.barplot(x=product_count.index, y=product_count.values)
plt.title("Figure 2: Number of Products by Main Category")
plt.xlabel("Main Category")
plt.ylabel("Number of Products")
plt.xticks(rotation=45)

plt.figtext(
    0.5, 0.01,
    "Comment: 3 categories (Electronics, Computers, Home&Kitchen) make up ~97% of the dataset.",
    ha="center",
    fontsize=10
)

plt.tight_layout()
plt.show()

avg_rating = df.groupby("main_category")["rating"].mean().sort_values(ascending=False)

plt.figure(figsize=(10, 5))
sns.barplot(x=avg_rating.index, y=avg_rating.values)
plt.title("Figure 3: Average Rating by Main Category")
plt.xlabel("Main Category")
plt.ylabel("Average Rating")
plt.xticks(rotation=45)

plt.figtext(
    0.5, 0.01,
    "Comment: All categories average rate between 3.8-4.3 - suspiciously narrow, suggesting a platform-wide positivity bias.",
    ha="center",
    fontsize=10
)

plt.tight_layout()
plt.show()

avg_discount = df.groupby("main_category")["discount_percentage"].mean().sort_values(ascending=False)

plt.figure(figsize=(10, 5))
sns.barplot(x=avg_discount.index, y=avg_discount.values)
plt.title("Figure 4: Average Discount Percentage by Main Category")
plt.xlabel("Main Category")
plt.ylabel("Average Discount %")
plt.xticks(rotation=45)

plt.figtext(
    0.5, 0.01,
    "Comment: HomeImprovement discounts the most (~57%), Toys&Games barely discounts at all.",
    ha="center",
    fontsize=10
)

plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x="actual_price", y="discounted_price", hue="price_bucket", alpha=0.6)
plt.title("Figure 5: Actual Price vs Discounted Price")
plt.xlabel("Actual Price")
plt.ylabel("Discounted Price")

plt.figtext(
    0.5, 0.01,
    "Comment: Price and discount follow a linear trend, but premium products (green, >₹20,000) show the most inconsistent discount depths.",
    ha="center",
    fontsize=10
)

plt.tight_layout()
plt.show()