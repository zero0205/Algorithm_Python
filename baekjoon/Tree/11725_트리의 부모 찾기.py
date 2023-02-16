from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n+1)]
ans = [1] * (n + 1)
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
    
q = deque([(0, 1)])
visited = [False] * (n+1)
visited[1] = True

while q:
    parent, child = q.popleft()
    ans[child] = parent
    for next in tree[child]:
        if not visited[next]:
            q.append((child, next))
            visited[next] = True

for i in ans[2:]:
    print(i)