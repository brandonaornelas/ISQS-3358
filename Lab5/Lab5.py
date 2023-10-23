import requests as r
import pandas as pd
import io

url = "http://drd.ba.ttu.edu/isqs3358/Labs/Lab5/security_sales_data.csv"
res = r.get(url)
df = pd.read_csv(io.StringIO(res.text), delimiter="|")

df['buyer_state'] = df['Buyer_Code'].str[2:4]
df['seller_state'] = df['Seller_Code'].str[2:4]
df['cost_of_goods'] = df['Price_per_unit'] * df['Quantity']
df['profit_markup'] = df['cost_of_goods'] * df['profit_markup_percent']
df['total_sale'] = df['cost_of_goods'] + df['profit_markup']
df["sales_rank"] = 'low'
df['sales_rank'][df['total_sale'] > 4800] = 'high'

