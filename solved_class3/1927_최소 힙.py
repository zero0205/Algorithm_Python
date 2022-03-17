# https://www.acmicpc.net/problem/1927

import heapq
import sys
input = sys.stdin.readline

n = int(input())

q = []

for _ in range(n):
    num = int(input())
    if num == 0:    # 배열에서 가장 작은 값 pop
        if len(q) == 0:
            print(0)
        else:
            print(heapq.heappop(q))
    else:
        heapq.heappush(q, num)
        
#######################################
