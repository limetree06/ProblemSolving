import sys
import heapq as hp

""" 
heapq라이브러리 안쓰고 한번 구현해볼껏!

"""


def heap_tree(numbers):
    min_tree = []
    for num in numbers:
        if num == 0:
            print(hp.heappop(min_tree))
        else:
            hp.heappush(min_tree, num)


for i in range(2, 3):
    print(f"--------{i}문제----------")
    sys.stdin = open(f"test/in{i}.txt", "rt")
    numbers = []
    while True:
        num = int(input())
        if num == -1:
            break
        else:
            numbers.append(num)
    heap_tree(numbers)
