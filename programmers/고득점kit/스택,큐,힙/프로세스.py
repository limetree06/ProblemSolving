from collections import deque

def solution(priorities, location):
    Q = deque(priorities)
    count = 1
    
    while Q:
        MAX = max(Q)
        priority = Q.popleft()
        if MAX == priority and location == 0:
            break
        elif MAX == priority and location != 0:
            count += 1
        else:
            Q.append(priority)
        location = (location-1) % len(Q)
        
    return count