"""Loads used_cars.csv into a PostgreSQL 'cars' table with pandas and SQLAlchemy."""

import os
from pathlib import Path

import pandas as pd
from sqlalchemy import create_engine

# Step 1: Create a connection to the PostgreSQL database
# The connection string is read from the DATABASE_URL environment variable.
# Expected format (never hardcode the real password in the source):
#   postgresql://user:password@localhost:5432/used_cars
database_url = os.getenv("DATABASE_URL")
if not database_url:
    raise SystemExit(
        "DATABASE_URL is not set. Example: "
        "export DATABASE_URL='postgresql://user:password@localhost:5432/used_cars'"
    )

# Step 2: Read the CSV into a pandas DataFrame (path relative to this script)
csv_path = Path(__file__).parent / "used_cars.csv"
df = pd.read_csv(csv_path)

# Step 2b: Strip whitespace from string columns ('country' and 'vin' have leading spaces)
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].str.strip()

# Step 3: Establish the connection with PostgreSQL using SQLAlchemy
engine = create_engine(database_url)

# Step 4: Create the 'cars' table and insert the data
df.to_sql('cars', engine, if_exists='replace', index=False)

print("Data has been successfully loaded into the 'cars' table.")
