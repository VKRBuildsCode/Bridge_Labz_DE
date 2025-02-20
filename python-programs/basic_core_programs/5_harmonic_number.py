
#The nth harmonic number is the sum of the reciprocals of the first n natural numbers
def nth_harmonic_number():
    nth_num=0
    try:
        nth_num = int(input("Enter a number : "))
    except ValueError:
        print("Try again, something gone wrong.")
        nth_harmonic_number()
    finally:
        harmonic_number=0
        numbers = [1 / i for i in range(1, nth_num + 1)]
        for i in numbers:
            harmonic_number+=i
        print(f"The {nth_num}th harmonic number is {harmonic_number:.4f}")
nth_harmonic_number()