import io
import pandas as pd
import requests as r

#variables needed for ease of file access
url = 'http://drd.ba.ttu.edu/isqs3358/ex/L2.1/'
file_1 = 'test_data.csv'

###############################################################################
#                      File Read direct from Web Request                      #
###############################################################################

res = r.get(url + file_1)
res.status_code
df = pd.read_csv(io.StringIO(res.text))  
df

###############################################################################
#                             Column Encoding                                 #
###############################################################################

#let's just add a column, all values are 100
df['100_col'] = 100

#Let's scale our 7 pt likert to a 100 point scale.
#why we would do this, I have no idea.

df['likert_100'] = 100/df['Ordinal_7pt']


#What about iterative operations, Why didn't this work?
for index, row in df.iterrows():
    row['iterval'] = row['Ordinal_7pt'] + row['Ordinal_5pt']

df

#Note, we will talk about how to do more custom row actions later.
#for now, note, that iterrows really should not be used for updating values.

###############################################################################
#                           Column Translation                                #
###############################################################################

#Let's encode all ordinal 7 values above 4 as High and otherwise low

#set the default value
df['7highlow'] = 'low'
#set the other value
df['7highlow'][df['Ordinal_7pt'] > 4] = 'high'
#note the warning.  While it works, there are better ways
df

###############################################################################
#                            Drop a column                                    #
###############################################################################

df.columns
df1 = df.drop('7highlow', axis=1) #axis specifies column
df1
#note, this created a new copy.  Higher memory usage.  
#Instead try the following
df
df.drop('7highlow', axis=1, inplace=True)
df

###############################################################################
#                           String Access                                     #
###############################################################################

df['Nominal']

#Let's access the first character:
df['Nominal'].str[0]

#How let's change casing:
df['Nominal'].str.lower()
df['Nominal'].str.upper()
