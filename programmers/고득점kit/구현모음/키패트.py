def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def solution(numbers, hand):
    cord_y = lambda num : ((12 - num) // 3) % 4
    answer = ''
    prev_left = [0,0]
    prev_right = [2,0]
    for num in numbers:
        if num in [1, 4, 7]:
            answer+='L'
            prev_left = [0, cord_y(num)]
        elif num in [3, 6, 9]:
            answer+='R'
            prev_right = [2, cord_y(num)]
        elif num in [2,5,8,0]:
            cord = [1, cord_y(num)]
            left_dis = distance(prev_left, cord)
            right_dis = distance(prev_right, cord)
            
            if left_dis > right_dis:
                answer+='R'
                prev_right = cord
            elif right_dis > left_dis:
                answer+='L'
                prev_left = cord
            else:
                if hand == "left":
                    answer+='L'
                    prev_left = cord
                else:
                    answer+='R'
                    prev_right = cord
        
    return answer