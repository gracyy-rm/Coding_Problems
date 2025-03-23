# Question: Finding the number if times the digit x occurs in the input 

def countOccurances(n, d):
    count = 0

    while(n>0):

        if(n%10 == d):
            count = count +1
        
        n=n//10

    return count
d=2
n=8282828282
print(countOccurances(n,d))