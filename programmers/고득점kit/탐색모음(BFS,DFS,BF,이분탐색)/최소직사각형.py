def solution(sizes):
    ROW_MAX = 0
    COL_MAX = 0
    for a, b in sizes:
        row, col = max(a, b), min(a,b)
        ROW_MAX, COL_MAX = max(row, ROW_MAX), max(col, COL_MAX)
    return ROW_MAX * COL_MAX