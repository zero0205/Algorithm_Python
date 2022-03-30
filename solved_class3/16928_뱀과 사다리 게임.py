# https://www.acmicpc.net/problem/16928

# n, m = map(int, input().split())
# map_data = [i for i in range(101)]
# dp = [101] * 101
# # 사다리 정보 입력
# for _ in range(n):
#     # x번 칸에 도착하면 y번 칸으로 이동 (x < y)
#     x, y = map(int, input().split())
#     map_data[x] = y
# # 뱀의 정보 입력
# for _ in  range(m):
#     # u번 칸에 도착하면 v번 칸으로 이동 (u > v)
#     u, v = map(int, input().split())
#     map_data[u] = v

# # 초기값 세팅    
# for i in range(2, 8):
#     dp[i] = 1
#     # 사다리 타고 올라갈 수 있는 경우
#     if map_data[i] > i:
#         dp[map_data[i]] = 1
# # DP    
# for j in range(8, 101):
#     dp[j] = min(min(dp[j-6 : j]) + 1, dp[j])
#     # 사다리 타고 올라가는 경우
#     if map_data[j] > j:
#         dp[map_data[j]] = dp[j]
#     # 뱀 타고 내려가는 경우
#     elif map_data[j] < j:
#         dp[map_data[j]] = min(dp[map_data[j]], dp[j])
        
# print(dp[100])

###############################3
# BFS
from collections import deque
INF = int(1e9)

n, m = map(int, input().split())
map_data = [i for i in range(101)]
# 사다리 정보 입력
for _ in range(n):
    # x번 칸에 도착하면 y번 칸으로 이동 (x < y)
    x, y = map(int, input().split())
    map_data[x] = y
# 뱀의 정보 입력
for _ in  range(m):
    # u번 칸에 도착하면 v번 칸으로 이동 (u > v)
    u, v = map(int, input().split())
    map_data[u] = v
    
q = deque([1])
dist = [INF] * 101
dist[1] = 0

while q:
    now = q.pop()
    if now == 100:
        print(dist[100])
        break
    for i in range(1, 7):
        if dist + i > 100:
            continue
        if dist[now + i] == INF:
            dist[now + i] = dist[now] + 1
            q.append(now + i)
            if map_data[now + i] > now + i:
                dist[map_data[now + i]] = dist[now + i]
                q.append(map_data[now + i])
            