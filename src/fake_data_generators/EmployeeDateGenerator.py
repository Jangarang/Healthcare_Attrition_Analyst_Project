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

    def run(self):
        self._generate_fake_managers()
        self._assign_managers()
        self._calculate_max_years_per_manager()
        self._assign_manager_start_dates()

