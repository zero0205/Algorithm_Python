# from collections import deque, defaultdict
# from copy import deepcopy

# def op(q1, q2):
#     newq1 = deepcopy(q1)
#     newq2 = deepcopy(q2)  
#     if newq1:
#         tmp = newq1[0]
#         newq2.append(tmp)    
#         return [newq1[1:], newq2]
#     else:
#         return q1, q2

# def solution(q1, q2):
#     answer = -1

#     dq = deque([[q1, q2, 0]])
#     visited = defaultdict(list)
#     visited[len(q1)].extend([q1, q2])
#     while dq:
#         que1, que2, cnt = dq.popleft()
#         if sum(que1) == sum(que2):
#             answer = cnt
#             break
#         # q1 -> q2
#         nque1, nque2 = op(que1, que2)
#         if [nque1, nque2] not in visited[len(nque1)]:
#             dq.append([nque1, nque2, cnt + 1])
#             visited[len(nque1)].append([nque1, nque2])
#         # q2 -> q1
#         nque2, nque1 = op(que2, que1)
#         if [nque1, nque2] not in visited[len(nque1)]:
#             dq.append([nque1, nque2, cnt + 1])
#             visited[len(nque1)].append([nque1, nque2])
#     return answer

#######################################
# from collections import deque, defaultdict
# from copy import deepcopy

# def op(q1, q2):
#     newq1 = deepcopy(q1)
#     newq2 = deepcopy(q2)  
#     if newq1:
#         tmp = newq1[0]
#         newq2.append(tmp)    
#         return [newq1[1:], newq2]
#     else:
#         return q1, q2

# def solution(q1, q2):
#     answer = -1

#     dq = deque([[q1, q2, sum(q1), sum(q2), 0]])
#     visited = defaultdict(list)
#     visited[len(q1)].extend([q1, q2])
#     while dq:
#         que1, que2, q1sum, q2sum, cnt = dq.popleft()
#         if q1sum == q2sum:
#             answer = cnt
#             break
#         # q1 -> q2
#         nque1, nque2 = op(que1, que2)
#         if [nque1, nque2] not in visited[len(nque1)]:
#             dq.append([nque1, nque2, q1sum - que1[0], q2sum + que1[0], cnt + 1])
#             visited[len(nque1)].append([nque1, nque2])
#         # q2 -> q1
#         nque2, nque1 = op(que2, que1)
#         if [nque1, nque2] not in visited[len(nque1)]:
#             dq.append([nque1, nque2, q1sum + que2[0], q2sum - que2[0], cnt + 1])
#             visited[len(nque1)].append([nque1, nque2])
#     return answer

###############################################
def solution(queue1, queue2):
    answer = int(1e6)
    q = queue1 + queue2 + queue1
    n = len(queue1)
    now_sum = sum(queue1)
    half = (now_sum + sum(queue2)) // 2
    start = 0
    end = n - 1
    while start < 3 * n and end < 3 * n:
        if end - start > 2 * n:
            start += 1
            continue
        if now_sum == half:   # 절반이 되는 지점 찾음
            answer = min(answer, end - (n-1) + start)
            start += 1
            continue
        if now_sum > half:
            now_sum -= q[start]
            start += 1
        else:
            end += 1   
            if end < 3 * n:    
                now_sum += q[end]
    if answer == int(1e6):
        return -1
    else:
        return answer

# 테스트 케이스
print(solution([3, 2, 7, 2], [4, 6, 5, 1]))
print(solution([1, 2, 1, 2], [1, 10, 1, 2]))
print(solution([1, 1], [1, 5]))

# 정답
# 2
# 7
# -1