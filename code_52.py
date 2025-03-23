#Counting the number of even and odd elemnts in an array
arr=[1,7,8,4,5,16,8]
n=len(arr)
countEven = 0
countodd= 0
for i in range(0,n):
    if arr[i]%2==0:
        countEven +=1
    else:
        countodd +=1
print("even elements:")
print(countEven)
print("Odd elements:")
print(countodd)