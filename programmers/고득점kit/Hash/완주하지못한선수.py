def solution(participant, completion):
    name = dict()
    name[participant.pop()] = 1
    
    for i in range(len(completion)):
        p = participant[i]
        c = completion[i]
        keys = name.keys()
        if p in keys:
            name[p] = name[p]+1
        else:
            name[p] = 1
        if c in keys:
            name[c] = name[c]-1
        else:
            name[c] = -1

    answer = [key for key, value in name.items() if value == 1]
    return answer[0]


import collections
#Counter 객체 이용가능
def solution_2(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]