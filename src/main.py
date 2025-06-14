from db.connect import conn
from db.create_tables import create_tables
from db.delete_tables import reset_database
from data_loaders.read_excel import load_excel, create_excel_obj
from data_loaders.read_sav import create_sav_object
from data_loaders.read_csv import create_csv
from fake_data_generators.EmployeeDateGenerator import EmployeeDateGenerator
from db.insert import *

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


    # print(generator.get_fake_managers())
    # print(generator.get_employee_and_manager())
    print(generator.get_fake_managers_start_dates())

    print(insert_into_employee_table(df_attrition))
    generate_table_values(df_attrition,['education', 'education_field'], prefix='EDU')
    # Step 5 Generate manager start dates based on that 
     
    # for index,emp in employee_list.iterrows():
    #     years_at_company = emp['YearsAtCompany']
    #     years_with_mgr = emp['YearsWithCurrManager']
    #     years_in_role = float(emp['YearsInCurrentRole'])

    #     # Add some realism/randomness
    #     buffer_company = random.randint(0, 60)
    #     buffer_mgr = random.randint(0, 30)
    #     buffer_role = random.randint(0, 30)

    #     # Start date at company
    #     start_offset_days = int(years_at_company * 365) + buffer_company
    #     start_date = reference_date - timedelta(days=start_offset_days)
    #     start_with_role = reference_date - timedelta(days=int(years_in_role * 365 + buffer_role))

    #     # If employee left create end date
    #     if (emp['Attrition'] == 'Yes'):
    #         end_date = start_date + timedelta(days=years_at_company)
    #         employee_list.loc[index,'EndDate'] = end_date.strftime("%Y-%m-%d")

    #     # Start date with manager
    #     mgr_offset_days = int(years_with_mgr * 365) + buffer_mgr
    #     start_with_mgr = reference_date - timedelta(days=mgr_offset_days)

    #     start_with_mgr = max(start_with_mgr, start_date)
    #     start_with_role = max(start_with_role, start_date)

    #     # Final result
    #     employee_list.loc[index,'StartDate'] = start_date.strftime("%Y-%m-%d")
    #     employee_list.loc[index,'StartDateWithManager'] = start_with_mgr.strftime("%Y-%m-%d")
    #     employee_list.loc[index,'StartDateWithCurrentRole'] = start_with_role.strftime("%Y-%m-%d")
    
    # Step 6 Generate birthdates of 

    # Create tables 
    #create_tables()
    #reset_database()


if __name__ == "__main__":
    main()