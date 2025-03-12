from heapq import heappop, heappush
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
power_stations = set(map(int, input().split()))
parent = [i for i in range(n+1)]


def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a == b:
        return False

    if a in power_stations:
        parent[b] = a
    elif b in power_stations:
        parent[a] = b
    else:
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
    return True


cables = []
for _ in range(m):
    u, v, w = map(int, input().split())
    heappush(cables, (w, u, v))

answer = 0
while cables:
    cost, u, v = heappop(cables)
    if find_parent(u) in power_stations and find_parent(v) in power_stations:
        continue

    if union(u, v):
        answer += cost

    is_all_connected = True
    for i in range(1, n+1):
        if find_parent(i) not in power_stations:
            is_all_connected = False
            break
    if is_all_connected:
        break

print(answer)
