# question: largest element n the array
def findMaxRec(A,n):
    if(n==1):
        return A[0]
    return max(A[n-1], findMaxRec(A, n-1))

if __name__=="__main__":
    a=[1,4,45,6,-50,10,2]
    n=len(a)
    print(findMaxRec(a,n))