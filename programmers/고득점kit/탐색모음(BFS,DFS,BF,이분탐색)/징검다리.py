#이분탐색
def solution(distance, rocks, n):
    N = len(rocks) - n +1
    rocks.append(distance)
    rocks.sort()
    
    min_value = 0
    max_value = distance
    while min_value <= max_value:
        mid = (min_value + max_value) // 2
        count = 1
        start = mid
        for r in rocks:
            if start == r:
                count += 1
                start += mid
            elif start < r:
                start = r + mid
                count += 1
        if count > N :
            min_value = mid + 1
        else:
            max_value = mid - 1
    return max_value