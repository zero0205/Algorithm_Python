from collections import deque

def solution(receive, sell):
    answer = []
    n = len(receive)

    # bfs
    q = deque([(0, 0, [])]) # 날짜, 총구매량, 방문 매장리스트
    while q:
        date, num, visited = q.popleft()
        for i in range(n):
            pass
    return answer