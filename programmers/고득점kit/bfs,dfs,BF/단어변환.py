def difference(start, end):
    count = 0
    for i in range(len(start)):
        if list(start)[i] != list(end)[i]:
            count +=1
    return count

def bfs(begin, target, words):
    queue = [(begin, 0)]
    visited = set() 

    while queue:
        current_word, count = queue.pop(0)
        if current_word == target:
            return count
        
        for word in words:
            if word not in visited and difference(current_word, word) == 1:
                visited.add(word)
                queue.append((word, count + 1))
    return 0 

def solution(begin, target, words):
    if target not in words:
        return 0

    return bfs(begin, target, words)