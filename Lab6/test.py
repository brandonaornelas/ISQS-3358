import requests as r
import pandas as pd
import io

url = 'http://drd.ba.ttu.edu/isqs3358/ex/L2.2/'
file_1 = 'employment.csv'
file_2 = 'job_title.csv'
file_3 = 'job_title_year.csv'
file_4 = 'job_title_devs.csv'

# Employment 
res = r.get(url + file_1)
df_emp = pd.read_csv(io.StringIO(res.text))

# Job
res = r.get(url + file_2)
df_job = pd.read_csv(io.StringIO(res.text))
"""
print(df_emp.head())
print(df_job.head())
print()
df_emp_merge = df_emp.merge(df_job, how='inner', left_on='jobtitleid', right_on='jobtitleid')
print(df_emp_merge.head())
print()

print(df_emp_merge['jobtitle'].value_counts())
print(df_job['jobtitle'].head())


df_emp_merge_left = df_emp.merge(df_job, how='left', on='jobtitleid')
print(df_emp_merge_left['jobtitle'].value_counts())
print()
df_emp_merge_right = df_emp.merge(df_job, how='right', on='jobtitleid')
print(df_emp_merge_right['jobtitle'].value_counts())

"""


'''
Brandon Ornelas, Connor Case, Kai Clough, Leo Ramirez
Lab 6
'''
import io
import pandas as pd
import requests as r

url = 'http://drd.ba.ttu.edu/isqs3358/Labs/Lab6/'
file_1 = 'hr_data.csv'
file_2 = 'sales_data.csv'

res1 = r.get(url + file_1)
df_hr = pd.read_csv(io.StringIO(res1.text), delimiter ="|")

res2 = r.get(url + file_2)
df_sales = pd.read_csv(io.StringIO(res2.text), delimiter ="|")

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

#All the averages!

# Calculate the average statistics for each job title
average_stats = merged_df.groupby('Title').agg({'Salary': 'mean', 'Benefits': 'mean', 'ItemsSold': 'mean', 'SalesValue': 'mean'}).reset_index()
# Merge the average statistics back into the original DataFrame
merged_df = pd.merge(merged_df, average_stats, on='Title', suffixes=('', '_avg'))
# Rename the new columns
merged_df.rename(columns={'Salary_avg': 'Avg_Salary', 'Benefits_avg': 'Avg_Benefits', 'ItemsSold_avg': 'Avg_ItemsSold', 'SalesValue_avg': 'Avg_SalesValue'}, inplace=True)
# Write the DataFrame back to the CSV file
#merged_df.to_csv("data.csv", index=False)




# Calculate the total benefits
merged_df['total_benefits'] = merged_df['Salary'] + merged_df['Benefits']

# Calculate the average total benefits for the entire DataFrame
average_total_benefits = merged_df['total_benefits'].mean()

# Assign 'employee_comp' based on total benefits
merged_df['employee_comp'] = 'high'
merged_df.loc[merged_df['total_benefits'] <= average_total_benefits, 'employee_comp'] = 'low'

# Calculate the average total benefits by job title
avg_total_benefits_by_title = merged_df.groupby('Title')['total_benefits'].transform('mean')

# Assign 'position_comp' based on total benefits by title
merged_df['position_comp'] = 'high'
merged_df.loc[merged_df['total_benefits'] <= avg_total_benefits_by_title, 'position_comp'] = 'low'

# Calculate the average total benefits for the entire DataFrame
average_total_benefits = merged_df['total_benefits'].mean()

# Insert the 'AverageTotalBenefits' column between 'employee_comp' and 'position_comp'
merged_df.insert(merged_df.columns.get_loc('position_comp'), 'AverageTotalBenefits', average_total_benefits)

# Write the DataFrame back to the CSV file
merged_df.to_csv("all_data.csv", index=False)


merged_df['total_benefits'] = merged_df['Salary'] + merged_df['Benefits']
average_total_benefits = merged_df['total_benefits'].mean()

merged_df['employee_comp'] = 'high'
merged_df.loc[merged_df['total_benefits'] <= average_total_benefits, 'employee_comp'] = 'low'


avg_total_benefits_by_title = merged_df.groupby('Title')['total_benefits'].transform('mean')

merged_df['position_comp'] = 'high'
merged_df.loc[merged_df['total_benefits'] <= avg_total_benefits_by_title, 'position_comp'] = 'low'

merged_df.to_csv('all_data.csv', index=False)



employee_high_benefit = merged_df[merged_df['total_benefits'] > average_total_benefits]
#employee_high_benefit.to_csv('employee_high_benefit.csv', index=False)

positiondata_high = merged_df[merged_df['total_benefits'] > avg_total_benefits_by_title]
#positiondata_high.to_csv('positiondata_high.csv', index=False)



