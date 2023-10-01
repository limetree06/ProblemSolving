import sys


""" 
철수는 그의 바둑이들을 데리고 시장에 가려고 한다. 그런데 그의 트럭은 C킬로그램 넘게 태 울수가 없다. 
철수는 C를 넘지 않으면서 그의 바둑이들을 가장 무겁게 태우고 싶다.
N마리의 바둑이와 각 바둑이의 무게 W가 주어지면, 철수가 트럭에 태울 수 있는 가장 무거운 무게를 구하는 프로그램을 작성하세요.

▣ 입력예제
259 5
81
58
42 
33
61

▣ 출력예제
242
"""


def cal_weight(index, sum, tsum):
    global result
    # 너무 느릴때 이렇게 cut edge할만한것들 다 해야함
    if sum + (total - tsum) < result:
        return
    if sum > C:
        return
    if index == N:
        if result < sum <= C:
            result = sum
        return

    else:
        cal_weight(index + 1, sum + weight_list[index], tsum + weight_list[index])
        cal_weight(index + 1, sum, tsum + weight_list[index])


if __name__ == "__main__":
    for i in range(1, 6):
        sys.stdin = open(f"test/in{i}.txt", "rt")
        C, N = map(int, input().split())
        weight_list = []
        result = 0
        for _ in range(N):
            weight_list.append(int(input()))
        total = sum(weight_list)
        cal_weight(0, 0, 0)
        print(result)
