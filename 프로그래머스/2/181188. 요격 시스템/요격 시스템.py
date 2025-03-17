def solution(targets):
    targets.sort(key = lambda x:x[1])
    
    rs = 0
    fin = 0
    for s, e in targets:    
        if s < fin:
            continue
        else:
            rs += 1
            fin = e
    return rs