#Question: Automorphic Number
#- number whose square end with the same digits as number itself
number = 46576
sq = pow(number,2)
mod = pow(10, len(str(number)))

if sq % mod == number:
    print(f"{number} is an automorphic number")
else:
    print(f"{number} is not a automorphic number")