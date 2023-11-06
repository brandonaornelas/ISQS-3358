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

mode_by_title = df_merged_all_datasets.groupby('Title').transform(lambda x: x.mode().iloc[0] if not x.mode().empty else None)

# Fill missing values based on "Title"
df_filled = df_merged_all_datasets.fillna(mode_by_title)

# Calculate the "Per_Item_Benefit" and add it as a new column
df_filled['Per_Item_Benefit'] = df_filled['Benefits'] / df_filled['ItemSold']

# Calculate the "Total_Compensation" and add it as a new column
df_filled['Total_Compensation'] = df_filled['Salary'] + df_filled['Benefits']

avg_item_sold = df_filled['ItemSold'].mean()

# Calculate the "Performance_metrics" and add it as a new column
df_filled['Performance_metrics'] = (df_filled['Total_Compensation'] / df_filled['ItemSold']) / avg_item_sold

# Define a function to determine eligibility
def determine_eligibility(row):
    if row['Title'] == 'Sales Associate 1' and row['Performance_metrics'] > 238:
        return 'Yes'
    elif row['Title'] == 'Sales Associate 2' and row['Performance_metrics'] > 704:
        return 'Yes'
    elif row['Title'] == 'Sales Associate 3' and row['Performance_metrics'] > 938:
        return 'Yes'
    elif row['Title'] == 'Sales Manager' and row['Performance_metrics'] > 2146:
        return 'Yes'
    else:
        return 'No'

# Apply the function to create the "employee_raise_elligible" column
df_filled['employee_raise_elligible'] = df_filled.apply(determine_eligibility, axis=1)


# Compute the averages by Title
title_aggregates = df_filled.groupby('Title').agg({
    'Total_Compensation': 'mean',
    'Per_Item_Benefit': 'mean',
    'Performance_metrics': 'mean'
}).reset_index()

# Rename the columns for clarity
title_aggregates.rename(columns={
    'Total_Compensation': 'Average_Total_Compensation',
    'Per_Item_Benefit': 'Average_Per_Item_Benefit',
    'Performance_metrics': 'Average_Performance_metrics'
}, inplace=True)

# Save the results to a CSV file
title_aggregates.to_csv('ti_aggregate.csv', index=False)

# Filter employees who will receive a raise
eligible_for_raise = df_filled[
    ((df_filled['Title'] == 'Sales Associate 1') & (df_filled['Performance_metrics'] > 238)) |
    ((df_filled['Title'] == 'Sales Associate 2') & (df_filled['Performance_metrics'] > 704)) |
    ((df_filled['Title'] == 'Sales Associate 3') & (df_filled['Performance_metrics'] > 938)) |
    ((df_filled['Title'] == 'Sales Manager') & (df_filled['Performance_metrics'] > 2146))
]

# Save the filtered data to "employee_raise.csv"
eligible_for_raise.to_csv('employee_raise.csv', index=False)

# Define the benefit raise percentages by title
benefit_raises = {
    'Sales Associate 1': 0.075,  # 7.5% raise
    'Sales Associate 2': 0.07,   # 7% raise
    'Sales Associate 3': 0.065,  # 6.5% raise
    'Sales Manager': 0.06        # 6% raise
}

# Create the "updated_benefit" column based on title
df_filled['updated_benefit'] = df_filled['Title'].map(benefit_raises)

# Create the "benefit_diff" column based on the benefit raise
df_filled['benefit_diff'] = df_filled['Benefits'] * df_filled['updated_benefit']


# Filter employees who will receive a raise
eligible_for_raise = df_filled[
    ((df_filled['Title'] == 'Sales Associate 1') & (df_filled['Performance_metrics'] > 238)) |
    ((df_filled['Title'] == 'Sales Associate 2') & (df_filled['Performance_metrics'] > 704)) |
    ((df_filled['Title'] == 'Sales Associate 3') & (df_filled['Performance_metrics'] > 938)) |
    ((df_filled['Title'] == 'Sales Manager') & (df_filled['Performance_metrics'] > 2146))
]

# Group by job title and calculate the total benefit, updated benefit, and benefit difference
title_benefit_totals = eligible_for_raise.groupby('Title').agg({
    'Benefits': 'sum',
    'updated_benefit': 'sum',
    'benefit_diff': 'sum'
}).reset_index()

# Save the result to a CSV file
title_benefit_totals.to_csv('title_benefit_raises.csv', index=False)






