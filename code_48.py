# Question: finding the frequency of the elements in an array
def countFreq(arr, size):
    frequency={}

    for num in arr:
        frequency[num] = frequency.get(num,0) + 1
    for key,value in frequency.items():
        print(f"{key}: {value}")
        
    
arr=[5, 8, 5, 7, 8, 19]
n=len(arr)
countFreq(arr,n)