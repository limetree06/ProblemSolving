import sys

""" 
중위표기식이 입력되면 후위표기식으로 변환하는 프로그램을 작성하세요.
중위표기식은 우리가 흔히 쓰은 표현식입니다. 즉 3+5 와 같이 연산자가 피연산자 사이에 있 으면 중위표기식입니다.
후위표기식은 35+ 와 같이 연산자가 피연산자 뒤에 있는 표기식입니다.
예를 들어 중위표기식이 3+5*2 를 후위표기식으로 표현하면 352*+ 로 표현됩니다.
만약 다음과 같이 연산 최우선인 괄호가 표현된 식이라면
(3+5)*2 이면 35+2* 로 바꾸어야 합니다.
"""


def func(input):
    op_stack = []
    in_bracket = ""
    bracket = False
    answer = ""
    for char in input:
        if bracket and char != ")":
            in_bracket += char

        else:
            if char in ["*", "/"]:
                while op_stack and op_stack[-1] in ["*", "/"]:
                    answer += op_stack.pop()
                op_stack.append(char)
            elif char in ["+", "-"]:
                while op_stack:
                    answer += op_stack.pop()
                op_stack.append(char)
            elif char == "(":
                bracket = True
            elif char == ")":
                answer += func(in_bracket)
                bracket, in_bracket = False, ""
            else:  # 숫자일때
                answer += char
    while op_stack:
        answer += op_stack.pop()
    return answer


for i in range(1, 6):
    sys.stdin = open(f"test/in{i}.txt", "rt")
    in_list = list(input())
    mine = func(in_list)

    sys.stdin = open(f"test/out{i}.txt", "rt")
    answer = input()

    if mine == answer:
        print(i, True, answer)
    else:
        print(i, False, mine, answer)
