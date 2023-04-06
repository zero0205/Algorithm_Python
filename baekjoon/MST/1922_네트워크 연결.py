from heapq import heappop, heappush

n = int(input())

parent = [i for i in range(n+1)]
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
        
network = []
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    heappush(network, (c, a, b))
    
ans, cnt = 0, 1
while network:
    c, a, b = heappop(network)
    if find(a) != find(b):  # 사이클을 만들지 않는다면 union
        union(a, b)
        ans += c
        cnt += 1
    if cnt == n:    # 모든 컴퓨터 연결 완료
        break
print(ans)