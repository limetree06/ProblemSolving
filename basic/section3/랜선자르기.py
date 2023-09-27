import sys

""" 
엘리트 학원은 자체적으로 K개의 랜선을 가지고 있다. 그러나 K개의 랜선은 길이가 제각각이 다. 선생님은 랜선을 모두 N개의 같은 길이의 랜선으로 만들고 싶었기 때문에 K개의 랜선을 잘라서 만들어야 한다. 예를 들어 300cm 짜리 랜선에서 140cm 짜리 랜선을 두 개 잘라내면 20cm 은 버려야 한다. (이미 자른 랜선은 붙일 수 없다.)
편의를 위해 랜선을 자를때 손실되는 길이는 없다고 가정하며, 기존의 K개의 랜선으로 N개의 랜선을 만들 수 없는 경우는 없다고 가정하자. 그리고 자를 때는 항상 센티미터 단위로 정수 길이만큼 자른다고 가정하자. N개보다 많이 만드는 것도 N개를 만드는 것에 포함된다. 이때 만들 수 있는 최대 랜선의 길이를 구하는 프로그램을 작성하시오.
▣ 입력설명
첫째 줄에는 엘리트학원이 이미 가지고 있는 랜선의 개수 K, 그리고 필요한 랜선의 개수 N이 입력된다. K는 1이상 10,000이하의 정수이고, N은 1이상 1,000,000이하의 정수이다. 그리고 항상 K ≦ N 이다. 그 후 K줄에 걸쳐 이미 가지고 있는 각 랜선의 길이가 센티미터 단위의   이하의 자연수로 주어진다.
▣ 출력설명
첫째 줄에 N개를 만들 수 있는 랜선의 최대 길이를 센티미터 단위의 정수로 출력한다.
▣ 입력예제 1 4 11
802
743
457 539
▣ 출력예제 1 200
예제설명) 802cm 랜선에서 4개, 743cm 랜선에서 3개, 457cm 랜선에서 2개, 539cm 랜선에서 2개를 잘라내 모두 11개를 만들 수 있다
"""

""" 
기존의 나의 방식 : 랜선 길이를 다 더해서 잘라야 하는 갯수 만큼 나누면 최대 길이가 나온다. 
그래서 그 최대 길이보다 1씩 길이를 줄여가면서 가장 최대값을 찾는 방식
-> 어째튼 탐색을 하는 과정인데 1씩 줄여가면서 찾는 과정은 배우 비효율적

1씩 줄이는 것이 아니라 절반씩 줄이면서 이분 탐색을 하는 거다.
"""
# 기존 방식 코드
# def longest_line(line_size_list, N):
#     total_size = sum(line_size_list)
#     max_size = total_size // N

#     for cutting_size in range(max_size, 0, -1):
#         count = 0
#         for size in line_size_list:
#             count = count + (size // cutting_size)
#         if count >= N:
#             return cutting_size


# 이분 탐색 적용한 코드
def longest_line(line_size_list, N):
    total_size = sum(line_size_list)
    max_value = total_size // N
    min_value = 0

    while max_value >= min_value:
        cut_size = (max_value + min_value) // 2
        count = 0
        for size in line_size_list:
            count = count + (size // cut_size)
        if count >= N:
            min_value = cut_size + 1
        else:
            max_value = cut_size - 1
    return (max_value + min_value) // 2


for i in range(1, 6):
    sys.stdin = open(f"test/in{i}.txt", "rt")
    line_size_list = []
    K, N = map(int, input().split())
    for i in range(K):
        line_size_list.append(int(input()))

    print(longest_line(line_size_list, N))
