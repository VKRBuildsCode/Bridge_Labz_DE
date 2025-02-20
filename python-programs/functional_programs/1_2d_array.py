
def print_2d_array(rows,columns):
    array=[]
    print(f"Enter the values of the 2d array ,with {rows} rows and {columns} columns")
    for row in range(0,rows):
        x=[]
        for column in range(0,columns):
            x.append(int(input(f"Enter the value for array[{row}][{column}] : ")))
        array.append(x)
    print("The final array is : ",end=" ")
    print(array)
rows=int(input("Enter the number of rows : "))
columns=int(input("Enter the number of columns : "))
print_2d_array(rows,columns)