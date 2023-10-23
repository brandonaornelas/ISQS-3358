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

merged_df['total_benefits'] = merged_df['Salary'] + merged_df['Benefits']
average_total_benefits = merged_df['total_benefits'].mean()

merged_df['employee_comp'] = 'high'
merged_df.loc[merged_df['total_benefits'] <= average_total_benefits, 'employee_comp'] = 'low'

avg_total_benefits_by_title = merged_df.groupby('Title')['total_benefits'].transform('mean')

merged_df['position_comp'] = 'high'
merged_df.loc[merged_df['total_benefits'] <= avg_total_benefits_by_title, 'position_comp'] = 'low'

merged_df.to_csv('all_data.csv', index=False)

employee_high_benefit = merged_df[merged_df['total_benefits'] > average_total_benefits]
employee_high_benefit.to_csv('employee_high_benefit.csv', index=False)

positiondata_high = merged_df[merged_df['total_benefits'] > avg_total_benefits_by_title]
positiondata_high.to_csv('positiondata_high.csv', index=False)
