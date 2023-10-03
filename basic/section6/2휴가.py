import sys


def dfs(day, money):
    global selery
    if day == N:
        if selery < money:
            selery = money
        return

    else:
        if day + counsel[day][0] <= N:
            dfs(day + counsel[day][0], money + counsel[day][1])
        dfs(day + 1, money)


for i in range(1, 6):
    sys.stdin = open(f"test/in{i}.txt", "rt")
    N = int(input())
    counsel = []
    selery = 0
    for i in range(N):
        counsel.append(list(map(int, input().split())))
    dfs(0, 0)
    print(selery)
