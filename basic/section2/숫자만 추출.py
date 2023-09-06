import sys

""" 
문자와 숫자가 섞여있는 문자열이 주어지면 그 중 숫자만 추출하여 그 순서대로 자연수를 만 듭니다. 만들어진 자연수와 그 자연수의 약수 개수를 출력합니다.
만약 “t0e0a1c2h0er”에서 숫자만 추출하면 0, 0, 1, 2, 0이고 이것을 자연수를 만들면 120이 됩니다.즉첫자리0은자연수화할때무시합니다. 출력은120를출력하고,다음줄에120 의 약수의 개수를 출력하면 됩니다.
추출하여 만들어지는 자연수는 100,000,000을 넘지 않습니다.

▣ 입력설명
첫 줄에 숫자가 썩인 문자열이 주어집니다. 문자열의 길이는 50을 넘지 않습니다.

▣ 출력설명
첫 줄에 자연수를 출력하고, 두 번째 줄에 약수의 개수를 출력합니다.

▣ 입력예제 1 
g0en2Ts8eSoft

▣ 출력예제 1 
28
6
"""


def extract_num(word):
    letter_list = list(word)
    num = 0
    for i in letter_list:
        if ord(i) > 47 and ord(i) < 58:
            num = num * 10 + int(i)
    print(num)
    get_divisors(num)


def get_divisors(num):
    square = int(num**0.5)
    count = 0
    for i in range(1, square + 1):
        if num % i == 0:
            count = count + 1
    count = count * 2
    if num % square == square:
        count = count - 1
    print(count)


for i in range(1, 6):
    sys.stdin = open(f"test/in{i}.txt", "rt")
    word = input()
    extract_num(word)
