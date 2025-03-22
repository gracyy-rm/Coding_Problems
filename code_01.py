# Question: Find the sum of N natural numbers
number=int(input("Enter the number for sum"))
s=0
for i in range(number+1):
    s += i
print(s)