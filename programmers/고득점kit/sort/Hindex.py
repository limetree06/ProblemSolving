def solution(citations):
    citations.sort(reverse = True)
    LEN = len(citations)
    for index in range(LEN, 0, -1):
        count = 0
        for j in citations:
            if j >= index:
                count+=1
            else:
                break
        if count >= index and index >=LEN-count:
            return index
    return 0