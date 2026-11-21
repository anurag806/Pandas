import pandas as pd
df=pd.read_csv('messy_data.csv')
print(df)
#finding missing values
print(df.isnull())
print(df.isnull().sum())
print(df.info())
print(len(df))
print(df.describe())
print(df.dropna())
df.dropna(subset=['City'])
print(df)
print(df.fillna("hii"))
# drop dulpicates
print(df.drop_duplicates())
print(df.drop_duplicates(keep='last'));
print(df.drop_duplicates(subset=['Email','City']));
#date and time
print(pd.to_datetime(df['OrderDate']))
sd=pd.read_csv('orders.csv')
print(sd)
sd['dates']=pd.to_datetime(sd['order_date'],format='%d-%m-%Y')
sd['year']=sd['dates'].dt.year
sd['month']=sd['dates'].dt.month
sd['day']=sd['dates'].dt.day
print(sd['year'])
print(sd['month'])
print(sd['day'])
#filter by dates
sd['filter_dates']=sd['dates']>="01-01-2023"
print(sd['filter_dates'])
#filtering data with dates
q4_orders = sd[
    (sd['dates'] <= pd.Timestamp('2026-10-01'))
]
print(q4_orders)
sd['order_dates']=pd.to_datetime(sd['order_date'],format='%d-%m-%Y')
sd['ship_dates']=pd.to_datetime(sd['ship_date'],format='%d-%m-%Y')
sd['transit_days']=(sd['ship_dates']-sd['order_dates']).dt.days
print(sd)
print(sd.groupby('region')['sales'].sum())
print(sd.groupby(['region','ship_date'])['sales'].mean())
print(sd.groupby('region')['sales'].agg(['max','min']));
print(sd['category'].value_counts())
#merging tables
sd_order=pd.read_csv('orders.csv')
print(sd_order)
sd_return=pd.read_csv('returns.csv')
print(sd_return)
sd_merge=pd.merge(left=sd_order,right=sd_return,how='inner',left_on='order_id',right_on='return_order_id')
print(sd_merge)
d1=pd.DataFrame({
"id": [1, 2, 3],
    "name": ["Ankit", "Sumit", "Amit"],
    "salary": [100, 200, 300]
})
print(d1)
d2=pd.DataFrame({
"id": [4, 5, 6],
    "name": ["Ankita", "Sunny", "Anu"],
    "salary": [800, 700, 600]
})
print(d2)
d3=pd.concat([d1,d2],ignore_index=True)
print(d3)