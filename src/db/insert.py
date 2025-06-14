from db.connect import cursor, conn
from itertools import product
from utils.string_utils import *
# === ===
def generate_table_values(df, columns_db,  prefix="ID", just_ids=False):
    """
    """ 
    unique_list = [
        [val.item() if hasattr(val, "item") else val for val in df[snake_to_pascal(col)].unique()]
        for col in columns_db
    ]

    combos = list(product(*unique_list))
    
    if just_ids:
        return [f"{prefix}{i}" for i in range(1, len(combos) + 1)]

    result = []
    
    for i, combo in enumerate(combos, start=1):
        entry = {"id": f"{prefix}{i}"}
        entry.update(dict(zip(columns_db, combo)))
        result.append(entry)
    print(result) 
    return result
    
#
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


