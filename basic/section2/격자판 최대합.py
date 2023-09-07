import sys

""" 
N*N의 격자판이 주어지면 각 행의 합, 각 열의 합, 두 대각선의 합 중 가 장 큰 합을 출력합니다.

▣ 입력설명
첫 줄에 자연수 N이 주어진다.(1<=N<=50)
두 번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어진다. 각 자연수는 100을 넘지 않는다.

▣ 출력설명 최대합을 출력합니다.

▣ 입력예제 1
5
10 13 10 12 15 12 39 30 23 11 11 25 50 53 15 19 27 29 37 27 19 13 30 13 19

▣ 출력예제 1 
155
"""


def get_max_line(N, table):
    sum_list = []

    for row in range(0, N * N, N):
        diagonal_line_1 = 0
        diagonal_line_2 = 0
        sum_list.append(sum(table[row : row + N]))
        diagonal_line_1 = diagonal_line_1 + table[row + row // N]
        diagonal_line_2 = diagonal_line_2 + table[row - row // N]

    sum_list.append(diagonal_line_1)
    sum_list.append(diagonal_line_2)

    for col in range(N):
        col_sum = 0
        for num in range(N):
            col_sum = col_sum + table[num * N + col]
        sum_list.append(col_sum)

    print(max(sum_list))


for i in range(1, 6):
    sys.stdin = open(f"test/in{i}.txt", "rt")
    N = int(input())
    table = []
    for i in range(N):
        table = table + list(map(int, input().split()))
    get_max_line(N, table)
