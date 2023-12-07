from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    k, m, p = map(int, input().split())
    edges = [[] for _ in range(m+1)]    # a->b 간선
    indegree = [0] * (m+1)  # 진입차수
    strahler = [[] for _ in range(m+1)]   # 들어오는 강 순서, 2개 이상인지?
    for _ in range(p):
        a, b = map(int, input().split())
        edges[a].append(b)  # a->b
        indegree[b] += 1
    q = deque()
    # 초기에 진입차수가 0인 노드들 q에 넣기
    for i in range(1, m+1):
        if indegree[i] == 0:
            q.append(i)    # 노드 번호
            strahler[i] = [1, 0]
    # 위상 정렬
    while q:
        node = q.popleft()
        order = strahler[node][0] + strahler[node][1]
        for nx in edges[node]:
            indegree[nx] -= 1
            # Strahler
            if not strahler[nx] or strahler[nx][0] < order:
                strahler[nx] = [order, 0]
            elif strahler[nx][0] == order:
                strahler[nx][1] = 1
            # 진입차수가 0이 된 노드
            if indegree[nx] == 0:
                q.append(nx)
    print(k, sum(strahler[m]))
