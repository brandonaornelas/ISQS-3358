import pandas as pd
import io
import requests as r
import matplotlib.pyplot as plt

url = 'http://drd.ba.ttu.edu/isqs3358/ex/L2.0/'
file = 'test_data.csv'


res = r.get(url + file)
status = res.status_code
df = pd.read_csv(io.StringIO(res.text))

"""
print(df.head(5))
print()
print(df.tail(5))
print()
"""
#print(df.describe())

#print(df['RecordId'].mean())
#print(df['Continuous'].describe())
#print(df.min())
#print(df.var())

#print(df['Continuous'].corr(df['RecordId']))

#print(df['RecordId'].hist())

#pd.plotting.scatter_matrix(df)

#plt.show()

#for index, row in df.iterrows():
#    print(row)