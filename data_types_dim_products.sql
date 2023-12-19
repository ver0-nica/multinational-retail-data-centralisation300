ALTER TABLE dim_products
ALTER COLUMN product_price TYPE FLOAT USING product_price::double precision;

ALTER TABLE dim_products
ALTER COLUMN weight TYPE FLOAT USING product_price::double precision;

ALTER TABLE dim_products
ALTER COLUMN "EAN" TYPE VARCHAR(17);

ALTER TABLE dim_products
ALTER COLUMN product_code TYPE VARCHAR(11);

ALTER TABLE dim_products
ALTER COLUMN date_added TYPE DATE USING date_added::date;

ALTER TABLE dim_products
ALTER COLUMN "uuid" TYPE UUID USING "uuid"::uuid; 

ALTER TABLE dim_products
ALTER COLUMN weight_class TYPE VARCHAR(15);

ALTER TABLE dim_products
RENAME removed TO still_available;

UPDATE dim_products
SET still_available = 'True'
WHERE still_available = 'Still_avaliable';

UPDATE dim_products
SET still_available = 'False'
WHERE still_available = 'Removed';

ALTER TABLE dim_products
ALTER COLUMN still_available TYPE BOOL USING still_available::bool;
