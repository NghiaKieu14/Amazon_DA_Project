SELECT category, AVG(rating) as avg_rating
FROM `bionic-slate-272814.Amazon_dataset.amazon_products` 
GROUP BY category
ORDER BY avg_rating DESC
limit 1;