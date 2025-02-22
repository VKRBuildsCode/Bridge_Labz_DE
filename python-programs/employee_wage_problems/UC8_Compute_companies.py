import random
# Class used for computing employee wages
class EmployeeWageComputation:
    def __init__(self, company_name, hourly_wage, working_days, working_hours):
        self.company_name = company_name
        self.hourly_wage = hourly_wage
        self.working_days = working_days
        self.working_hours = working_hours
    @classmethod
    def display_title(cls):
        print("WELCOME TO EMPLOYEE WAGE COMPUTATION!!!!")
    def check_attendance(self):
        attendance = random.randint(0, 2)
        if attendance == 0:
            print("Employee is Absent")
        elif attendance == 1:
            print("Regular Employee is Present")
        else:
            print("Part-time Employee is Present")
        return attendance

    def calculate_wage(self):
        attendance = self.check_attendance()
        if attendance == 1:
            wage = self.hourly_wage * self.working_hours
            print(f"Wage of the Regular Employee in {self.company_name} is: {wage}")
        elif attendance == 2:
            wage = self.hourly_wage * (self.working_hours / 2)
            print(f"Wage of the Part-time Employee in {self.company_name} is: {wage}")
        else:
            print("Wage of the Employee is: 0")
company1 = EmployeeWageComputation("BridgeLabz", 20, 20, 8)
company2 = EmployeeWageComputation("Google", 200, 10, 5)
EmployeeWageComputation.display_title()
company1.calculate_wage()
company2.calculate_wage()
