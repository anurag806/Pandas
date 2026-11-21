import pandas as pd
from lark.parse_tree_builder import inplace_transformer

df = pd.DataFrame({
    'emp_id': [101, 102, 103, 104, 105],
    'name': ['Amit', 'Priya', 'Rahul', 'Sneha', 'Vikram'],
    'dept': ['IT', 'HR', 'IT', 'Finance', 'HR'],
    'salary': [60000, 45000, 75000, 52000, 48000]
})
print(df);
df.info();
print(df.shape);
ab=pd.read_csv("C:/Users/anura/Downloads/customers-10000.csv")
#print(ab)
print(ab.head());
print(ab["Index"])
print(ab[['Customer Id','Index']])
abc=pd.read_csv("orders.csv")
print(abc.columns);
print(abc[['order_id','sales']])
print(abc.rename(columns={'order_id':'id','sales':'sale'}))
# creating new data frame from old one
abc_new=abc[['order_id','sales']]
print(abc_new)
print(type(abc_new))
# selecting from the rows iloc showing from row index
print(abc.iloc[5:10]);
# here we can select also columns
print(abc.iloc[[2,4,7,9],2:6])
# setting up index to any other columns
print(abc)
abc.set_index('order_id',inplace=True);
print(abc);
print(abc.loc['CA-2019-115742']);
