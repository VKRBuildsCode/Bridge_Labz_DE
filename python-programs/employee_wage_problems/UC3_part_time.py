from random import random

print("WELCOME TO EMPLOYEE WAGE COMPUTATION!!!!")
#Function to check the attendance of the employee and parameters
def Check_Attendance():
    attendace = random.randint(0,2)
    if attendace == 0:
        print("Employee is Absent")
    elif attendace == 1:
        print("Regular Employee is Present")
    else:
        print("Partime Employee is Present")
    return attendace

#Calculating the wage of the employee and parameters
def calculate_wage():
    attendance = Check_Attendance()

    if attendance == 1:  # Regular Employee
        wage = 20 * 8
        print(f"Wage of the Regular Employee is: {wage}")
    elif attendance == 2:  # Part-time Employee
        wage = 20 * 4
        print(f"Wage of the Part-time Employee is: {wage}")
    else:  # Absent
        print("Wage of the Employee is: 0")
calculate_wage()
