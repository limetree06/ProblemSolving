import sys


def check(classes, a):
    required = list(a)
    while classes and required:
        lesson = classes.pop(0)
        if lesson == required[0]:
            required.pop(0)

    if required:
        return "NO"
    else:
        return "YES"


for i in range(1, 6):
    print(f"-------{i} 채점--------")
    sys.stdin = open(f"test/in{i}.txt", "rt")
    required = list(input())
    N = int(input())

    for i in range(N):
        classes = list(input())
        result = check(classes, required)
        print(f"#{i+1} {result}")
