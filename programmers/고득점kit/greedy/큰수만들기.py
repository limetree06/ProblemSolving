def solution(number, k):
    num_list = list(number)
    answer = []
    while num_list:
        MAX = max(num_list[0 : k+1])
        for i in list(num_list[0 : k+1]):
            if i == MAX:
                answer.append(num_list.pop(0))
                break
            else:
                num_list.pop(0)
                k -= 1
    if k:
        return "".join(answer[:-k] + num_list)
    else:
        return "".join(answer + num_list)
    
def solution(number, k):
    stack = []
    
    for digit in number:
        # 스택에 있는 숫자가 현재 숫자보다 작고, 아직 제거해야 할 숫자(k)가 남아 있다면
        while k > 0 and stack and stack[-1] < digit:
            stack.pop()  # 스택에서 더 작은 숫자를 제거
            k -= 1

        stack.append(digit)
    
    # 만약 k개의 숫자를 다 제거하지 못한 경우, 나머지 숫자를 제거
    if k > 0:
        stack = stack[:-k]

    return ''.join(stack)
