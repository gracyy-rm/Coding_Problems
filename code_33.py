# Question: Finding the roots of the quadratic equation

import math

def findRoots(a,b,c):

    if a ==0:
        print("Invalid")
        return -1
    d = b * b -4 * a * c 
    sqrt_val= math.sqrt(abs(d))

    if d >0:
        print("Roots are real and different ")
        print((-b + sqrt_val)/(2 * a))
        print((-b - sqrt_val)/(2 * a))
    elif d == 0:
        print("Roots are real and same")
        print(-b/(2 * a))
    else:
        print("Roots are complex")
        print(f"{-b/(2 * a)} + i {sqrt_val}")
        print(f"{-b/(2 * a)} -i {sqrt_val}")

a=1
b=4
c=4

findRoots(a, b, c)