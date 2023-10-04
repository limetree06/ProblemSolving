import sys
from collections import deque


"""  
섬나라 아일랜드의 지도가 격자판의 정보로 주어집니다. 각 섬은 1로 표시되어 상하좌우와 대 각선으로 연결되어 있으며, 0은 바다입니다. 
섬나라 아일랜드에 몇 개의 섬이 있는지 구하는 프로그램을 작성하세요.


▣ 입력설명
첫 번째 줄에 자연수 N(3<=N<=20)이 주어집니다. 두 번째 줄부터 격자판 정보가 주어진다.

▣ 출력설명
첫 번째 줄에 섬의 개수를 출력한다.

▣ 입력예제
7 
1 1 0 0 0 1 0
0 1 1 0 1 1 0
0 1 0 0 0 0 0
0 0 0 1 0 1 1
1 1 0 1 1 0 0
1 0 0 0 1 0 0
1 0 1 0 1 0 0

▣ 출력예제
5
"""

dy = [-1, -1, -1, 0, 0, 1, 1, 1]
dx = [1, 0, -1, 1, -1, 1, 0, -1]


def print_board():
    print(f"========{count}==========")
    for i in board:
        print(i)


for i in range(1, 6):
    sys.stdin = open(f"test/in{i}.txt", "rt")
    N = int(input())
    board = []
    dQ = deque()
    count = 0

    for i in range(N):
        board.append(list(map(int, input().split())))

    for x in range(N):
        for y in range(N):
            if board[x][y] == 1:
                board[x][y] = 0
                dQ.append((x, y))
                count += 1
                while dQ:
                    now_x, now_y = dQ.popleft()
                    for i in range(8):
                        xx = now_x + dx[i]
                        yy = now_y + dy[i]
                        if 0 <= xx < N and 0 <= yy < N and board[xx][yy] == 1:
                            board[xx][yy] = 0
                            dQ.append((xx, yy))

    print(count)
