SELECT main_category, avg(discount_percentage) as avg_discount
FROM `bionic-slate-272814.Amazon_dataset.amazon_products` 
GROUP BY main_category
ORDER BY avg_discount DESC
LIMIT 1
