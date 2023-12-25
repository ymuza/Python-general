import pandas as pd

# Create a dataframe with sales data
data = {'Date': ['2021-01-01', '2021-01-02', '2021-01-03', '2021-01-04', '2021-01-05', '2021-01-06'],
        'Product': ['A', 'B', 'A', 'B', 'A', 'B'],
        'Region': ['North', 'North', 'South', 'South', 'East', 'East'],
        'Sales': [100, 200, 150, 250, 300, 350]}
df = pd.DataFrame(data)

# Create a pivot table to summarize the data by Region and Product
pivot_table = df.pivot_table(values='Sales', index='Region', columns='Product', aggfunc='sum')

# Print the pivot table
print(pivot_table)
