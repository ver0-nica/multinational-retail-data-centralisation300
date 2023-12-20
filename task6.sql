WITH product_orders AS(
  SELECT dim_products.product_price,
         orders_table.product_quantity,
         orders_table.date_uuid
  FROM dim_products
  INNER JOIN orders_table 
    ON orders_table.product_code = dim_products.product_code)
	
SELECT ROUND(SUM(product_orders.product_quantity * product_orders.product_price)::numeric, 2) AS total_sales,
       dim_date_times.year,
	   dim_date_times.month
FROM product_orders, dim_date_times
WHERE product_orders.date_uuid = dim_date_times.date_uuid
GROUP BY dim_date_times.month, dim_date_times.year
ORDER BY total_sales DESC
LIMIT 10;