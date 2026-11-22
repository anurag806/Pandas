import pandas as pd
from sqlalchemy import create_engine,URL
connection_url=URL.create(
    drivername='mysql+pymysql',
    username='root',
    password='Anurag@123',
    host='127.0.0.1',
    port=3306,
    database='ecom'
)
engine=create_engine(connection_url)
query='select * from dim_customer';
df=pd.read_sql(query,con=engine)
print(df)
