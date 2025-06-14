from db.connect import cursor, conn

# === Leaf Tables ===
def create_job_title_table():
    """
    Creates the 'job_title' table.
    This is a lookup table containing the job titles.
    """
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS job_title (
            id SERIAL PRIMARY KEY,
            occupation_name TEXT
        );
    """)

def create_department_table():
    """
    Creates the 'department' table.
    This is a lookup table containing all departments.
    """
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS department (
            id SERIAL PRIMARY KEY,
            department_name TEXT
        );
    """)

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
    create_job_title_table()
    create_department_table()
    create_education_table()
    create_gender_table()

# === Enums ===
def create_enum_tables():
    """
    Creates custom ENUMS types for:
    - marital_status_enum
    - satisfaction_enum
    - shift_enum
    """

    # Marital Status
    cursor.execute("""
        DO $$
        BEGIN
            IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'marital_status_enum') THEN
                CREATE TYPE marital_status_enum AS ENUM ('Married', 'Single', 'Divorced');
            END IF;
        END
        $$;
    """)

    # Statisfaction 
    cursor.execute("""
        DO $$
        BEGIN
            IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'satisfaction_enum') THEN
                CREATE TYPE satisfaction_enum AS ENUM ('environment','job','relationship');
            END IF;
        END
        $$;
    """) 

    # Shift 
    cursor.execute("""
        DO $$
        BEGIN
            IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'shift_type_enum') THEN
                CREATE TYPE shift_type_enum AS ENUM ('morning','afternoon','evening','graveyard');
            END IF;
        END
        $$;
    """)

    # Business Travel
    cursor.execute("""
        DO $$
        BEGIN
            IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'business_travel_enum') THEN
                CREATE TYPE business_travel_enum AS ENUM ('Non_Travel','Travel_Frequently','Travel_Rarely');
            END IF;
        END
        $$;
    """)

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

def create_tables():
    create_leaf_tables()
    
    create_enum_tables()
    
    create_employees()
    
    create_relational_tables()

    conn.commit()