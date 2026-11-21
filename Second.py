import  pandas as pd;
df=pd.read_csv("orders.csv");
print(df);
a=df.set_index('order_id');
print(a);
c=df.reset_index(drop=True);
print(c);
#loc is the for locationa and all
b=a.loc[['CA-2019-115742'],['order_date','profit']];
print(b);
# sorting index
d=df.sort_index()
bc=df.set_index('order_id')
print(bc)
s=bc.sort_index()
print(s);
print(s.index.is_monotonic_increasing)
print(bc.sort_values('profit',ascending=False))
# for two values
print(bc.sort_values(['profit','quantity'],ascending=[False,False]))
#filteration data
print(df['region']=='South')
av=df.loc[df['region']=='South',['order_date','profit','region']]
print(av);
ac=df.loc[(df['region']=='South') & (df['profit']>0)]
print(ac);
ad=df.loc[(df['region']=='South') | (df['profit']>0),['region','profit']]
print(ad)
print(len(ad));
print(
    ((ad['region'] == 'South') | (ad['profit'] > 0)).all()
)
#~ is used for reversed condition
ad = df[~(df['region'] == 'South')]
print(ad)

# data manupluation
#adding column
df['country']='USA'
print(df)
#modifying columns
df['country']='INDIA'
print(df)
#drop columns
df.drop(columns='country',inplace=True)
print(df)
# apply in pandas  apply is use for function
df['category_len']=df['category'].apply(len);
print(df)
def profit_loss(profit):
    if profit > 0:
        return "profit";
    else :
        return "loss";
df['business']=df['profit'].apply(profit_loss);
print(df)
df['category_upper']=df['category'].str.upper();
print(df)