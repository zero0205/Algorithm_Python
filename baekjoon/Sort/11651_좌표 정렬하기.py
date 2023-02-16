# https://www.acmicpc.net/problem/11651

import heapq

n = int(input())
q = []
for _ in range(n):
    x, y = map(int, input().split())
    heapq.heappush(q, (y, x))
    
while q:
    b, a = heapq.heappop(q)
    print(a, b)