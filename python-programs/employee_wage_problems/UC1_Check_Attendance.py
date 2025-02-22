from random import randint

#Function used to check attendance
def check_attendance():
    attendance = randint(0, 2)
    if attendance == 0:
        print("Employee is Absent")
    elif attendance == 1:
        print("Regular Employee is Present")
    else:
        print("Part-time Employee is Present")
    return attendance
check_attendance()