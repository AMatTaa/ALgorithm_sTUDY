def dumb_comparison(n1, n2):
    flipped1 = int(n1[::-1])
    flipped2 = int(n2[::-1])
    return max(flipped1, flipped2)


num1, num2 = map(str, input().split())
print(dumb_comparison(num1, num2))
