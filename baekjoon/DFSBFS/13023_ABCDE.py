n, m = map(int, input().split())
friend = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    friend[a].append(b)
    friend[b].append(a)
    
def dfs(node, cnt, visited):
    visited.add(node)
    if len(visited) == 5:
        print(1)
        exit()
    for nx in friend[node]:
        if nx not in visited:
            dfs(nx, cnt+1, set(visited))

for i in range(n):
    dfs(i, 1, set())
print(0)