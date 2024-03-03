UPDATE dim_products
SET product_price = REPLACE(product_price, '£', '');