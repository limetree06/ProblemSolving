import sys

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def dfs(x, y):
    global count
    board[x][y] = 0
    count += 1
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < N and 0 <= yy < N and board[xx][yy] == 1:
            dfs(xx, yy)


if __name__ == "__main__":
    for i in range(2, 3):
        print(f"--------------{i}문제=================")
        sys.stdin = open(f"test/in{i}.txt", "rt")
        N = int(input())
        board = []
        count = 0
        result = []
        for i in range(N):
            board.append(list(map(int, input())))

    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                count = 0
                dfs(i, j)
                result.append(count)

    print(len(result))
    for res in result:
        print(res)
    print()
