import sys

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def dfs(x, y, index):
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < N and 0 <= yy < N and board[xx][yy] > height[index]:
            print()


for i in range(1, 2):
    sys.stdin = open(f"test/in{i}.txt", "rt")
    N = int(input())
    board = []
    height = set()
    for i in range(N):
        a = list(map(int, input().split()))
        board.append(a)
        height.update(a)
    height = list(height)

    dfs(0, 0, 0)
