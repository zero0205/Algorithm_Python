# https://www.acmicpc.net/problem/2887
# # 크루스칼 알고리즘

# import sys

# input = sys.stdin.readline

# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]

# def union_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
    
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b

# # n : 행성 개수
# n = int(input())
# # 각 행성의 x, y, z 좌표 입력받기
# planet = []
# for _ in range(n):
#     planet.append(list(map(int, input().split())))
    
# # parent 배열 생성 & 초기화 (0 ~ n-1번째 행성)
# parent = [i for i in range(n)]

# # 모든 행성 간의 거리 구하기
# for el in planet:
#     min_value = int(1e9)
#     x1, y1, z1 = el
#     for el2 in planet:
#         x2, y2, z2 = el2
#         min_value = min(min_value, min(abs(x1-x2), abs(y1-y2), abs(z1-z2)))

           
##### 답지 #####
# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면 루트 노드를 찾을 떄까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기 
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수 입력받기
n = int(input())
parent = [i for i in range(n + 1)]  # 부모 테이블을 자기 자신으로 초기화

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

x = []
y = []
z = []

# 모든 노드에 대한 좌표 값 입력받기
for i in range(1, n + 1):
    data = list(map(int, input().split()))
    x.append((data[0], i))
    y.append((data[1], i))
    z.append((data[2], i))
    
x.sort()
y.sort()
z.sort()

# 인접합 노드들로부터 간선 정보를 추출하여 처리
for i in range(n - 1):
    # 비용 순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((x[i + 1][0] - x[i][0], x[i][1], x[i + 1][1]))
    edges.append((y[i + 1][0] - y[i][0], y[i][1], y[i + 1][1]))
    edges.append((z[i + 1][0] - z[i][0], z[i][1], z[i + 1][1]))
    
# 간선을 비용 순으로 정렬
edges.sort()

# 간선을 하나씩 확인하며
for edge in edges:
    cost,a,b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += cost

print(result)