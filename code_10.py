# question : Strong Number
# if the sum of factorial of the digits is equal to the number itself- strong number

def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact *= i
    return fact

def is_strong_number(num):
    temp = num
    sum_fact = 0

    while temp > 0:
        d = temp%10
        sum_fact += factorial(d)
        temp //= 10
    
    return sum_fact == num

num = int(input("Enter a number"))

if is_strong_number(num):
    print(f"{num} is a strong number")
else:
    print(f"{num} is not a strong number")