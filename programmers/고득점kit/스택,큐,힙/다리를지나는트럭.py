from collections import deque

def solution(bridge_length, weight, truck_weights):
    waiting = deque(truck_weights)
    on_bridge = deque([0 for _ in range(bridge_length)])
    
    total_weight = 0
    hours = 0
    while total_weight or waiting:
        hours += 1
        total_weight -= on_bridge.popleft()
        truck = waiting.popleft() if waiting else 0
        
        if total_weight + truck <= weight:
            on_bridge.append(truck)
            total_weight += truck
        else:
            on_bridge.append(0)
            waiting.appendleft(truck)
            
    return hours