# 서로소 집합 알고리즘 문제
# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
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
        
# 여행지의 수: n, 여행 계획에 속한 도시의 수: m
n, m = map(int, input().split())
# 여행지들의 연결 여부를 나타내는 2차원 배열 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

# 여행 계획에 포함된 도시들 번호 입력받기
travel = list(map(int, input().split()))

parent = [i for i in range(n + 1)]    # 부모 테이블 자기 자신으로 초기화
  
# 도시들에 대해 union_find로 연결 여부 확인
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if graph[i][j] == 1:
            union_parent(parent, i + 1, j + 1)


# 여행 계획에 포함된 도시들의 root가 모두 같은지 확인
root = find_parent(parent, travel[0])
is_possible = True
for city in travel[1:]:
    if find_parent(parent, city) != root:
        is_possible = False
        break
    
if is_possible:
    print("YES")
else:
    print("NO")
### test case ###
# 5 4
# 0 1 0 1 1
# 1 0 1 1 0
# 0 1 0 0 0
# 1 1 0 0 0
# 1 0 0 0 0
# 2 3 4 3