#Find the Union and Intersection of the two sorted arrays in Python
def union_sorted(arr1,arr2):
    i,j =0 , 0
    union_res = []

    while i< len(arr1) and j<len(arr2):
        if arr1[i] < arr2[j]:
            union_res.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            union_res.appemd(arr2[j])
            j+=1
        else:
            union_res.append(arr1[i])
            i += 1
            j +=1

    while i<len(arr1):
        union_res.append(arr1[i])
        i+=1
    while j<len(arr2):
        union_res.append(arr2[j])
        j+=1
    return union_res
def intersection_sorted(arr1,arr2):
    i,j =0,0
    intersection_res=[]
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            i +=1
        elif arr1[i] > arr2[j]:
            j +=1
        else:
            intersection_res.append(arr1[i])
            i+=1
            j+=1
    return intersection_res
arr1=[1,2,3,4,5,6]
arr2=[2,3,5,7]
print("Union", union_sorted(arr1,arr2))
print("Intersetion", intersection_sorted(arr1,arr2))