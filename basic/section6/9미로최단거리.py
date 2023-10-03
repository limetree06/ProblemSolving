import sys
from collections import deque

"""  
7*7 격자판 미로를 탈출하는 최단경로의 경로수를 출력하는 프로그램을 작성하세요. 
경로수는 출발점에서 도착점까지 가는데 이동한 횟수를 의미한다. 출발점은 격자의 (1, 1) 좌표이고, 탈 출 도착점은 (7, 7)좌표이다. 
격자판의 1은 벽이고, 0은 도로이다.


▣ 입력설명
7*7 격자판의 정보가 주어집니다.

▣ 출력설명
첫 번째 줄에 최단으로 움직인 칸의 수를 출력한다. 도착할 수 없으면 -1를 출력한다.

▣ 입력예제
0 0 0 0 0 0 0 
0 1 1 1 1 1 0
0 0 0 1 0 0 0
1 1 0 1 0 1 1
1 1 0 1 0 0 0
1 0 0 0 1 0 0
1 0 1 0 0 0 0

▣ 출력예제
12

"""


def find(maze):
    dQ = deque()
    dQ.append(0)
    check[0] = 0
    while dQ:
        now = dQ.popleft()
        if now == 48:
            break
        if (now + 1) % 7 != 0:  # 오른쪽 갈수있음
            if maze[now + 1] == 0 and check[now + 1] == 0:
                dQ.append(now + 1)
                check[now + 1] = check[now] + 1
        if now % 7 != 0 and check[now - 1] == 0:  # 왼쪽으로 갈수있음
            if maze[now - 1] == 0:
                dQ.append(now - 1)
                check[now - 1] = check[now] + 1

        if now > 6 and check[now - 7] == 0:  # 위로 갈수있음
            if maze[now - 7] == 0:
                dQ.append(now - 7)
                check[now - 7] = check[now] + 1

        if now < 42 and check[now + 7] == 0:  # 아래로 갈수있음
            if maze[now + 7] == 0:
                dQ.append(now + 7)
                check[now + 7] = check[now] + 1


for i in range(1, 6):
    sys.stdin = open(f"test/in{i}.txt", "rt")
    maze = []
    check = [0] * 49
    for _ in range(7):
        maze += list(map(int, input().split()))
    find(maze)
    if check[48] == 0:
        print(-1)
    else:
        print(check[48])
