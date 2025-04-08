from collections import defaultdict, deque

graph = [[] for _ in range(13)]
for _ in range(12):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def bfs(start):
    dist = [12]*13
    dist[start] = 0
    q = deque([start])

    while q:
        now = q.popleft()
        for nx in graph[now]:
            if dist[nx] > dist[now]+1:
                q.append(nx)
                dist[nx] = dist[now]+1

    result = defaultdict(int)
    for i in range(1, 13):
        result[dist[i]] += 1
    return result


for i in range(1, 13):
    if len(graph[i]) == 1:
        result = bfs(i)
        if result[1] == 1 and result[3] == 3:
            print(graph[i][0])
            break
