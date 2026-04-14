from collections import defaultdict
import math
def solution(fees, records):
    parking = dict()
    total = defaultdict(int)
    
    for record in records:
        time, num, k = record.split()
        hour, minute = time.split(":")
        tmp = int(hour)*60 + int(minute)
        if k == "IN":
            parking[num] = tmp
        else:
            intime = parking.pop(num)
            total[num] += tmp - intime
    
    for num, intime in parking.items():
        tmp = 1439 - intime
        total[num] += tmp
    total = sorted(total.items())
    
    rs = []
    for num, time in total:
        money = 0
        if time >= fees[0]:
            money += fees[1]
            time -= fees[0]
            money += math.ceil(time/fees[2]) * fees[3]
        else:
            money = fees[1]
        rs.append(money)
    return rs