def solution(a):
    result = set()
    
    # 1. 왼쪽에서 오른쪽으로 가면서 지금까지의 최솟값들을 저장
    min_val = float('inf')
    for num in a:
        if num < min_val:
            min_val = num
            result.add(num)
            
    # 2. 오른쪽에서 왼쪽으로 가면서 지금까지의 최솟값들을 저장
    min_val = float('inf')
    for num in reversed(a):
        if num < min_val:
            min_val = num
            result.add(num)
            
    # 3. 양쪽 기준 최솟값으로 등록된 숫자들의 총 개수를 반환 (중복 제거됨)
    return len(result)