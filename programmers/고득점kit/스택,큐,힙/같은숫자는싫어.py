def solution(arr):
    stack = [arr.pop(0)]
    for num in arr:
        if num != stack[-1]:
            stack.append(num)
    return stack