from db.connect import cursor, conn
from utils.string_utils import *

from db.generate_table_data import *

# === ===
    
#
def insert_lookup_table(df, table_name, columns_db, prefix="ID"):
    """
    Args:
    - table_name(string): Name of table 
    - columns_db(list[string]): Names of relevant columns 
    """
    columns_str = ', '.join(columns_db)
    # print(columns_str)    
    data = generate_lookup_table_values(df, columns_db, prefix) # [{},{}]
    data_length_tuple = len(data[0])
    placeholders = ', '.join(['%s'] * data_length_tuple)
    values_tuple = [tuple(d.values()) for d in data] 

    query = f"INSERT INTO {table_name} (id, {columns_str}) VALUES ({placeholders})"

    cursor.executemany(query, values_tuple)

    conn.commit() 

def insert_into_employee_table(df):
    """
    Insert data into employee table.

    Parameters:
        - df (dataframe): The dataframe from csv file.
    """
    df_relevant = df[['MaritalStatus']]
    records = df.to_records(index=False)
    values = list(records)

    columns = ', '.join(df.columns)

    # placeholders for query
    placeholders = ', '.join(['%s'] * len(df.columns))
    # query = f"INSERT INTO {}"
 
# === Helper Functions ===
def insert_into_department_table(df):
    """
    """
