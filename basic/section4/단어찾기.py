import sys


for i in range(1, 6):
    sys.stdin = open(f"test/in{i}.txt", "rt")
    N = int(input())
    words = dict()
    notes = []
    for _ in range(N):
        word = input()
        words[word] = False

    for _ in range(N - 1):
        poem = input()
        words[poem] = True

    for key, value in words.items():
        if value == False:
            print(key)
            break
