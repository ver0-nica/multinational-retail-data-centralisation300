WITH store_orders AS(
  SELECT dim_products.product_price,
         orders_table.product_quantity,
         orders_table.store_code
  FROM dim_products
  INNER JOIN orders_table 
    ON orders_table.product_code = dim_products.product_code)
	
SELECT dim_store_details.store_type,
       ROUND(SUM(store_orders.product_quantity * store_orders.product_price)::numeric, 2) AS total_sales
FROM store_orders, dim_store_details
WHERE store_orders.store_code = dim_store_details.store_code
GROUP BY dim_store_details.store_type
ORDER BY total_sales DESC;