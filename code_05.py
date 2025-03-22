# Question: Pallindrome Number

num=2365654
temp = num
rev = 0

while temp>0:
    d=temp%10
    rev = (rev * 10) + d
    temp = temp // 10
if num == rev:
    print("Pallindrome")
else:
    print("Not Pallindrome")