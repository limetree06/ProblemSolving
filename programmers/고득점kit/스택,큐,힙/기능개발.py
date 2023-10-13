def solution(progresses, speeds):
    answer = []
    while progresses:
        count = 0
        for index in range(len(progresses)):
            progresses[index] += speeds[index]

        while progresses:
            if progresses[0] >=100:
                count+=1
                progresses.pop(0)
                speeds.pop(0)
            else:
                break
        
        if count:
            answer.append(count) 
    return answer