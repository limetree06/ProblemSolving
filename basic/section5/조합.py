import sys


def combination(level, start):
    global count
    if level == M:
        for i in check:
            print(i, end=" ")
        count += 1
        print()
        return
    else:
        for i in range(start, N + 1):
            check[level] = i
            combination(level + 1, i + 1)
    return 0


for i in range(5, 6):
    sys.stdin = open(f"test/in{i}.txt", "rt")
    N, M = map(int, input().split())
    count = 0
    check = [0] * M
    combination(0, 1)
    print(count)
