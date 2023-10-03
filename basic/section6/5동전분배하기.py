import sys


def max_min_sub(A, B, C):
    if A > B > C or C > B > A:
        return abs(A - C)
    elif A > C > B or B > C > A:
        return abs(A - B)
    elif B > A > C or C > A > B:
        return abs(C - B)


def dfs(level, A, B, C):
    global sub
    if level == N:
        if A == 0 or B == 0 or C == 0:
            return
        if A == B or B == C or C == A:
            return
        res = max_min_sub(A, B, C)
        if res < sub:
            sub = res
        return
    else:
        dfs(level + 1, A + coins[level], B, C)
        dfs(level + 1, A, B + coins[level], C)
        dfs(level + 1, A, B, C + coins[level])


for i in range(1, 6):
    sys.stdin = open(f"test/in{i}.txt", "rt")
    N = int(input())
    coins = []
    for i in range(N):
        coins.append(int(input()))
    sub = sum(coins)

    dfs(0, 0, 0, 0)
    print(sub)
