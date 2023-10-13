
#O(n^2) 풀이
def solution(prices):
    N = len(prices)
    answer = [0] * N
    
    for index, value in enumerate(prices):
        for j in range(index + 1, N):
            if value > prices[j]:
                answer[index] = j - index
                break
        else:
            answer[index] = N - index -1
    return answer

#O(n) 풀이 -> stack 활용

