# https://www.acmicpc.net/problem/16953

from collections import deque

a, b = map(int, input().split())

def bfs():
    q = deque([(a, 1)])
    while q:
        now, cnt = q.popleft()
        if now == b:
            return cnt
        # 곱하기 2
        if now * 2 > b:
            pass
        else:
            q.append((now * 2, cnt + 1))
        # 1을 수의 가장 오른쪽에 추가
        if (now * 10  + 1) > b:
            continue
        else:
            q.append((now * 10 + 1, cnt + 1))
    return -1

print(bfs())           