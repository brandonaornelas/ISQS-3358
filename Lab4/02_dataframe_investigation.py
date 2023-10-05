#Example:  L_2.3 ex2


import io
import pandas as pd
import requests as r

#variables needed for ease of file access
url = 'http://drd.ba.ttu.edu/isqs3358/ex/L2.0/'
file_1 = 'test_data.csv'

###############################################################################
#                      File Read direct from Web Request                      #
###############################################################################

res = r.get(url + file_1)
res.status_code
df = pd.read_csv(io.StringIO(res.text))  
df

# Examine first 5 records
df.head(5)

# Examine last 5 records
df.tail(5)

# basic description of dataset, does not do nominal data
df.describe()

#Individual calls
df.mean()
df.median()
df.std()
df.var()

#running method on individual variable
df['Continuous'].describe()

#frequency table
df['Nominal'].value_counts()

#compute correlation
df.corr()

#histogram of all numerics
df.hist()

#scatter matrix
pd.plotting.scatter_matrix(df)

#Report Row Count
df.count()

#report column names
df.columns

#Iterate on rows (note the need for two items in looop)
for index, row in df.iterrows():
    print(row)
    #break
    
