def solution(s):
    answer = True
    stack = []
    p = list(s)
    
    for c in p:
        if c == "(":
            stack.append(c)
        elif c == ")" and stack:
            last = stack.pop()
            if last != "(":
                return False
        else:
            return False
    if stack:
        return False
    
    return True