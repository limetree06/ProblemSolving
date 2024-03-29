import sys

"""  
현수와 친구들은 과자를 사먹기 위해 사다리 타기를 합니다. 사다리 표현은 2차원 평면은 0으 로 채워지고, 사다리는 1로 표현합니다.
현수는 특정도착지점으로 도착하기 위해서는 몇 번째 열에서 출발해야 하는지 알고싶습니다. 특정 도착지점은 2로 표기됩니다. 

▣ 입력설명
10*10의 사다리 지도가 주어집니다.

▣ 출력설명
출발지 열 번호를 출력하세요.

▣ 입력예제
1 0 1 0 0 1 0 1 0 1 
1 0 1 1 1 1 0 1 0 1 
1 0 1 0 0 1 0 1 0 1 
1 0 1 0 0 1 0 1 1 1 
1 0 1 0 0 1 0 1 0 1 
1 0 1 1 1 1 0 1 0 1 
1 0 1 0 0 1 0 1 1 1 
1 1 1 0 0 1 0 1 0 1 
1 0 1 0 0 1 1 1 0 1 
1 0 1 0 0 2 0 1 0 1

▣ 출력예제
7

"""
dx = [-1, 1, 0]
dy = [0, 0, 1]


def dfs(y, x):
    if y == 0:
        return x
    else:
        board[y][x] = 0
        if 0 <= x - 1 < 10 and board[y][x - 1] == 1:
            return dfs(y, x - 1)
        elif 0 <= x + 1 < 10 and board[y][x + 1] == 1:
            return dfs(y, x + 1)
        else:
            return dfs(y - 1, x)


for i in range(1, 6):
    sys.stdin = open(f"test/in{i}.txt", "rt")
    board = []
    for i in range(10):
        board.append(list(map(int, input().split())))

    for i in range(10):
        if board[9][i] == 2:
            print(dfs(9, i))
