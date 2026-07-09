def solution(plans):
    idx = 0
    for s, time, d in plans:
        hour, minute = time.split(":")
        tmp = int(hour)*60 + int(minute)
        plans[idx][1] = tmp
        plans[idx][2] = int(d)
        idx += 1
    plans.sort(key=lambda x:x[1])
    
    rs = []
    tmp = []
    index = 0
    while index < len(plans)-1:
        #다음 과목까지의 시간
        next_time = plans[index+1][1] - plans[index][1]
        if next_time >= plans[index][2]:
            rs.append(plans[index][0])
            k = next_time - plans[index][2]
            while k > 0 and tmp:
                sub, time, dur = tmp.pop()
                if k >= dur:
                    rs.append(sub)
                    k -= dur
                else:
                    tmp.append((sub, time, dur-k))
                    k = 0
            index += 1
        else:
            tmp.append((plans[index][0], plans[index][1], plans[index][2] - next_time))
            index += 1
    rs.append(plans[-1][0])
    while tmp:
        rs.append(tmp.pop()[0])
    return rs