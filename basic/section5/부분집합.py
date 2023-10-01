import sys

""" 
자연수 N이 주어지면 1부터 N까지의 원소를 갖는 집합의 부분집합을 모두 출력하는 프로그램 을 작성하세요.
"""


def subsets(num):
    if num == N + 1:
        for i in range(1, N + 1):
            if check[i]:
                print(i, end=" ")
        print()
        return
    else:
        check[num] = 1
        subsets(num + 1)
        check[num] = 0
        subsets(num + 1)


if __name__ == "__main__":
    for i in range(1, 6):
        sys.stdin = open(f"test/in{i}.txt", "rt")
        N = int(input())
        check = [0] * (N + 1)
        subsets(1)
