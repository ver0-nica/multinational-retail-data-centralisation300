WITH store_orders AS(
  SELECT dim_products.product_price,
         orders_table.product_quantity,
         orders_table.store_code
  FROM dim_products
  INNER JOIN orders_table 
    ON orders_table.product_code = dim_products.product_code)
	
SELECT ROUND(SUM(store_orders.product_quantity * store_orders.product_price)::numeric, 2) AS total_sales,
       dim_store_details.store_type,
	   dim_store_details.country_code
FROM store_orders, dim_store_details
WHERE store_orders.store_code = dim_store_details.store_code
GROUP BY dim_store_details.store_type, dim_store_details.country_code
HAVING dim_store_details.country_code = 'DE'
ORDER BY total_sales;