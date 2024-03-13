from collections import deque

n, k = map(int, input().split())
waters = list(map(int, input().split()))

q = deque()
visited = set()  # 이미 방문한 위치
for w in waters:
    visited.add(w)  # 샘터 방문 처리
    q.append((w, 0))

houses_num = 0  # 지은 집의 개수
ans = 0  # 불행도의 합
while q:
    now, dist = q.popleft()
    for nx in [now-1, now+1]:
        if nx not in visited:
            q.append((nx, dist+1))
            visited.add(nx)
            houses_num += 1
            ans += (dist+1)
        if houses_num == k:  # k개의 집 건설 완료
            break
    if houses_num == k:
        break
print(ans)
