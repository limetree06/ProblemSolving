import sys

""" 
임의의 N개의 숫자가 입력으로 주어집니다. N개의 수를 오름차순으로 정렬한 다음 N개의 수 중 한 개의 수인 M이 주어지면 이분검색으로 M이 정렬된 상태에서 몇 번째에 있는지 구하는 프로그램을 작성하세요. 단 중복값은 존재하지 않습니다.

▣ 입력설명
첫 줄에 한 줄에 자연수 N(3<=N<=1,000,000)과 M이 주어집니다. 두 번째 줄에 N개의 수가 공백을 사이에 두고 주어집니다.

▣ 출력설명
첫 줄에 정렬 후 M의 값의 위치 번호를 출력한다.

▣ 입력예제
8 32
23 87 65 12 57 32 99 81

▣ 출력예제
3
"""


def selection_sort(numbers):
    list_len = len(numbers)
    for i in range(list_len):
        minimum_index = i
        minimum = numbers[i]
        for j in range(i, list_len):
            if numbers[j] < minimum:
                minimum = numbers[j]
                minimum_index = j
        numbers[i], numbers[minimum_index] = numbers[minimum_index], numbers[i]
    return numbers


def binary_search(numbers, M):
    start = 0
    end = len(numbers)
    while 1:
        middle_index = (start + end) // 2
        if numbers[middle_index] > M:
            end = middle_index
        elif numbers[middle_index] < M:
            start = middle_index
        elif numbers[middle_index] == M:
            break
    print(middle_index + 1)


for i in range(1, 6):
    sys.stdin = open(f"test/in{i}.txt", "rt")
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    numbers = selection_sort(numbers)
    binary_search(numbers, M)
