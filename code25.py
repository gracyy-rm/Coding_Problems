# Addition of two fractions
import math 
def add_fractions(a,b,c,d):
    num=a*d + b*c
    den = b*d

    gcd=math.gcd(num,den)
    num //= gcd
    den //= gcd
    
    return f"{num}/{den}"

a,b=map(int, input("enter first fraction (numerator denominator): ").split())
c,d=map(int, input("enter second fraction (numerator denominator): ").split())

print(f"sum of fractions: {add_fractions(a,b,c,d)}")