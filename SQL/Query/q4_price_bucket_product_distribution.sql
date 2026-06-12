SELECT price_bucket, Count(price_bucket) as product_count
FROM `bionic-slate-272814.Amazon_dataset.amazon_products` 
GROUP BY price_bucket
ORDER BY product_count DESC