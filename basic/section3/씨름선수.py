import sys


def athlete_num(spec):
    count = 0
    tallest = 0
    for height, weight in spec:
        if height > tallest:
            count = count + 1
            tallest = height
    return count


for i in range(1, 6):
    sys.stdin = open(f"test/in{i}.txt", "rt")
    N = int(input())
    spec = []
    for i in range(N):
        spec.append(list(map(int, input().split())))

    spec.sort(key=lambda x: [x[1], x[0]], reverse=True)
    print(athlete_num(spec))
