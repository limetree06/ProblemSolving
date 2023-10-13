#이분탐색
def solution(n, times):
    max_value = 2 * min(times) * n
    min_value = 0
    time = 0
    while max_value >= min_value:
        time = (max_value + min_value) // 2
        people = 0
        for wait in times:
            people += (time // wait)
        
        if people >= n:
            max_value = time - 1
        elif people == n:
            max_value = time - 1
        else:
            min_value = time + 1
    return max(max_value, min_value)