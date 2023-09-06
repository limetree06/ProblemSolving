import sys


def func():
    print()


def input_parse_func():
    print()


for i in range(1, 6):
    sys.stdin = open(f"test/in{i}.txt", "rt")
    input_parse_func()
