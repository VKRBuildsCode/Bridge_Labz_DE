def check_leap_year():
    """
    This function is used to take input(year) from user and
    check whether the year is leap year or not.
    """
    try:
        year = int(input("Please enter a year : "))
        if (year % 100):
            if (year % 400):
                print(f"Yes, {year} is a leap year")
            else:
                print(f"No, {year} is not an leap year")
        else:
            if (year % 400):
                print(f"Yes, {year}it is a leap year")
            else:
                print(f"No, {year} is not an leap year")
    except ValueError as e:
        print(e)
        print("Try again...")
        check_leap_year()
#Calling function of leap year
check_leap_year()