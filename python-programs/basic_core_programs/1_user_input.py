def print_user_input():
    """
    This function is used to take username as input from user, and greet user
    """
    user_name = input("Please enter your username : ")
    if len(user_name)>2:print(f"👋 Hello {user_name}, How are you? ☺️")
    else:
        print(f"Sorry username can't be less than three characters")
        print("Try again !!!")
        print_user_input()
#Calling the function here
print_user_input()

