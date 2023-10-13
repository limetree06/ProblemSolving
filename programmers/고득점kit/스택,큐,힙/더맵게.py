import heapq

def solution(scoville, K):
    scoville.sort()
    answer = 0
    while len(scoville) > 1:
        MIN = heapq.heappop(scoville)
        if MIN >= K:
            break
        else:
            MIN_2 = heapq.heappop(scoville)
            heapq.heappush(scoville, MIN + MIN_2 * 2)
            answer += 1
    
    if scoville[0] < K:
        return -1
    else:
        return answer