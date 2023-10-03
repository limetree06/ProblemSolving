import sys

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def dfs(x, y):
    global count
    if x == end_x and y == end_y:
        count += 1
        return
    else:
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < N and 0 <= yy < N and board[xx][yy] == 0:
                if mount[x][y] < mount[xx][yy]:
                    board[xx][yy] = 1
                    dfs(xx, yy)
                    board[xx][yy] = 0


for i in range(1, 6):
    sys.stdin = open(f"test/in{i}.txt", "rt")
    N = int(input())
    mount = [list(map(int, input().split())) for _ in range(N)]
    board = [[0 for _ in range(N)] for _ in range(N)]
    count = 0
    MAX = max(map(max, mount))
    MIN = min(map(min, mount))
    start_x, start_y = 0, 0
    end_x, end_y = 0, 0
    for i in range(N):
        for j in range(N):
            if mount[i][j] == MIN:
                start_x, start_y = i, j
            if mount[i][j] == MAX:
                end_x, end_y = i, j
    dfs(start_x, start_y)
    print(count)
