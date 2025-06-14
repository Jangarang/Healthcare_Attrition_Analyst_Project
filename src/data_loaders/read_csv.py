import pandas as pd 

def create_csv(file):
    try:
        df = pd.read_csv(file)
        return df 
    except Exception as e: 
        print(f"Error creating csv file {e}")
        return None