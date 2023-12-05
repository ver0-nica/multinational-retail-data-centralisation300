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
    
    def clean_card_data(self, card_df):
        pd.to_datetime(card_df.date_payment_confirmed, format='mixed', errors='coerce')
        pd.to_datetime(card_df.expiry_date, format='mixed', errors='coerce')
        card_df = card_df.dropna()
        return card_df
    
    def clean_store_data(self,store_df):
        store_df['address'] = store_df['address'].replace({r'\n':', '}, regex=True)
        pd.to_numeric(store_df.longitude, errors='coerce')
        pd.to_numeric(store_df.lat, errors='coerce')
        pd.to_numeric(store_df.latitude, errors='coerce')
        pd.to_numeric(store_df.staff_numbers, errors='coerce')
        pd.to_datetime(store_df.opening_date, errors='coerce')
        store_df = store_df.dropna()
        return store_df
    
    def convert_products_weight(self, products_df):
        products_df['weight'].dropna()   
        for item in products_df['weight']:
            item = str(item)  

        for item in products_df['weight']:
            
            if item == float:
                item = None
            elif 'kg' in item:
                index = item.index('k')
                item = item[:index]
                item = float(item)
            elif 'g' in item:
                index = item.index('g')
                item = item[:index]
                item = float(item)
                item = item / 1000
            elif 'ml' in item:
                index = item.index('m')
                item = item[:index]
                item = float(item)
                item = item / 1000
        
        products_df['weight'].dropna() 
        
        return products_df

    def clean_products_data(self, products_df):
        pd.to_datetime(products_df.date_added, format='mixed', errors='coerce')
        products_df = products_df.dropna()
        return products_df
    
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

