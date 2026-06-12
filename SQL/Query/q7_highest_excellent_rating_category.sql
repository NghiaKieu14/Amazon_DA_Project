SELECT main_category, count(rating_label) as rating_count
FROM `bionic-slate-272814.Amazon_dataset.amazon_products`
WHERE rating_label = "Excellent"
GROUP BY main_category
ORDER BY rating_count DESC
LIMIT 1