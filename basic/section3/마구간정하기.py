import sys

""" 
N개의 마구간이 수직선상에 있습니다. 각 마구간은 x1, x2, x3, ......, xN의 좌표를 가지며, 마 구간간에 좌표가 중복되는 일은 없습니다.
현수는 C마리의 말을 가지고 있는데, 이 말들은 서로 가까이 있는 것을 좋아하지 않습니다. 각 마구간에는 한 마리의 말만 넣을 수 있고, 가장 가까운 두 말의 거리가 최대가 되게 말을 마구간에 배치하고 싶습니다.
C마리의 말을 N개의 마구간에 배치했을 때 가장 가까운 두 말의 거리가 최대가 되는 그 최대 값을 출력하는 프로그램을 작성하세요.

▣ 입력설명
첫 줄에 자연수 N(3<=N<=200,000)과 C(2<=C<=N)이 공백을 사이에 두고 주어집니다. 둘째 줄부터 N개의 줄에 걸쳐 마구간의 좌표 xi(0<=xi<=1,000,000,000)가 한 줄에 하나씩 주어집니다.

▣ 출력설명
첫 줄에 가장 가까운 두 말의 최대 거리를 출력하세요.

▣ 입력예제
53
1
2
8 4 9

▣ 출력예제
3
"""


def get_horse_num(house_list, distance):
    left_horse = house_list[0]
    N = len(house_list)
    count = 1
    for i in range(1, N):
        right_horse = house_list[i]
        if right_horse - left_horse >= distance:
            count = count + 1
            left_horse = right_horse
    return count


def max_range(house_list, horse_num):
    max = house_list[-1]
    min = 1
    result = 0
    while max >= min:
        mid = (max + min) // 2
        horses = get_horse_num(house_list, mid)
        if horses >= horse_num:
            result = mid
            min = mid + 1
        else:
            max = mid - 1
    return result


for i in range(1, 6):
    sys.stdin = open(f"test/in{i}.txt", "rt")
    house_list = []
    N, C = map(int, input().split())
    for i in range(N):
        house_list.append(int(input()))

    house_list.sort()
    print(max_range(house_list, C))
