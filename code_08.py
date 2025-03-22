# question: factor of the number
def printDivisor(n):
    i=1
    while i<=n:
        if(n % i ==0):
            print(i,end=" ")
        i = i+1

print("The divisors fo 101 are:")
printDivisor(101)
