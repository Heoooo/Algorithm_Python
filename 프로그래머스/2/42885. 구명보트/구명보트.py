def solution(people, limit):
    people.sort(reverse = True)
    rs = 0
    for i in people:
        big = i
        if big + people[-1] <= limit:
            people.pop()
        rs += 1
    return rs