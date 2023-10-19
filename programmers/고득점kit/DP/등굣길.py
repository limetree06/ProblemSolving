def solution(m, n, puddles):
    table = [[0] * m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if [j + 1, i + 1] in puddles:
                table[i][j] = 0
                continue
            else:
                if i==0 and j==0:
                    table[0][0] = 1
                elif i==0:
                    table[0][j] = table[0][j-1]
                elif j==0:
                    table[i][0] = table[i-1][0]
                else:
                    table[i][j] = table[i-1][j] + table[i][j-1]
    
    return table[-1][-1] % 1000000007