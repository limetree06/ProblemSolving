def is_visited(visited, tic):
    count = 0
    for v in visited:
        if v == tic:
            count+=1
    return count
    
def solution(tickets):
    tickets.sort()
    visited = []
    
    answer = ['ICN']
    def dfs(start):
        if len(visited) == len(tickets):
            return True
        else:
            for tic in tickets:
                if tic[0] == start and is_visited(visited, tic) != is_visited(tickets, tic):
                    visited.append(tic)
                    answer.append(tic[1])
                    if dfs(tic[1]):
                        return True
                    else:
                        answer.pop()
                        visited.pop()
            
    dfs('ICN')
    return answer