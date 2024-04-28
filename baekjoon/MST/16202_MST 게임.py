from heapq import heappop, heappush
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = []
for i in range(m):
    x, y = map(int, input().split())
    graph.append((i+1, x, y))


def find_parent(x, parent):
    if x != parent[x]:
        parent[x] = find_parent(parent[x], parent)
    return parent[x]


def union(a, b, parent):
    a = find_parent(a, parent)
    b = find_parent(b, parent)

    if a == b:
        return False

    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    return True


possible = [True]*(m+1)
answer = [0]*k
for i in range(k):
    parent = [j for j in range(n+1)]
    # Kruskal
    edges = []
    total_score = 0
    for cost, x, y in graph:
        if possible[cost] and find_parent(x, parent) != find_parent(y, parent):
            union(x, y, parent)
            heappush(edges, (cost, x, y))
            total_score += cost
            if len(edges) == n-1:
                break
    possible[edges[0][0]] = False
    if len(edges) == n-1:
        answer[i] = total_score
    else:
        break
print(*answer)
