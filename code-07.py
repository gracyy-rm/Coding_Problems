# question: Armstring Number in a given interval
low, high = 10, 100001
for n in range(low,high+1):
    order=len(str(n))
    s = 0
    
    temp =n 
    while temp> 0:
        digit= temp%10
        s += digit ** order
        temp //= 10
    if n == s:
        print(n, end = " , ")