id_serial = 'id SERIAL PRIMARY KEY'

marital_status_enum_name = 'marital_status_enum'
satisfaction_enum_name = 'satisfaction_enum'
shift_enum_name = 'shift_enum'
business_travel_enum_name = 'business_travel_enum'

# === table enums ===

marital_status = ['Married', 'Single', 'Divorced']
satisfaction = ['Environment', 'Job', 'Relationship']
shift = ['Morning', 'Afternoon', 'Evening', 'Graveyard']
business_travel = ['Non_Travel', 'Travel_Frequently', 'Travel_Rarely']

# === table schemas ===
education_schema = {
    'id': id_serial,
    'education_level': 'INTEGER',
    'education_field': 'TEXT'
}

employee_schema = {
    'id': id_serial,
    'birthdate': 'DATE',
    'marital_status': 'marital_status_enum',
    'employment_start_date': 'DATE',
    'distance_from_home': 'INTEGER', 
    'job_title_id': 'INTEGER REFERENCES job_title(id)',
    'department_id': 'INTEGER REFERENCES department(id)',
    'gender_id': 'INTEGER REFERENCES gender(id)',
    'education_id': 'INTEGER REFERENCES education(id)'
}

job_title_history_schema = {
    'id': id_serial,
    'job_title_id': 'INTEGER REFERENCES job_title(id)',
    'employee_id': 'INTEGER REFERENCES employee(id)',
    'start_date': 'DATE'
}

satisfaction_schema = {
    'id': id_serial,
    'type': 'satisfaction_enum',
    'score': 'INTEGER'
}

employment_terms_schema = {
    'id': id_serial,
    'employee_id': 'INTEGER REFERENCES employee(id)',
    'employment_start_date': 'DATE',
    'employment_end_date':'DATE' ,
    'last_salary_promotion_date': 'DATE'
}

shifts_schema = {
    'id': id_serial,
    'employee_id': 'INTEGER REFERENCES employee(id)',
    'business_travel': 'TEXT',
    'shift_type': 'shift_type_enum',
    'overtime': 'INTEGER'
} 

department_history_table_schema = {
    'id': id_serial,
    'department_id': 'INTEGER REFERENCES department(id)',
    'employee_id': 'INTEGER REFERENCES employee(id)',
    'start_date': 'DATE'''
}

create_salary_payment_schema = {
    'id': id_serial,
    'employee_id': 'INTEGER REFERENCES employee(id)',
    'monthly_income': 'INTEGER'
}

create_salary_adjustment_table = {
    'id': id_serial,
    'salary_payment_id': 'INTEGER REFERENCES salary_payment(id)',
    'adjustment_amount': 'INTEGER'
}