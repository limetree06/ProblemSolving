import sys
import time

""" 
자연수 N이 입력되면 1부터 N까지의 소수의 개수를 출력하는 프로그램을 작성하세요.
만약 20이 입력되면 1부터 20까지의 소수는 2, 3, 5, 7, 11, 13, 17, 19로 총 8개입니다.
제한시간은 1초입니다.

"""


def prime_num_count(N):
    count_list = [0] * (N + 1)
    square = int(N**0.5)
    for i in range(2, square + 1):
        for j in range(i * 2, N + 1, i):
            count_list[j] = 1

    count = 0
    for cnt in count_list:
        if cnt == 0:
            count = count + 1
    print(count - 2)


# def prime_num_count(N):
#     prime_num_list = [2]
#     for n in range(2, N + 1):
#         for prime_num in prime_num_list:
#             if n % prime_num == 0:
#                 break
#             elif prime_num == prime_num_list[-1]:
#                 prime_num_list.append(n)
#     print(len(prime_num_list))


for i in range(1, 6):
    sys.stdin = open(f"test/in{i}.txt", "rt")
    N = int(input())
    start = time.time()
    prime_num_count(N)
    print(time.time() - start)
