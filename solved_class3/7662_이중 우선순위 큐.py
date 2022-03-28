# https://www.acmicpc.net/problem/7662

# from collections import deque
# import sys
# input = sys.stdin.readline

# t =int(input())
# for _ in range(t):
#     k = int(input())
#     q = deque()
#     for _ in range(k):
#         cmd, num = input().split()
#         num = int(num)
#         if cmd == 'D':  # 삭제 연산
#             if num == 1:  # 최댓값 삭제
#                 if q:
#                     q.pop()
#             else:   # 최솟값 삭제
#                 if q:
#                     q.popleft()
#         elif cmd == 'I':
#             q.append(num)
#             q = deque(sorted(list(q)))    
#     if q:
#         print(q.pop(), q.popleft())
#     else:
#         print("EMPTY")

#############################

import heapq
import sys
input = sys.stdin.readline

t =int(input())
for _ in range(t):
    k = int(input())
    visited = [False] * 1000000
    maxH, minH = [], []
    for i in range(k):
        cmd, num = input().split()
        num = int(num)
        if cmd == "I":  # 삽입 연산
            heapq.heappush(maxH, (-num, i))
            heapq.heappush(minH, (num, i))
            visited[i] = True
        if cmd == 'D':  # 삭제 연산
            if num == 1:
                while maxH and not visited[maxH[0][1]]: # 힙이 empty하지 않은지, 이미 삭제된 숫자인지 체크
                    heapq.heappop(maxH)
                if maxH:
                    visited[maxH[0][1]] = False
                    heapq.heappop(maxH)
            else:
                while minH and not visited[minH[0][1]]: # 힙이 empty하지 않은지, 이미 삭제된 숫자인지 체크
                    heapq.heappop(minH)
                if minH:
                    visited[minH[0][1]] = False
                    heapq.heappop(minH)
    while maxH and not visited[maxH[0][1]]:
        heapq.heappop(maxH)
    while minH and not visited[minH[0][1]]:
        heapq.heappop(minH)
    if maxH and minH:
        print(-maxH[0][0], minH[0][0])
    else:
        print("EMPTY")