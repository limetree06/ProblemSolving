import sys

""" 
월드컵축구의 응원을 위한 모임에서 회장을 선출하려고 한다. 
이모임은 만들어진지 얼마 되지 않았기 때문에 회원사이에 서로 모르는 사람도 있지만, 몇 사람을 통하면 서로 모두 알 수 있 다.
각 회원은 다른 회원들과 가까운 정도에 따라 점수를 받게 된다. 예를 들어 어느 회원이 다른 모든 회원과 친구이면, 이 회원의 점수는 1점이다. 
어느 회원의 점수가 2점이면, 다른 모든 회원이 친구이거나, 친구의 친구임을 말한다. 
또한, 어느 회원의 점수가 3점이면, 다른 모든 회원이 친구이거나, 친구의 친구이거나, 친국의 친구의 친구임을 말한다.
4점, 5점등은 같은 방법으로 정해진다.각 회원의 점수를 정할 때 주의할 점은 어떤 두 회원이 친구 사이이면서 동시에 친구의 친구 사이이면, 
이 두 사람은 친구사이라고 본다. 회장은 회원들 중에서 점수가 가장 작은 사람이 된다.
회장의 점수와 회장이 될 수 있는 모든 사람을 찾는 프로그램을 작성하시오.

▣ 입력설명
입력의 첫째 줄에는 회원의 수가 있다.
단, 회원의 수는 50명을 넘지 않는다. 둘째 줄 이후로는 한 줄에 두 개의 회원번호가 있는데, 이것은 두 회원이 서로 친구임을 나타낸다. 
회원번호는 1부터 회원의 수만큼 번호가 붙어있다. 마지막 줄에는 -1이 두 개 들어있다

▣ 출력설명
첫째 줄은 회장 후보의 점수와 회장후보 수를 출력하고 두 번째 줄은 회장 후보를 모두 출력 한다.

▣ 입력예제
5
1 2 
2 3
3 4
4 5
2 4
5 3
-1 -1
▣ 출력예제
2 3
2 3 4

"""


def func():
    print()


for i in range(1, 6):
    print(f"============={i}==================")
    sys.stdin = open(
        f"/Users/minjison/Desktop/취업준비/ProblemSolving/basic/test/in{i}.txt", "rt"
    )
    N = int(input())
    community = [[N for _ in range(N)] for _ in range(N)]
    while True:
        s, e = list(map(int, input().split()))
        if s == -1 or e == -1:
            break
        else:
            community[s - 1][e - 1] = 1
            community[e - 1][s - 1] = 1

    for a in range(N):
        community[a][a] = 0

    for k in range(N):
        for start in range(N):
            for end in range(N):
                community[start][end] = min(
                    community[start][end], community[start][k] + community[k][end]
                )

    result = [max(community[i]) for i in range(N)]
    res = min(result)
    answer = []
    for index, value in enumerate(result):
        if value == res:
            answer.append(index + 1)
    print(res, len(answer))
    print(answer)
