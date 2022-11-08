def solution(citations):
    answer = 0
    citations.sort(reverse=True)

    for i in range(len(citations)):
        if i+1 <= citations[i]:
            answer = i+1
        else:
            break
    return answer


print(solution([3, 0, 6, 1, 5]))
# 3
print(solution([6, 5, 5, 5, 3, 2, 1, 0]))
# 4
print(solution([0, 1, 1]))
# 1