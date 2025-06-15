from db.connect import conn
from db.setup.create_tables import *
from db.delete_tables import reset_database
from data_loaders.read_excel import load_excel, create_excel_obj
from data_loaders.read_csv import create_csv
from fake_data_generators.EmployeeDateGenerator import EmployeeDateGenerator
from db.setup.insert import *
from db.setup.generate_table_data import *
import os
import pandas as pd
import random
from datetime import datetime, timedelta

# To be decided
canada_xlsx_path = "health-workforce-canada-2019-2023-overview-data-tables-en.xlsx"
uk_xlsx_path = "Healthcare Workforce Statistics, England March 2019.xlsx"
iranian_sav_path = "mental health Dataset.sav"
canadian_csv_path = "health_dataset.csv"

# Relevant datasets 
health_workforce_mental_health_path = "Healthcare Workforce Mental Health Dataset.csv"
health_worforce_attrition = "watson_healthcare_modified.csv"

def xls_viewer(file_path):
    df = load_excel(file_path)

    if df is not None:
        print(df.head())
        
    xls = create_excel_obj(file_path) 

    xls_sheets = 0

    if xls is not None:
        xls_sheets = xls.sheet_names

    if len(xls.sheet_names) > 0:
        print(f"The number of sheets is {xls_sheets}")
        print(xls.parse('Table 7').iloc[0].tolist())
        # print(xls.parse('Table 1').iloc[:,3])
        # print(xls.parse(('Table 1'), header=None))
        

def csv_viewer(path):
    df = create_csv(path) 

    if df is None: 
        print("df is none")
    
    # print(df.head())
    # print(df.columns.str.strip())
 

'''
Entry Point 
'''
def main():
    base_dir = os.path.dirname(__file__)
    
    file_path_attrition = os.path.join(base_dir, f"datasets/{health_worforce_attrition}") 

    df_attrition = create_csv(file_path_attrition) # Creates a dataframe

    generator = EmployeeDateGenerator(df_attrition)
    generator.run()
    # print(generator.get_fake_managers_start_dates())
    
    
    # print(create_table('hello',{'id': 'SERIAL PRIMARY KEY','birthdate': 'DATE'}))
    # print(create_enum_table('hello',['Married','Single'])) 
    # create_enum_tables()
    
    # ===== /db =====

    # === create&resest db ===

    create_tables()
    # reset_database()
    # === TESTING db/insert.py ===
    # print(insert_into_employee_table(df_attrition))
    # print(generate_table_values(df_attrition,['education', 'education_field'], prefix='EDU'))
    insert_lookup_table(df_attrition, 'job_role', ['job_role'])

if __name__ == "__main__":
    main()