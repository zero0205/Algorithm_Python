# n,l,r 입력받기
from collections import deque
from pydoc import visiblename


n, l, r = map(int, input().split())
# 인구수 입력
map_data = []
for i in range(n):
    map_data.append(list(map(int, input().split())))
    
def bfs(graph, visited, loc):
    global l,r
    dir = [(-1,0),(1,0),(0,-1),(0,1)]
    que = deque([loc])
    visited[loc[0]][loc[1]] = True
    visited_country = []
    people = 0
    is_execute = False
    while que:
        row, col = que.popleft()
        people += graph[row][col]
        for d in dir:
            nr = row + d[0]
            nc = col + d[1]
            if nr < 0 or nr >= len(graph) or nc < 0 or nc >= len(graph):
                continue
            if l <= abs(graph[nr][nc] - graph[row][col]) <= r and not visited[nr][nc]:  
                que.append((nr, nc))
                visited[nr][nc] = True
                visited_country.append((nr,nc))
                is_execute = True
    if not is_execute:
        return False
    for cr,cc in visited_country:
        graph[cr][cc] = people // len(visited_country)
    return True
    
visited = [[False] * n for _ in range(n)]
is_done = False
cnt = 0 

while not is_done:
    for i in range(n):
        for j in range(n):
            if bfs(map_data, visited, (i,j)):
                cnt += 1                
            else:
                is_done = True
print(cnt)