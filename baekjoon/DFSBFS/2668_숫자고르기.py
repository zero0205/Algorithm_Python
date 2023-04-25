n = int(input())
arr = [[] for _ in range(n+1)]
for i in range(1, n+1):
    arr[int(input())].append(i)
    
ans = []
def dfs(node, visited):
    visited.add(node)
    checked[node] = True
    for nx in arr[node]:
        if nx not in visited:
            dfs(nx, set(visited))
        else:   # 사이클 발생
            ans.extend(list(visited))
            return

checked = [False] * (n+1)
for i in range(1, n+1):
    if not checked[i]:
        dfs(i, set())
print(len(ans))
print(*sorted(ans), sep='\n')