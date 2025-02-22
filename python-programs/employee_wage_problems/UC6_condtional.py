from random import random

total_working_hours=100

total_days=20

print("WELCOME TO EMPLOYEE WAGE COMPUTATION!!!!")
#Function to check the attendance of the employee with parameters provided
def Check_Attendance():
    attendace = random.randint(0,2)
    if attendace == 0:
        print("Employee is Absent")
    elif attendace == 1:
        print("Regular Employee is Present")
    else:
        print("Partime Employee is Present")
    return attendace

#Calculating the wage of the employee with parameters provided
def calculate_wage_on_condition(days,hours):
    attendance = Check_Attendance()

    match attendance:
        case 1:
            wage = 20 * 8
            print(f"""Wage of the Employee is till a condition of total working hours: {wage*hours}""")
            print(f"""Wage of the Employee is till a condition of days is reached for a month - Assume 100 hours: {wage * days}""")
        case 2:
            wage = 20 * 4
            print(f"""Wage of the Employee is till a condition of total working hours: {wage*hours}""")
            print(f"""Wage of the Employee is till a condition of days is reached for a month - Assume 100 hours: {wage * days}""")
        case _:
            print(f"""Wage of the Employee is till a condition of total working hours: {wage * hours}""")
            print(
                f"""Wage of the Employee is till a condition of days is reached for a month - Assume 100 hours: {wage * days}""")
#Invoking the function from here
calculate_wage_on_condition(total_days,total_working_hours)