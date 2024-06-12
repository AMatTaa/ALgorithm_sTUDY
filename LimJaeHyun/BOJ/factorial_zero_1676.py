import math

def factorial_zero(n):
    string_cheese = str(math.factorial(n))
    cnt = 0
    for i in range(len(string_cheese)-1, -1, -1):
        if string_cheese[i] == '0':
            cnt += 1
        else:
            break
    return cnt