import sys


def combination(nums, last, sum):
    global count
    if nums == M:
        if sum % div == 0:
            count += 1
        return
    else:
        for i in range(last, N):
            combination(nums + 1, i + 1, sum + nums_list[i - 1])
    return 0


for i in range(1, 6):
    sys.stdin = open(f"test/in{i}.txt", "rt")
    N, M = map(int, input().split())
    nums_list = list(map(int, input().split()))
    div = int(input())

    count = 0
    check = [0] * M
    combination(0, 0, 0)
    print(count)
