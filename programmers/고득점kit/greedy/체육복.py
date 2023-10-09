def solution(n, _lost, _reserve):
    lost = [l for l in _lost if l not in _reserve]
    reserve = [r * (-1) for r in _reserve if r not in _lost]
    
    table = lost + reserve
    table.sort(key=lambda x : abs(x))
    
    for i in range(len(table)-1):
        lost_s = max(table[i], table[i+1])
        borrow_s = min(table[i], table[i+1])
        
        if lost_s in lost and borrow_s in reserve:
            if -2 < table[i] + table[i+1] < 2 and table[i] * table[i+1] < 0:
                lost.remove(lost_s)
                reserve.remove(borrow_s)
    
    return n - len(lost)