import io
import requests as r
import pandas as pd
#variable and file path setup
url = 'http://drd.ba.ttu.edu/isqs3358/ex/L2.2/'
onemeasure = 'onemeasure.csv'
twomeasure = 'twomeasure.csv'
#make a request to get the csv from the server
res = r.get(url + onemeasure)
dfone = pd.read_csv(io.StringIO(res.text),delimiter=',')
res = r.get(url + twomeasure)
dftwo = pd.read_csv(io.StringIO(res.text),delimiter=',')


#These are made up (random) datasets.  
#onemeasure list texas counties with case counts (random number)
#twomeasure list texas counties with 2 measures (cases and test) again random.  

#goal, put the measures on columns, and the dates as rows.
#i.e.  date, county, measure

##############################################################################
#                                One field stay example
##############################################################################

print(dfone)
dfone.columns[1:len(dfone.columns)]

#this is a nice brute force way of coding this.  basically, list hte columns you want to become rows and which columns stay on rows.  
#id_vars:  fields that stay as they are (on rows)
#value_vars:  columns you want to swap to rows.
x = dfone.melt(id_vars='locations', value_vars=['04/01/20', '04/02/20', '04/03/20', '04/04/20', '04/05/20',
       '04/06/20', '04/07/20', '04/08/20', '04/09/20', '04/10/20'])

#Now, let's say we have many columns, we don't want to type all that.  Let's do this.
#recall that the .columns call on a dataframe is a list
#recall also that we can subset a list using the colon notation in python.

#example, print all columns
print(dfone.columns)

#well we don't want to flip the first column, so let's remove it from teh list.
#The len command here might look odd.  This is to help so you don't have to hardcode
#all the total number of columns in the list.
print(dfone.columns[1:len(dfone.columns)])

#now, these past items aside, let's do the previous example using this syntax.
x1 = dfone.melt(id_vars='locations', value_vars=dfone.columns[1:len(dfone.columns)])

##############################################################################
#                                Two field stay example
##############################################################################
#note, we will do this twice and teh first time is the explict version with 
#the columns all enumerated so you can see what is going on.  The last example
#will be similar to the last example of teh one field stay method

x2 = dftwo.melt(id_vars=['locations','Measure'], value_vars=['04/01/20', '04/02/20', '04/03/20', '04/04/20', '04/05/20',
       '04/06/20', '04/07/20', '04/08/20', '04/09/20', '04/10/20'])

#cleaner method.  Note, starting at 2 as we want to keep teh first 2 as is:

x2a = dftwo.melt(id_vars=dftwo.columns[0:2], value_vars=dftwo.columns[2:len(dftwo.columns)])


##############################################################################
#                                How about rows to columns
##############################################################################
#in some cases, a pivot would work, but most times you have an issue where you
#have 2 measures (separate rows) that you want to flip.  Example, look at dftwo
#in this code.  While you can dig around in pivot and other methods, a more 
#direct approach is to subset then use a join.  In this example, we will move
#dftwo to have 2 numerical columns (test, cases) and remove the measure column.

#First, let's melt the dates onto the rows:
x4 = dftwo.melt(id_vars=dftwo.columns[0:2], value_vars=dftwo.columns[2:len(dftwo.columns)])

#rename the date column
x4.rename(columns={'variable': 'Date'}, inplace=True)
#convert to date type
x4['Date'] = pd.to_datetime(x4['Date'])

#now, let's split the date (easier when we rejoin)
x4['year'] = x4['Date'].dt.year
x4['mn'] = x4['Date'].dt.month
x4['dy'] = x4['Date'].dt.day

#Now, let's subset based on the text in the measure column.

x4cases = x4[x4['Measure'] == 'Cases']
x4test = x4[x4['Measure'] == 'Test']

#Let's rename the measurement field to either test or cases
x4cases.rename(columns={'value' : 'Cases'}, inplace=True)
x4test.rename(columns={'value' : 'Test'}, inplace=True)

#Now, we could get tricky with the index (subtract 1) as they were ordered, but let's
#not do that as that requires additional assumptions.  Instead, let's join on county and date

x4_merge = x4cases.merge(x4test, how='inner', on=['locations', 'year', 'mn', 'dy'])

#now, let's drop the fields we don't need and rename a field to remove the 'X'
x4_merge.drop(['Measure_x', 'Measure_y', 'year', 'mn', 'dy', 'Date_y'], axis=1, inplace=True)
x4_merge.rename(columns={'Date_x': 'Date'}, inplace=True)
































