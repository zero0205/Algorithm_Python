from collections import deque
import sys
input = sys.stdin.readline

n, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
trunk = -1
longest_branch = 0
for _ in range(n-1):
    a, b, d = map(int, input().split())
    graph[a].append((b, d))
    graph[b].append((a, d))
q = deque([(r, 0)])
visited = [False] * (n+1)
visited[r] = True

# 기둥 길이 구하기
while q:
    now, dist = q.popleft()
    cnt = 0
    for nx, d in graph[now]:
        if not visited[nx]:
            q.append((nx, dist+d))
            visited[nx] = True
            cnt += 1
    if cnt >= 2 and trunk == -1:    # 기가 노드
        trunk = dist
    if cnt == 0:  # 리프 노드
        if trunk == -1:  # 리프 노드 == 기가 노드인 경우
            trunk = dist
        else:
            longest_branch = max(longest_branch, dist-trunk)

print(trunk, longest_branch)
