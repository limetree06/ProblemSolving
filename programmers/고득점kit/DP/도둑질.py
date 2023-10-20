def solution(money):
    if len(money) == 3:
        return (max(money))
    dp_table = [[0, 0] for _ in money]
    for idx, value in enumerate(money):
        if idx != 1:
            dp_table[idx][0] = max(dp_table[idx-2][0], dp_table[idx-3][0]) + money[idx]
        if idx != 0:
            dp_table[idx][1] = max(dp_table[idx-2][1], dp_table[idx-3][1]) + money[idx]
    A = [i[0] for i in dp_table]
    B = [i[1] for i in dp_table]
    A.pop()
    return max(max(A), max(B))
    
        