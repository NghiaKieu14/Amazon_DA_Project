SELECT product_name, discounted_price, actual_price, savings
FROM `bionic-slate-272814.Amazon_dataset.amazon_products`
ORDER BY savings desc
LIMIT 1