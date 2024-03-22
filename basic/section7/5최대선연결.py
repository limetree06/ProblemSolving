import sys

""" 
Longest Increasing Subsequence 문제
"""


for i in range(1, 6):
    sys.stdin = open(f"test/in{i}.txt", "rt")
    N = int(input())
    lines = list(map(int, input().split()))
    dp = [1] * N
    for i in range(N):
        MAX = dp[i]
        for j in range(i, -1, -1):
            if lines[i] > lines[j] and dp[j] + 1 > MAX:
                MAX = dp[j] + 1
        dp[i] = MAX
    print(max(dp))
