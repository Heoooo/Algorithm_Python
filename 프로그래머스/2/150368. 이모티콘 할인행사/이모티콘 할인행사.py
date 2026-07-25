def solution(users, emoticons):
    N = len(users)
    M = len(emoticons)
    discount = [0] * M
    disc = [10, 20, 30, 40]
    answer = [0, 0]
    
    def emo(idx):
        nonlocal answer
        if idx == M:
            rs1 = 0
            rs2 = 0
            for i in range(N):
                tmp = 0
                for j in range(M):
                    if users[i][0] <= discount[j]:
                        tmp += emoticons[j] * (1 - discount[j] / 100)
                if tmp >= users[i][1]:
                    rs1 += 1
                else:
                    rs2 += tmp
            
            if rs1 > answer[0] or (rs1 == answer[0] and rs2 >answer[1]):
                answer = [rs1, rs2]
            return
        
        for i in range(4):
            discount[idx] = disc[i]
            emo(idx+1)
    emo(0)
    return answer
            