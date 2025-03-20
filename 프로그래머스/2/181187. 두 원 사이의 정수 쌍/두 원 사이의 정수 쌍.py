import math
def solution(r1, r2):
    #원 방정식: x^2 + y^2 = r^2
    rs = 0
    for i in range(1, r2+1):    #x축 기준
        max_v = math.floor(math.sqrt(r2**2 - i**2))
        min_v = math.ceil(math.sqrt(max(0, (r1**2 - i**2))))
        
        rs += (max_v-min_v)+1
    
    return rs*4