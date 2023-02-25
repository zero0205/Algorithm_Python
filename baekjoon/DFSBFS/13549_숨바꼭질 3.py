# import sys
# sys.setrecursionlimit(10**6)

# n, k = map(int, input().split())
# visited = [False] * 100_001

# def dfs(pos, sec):
#     print(pos, sec)
#     if pos < 0 or pos > 100000:    # 범위 벗어남
#         return
#     if visited[pos]:    # 이미 방문 -> 더 빨리 가는 방법 있음
#         return
#     if pos == k:    # 동생 찾음
#         print(sec)
#         exit()
#     visited[pos] = True
#     dfs(2 * pos, sec)
#     dfs(pos + 1, sec + 1)
#     dfs(pos-1, sec + 1)
    
# dfs(n, 0)
#################################
from collections import deque

n, k = map(int, input().split())

q = deque([[n, 0]])
visited = [False] * 100_001
visited[n] = True
while q:
    now, cnt = q.popleft()
    if now == k:
        print(cnt)
        break
    if 0 <= now * 2 <= 100_000 and not visited[now * 2]:
        q.appendleft([now * 2, cnt])
        visited[now * 2] = True
    for i in [now - 1, now + 1]:
        if 0 <= i <= 100_000 and not visited[i]:
            q.append([i, cnt + 1])
            visited[i] = True