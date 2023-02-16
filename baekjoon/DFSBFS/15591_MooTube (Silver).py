from collections import deque
import sys

INF = int(1e9)

N, Q = map(int, sys.stdin.readline().split())

map_data = [[] for _ in range(N+1)]
for _ in range(N-1):
    p, q, r = map(int, sys.stdin.readline().split())
    map_data[p].append((q,r))
    map_data[q].append((p,r))
    
# BFS
def bfs(v, k):
    result = 0
    visited = [False] * (N+1)
    visited[v] = True   # 시작노드 방문처리
    q = deque([v]) # 노드번호
    while q:
        node= q.popleft()
        for nn, nd in map_data[node]:
            # USADO가 k보다 작아진다면 더이상 탐색할 필요 X
            # 이미 방문한 노드도 탐색할 필요 X
            if nd < k or visited[nn]:
                continue
            q.append(nn)
            visited[nn] = True
            result += 1
    return result

for _ in range(Q):
    k, v = map(int, sys.stdin.readline().split())
    print(bfs(v,k))