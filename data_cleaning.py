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
        unique_values = ['Diners Club / Carte Blanche', 'American Express', 'JCB 16 digit', 'JCB 15 digit', 'Maestro', 'Mastercard', 'Discover', 'VISA 19 digit', 'VISA 16 digit', 'VISA 13 digit']
        card_df = card_df[card_df['card_provider'].isin(unique_values)]
        
        pd.to_datetime(card_df.date_payment_confirmed, format='mixed', errors='coerce')
        pd.to_datetime(card_df.expiry_date, format='mixed', errors='coerce')
        card_df = card_df.dropna()
        return card_df
    
    def clean_store_data(self,store_df):
        unique_values = ['Local', 'Outlet', 'Mall Kiosk', 'Super Store']
        store_df = store_df[store_df['store_type'].isin(unique_values)]

        store_df['address'] = store_df['address'].replace({r'\n':', '}, regex=True)

        digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        for item in store_df['staff_numbers']:
            for i in range(len(item)):
                if item[i] not in digits:
                    new_item = item.replace(item[i], '')
                    store_df['staff_numbers'] = store_df['staff_numbers'].replace(item, new_item, regex=True)


    
        pd.to_datetime(store_df.opening_date, errors='coerce')

        continents = ['Europe', 'America']
        for item in store_df['continent']:
            if item not in continents:
                if item == 'eEurope' or item == 'eeEurope':
                    new_item = 'Europe' 
                    store_df['continent'] = store_df['continent'].replace(item, new_item, regex=True)
                if item == 'eeAmerica':
                    new_item = 'America'
                    store_df['continent'] = store_df['continent'].replace(item, new_item, regex=True)
        return store_df
    
    def convert_products_weight(self, products_df):
       
        unique_values = ['food-and-drink', 'toys-and-games', 'homeware', 'sports-and-leisure', 'diy', 'pets', 'health-and-beauty']
        products_df = products_df[products_df['category'].isin(unique_values)]

        products_df['weight'].dropna()

        for item in products_df['weight']:
               
            if 'kg' in item:
                index = item.index('k')
                new_item = item[:index]
                if 'x' in new_item:
                    x_index=new_item.index('x')
                    a = new_item[:x_index]
                    b = new_item[x_index+1:]
                    a = float(a)
                    b = float(b)
                    new_item = a * b 
                new_item = float(new_item)    
                products_df['weight'] = products_df['weight'].replace(item, new_item, regex=True)
                
            elif 'g' in item:
                index = item.index('g')
                item = item[:index]
                new_item = item[:index]
                if 'x' in new_item:
                    x_index=new_item.index('x')
                    a = new_item[:x_index]
                    b = new_item[x_index+1:]
                    a = float(a)
                    b = float(b)
                    new_item = a * b 

                new_item = float(new_item)
                new_item = new_item / 1000
                products_df['weight'] = products_df['weight'].replace(item, new_item, regex=True)

            elif 'ml' in item:
                index= item.index('m')
                new_item = item[:index]
                if 'x' in new_item:
                    x_index=new_item.index('x')
                    a = new_item[:x_index]
                    b = new_item[x_index+1:]
                    a = float(a)
                    b = float(b)
                    new_item = a * b 
                
                new_item = float(new_item)
                new_item = new_item / 1000                
                products_df['weight'] = products_df['weight'].replace(item, new_item, regex=True)

            elif 'oz' in item:
                index= item.index('o')
                new_item = item[:index]
                if 'x' in new_item:
                    x_index=new_item.index('x')
                    a = new_item[:x_index]
                    b = new_item[x_index+1:]
                    a = float(a)
                    b = float(b)
                    new_item = a * b 
                
                new_item = float(new_item)
                new_item = new_item / 35                
                products_df['weight'] = products_df['weight'].replace(item, new_item, regex=True)
        
        products_df['weight'].dropna() 
        
        return products_df

    def clean_products_data(self, products_df):
        pd.to_datetime(products_df.date_added, format='mixed', errors='coerce')
        products_df = products_df.dropna()
        return products_df
    
    def clean_orders_data(self, orders_df):
        #/orders_df.dropna(inplace=True)
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

        pd.to_numeric(date_df.month, errors='coerce')
        unique_values = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        date_df = date_df[date_df['month'].isin(unique_values)]
        
        pd.to_timedelta(date_df.timestamp, errors='coerce')
        
        pd.to_numeric(date_df.year, errors='coerce')
        pd.to_numeric(date_df.day, errors='coerce')
        date_df.dropna(inplace=True)
        return date_df

