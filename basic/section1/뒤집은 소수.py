import sys

""" N개의 자연수가 입력되면 각 자연수를 뒤집은 후 그 뒤집은 수가 소수이면 그 수를 출력하는 프로그램을 작성하세요. 예를 들어 32를 뒤집으면 23이고, 23은 소수이다. 그러면 23을 출력 한다. 단 910를 뒤집으면 19로 숫자화 해야 한다. 첫 자리부터의 연속된 0은 무시한다.
뒤집는 함수인 def reverse(x) 와 소수인지를 확인하는 함수 def isPrime(x)를 반드시 작성하 여 프로그래밍 한다.

▣ 입력설명
첫 줄에 자연수의 개수 N(3<=N<=100)이 주어지고, 그 다음 줄에 N개의 자연수가 주어진다. 각 자연수의 크기는 100,000를 넘지 않는다.

▣ 출력설명
첫 줄에 뒤집은 소수를 출력합니다. 출력순서는 입력된 순서대로 출력합니다.

▣ 입력예제 1
5
32 55 62 3700 250

▣ 출력예제 1 23 73
"""


def reverse(x):
    digit_list = list(str(x))
    reverse_value = 0
    for index, value in enumerate(digit_list):
        reverse_value = reverse_value + int(value) * 10 ** (index)
    return reverse_value


def isPrime(x):
    square = int(x**1 / 2)
    if x == 1:
        return True

    for i in range(2, square + 1):
        if x % i == 0:
            return False
    return True


def input_parse_func():
    N = int(input())
    num_list = list(map(int, input().split()))
    reverse_list = [reverse(x) for x in num_list]
    reverse_prime_list = [x for x in reverse_list if isPrime(x)]
    print(reverse_prime_list)


for i in range(1, 6):
    sys.stdin = open(f"test/in{i}.txt", "rt")
    input_parse_func()
