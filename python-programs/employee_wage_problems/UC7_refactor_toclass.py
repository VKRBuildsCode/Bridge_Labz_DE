import random

#Refactored to class
# Class used for computing employee wages
class EmployeeWageComputation:
    def __init__(self):
        self.hourly_rate = 20
    def display_title(self):
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
            wage = self.hourly_rate * 8
            print(f"Wage of the Regular Employee is: {wage}")
        elif attendance == 2:
            wage = self.hourly_rate * 4
            print(f"Wage of the Part-time Employee is: {wage}")
        else:
            print("Wage of the Employee is: 0")
employee_wage_computation = EmployeeWageComputation()
employee_wage_computation.display_title()
employee_wage_computation.calculate_wage()
