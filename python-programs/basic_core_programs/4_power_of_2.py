def print_power_of_2():
    num = int(input("Enter a number N :"))
    if(num>31):
        print("Only works if 0 <= N < 31 since 2^31 overflows an int")
        print_power_of_2()
    else:
        print("""A table of the powers of 2 that are less than or equal to 2^N are""")
        #Dictionary comprehension
        result={print(f"2^{i}:{2**i}") for i in range(1,num+1)}


    pass
print_power_of_2()