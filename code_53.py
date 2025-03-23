#check whether a character is a consonant or a vowel
def check_char(ch):
    vowels="AEIOUaeiou"
    if ch.isalpha():
       if ch in vowels:
            return f"{ch} is a vowel."
       else:
          return f"{ch} is a consonant."
    else:
        return " inavllid input"
char=input("enter a character")
print(check_char(char))