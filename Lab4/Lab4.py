import requests as r
import pandas as pd
import io
import matplotlib.pyplot as plt

url = "http://drd.ba.ttu.edu/isqs3358/Labs/lab4/"
file = "rando.csv"
filepath = "/Users/brandonornelas/ISQS-3358/Lab4/dataout.csv"

res = r.get(url + file)
df = pd.read_csv(io.StringIO(res.text))

stats = df.describe()

# Highest and Lowest STD
highest_std_column = stats.loc['std'].idxmax()
lowest_std_column = stats.loc['std'].idxmin()

# Highest and Lowest Average
highest_average_column = stats.loc['mean'].idxmax()
lowest_average_column = stats.loc['mean'].idxmin()


print("Highest and Lowest:")
print()
print(f"Highest Average Column: {highest_average_column}")
print(f"Highest STD Column: {highest_std_column}")
print()
print(f"Lowest Average Column: {lowest_average_column}")
print(f"Lowest STD Column: {lowest_std_column}")


print()
print("Correlation:")
# This outputs shows the correlation between all the columns and the pair that are postively, and negatively correlated with each other.
selected_columns = df[['Var1', 'Var2', 'Var3', 'Var4', 'Var5', 'Var6', 'Var7', 'Var8', 'Var9', 'Var10']]
corr_matrix = selected_columns.corr()
print(corr_matrix)
pairs = set()
print()
print("Negative and Postive Columns Correlations:")
for column1 in selected_columns.columns:
    for column2 in selected_columns.columns:
        if column1 != column2:
            if (column1, column2) not in pairs and (column2, column1) not in pairs:
                correlation = corr_matrix.loc[column1, column2]
                if correlation > .5:
                    print(f"{column1} and {column2} are positively correlated with a correlation coefficient of {correlation:.2f}")
                    pairs.add((column1, column2))
                elif correlation < -.5:
                    print(f"{column1} and {column2} are negatively correlated with a correlation coefficient of {correlation:.2f}")
                    pairs.add((column1, column2))

# This renders a scatter plot matrix
pd.plotting.scatter_matrix(df, figsize=(10,10))
plt.show()

selected_columns_csv = df[['Var2', 'Var4', 'Var6']]
selected_columns_csv.to_csv(filepath, sep="|", index=False)