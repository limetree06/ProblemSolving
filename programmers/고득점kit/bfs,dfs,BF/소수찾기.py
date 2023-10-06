def is_prime(num):
    if num < 2:
        return False
    MAX_ROOT = int(num ** (1/2))
    for i in range(2, MAX_ROOT+1):
        if num % i == 0:
            return False
    return True


def solution(numbers):
    num_list = list(numbers)
    N = len(num_list)
    check = [0] * N
    answer = set()
    
    def dfs(level, value):
        if value and is_prime(int(value)):
            answer.add(int(value))
        if level == N:
            return
        else:
            for i in range(N):
                if check[i] == 0:
                    check[i] = 1
                    dfs(level + 1, value + num_list[i]) 
                    check[i] = 0
                 
    dfs(0, "")
    return len(answer)