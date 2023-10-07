from collections import deque
def solution(n, computers):
    check = [0] * (n+1)
    check[0] = 1
    answer = 0
    q = deque()
    
    while 0 in check:
        for node in range(1, n+1):
            if check[node] == 0:
                q.append(node)
                answer += 1
            while q: 
                cur_node = q.popleft()
                check[cur_node] = 1
                for index, value in enumerate(computers[cur_node -1]):
                    if value == 1 and check[index+1] == 0:
                        q.append(index+1)
            
    return answer