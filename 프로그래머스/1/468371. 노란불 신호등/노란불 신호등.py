import math
def solution(signals):
    N = len(signals)
    
    max_time = 1
    for signal in signals:
        time = sum(signal)
        max_time = (max_time * time) // math.gcd(max_time, time)
    
    for i in range(1, max_time+1):
        flag = True
        
        for j in range(N):
            g, y, r = signals[j]
            cur = (i-1) % sum(signals[j])
            
            if not(g <= cur < g+y):
                flag = False
                break
        
        if flag:
            return i
    return -1