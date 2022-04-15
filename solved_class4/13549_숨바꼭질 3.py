# https://www.acmicpc.net/problem/13549

from collections import deque

n, k = map(int, input().split())

# (수빈이의 위치, 현재 시간) 덱에 저장
q = deque([(n, 0)])
visited = [False] * 100001
visited[n] = True   # 현재 수빈이 위치 방문 처리

while q:
    now, cnt = q.popleft()
    if now == k:
        print(cnt)
        break
    if 0 <= now * 2 <= 100000 and not visited[now * 2]:
        q.append((now * 2, cnt))
        visited[now * 2] = True
    for i in [now - 1, now + 1]:
        if 0 <= i <= 100000 and not visited[i]:
            q.append((i, cnt + 1))
            visited[i] = True