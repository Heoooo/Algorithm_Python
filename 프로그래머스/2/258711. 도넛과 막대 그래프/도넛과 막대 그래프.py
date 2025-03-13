from collections import defaultdict
def solution(edges):
    
    graphin = defaultdict(list)
    graphout = defaultdict(list)
    for start, end in edges:
        graphin[end].append(start)
        graphout[start].append(end)
    
    root = 0
    for node in graphout:
        if not graphin[node] and len(graphout[node]) >= 2:
            root = node
            break
            
    one, two, three = 0, 0, 0
    for node in graphout[root]:
        parent = node
        while True:
            if len(graphout[node]) == 1:
                node = graphout[node][0]
                if node == parent:
                    one += 1
                    break
            elif len(graphout[node]) >= 2:
                three += 1
                break
            else:
                two += 1
                break
    return [root, one, two, three]