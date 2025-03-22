#question: perfect square 
from math import sqrt

def isPerfectSquare(x):
    if x>=0:
        sr = int(sqrt(x))
        return (sr * sr) == x
    return False

n = 67
if isPerfectSquare(n):
    print("True")
else:
    print("False")