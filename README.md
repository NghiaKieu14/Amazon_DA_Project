<div align="center">

# Amazon Product Analysis - Personal Project

### *An end-to-end data analytics project from raw e-commerce data to SQL queries and Power BI dashboard*

<h3>🛒 📊 🧹 🔍 🗄️ 📈</h3>

<p>
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python 3.10+" />
  <img src="https://img.shields.io/badge/pandas-Data%20Analysis-150458?style=flat-square&logo=pandas&logoColor=white" alt="pandas" />
  <img src="https://img.shields.io/badge/Matplotlib-Visualization-11557C?style=flat-square" alt="Matplotlib" />
  <img src="https://img.shields.io/badge/Seaborn-Statistical%20Charts-4C72B0?style=flat-square" alt="Seaborn" />
</p>

<p>
  <img src="https://img.shields.io/badge/Google%20BigQuery-SQL%20Analysis-4285F4?style=flat-square&logo=googlebigquery&logoColor=white" alt="BigQuery" />
  <img src="https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?style=flat-square&logo=powerbi&logoColor=black" alt="Power BI" />
  <img src="https://img.shields.io/badge/Jupyter-Notebook-F37626?style=flat-square&logo=jupyter&logoColor=white" alt="Jupyter" />
</p>

<br />

*From raw Amazon product listings to cleaned analytical data, pricing insights, SQL queries on BigQuery, and an interactive Power BI dashboard.*

<p>
  <b>🛒 E-commerce Data</b> &nbsp;•&nbsp;
  <b>🧹 Data Cleaning</b> &nbsp;•&nbsp;
  <b>🔧 Feature Engineering</b> &nbsp;•&nbsp;
  <b>📊 Exploratory Analysis</b> &nbsp;•&nbsp;
  <b>🗄️ SQL on BigQuery</b> &nbsp;•&nbsp;
  <b>📈 Power BI</b>
</p>

</div>

---

## Project Overview

An end-to-end personal data analytics project built on Amazon India product listings. The project turns raw, unformatted e-commerce data into a cleaned analytical dataset; engineers new features for richer analysis; explores pricing and discount patterns; runs structured SQL queries on Google BigQuery; and delivers the findings through an interactive Power BI dashboard.

The work is designed to answer practical e-commerce questions:

- How are products distributed across price ranges and categories?
- Which categories apply the steepest discounts?
- How do customer ratings vary across product categories and price tiers?
- Which products attract the most customer reviews?
- Which products offer the highest absolute savings for buyers?
- Is there a relationship between price and customer satisfaction?

## Table of Contents

