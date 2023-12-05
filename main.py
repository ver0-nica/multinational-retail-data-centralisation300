from database_utils import DatabaseConnector
from data_extraction import DataExtractor
from data_cleaning import DataCleaning
#from sqlalchemy import create_engine
from header_details import header_details
import pandas as pd

filepath = 'db_creds.yaml'
connector = DatabaseConnector(filepath)
extractor = DataExtractor()
db = extractor.read_rds_table(connector,'legacy_users')

cleaner = DataCleaning()
clean_data = cleaner.clean_user_data(db)

my_filepath = 'my_creds.yml'
my_connector = DatabaseConnector(my_filepath)

#my_connector.upload_to_db(clean_data, 'dim_users')

#card_data = extractor.retrieve_pdf_data('https://data-handling-public.s3.eu-west-1.amazonaws.com/card_details.pdf')
#card_data_cleaned = cleaner.clean_card_data(card_data)
#my_connector.upload_to_db(card_data_cleaned, 'dim_card_details')

number_of_stores_endpoint = 'https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/number_stores'
number_of_stores = extractor.list_number_of_stores(number_of_stores_endpoint, header_details)
#print(number_of_stores)

stores_dataframe = pd.DataFrame()
for i in range(number_of_stores):
    store_endpoint_i = f'https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details/{i+1}'
    stores_dataframe_i = extractor.retrieve_stores_data(store_endpoint_i, header_details)
    stores_dataframe = pd.concat([stores_dataframe,stores_dataframe_i])
    print(i)

#print(stores_dataframe.info())


stores_dataframe_cleaned = cleaner.clean_store_data(stores_dataframe)
#print(stores_dataframe_cleaned.info())
my_connector.upload_to_db(stores_dataframe_cleaned, 'dim_store_details')

#products_address = 's3://data-handling-public/products.csv'
#products_dataframe = extractor.extract_from_s3(products_address)
#cleaner.convert_products_weight(products_dataframe)
#print(products_dataframe['weight'])
#products_dataframe = cleaner.clean_products_data(products_dataframe)
#my_connector.upload_to_db(products_dataframe, 'dim_products')

#print(connector.list_db_tables())
#orders_df = extractor.read_rds_table(connector, 'orders_table')
#orders_df = cleaner.clean_orders_data(orders_df)
#print(orders_df)
#my_connector.upload_to_db(orders_df, 'orders_table')

#date_address = 'https://data-handling-public.s3.eu-west-1.amazonaws.com/date_details.json'
#date_dataframe = pd.read_json(date_address)
#date_dataframe = cleaner.clean_date_data(date_dataframe)
#my_connector.upload_to_db(date_dataframe, 'dim_date_times')

