from collections import deque 

v = int(input())    # 트리의 정점의 개수
# 트리 정보 입력
tree = [[] for _ in range(v + 1)]
for _ in range(v):
    info = list(map(int, input().split()))
    for i in range(1, len(info)-1, 2):
        tree[info[0]].append((info[i], info[i+1]))
        
# 풀이 방법 
# 1. 어떤 정점 x에서 가장 먼 정점 y를 찾는다
# 2. y에서 가장 먼 정점 z를 찾는다

def bfs(graph, start):
    max_vertex = 0
    max_dist = 0
    q = deque([(start, 0)])
    
    visited = [False] * (len(graph))
    visited[start] = True   # 시작 정점 방문 처리
    
    while q:
        now_v, now_c = q.popleft()
        for nx_v, nx_c in graph[now_v]:
            if not visited[nx_v]:
                q.append((nx_v, now_c + nx_c))
                visited[nx_v] = True
                if max_dist < now_c + nx_c:
                    max_dist = now_c + nx_c
                    max_vertex = nx_v
                    
    return [max_vertex, max_dist]

y, y_dist = bfs(tree, 1)
z, z_dist = bfs(tree, y)
print(z_dist)