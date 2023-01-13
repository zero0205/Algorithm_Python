# https://programmers.co.kr/learn/courses/30/lessons/81302

from collections import deque

def bfs(r, c, place):
    q = deque([(r, c, 0)])
    visited = [[False] * 5 for _ in range(5)]
    visited[r][c] = True
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while q:
        x, y, d = q.popleft()
        if d >= 2:   # 이 응시자로부터는 맨해튼 거리 2 내에 사람 없음
            return True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 5 and 0 <= ny < 5: # 범위 내에 있는지 체크
                if place[nx][ny] == 'P' and not visited[nx][ny]:    # 맨해튼 거리 내에 사람 있음
                    return False
                elif place[nx][ny] == 'O' and not visited[nx][ny]:  # 빈 테이블이고 아직 방문 안 한 칸
                    q.append((nx, ny, d + 1))
                    visited[nx][ny] = True
                else:   # 파티션인 경우
                    visited[nx][ny] = True  # 큐에 넣지는 않지만 다시 방문은 안 하도록
    return True

def solution(places):
    answer = []
    for place in places:
        distancing = True
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    distancing = bfs(i, j, place) & distancing
        if distancing:
            answer.append(1)
        else:
            answer.append(0)
    return answer

# 테스트 케이스
print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], 
                ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], 
                ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], 
                ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
                ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))