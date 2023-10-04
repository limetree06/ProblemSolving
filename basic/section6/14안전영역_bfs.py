import sys
from collections import deque
import copy

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def safty_dfs(depth, flood):
    dQ = deque()
    count = 0
    for i in range(N):
        for j in range(N):
            if flood[i][j] > depth:
                flood[i][j] = 0
                dQ.append((i, j))
                while dQ:
                    x, y = dQ.popleft()
                    for k in range(4):
                        xx = x + dx[k]
                        yy = y + dy[k]
                        if 0 <= xx < N and 0 <= yy < N and flood[xx][yy] > depth:
                            flood[xx][yy] = 0
                            dQ.append((xx, yy))
                count += 1
    return count


for i in range(1, 6):
    sys.stdin = open(f"test/in{i}.txt", "rt")
    N = int(input())
    board = []
    max_num = 0
    candidate = set()
    result = 0
    for i in range(N):
        a = list(map(int, input().split()))
        board.append(a)
        candidate.update(a)

    for depth in candidate:
        flood = copy.deepcopy(board)
        num = safty_dfs(depth, flood)
        if num > max_num:
            max_num = num
            result = depth

    print(max_num)
