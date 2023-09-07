import sys

""" 
완성된 9×9 크기의 수도쿠가 주어지면 정확하게 풀었으면 “YES", 잘 못 풀었으면 ”NO"를 출 력하는 프로그램을 작성하세요.

▣ 입력설명
첫 번째 줄에 완성된 9×9 스도쿠가 주어집니다.

▣ 출력설명
첫째 줄에 “YES" 또는 ”NO"를 출력하세요.
"""


def check_sutoku(sutoku):
    row = [0] * 9
    col = [0] * 9

    """ 
    0, 1, 2,
    3, 4, 5,
    7, 8, 9
    """
    square = [0] * 9
    for i in range(9):
        for j in range(9):
            number = sutoku[i][j]
            row[i] = row[i] + 2**number
            col[i] = col[i] + 2**number
            square_num = (i // 3) * 3 + (j // 3)
            square[square_num] = square[square_num] + 2**number

    for i in range(9):
        if row[i] != 1022 or col[i] != 1022 or square[i] != 1022:
            return False
    return True


for i in range(1, 6):
    sys.stdin = open(f"test/in{i}.txt", "rt")
    sutoku = []
    for _ in range(9):
        sutoku.append(list(map(int, input().split())))
    if check_sutoku(sutoku):
        print("YES")
    else:
        print("NO")
