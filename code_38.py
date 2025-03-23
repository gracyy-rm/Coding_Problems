#Question : Find all the permuations of the string
def permute(string, path=""):
    if not string:
        print(path)
        return
    for i in range(len(string)):
        remaining = string[:i] + string[i+1:]
        permute(remaining, path+string[i])

s="ABC"
permute(s)