from collections import deque

def is_line(rectangle, x, y):
    for rec in rectangle:
        if rec[0] < x < rec[2] and rec[1] < y < rec[3]:
            return False
        
    for rec in rectangle: 
        if rec[0] <= x <= rec[2]:
            if y == rec[1] or y == rec[3]:
                #print(x, y, rec)
                return True
        if rec[1] <= y <= rec[3]:
            if x == rec[0] or x == rec[2]:
                #print(x, y, rec)
                return True
    return False
    
    

def solution(rectangle, characterX, characterY, itemX, itemY):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    MAX = 0
    Q = deque()
    Q.append((characterX, characterY))
    visited = [[0 for _ in range(51)] for _ in range(51)]
    visited[characterX][characterY] = 0
    
    while Q:
        x, y = Q.popleft()
        if x == itemX and y == itemY:
            if visited[x][y] > MAX:
                MAX = visited[x][y]
                break
        else:
            for i in range(4):
                xx = x + dx[i]
                yy = y + dy[i]
                if visited[xx][yy] == 0:
                    xxx = x + (dx[i] / 2)
                    yyy = y + (dy[i] / 2)
                    if is_line(rectangle, xxx, yyy):
                        visited[xx][yy] = visited[x][y] + 1
                        Q.append((xx, yy))
                    
    return MAX