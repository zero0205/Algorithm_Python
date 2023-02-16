from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

INF = int(1e6)

def bfs(x, y):
    visited = [False for _ in range(n)]
    q = deque([(x, y)])
    
    while q:
        x, y = q.popleft()
        if abs(x-rx) + abs(y-ry) <= 1000:   # 락페 도착
            print("happy")
            return
        for i in range(len(cs)):
            if abs(x-cs[i][0]) + abs(y-cs[i][1]) <= 1000 and not visited[i]:
                q.append((cs[i][0], cs[i][1]))
                visited[i] = True
    print("sad")
    return 

for _ in range(int(input())):
    n = int(input())    # 편의점 개수
    # 상근이네 집
    x, y = map(int, input().split())
    hx, hy = x + 32768, y + 32768
    # 편의점
    cs = []
    for _ in range(n):
        x, y = map(int, input().split())
        cs.append((x + 32768, y + 32768))
    # 락페
    x, y = map(int, input().split())
    rx, ry = x + 32768, y + 32768
    
    bfs(hx, hy)