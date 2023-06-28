import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
# 다리 정보 입력
bridge = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    bridge[a].append([b, c])
    bridge[b].append([a, c])
# 공장이 위치한 섬들
island1, island2 = map(int, input().split())

def bfs(weight):    # weight : 옮기는 물품들의 중량
    q = deque([island1])
    visited = [False] * (n+1)
    visited[island1] = True
    while q:
        now = q.popleft()
        if now == island2:
            return True
        for next, w in bridge[now]: # 다음 섬, 중량제한
            if not visited[next] and w >= weight:
                visited[next] = True
                q.append(next)
    return False

# 이분탐색
start, end = 1, int(1e9)
ans = 0
while start <= end: 
    mid = (start + end) // 2
    if bfs(mid):    # 옮기는 물건들의 중량이 mid일 때 이동이 가능한지?
        ans = mid
        start = mid + 1
    else:
        end = mid - 1
print(ans)