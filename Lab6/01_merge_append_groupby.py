#Example:  Lecture 2.4:  Example Joins


import io
import pandas as pd
import requests as r

#variables needed for ease of file access
url = 'http://drd.ba.ttu.edu/isqs3358/ex/L2.2/'
file_1 = 'employment.csv'
file_2 = 'job_title.csv'
file_3 = 'job_title_year.csv'
file_4 = 'job_title_devs.csv'

#pull employment
res = r.get(url + file_1)
res.status_code
df_emp = pd.read_csv(io.StringIO(res.text)) 

#pull job
res = r.get(url + file_2)
res.status_code
df_job = pd.read_csv(io.StringIO(res.text)) 

df_emp.head()
df_job.head()

###############################################################################
#                Basic joins                                                  #
###############################################################################

#Note, could just use "on" rather than left/right on as the field is the same name
df_emp_merge = df_emp.merge(df_job, how="inner", left_on="jobtitleid", right_on="jobtitleid")
df_emp_merge.head()

#Did we lose any data?  i.e.  what is the meaning of an inner join
df_emp_merge['jobtitle'].value_counts()
df_job['jobtitle']

#Let's do a left join
df_emp_merge_left = df_emp.merge(df_job, how='left', on='jobtitleid')
df_emp_merge_left['jobtitle'].value_counts() #wait!  we left join, where's the mungers!

#Time to demo the right join
df_emp_merge_right = df_emp.merge(df_job, how='right', on='jobtitleid')
df_emp_merge_right['jobtitle'].value_counts() #Ahh, so outside is left side of 
#operator and inside is the right side of the operator.

#Wait, why is Munger a "1" on value_counts????
#Answer, we only asked it to count that column
#More on how this can help us later.

###############################################################################
#                               Multikey join                                 #
###############################################################################

#Let's say our employees were only for 2018 and our job title file was
#also keyed to year.  

#Let's get our new job title file
#pull job
res = r.get(url + file_3)
res.status_code
df_job_year = pd.read_csv(io.StringIO(res.text)) 

#Notice the yr and salary increases of 2K
df_job_year

#Let's add a yr field to our emps and make it 2019
df_emp['yr'] = 2019
df_emp.head()

#Now, let's join.  Note, we can't do it on a single field
df_emp_merge_yr = df_emp.merge(df_job_year, how='inner', on=['jobtitleid', 'yr'])
df_emp_merge_yr

#similar logic using left_on, right_on.  
df_emp_merge_yr_lr = df_emp.merge(df_job_year, how='inner', left_on=['jobtitleid', 'yr'], right_on=['jobtitleid', 'yr'])
df_emp_merge_yr_lr

#Note, the order of the fields matters
df_emp_merge_yr_lr2 = df_emp.merge(df_job_year, how='inner', left_on=['yr', 'jobtitleid'], right_on=['jobtitleid', 'yr'])
df_emp_merge_yr_lr2

###############################################################################
#                        Data Appending                                       #
###############################################################################

#let's add a new job title
res = r.get(url + file_2)
res.status_code
df_job_to_append = pd.read_csv(io.StringIO(res.text)) 

print(df_job_to_append)

#option #1:  use loc  (simple & straight forward.  Could easily be in a loop)
df_job_to_append.loc[len(df_job_to_append.index)] = [11, 'Developer L1', 71000, 27]

#option #2:  What if it is an entire new dataframe

#retrieve dataframe of jobs to append
res = r.get(url + file_4)
res.status_code
df_dev_jobs = pd.read_csv(io.StringIO(res.text)) 

print(df_dev_jobs)

#concat the new jobs into the old jobs list.

pd.concat([df_job_to_append, df_dev_jobs], ignore_index=True)
#wait.....where did hte results go???

df_newjob_list = pd.concat([df_job_to_append, df_dev_jobs], ignore_index=True)


###############################################################################
#                               Groupby                                       #
###############################################################################

#Let's produce a group by with position and salary

df_emp_merge[['jobtitle', 'salary']].groupby('jobtitle').mean()

#Note the groupby fieldmust be included in the dataframe column slice
#this shows the error
df_emp_merge[['jobtitle', 'salary']].groupby('jobtitle').mean()

#Let's add an encoded field
df_emp_merge['age_category'] = 'New'
df_emp_merge['age_category'][df_emp_merge['age'] > 25] = 'Middle'
df_emp_merge['age_category'][df_emp_merge['age'] > 40] = 'Senior'

df_emp_merge[['jobtitle', 'salary', 'age_category']].groupby(['jobtitle', 'age_category']).mean()

#To Export to CSV, you must have index=True, otherwise you lose your grouped by fields.