# https://www.acmicpc.net/problem/1697

from collections import deque

INF = int(1e9)

n, k = map(int, input().split())

arr = [INF] * 100001
arr[n] = 0
q = deque([n])

while True:
    now = q.popleft()
    if now == k:
        break
    for next in [now -1, now + 1, now *2]:
        # 범위를 벗어날 경우
        if next < 0 or next > 100000:
            continue
        if arr[next] == INF:    # 아직 방문한적 없음
            arr[next] = arr[now] + 1
            q.append(next)
print(arr[k])