#1
def calculate_area(base,height,type):
    if type=="rectangle":
        return base*height
    else:
        return (1/2)*base*height


print(calculate_area(2,3,"rectangle"))

#3
def print_pattern(num):
    for i in range(1,num+1):
        j=""
        for a in range(i):
            j+="*"
        print(j)


print_pattern(5)