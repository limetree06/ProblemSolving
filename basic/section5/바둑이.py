import sys


def cal_weight(index, sum):
    global result
    if sum > C:
        return
    if index == N:
        if result < sum <= C:
            result = sum
        return

    else:
        cal_weight(index + 1, sum + weight_list[index])
        cal_weight(index + 1, sum)


if __name__ == "__main__":
    for i in range(1, 6):
        sys.stdin = open(f"test/in{i}.txt", "rt")
        C, N = map(int, input().split())
        weight_list = []
        result = 0
        for _ in range(N):
            weight_list.append(int(input()))

        cal_weight(0, 0)
        print(result)
