def solution(schedules, timelogs, startday):
    N = len(schedules)
    rs = 0
    
    for i in range(N):
        minute = schedules[i] % 100
        hour = schedules[i] // 100
        minute += 10
        if minute >= 60:
            hour += 1
            # if hour == 24:
            #     hour = 0
            minute %= 60
        time = hour*100 + minute
        
        flag = False
        s_day = startday
        for j in range(7):
            if s_day > 7:
                s_day = 1
            if s_day % 6 == 0 or s_day % 7 == 0:
                s_day += 1
                continue
            if timelogs[i][j] > time:
                flag = True
                break
            s_day += 1
        if not flag:
            rs += 1
        
    return rs
            