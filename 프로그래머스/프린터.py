def solution(priorities, location):
    answer = 0

    while True:
        max_doc = max(priorities)
        for i in range(len(priorities)):
            if max_doc == priorities[i]:
                answer += 1
                priorities[i] = 0
                max_doc = max(priorities)
                if i == location:
                    return answer

print(solution([2, 1, 3, 2], 2))
# 1
print(solution([1, 1, 9, 1, 1, 1], 0))
# 5