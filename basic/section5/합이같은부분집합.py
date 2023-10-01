import sys

""" 
N개의 원소로 구성된 자연수 집합이 주어지면, 이 집합을 두 개의 부분집합으로 나누었을 때 두 부분집합의 원소의 합이 서로 같은 경우가 존재하면 “YES"를 출력하고, 
그렇지 않으면 ”NO"를 출력하는 프로그램을 작성하세요.
둘로 나뉘는 두 부분집합은 서로소 집합이며, 두 부분집합을 합하면 입력으로 주어진 원래의 집합이 되어 합니다.
예를 들어 {1, 3, 5, 6, 7, 10}이 입력되면 {1, 3, 5, 7} = {6, 10} 으로 두 부분집합의 합이 16으로 같은 경우가 존재하는 것을 알 수 있다.
"""

""" 
<새로 알게된 사실>
sys.exit(0) -> 이러면 바로 빠져나간다.

<나의 풀이 방식>
index 로 재귀
"""


def subset_sum(index):
    if index == N - 1:
        sum_1 = 0
        sum_2 = 0
        for i in range(N):
            if check[i]:
                sum_1 += num_list[i]
            else:
                sum_2 += num_list[i]

        if sum_1 == sum_2:
            return True
        else:
            return False
    else:
        check[index] = 1
        if subset_sum(index + 1):
            return True
        check[index] = 0
        if subset_sum(index + 1):
            return True
        return False


if __name__ == "__main__":
    for i in range(1, 6):
        sys.stdin = open(f"test/in{i}.txt", "rt")
        N = int(input())
        num_list = list(map(int, input().split()))
        check = [0] * N
        result = subset_sum(0)
        print(result)
