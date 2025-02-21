import UC1_
def calculate_wage():
    attendance = UC1_.Check_Attendance()
    match attendance:
        case 1:
            wage = 20 * 8
            print(f"Wage of the Employee is: {wage}")
        case 2:
            wage = 20 * 4
            print(f"Wage of the Partime Employee is: {wage}")
        case _:
            print("Wage of the Employee is: 0")
