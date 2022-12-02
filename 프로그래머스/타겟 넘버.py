from collections import deque

def solution(numbers, target):
    answer = 0
    q = deque([(0, -1)])
    
    while q:
        now, idx = q.popleft()
        if idx + 1 == len(numbers):
            if now == target:
                answer += 1
            continue
        for i in [numbers[idx+1], numbers[idx+1]*(-1)]:
            q.append((now+i, idx+1))
    return answer

######### 재귀 이용 풀이 ###########
def solution2(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])

# print(solution([1, 1, 1, 1, 1], 3))
# 5
# print(solution([4, 1, 2, 1], 4))
# 2

print(solution2([1, 1, 1, 1, 1], 3))
print(solution2([4, 1, 2, 1], 4))