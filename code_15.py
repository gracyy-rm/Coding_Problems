# question :  Abundant number
n=12
s = 1

for i in range(2,n):
    if(n%i==0):
        s=s+i
if(s>n):
    print(n,"is abundant number")
else:
    print(n,"is not abundant number")