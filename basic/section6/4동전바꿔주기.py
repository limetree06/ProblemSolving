import sys

""" 
명보네 동네 가게의 현금 출납기에는 k가지 동전이 각각n1, n2, ... , nk개 씩 들어있다.
가게 주인은 명보에게 T원의 지폐를 동전으로 바꿔 주려고한다. 이때, 동전 교환 방법은 여러 가지가 있을 수 있다.
예를 들어, 10원 짜리, 5원 짜리, 1원 짜리 동전이 각각2개, 3개, 5개씩 있을 때, 20원 짜리 지폐를 다음과 같은4가지 방법으로 교환할 수 있다.
20 = 10 × 2
20 = 10 × 1+5 × 2
20 = 10 × 1+5 × 1+1 × 5
20 = 5 × 3+1 × 5
입력으로 지폐의 금액 T, 동전의 가지수 k, 각 동전 하나의금액 pi와 개수 ni가 주어질 때 (i=1,2,...,k)
지폐를 동전으로 교환하는 방법의 가지 수를 계산하는프로그램을 작성하시오. 방법의 수는 231 을 초과하지않는 것으로 가정한다.

▣ 입력설명
첫째 줄에는지폐의 금액 T(0<T≤10,000), 둘째 줄에는 동전의 가지 수k(0<k≤10), 
셋째 줄부터 마지막 줄까지는 각 줄에 동전의금액 pi(0<pi≤T)와 개수 ni(0<ni≤10)가 주어진다. pi와 ni 사이 에는 빈 칸이 하나씩 있다.

▣ 출력설명
첫 번째 줄에 동전 교환 방법의 가지 수를 출력한다.(교환할 수 없는 경우는 존재하지 않는 다.)

▣ 입력예제
20
3
5 3
10 2
1 5

▣ 출력예제
4

"""


def exchange(level, sum):
    global count
    if sum == cash:
        count += 1
        return
    if level == k:
        return
    elif sum > cash:
        return
    else:
        for i in range(coin_info[level][1] + 1):
            exchange(level + 1, sum + coin_info[level][0] * i)


for i in range(1, 6):
    sys.stdin = open(f"test/in{i}.txt", "rt")
    cash = int(input())
    k = int(input())
    coin_info = []
    count = 0
    for i in range(k):
        coin_info.append(list(map(int, input().split())))
    exchange(0, 0)
    print(count)
