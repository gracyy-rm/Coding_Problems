#Question : Count Possible decoding of a given digit sequence:

def count_decodings_memo(digits, index, memo):
    if index == len(digits):
        return 1
    if digits[index] == '0':
        return 0
    if index in memo:
        return memo[index]
    
    count = count_decodings_memo(digits, index+1, memo)

    if index + 1 < len(digits) and 10 <= int(digits[index:index + 2]) <= 26:
        count += count_decodings_memo(digits, index + 2, memo)

    memo[index] = count
    return count
def count_decodings(digits):
    return count_decodings_memo(digits,0,{})

digit_sequence="226"
print(count_decodings(digit_sequence))