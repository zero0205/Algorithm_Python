# https://www.acmicpc.net/problem/1916

import sys, heapq
input = sys.stdin.readline

INF = int(1e9)
n = int(input())
m = int(input())
bus = [[] for _ in range(n + 1)]
cost = [INF] * (n + 1)
for _ in range(m):
    a, b, c = map(int, input().split())
    bus[a].append((b,c))
    
def dijkstra(start, end):
    q = []
    heapq.heappush(q, (0, start))   # 자기 자신으로 가는 비용은 0으로 처리
    cost[start] = 0
    while q:
        c, now = heapq.heappop(q)
        if now == end:
            print(c)
            return
        if cost[now] < c: # 이미 처리된 적 있는 노드
            continue
        for dest, d_cost in bus[now]:
            d_cost += c
            if d_cost < cost[dest]:
                heapq.heappush(q, (d_cost, dest))
                cost[dest] = d_cost
                
start, end = map(int, input().split())
dijkstra(start, end)