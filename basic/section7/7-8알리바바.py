import sys

""" 
알리바바는 40인의 도둑으로부터 금화를 훔쳐 도망치고 있습니다.
알리바바는 도망치는 길에 평소에 잘 가지 않던 계곡의 돌다리로 도망가고자 한다. 계곡의 돌다리는 N×N개의 돌들로 구성되어 있다. 
각 돌다리들은 높이가 서로 다릅니다.해당 돌다리를 건널때 돌의 높이 만큼 에너지가 소비됩니다. 이동은 최단거리 이동을 합니다. 
즉 현재 지점에서 오른쪽 또는 아래쪽으로만 이동해야 합니다.
N*N의 계곡의 돌다리 격자정보가 주어지면 (1, 1)격자에서 (N, N)까지 가는데 드는 에너지의 최소량을 구하는 프로그램을 작성하세요.
만약 N=3이고, 계곡의 돌다리 격자 정보가 다음과 같다면

3 3 5
2 3 4
6 5 2
(1, 1)좌표에서 (3, 3)좌표까지 가는데 드는 최소 에너지는 3+2+3+4+2=14이다.

▣ 입력설명
첫 번째 줄에는 자연수 N(1<=N<=20)이 주어진다.
두 번째 줄부터 계곡의 N*N 격자의 돌다리 높이(10보다 작은 자연수) 정보가 주어진다.

▣ 출력설명
첫 번째 줄에 (1, 1)출발지에서 (N, N)도착지로 가기 위한 최소 에너지를 출력한다.

▣ 입력예제
5
3 7 2 1 9
5 8 3 9 2
5 3 1 2 3
5 4 3 2 1
1 7 5 2 4

▣ 출력예제
25


"""


def bottom_up():
    energy = [[0 for _ in range(N)] for _ in range(N)]

    def get_energy(x, y):
        if x == 0 and y == 0:
            energy[0][0] = board[0][0]
        elif x == 0:
            energy[y][0] = energy[y - 1][0] + board[y][0]
        elif y == 0:
            energy[0][x] = energy[0][x - 1] + board[0][x]

        else:  # 비교필요
            # if energy[y - 1][x] < energy[y][x - 1]:
            #     energy[y][x] = board[y][x] + energy[y - 1][x]
            # else:
            #     energy[y][x] = board[y][x] + energy[y][x - 1]
            energy[y][x] = min(energy[y - 1][x], energy[y][x - 1]) + board[y][x]

    for i in range(N):
        for y in range(i + 1):
            x = i - y
            get_energy(x, y)

    for i in range(N):
        for j in range(1, N - i):
            x = N - j
            y = i + j
            get_energy(x, y)
    return energy[N - 1][N - 1]


def top_down(x, y):
    if energy[x][y] != 0:
        return energy[x][y]
    if x == 0 and y == 0:
        energy[0][0] = board[0][0]
        return energy[0][0]
    else:  # 값이 없을 때
        if x == 0:
            energy[x][y] = top_down(x, y - 1) + board[x][y]
        elif y == 0:
            energy[x][y] = top_down(x - 1, y) + board[x][y]
        else:
            energy[x][y] = min(top_down(x, y - 1), top_down(x - 1, y)) + board[x][y]
        return energy[x][y]


for i in range(1, 6):
    sys.stdin = open(f"test/in{i}.txt", "rt")
    N = int(input())
    board = []
    MAX = 0
    for _ in range(N):
        a = list(map(int, input().split()))
        board.append(a)
        MAX += sum(a)
    energy = [[0 for _ in range(N)] for _ in range(N)]

    print(bottom_up())
    print(top_down(N - 1, N - 1))
