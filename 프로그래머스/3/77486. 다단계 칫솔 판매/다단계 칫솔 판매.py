import math
def solution(enroll, referral, seller, amount):
    rs = []
    ref = dict()
    profit = dict()
    
    N = len(enroll)
    for i in range(N):
        ref[enroll[i]] = referral[i]
        profit[enroll[i]] = 0
    
    M = len(seller)
    for i in range(M):
        p = amount[i] * 100
        k = ref[seller[i]]

        tmp = p - math.trunc(p * 0.1)
        profit[seller[i]] += tmp

        p = math.trunc(p * 0.1)

        while k != "-" and p > 0:
            tmp = p - math.trunc(p * 0.1)
            profit[k] += tmp
            k = ref[k]
            p = math.trunc(p*0.1)
    
    for i in range(N):
        rs.append(profit[enroll[i]])
    return rs