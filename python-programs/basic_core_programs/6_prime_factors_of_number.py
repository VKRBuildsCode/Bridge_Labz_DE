prime_factors=[]
product=[]
def is_prime(num):
    i=2
    while i*i<=num:
        if num%i==0:
            return False
        i=i+1
    return True
def print_prime_factors_of(num):
    prime_factors=[i for i in range(2,num+1) if num%i==0 and is_prime(i)]
    if len(prime_factors)==1:print(f"The prime factor of number {num} is {prime_factors[0]}")
    else: print(f"The prime factors of number {num} are {prime_factors}")
def product_of_prime_factors(num):
    i=0
    while(True):
        if num in prime_factors:
            product.append(num)
        elif(num%i==0):
            product.append(num)
def get_number():
    try:
        num=int(input("Please enter a number : "))
        if num==1:
            print(f"1 is neither prime nor composite")
        elif num<1:
            print("A number is prime or composite is a property defined for positive integers only")
            print("Try again ....")
            get_number()
        else:
            print_prime_factors_of(num)
    except ValueError as e:
        print(e)
        print("Try again ....")
        get_number()
get_number()
