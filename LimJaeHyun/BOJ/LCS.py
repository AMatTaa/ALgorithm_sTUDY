import sys
input = sys.stdin.readline

first_string = list(input().strip())
second_string = list(input().strip())

memo = list([0] * (len(second_string) + 1) for _ in range(len(first_string) + 1))

for i in range(1, len(first_string) + 1):
    for j in range(1, len(second_string) + 1):
        if first_string[i - 1] == second_string[j - 1]:
            memo[i][j] = memo[i - 1][j - 1] + 1
        else:
            memo[i][j] = max(memo[i - 1][j], memo[i][j - 1])

print(memo[-1][-1])
