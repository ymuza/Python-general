import pandas as pd
import numpy as np

# sample DataFrame
dict1 = {
    'name': ['Alice Smith', 'Bob Johnson', 'Charlie Brown'],
    'age': [25, 30, 35],
    'city': ['New York', 'London', 'Tokyo'],
    'tax_percentage':[13.5, 15, 20],
    'salary': [50000, 60000, 70000]
}


def add_net_salary_column():
    """creates a net_salary column calculated by removing the tax percentage from salary"""
    df = pd.DataFrame(dict1)  # transform dict to dataframe
    print(" ")
    print("before adding net salary column:")
    print(df)

    df['net_salary'] = df['salary'] - (df['salary'] * df['tax_percentage'] / 100)
    print(" ")
    print("after adding net salary column:")
    return df


def add_salary_category_column():
    """ Creates a column using a custom function and 'apply' keyword """
    df = pd.DataFrame(dict1)
    df['salary_category'] = (df['salary']
                             .apply(lambda x : 'low' if x < 50000 else 'medium' if x <65000 else 'high'))
    return df


def remove_columns(column1, column2):
    """removes 2 columns"""
    df = pd.DataFrame(dict1)
    print(df)
    df.drop(columns=[column1, column2], inplace=True)
    print(f"after dropping {column1} and {column2}: ")
    return df


def split_name_columns():
    """splits name into name and lastname columns"""
    df = pd.DataFrame(dict1)
    print(" ")
    print("before splitting name column:")
    print(" ")
    print(df)
    df[['first_name', 'last_name']] = df['name'].str.split(' ', expand=True)
    print(" ")
    print("after splitting name column and dropping it and ordering the dataframe:")
    print(" ")
    cols = df.columns.tolist()
    cols.remove('first_name')
    cols.remove('last_name')
    cols.insert(0, 'first_name')
    cols.insert(1, 'last_name')
    df = df[cols]
    df.drop(columns=['name'], inplace=True)
    return df


def read_csv_file(file_name):
    """reads a csv file"""
    df = pd.read_csv(file_name, encoding='utf-8')
    print(df)


def modify_dataframe(csv_file):
    # Read the CSV file
    df = pd.read_csv(csv_file)
    #print("Original data:")
    # print(df.head())

    # Add new columns
    df['under_age'] = np.where(df['age'] <= 21, "YES", "NO")


    # Sort the data
    df = df.sort_values('age', ascending=True)
    print(df)
    return df


def save_to_csv_in_place(csv_file):

    df = modify_dataframe(csv_file)
    df.to_csv(csv_file, encoding='utf-8', index=False)


def create_new_csv_from_old(csv_file):
    df = modify_dataframe(csv_file)
    df['under_age'] = np.where(df['age'] <= 21, "Yes", "No")

    df.to_csv('random_people_modified', encoding='utf-8', index=False)



def main():

    csv = "../test_CSVs/random_people.csv"
    print("\n")
    print("1 - Add net salary column with values",end="    ")
    print("2 - Add salary category column with values", end="    ")
    print("3 - Remove columns", end="    ")
    print("4 - Split columns")
    print("5 - Read a CSV file", end="                      ")
    print("6 - Modify dataframe",end="                          ")
    print("7 - Writing back to CSV (in place)")
    print("8 - Create new CSV with modified data from previous CSV")
    print("_______________________________________________")


    try:
        choice = int(input("Choose an algorithm: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    match choice:

        case 1:
            print(add_net_salary_column())

        case 2:
            print(add_salary_category_column())

        case 3:
            print(remove_columns("salary", "tax_percentage"))

        case 4:
            print(split_name_columns())


        case 5:

            read_csv_file(csv)

        case 6:

            modify_dataframe(csv)

        case 7:
            save_to_csv_in_place(csv)

        case 8:
            create_new_csv_from_old(csv)

        case _:
            print("Invalid choice.")

main()