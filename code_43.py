# Question: Guven a set of Positive Integers . Find All Subsets

def subsets(A,subset=[],index=0):
    print(*subset)

    for i in range(index,len(A)):
        subset.append(A[i])

        subsets(A,subset, i+1)

        subset.pop(-1)
    return 

array=[1,2,3]
subsets(array)