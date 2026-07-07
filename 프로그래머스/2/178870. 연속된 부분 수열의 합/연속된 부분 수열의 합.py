def solution(sequence, k):
    N = len(sequence)
    rs = [0, N]
    left = 0
    right = 0
    tmp = sequence[0]
    while True:
        if tmp < k:
            right += 1
            if right == N:
                break
            tmp += sequence[right]
        
        elif tmp > k: 
            tmp -= sequence[left]
            left += 1
        else:
            if right - left < rs[1] - rs[0]:
                rs = [left, right]
            right += 1
            if right == N:
                break
            tmp += sequence[right]
    return rs