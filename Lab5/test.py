import requests as r
import pandas as pd
import io
"""
url = 'http://drd.ba.ttu.edu/isqs3358/ex/L2.1/'
file = 'test_data.csv'

res = r.get(url + file)
#print(res.status_code)
df = pd.read_csv(io.StringIO(res.text))

df['100_col'] = 100

df['likert_100'] = 100/df['Ordinal_7pt']

df['7highlow'] = 'low'
df['7highlow'][df['Ordinal_7pt'] > 4] = 'high'
#print(df)

#df.columns
#df2 = df.drop('7highlow', axis=1, inplace=True)
#print(df2)
"""
"""
url = 'http://drd.ba.ttu.edu/isqs3358/ex/L2.1/'
file = 'test_data_bad.csv'


res = r.get(url + file)
df = pd.read_csv(io.StringIO(res.text))
"""

#print(df.dtypes)
#print(df.describe())
#print(df['Ordinal_7pt'].value_counts())
#print(df['Ordinal_5pt'].value_counts())

#df.drop(0, axis=0, inplace=True)
#df.drop(49, axis=0, inplace=True)
#df.reset_index(drop=True, inplace=True)
#df['Ordinal_7pt'] = pd.to_numeric(df['Ordinal_7pt'])
#df['Ordinal_5pt'] = pd.to_numeric(df['Ordinal_5pt'])
#print(df.dtypes)
#print(df.describe())
#print(df)

#url = 'http://drd.ba.ttu.edu/isqs3358/ex/L2.1/'
#file = 'employment.csv'

#res = r.get(url + file)
#df = pd.read_csv(io.StringIO(res.text))

#print(df.iloc[21])
#print(df.iloc[[21, 23, 25]])
#print(df[df['age'] >= 48])
#print(df[(df['age'] >= 48) & (df['salary'] < 50000)])
#print()
#print(df[(df['age'] >= 48) | (df['salary'] < 50000)])

#print(df[['age', 'salary']][(df['age'] >= 48) & (df['salary'] < 50000)])


