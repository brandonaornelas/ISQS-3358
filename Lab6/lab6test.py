'''
Brandon Ornelas, Connor Case, Kai Clough, Leo Ramirez
Lab 6
'''

import requests as r
import pandas as pd
import io

url = 'http://drd.ba.ttu.edu/isqs3358/Labs/Lab6/'
hr = 'hr_data.csv'
sales = 'sales_data.csv'

res_hr = r.get(url + hr)
df_hr = pd.read_csv(io.StringIO(res_hr.text), delimiter="|")

res_sales = r.get(url + sales)
df_sales = pd.read_csv(io.StringIO(res_sales.text), delimiter="|")

# Merge the DataFrames
merged_df = pd.merge(df_hr, df_sales, left_on='EmpId', right_on='EmpId', how='inner')

# Fill missing 'Title' based on mode
merged_df['Title'].fillna(merged_df['Title'].mode()[0], inplace=True)
print("Filled missing 'Title' values with the mode (most frequent title).")

# Fill missing 'Salary' based on median
merged_df['Salary'].fillna(merged_df['Salary'].median(), inplace=True)
print("Filled missing 'Salary' values with the median salary.")

# Fill missing 'Benefits' based on median
merged_df['Benefits'].fillna(merged_df['Benefits'].median(), inplace=True)
print("Filled missing 'Benefits' values with the median benefits.")


average_stats = merged_df.groupby('Title').agg({'Salary': 'mean', 'Benefits': 'mean', 'ItemsSold': 'mean', 'SalesValue': 'mean'}).reset_index()

merged_df = pd.merge(merged_df, average_stats, on='Title', suffixes=('', '_avg'))

merged_df.rename(columns={'Salary_avg': 'Avg_Salary', 'Benefits_avg': 'Avg_Benefits', 'ItemsSold_avg': 'Avg_ItemsSold', 'SalesValue_avg': 'Avg_SalesValue'}, inplace=True)

# Calculate the total benefits
merged_df['total_benefits'] = merged_df['Salary'] + merged_df['Benefits']

# Calculate the average total benefits for each job title
merged_df['avg_total_benefits'] = merged_df.groupby('Title')['total_benefits'].transform('mean')

# Assign 'employee_comp' based on total benefits
average_total_benefits = merged_df['total_benefits'].mean()
merged_df['employee_comp'] = 'high'
merged_df.loc[merged_df['total_benefits'] <= average_total_benefits, 'employee_comp'] = 'low'

# Assign 'position_comp' based on total benefits by title
merged_df['position_comp'] = 'high'
merged_df.loc[merged_df['total_benefits'] <= merged_df['avg_total_benefits'], 'position_comp'] = 'low'

# Reorder the columns as per the desired output
merged_df = merged_df[['EmpId', 'Title', 'Salary', 'Benefits', 'ItemsSold', 'SalesValue',
                     'Avg_Salary', 'Avg_Benefits', 'Avg_ItemsSold', 'Avg_SalesValue',
                     'total_benefits', 'employee_comp', 'avg_total_benefits', 'position_comp']]


merged_df.to_csv("all_data.csv", index=False)

#Employee High Benefits csv file
high_benefit_df = merged_df[(merged_df['employee_comp'] == 'high') & (merged_df['position_comp'] == 'high')]
high_benefit_df = high_benefit_df[['EmpId', 'Title', 'Salary', 'Benefits', 'SalesValue', 'employee_comp', 'position_comp']]
high_benefit_df.to_csv("employee_high_benefit.csv", index=False)

#Position High csv file
positiondata_high = merged_df[(merged_df['employee_comp'] == 'high') & (merged_df['position_comp'] == 'high')]
positiondata_high = positiondata_high[['EmpId', 'Title', 'Salary', 'Benefits', 'SalesValue', 'employee_comp', 'position_comp']]
positiondata_high.to_csv("positiondata_high.csv", index=False)

