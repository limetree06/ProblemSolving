def solution(clothes):
    closet = dict()
    for name, categroy in clothes:
        if categroy in closet.keys():
            closet[categroy] = closet[categroy] + 1
        else:
            closet[categroy] = 1
    
    case = list(closet.values())
    N = 2 ** len(case)
    answer = 0
    for i in range(1, N):
        num = i
        count = 0
        multi = 1
        while count != len(case) and num > 0 :
            if num % 2 == 1:
                multi *= case[count]
            count +=1
            num = num // 2
        answer += multi
        multi = 1
            
    return answer


def solution_1(clothes):
    closet = dict()
    for name, categroy in clothes:
        if categroy in closet.keys():
            closet[categroy] = closet[categroy] + 1
        else:
            closet[categroy] = 1
    
    # (a+b+b) + (ab+bc+ac) + abc = (a+1)(b+1)(c+1) - 1
    value_list = closet.values()
    answer = 1
    for i in value_list:
        answer *= (i +1)
    
    return answer-1

# 하 나 진짜 수학 감 다 잃엇네..