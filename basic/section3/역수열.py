import sys

""" 
1부터 n까지의 수를 한 번씩만 사용하여 이루어진 수열이 있을 때,
1부터 n까지 각각의 수 앞 에 놓여 있는 자신보다 큰 수들의 개수를 수열로 표현한 것을 역수열이라 한다.
예를 들어 다음과 같은 수열의 경우
[4 8 6 2 5 1 3 7]
1 앞에 놓인 1보다 큰 수는 4, 8, 6, 2, 5. 이렇게 5개이고,
2 앞에 놓인 2보다 큰 수는 4, 8, 6. 이렇게 3개,
3 앞에 놓인 3보다 큰 수는 4, 8, 6, 5 이렇게 4개...
따라서 [4 8 6 2 5 1 3 7] 의 역수열은 [5 3 4 0 2 1 1 0] 이 된다.
n과 1부터 n까지의 수를 사용하여 이루어진 수열의 역수열이 주어졌을 때, 원래의 수열을 출 력하는 프로그램을 작성하세요.

▣ 입력설명
첫 번째 줄에 자연수 N(3<=N<100)이 주어지고, 두 번째 줄에는 역수열이 숫자 사이에 한칸의 공백을 두고 주어진다.

▣ 출력설명 
원래 수열을 출력합니다.

▣ 입력예제 
8
5 3 4 0 2 1 1 0

▣ 출력예제
4 8 6 2 5 1 3 7 
"""


def normal_list(reverse_list, N):
    answer = [-1 for _ in range(N)]
    for index, reverse in enumerate(reverse_list):
        count = 0
        blank = 0

        for i in range(0, N):
            if index + 1 > answer[i] > -1:
                count = count + 1
            else:
                blank = blank + 1
            if blank == reverse + 1:
                break

        if reverse == 0 and count == 0:
            answer[0] = index + 1
        else:
            answer[reverse + count] = index + 1
    return answer


for i in range(1, 6):
    sys.stdin = open(f"test/in{i}.txt", "rt")
    N = int(input())
    reverse_list = list(map(int, input().split()))
    normal = normal_list(reverse_list, N)
    print(normal)
