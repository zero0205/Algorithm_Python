import sys
import heapq
input = sys.stdin.readline

for _ in range(int(input())):
    q = []
    n, m = map(int, input().split())
    remain = [True] * (n+1)
    for _ in range(m):
        a, b = map(int, input().split())
        heapq.heappush(q, (b, a))
    cnt = 0
    while q:
        b, a = heapq.heappop(q)
        for i in range(a, b+1):
            if remain[i]:
                remain[i] = False   # 책 나눠줌
                cnt += 1
                break
    print(cnt)
