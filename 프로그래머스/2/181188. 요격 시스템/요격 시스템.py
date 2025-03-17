def solution(targets):
    targets.sort(key = lambda x:x[1])
    
    rs = 0
    fin = 0
    for s, e in targets:
        if fin == 0:
            rs += 1
            fin = e
            continue
        
        if s < fin <= e:
            continue
        else:
            rs += 1
            fin = e
    return rs