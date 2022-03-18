# https://www.acmicpc.net/problem/11279

import heapq, sys

n = int(input())

q = []
for _ in range(n):
    num = int(sys.stdin.readline())
    if num == 0:
        if len(q) == 0:
            print(0)
        else:
            print(heapq.heappop(q) * (-1))
    else:
        heapq.heappush(q, num * (-1))