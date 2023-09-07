import sys

""" 
1부터 9까지의 자연수로 채워진 7*7 격자판이 주어지면 격자판 위에서 가로방향 또는 세로방향으로 길이 5자리 회문수가 몇 개 있는지 구하는 프로그램을 작성하세요. 
회문수란 121과 같이 앞에서부터 읽으나 뒤에서부터 읽으나 같은 수를 말합니다.

▣ 입력설명
1부터 9까지의 자연수로 채워진 7*7격자판이 주어집니다.

▣ 출력설명 5자리 회문수의 개수를 출력합니다.
▣ 입력예제
2415326 
3518717 
8327138 
6123211 
1313532 
1125652 
1222215

▣ 출력예제 1 3


"""


def check_anagram(board):
    count = 0

    for i in range(7):
        row_line = board[i]
        col_line = [board[row][i] for row in range(7)]
        for j in range(3):
            if row_line[j] == row_line[j + 4] and row_line[j + 1] == row_line[j + 3]:
                count = count + 1
            if col_line[j] == col_line[j + 4] and col_line[j + 1] == col_line[j + 3]:
                count = count + 1
    print(count)


for i in range(1, 6):
    sys.stdin = open(f"test/in{i}.txt", "rt")
    board = []
    for _ in range(7):
        board.append(list(map(int, input().split())))
    check_anagram(board)
