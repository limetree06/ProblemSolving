def solution(routes):
    routes.sort(key = lambda x: x[1])
    count = 0
    last_cam = -float('inf')
    for index in range(len(routes)-1):
        first = routes[index]
        second = routes[index+1]
        if first[0] <= last_cam <= first[1]:
            continue
        else:
            count += 1
            if first[1] < second[0]:
                last_cam = first[1]
            elif second[0] <= first[1] < second[1]:
                last_cam = first[1]
            elif second[1] <= first[1] :
                last_cam = second[1]
            else:
                count -=1
            
    if routes[-1][0] <= last_cam <= routes[-1][1]:
        return count
    else: return count +1


''' 
<Testcase>
print(solution([[-2,-1], [1,2],[-3,0]])) #2
print(solution([[0,0],])) #1
print(solution([[0,1], [0,1], [1,2]])) #1
print(solution([[0,1], [2,3], [4,5], [6,7]])) #4
print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]])) #2
print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]])) #2
print(solution([[-20,15], [-20,-15], [-14,-5], [-18,-13], [-5,-3]])) #2


'''