import sys


def find_route(now):
    global count
    if now == 48:
        count += 1
        return
    else:
        next_list = []
        if (now + 1) % 7 != 0:  # 오른쪽 갈수있음
            next_list.append(now + 1)

        if now % 7 != 0:  # 왼쪽으로 갈수있음
            next_list.append(now - 1)

        if now < 42:  # 아래로 갈수있음
            next_list.append(now + 7)

        if now > 6:  # 위로 갈수있음
            next_list.append(now - 7)

        for next in next_list:
            if maze[next] == 0 and check[next] == 0:
                check[next] = 1
                find_route(next)
                check[next] = 0


for i in range(1, 6):
    sys.stdin = open(f"test/in{i}.txt", "rt")
    maze = []
    check = [0] * 49
    count = 0
    check[0] = 1
    for _ in range(7):
        maze += list(map(int, input().split()))
    find_route(0)
    print(count)
