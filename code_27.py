# Question: Can a number be expressed as a sum of two prime number ?
Number = int(input("Enter a number"))

arr=[]

for i in range(2,Number):
    flag=0
    for j in range(2, i):
        if i%j == 0:
            flag=1
    if flag == 0:
        arr.append(i)
flag=0
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] + arr[j] == Number:
            flag=1
            print(f"{str(arr[i])} add  {str(arr[j])} are prime numbers when added gives {str(Number)}")
            break

if flag == 0:
    print(f"No Prime Numbers can guve sum of {str(Number)}")