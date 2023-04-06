from heapq import heappop, heappush

v, e = map(int, input().split())

parent = [i for i in range(v+1)]
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    
    if a == b:
        return
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
edges = []
for _ in range(e):
    a, b, c = map(int, input().split())
    heappush(edges, (c, a, b))

total_cost, cnt = 0, 1  
while edges:
    c, a, b = heappop(edges)
    if find(a) != find(b):  # 사이클 형성하는지 체크
        union(a,b)
        total_cost += c
        cnt += 1
    if cnt == v:  # 모든 정점을 포함하는 MST 완성
        break
print(total_cost)