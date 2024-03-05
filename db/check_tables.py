# from app.db import db 
# import pyodbc

import pyodbc
cnxn_str = ("Driver={SQL Server Native Client 11.0};"
            "Server=auspwdgadb05.aus.amer.dell.com;"
            "Database=Working_db;"
            "Trusted_Connection=yes;")

conn = pyodbc.connect(cnxn_str)


cur = db.conn.cursor();

def check_tables():
    try:
        cur.execute('SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES')
        expected_tables = {'users', 'products', 'orders'}
        existing_tables = {row[0] for row in cur.fetchall()}

        missing_tables = expected_tables - existing_tables

        if missing_tables:
            for table in missing_tables:
                globals()[table]()
                db.conn.commit()  # Commit changes after creating each table

    except pyodbc.Error as e:
        print(f"An error occurred while creating tables: {e}")
    finally:
        cur.close()

def products():
    cur.execute("""
        IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[products]') AND type in (N'U'))
        BEGIN
            CREATE TABLE products (
                id INT PRIMARY KEY IDENTITY(1,1),
                name VARCHAR(255) NOT NULL,
                description VARCHAR(255) NOT NULL,
                stock INT NOT NULL,
                price INT NOT NULL
            )
        END
    """)

def users():
    cur.execute("""
        IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[users]') AND type in (N'U'))
        BEGIN
            CREATE TABLE users (
                id INT PRIMARY KEY IDENTITY(1,1),
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                address TEXT,
                mobile VARCHAR(10) NOT NULL
            )
        END
    """)

def orders():
    cur.execute("""
        IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[orders]') AND type in (N'U'))
        BEGIN
            CREATE TABLE orders (
                id INT PRIMARY KEY IDENTITY(1,1),
                user_id INT NOT NULL,
                product_id INT NOT NULL,
                order_quantity INT NOT NULL,
                total_price INT NOT NULL
            )
        END
    """)