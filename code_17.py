# highest common factor
num1=36
num2=60
a=num1
b=num2

while num1 != num2:
    if num1 > num2:
        num1 -= num2
    else:
        num2 -= num1

print("HCF of ", a, "and",b, "is", num1)