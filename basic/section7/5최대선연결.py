import sys

""" 
Longest Increasing Subsequence 문제
"""


for i in range(1, 6):
    sys.stdin = open(f"test/in{i}.txt", "rt")
    N = int(input())
    lines = list(map(int, input().split()))
    check = [1] * N
    for i in range(N):
        MAX = 1
        for j in range(i, -1, -1):
            prev_num = lines[j]
            if lines[j] < lines[i] and MAX < check[j] + 1:
                MAX = check[j] + 1
        check[i] = MAX
    print(max(check))
