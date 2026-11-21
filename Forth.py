import pandas as pd
import mysql.connector
from pymsgbox import password

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
    password="Anurag@123",
    database="ecom"
)
query='select * from dim_customer'
df=pd.read_sql(query,mydb)
print(df)