import sys
from collections import deque

"""  
현수는 송아지를 잃어버렸다. 다행히 송아지에는 위치추적기가 달려 있다. 
현수의 위치와 송아 지의 위치가 직선상의 좌표 점으로 주어지면 현수는 현재 위치에서 송아지의 위치까지 다음과 같은 방법으로 이동한다.
현수는 스카이 콩콩을 타고 가는데 한 번의 점프로 앞으로 1, 뒤로 1, 앞으로 5를 이동할 수 있다. 
최소 몇 번의 점프로 현수가 송아지의 위치까지 갈 수 있는지 구하는 프로그램을 작성 하세요.

▣ 입력설명
첫 번째 줄에 현수의 위치 S와 송아지의 위치 E가 주어진다. 직선의 좌표 점은 1부터 10,000 까지이다.

▣ 출력설명
점프의 최소횟수를 구한다.

▣ 입력예제
5 14

▣ 출력예제
3
"""


# def min_jump(distance):
#     if distance <= 0:
#         return distance * -1
#     else:
#         count = distance // 5
#         distance -= 5 * count
#         if distance == 4:
#             return count + 2
#         else:
#             return count + distance


def bfs(start, end):
    ch[start] = 1
    dQ = deque()
    dQ.append(start)
    while dQ:
        now = dQ.popleft()
        if now == end:
            break
        for next in (now + 5, now + 1, now - 1):
            if 0 < next <= 10000 and ch[next] == 0:
                dQ.append(next)
                ch[next] = ch[now] + 1


for i in range(1, 6):
    sys.stdin = open(f"test/in{i}.txt", "rt")
    start, end = map(int, input().split())
    # min_jump(end - start)
    MAX = 10000
    ch = [0] * (MAX + 1)
    bfs(start, end)
    print(ch[end] - 1)
