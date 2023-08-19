############# BFS #############
# from collections import deque

# n, m = map(int, input().split())
# graph = [[] for _ in range(n+1)]
# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[b].append(a)
# x = int(input())

# visited = [False] * (n+1)
# visited[x] = True
# q = deque([x])

# ans = 0
# while q:
#     now = q.popleft()
#     for nx in graph[now]:
#         if not visited[nx]:
#             q.append(nx)
#             visited[nx] = True
#             ans += 1
# print(ans)
############################################
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)
x = int(input())
ans = 0
visited = [False] * (n+1)


def dfs(now):
    global ans

    visited[now] = True
    for nx in graph[now]:
        if not visited[nx]:
            ans += 1
            dfs(nx)


dfs(x)
print(ans)
