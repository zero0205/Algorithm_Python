# 크루스칼 
import heapq

INF = 1000001
v, e = map(int, input().split())
edge = []
parent = [i for i in range(v+1)]

for _ in range(e):
    a,b,c = map(int, input().split())
    heapq.heappush(edge, (c, a, b))
       
def find_parent(parent, x):
    # 루트 노드가 아니라면 루트 노드 찾을때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a == b:  # 루트 노드가 같으면 사이클 발생
        return False
    # 합치기
    if a < b:
        parent[a] = b   # 정점 번호가 더 작은 경우를 루트쪽으로
    else:
        parent[b] = a
    return True

ans = 0

while edge:
    cost, a, b = heapq.heappop(edge)
    if union_parent(parent, a, b):
        ans += cost
print(ans)