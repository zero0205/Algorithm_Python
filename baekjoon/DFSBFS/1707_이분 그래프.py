from collections import deque
import sys
input = sys.stdin.readline


def bfs(edges, start, colors):
    q = deque([start])
    colors[start] = 1
    while q:
        now = q.popleft()
        for nx in edges[now]:
            if colors[nx] == 0:
                colors[nx] = colors[now] % 2+1
                q.append(nx)
            elif colors[nx] == colors[now]:
                return False
    return True


for _ in range(int(input())):
    answer = True
    v, e = map(int, input().split())
    edges = [[] for _ in range(v+1)]
    for _ in range(e):
        a, b = map(int, input().split())
        edges[a].append(b)
        edges[b].append(a)

    colors = [0]*(v+1)
    for i in range(1, v+1):
        if colors[i] != 0:
            continue
        result = bfs(edges, i, colors)
        if result == False:
            answer = False
            break
    print("YES" if answer else "NO")
