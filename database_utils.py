import yaml
from sqlalchemy import create_engine
from sqlalchemy import inspect
import pandas as pd
import psycopg2

class DatabaseConnector:
    def __init__(self, filepath):

        self.filepath = filepath
 
    def read_db_creds(self):
        with open(self.filepath) as creds:
            data = yaml.safe_load(creds)
            credentials = dict(data)
        return credentials    
    
    def init_db_engine(self):
        credentials = self.read_db_creds()
        DATABASE_TYPE = 'postgresql'
        DBAPI = 'psycopg2'
        HOST = credentials['HOST']
        USER = credentials['USER']
        PASSWORD = credentials['PASSWORD']
        DATABASE = credentials['DATABASE'] 
        PORT = credentials['PORT']
        engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")
        return engine
    
    def list_db_tables(self):
        engine = self.init_db_engine()
        engine.connect()
        inspector = inspect(engine)
        return inspector.get_table_names()
    
    def upload_to_db(self, pandas_df, table_name):
        engine = self.init_db_engine()
        conn = engine.connect()
        pandas_df = pandas_df.to_sql(table_name, conn, if_exists = 'replace')
        return pandas_df
        
#filepath = 'db_creds.yaml'
#instance = DatabaseConnector(filepath)
#instance.read_db_creds()
#instance.init_db_engine()
#print(instance.list_db_tables())



        
        
