import sys


def cal_prize(num_list):
    if num_list[0] == num_list[1] and num_list[1] == num_list[2]:  # 모두 같은 경우
        return 10000 + num_list[0] * 1000
    elif (
        num_list[0] != num_list[1]
        and num_list[1] != num_list[2]
        and num_list[0] != num_list[2]
    ):  # 모두 다른 경우
        return max(num_list) * 100
    else:  # 3개중 3개 같은 경우
        if num_list[0] == num_list[1]:
            return num_list[0] * 100 + 1000
        elif num_list[1] == num_list[2]:
            return num_list[1] * 100 + 1000
        elif num_list[0] == num_list[2]:
            return num_list[0] * 100 + 1000


def input_parse_func():
    N = int(input())
    num_list = []
    for i in range(N):
        numbers = list(map(int, input().split()))
        num_list.append(numbers)

    prizes = [cal_prize(nums) for nums in num_list]
    print(max(prizes))


for i in range(1, 6):
    sys.stdin = open(f"test/in{i}.txt", "rt")
    input_parse_func()
