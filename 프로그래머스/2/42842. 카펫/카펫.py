import math
def solution(brown, yellow):
    for line in range(1, int(math.sqrt(yellow))+1):
        if yellow % line == 0:
            if brown == ((yellow//line)+2)*2 + (line*2):
                rs = [(yellow//line)+2, line+2]
    return rs
    