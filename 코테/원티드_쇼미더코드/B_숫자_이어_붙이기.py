from collections import deque
import sys
input = sys.stdin.readline

INF = int(1e9)
                
n, q = map(int, input().split())
arr = list(input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def bfs(start, end):
    q = deque([start])    
    visited = [False] * (n + 1)
    visited[start] = True
    ans = arr[start - 1]
    while q:
        now = q.popleft()
        if now == end:
            return int(ans)
        for node in graph[now]:
            if not visited[node]:
                q.append(node)   
                ans += arr[node - 1]
                visited[node] = True
                
for _ in range(q):
    x, y = map(int, input().split())
    print(bfs(x,y) % (INF + 7))