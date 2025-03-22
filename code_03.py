# Question : Greatest of three numbers
num1, num2, num3 = 45, 30, 20
maxx = num1 if num1>num2 else num2
maxx = num3 if num3>maxx else maxx
print(maxx)
