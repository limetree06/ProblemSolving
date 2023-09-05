'''
문제 : 

고려하지 못했던 점:
- 약수를 구할때 약수를 구하고자하는 값의 루트를 씌워서 그 전까지 나눠봐야하는데 그냥 나누기 2해서 나머지가 0인애들 구했음.
    문제점 : 중복으로 값이 들어가는 친구들이 생겨서 에러 발생
    
- 완전 제곱수의 경우 나누기했을 때 같은 값이 두번 나오게 되는데 그 경우도 값이 중복으로 들어가서 케이스 고려안됨  
    
강의에서의 문제 풀이 법:

'''
# def kth_divisor(N, K):
#     div_list = []
#     for i in range(1, int(N**(1/2))+1):
#         if N % i == 0:
#            div_list.append(i)
#            if i != N//i:
#                 div_list.append(N // i) 
#     div_list.sort()
#     if len(div_list) < K:
#         return -1
#     else:
#         return div_list[K-1]

def kth_divisor(N,k):
    count = 0
    for i in range(1, N+1):
        if N%i == 0:
            count = count + 1
        if k == count:
            return i
    else:
        return -1
            
    
print(kth_divisor(8,4))
print(kth_divisor(25,5))
print(kth_divisor(100,5))
print(kth_divisor(100,7))
print(kth_divisor(1000,12))
            

