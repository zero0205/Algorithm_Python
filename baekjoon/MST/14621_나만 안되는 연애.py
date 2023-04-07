from heapq import heappop, heappush

n, m = map(int, input().split())
univ = ["N"] + input().split()
parent = [i for i in range(n+1)]
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:  # 사이클을 형성
        return
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
roads = []
for _ in range(m):
    u, v, d = map(int, input().split())
    heappush(roads, (d, u, v))

dist, cnt = 0, 1  
while roads:
    c, a, b = heappop(roads)
    if univ[a] == univ[b]:  # 같은 성별 학교
        continue
    if find(a) != find(b):  # 사이클 형성하는지 체크
        union(a,b)
        dist += c
        cnt += 1
    if cnt == n:  # 경로 완성
        print(dist)
        exit()
print(-1)