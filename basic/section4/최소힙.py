import sys


def func():
    return 0


for i in range(1, 6):
    sys.stdin = open(f"test/in{i}.txt", "rt")
