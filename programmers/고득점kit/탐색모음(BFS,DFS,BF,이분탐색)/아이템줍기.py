'''
프로그래머스에서 런타임 에러가 발생한다면
0으로 나눈것이 없는지
배열의 index를 넘어가는게 없는지 체크해볼것........
이것때문에 몇시간을 날렸냐........으악으악
BFS, DFS문제 할때 조건마다 범위 설정 까먹지 말것................
'''
from collections import deque
rectangle = []

def is_line(x, y):
    for rec in rectangle:
        if rec[0] < x < rec[2] and rec[1] < y < rec[3]:
            return False
    for rec in rectangle: 
        if rec[0] <= x <= rec[2]:
            if y == rec[1] or y == rec[3]:
                return True
        if rec[1] <= y <= rec[3]:
            if x == rec[0] or x == rec[2]:
                return True
    return False
    

def solution(_rectangle, characterX, characterY, itemX, itemY):
    global rectangle
    rectangle = _rectangle 
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    visited = [[0 for _ in range(51)] for _ in range(51)]
    visited[characterX][characterY] = 0
    Q = deque()
    Q.append((characterX, characterY))
    
    while Q:
        x, y = Q.popleft()
        if x == itemX and y == itemY:
            return visited[x][y]
        else:
            for i in range(4):
                xx = x + dx[i]
                yy = y + dy[i]
                if 0 <= xx <= 50 and 0 <= yy <= 50 and not visited[xx][yy] and is_line(x + dx[i]/2, y + dy[i]/2):
                    Q.append((xx, yy))
                    visited[xx][yy] = visited[x][y] + 1
    return -1