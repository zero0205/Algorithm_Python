####### Prim Algorithm #######
# import sys
# input = sys.stdin.readline

# INF = int(1e9)

# n = int(input())
# star = []
# for _ in range(n):
#     x, y = map(float, input().split())
#     star.append((x, y))
    
# def get_dist(a, b):
#     return ((a[0] - b[0])**2 + (a[1] - b[1]) ** 2) ** (1/2)

# distance = [[INF for _ in range(n)] for _ in range(n)]
# for i in range(n):
#     for j in range(n):
#         distance[i][j] = get_dist(star[i],star[j])

# selected = set([0]) # MST에 포함된 별
# unselected = set([i for i in range(1, n)])
# ans = 0

# while len(selected) != n:
#     min_dist = 2000
#     tmp = -1
#     for i in selected:
#         for j in unselected:
#             if distance[i][j] < min_dist:
#                 tmp = j
#                 min_dist = distance[i][j]
#     selected.add(tmp)
#     unselected.remove(tmp)
#     ans += min_dist
# print(round(ans, 2))

####### Kruskal Algorithm #######
import heapq
from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())
star = []
for _ in range(n):
    x, y = map(float, input().split())
    star.append((x, y))

parent = [i for i in range(n)]
def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def get_dist(a, b):
    return ((a[0] - b[0])**2 + (a[1] - b[1]) ** 2) ** (1/2)

distance = []
for a, b in combinations(range(n), 2):
    heapq.heappush(distance, (get_dist(star[a], star[b]), a, b))

num = 0
ans = 0    
while num != n - 1:
    dist, a, b = heapq.heappop(distance)
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        num += 1
        ans += dist
        
print(round(ans, 2))