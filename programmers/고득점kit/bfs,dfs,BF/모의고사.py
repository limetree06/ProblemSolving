def solution(answers):
    student_ans = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    score = [0, 0, 0]
    
    for index in range(len(answers)):
        for _id in range(3):
            ans = student_ans[_id]
            if ans[index % len(ans)] == answers[index]:
                score[_id] +=1
    
    MAX_SCORE = max(score)
    answer = []
    for i in range(3):
        if score[i] == MAX_SCORE:
            answer.append(i+1)
    return answer