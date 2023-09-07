import sys

""" 
N개의 수로 된 수열 A[1], A[2], ..., A[N] 이 있다. 이 수열의 i번째 수부터 j번째 수까지의 합 A[i]+A[i+1]+...+A[j-1]+A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.

▣ 입력설명
첫째 줄에 N(1≤N≤10,000), M(1≤M≤300,000,000)이 주어진다. 다음 줄에는 A[1], A[2], ..., A[N]이 공백으로 분리되어 주어진다. 각각의 A[x]는 30,000을 넘지 않는 자연수이다.

▣ 출력설명
첫째 줄에 경우의 수를 출력한다.

▣ 입력예제
83 12131112

▣ 출력예제
5

나의 풀이 방식 : M이 3이라면 1개씩 전체 리스트 체크, 2개식 전체 리스트 체크, 3개씩 전체 리스트 체크를 했다. 
더욱 효율적이니 풀이 방식 : 두개의 포인터를 두고 하나는0번째 하나는 1번째(그 다은번째를 가르킨다.) 그리고 그 사이의 합을 total로 두는데,
total이 M보다 작으면 두번째 포인터를 움직이고 M이랑 같으면 Count를 증가 시키고 M보다 크면 첫번째 포인터를 움직인다.

"""

# 너무너무 비효율적이었던 나의 방식
# def get_sum(N, M, num_list):
#     total_len = len(num_list)
#     count = 0
#     for i in range(M):
#         for j in range(total_len - i):
#             if M == sum(num_list[j : j + i + 1]):
#                 count = count + 1
#     print(count)


def get_sum(N, M, num_list):
    count = 0
    for i in range(len(num_list)):
        for j in range(i + 1, len(num_list) + 1):
            total = sum(num_list[i:j])
            if total > M:
                break
            elif total == M:
                count = count + 1
                break
            elif total < M:
                continue
    print(count)


for i in range(1, 6):
    sys.stdin = open(f"test/in{i}.txt", "rt")
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))
    get_sum(N, M, num_list)
