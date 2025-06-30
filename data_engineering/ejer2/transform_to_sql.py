import pandas as pd
import psycopg2
from sqlalchemy import create_engine

# Step 1: Create a connection to the PostgreSQL database
# Replace the placeholders with your database connection details
database_url = "postgresql://yamil:32874993@localhost:5432/used_cars"

# Step 2: Read the CSV into a pandas DataFrame
df = pd.read_csv('used_cars.csv')

# Step 3: Establish the connection with PostgreSQL using SQLAlchemy
engine = create_engine(database_url)

# Step 4: Create the 'cars' table and insert the data
df.to_sql('cars', engine, if_exists='replace', index=False)

print("Data has been successfully loaded into the 'cars' table.")
