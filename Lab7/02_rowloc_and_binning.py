import io
import pandas as pd
import requests as r

url = 'http://drd.ba.ttu.edu/isqs3358/ex/L2.3/'
dtfile = 'test_data.csv'
empfile = 'emplist.csv'

#import datas file
res = r.get(url + empfile)
dfemp = pd.read_csv(io.StringIO(res.text))
res = r.get(url + dtfile)
dfdata = pd.read_csv(io.StringIO(res.text))

###############################################################################

#For specific informatino about .loc and .at, please refer to the following 
#examples:  

#.loc:  https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html#pandas.DataFrame.loc
#.at:  https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.at.html

#Additional readings on this topic:

#https://izziswift.com/what-is-the-difference-between-using-loc-and-using-just-square-brackets-to-filter-for-columns-in-pandas-python/
#https://www.dataquest.io/blog/settingwithcopywarning/

#Let's look at ways to find data in your dataframe.  
dfemp.loc[0]

dfemp.loc[0:2]

dfempag = dfemp[['jobtitle', 'salary', 'age']].groupby(['jobtitle']).mean()
dfempag
dfempag.loc['Analyst']

dfempag.loc[['Analyst', 'CEO']]

#Let's set all values for those rows to 0.
dfempag.loc[['Analyst', 'CEO']] = 0
dfempag

#where loc is a row, .at focuses on a field

#show the row
dfemp.loc[0]
dfemp.at[0, 'salary']

#update an individual cell.
dfemp.at[0, 'salary'] = 500
dfemp.loc[0]

#Can even use a loop if necessary.  (Remember the one that didn't work?)
#let's give everyone a 10% raise.  Note, you could easily nest if statements
#in this loop to only give raises to certain jobtitles.
dfemp.head()

for index, row in dfemp.iterrows():
    dfemp.at[index, 'salary'] = row['salary'] * 1.10
    
dfemp.head()

#Well, let's think like DB developers.  Recall how we sliced up our dataframe.
#let's only give a raise to the Analyst.
#let's look at the salaries
dfemp['salary'][dfemp['jobtitle'] == 'Analyst']

#now let's update them all to 100000
dfemp['salary'][dfemp['jobtitle'] == 'Analyst'] = 1000000

#now that is an odd warning?  did it work?
dfemp['salary'][dfemp['jobtitle'] == 'Analyst']

#what is we swap the logical order.  
dfemp[dfemp['jobtitle'] == 'Analyst']['salary']

#Now, let's set them all to 200000
dfemp[dfemp['jobtitle'] == 'Analyst']['salary'] = 200000
dfemp[dfemp['jobtitle'] == 'Analyst']['salary']
#so why didn't the above update????  Check out the article, and note the order
#of what worked and what didn't.

#Finally, let's look at making a categorical variable.  
#you can use method on line 69 with varying levels (i.e. how we solve for letter
#grades), or you can use cut.

#refresh out dataset.
res = r.get(url + empfile)
dfemp = pd.read_csv(io.StringIO(res.text))

#Let's do this explicitly with labels
bins = [0, 40000, 70000, 1000000]
labels = ['Low', 'Medium', 'High'] #note, labels MUST be 1 items less than bins
dfemp['pay_category'] = pd.cut(dfemp['salary'], bins=bins, labels=labels)
