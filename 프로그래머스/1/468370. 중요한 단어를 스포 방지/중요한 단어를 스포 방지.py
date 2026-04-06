def solution(message, spoiler_ranges):
    words = message.split()
    
    base = set()
    spo = []
    
    left_idx = 0
    if message[0] == ' ':
        left_idx = 1
    
    right_idx = 0
    for word in words:
        flag = False
        right_idx = left_idx + len(word)-1
        for spoiler_left, spoiler_right in spoiler_ranges:
            if (spoiler_left <= left_idx <= spoiler_right or spoiler_left <= right_idx <= spoiler_right or (left_idx <= spoiler_left and spoiler_right <= right_idx)) and not flag:
                spo.append(word)
                flag = True
                break
        if not flag:
            base.add(word)
            
        left_idx += len(word) + 1
    
    rs = 0
    for s in spo:
        if s not in base:
            rs += 1
            base.add(s)
    return rs
        