def solution(book_time):
    check = [0] * 1440
    for start, end in book_time:
        h1, m1 = start.split(":")
        tmp1 = int(h1)*60
        tmp1 += int(m1)
        
        h2, m2 = end.split(":")
        tmp2 = int(h2)*60
        tmp2 += int(m2)
        
        for i in range(tmp1, min(tmp2+10, 1440)):
            check[i] += 1
        # for j in range(tmp2+1, min(tmp2+11, 1440)):
        #     check[j] -= 1
    
    return max(check)
    