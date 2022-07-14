# intensity는 가는 경로 중 최대 비용
def find_path(start, summit, max_c, gs_intensity, graph, visited):
    global intensity, intent_summit
    
    visited[start] = True
    if start == summit: # 산봉우리까지 도착! intensity 저장
        return max_c
    for i in graph[start]:
        if i[1] >= gs_intensity:    # 이 경로에 이전에 구해진 intensity보다 비용 많이 씀
            return max_c
        if not visited[i[0]]:
            visited[i[0]] = True
            max_c = max(max_c, i[1])    # 가는 경로에 있는 비용 중 최대인 것 저장 => 산봉우리까지 가면 최종 max_c가 intensity인 것
            max_c = find_path(i[0], summit, max_c, gs_intensity, graph, visited)
            visited[i[0]] = False

def solution(n, paths, gates, summits):
    graph = [[] for _ in range(n + 1)]
    max_cost = 0
    
    for p in paths:
        i, j, w = p 
        graph[i].append([j, w])
        graph[j].append([i, w])
        max_cost = max(max_cost, w)
    max_cost += 1
    answer = [-1, max_cost]
    
    for g in gates:
        for s in summits:
            # g->s로 가는 경로만 볼 때의 intensity
            gs_intensity = find_path(g, s, 0, max_cost, graph, [False] * (n + 1))
            if gs_intensity < answer[1]:
                answer = [s, gs_intensity]
    return answer

# 테스트 케이스
# print(solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5]))
# print(solution(7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]], [1], [2, 3, 4]))
# print(solution(7, [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]], [3, 7], [1, 5]))
print(solution(5, [[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]], [1, 2], [5]))

# 정답
# [5, 3]
# [3, 4]
# [5, 1]
# [5, 6]