from utils.string_utils import *
from itertools import product

def generate_lookup_table_values(df, columns_db,  prefix="ID", just_ids=False):
    """
    Fills in table that has a combination of values. 
    Does not require data from rows in csv file.

    Args:
    - df: csv dataframe object
    - columns_db(list): names of relevant column names
    - just_ids(boolean): Return ids only or not

    Returns:
    - A list of objects.
    """ 
    unique_list = [
        [val.item() if hasattr(val, "item") else val for val in df[snake_to_pascal(col)].unique()]
        for col in columns_db
    ]
    
    combos = list(product(*unique_list))

    if just_ids:
        # return [f"{prefix}{i}" for i in range(1, len(combos) + 1)]
        return [i for i in range(1, len(combos) + 1)]

    result = []
    
    for i, combo in enumerate(combos, start=1):
        # entry = {"id": f"{prefix}{i}"}
        entry = {"id": i}
        entry.update(dict(zip(columns_db, combo))) # Creates two seperate dictionaries 
        result.append(entry)
   
    return result