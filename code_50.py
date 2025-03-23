#question: find the longest pallindrome in an array
def is_palindrome(s):
    return str(s) == str(s)[::-1]
def longest_palindrome_in_array(arr):
    longest=""
    for item in arr:
        if is_palindrome(item):
            if len(str(item)) > len(longest):
                longest = str(item)
    return longest if longest else None

arr=["racecar","apple","madam","banana","refer",12321,45654,"hello"]
result=longest_palindrome_in_array(arr)
print("longest palindrome:",result)
                