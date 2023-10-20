def solution(triangle):
    dp_table = []
    for line in triangle:
        if not dp_table:
            dp_table.append(line)
        else:
            up = dp_table[-1]
            total = [line[0] + up[0]]
            for i in range(1, len(up)):
                total.append(line[i] + max(up[i-1], up[i]))
            total.append(line[-1] + up[-1])
            dp_table.append(total)
    return max(dp_table[-1])
                
        