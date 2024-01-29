import sys
input = sys.stdin.readline


def dfs(now, cnt):
    visited[now] = True

    for next in edges[now]:
        if not visited[next]:
            cnt = dfs(next, cnt+1)
    return cnt


for _ in range(int(input())):
    n, m = map(int, input().split())
    edges = [[] for _ in range(n+1)]

    for _ in range(m):
        a, b = map(int, input().split())
        edges[a].append(b)
        edges[b].append(a)

    visited = [False] * (n+1)
    print(dfs(1, 0))
