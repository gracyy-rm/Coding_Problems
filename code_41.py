# question: Find all possible Pallindromin partitions of the given string 

def is_palindrome(s):
    return s == s[::-1]
def partition_helper(s,start,path,result):
    if start == len(s):
        result.append(path[:])
        return
    for end in range(start,len(s)):
        substring = s[start:end+1]
        if is_palindrome(substring):
            path.append(substring)
            partition_helper(s,end+1,path,result)
            path.pop()

def palindromic_partitions(s):
    result = []
    partition_helper(s,0,[],result)
    return result

s="aab"
print(palindromic_partitions(s))