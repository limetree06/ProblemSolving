import sys


def calculate(farm):
    apples = 0
    N = len(farm)
    for i in range(N // 2):
        apples = apples + sum(farm[i][i : N - i]) + sum(farm[N - i - 1][i : N - i])
    apples = apples + farm[N // 2][N // 2]
    print(apples)


def dry(farm, action_list):
    for action in action_list:
        changed_farm = farm[action[0] - 1]
        if action[1] == 1:  # 오른쪽으로
            for _ in range(action[2]):
                pop = changed_farm.pop()
                changed_farm.insert(0, pop)

        elif action[1] == 0:  # 왼쪽으로
            for _ in range(action[2]):
                pop = changed_farm.pop(0)
                changed_farm.append(pop)
        farm[action[0] - 1] = changed_farm
    calculate(farm)


for i in range(1, 6):
    sys.stdin = open(f"test/in{i}.txt", "rt")
    N = int(input())
    farm = []
    for i in range(N):
        farm.append(list(map(int, input().split())))

    action = int(input())
    action_list = []

    for j in range(action):
        action_list.append(list(map(int, input().split())))

    dry(farm, action_list)
