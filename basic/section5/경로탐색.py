import sys


def find_path(level, start):
    global count
    if start == N:
        count += 1
        return
    elif level == N:
        return
    else:
        for i in range(1, N + 1):
            if road[start][i] == 1 and i not in check:
                check[level] = i
                find_path(level + 1, i)
                check[level] = 0


for i in range(1, 6):
    sys.stdin = open(f"test/in{i}.txt", "rt")
    N, M = map(int, input().split())
    road = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    check = [0] * N
    count = 0
    for _ in range(M):
        start, end = map(int, input().split())
        road[start][end] = 1
    check[0] = 1
    find_path(1, 1)
    print(count)
