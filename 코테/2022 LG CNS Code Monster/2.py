def solution(k, limits, sockets):
    answer = 0
    n = len(limits) # 멀티탭 개수
    graph = [[] for _ in range(n)]
    # 그래프 구성
    for i in range(n):
        for j in range(5):
            if sockets[i][j] >= 2:
                graph[i].append(sockets[i][j])

    return answer