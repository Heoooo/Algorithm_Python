def solution(sequence):

    dp1, dp2 = 0, 0
    max_sum1, max_sum2 = float('-inf'), float('-inf')
    
    pulse = 1
    for num in sequence:
        val1 = num * pulse
        val2 = num * (-pulse)
        
        dp1 = max(dp1 + val1, val1)
        dp2 = max(dp2 + val2, val2)
        
        max_sum1 = max(max_sum1, dp1)
        max_sum2 = max(max_sum2, dp2)
        
        pulse *= -1
        
    return max(max_sum1, max_sum2)