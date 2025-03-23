#Question : given a string s , remove all adjacent duplicate characters

def remove_adjacent_duplicates(s):
    n=len(s)
    if n == 0 or n==1:
        return s
    result=[]
    i=0

    while i<n:

        if i<n-1 and s[i] == s[i+1]:
            while i<n-1 and s[i] == s[i+1]:
                i+=1
        else:
            result.append(s[i])
        i+=1
    new_s="".join(result)

    return new_s if new_s == s else remove_adjacent_duplicates(new_s)
s="acaabbbceddd"
print(remove_adjacent_duplicates(s))