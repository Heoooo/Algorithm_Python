from collections import defaultdict
def solution(k, tangerine):
    tang = defaultdict(int)
    for t in tangerine:
        tang[t] += 1
    sort_tang = sorted(tang.items(), key=lambda x:x[1], reverse=True)
    
    rs = 0
    tmp = 0
    for key, value in sort_tang:
        tmp += value
        rs += 1
        if tmp >= k:
            return rs
        
    return rs
    