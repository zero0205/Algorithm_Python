from collections import deque

def solution(edges, roots):
    answer = []
    now_root = 1
    n = len(edges) + 1
    graph = [[] for _ in range(n+1)]
    connected = [[False for _ in range(n+1)] for _ in range(n+1)]
    changed = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for a, b in edges:  # a가 부모, b가 자식
        graph[a].append(b)
        connected[a][b] = True
        connected[b][a] = True

    for r in roots:
        q = deque([r])
        visited = [False for _ in range(n+1)]
        visited[r] = True

        while q:
            now = q.popleft()
            for i in range(1, n+1):
                if not visited[i] and connected[now][i] :
                    q.append(i)
                    visited[i] = True
                    if now in graph[i]:   # 부모자식 역전
                        graph[i].remove(now)
                        graph[now].append(i)
                        changed[now][i] += 1
                        changed[i][now] += 1
    for a,b in edges:
        answer.append(changed[a][b])
    return answer

print(solution([[1,3],[1,2],[2,4],[2,5]],[2,3]))
# [1,2,0,0]
print(solution([[1,2],[1,3],[2,4]],[3,4,1,2]))
# [3, 2, 2]