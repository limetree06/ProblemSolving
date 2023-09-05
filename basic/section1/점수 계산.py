import sys


def cal_score(answer_list):
    extra_score = 0
    total_score = 0
    for i in answer_list:
        if i == 1:
            total_score = total_score + extra_score + 1
            extra_score = extra_score + 1
        else:
            extra_score = 0
    print(total_score)


for i in range(1, 6):
    sys.stdin = open(f"test/in{i}.txt", "rt")
    N = int(input())
    answer_list = list(map(int, input().split()))
    cal_score(answer_list)
