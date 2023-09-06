import sys

""" 
오름차순으로 정렬이 된 두 리스트가 주어지면 두 리스트를 오름차순으로 합쳐 출력하는 프로 그램을 작성하세요.

▣ 입력설명
첫 번째 줄에 첫 번째 리스트의 크기 N(1<=N<=100)이 주어집니다. 두 번째 줄에 N개의 리스트 원소가 오름차순으로 주어집니다.
세 번째 줄에 두 번째 리스트의 크기 M(1<=M<=100)이 주어집니다. 네 번째 줄에 M개의 리스트 원소가 오름차순으로 주어집니다.
각 리스트의 원소는 int형 변수의 크기를 넘지 않습니다.

▣ 출력설명
오름차순으로 정렬된 리스트를 출력합니다.
"""


def combine_list(n, n_list, m, m_list):
    new_list = [0] * (n + m)
    for i in range(n + m):
        if len(n_list) == 0 or len(m_list) == 0:
            break
        if n_list[0] >= m_list[0]:
            new_list[i] = m_list.pop(0)
        else:
            new_list[i] = n_list.pop(0)

    if len(n_list) == 0:
        left_len = len(m_list)
        for i in range(left_len):
            new_list[n + m - i - 1] = m_list.pop()

    elif len(m_list) == 0:
        left_len = len(n_list)
        for i in range(left_len):
            new_list[n + m - i - 1] = n_list.pop()
    print(new_list)


for i in range(1, 6):
    sys.stdin = open(f"test/in{i}.txt", "rt")
    N_1 = int(input())
    list_1 = list(map(int, input().split()))
    N_2 = int(input())
    list_2 = list(map(int, input().split()))
    combine_list(N_1, list_1, N_2, list_2)
