import sys

"""
현수는 네트워크 선을 1m, 2m의 길이를 갖는 선으로 자르려고 합니다. 예를 들어 4m의 네트워크 선이 주어진다면
1) 1m+1m+1m+1m 2) 2m+1m+1m
3) 1m+2m+1m
4) 1m+1m+2m
5) 2m+2m
의 5가지 방법을 생각할 수 있습니다. (2)와 (3)과 (4)의 경우 왼쪽을 기준으로 자르는 위치가 다르면 다른 경우로 생각한다.
그렇다면 네트워크 선의 길이가 Nm라면 몇 가지의 자르는 방법을 생각할 수 있나요?
    
"""


def top_up(x):
    if x == 1 or x == 2:
        return x
    else:
        return top_up(x - 1) + top_up(x - 2)


def bottom_up(N):
    dp = [0] * (N + 1)
    for i in range(1, N + 1):
        if i == 1 or i == 2:
            dp[i] = i
        else:
            dp[i] = dp[i - 1] + dp[i - 2]
    return dp[N]


for i in range(1, 6):
    sys.stdin = open(f"test/in{i}.txt", "rt")
    N = int(input())
    print(bottom_up(N))
    print(top_up(N))
