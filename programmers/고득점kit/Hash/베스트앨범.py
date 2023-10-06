def solution(genres, plays):
    table = []
    c_type = dict()
    for i in range(len(genres)):
        table.append([genres[i] ,plays[i], i])
        if genres[i] in c_type.keys():
            c_type[genres[i]] = c_type[genres[i]] + plays[i]
        else:
            c_type[genres[i]] = plays[i]
    
    table.sort(key = lambda x :[x[0], x[1], -x[2]], reverse=True)
    
    answer = []
    
    while c_type:
        MAX = max(c_type.values())
        for key, value in c_type.items():
            if value == MAX:
                break
        count = 0
        for music in table:
            if music[0] == key:
                answer.append(music[2])
                count +=1
                if count == 2:
                    break
        del c_type[key]
        
    return answer