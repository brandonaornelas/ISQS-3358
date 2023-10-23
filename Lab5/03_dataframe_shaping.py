import io
import pandas as pd
import requests as r

#variables needed for ease of file access
url = 'http://drd.ba.ttu.edu/isqs3358/ex/L2.1/'
file_1 = 'employment.csv'

#pull employment
res = r.get(url + file_1)
res.status_code
df_emp = pd.read_csv(io.StringIO(res.text)) 

###############################################################################
#                     Let's select only certain rows                          #
###############################################################################

df_emp.head()

#Notice the index.  Let's pull index 21

df_emp.iloc[21]

#How about several indexes....say 21, 23, 25
df_emp.iloc[[21, 23, 25]]

#How about a range for all items in index 20-29
#Note, top end is not bound inclusive
#Also, reduction in brackets
df_emp.iloc[20:30]


#That's all well and good, but how about something more useful!
#Let's pull everyone over 48 years old
#note, the restatement of the dataframe
df_emp[df_emp['age'] >= 48]

#how about over 48 and salary less than 50K
#wait why doesn't this work?????
df_emp[df_emp['age'] >= 48 & df_emp['salary'] < 50000]

#Check the syntax difference
#also for all those past programmers, note the logical "and" comparison
#is a single &
df_emp[(df_emp['age'] >= 48) & (df_emp['salary'] < 50000)]

#How about the same results with an "or"
df_emp[(df_emp['age'] >= 48) | (df_emp['salary'] < 50000)]

###############################################################################
#                        How to return only certain columns                   #
###############################################################################

#Specify the columns you want
#as we have seen
df_emp['age']

#How about age and salary
df_emp[['age', 'salary']]

#How about returning age, salary, & job title for our previous row filtering
df_emp[['age', 'salary', 'jobtitleid']][(df_emp['age'] >= 48) & (df_emp['salary'] < 50000)]

#Note, the first set of brackets specifies the fields to return.  
#the second specifies the row return criteria.
