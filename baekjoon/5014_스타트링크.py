from collections import deque

# f: 건물의 층수, s: 시작층, g: 목적층, u: 위로, d: 아래로
f, s, g, u, d = map(int, input().split())   

q = deque([(s, 0)])
visited = [False for _ in range(f + 1)]
visited[s] = True

# BFS
while q:
    now, cnt = q.popleft()
    if now == g:
        print(cnt)
        exit()
    if now + u < f + 1 and not visited[now+u]:
        q.append((now+u, cnt+1))
        visited[now+u] = True
    if now - d > 0 and not visited[now-d]:
        q.append((now-d, cnt+1))
        visited[now-d] = True
        
print("use the stairs")