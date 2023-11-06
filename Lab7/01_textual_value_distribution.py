import io
import pandas as pd
import requests as r

#variables needed for ease of file access
url = 'http://drd.ba.ttu.edu/isqs3358/ex/L2.3/'
file_1 = 'colors.csv'

#pull employment
res = r.get(url + file_1)
dfcol = pd.read_csv(io.StringIO(res.text)) 

dfcol[dfcol['val'].isna()]

#option 1:  Make an "other" group.  Pick a value that will nto appear and populate

dfcol['val'].fillna('Other-Value Not Found', inplace=True)

dfcol['val'].value_counts()

#Option 2:  Let's sample from a distribution.  Where do we get our distribution?
#From the data we have.  

dfcol = pd.read_csv(io.StringIO(res.text)) 

#note, the to_frame to convert the series to a dataframe.
dfreq = dfcol['val'].value_counts().to_frame()

#random_state is for standardization of the random sample
dfreq.sample(n=1, weights='val')

#Let's loop.
for index, row in dfcol[dfcol['val'].isna()].iterrows():
    dfcol.at[index, 'val'] = dfreq.sample(n=1, weights='val').index.tolist()[0]

dfcol.sort_values(by='IsMissing', ascending=False)


#what is good/bad of each of these methods?
