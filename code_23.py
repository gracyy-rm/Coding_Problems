# permutations in which n people can occupy r seats in a classroom

def factorial(num):
    fact=1
    for i in range(num, 1, -1):
        fact *=i
    return fact

def permutations(n,r):
    if n<r:
        return "invalid N must be grater than or equal to R."
    return factorial(n) // factorial(n-r)


N=int(input("enter number of people: "))
R=int(input("enter number of seats: "))



print(f"total ways to arrange {N} people in {R} seats : {permutations(N,R)}")