import pyreadstat
import pandas as pd

def create_sav_object(file_path):
    try: 
        df, meta = pyreadstat.read_sav(file_path)
        print("Created sav object correctly")
        return df, meta
    except Exception as e:
        print(f"Error creating save object {e}") 