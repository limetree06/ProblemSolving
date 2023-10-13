from collections import deque

def solution(maps):
    N = len(maps)
    M = len(maps[0])
    count = 1
    MAX = 0
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    Q = deque()
    Q.append((0,0, count))
    while Q:
        x, y, cur_count = Q.popleft()
        
        if x == N-1 and y== M-1:
            if cur_count > MAX:
                MAX = cur_count
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0<= xx < N and 0<= yy< M and maps[xx][yy] == 1:
                maps[xx][yy] = 0
                Q.append((xx, yy, cur_count+1))
    
    if MAX == 0: return -1
    else: 
        return MAX