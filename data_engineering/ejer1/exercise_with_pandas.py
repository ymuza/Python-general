import pandas as pd
import io

# Create a DataFrame from the CSV data

df = pd.read_csv("employees.csv")


# Display the DataFrame
print("Employee DataFrame:")
print(df.head())
print("\nDataFrame shape:", df.shape)
print("\nDataFrame info:")
print(df.info())
print("\nDataFrame summary statistics:")
print(df.describe())

# Export the DataFrame to Excel
excel_file = "employees.xlsx"
df.to_excel(excel_file, index=False)

print(f"\nExcel file '{excel_file}' has been created successfully!")

# Print a sample of the data by department
print("\nEmployee count by department:")
print(df['department'].value_counts())

print("\nAverage salary by department:")
print(df.groupby('department')['salary'].mean())