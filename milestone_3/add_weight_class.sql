ALTER TABLE dim_products
ADD COLUMN weight_class VARCHAR(15);

UPDATE dim_products
SET weight_class = 'Light'
WHERE weight < 2;

UPDATE dim_products
SET weight_class = 'Mid_Sized'
WHERE weight >= 2 and weight < 40;

UPDATE dim_products
SET weight_class = 'Heavy'
WHERE weight >= 40 and weight < 140;

UPDATE dim_products
SET weight_class = 'Truck_Required'
WHERE weight >= 140;