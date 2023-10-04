import sys
from collections import deque


"""' 
기존 나의 방법 : dg에 append하는 기준을 하루 단위로 했다. 그래서 while문 한 사이클 마다 count1 추가되는거다. 
나의 방법의 문제점 : 전체가 익지 못할 경우를 찾기 못한다... + 시간이 많이 걸린다.
이렇게 구현한 이유는 count를 어떻게 해야할지 몰라서..익은 토마토가 몇일쨰 익은건지 몰랐기 때문
익은 상태를 board에 그저 1두기엔 1을 flag로 확인해서 append, popleft하기 때문에 무한루프를 돌았다.

풀이 방법 : board에 익는데 걸린 날짜로 표시..
조금더 신중하게 생각하자 민지야..
+ 초반에 1 인 토마토 전부를 찾아서 Q에 넣어주는게 BFS이다. 넓이 우선 탐색의 의미를 깊이 생각해보자


"""

""" 
문제 : 현수의 토마토 농장에서는 토마토를 보관하는 큰 창고를 가지고 있다. 
토마토는 아래의 그림 과 같이 격자 모양 상자의 칸에 하나씩 넣어서 창고에 보관한다.

창고에 보관되는 토마토들 중에는 잘 익은 것도 있지만, 아직 익지 않은 토마토들도 있을 수 있다. 보관 후 하루가 지나면, 
익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다. 
하나의 토마토의 인접한 곳은 왼쪽, 오른쪽, 앞, 뒤 네 방향 에 있는 토마토를 의미한다. 
대각선 방향에 있는 토마토들에게는 영향을 주지 못하며, 토마토 가 혼자 저절로 익는 경우는 없다고 가정한다.
현수는 창고에 보관된 토마토들이 며칠이 지나 면 다 익게 되는지, 그 최소 일수를 알고 싶어 한다.
토마토를 창고에 보관하는 격자모양의 상자들의 크기와 익은 토마토들과 익지 않은 토마토들 의 정보가 주어졌을 때, 
며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하는 프로 그램을 작성하라. 단, 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다.

▣ 입력설명
첫 줄에는 상자의 크기를 나타내는 두 정수 M, N이 주어진다. 
M은 상자의 가로 칸의 수, N 은 상자의 세로 칸의 수를 나타낸다. 단, 2 ≤ M, N ≤ 1,000 이다.
둘째 줄부터는 하나의 상자에 저장된 토마토들의 정보가 주어진다. 즉, 둘째 줄부터 N개의 줄 에는 상자에 담긴 토마토의 정보가 주어진다. 
하나의 줄에는 상자 가로줄에 들어있는 토마토 의 상태가 M개의 정수로 주어진다. 
정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다.

▣ 출력설명
여러분은 토마토가 모두 익을 때까지의 최소 날짜를 출력해야 한다. 
만약, 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고, 토마토가 모두 익지는 못하는 상황이면 -1을 출력해야 한다.



"""


dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def get_tomato():
    day = []
    is_done = True
    for x in range(N):
        for y in range(M):
            if board[x][y] == 1:
                day.append((x, y))
            elif board[x][y] == 0:
                is_done = False
    if is_done:
        return []
    else:
        return day


for i in range(1, 6):
    sys.stdin = open(f"test/in{i}.txt", "rt")
    M, N = map(int, input().split())  # M은 가로, N은 세로
    board = []
    dQ = deque()
    for _ in range(N):
        board.append(list(map(int, input().split())))

    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                dQ.append((i, j))

    while dQ:
        x, y = dQ.popleft()
        for k in range(4):
            xx = x + dx[k]
            yy = y + dy[k]
            if 0 <= xx < N and 0 <= yy < M and board[xx][yy] == 0:
                board[xx][yy] = board[x][y] + 1
                dQ.append((xx, yy))

    MAX = max(map(max, board))
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                MAX = 0
                break
        if MAX == 0:
            break
    print(MAX - 1)
