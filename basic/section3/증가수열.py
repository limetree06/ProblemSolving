import sys

""" 
1부터 N까지의 모든 자연수로 구성된 길이 N의 수열이 주어집니다.
이 수열의 왼쪽 맨 끝 숫자 또는 오른쪽 맨 끝 숫자 중 하나를 가져와 나열하여 가장 긴 증가수열 을 만듭니다. 
이때 수열에서 가져온 숫자(왼쪽 맨 끝 또는 오른쪽 맨 끝)는 그 수열에서 제거됩니 다.
예를 들어 2 4 5 1 3 이 주어지면 만들 수 있는 가장 긴 증가수열의 길이는 4입니다.
맨 처음 왼쪽 끝에서 2를 가져오고, 그 다음 오른쪽 끝에서 3을 가져오고, 왼쪽 끝에서 4, 왼쪽끝에서5를가져와 2345 증가수열을만들수있습니다.

▣ 입력설명
첫째 줄에 자연수 N(3<=N<=100)이 주어집니다. 두 번째 줄에 N개로 구성된 수열이 주어집니다.

▣ 출력설명
첫째 줄에 최대 증가수열의 길이를 출력합니다.
두 번째 줄에 가져간 순서대로 왼쪽 끝에서 가져갔으면 ‘L', 오른쪽 끝에서 가져갔으면 ’R'를 써 간 문자열을 출력합니다.(단 마지막에 남은 값은 왼쪽 끝으로 생각합니다.)

▣ 입력예제
5
2 4 5 1 3

▣ 출력예제
4
LRLL
"""


def sequence(numbers):
    new_numbers = list(numbers)
    answer = ""
    last = 0
    while True:
        left = new_numbers[0]
        right = new_numbers[-1]
        if right >= last and left >= last:
            if left >= right >= last:
                last = new_numbers.pop()
                answer = answer + "R"

            elif right >= left >= last:
                last = new_numbers.pop(0)
                answer = answer + "L"

        elif right >= last >= left or left >= last >= right:
            if right >= last:
                last = new_numbers.pop()
                answer = answer + "R"

            elif left >= last:
                last = new_numbers.pop(0)
                answer = answer + "L"

        elif last >= left and last >= right:
            break

    print(len(answer))
    print(answer)


for i in range(1, 6):
    sys.stdin = open(f"test/in{i}.txt", "rt")
    N = int(input())
    numbers = list(map(int, input().split()))
    sequence(numbers)
