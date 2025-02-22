#Finding  roots of quadratic equation
def find_roots(a,b,c):
    delta = (b * b) - 4 * a * c
    Root_1x = (-b + delta ** 0.5) / 2 * a
    Root_2x = (-b - delta ** 0.5) / 2 * a
    print(f"The two roots of the equation {a}x^2 + {b}x + {c} are : {Root_1x } and {Root_2x}")
a=int(input("Enter first number"))
b=int(input("Enter second number"))
c=int(input("Enter third number"))

#Calling function here
find_roots(a,b,c)