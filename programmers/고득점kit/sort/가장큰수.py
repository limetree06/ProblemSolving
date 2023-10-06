# def lambda_func(x, MAX_LEN):
#     require_len = MAX_LEN - len(str(x))
#     res = x * (10 ** require_len)
#     for i in range(require_len):
#         res += (x % 10) * (10**i)
#     return res

# def sort(sort_list):
#     if len(sort_list) <2:
#         return sort_list
#     for i in range(len(sort_list)):
#         for j in range(i+1, len(sort_list)):
#             a = sort_list[i]
#             b = sort_list[j]
#             left = int(str(a) + str(b))
#             right = int(str(b) + str(a))
#             if right > left :
#                 mid = sort_list[i]
#                 sort_list[i] = sort_list[j]
#                 sort_list[j] = mid
#     return sort_list


# def solution(numbers):
#     answer = []
#     numbers.sort(key = lambda x: str(x)[0], reverse=True)
#     compare = int(str(numbers[0])[0])
#     sorting = []
#     for num in numbers:
#         if str(compare) == str(num)[0]:
#             sorting.append(num)
#         else:
#             answer += sort(sorting)
#             sorting = [num]
#             compare = int(str(num)[0])
    
#     answer += sort(sorting)
#     res = ""
#     for r in answer:
#         res += str(r)
#     return str(int(res))

def solution(numbers):
    sorted_numbers = sorted(map(str, numbers), key=lambda x: x * 3, reverse=True)
    
    if sorted_numbers[0] == '0':
        return '0'
    
    return ''.join(sorted_numbers)
