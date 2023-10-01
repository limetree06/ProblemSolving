import sys

""" 
1부터N까지번호가적힌구슬이있습니다.
이중 M개를뽑아일렬로나열하는방법을모두 출력합니다

"""


def func(num):
    global count
    if num == M:
        for n in check:
            print(n, end=" ")
        count += 1
        print()
        return
    else:
        for i in range(N):
            if num_list[i] == 0:
                check[num] = i + 1
                num_list[i] = 1
                func(num + 1)
                num_list[i] = 0


for i in range(1, 6):
    sys.stdin = open(f"test/in{i}.txt", "rt")
    N, M = map(int, input().split())
    check = [0] * M
    num_list = [0] * N
    count = 0
    func(0)
    print(count)
