# from collections import deque
# import sys
# input = sys.stdin.readline

# def bfs(start):
#     res = items[start - 1]
#     q = deque([(start, 0)])
#     visited = [False] * (n+1)
#     visited[start] = True
    
#     while q:
#         now, dist = q.popleft()
#         for next, length in road[now]:
#             if visited[next] or length + dist > m:   # 이미 방문했거나 수색 범위를 벗어남
#                 continue
#             else:
#                 res += items[next-1]    
#                 q.append((next, dist + length))   
#                 visited[next] = True
#     return res           

# # n : 지역의 개수, m : 예은이의 수색범위, r : 길의 개수
# n, m, r = map(int, input().split())
# # 각 구역의 아이템의 수
# items = list(map(int, input().split()))
# road = [[] for _ in range(n + 1)]
# for _ in range(r):
#     a, b, l = map(int, input().split())
#     road[a].append((b, l))
#     road[b].append((a, l))

# answer = 0
# for i in range(1, n + 1):
#     answer = max(answer, bfs(i))
    
# print(answer)

########################
# 플로이드 워셜
import sys
input = sys.stdin.readline

INF = int(1e9)

# n : 지역의 개수, m : 예은이의 수색범위, r : 길의 개수
n, m, r = map(int, input().split())
# 각 구역의 아이템의 수
items = list(map(int, input().split()))

road = [[INF for _ in range(n+1)] for _ in range(n+1)]
# 자기 자신으로 가는 거리는 0으로 초기화
for i in range(1, n+1):
    road[i][i] = 0
    
for _ in range(r):
    a, b, l = map(int, input().split())
    road[a][b] = l
    road[b][a] = l
# 플로이드 워셜
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            road[i][j] = min(road[i][j], road[i][k] + road[k][j])
            
answer = 0
for i in range(1, n+1):
    sum = 0
    for j in range(1, n+1):
        if road[i][j] <= m: # 탐색 가능한 범위라면
            sum += items[j-1]
    answer = max(answer, sum)
    
print(answer)