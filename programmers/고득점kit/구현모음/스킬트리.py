def solution(skill, skill_trees):
    count = len(skill_trees)
    sdict = dict()
    for s in range(len(skill)):
        sdict[skill[s]] = s
    
    for st in skill_trees:
        index = 0
        for word in list(st):
            if word in skill:
                if index != sdict[word]:
                    count -= 1
                    break
                else:
                    index+=1
    return count

            
            