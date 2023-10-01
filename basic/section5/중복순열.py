import sys


""" 
1부터 N까지 번호가 적힌 구슬이 있습니다. 이 중 중복을 허락하여 M번을 뽑아 일렬로 나열 하는 방법을 모두 출력합니다.

▣ 입력설명
첫 번째 줄에 자연수 N(3<=N<=10)과 M(2<=M<=N) 이 주어집니다.

▣ 출력설명
첫 번째 줄에 결과를 출력합니다.
맨 마지막 총 경우의 수를 출력합니다. 출력순서는 사전순으로 오름차순으로 출력합니다.


"""


def func(num):
    global count
    if num == M:
        for i in check:
            print(i, end=" ")
        count += 1
        print()
        return
    else:
        for i in range(N):
            check[num] = i + 1
            func(num + 1)


for i in range(1, 6):
    print(f"-------------{i}-----------------")
    sys.stdin = open(f"test/in{i}.txt", "rt")
    N, M = map(int, input().split())
    check = [0] * M
    count = 0
    func(0)
    print(count)
