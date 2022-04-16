min_dist = int(1e9)

# a, b가 현재 위치한 지점, 도로 거리 정보 graph, 이제까지 이동거리의 총합 s, 몇번 이동했는지 cnt, 이미 방문한 지점 체크 visited
def dfs(a, b, graph, s, cnt, visited):   
    global min_dist
    if s > min_dist:    # 총합이 이전에 구한 min_dist보다 크다면 더 볼 필요X
        return
    if cnt <= 0:    # 모든 지점 방문 완료
        min_dist = min(min_dist, s)
        return
    for i in range(1, len(graph)):
        for j in range(1, len(graph)):
            if not visited[i] and not visited[j]:   # i, j 둘 다 방문 예정
                visited[i] = True
                visited[j] = True
                dfs(i, j, graph, s + graph[a][i] + graph[b][j], cnt - 2, visited)
                visited[i] = False
                visited[j] = False
            elif not visited[i] and visited[j]: # i만 방문 예정
                visited[i] = True
                dfs(i, j, graph, s + graph[a][i], cnt - 1, visited)
                visited[i] = False
            elif visited[i] and not visited[j]:  # j만 방문 예정
                visited[j] = True
                dfs(i, j, graph, s + graph[b][j], cnt - 1, visited)
                visited[j] = False

def solution(N, dist, pos1, pos2):
    answer = -1
    visited = [False] * (N + 1)
    visited[pos1] = True
    visited[pos2] = True
    graph = [[0] * (N + 1) for _ in range(N + 1)]
    for d in dist:
        graph[d[0]][d[1]] = d[2]
        graph[d[1]][d[0]] = d[2]
    dfs(pos1, pos2, graph, 0, N - 2, visited)
    return min_dist