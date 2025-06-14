import random
from datetime import datetime, timedelta

reference_date = datetime(2022, 1 ,1)

def random_date_back(years_ago: int):
    # Pick a random date within the year range ago
    days = random.randint(0, 364)
    return reference_date - timedelta(days=int(years_ago * 365 + days))

def generate_dates(row):
    hire_date = random_date_back(row["YearsAtCompany"])
    
    role_years = min(row["YearsInCurrentRole"], row["YearsAtCompany"])
    role_start = random_date_back(role_years)
    role_start = max(role_start, hire_date)  # ensure it's not before hire
    
    manager_years = min(row["YearsWithCurrManager"], row["YearsAtCompany"])
    manager_start = random_date_back(manager_years)
    manager_start = max(manager_start, hire_date)

    return {
        "HireDate": hire_date.date(),
        "RoleStartDate": role_start.date(),
        "ManagerStartDate": manager_start.date()
    }

def generate_dates_manager(row):
    hire_date = random_date_back(row["YearsAtCompany"])

    manager_years = min(row["YearsWithCurrManager"], row["YearsAtCompany"])
    manager_start = random_date_back(manager_years)
    manager_start = max(manager_start, hire_date)


test_employees = [
    {
        "Name": "Alice",
        "YearsAtCompany": 5,
        "YearsInCurrentRole": 3,
        "YearsWithCurrManager": 2
    },
    {
        "Name": "Bob",
        "YearsAtCompany": 10,
        "YearsInCurrentRole": 7,
        "YearsWithCurrManager": 5
    },
    {
        "Name": "Charlie",
        "YearsAtCompany": 1,
        "YearsInCurrentRole": 1,
        "YearsWithCurrManager": 1
    },
    {
        "Name": "Dana",
        "YearsAtCompany": 8,
        "YearsInCurrentRole": 2,
        "YearsWithCurrManager": 4
    }
]

# for employee in test_employees:
#     dates = generate_dates(employee)
#     print(f"{employee['Name']} - HireDate: {dates['HireDate']}, RoleStartDate: {dates['RoleStartDate']}, ManagerStartDate: {dates['ManagerStartDate']}")

