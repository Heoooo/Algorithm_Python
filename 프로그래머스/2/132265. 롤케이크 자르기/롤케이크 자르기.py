def solution(topping):
    N = len(topping)
    left = set()
    right = set(topping)
    right_check = [0] * 10001
    
    for t in topping:
        right_check[t] += 1
    
    rs = 0
    for t in topping:
        left.add(t)
        right_check[t] -= 1
        if right_check[t] == 0:
            right.remove(t)
            
        if len(left) == len(right):
            rs += 1
        
        if len(left) >  len(right):
            break
    return rs
    
    
    
    