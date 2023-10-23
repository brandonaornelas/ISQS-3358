import io
import pandas as pd
import requests as r

#variables needed for ease of file access
url = 'http://drd.ba.ttu.edu/isqs3358/ex/L2.1/'
file_1 = 'test_data_bad.csv'

###############################################################################
#                      File Read direct from Web Request                      #
###############################################################################

res = r.get(url + file_1)
res.status_code
df = pd.read_csv(io.StringIO(res.text))  
df

###############################################################################
#                        Let's examine the data types                         #
###############################################################################

#why am I missing fields?
df.describe()
df.dtypes


###############################################################################
#                        Let's look at a bad read                             #
###############################################################################

res = r.get(url + file_1)
res.status_code
df = pd.read_csv(io.StringIO(res.text))  

#why are numericals coming up objects?
df.dtypes

#Let's enumerate the items, note the "a" value
df['Ordinal_7pt'].value_counts()
df['Ordinal_5pt'].value_counts()

#For now, let's take the easy route and just drop the rows.  Note it is 
#row #0 and row # 49
df.drop(0, axis=0, inplace=True)
df.drop(49, axis=0, inplace=True)
df

#WAIT, WHY ON EARTH DID THAT WORK?  Deleted 0 and index didn't shift?????
#Let's reset the index
df.reset_index(drop=True, inplace=True)
df

###############################################################################
#                         How do we change data types?                        #
###############################################################################
df.dtypes
#we fixed the offending values, but our type is wrong.
#Let's type conver those fields

df['Ordinal_7pt'] = pd.to_numeric(df['Ordinal_7pt'])
df['Ordinal_5pt'] = pd.to_numeric(df['Ordinal_5pt'])

#Types look good
df.dtypes

#Now we can describe!
df.describe()







