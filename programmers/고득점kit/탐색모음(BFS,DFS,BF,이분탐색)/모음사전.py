words = [ 'A', 'E', 'I', 'O', 'U']
order = 0
_word = [""] * 5
find = False
check = [""] * 5

def dfs(level):
    global order
    global _word
    global check
    global find
    order += 1
    if check == _word:
        find = True
        order -= 1
        return
    if level == len(_word):
        return
    else:
        for i in range(5):
            if not find:
                check[level] = words[i]
                dfs(level + 1)
                check[level] = ""

def solution(word):
    global order
    global _word
    for i in range(len(word)):
        _word[i] = word[i]
    
    dfs(0)
    return order