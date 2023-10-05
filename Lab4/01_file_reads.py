#Example:  L_2.3 ex1

import io
import pandas as pd
import requests as r

#variables needed for ease of file access
url = 'http://drd.ba.ttu.edu/isqs3358/ex/L2.0/'
path = '/home/isqsdac/'
file_1 = 'test_data.csv' #http://drd.ba.ttu.edu/isqs3358/ex/L2.3/test_data.csv
file_2 = 'test_data_pipe.csv'
file_out = 'outfile.csv'

###############################################################################
#                        Basic File Read From Local                           #
###############################################################################

#download file first for example.
df = pd.read_csv(path + file_1)  
df

###############################################################################
#                      File Read direct from Web Request                      #
###############################################################################

res = r.get(url + file_1)
res.status_code
df = pd.read_csv(io.StringIO(res.text))  
df


###############################################################################
#               Basic File Read From Local /w diff delim                      #
###############################################################################

#WAit!  What happened???
res = r.get(url + file_2)
res.status_code
df = pd.read_csv(io.StringIO(res.text))  
df

#check the file
#Test the delimiter
df = pd.read_csv(io.StringIO(res.text), delimiter='|')  
df

###############################################################################
#                             File write output                               #
###############################################################################

#Note, the number of columns to column headers....what is wrong?
df.to_csv(path + file_out)

#Let's remove the row index and change the delimiter to pipes
df.to_csv(path + file_out, sep='|', index=False)

####Note the documentation for Line terminators
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html
#Issue when translation between OSes
