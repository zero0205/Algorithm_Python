# 집의 수: n, 도로의 개수: m
n, m = map(int, input().split())
# 각 도로에 대한 정보 입력받기 (x와 y 사이에 길이가 z인 양방향 도로가 있음)
roads = []
total_cost = 0
for _ in range(m):
    x, y, z = map(int, input().split())
    roads.append((z, x, y))  # 길이순으로 정렬하려고
    total_cost += z
    
parent = [i for i in range(n)]
    
# 최소 비용 신장 트리 만들기 스따또-☆
# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    if parent[x] != x: # 내가 루트가 아니라면
        parent[x] = find_parent(parent, parent[x])  
    return parent[x]
        
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
# 길이가 짧은 순으로 정렬
roads.sort()

res = 0
for r in roads:
    z, x, y = r
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, x) != find_parent(parent, y):
        union_parent(parent, x, y)
        res += z
        
print(total_cost - res)

### test case ###
# 7 11
# 0 1 7
# 0 3 5
# 1 2 8
# 1 3 9
# 1 4 7
# 2 4 5
# 3 4 15
# 3 5 6
# 4 5 8
# 4 6 9
# 5 6 11