#Question : calulate the length of the string using recursion
def length(str):
    if str == "":
        return 0

    return 1 + length(str[1:])
str="Gracy"
print(f"length of {str} is {length(str)}") 