def solution(storey):
    rs = 0
    while storey > 0:
        k = storey % 10
        tmp = storey // 10
        if k < 5 or (k == 5 and tmp%10 < 5):
            rs += k
        else:
            rs += (10 - k)
            tmp += 1
        storey = tmp
    return rs