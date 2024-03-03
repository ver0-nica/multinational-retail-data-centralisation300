import pandas as pd
#from database_utils import DatabaseConnector
import tabula
import requests
import boto3

class DataExtractor:
    def read_rds_table(self, connector, table_name):
        tables = connector.list_db_tables()
        index = tables.index(table_name)
        df = pd.read_sql_table(tables[index], connector.init_db_engine())
        return df
    
    def retrieve_pdf_data(self, url):
        pdf_data = tabula.read_pdf(url, force_subprocess=True, multiple_tables=True, pages="all", lattice=True) #create a file to be uploaded on a Pandas DataFrame
        df = pd.concat(pdf_data) #upload the file on a pandas dataframe
        return df

    def list_number_of_stores(self, number_of_stores_endpoint, header_dictionary):
        response = requests.get(number_of_stores_endpoint, headers=header_dictionary)
        if response.status_code == 200:
            data = response.json()
            return data['number_stores']
        else:
            print(f"Request failed with status code: {response.status_code}")
            print(f"Response Text: {response.text}")
    
    def retrieve_stores_data(self, retrieve_a_store_endpoint, header_dictionary):
        response = requests.get(retrieve_a_store_endpoint, headers=header_dictionary)
        if response.status_code == 200:
            data = response.json()
            df = pd.DataFrame(data, index=[0])
            return(df)
        else:
            print(f"Request failed with status code: {response.status_code}")
            print(f"Response Text: {response.text}")

    def extract_from_s3(self, address):
        s3 = boto3.client('s3')
        df = pd.read_csv(address)
        return df





        




