"""Loads employees.csv with pandas, prints summaries and exports it to Excel."""

from pathlib import Path

import pandas as pd

# Paths relative to this script, so it works from any cwd
BASE_DIR = Path(__file__).parent

# Create a DataFrame from the CSV data

df = pd.read_csv(BASE_DIR / "employees.csv")


# Display the DataFrame
print("Employee DataFrame:")
print(df.head())
print("\nDataFrame shape:", df.shape)
print("\nDataFrame info:")
print(df.info())
print("\nDataFrame summary statistics:")
print(df.describe())

# Export the DataFrame to Excel (needs the optional 'openpyxl' package)
excel_file = BASE_DIR / "employees.xlsx"
try:
    df.to_excel(excel_file, index=False)
    print(f"\nExcel file '{excel_file}' has been created successfully!")
except ImportError:
    print("\nSkipping Excel export: 'openpyxl' is required (poetry install --with data).")

# Print a sample of the data by department
print("\nEmployee count by department:")
print(df['department'].value_counts())

print("\nAverage salary by department:")
print(df.groupby('department')['salary'].mean())
