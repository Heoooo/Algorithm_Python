def solution(weights):
    N = len(weights)
    w = dict()
    for i in range(N):
        if weights[i] in w:
            w[weights[i]] += 1
        else:
            w[weights[i]] = 1
    
    rs = 0
    for k in w:
        if w[k] > 1:
            rs += w[k] * (w[k]-1) // 2
        if k*2 in w:
            rs += w[k] * w[k*2]
        if k%2 == 0 and k*3//2 in w:
            rs += w[k] * w[k*3//2]
        if k%3 == 0 and k*4//3 in w:
            rs += w[k] * w[k*4//3]

    return rs