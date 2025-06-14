import psycopg2

try:
    conn = psycopg2.connect(
        dbname="Hospital Workforce",
        user="postgres",
        password="password",
        host="localhost",
        port="5432"
    )
    if conn:
        print("✅ Database connection established")
    cursor = conn.cursor()
except psycopg2.Error as e:
    print(f"Error connecting to database: {e}")

