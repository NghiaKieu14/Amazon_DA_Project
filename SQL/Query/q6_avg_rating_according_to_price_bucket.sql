SELECT price_bucket, avg(rating) as avg_rating
FROM `bionic-slate-272814.Amazon_dataset.amazon_products` 
GROUP BY price_bucket
ORDER BY avg_rating DESC
