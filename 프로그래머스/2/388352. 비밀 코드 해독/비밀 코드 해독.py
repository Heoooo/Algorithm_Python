from itertools import combinations
def solution(n, q, ans):
    lst = []
    m = len(ans)
    for i in range(n):
        lst.append(i+1)
    
    rs = 0
    for comb in combinations(lst, 5):
        flag = True
        for i in range(m):
            a = set(comb)
            b = set(q[i])
            if len(a & b) != ans[i]:
                flag = False
                break
                
        if flag:
            rs += 1
    return rs