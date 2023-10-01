import sys


# 이항계수로 바꿔볼것
def vaild(num_list):
    result = list(num_list)
    while len(result) > 1:
        answer = []
        for i in range(len(result) - 1):
            answer.append(result[i] + result[i + 1])
        result = answer

    if result[0] == total:
        return True
    else:
        return False


def pascal(nums):
    if nums == N:
        if vaild(answer):
            print(answer)
            sys.exit(0)
        else:
            return
    else:
        for i in range(N):
            if check[i] == 0:
                answer[nums] = i + 1
                check[i] = 1
                pascal(nums + 1)
                check[i] = 0


if __name__ == "__main__":
    for i in range(5, 6):
        sys.stdin = open(f"test/in{i}.txt", "rt")
        N, total = map(int, input().split())
        answer = [0] * N
        check = [0] * N
        pascal(0)
