from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    parent = [-1]*(n+1)
    children = [[] for _ in range(n+1)]
    for _ in range(n-1):
        a, b = map(int, input().split())
        parent[b] = a
        children[a].append(b)
    x, y = map(int, input().split())

    # 루트 노드 찾기
    root_node = -1
    for i in range(1, n+1):
        if parent[i] == -1:
            root_node = i
            break

    # 각 노드의 depth 구하기
    q = deque([(root_node, 0)])
    depth = [0] * (n+1)
    while q:
        now, d = q.popleft()
        for nx in children[now]:
            q.append((nx, d+1))
            depth[nx] = d+1

    # 최소 공통 조상 (LCA)
    if depth[x] > depth[y]:
        x, y = y, x
    while depth[x] < depth[y]:  # x, y 깊이 같게 맞춰주기
        y = parent[y]
    for i in range(n):
        if x == y:
            print(x)
            break
        x = parent[x]
        y = parent[y]
