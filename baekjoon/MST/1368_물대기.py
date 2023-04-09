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
    if a == b:  # 사이클을 형성
        return
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
costs = []  # i번째 논에 우물 파는데 드는 비용 = 0번(가상의 논)에서 i번으로 물 대주는 비용
for i in range(1, n+1):
    heappush(costs, (int(input()), 0, i))
    
# i번째 논과 j번째 논을 연결하는데 드는 비용
for i in range(1, n+1):  
    arr = [0] + list(map(int, input().split()))
    for j in range(i+1, n+1):
        heappush(costs, (arr[j], i, j))
ans = 0
cnt = 0
while costs:
    c, a, b = heappop(costs)
    # 연결하는데 드는 비용
    if find(a) != find(b):
        union(a,b)
        ans += c
        cnt += 1
        if cnt == n:
            break        
print(ans)