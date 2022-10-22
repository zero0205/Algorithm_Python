def solution(n, works):
    answer = 0
    if len(works) == 1:
        return (works[0] - n) ** 2 if (works[0] - n) > 0 else 0
    works = sorted(works, reverse=True)
    idx = 0
    while n > 0:
        works[idx] -= 1
        idx += 1
        n -= 1
        if idx == len(works) or works[idx-1] >= works[idx]:
            idx = 0
    
    if works[0] < 0:
        return 0
    
    for i in works:
        answer += i ** 2
    return answer

print(solution(4, [4,3,3]))
print(solution(1, [2,1,2]))
print(solution(3, [1,1]))