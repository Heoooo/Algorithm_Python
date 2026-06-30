def solution(bandage, health, attacks):
    start_time = 0
    end_time = attacks[-1][0]
    attack_time = [0] * (end_time+1)
    for t, p in attacks:
        attack_time[t] = p
    
    t, x, y = bandage
    tmp = 1
    hp = health
    for i in range(1, end_time+1):
        if attack_time[i] != 0:
            hp -= attack_time[i]
            tmp = 0
            if hp <= 0:
                return -1
        else:
            tmp += 1
            hp = min(hp+x, health)
            if tmp == t:
                hp = min(hp+y, health)
                tmp = 0
    return hp
            
        
    