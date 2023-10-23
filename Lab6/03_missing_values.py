#Example:  Lecture 2.4:  Example Missing Values

import io
import pandas as pd
import requests as r
import datetime as dt

#variables needed for ease of file access
url = 'http://drd.ba.ttu.edu/isqs3358/ex/L2.2/'
file_1 = 'employment_missing.csv'
file_2 = 'job_title_missing.csv'
file_3 = 'stock.csv'

#pull employment
res = r.get(url + file_1)
res.status_code
df_emp = pd.read_csv(io.StringIO(res.text)) 

#pull job
res = r.get(url + file_2)
res.status_code
df_job = pd.read_csv(io.StringIO(res.text)) 

#pull stock data
res = r.get(url + file_3)
df_stock = pd.read_csv(io.StringIO(res.text), delimiter='|')


###############################################################################
#                  Let's inspect the dataset with replace val                 #
###############################################################################

#Let's look at our dataset....seems resonable
df_emp.head()

#Let's look at the count
#Note the odd/different values
df_emp.count()

#How to fix salary......suggestions?
#These will be basic options.  Note, you can always use the apply
#function to update the values using more robust methods found in
#your other stats classes.

#Identify the "not" nas....
df_emp[df_emp['salary'].notna()]

#how about the nas
df_emp[df_emp['salary'].isnull()]

#Let's fill in with 0's
df_emp['salary'].fillna(0, inplace=True)
df_emp.count()

#That is great, but we have other info to derive an average
#recall we have average salary in job file.
#reset our dataframe
res = r.get(url + file_1)
res.status_code
df_emp = pd.read_csv(io.StringIO(res.text)) 

#Let's populate via the average
#bit brute force, but gets the job done
for index, row in df_job.iterrows():
        df_emp['salary'][(df_emp['jobtitleid'] == row['jobtitleid']) & (df_emp['salary'].isnull())] = row['avg_salary']

df_emp.count()

#Let's look at a slightly nicer way of doing what we just did.

#reset the dataframe
res = r.get(url + file_1)
res.status_code
df_emp = pd.read_csv(io.StringIO(res.text)) 

for index, row in df_emp.iterrows():
    if pd.isna(df_emp.at[index, 'salary']):
        df_emp.at[index, 'salary'] = df_job['avg_salary'][df_job['jobtitleid']==row['jobtitleid']]

#What is the major difference between the last 2 blocks of code.  
#How are they operating differently?
        
#Let's do one more example.  i.e. what happens if we don't have the average
#already computed???  Or if we want to join the sets then do an update?
#Effectively, this is the equivalent to an update join from SQL.

#Let's reset the files
res = r.get(url + file_1)
res.status_code
df_emp = pd.read_csv(io.StringIO(res.text))       

#Let's do a groupby with the job id:

job_avg_salary_df = df_emp[['jobtitleid', 'salary']].groupby('jobtitleid').mean()
job_avg_salary_df.rename(columns = {'salary' : 'avg_job_salary'}, inplace=True)
print(job_avg_salary_df)

#Let's do a join, but remember, jobtitleid in job_avg_salary_df is in the index
#how do we reference this???
df_emp_merge = df_emp.merge(job_avg_salary_df, left_on='jobtitleid', right_index=True)

#Now, let's update by a value in the same dataframe if the value is null.
df_emp_merge['salary'][df_emp_merge['salary'].isna()] = df_emp_merge['avg_job_salary']

#Let's resort by index
df_emp_merge.sort_index(inplace=True)

#Note, this last example is the best for performance, but perhaps not the most 
#straight forward.

###############################################################################
#                            Join Issues - Missing Key                        #
###############################################################################

#Let's join our files
dfmerged = df_emp.merge(df_job, how='inner', on='jobtitleid')
dfmerged.head()

#let's look at count
dfmerged.count()
#where are our rows???? 80 vs 99.  note our join type
dfmerged = df_emp.merge(df_job, how='left', on='jobtitleid')
dfmerged.count()

#so what happened?
#Let's update with an "other" option.  0 for average age and salary
dfmergedcln = dfmerged.fillna({'jobtitleid' : -1, 'jobtitle':'other', 'avg_salary':0, 'avg_age':0})
dfmergedcln.count()

#Note, the prior example has us update values "hardcoded"
#in practice, it may be better to add that row to the job file,
#add our 'dummy' job titleid to our file
#then remerge.  It may save potential errors in keying in data.


###############################################################################
#                  Missing Consecutive Values - Stocks                        #
###############################################################################

#Let's look at a stock value
#do we see any missing values?
print(df_stock)

df_stock['Date'] = pd.to_datetime(df_stock['Date'])
mindate = df_stock['Date'].min()
days_between = (df_stock['Date'].max() - mindate).days

#let's add weekends
for i in range(0, days_between):
    dateval = mindate + dt.timedelta(days=i)

    if not df_stock['Date'].isin([dateval]).any().any():
        df_stock = df_stock.append({'Date':dateval}, ignore_index=True)

#Let's sort by date
df_stock = df_stock.sort_values('Date')

#whoops, it did it but didn't persist it
df_stock.ffill(axis=0)    
    
#now done in place
df_stock.ffill(axis=0,inplace=True)    
    
    
    
    
    
    