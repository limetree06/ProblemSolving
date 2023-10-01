import sys


def binary(num):
    if num == 1 or num == 0:
        return str(num)
    else:
        return binary(num // 2) + str(num % 2)


for i in range(1, 6):
    sys.stdin = open(f"test/in{i}.txt", "rt")
    num = int(input())
    result = binary(num)

    sys.stdin = open(f"test/out{i}.txt", "rt")
    answer = input()

    if answer == result:
        print(i, True, result)
    else:
        print(i, False, result, answer)
