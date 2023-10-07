count = 0
numbers = []
target = 0
def dfs(level, value):
    global count  
    if level == len(numbers):
        if value == target:
            count +=1
        return
    else:
        dfs(level+1, value + numbers[level])
        dfs(level+1, value - numbers[level])

def solution(a, b):  
    global numbers
    global target
    numbers = a
    target = b
    dfs(0, 0)
    return count