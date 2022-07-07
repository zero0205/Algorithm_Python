def sort_func(i, p, answer):
    n = len(p)
    min_value = min(p[i:])
    j = p.index(min_value)
    if  j != i:
        p[i], p[j] = p[j], p[i]
        answer[i] += 1
        answer[j] += 1        


def solution(p):
    answer = [0] * len(p)
    for i in range(len(p)):
        sort_func(i, p, answer)
    return answer

print(solution([2,5,4,1,4]))
print(solution([2,3,4,5,6,1]))
print(solution([1,2,3,4,5,6,7,8,9]))