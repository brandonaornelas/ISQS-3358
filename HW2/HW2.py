import requests as r
import pandas as pd
import io

urls = [
    'http://drd.ba.ttu.edu/isqs3358/hw2/hr_data.csv',
    'http://drd.ba.ttu.edu/isqs3358/hw2/sales_data.csv',
    'http://drd.ba.ttu.edu/isqs3358/hw2/item_data.csv'
]

res_hr = r.get(urls[0]) # has delimiter of |
res_sales = r.get(urls[1]) # has commas
res_item = r.get(urls[2]) # has delimiter of |

df_hr = pd.read_csv(io.StringIO(res_hr.text), delimiter="|")
df_sales = pd.read_csv(io.StringIO(res_sales.text))
df_item = pd.read_csv(io.StringIO(res_item.text), delimiter="|")

df_merge = df_hr.merge(df_sales, how='inner', on='EmpId')
df_merged_all_datasets = df_merge.merge(df_item, how='inner', left_on='VendorCode', right_on="VendorID")


# Handle Missing Values by filling 'Benefits' based on 'Title' means
title_means = df_merged_all_datasets.groupby('Title')['Benefits'].transform('mean')
df_merged_all_datasets['Benefits'] = df_merged_all_datasets['Benefits'].fillna(title_means)

# Create Computational Columns
df_merged_all_datasets['Per_Item_Benefit'] = df_merged_all_datasets['Benefits'] / df_merged_all_datasets['ItemSold']
df_merged_all_datasets['Total_Compensation'] = df_merged_all_datasets['Salary'] + df_merged_all_datasets['Benefits']
df_merged_all_datasets['Performance_metrics'] = (df_merged_all_datasets['Total_Compensation'] / df_merged_all_datasets['ItemSold']) / df_merged_all_datasets.groupby('Title')['ItemSold'].transform('mean')

# Define 'employee_raise_elligible' based on conditions
conditions = [
    (df_merged_all_datasets['Performance_metrics'] > 238) & (df_merged_all_datasets['Title'] == 'Sales Associate 1'),
    (df_merged_all_datasets['Performance_metrics'] > 704) & (df_merged_all_datasets['Title'] == 'Sales Associate 2'),
    (df_merged_all_datasets['Performance_metrics'] > 938) & (df_merged_all_datasets['Title'] == 'Sales Associate 3'),
    (df_merged_all_datasets['Performance_metrics'] > 2146) & (df_merged_all_datasets['Title'] == 'Sales Manager')
]

choices = ['Yes' if condition.any() else 'No' for condition in conditions]
df_merged_all_datasets['employee_raise_elligible'] = pd.Series(choices)

# Calculate Average Statistics by 'Title'
title_aggregate = df_merged_all_datasets.groupby('Title').agg({
    'Total_Compensation': 'mean',
    'Per_Item_Benefit': 'mean',
    'Performance_metrics': 'mean'
}).reset_index()

# Filter employees getting a raise
employee_raise = df_merged_all_datasets[df_merged_all_datasets['employee_raise_elligible'] == 'Yes']

# Calculate benefit raises based on job titles
benefit_raises = {
    'Sales Associate 1': 0.075,
    'Sales Associate 2': 0.07,
    'Sales Associate 3': 0.065,
    'Sales Manager': 0.06
}

df_merged_all_datasets['updated_benefit'] = df_merged_all_datasets['Title'].map(benefit_raises)
df_merged_all_datasets['benefit_diff'] = df_merged_all_datasets['updated_benefit'] * df_merged_all_datasets['Benefits']

# Calculate total benefit, updated benefit, and benefit difference
benefit_stats = df_merged_all_datasets[df_merged_all_datasets['employee_raise_elligible'] == 'Yes'].groupby('Title').agg({
    'Benefits': 'sum',
    'updated_benefit': 'sum',
    'benefit_diff': 'sum'
}).reset_index()

# Save results to CSV files
title_aggregate.to_csv('title_aggregate.csv', index=False)
employee_raise.to_csv('employee_raise.csv', index=False)
benefit_stats.to_csv('title_benefit_raises.csv', index=False)
