import sys


def dfs(level, left, right):
    check[abs(left - right)] = 1
    if level == N:
        return
    else:
        dfs(level + 1, left + weights[level], right)
        dfs(level + 1, left, right + weights[level])
        dfs(level + 1, left, right)


for i in range(1, 6):
    sys.stdin = open(f"test/in{i}.txt", "rt")
    N = int(input())
    weights = list(map(int, input().split()))
    check = [0] * (sum(weights) + 1)
    dfs(0, 0, 0)
    print(sum(weights) - sum(check) + 1)
