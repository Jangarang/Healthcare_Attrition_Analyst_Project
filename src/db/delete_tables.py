from db.connect import cursor, conn

def reset_database():
    cursor.execute("""
        DROP TABLE IF EXISTS employee, 
            education, 
            employment_terms, 
            job_title, 
            job_title_history, 
            satisfaction,
            shifts,
            salary_payment,
            salary_adjustment,
            gender,
            department,
            department_history 
        CASCADE;
    """)
    
    cursor.execute("""
        DROP TYPE IF EXISTS
            business_travel_enum,
            marital_status_enum,
            satisfaction_enum,
            shift_enum,
            shift_type_enum
        """)

    conn.commit()