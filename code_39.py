# question : Last non-zero digit of a factorial

def last_nonzero_digit(n):
    digits=[1,1,2,6,4]
    result = 1
    count_2=0
    count_5=0

    for i in range(1,n+1):
        num=i

        while num%2 == 0:
            count_2 += 1
            num //= 2
        while num%5 == 0:
            count_5 += 1
            num //=5

        result = (result*(num%10)) %10
    for _ in range(count_2-count_5):
        result = (result*2) % 10

    return result

n=10
print(last_nonzero_digit(n))