import sys


def cut(input):
    stack = []
    count = 0
    last_piece = 0
    before = ""
    for e in input:
        if e == "(":
            stack.append("(")
        elif e == ")":
            stack.pop()
            if before == "(":  # cutting
                count = count + last_piece + len(stack)
                last_piece = 0
            elif before == ")":
                last_piece = last_piece + 1
        before = e
    return count + last_piece


for i in range(1, 6):
    sys.stdin = open(f"test/in{i}.txt", "rt")
    input_list = list(input())
    mine = cut(input_list)
    sys.stdin = open(f"test/out{i}.txt", "rt")
    answer = int(input())
    if mine == answer:
        print(i, True, mine, answer)
