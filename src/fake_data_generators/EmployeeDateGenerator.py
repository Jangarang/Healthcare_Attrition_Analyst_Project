from datetime import datetime
import random
from datetime import datetime, timedelta
__all__ = ['get_fake_managers','run','EmployeeDateGenerator']

class EmployeeDateGenerator:
    def __init__(self, df, reference_date=datetime(2025, 6, 1)):
        self.employee_df = df[['EmployeeID', 'Age','Department', 'Attrition', 'YearsWithCurrManager','YearsAtCompany','YearsInCurrentRole']].copy()
        self.manager_pool = []
        self.reference_date = reference_date
        
    def _generate_fake_managers(self):
        departments = self.employee_df['Department'].unique()
        for dept in departments:
            for i in range(1,3):
                self.manager_pool.append({
                    "ManagerID": f"{dept[:2].upper()}M{i}",
                    "Department": dept,
                    "Name": f"{dept} Manager {i}", 
                }) 

    def _assign_managers(self):
        for index,row in self.employee_df.iterrows(): # iterrows creates a copy
            dept = row["Department"]
            eligible_managers = [m for m in self.manager_pool if m["Department"] == dept]
            chosen_manager = random.choice(eligible_managers)
            self.employee_df.loc[index,"ManagerID"] = chosen_manager["ManagerID"] # It lets you access and modify data in your DataFrame based on labels

        return self.employee_df[['EmployeeID','ManagerID']]

    def _calculate_max_years_per_manager(self):
        for _,emp in self.employee_df.iterrows():
            mgr_id = emp['ManagerID']
            years = emp['YearsWithCurrManager']
            for mgr in self.manager_pool:
                if mgr['ManagerID'] == mgr_id:
                    mgr['MaxYears'] = max(mgr.get('MaxYears',0), years)
        
    def _assign_manager_start_dates(self):
        for mgr in self.manager_pool:
            max_years = mgr['MaxYears']
            buffer = random.randint(0, 90)
            start = self.reference_date - timedelta(days=int(max_years * 365 + buffer))
            mgr['StartDate'] = start.strftime("%Y-%m-%d")

    def get_fake_managers(self):
        return self.manager_pool
    
    def get_fake_managers_and_department(self):
        return [{'Manager': m['ManagerID'],'Department:': m['Department']} for m in self.manager_pool]

    def get_fake_managers_start_dates(self):
        return [{ 'ManagerID': m['ManagerID'], 'StartDate:': m['StartDate']} for m in self.manager_pool]

    def get_employee_and_manager(self):
        return self._assign_managers()

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
    def run(self):
        self._generate_fake_managers()
        self._assign_managers()
        self._calculate_max_years_per_manager()
        self._assign_manager_start_dates()

