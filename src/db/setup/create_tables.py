from db.connect import cursor, conn
from db.schemas import *

def create_table(table_name,schema_dict=None,*args):
    """
    """
    if schema_dict is None:
        return ''
    
    columns = ', '.join(f"{col} {dtype}" for col, dtype in schema_dict.items()) 
    
    try:
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns});")
        return True
    except:
        return False

# === Leaf Tables ===
def create_education_table():
    """
    Creates the 'education' table.
    This is a lookup table containing education types and their levels.
    """
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS education (
            id SERIAL PRIMARY KEY,
            education_level INTEGER,
            education_field TEXT
            );
    """)

def create_gender_table():
    """
    """
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS gender (
            id SERIAL PRIMARY key,
            gender TEXT
        )
""")

def create_leaf_tables():
    # Create job_role table
    if create_table('job_role',basic_schema('job_role','TEXT')) == False:#TODO create a variable
        print('create_leaf_tables error job_role table')
    # Create education_table
    if create_table('education', education_schema) == False:
        print('create_leaf_tables() error education table')
    # Create gender_table
    if create_table('gender', basic_schema('gender', 'TEXT')) == False:
        print('create_leaf_tables() error gender table')

# === Enums ===

def create_enum_table(table_name, schema_enum_list=None):
    """
    """

    columns = ', '.join(f"'{col}'" for col in schema_enum_list) 

    query = f"""
    DO $$
    BEGIN
        IF NOT EXISTS (
            SELECT 1 FROM pg_type WHERE typname = '{table_name}'
        ) THEN
            CREATE TYPE {table_name} AS ENUM ({columns});
        END IF;
    END
    $$;
    """
    return query

def create_enum_tables():
    """
    """
    cursor.execute(create_enum_table(marital_status_enum_name, marital_status))
    cursor.execute(create_enum_table(satisfaction_enum_name, satisfaction))
    cursor.execute(create_enum_table(shift_enum_name, shift))
    cursor.execute(create_enum_table(business_travel_enum_name, business_travel))
    conn.commit()

# === Core Table ===
def create_employees():
    """
    Creates the core 'employee' table, containing primary information:
    - employee demographics
    - job metadata
    - shift
    - satisfaction

    Forein Keys:
    - job_title_id -> job_title(id)
    - department_id -> department(id)

    Enum:
    - marital_status -> marital_status_enum

    """
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employee (
            id SERIAL PRIMARY KEY,
            birthdate DATE,
            marital_status marital_status_enum,
            employment_start_date DATE,
            distance_from_home INTEGER, 
            job_title_id INTEGER REFERENCES job_title(id),
            department_id INTEGER REFERENCES department(id),
            gender_id INTEGER REFERENCES gender(id),
            education_id INTEGER REFERENCES education(id)
        );
    """) 
   
# === Relation Tables ===
def create_job_title_history():
    """
    Creates the 'job_title_history' table.

    This table represents employee start date of employees and 
    depends on the existence of:

    - 'employee' (employee_id FOREIGN KEY)
    - 'job_title' (job_title_id FOREIGN KEY)

    Constraints:
    - 'job_title' -> must be created before this table
    ' 'employee' -> must be created before this table
    """
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS job_title_history (
            id SERIAL PRIMARY KEY,
            job_title_id INTEGER REFERENCES job_title(id),
            employee_id INTEGER REFERENCES employee(id),
            start_date DATE
        );
""")
    
def create_satisfaction_table():
    """
    This table represents employee's satisfaction based on `satisfaction_enum` and 
    depends on the existence of:
    - 'employee' (employee_id )
    -

    """
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS satisfaction (
            id SERIAL PRIMARY KEY,
            type satisfaction_enum,
            score INTEGER
        );
    """)

def create_employment_terms_table():
    """
    """
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employment_terms (
            id SERIAL PRIMARY KEY,
            employee_id INTEGER REFERENCES employee(id),
            employment_start_date DATE,
            employment_end_date DATE,
            last_salary_promotion_date DATE
        );    
""")

def create_shifts_table():
    """
    """
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS shifts (
            id SERIAL PRIMARY KEY,
            employee_id INTEGER REFERENCES employee(id),
            business_travel TEXT,
            shift_type shift_type_enum,
            overtime INTEGER
        );
    """)

def create_department_history_table():
    """
        Creates the 'department_history' table.

        This table represents the start date an employee worked in a department
        and depends on the existence of:

        - 'employee' (employee_id FOREIGN KEY)
        - 'department' (department_id FOREIGN KEY)

        Constraints:
        - 'department' -> must be created before this table
        - 'employee' -> must be created before this table
    """
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS department_history (
            id SERIAL PRIMARY KEY,
            department_id INTEGER REFERENCES department(id),
            employee_id INTEGER REFERENCES employee(id),
            start_date DATE
        );
    """)

def create_salary_payment_table():
    """
    Constraints: 
    - 'employee' -> must be created before this table
    """
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS salary_payment (
            id SERIAL PRIMARY KEY,
            employee_id INTEGER REFERENCES employee(id),
            monthly_income INTEGER
    );
    """)

def create_salary_adjustment_table():
    """
    """
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS salary_adjustment (
        id SERIAL PRIMARY KEY,
        salary_payment_id INTEGER REFERENCES salary_payment(id),
        adjustment_amount INTEGER       
    );
""")

def create_relational_tables():
    create_job_title_history()
    create_satisfaction_table()
    create_employment_terms_table()
    create_shifts_table()
    create_department_history_table()
    create_salary_payment_table()
    create_salary_adjustment_table()

# def create_tables():
#     create_leaf_tables()
    
#     create_enum_tables()
    
#     create_employees()
    
#     create_relational_tables()

#     conn.commit()
def create_tables():
    """
    """
    # def create_table(table_name,schema_dict=None,*args):
    create_leaf_tables()  
    conn.commit()