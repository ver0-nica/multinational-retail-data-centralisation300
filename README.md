# Multinational-Retail-Data-Centralisation300

The first goal of this project is to produce a system that stores some current company data in a database so that it's accessed from one centralised location and acts as a single source of truth for sales data.
After that the database could be query to get up-to-date metrics for the business.

In order to create the database with the correct data we can use three different python files, and each of them describes the methods and attributes of a newly created class.
- In the database_utils.py file is described the DatabaseConnector class. In order to create an instance of this class we just need an instance name and the file path containing the credentials of our project. Then, the read_db_creds method uploads these credentials into a yaml file, and the init_db_engine method creates a database on Postgresql using the same yaml file.
The other two methods of this class are list_of_tables, which returns a list with the names of all the tables in our database; and the upload_to_db method, which takes as arguments a pandas dataframe and a table to upload into.
- data_extraction.py defines the DataExtractor class. The aim of this class is to retreive data from different sources and making them ready to be uploaded into a dataframe. 
  - The read_rds_table method takes an istance of the DatabaseConnector class and a table from the ones retrieved by the same instance. Then, by using methods of the previous class, it creates a pandas dataframe made by the table given.
  - The retreive_pdf_data method takes an URL of a PDF file as argument and creates a pandas dataframe by reading this file.
  - The next two methods are list_number_of_stores and retrieve_store_data and they are used to retrieve data from an API. The first one takes as arguments an endpoint which gives information on the number of stores the company manage, and the header details in the form of a dictionary; then it returns the number if stores to extract. 
  Instead, the retrieve_store_data method takes as arguments the enpoint of a specific store and the same header details and retrieve a dataframe containg the data on the specific store.
  - The last method is extract_from_s3, and retreives data from an AWS S3 taking its address as argument and returning a pandas dataframe.
- Last python file is data_cleaning.py and describes all the methods af the DataCleaning class, which are designed to clean the data retrieved step-by-step for every table of the project.

The last python file is main.py. In this file all the methods are applied to our scenario using the given data.
- Firstly, we create two instance of the DatabaseConnector class: one using the credentials given specifically for this project, and one using the personal credentials of the user. The first connector is used to retrieve the information about the users data and, after having extracted and cleaned this data, the second connector is used to create and store the data on a Postgresql database.
- Then table on the card details is retreived by using the retreive_pdf_data, is cleaned, and uploaded on the same Postgresql database
- Retreiving the data on the stores is a bit more complex. This data is contained in a web API. Using list_number_of_stores we take the number of stores and we use this number to create a loop that retreives the data of each store and concats the data as rows of a dataframe. This dataframe is then cleaned and uploaded on Postsgresql.
- Products data is retreived using the extract_from_s3 method, is cleaned and uploaded on Postgresql.
- Orders data is retreived using the read_rds_table method, is cleaned and uploaded on Postgresql.
- Date/Time data is on a json file, which is used to create a dataframe that then is cleaned and uploaded on Postgresql.

Now all the data is on a relational database on PostgreSQL and we can perform queries to change the datatype of specific column, to add or remove columns, and to retreive information required by our company