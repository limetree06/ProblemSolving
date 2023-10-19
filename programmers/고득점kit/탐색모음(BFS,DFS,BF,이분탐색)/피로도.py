MAX = 0
dungeons = []
visited = []
def dfs(energy, count):
    global MAX
    global visited
    MAX = max(count, MAX)
    for index in range(len(dungeons)):
        if visited[index] == 0 and energy >= dungeons[index][0]:
            visited[index] = 1
            dfs(energy - dungeons[index][1], count+1)
            visited[index] = 0

def solution(k, _dungeons):
    global dungeons
    global visited
    visited = [0] * len(_dungeons)
    dungeons.sort(key = lambda x : x[0], reverse=False)
    dungeons = _dungeons
    dfs(k, 0)
    return MAX