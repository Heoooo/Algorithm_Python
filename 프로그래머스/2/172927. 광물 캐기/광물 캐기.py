def solution(picks, minerals):
    N = min(sum(picks)*5, len(minerals))
    
    total = []
    tmp = []
    for i in range(N):
        if i % 5 == 0:
            if tmp:
                total.append(tmp)
            tmp = [0, 0, 0]
        
        if minerals[i] == 'diamond':
            tmp[0] += 1
        elif minerals[i] == 'iron':
            tmp[1] += 1
        else:
            tmp[2] += 1
        
        if i == N-1:
            total.append(tmp)
    total.sort(key=lambda x: (-x[0], -x[1], -x[2]))
    
    rs = 0
    for t in total:
        if picks[0] > 0:
            rs += t[0]*1 + t[1]*1 + t[2]*1
            picks[0] -= 1
        elif picks[1] > 0:
            rs += t[0]*5 + t[1]*1 + t[2]*1
            picks[1] -= 1
        else:
            rs += t[0]*25 + t[1]*5 + t[2]*1
            picks[2] -= 1
    return rs