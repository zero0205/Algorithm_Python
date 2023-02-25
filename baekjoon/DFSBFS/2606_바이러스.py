from collections import deque

computer = int(input())
network = [[] for _ in range(computer+1)]
for _ in range(int(input())):
    a, b = map(int, input().split())
    network[a].append(b)
    network[b].append(a)

visited = [False] * (computer+1)
q = deque([1])
visited[1] = True
ans = 0
while q:
    now = q.popleft()
    for nx in network[now]:
        if not visited[nx]: # 아직 방문하지 않은 곳이라면
            ans += 1
            visited[nx] = True
            q.append(nx)

print(ans)