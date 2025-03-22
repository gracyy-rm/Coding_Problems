# Question : Prime number within a given range
low, high = 2, 13
primes=[]

for num in range(low,high+1):
    flag=0
    if num <2:
       continue

    if num == 2:
        primes.append(2)
        continue

    for x in range(2,num):
        if num % x == 0:
            flag = 1
            break

    if flag == 0:
        primes.append(num)

print(primes)