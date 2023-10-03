import sys

""" 
이번 정보올림피아드대회에서 좋은 성적을 내기 위하여 현수는 선생님이 주신 N개의 문제를 풀려고 합니다.
각 문제는 그것을 풀었을 때 얻는 점수와 푸는데 걸리는 시간이 주어지게 됩니다. 
제한시간 M안에 N개의 문제 중 최대점수를 얻을 수 있도록 해야 합니다. (해당문제는 해당시간이 걸리면 푸는 걸로 간주한다, 한 유형당 한개만 풀 수 있습니다.)

▣ 입력설명
첫 번째 줄에 문제의 개수N(1<=N<=20)과 제한 시간 M(10<=M<=300)이 주어집니다.
두 번째 줄부터 N줄에 걸쳐 문제를 풀었을 때의 점수와 푸는데 걸리는 시간이 주어집니다.

▣ 출력설명
첫 번째 줄에 제한 시간안에 얻을 수 있는 최대 점수를 출력합니다.

▣ 입력예제
5 20
10 5
25 12
15 8
63 74

▣ 출력예제
41
"""


# def max_score(level, tscore, ttime):
#     global score
#     if level == nums - 1:
#         if score < tscore:
#             score = tscore
#         return
#     else:
#         for i in range(level + 1, nums):
#             if ttime + load[i][1] <= limited:
#                 max_score(i, tscore + load[i][0], ttime + load[i][1])
#             else:
#                 if score < tscore:
#                     score = tscore


def max_score(level, tscore, ttime):
    global score
    if ttime > limited:
        return
    if level == nums:
        if tscore > score:
            score = tscore
        return
    else:
        max_score(level + 1, tscore + load[level][0], ttime + load[level][1])
        max_score(level + 1, tscore, ttime)


for i in range(1, 6):
    sys.stdin = open(f"test/in{i}.txt", "rt")
    nums, limited = map(int, input().split())
    load = []
    for _ in range(nums):
        load.append(list(map(int, input().split())))
    score = 0
    max_score(0, 0, 0)
    print(score)
