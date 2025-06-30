import pandas as pd
from polar import Polar
import os

# First, let's create our example CSV file
employees_data = """employee_id,first_name,last_name,department,salary,hire_date
1001,John,Smith,Engineering,75000,2020-05-15
1002,Maria,Garcia,Marketing,68000,2021-03-10
1003,Robert,Johnson,Engineering,82000,2019-11-22
1004,Sarah,Williams,HR,65000,2022-01-05
1005,Michael,Brown,Finance,90000,2018-07-18
1006,Jennifer,Jones,Marketing,72000,2020-09-30
1007,David,Miller,Engineering,78000,2021-06-12
1008,Lisa,Davis,HR,67000,2019-04-25
1009,James,Wilson,Finance,85000,2020-02-28
1010,Patricia,Taylor,Marketing,69000,2022-05-03"""

# Write the data to a CSV file
csv_file_path = "employees.csv"
with open(csv_file_path, "w") as f:
    f.write(employees_data)

print(f"Created CSV file: {csv_file_path}")

# Create a Polar instance for authorization
polar = Polar()

# Define our authorization policies
polar.load_str("""
# Define different access levels
# Admin can access all data
can_access(user, "employees", _) if user.role = "admin";

# HR can access all employee data except salary information
can_access(user, "employees", ["employee_id", "first_name", "last_name", "department", "hire_date"]) if 
    user.role = "hr";

# Department managers can only access data for their own department
can_access(user, "employees", ["employee_id", "first_name", "last_name", "hire_date"]) if 
    user.role = "manager" and
    user.department = "Engineering";

# Define what columns different roles can modify
can_modify(user, "employees", "salary") if user.role = "admin" or user.role = "finance";
can_modify(user, "employees", "department") if user.role = "admin" or user.role = "hr";
""")


# Test with different user roles
def process_csv_to_excel(user_role, user_department=None):
    user = {"role": user_role}
    if user_department:
        user["department"] = user_department

    print(f"\nProcessing as {user_role}" + (f" in {user_department}" if user_department else ""))

    # Check what columns the user can access
    accessible_columns = None
    for query in polar.query("can_access(user, \"employees\", columns)", {"user": user}):
        accessible_columns = query.columns
        break

    if not accessible_columns:
        print(f"Access denied for user with role: {user_role}")
        return None

    if accessible_columns == "_":  # Admin can access all columns
        accessible_columns = None  # None means all columns in pandas

    # Read the CSV with appropriate column access
    df = pd.read_csv(csv_file_path, usecols=accessible_columns)

    # Apply some transformations based on role
    if user_role == "admin" or user_role == "finance":
        # Calculate a bonus column (5% of salary)
        if "salary" in df.columns:
            df["bonus"] = df["salary"] * 0.05

    if user_role == "hr" or user_role == "admin":
        # Calculate years of service
        if "hire_date" in df.columns:
            df["hire_date"] = pd.to_datetime(df["hire_date"])
            current_date = pd.Timestamp('2025-05-20')  # Using the current date from the prompt
            df["years_of_service"] = ((current_date - df["hire_date"]) / pd.Timedelta(days=365.25)).round(1)

    # Filter by department if needed
    if user_role == "manager" and user_department:
        df = df[df["department"] == user_department] if "department" in df.columns else df

    # Display the data
    print("\nAccessible data:")
    print(df.head())

    # Save to Excel with role-specific filename
    excel_file = f"employees_{user_role}" + (f"_{user_department.lower()}" if user_department else "") + ".xlsx"
    df.to_excel(excel_file, index=False)
    print(f"Data saved to {excel_file}")

    return df


# Process the data with different user roles
admin_df = process_csv_to_excel("admin")
hr_df = process_csv_to_excel("hr")
manager_df = process_csv_to_excel("manager", "Engineering")
finance_df = process_csv_to_excel("finance")

# Cleanup
print("\nCleaning up...")
if os.path.exists(csv_file_path):
    os.remove(csv_file_path)
    print(f"Removed {csv_file_path}")

print("\nProcess completed successfully!")