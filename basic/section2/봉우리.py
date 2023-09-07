import sys

""" 
나의 풀이 방법 : 그냥 상화좌우 일일히 비교하는것
새로운 풀이 방법 : 상화좌우에 -1를 곱하고 봉우리랑 더해서 더 큰지 작은지 비교하는 것
"""


def check_peak(N, field):
    count = 0
    for i in range(N):
        for j in range(N):
            peak = field[i + 1][j + 1]

            if (
                peak > field[i][j + 1]
                and peak > field[i + 1][j]
                and peak > field[i + 1][j + 2]
                and peak > field[i + 2][j + 1]
            ):
                count = count + 1
    print(count)


for i in range(1, 6):
    sys.stdin = open(f"test/in{i}.txt", "rt")
    N = int(input())
    field = [[0] * (N + 2)] * (N + 2)
    for i in range(N):
        mount = list(map(int, input().split()))
        field[i + 1] = [0] + mount + [0]
    check_peak(N, field)
