############## 효율성 0점 ###################
# from collections import deque

# def solution(A, B):
#     answer = 0
#     B = deque(sorted(B))
#     for idx in range(len(A)):
#         tmp = deque([])
#         now = B.popleft()
#         while True:
#             if now > A[idx]:
#                 B = tmp + B
#                 answer += 1
#                 break
#             else:
#                 tmp.append(now)
#                 if not B:
#                     tmp.popleft()
#                     B = tmp + B
#                     break
#                 else:
#                     now = B.popleft()
#     return answer

################ 정확성, 효율성 모두 틀린 코드(이분탐색) #########################
# def bin_search(x, arr, used):
#     start, end = 0, len(arr) - 1 
#     find_idx = -1
#     while start <= end:
#         mid = (start + end) // 2
#         if arr[mid] == x:   # 동점 => 점수 못 얻음 => 이전에 저장된 arr[find_idx]가 이길 수 있는 최소값
#             break
#         elif arr[mid] > x:
#             find_idx = mid
#             end = mid - 1
#         else:
#             start = mid + 1            
            
#     while used[find_idx]:
#         find_idx += 1
#         if find_idx == len(arr):    # 이 위로는 이미 다 쓴 것들이어서 쓸 수 없음 => 제일 작은 놈 소모하고 이번 판은 진다
#             find_idx = 0
#     used[find_idx] = True
#     return arr[find_idx]

# def solution(A, B):
#     answer = 0
#     B = sorted(B)
#     used = [False for _ in range(len(B))]
    
#     for el in A:
#         now = bin_search(el, B, used)
#         if now > el:
#             answer += 1
#     return answer

###############################################################
import heapq

def solution(A, B):
    answer = 0
    
    heapq.heapify(A)    
    heapq.heapify(B)    
    
    a = heapq.heappop(A)
    b = heapq.heappop(B)
    
    while True:
        if a >= b:  # B팀이 이길 수 없다면 이번에 나온 숫자는 버림
            if B:
                b = heapq.heappop(B)
            else:
                break
        else:
            answer += 1
            if not A:
                answer += len(B)
            if not B:
                break
            a = heapq.heappop(A)
            b = heapq.heappop(B)
                
    return answer

print(solution([5,1,3,7], [2,2,6,8]))
print(solution([2,2,2,2], [1,1,1,1]))