import sys


def func():
    print()


for i in range(1, 6):
    sys.stdin = open(f"test/in{i}.txt", "rt")
    func()
