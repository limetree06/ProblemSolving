import sys

"""
현수는 1부터 100사이의 자연수가 적힌 N장의 카드를 가지고 있습니다. 같은 숫자의 카드가 여러장 있을 수 있습니다. 현수는 이 중 3장을 뽑아 각 카드에 적힌 수를 합한 값을 기록하려 고 합니다. 3장을 뽑을 수 있는 모든 경우를 기록합니다. 기록한 값 중 K번째로 큰 수를 출력 하는 프로그램을 작성하세요.
만약 큰 수부터 만들어진 수가 25 25 23 23 22 20 19......이고 K값이 3이라면 K번째 큰 값 은 22입니다.

▣ 입력설명
첫 줄에 자연수 N(3<=N<=100)과 K(1<=K<=50) 입력되고, 그 다음 줄에 N개의 카드값이 입력 된다.

▣ 출력설명
첫 줄에 K번째 수를 출력합니다. K번째 수는 반드시 존재합니다.

▣ 입력예제 1
10 3
13 15 34 23 45 65 33 11 26 42

▣ 출력예제 1 143
"""


def kth_largest(N, K, num_list):
    sum_list = []
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                sum = num_list[i] + num_list[j] + num_list[k]
                sum_list.append(sum)
    sum_list.sort(reverse=True)
    count = 0
    compare = -1
    for sum_num in sum_list:
        if compare != sum_num:
            count = count + 1
            compare = sum_num
        if count == K:
            return sum_num


def input_parse_func():
    N, K = map(int, input().split())
    num_list = list(map(int, input().split()))
    print(kth_largest(N, K, num_list))


for i in range(1, 6):
    sys.stdin = open(f"test/in{i}.txt", "rt")
    input_parse_func()

"""
set()이라는 자료구조는 중복되는 값을 제거하고 들어가진다.
res=set()
for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            res.add(a[i]+a[j]+a[m])
res=list(res)
res.sort(reverse=True)
print(res[k-1])
"""
