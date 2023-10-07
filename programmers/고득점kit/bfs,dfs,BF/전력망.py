from collections import deque

''' 
이 문제의 교훈!
정석대로 풀고나서 문제점을 해결해나가는 방식으로 문제 풀것.
내가 생각한 방법이 해보지도 않고 시간초관 날것이라는 생각에 계속 다릉 방법으로 시도하다 시간만 날렸다..
'''

def bfs(wire, n):
    q = deque()
    check = [0] * n
    q.append(1)
    while q:
        num = q.popleft()
        check[num - 1] = 1
        for node in wire[num]:
            if check[node-1] == 0:
                q.append(node)
    
    visited = sum(check)
    not_visited = n -  sum(check)
    return  abs(visited - not_visited)


def solution(n, wires):
    wire = dict()
    MIN = n
    for i in range(n):
        wire[i+1] = []
    
    for s, e in wires:
        wire[s].append(e)
        wire[e].append(s)
        
    for s, e in wires:
        wire[s].remove(e)
        wire[e].remove(s)
        value = bfs(wire, n)
        if MIN > value:
            MIN = value
        wire[s].append(e)
        wire[e].append(s)
    return MIN