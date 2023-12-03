import pandas as pd
import numpy as np

class DataCleaning:    

    def clean_user_data(self, db):
        pd.to_datetime(db.date_of_birth, format='mixed', errors='coerce')
        
        db = db.drop_duplicates()
    
    
        db['address'] = db['address'].replace({r'\n':', '}, regex=True)
                  
        db['phone_number'] = db['phone_number'].replace({r'\+44': '0', r'\(':'', r'\)': '', r'\.': '', r' ': ''}, regex=True)
        db['phone_number'] = db['phone_number'].replace({r'00':'0'}, regex=True)
        regex_expression = '^(?:(?:\(?(?:0(?:0|11)\)?[\s-]?\(?|\+)44\)?[\s-]?(?:\(?0\)?[\s-]?)?)|(?:\(?0))(?:(?:\d{5}\)?[\s-]?\d{4,5})|(?:\d{4}\)?[\s-]?(?:\d{5}|\d{3}[\s-]?\d{3}))|(?:\d{3}\)?[\s-]?\d{3}[\s-]?\d{3,4})|(?:\d{2}\)?[\s-]?\d{4}[\s-]?\d{4}))(?:[\s-]?(?:x|ext\.?|\#)\d{3,4})?$'
        db.loc[~db['phone_number'].str.match(regex_expression), 'phone_number'] = np.nan
        
        pd.to_datetime(db.join_date, format='mixed', errors='coerce')
        
        db = db.dropna()
        return db        
    
    def clean_card_data(self, data):
        pd.to_datetime(data.date_payment_confirmed, format='mixed', errors='coerce')
        pd.to_datetime(data.expiry_date, format='mixed', errors='coerce')
        data = data.dropna()
        return data
    
    def clean_store_data(self,data):
        data['address'] = data['address'].replace({r'\n':', '}, regex=True)
        pd.to_datetime(data.opening_date, format='mixed', errors='coerce')
        data = data.dropna()
        return data
    
    def convert_products_weight(self, products_dataframe):
        #digits = [1,2,3,4,5,6,7,8,9]
        products_dataframe['weight'].dropna()
        for item in products_dataframe['weight']:
            print(len(item))
            #for i in range(len(item)):
                #if item[i] not in digits:
                    #item.split(item[i])
        return products_dataframe

    def clean_products_data(self, products_dataframe):
        pd.to_datetime(products_dataframe.date_added, format='mixed', errors='coerce')
        products_dataframe = products_dataframe.dropna()
        return products_dataframe
    
    def clean_orders_data(self, orders_df):
        orders_df.dropna(inplace=True)
        pd.to_datetime(orders_df.date_uuid, format='mixed', errors='coerce')
        orders_df = orders_df.drop_duplicates()
        orders_df.drop('1', axis=1, inplace=True, errors='coerce')
        orders_df.drop('level_0', axis=1, inplace=True, errors='coerce')
        orders_df.drop('first_name', axis=1, inplace=True, errors='coerce')
        orders_df.drop('last_name', axis=1, inplace=True, errors='coerce')
        return orders_df
    
    def clean_date_data(self,date_df):
        date_df.dropna(inplace=True)
        date_df.drop_duplicates(inplace=True)
        pd.to_timedelta(date_df.timestamp, errors='coerce')
        pd.to_numeric(date_df.month, errors='coerce')
        pd.to_numeric(date_df.year, errors='coerce')
        pd.to_numeric(date_df.day, errors='coerce')
        date_df.dropna(inplace=True)
        return date_df

