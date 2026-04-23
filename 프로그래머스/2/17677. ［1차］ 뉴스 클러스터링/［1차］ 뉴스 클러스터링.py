def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()
    N = len(str1)
    M = len(str2)
    tmp1 = []
    tmp2 = []
    for i in range(N-1):
        if 65 <= ord(str1[i]) <= 90:
            if 65 <= ord(str1[i+1]) <= 90:
                tmp1.append(str1[i] + str1[i+1])
    for i in range(M-1):
        if 65 <= ord(str2[i]) <= 90:
            if 65 <= ord(str2[i+1]) <= 90:
                tmp2.append(str2[i] + str2[i+1])
                
    merges = set(tmp1 + tmp2)
    min_merge = []
    max_merge = []
    for merge in merges:
        k1 = tmp1.count(merge)
        k2 = tmp2.count(merge)
        min_merge.append(min(k1, k2))
        max_merge.append(max(k1, k2))
    

    if sum(min_merge) != 0 and len(max_merge) != 0:
        return int(sum(min_merge) /sum(max_merge) * 65536)
    elif sum(min_merge) == 0 and len(max_merge) != 0:
        return 0
    else:
        return 65536
    
    
    