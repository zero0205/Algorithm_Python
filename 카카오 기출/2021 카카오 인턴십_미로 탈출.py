# https://programmers.co.kr/learn/courses/30/lessons/81304

# 내 풀이 -> 실패
from collections import deque

# 함정 도달했을때 화살표 방향 뒤집어 주는 함수
def you_are_in_trap(graph, trap):
    for i in graph[trap]:
        i[1] *= (-1)
        for j in graph[i[0]]:
            if j[0] == trap:
                j[1] *= (-1)
    return graph
    
def solution(n, start, end, roads, traps):
    answer = 0
    # i번째 방에서 갈 수 있는 방의 번호와 그 때의 비용 저장 리스트
    # 비용이 음수이면 나에게로 들어오는 길인것
    graph = [[] for _ in range(n + 1)]  
    for p, q, s in roads:
        graph[p].append([q, s]) 
        graph[q].append([p, -s])
    
    q = deque([[start, 0]])
    while q:
        now, c = q.popleft()
        if now == end:
            answer = c
            break
        if now in traps:
            graph = you_are_in_trap(graph, now)
        for nn, nc in graph[now]:
            if nc < 0:  # 비용이 음수인건 나에게로 들어오는 길
                continue
            else:
                q.append([nn, c + nc])
    return answer

# 테스트 케이스
print(solution(3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2]))
print(solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3]))