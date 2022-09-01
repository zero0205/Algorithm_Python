import heapq, sys
input = sys.stdin.readline

n, m = map(int, input().split())
road = []
parent = [i for i in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    heapq.heappush(road, (c, a, b))
    
def find_parent(parent, x):
    if parent[x] != x:  # x가 루트 노드가 아니라면
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a == b:
        return False
     
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
    return True

# 하나의 큰 MST를 만들고 가장 유지비가 큰 길 하나를 마지막에 끊어서 마을을 2개로 분리
num = 0
total = 0
while road and num < n-2:
    c, a, b = heapq.heappop(road)
    if union_parent(parent, a, b):
        num += 1
        total += c

print(total)