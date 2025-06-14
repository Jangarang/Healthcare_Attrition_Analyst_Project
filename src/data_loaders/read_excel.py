import pandas as pd

def load_excel(file_path):
    try:
        df = pd.read_excel(file_path,engine='openpyxl')
        print("Excel file loaded successfully!")
        return df
    except Exception as e:
        print(f"Failed to load Excel file")
        return None

def create_excel_obj(file_path):
    try: 
        xls = pd.ExcelFile(file_path)
        print("Excel object created")
        return xls
    except Exception as e:
        print("Failed to create excel object")
        return None