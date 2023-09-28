import sys


def postfix_calc(input):
    is_bracket = False
    bracket = ""
    stack = []
    for char in input:
        if is_bracket and char != ")":
            bracket += char
            continue

        if char in ["+", "-", "*", "/"]:
            x = stack.pop()
            y = stack.pop()
            if char == "+":
                stack.append(y + x)
            elif char == "-":
                stack.append(y - x)
            elif char == "*":
                stack.append(y * x)
            elif char == "/":
                stack.append(y / x)

        elif char == "(":
            is_bracket = True
        elif char == ")":
            is_bracket, bracket = False, ""
            stack.append(postfix_calc(list(bracket)))
        else:
            stack.append(int(char))
    return stack.pop()


for i in range(1, 6):
    sys.stdin = open(f"test/in{i}.txt", "rt")
    in_list = list(input())
    result = postfix_calc(in_list)

    sys.stdin = open(f"test/out{i}.txt", "rt")
    answer = int(input())

    if result == answer:
        print(i, True, answer)
    else:
        print(i, False, result, answer)
