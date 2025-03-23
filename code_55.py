#count the number of vowels

def count_vowels(s):
    vowels="AEIOUaeiou"
    count=0
    for char in vowels:
        if char in vowels:
            count+=1
    return count

text="hello, world"
print("number of vowels:",count_vowels(text))