import heapq 
def solution(operations):
    Q = []
    for operation in operations:
        operator, operand = operation.split(' ')
        if operator == "I":
            heapq.heappush(Q, int(operand))
            
        elif operator == "D" and Q:
            if operand == "-1":
                heapq.heappop(Q)
            else:
                Q.remove(max(Q))
                
    return [max(Q), min(Q)] if Q else [0,0]