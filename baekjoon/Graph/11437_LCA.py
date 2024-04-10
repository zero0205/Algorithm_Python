from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]    # 노드 간 연결
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 각 노드 레벨 구하기(BFS)
level = [-1]*(n+1)
parent = [i for i in range(n+1)]
q = deque([1])
level[1] = 0
while q:
    now = q.popleft()
    for nx in graph[now]:
        if level[nx] == -1:
            q.append(nx)
            level[nx] = level[now]+1
            parent[nx] = now


def find_lca(a, b):  # a, b의 LCA 찾기
    if level[a] < level[b]:  # a가 더 큰 레벨을 갖도록
        a, b = b, a
    # a, b 레벨 같게 맞추기
    while level[a] != level[b]:
        a = parent[a]
    # 같은 부모 찾기
    while a != b:
        a = parent[a]
        b = parent[b]
    return a


# 입력받은 두 정점의 가장 가까운 공통 조상(LCA) 출력
m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    print(find_lca(a, b))
