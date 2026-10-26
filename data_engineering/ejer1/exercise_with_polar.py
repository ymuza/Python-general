"""Role-based access to employee data: an Oso Polar policy decides which columns each
role can read before pandas exports the result to Excel.

Note: the Oso Library (embedded Polar engine) was deprecated by Oso in Dec 2023; this file
is kept as a reference exercise."""

from datetime import date
from pathlib import Path

import pandas as pd
from polar import Polar

# Read the existing CSV that lives next to this script (no temp file written to the cwd)
csv_file_path = Path(__file__).parent / "employees.csv"
print(f"Using CSV file: {csv_file_path}")

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
# ('department' is included so the department filter below can actually be applied)
can_access(user, "employees", ["employee_id", "first_name", "last_name", "department", "hire_date"]) if
    user.role = "manager" and
    user.department = "Engineering";

# Define what columns different roles can modify
can_modify(user, "employees", "salary") if user.role = "admin" or user.role = "finance";
can_modify(user, "employees", "department") if user.role = "admin" or user.role = "hr";
""")


# Test with different user roles
def process_csv_to_excel(user_role, user_department=None):
    """Exports the employee columns this role may access to a role-specific Excel file.

    Returns the resulting DataFrame, or None if access is denied.
    """
    user = {"role": user_role}
    if user_department:
        user["department"] = user_department

    print(f"\nProcessing as {user_role}" + (f" in {user_department}" if user_department else ""))

    # Check what columns the user can access
    accessible_columns = None
    for query in polar.query("can_access(user, \"employees\", columns)", {"user": user}):
        accessible_columns = query.columns  # TODO: verify against the installed oso version
        break

    if not accessible_columns:
        print(f"Access denied for user with role: {user_role}")
        return None

    if accessible_columns == "_":  # Admin can access all columns  # TODO: verify against the installed oso version
        accessible_columns = None  # None means all columns in pandas

    # Read the CSV with appropriate column access
    df = pd.read_csv(csv_file_path, usecols=accessible_columns)

    # Apply some transformations based on role
    if user_role in ("admin", "finance"):
        # Calculate a bonus column (5% of salary)
        if "salary" in df.columns:
            df["bonus"] = df["salary"] * 0.05

    if user_role in ("hr", "admin"):
        # Calculate years of service
        if "hire_date" in df.columns:
            df["hire_date"] = pd.to_datetime(df["hire_date"])
            current_date = pd.Timestamp(date.today())
            service = (current_date - df["hire_date"]) / pd.Timedelta(days=365.25)
            df["years_of_service"] = service.round(1)

    # Filter by department if needed
    if user_role == "manager" and user_department:
        df = df[df["department"] == user_department] if "department" in df.columns else df

    # Display the data
    print("\nAccessible data:")
    print(df.head())

    # Save to Excel with role-specific filename (next to this script)
    suffix = f"_{user_department.lower()}" if user_department else ""
    excel_file = Path(__file__).parent / f"employees_{user_role}{suffix}.xlsx"
    df.to_excel(excel_file, index=False)
    print(f"Data saved to {excel_file}")

    return df


# Process the data with different user roles
admin_df = process_csv_to_excel("admin")
hr_df = process_csv_to_excel("hr")
manager_df = process_csv_to_excel("manager", "Engineering")
finance_df = process_csv_to_excel("finance")

print("\nProcess completed successfully!")
