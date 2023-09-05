"""
문제 : 
N개의 숫자로 이루어진 숫자열이 주어지면 해당 숫자열중에서 s번째부터 e번째 까지의 수를 오름 차순 정렬했을 때 k번째로 나타나는 숫자를 출력하는 프로그램을 작성하세요.

▣ 입력예제 1 2
6253 527389 15 3 10 3
4 15 8 16 6 6 17 3 10 11 18 7 14 7 15

▣ 출력예제 1 #1 7
#2 6

"""
import sys


def kth(n, s, e, k, case_list):
    sort_list = case_list[s - 1 : e]
    sort_list.sort()
    print(sort_list[k - 1])


def input_parse_func():
    T = int(input())
    for i in range(T):
        n, s, e, k = map(int, input().split())
        case_list = list(map(int, input().split()))
        kth(n, s, e, k, case_list)


for i in range(1, 6):
    sys.stdin = open(f"test/in{i}.txt", "rt")
    input_parse_func()

    """
    ** input() 라이브러리는 한줄씩 불러오는 거다.
    n, s, e, k = map(int, input.split()) 하면 공백으로 나눠져서 각 값에 들어가서
    여기서 list로 묶어주면 list(map(int, input().split())) 값들의 리스트가 됨.
    """
