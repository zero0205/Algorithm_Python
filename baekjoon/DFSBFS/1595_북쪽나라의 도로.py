import sys
input = sys.stdin.readline

MAX_NODE = 10_001

graph = [[] for _ in range(MAX_NODE)]
while True:
    try:
        a, b, dist = map(int, input().split())
        graph[a].append((b, dist))
        graph[b].append((a, dist))
    except:
        break


def dfs(start):
    visited = [False] * MAX_NODE
    visited[start] = True

    stack = [(start, 0)]
    farthest_node = start
    farthest_dist = 0

    while stack:
        now, now_dist = stack.pop()

        if now_dist > farthest_dist:
            farthest_dist = now_dist
            farthest_node = now

        for nx, nx_dist in graph[now]:
            if not visited[nx]:
                visited[nx] = True
                stack.append((nx, now_dist + nx_dist))

    return farthest_node, farthest_dist


start = 1
for i in range(1, 10_001):
    if graph[i]:
        start = i
        break

farthest_node, _ = dfs(start)
_, farthest_dist = dfs(farthest_node)

print(farthest_dist)