- [Project Overview](#project-overview)
- [Project Highlights](#project-highlights)
- [Repository Structure](#repository-structure)
- [Dataset Overview](#dataset-overview)
- [Workflow](#workflow)
- [SQL Analysis](#sql-analysis)
- [Key Findings](#key-findings)
- [Dashboard](#dashboard)
- [Limitations](#limitations)
- [What I Learned](#what-i-learned)

## Project Highlights

| Area | What this project does |
| ---- | ---  |
| Data cleaning | Strips currency symbols, commas, and percent signs from raw string fields; converts to numeric types; fills missing values using the median. |
| Feature engineering | Creates `main_category`, `savings`, `price_bucket`, and `rating_label` columns to enable richer segmentation and analysis. |
| Exploratory analysis | Studies price distributions, category composition, average ratings, discount patterns, and price-to-discount relationships across five visualisations. |
| SQL analysis | Runs seven targeted queries on Google BigQuery to answer specific business questions about ratings, discounts, price buckets, top products, and savings. |
| Power BI dashboard | Builds an interactive report for filtering and exploring results by category, price bucket, and rating label. |

## Repository Structure

```text
Personal_Project1/
|
|-- Data/
│   |-- amazon_raw.csv              # Original dataset (untouched)
│   |-- amazon_cleaned.csv          # After cleaning step
│   |-- amazon_transformed.csv     # Final enriched dataset (used for analysis)
│
|-- Python/
│   |-- Understanding_data.ipynb   # Full workflow: cleaning -> transforming -> EDA & visualisation
│
|-- SQL/
│   |-- Query/
│   │   |-- q1_avg_rating_by_category.sql
│   │   |-- q2_top_10_most_reviewed_products.sql
│   │   |-- q3_highest_avg_discount_category.sql
│   │   |-- q4_price_bucket_product_distribution.sql
│   │   |-- q5_highest_savings_product.sql
│   │   |-- q6_avg_rating_according_to_price_bucket.sql
│   │   |-- q7_highest_excellent_rating_category.sql
│   |-- Result/
│       |-- q1_result.csv
│       |-- q2_result.csv
│       |-- q3_result.csv
│       |-- q4_result.csv
│       |-- q5_result.csv
│       |-- q6_result.csv
│       |-- q7_result.csv
│
|-- Dashboard_amazon.pbix           # Power BI dashboard
|-- README.md                       # Project documentation (this file)
```

## Dataset Overview

The project works with a static snapshot of Amazon India product listings. The cleaned analytical file contains **1,465 product records** and **20 columns** after preprocessing and feature engineering.

### Raw data source

Source: https://www.kaggle.com/datasets/karkavelrajaj/amazon-sales-dataset

### Main data files

| File | Description |
| --- | --- |
| `Data/amazon_raw.csv` | Raw product data with 1,465 rows and 16 columns. All numeric fields are stored as strings with currency symbols and formatting characters. |
| `Data/amazon_cleaned.csv` | Cleaned dataset with numeric types, no formatting noise, and median-imputed missing values. |
| `Data/amazon_transformed.csv` | Final analytical dataset with four engineered columns added: `main_category`, `savings`, `price_bucket`, and `rating_label`. |

### Key original fields

| Field | Meaning |
| --- | --- |
| `product_id` | Unique product identifier. |
| `product_name` | Full product name. |
| `category` | Full nested category path separated by `\|`. |
| `actual_price` | Original listed price in ₹ (stored as string in raw data). |
| `discounted_price` | Price after discount in ₹ (stored as string in raw data). |
| `discount_percentage` | Discount applied as a percentage (stored as string in raw data). |
| `rating` | Average customer rating (0–5 scale). |
| `rating_count` | Number of customer ratings. |
| `review_title` / `review_content` | Customer review text. |

## Workflow

All steps are documented in `Python/Understanding_data.ipynb`.

### Step 1 — Data Cleaning

The raw dataset stores all numeric fields as strings with currency symbols and formatting characters that must be removed before analysis.

- Stripped `₹` and `,` from `discounted_price` and `actual_price` → cast to `float`
- Stripped `%` from `discount_percentage` → cast to `float`
- Cleaned `rating_count` (removed commas) → cast to `float`; filled missing values with the **median** to avoid skew from outliers
- Exported result to `amazon_cleaned.csv`

### Step 2 — Feature Engineering

Four derived columns were added to enable segmentation and richer queries:

| New Column | Logic |
| --- | --- |
| `main_category` | Extracted the top-level category by splitting the full path on `\|` — e.g. `Electronics\|Accessories` -> `Electronics` |
| `savings` | `actual_price − discounted_price` — absolute saving per product |
| `price_bucket` | Binned `actual_price` into five ranges: Under 200 / 200–1,000 / 1,000-5,000 / 5,000-20,000 / Above 20,000 (₹) |
| `rating_label` | Mapped numeric rating to a text label: Poor / Moderate / Average / Good / Excellent |

Final column selection was fixed at 20 meaningful columns, then exported to `amazon_transformed.csv`.

### Step 3 — Exploratory Data Analysis

Five visualisations were produced with matplotlib and seaborn:

| Figure | Chart type | What it shows |
| --- | --- | --- |
| Figure 1 | Histogram + KDE | Distribution of discounted prices — heavy right skew, market is budget-focused |
| Figure 2 | Bar chart | Number of products per main category — three categories dominate |
| Figure 3 | Bar chart | Average rating per main category — narrow band of 3.8–4.3 across all categories |
| Figure 4 | Bar chart | Average discount % per main category — Home Improvement leads at ~57.5% |
| Figure 5 | Scatter plot | Actual price vs discounted price coloured by price bucket — linear trend, widest spread in premium tier |

## SQL Analysis

All queries were run on **Google BigQuery** against the transformed dataset.

| # | Business question | Query file |
| --- | --- | --- |
| Q1 | Which category has the highest average rating? | `q1_avg_rating_by_category.sql` |
| Q2 | Which are the top 10 most-reviewed products? | `q2_top_10_most_reviewed_products.sql` |
| Q3 | Which main category has the highest average discount? | `q3_highest_avg_discount_category.sql` |
| Q4 | How are products distributed across price buckets? | `q4_price_bucket_product_distribution.sql` |
| Q5 | Which product offers the highest absolute saving? | `q5_highest_savings_product.sql` |
| Q6 | Does a higher price bucket mean a higher average rating? | `q6_avg_rating_according_to_price_bucket.sql` |
| Q7 | Which category has the most "Excellent"-rated products? | `q7_highest_excellent_rating_category.sql` |

Results for each query are saved in the corresponding `SQL/Result/q*_result.csv` file.

## Key Findings

### Pricing & Discounts

- **Most products (610 out of 1,465) fall in the ₹1,000–5,000 range** - the dominant price tier. Only 37 products are priced under ₹200.
- **HomeImprovement offers the steepest average discount at ~57.5%** - nearly double that of most other categories, suggesting aggressive promotional pricing.
- **The product with the highest absolute saving** is the *Sony Bravia 65" 4K Smart TV*, discounted from ₹139,900 to ₹77,990 - a saving of ₹61,910 for the buyer.
- Premium products (Above ₹20,000) show the widest variation in discount depth, while budget products are discounted more consistently.

### Ratings

- **All categories average between 3.8–4.3 stars** - a suspiciously narrow range that likely reflects a platform-wide positivity bias in Amazon reviews.
- **Electronics leads in "Excellent" ratings** with 393 products rated 4.0-5.0, the most of any main category.
- **Higher price buckets tend to have marginally higher average ratings** (Above 20,000: 4.23 vs 200–1,000: 4.07), but the difference is small - price alone does not predict customer satisfaction.

### Most Reviewed Products

- Amazon Basics HDMI Cables dominate the top 10 most-reviewed products (~426,973 reviews each), reflecting high sales volume for commodity accessories.
- boAt Bassheads earphones appear multiple times, confirming strong demand for budget audio products in the Indian market.

### Category Composition

- Electronics (526), Computers&Accessories (453), and Home&Kitchen (448) account for ~97% of all products.
- Remaining categories - Office Products, Musical Instruments, Home Improvement, Toys & Games, Car & Motorbike, Health & Personal Care — together represent only ~38 products and carry limited analytical weight.

## Dashboard

The `Dashboard_amazon.pbix` file provides an interactive view of the dataset in Power BI, with filters for category, price bucket, and rating label.

> Requires **Power BI Desktop** to open.

## Limitations

- **The dataset was relatively clean to begin with.** Most of the cleaning work was formatting-related - stripping currency symbols, commas, and percent signs. There were no major structural problems such as duplicate records, heavily corrupted fields, or complex missingness patterns. This means the cleaning step was good practice but does not reflect the messiness of real-world business data.
- **Insights remain at a descriptive level.** The analysis answers "what" questions (which category discounts the most? which product has the most reviews?) but does not go deeper into causality - for example, whether higher discounts actually drive more reviews, or whether the rating gap across price tiers is statistically meaningful.
- **The dataset is skewed toward three categories.** Electronics, Computers & Accessories, and Home & Kitchen make up ~97% of all records. Categories like Toys & Games, Musical Instruments, and Car & Motorbike have only one or two products each, making any category-level conclusions for them unreliable.
- **Review count is an imperfect proxy for sales volume.** Review count was used to identify popular products, but counts can be inflated by product variants sharing the same listing - likely the case for the Amazon Basics HDMI cables appearing multiple times with near-identical counts.
- **No time dimension.** The dataset is a static snapshot with no timestamps, so trends over time - seasonal discounts, rating drift, or new product launches - cannot be analysed.

## What I Learned

- **Data cleaning decisions have downstream consequences.** Choices like using median over mean for skewed fields (rating count), or how to define price bucket boundaries, directly shape the results of later analysis and SQL queries.
- **Feature engineering is where analytical value is created.** The raw dataset had no `main_category`, no `savings`, no `price_bucket`. Adding these four columns was what made the SQL queries and visualisations possible.
- **SQL and Python complement each other.** Python handled the messy transformation work and visualisation; SQL on BigQuery was faster and more readable for answering specific aggregation questions on the cleaned data.
- **End-to-end ownership reveals the full picture.** Owning every stage from raw CSV to BigQuery to Power BI made the tradeoffs at each step visible - and gave a realistic sense of what a data analyst workflow looks like in practice.

---

<div align="center">

*Built as a personal project to practise end-to-end data analytics skills for a Data Analyst Internship application.*

</div>
