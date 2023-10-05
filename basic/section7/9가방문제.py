import sys
import time

""" 
최고 17kg의 무게를 저장할 수 있는 가방이 있다. 그리고 각각 3kg, 4kg, 7kg, 8kg, 9kg의 무게를 가진 5종류의 보석이 있다. 
이 보석들의 가치는 각각 4, 5, 10, 11, 13이다.
이 보석을 가방에 담는데 17kg를 넘지 않으면서 최대의 가치가 되도록 하려면 어떻게 담아야 할까요? 
각 종류별 보석의 개수는 무한이 많다. 한 종류의 보석을 여러 번 가방에 담을 수 있 다는 뜻입니다.

▣ 입력설명
첫 번째 줄은 보석 종류의 개수와 가방에 담을 수 있는 무게의 한계값이 주어진다. 두 번째 줄부터 각 보석의 무게와 가치가 주어진다.
가방의 저장무게는 1000kg을 넘지 않는다. 보석의 개수는 30개 이내이다.

▣ 출력설명
첫 번째 줄에 가방에 담을 수 있는 보석의 최대가치를 출력한다.

▣ 입력예제
4 11
5 12
3 8
6 14 
4 8

▣ 출력예제
28

"""


"""
내 풀이
1키로 ~ limit키로를 돌면서 각 무게의 최대 value를 구한다.




시간 : 0.02
"""
for i in range(5, 6):
    sys.stdin = open(f"test/in{i}.txt", "rt")
    N, limit = map(int, input().split())
    values = [0] * (limit + 1)
    for _ in range(N):
        weight, value = map(int, input().split())
        values[weight] = value

    start = time.time()
    for i in range(1, limit + 1):
        MAX = values[i]
        for j in range(1, i + 1 // 2):
            if MAX < values[i - j] + values[j]:
                MAX = values[i - j] + values[j]
        values[i] = MAX
    print(values[limit])
    print(time.time() - start)


""" 
답지 풀이 : 
처음에는 보석하나만 쓴다고 가정하고 보석무게~limit무게까지 각 무게에서 구할 수 있는 최대 value를 구한다.

시간 : 0.004
20% 감소... 왜지?
"""

for i in range(5, 6):
    sys.stdin = open(f"test/in{i}.txt", "rt")
    N, limit = map(int, input().split())
    values = [0] * (limit + 1)
    jews = []
    for _ in range(N):
        jews.append(list(map(int, input().split())))
    start = time.time()
    for i in jews:
        for j in range(i[0], limit + 1):
            v = i[1] + values[j - i[0]]
            if values[j] < v:
                values[j] = v
    print(values[limit])
    print(time.time() - start)
