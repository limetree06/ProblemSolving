import sys

""" 
선생님은 현수에게 숫자 하나를 주고, 해당 숫자의 자릿수들 중 m개의 숫자를 제거하 여 가장 큰 수를 만들라고 했습니다.
여러분이 현수를 도와주세요.(단 숫자의 순서는 유지해야 합니다)
만약 5276823 이 주어지고 3개의 자릿수를 제거한다면
7823이 가장 큰 숫자가 됩니다.

▣ 입력설명 : 첫째 줄에 숫자(길이는 1000을 넘지 않습니다)와 제가해야할 자릿수의 개수가 주어집니다.

▣ 출력설명 : 가장 큰 수를 출력합니다.

▣ 입력예제 5276823 3
▣ 출력예제 7823
▣ 입력예제 9977252641 5
▣ 출력예제 99776
"""


def remove(number_list, N):
    stack = []
    count = 0
    for num in number_list:
        for j in reversed(stack):
            if count == N:
                break
            if j < num:
                stack.pop()
                count = count + 1
        stack.append(num)

    if count != N:
        for _ in range(N - count):
            stack.pop()
    return stack


for i in range(1, 6):
    sys.stdin = open(f"test/in{i}.txt", "rt")
    number, N = map(int, input().split())
    number_list = []
    while number != 0:
        number_list.append(number % 10)
        number = number // 10
    number_list.reverse()
    stack = remove(number_list, N)

    mine = ""
    for ans in stack:
        mine = mine + str(ans)

    sys.stdin = open(f"test/out{i}.txt", "rt")
    answer = input()
    if mine == answer:
        print(i, True, mine, answer)
