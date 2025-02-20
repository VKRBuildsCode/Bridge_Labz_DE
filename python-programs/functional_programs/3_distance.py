from math import sqrt
def calculate_euclidean_distance(x,y):
    euclidean_distance = sqrt(pow(x, 2) + pow(y, 2))
    return  euclidean_distance
x=int(input("Enter the coordinate point of x axis :"))
y=int(input("Enter the coordinate point of y axis :"))
print(f"The euclidean distance from the point({x},{y}) to the origin(0,0) is {calculate_euclidean_distance(x,y)}")