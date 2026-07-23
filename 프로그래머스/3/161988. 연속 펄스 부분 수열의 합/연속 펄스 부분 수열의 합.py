def solution(sequence):
    N = len(sequence)
    dp1 = [0] * N #첫번째가 -1
    dp2 = [0] * N
    
    dp1[0] = sequence[0] * -1
    dp2[0] = sequence[0]
    for i in range(1, N):
        if i%2 != 0:
            dp1[i] = max(dp1[i-1] + sequence[i], sequence[i])
            dp2[i] = max(dp2[i-1] + sequence[i]*-1, sequence[i]*-1)
        else:
            dp1[i] = max(dp1[i-1] + sequence[i]*-1, sequence[i]*-1)
            dp2[i] = max(dp2[i-1] + sequence[i], sequence[i])
    return max(max(dp1), max(dp2))