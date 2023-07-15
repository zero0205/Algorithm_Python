import sys
input = sys.stdin.readline

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return
    if a <= b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
parent = [i for i in range(v+1)]
degree = [0] * (v+1)
for _ in range(e):
    a, b = map(int, input().split())
    union(a,b)
    degree[a] += 1
    degree[b] += 1

# 루트 노드 정보 다시 한 번 업데이트
for i in range(1, v+1):
    find(i)

# 모두 같은 그래프에 속해 있는지 확인
if len(set(parent[1:])) != 1:
    print("NO")
    exit()

# 각 정점의 차수 확인(차수가 홀수개인 정점이 0개이거나 2개이어야 가능)
odd_degree = 0  # 차수가 홀수인 정점 개수
for i in range(1, v+1):
    if degree[i] % 2 == 1:
        odd_degree += 1
print("YES" if (odd_degree < 4) else "NO")