from collections import deque

n, k = map(int, input().split())

q = deque([(n, 0)])
visited = [[i, int(1e9)] for i in range(100_001)]
visited[n] = [-1, 0]   # 처음 수빈이 위치
while True:
    now, sec = q.popleft()
    if now == k:
        path = deque([k])
        for i in range(sec):
            path.appendleft(visited[now][0])
            now = visited[now][0]
        print(sec)
        print(*path)
        break
    for nx in [2*now, now-1, now+1]:
        if 0 <= nx <= 100_000 and visited[nx][1] > visited[now][1]+1:
            q.append((nx, sec+1))
            visited[nx] = [now, visited[now][1]+1]
