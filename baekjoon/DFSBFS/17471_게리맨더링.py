from itertools import combinations
from collections import deque


def bfs(start, visited, a, b):
    q = deque([start])
    visited[start] = True
    res = population[start]
    while q:
        now = q.popleft()
        for nx in graph[now]:
            if not visited[nx] and (((now in a) and (nx in a)) or ((now in b) and (nx in b))):
                q.append(nx)
                visited[nx] = True
                res += population[nx]
    return res


n = int(input())
population = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
for i in range(1, n+1):
    input_data = list(map(int, input().split()))
    if input_data[0] == 0:
        continue
    graph[i] = input_data[1:]
all = set(range(1, n+1))
ans = int(1e9)
for a_num in range(1, n//2+1):
    for a in combinations(all, a_num):
        a = set(a)
        b = all - a
        res = []
        visited = [False] * (n+1)
        for i in range(1, n+1):
            if not visited[i]:
                res.append(bfs(i, visited, a, b))
        if len(res) == 2:
            ans = min(ans, abs(res[0]-res[1]))
print(ans if ans != int(1e9) else -1)
