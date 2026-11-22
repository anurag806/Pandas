import pandas as pd
from sqlalchemy import true

data = {
    'emp_id': [101, 102, 103, 104, 105, 106, 107, 108],
    'name': ['Amit', 'Rahul', 'Priya', 'Neha',
             'Amit', 'Raj', 'Sneha', 'Rahul'],
    'department': ['IT', 'HR', 'IT', 'Finance',
                   'Finance', 'HR', 'IT', 'HR'],
    'salary': [60000, 45000, 75000, 80000,
               65000, 50000, 90000, 55000],
    'experience': [3, 2, 5, 7, 4, 3, 6, 5],
    'city': ['Delhi', 'Mumbai', 'Delhi', 'Pune',
             'Delhi', 'Mumbai', 'Pune', 'Mumbai']
}

df = pd.DataFrame(data)
print(df)
sd=df[df[('salary')]>60000]
print(sd)
asd=df[(df[('salary')]>40000) & (df[('salary')]<60000)]
print(asd)
three=df[(df['department']=='IT') | (df['department']=='HR')]
print(three)
# second and third largest salary
salary=df['salary'].unique()
salary.sort()
print(salary[-3])
#duplicate names
name=df[df['name'].duplicated(keep=False)];
print(name)
#Sort employees by salary in descending order.
sal=df['salary'].sort_values(ascending=False)
print(sal)
#Find employees having more than 4 years of experience.
sa=df[df['experience']>4]
print(sa)
# Extract employees who belong to Delhi.
emp=df[df['city']=="Delhi"]
print(emp)
#Find the top 3 highest-paid employees.
qw=df.sort_values(by='salary',ascending=False)
print(qw.iloc[0:3])

