from dotenv import load_dotenv
#import pymysql
import os

# # Load environment variables from a .env file
# load_dotenv()

# # Using environment variables for database connection
# USER = os.getenv('DB_USER')
# HOST = os.getenv('DB_HOST')
# PASSWORD = os.getenv('DB_PASSWORD')

# # Connect to the MySQL database
# conn = pymysql.connect(
#     database="ecommerce",
#     user=USER,
#     password=PASSWORD,
#     host=HOST,
#     port=3306
# )

import pyodbc
cnxn_str = ("Driver={SQL Server Native Client 11.0};"
            "Server=auspwdgadb05.aus.amer.dell.com;"
            "Database=Working_db;"
            "Trusted_Connection=yes;")

conn = pyodbc.connect(cnxn_str)

