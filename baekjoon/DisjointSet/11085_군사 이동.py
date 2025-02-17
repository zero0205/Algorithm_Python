from heapq import heappop, heappush
import sys
input = sys.stdin.readline


p, w = map(int, input().split())
c, v = map(int, input().split())

parent = [i for i in range(p)]


def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a == b:
        return

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


roads = []
for _ in range(w):
    start, end, width = map(int, input().split())
    heappush(roads, (-width, start, end))

while roads:
    width, start, end = heappop(roads)
    union(start, end)
    if find_parent(c) == find_parent(v):
        print(-width)
        break
