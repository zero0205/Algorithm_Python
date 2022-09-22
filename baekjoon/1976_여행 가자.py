n = int(input())
m = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
plan = list(map(int, input().split()))

parent = [i for i in range(n+1)]
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if graph[i][j] == 1:
            union(i+1, j+1)
            
tmp = find(plan[0])
for p in plan[1:]:
    if tmp != find(p):
        print("NO")
        exit()
        
print("YES")