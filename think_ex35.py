def grid_rows(x):
    #creates the designated number of spaces in a row
    unit = ['+', '-', '-', '-', '-', '+']
    unit2 = ['+', '-', '-', '-', '-', '+']
    out = ''
    for x in range(x-1):
        unit2.extend(unit[1:])
    print out.join(unit2)

def grid_columns(x):
    #default characters for grid "columns"
    unit = ['|',' ', ' ', ' ', ' ', '|']
    unit2 = ['|',' ', ' ', ' ', ' ', '|']
    out = ''
    for x in range(x-1):
        unit2.extend(unit[1:])
    for i in range(2):
        print out.join(unit2)



def grid_func1(x, y):
    #takes dimensions as an argument and then prints a grid those dimensions,
    for i in range(y):
        grid_rows(x)
        grid_columns(x)
    grid_rows(x)



#execution
d = input("How many Columns?: ")
p = input("How many Rows?: ")

grid_func1(d, p)
