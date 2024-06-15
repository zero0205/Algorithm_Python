from collections import deque

for _ in range(10):
    tc, n = map(int, input().split())
    arr = list(map(int, input().split()))
    graph = [[] for _ in range(100)]
    for i in range(0, len(arr)-1, 2):
        graph[arr[i]].append(arr[i+1])

    q = deque([0])
    visited = [False]*100
    visited[0] = True
    possible = 0
    while q:
        now = q.popleft()
        if now == 99:
            possible = 1
            break
        for nx in graph[now]:
            if not visited[nx]:
                q.append(nx)
                visited[nx] = True
    print(f"#{tc} {possible}")
