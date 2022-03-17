# https://www.acmicpc.net/problem/1931

# import sys
# input = sys.stdin.readline

# n = int(input())
# time = []
# max_value = -1
# for _ in range(n):
#     start, end = map(int, input().split())
#     time.append((start, end))
#     max_value = max(max_value, end)

# dp = [0] * (max_value + 1)

# for t in time:
#     a, b = t
#     for i in range(a + 1):
#         dp[b] = max(dp[i] + 1, dp[b])

# print(dp[max_value])

# 시간 초과

#############################
# import heapq
# import sys
# input = sys.stdin.readline

# n = int(input())
# time = []

# for _ in range(n):
#     start, end = map(int, input().split())
#     time.append((start, end))
# q = [(-1, 4)]   # 1번째 원소 최소힙에 넣어줌
# find = False
# for i in range(1, len(time)):
#     start, end = time[i]
#     for j in q:
#         if j[1] <= start:   # 끝나는 시간이 현재 회의 시간 시작 시간과 같거나 이전이라면
#             heapq.heappush(q, (j[0] - 1, end))
#             find = True
#             break
#     if find:
#         continue
#     else:
#         heapq.heappush(q, (-1, end))
    
# ans = heapq.heappop(q)
# print(ans[0] * (-1))

# 시간 초과

###################################
import sys
input = sys.stdin.readline

n = int(input())
time = []

for _ in range(n):
    start, end = map(int, input().split())
    time.append((start, end))
    
time.sort(key=lambda x : (x[1], x[0]))

prev_e, res = 0, 0
for t in time:
    if prev_e <= t[0]:
        res += 1
        prev_e = t[1]
print(res)