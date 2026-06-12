SELECT product_name, rating_count 
FROM `bionic-slate-272814.Amazon_dataset.amazon_products`
ORDER BY rating_count DESC
LIMIT 10