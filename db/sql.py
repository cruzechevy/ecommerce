import pyodbc
cnxn_str = ("Driver={SQL Server Native Client 11.0};"
            "Server=auspwdgadb05.aus.amer.dell.com;"
            "Database=Working_db;"
            "Trusted_Connection=yes;")

cnxn = pyodbc.connect(cnxn_str)
cursor = cnxn.cursor()
  

print(cursor.execute("Select top 10 * from ABU_AMER_SKU"))
cnxn.commit()
