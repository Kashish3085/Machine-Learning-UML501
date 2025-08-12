# Q 2.1 Creating a Dataset
# Assignment 2

import pandas as pd
data = {
    'Tid': [1,2,3,4,5,6,7,8,9,10],
    'Refund': ["Yes","No","No","Yes","No","No","Yes","No","No","No"],
    'Marital Status': ["Single","Married","Single","Married","Divorced","Married","Divorced","Single","Married","Single"],
    'Taxable Income': [125000,100000,70000,120000,95000,60000,220000,85000,75000,90000],
    'Cheat': ['No','No','No','No','Yes','No','No','Yes','No','Yes']}
df = pd.DataFrame(data)
print(df,"\n")

# 2.2

s= df.iloc[[0,4,7,8]]
print(s,"\n")

# 2.3

r1= df.iloc[3:8]
r2= df.iloc[4:9, 2:5]
r3= df.iloc[:, 1:4]
print(r1,"\n")
print(r2,"\n")
print(r3,"\n")