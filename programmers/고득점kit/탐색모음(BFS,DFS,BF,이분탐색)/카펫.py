def solution(brown, yellow):
    MAX_COL = int(yellow ** (1/2))
    for col in range(1, MAX_COL+1):
        if yellow % col == 0:
            row = yellow // col
            if row + col + 2 == brown // 2:
                return [row+2, col+2]

    