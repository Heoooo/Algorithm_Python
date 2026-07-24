def solution(scores):
    target_a, target_b = scores[0]
    target_sum = target_a + target_b
    
    scores.sort(key=lambda x: (-x[0], x[1]))
    
    rank = 1
    max_b = 0
    
    for a, b in scores:
        if target_a < a and target_b < b:
            return -1
            
        if b < max_b:
            continue
            
        if a + b > target_sum:
            rank += 1
            
        max_b = max(max_b, b)
        
    return rank