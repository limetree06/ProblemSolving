import sys


def move_box(box_list):
    box_list[0] = box_list[0] + 1
    box_list[-1] = box_list[-1] - 1
    box_list.sort()
    return box_list


def clean_up(box_list, count):
    for _ in range(count):
        move_box(box_list)

    print(box_list[-1] - box_list[0])


for i in range(1, 6):
    sys.stdin = open(f"test/in{i}.txt", "rt")
    row = int(input())
    box_list = list(map(int, input().split()))
    count = int(input())
    box_list.sort()
    clean_up(box_list, count)
