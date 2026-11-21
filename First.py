import pandas as pd;
dict1={
    "name":["anu","sikha","arya","swati"],
    "marks":[56,78,90,100],
    "city":["unnao","kanpur","lko","mau"]
}
df=pd.DataFrame(dict1)
print(df);
#df.to_csv("frnds.csv")
df.to_csv("frnd_inx_false.csv",index=False);
fd=pd.read_csv("orders.csv");
print(fd);
print(fd.head(10))
print(fd.tail(10))
print(fd[6:13]);
print(fd.dtypes)
print(fd.describe())
