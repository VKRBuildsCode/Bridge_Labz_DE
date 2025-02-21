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
Check_Attendance()