# Q 2.4 CSV file

import pandas as pd
d = pd.read_csv('iris.csv')
print("\nFirst five rows of Iris dataset:\n",d.head())

#Q.2.5 

s= d.drop(index=4, columns=d.columns[2])
print("\nModified Iris dataset:\n",s)
