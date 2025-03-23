# question: sort first half in ascending order and second half in descending order in an array
def printOrder(arr,n):
    arr.sort()
    
    for i in range(n//2):
        print(arr[i], end= " ")
    
    for j in range(n-1,n //2-1, -1):
        print(arr[j], end= " ")

arr=[5, 4, 6, 2, 1, 3, 8, -1]
n=len(arr)
printOrder(arr,n)