def solution(players, m, k):
    server = [0] * len(players)
    cnt = 0
    
    for i in range(len(players)):
        remain = players[i]-(server[i]*m)
        if remain >= m:
            end = i+k
            if end > len(players):
                end = len(players)
            for j in range(i, end):
                server[j] += remain // m
            cnt += remain // m
    return cnt
            