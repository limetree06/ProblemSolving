def solution(n, costs):
    costs.sort(key = lambda x: x[2])
    route = []
    visited = [0] * n
    total = 0
    for cost in costs:
        v_1 = cost[0]
        v_2 = cost[1]
        if visited[v_1] + visited[v_2] == 0:
            visited[v_1], visited[v_2] = 1, 1
            total += cost[2] 
            route.append(set([v_1, v_2]))
        elif visited[v_1] + visited[v_2] == 1:
            visited[v_1], visited[v_2] = 1, 1
            total += cost[2]
            for i in range(len(route)):
                if v_1 in route[i] or v_2 in route[i]:
                    route[i].update([v_1, v_2])
                    break
        elif len(route) > 1 and visited[v_1] + visited[v_2] == 2:
            index = []
            for i in range(len(route)):
                if v_1 in route[i]:
                    index.append(i)
                if v_2 in route[i]:
                    index.append(i)
            if index[0] != index[1]:
                total += cost[2]
                route[index[0]] = route[index[0]].union(route[index[1]])
                del route[index[1]]
                
    return total

'''
<Testcase>

7 [[2, 3, 7], [3, 6, 13], [3, 5, 23], [5, 6, 25], [0, 1, 29], [1, 5, 34], [1, 2, 35], [4, 5, 53], [0, 4, 75]] 159
5 [[0, 1, 5], [1, 2, 3], [2, 3, 3], [3, 1, 2], [3, 0, 4], [2, 4, 6], [4, 0, 7]] 15
5 [[0, 1, 1], [3, 4, 1], [1, 2, 2], [2, 3, 4]] 8
4 [[0, 1, 5], [1, 2, 3], [2, 3, 3], [1, 3, 2], [0, 3, 4]] 9
5 [[0, 1, 1], [3, 1, 1], [0, 2, 2], [0, 3, 2], [0, 4, 100]] 104
6 [[0, 1, 5], [0, 3, 2], [0, 4, 3], [1, 4, 1], [3, 4, 10], [1, 2, 2], [2, 5, 3], [4, 5, 4]] 11
5 [[0, 1, 1], [2, 3, 1], [3, 4, 2], [1, 2, 2], [0, 4, 100]] 6
5 [[0, 1, 1], [0, 4, 5], [2, 4, 1], [2, 3, 1], [3, 4, 1]] 8
5 [[0, 1, 1], [0, 2, 2], [0, 3, 3], [0, 4, 4], [1, 3, 1]] 8
5 [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 3], [2, 3, 8], [3, 4, 1]] 7
5 [[0, 1, 1], [3, 4, 1], [1, 2, 2], [2, 3, 4]] 8
4 [[0,1,1],[0,2,2],[2,3,1]] 4
'''