from collections import deque
 
n = int(input())
 
def bfs(n):
    q = deque([(n, [n])])
    visited = [False for _ in range(n + 1)]
    visited[n] = True
    
    while q:
        now, arr = q.popleft()
        if now == 1:
            print(len(arr)-1)
            for i in arr:
                print(i, end=" ")
            break
        if now % 3 == 0:
            nx = now // 3
            if not visited[nx]:
                q.append((nx, arr + [nx]))
                visited[nx] = True
        if now % 2 == 0:
            nx = now // 2
            if not visited[nx]:
                q.append((nx, arr + [nx]))
                visited[nx] = True
        nx = now - 1
        if not visited[nx]:
            q.append((nx, arr + [nx]))
            visited[nx] = True
            
bfs(n)

#######################################
########### Bottom-Up #################

from collections import deque

n2 = int(input())

def bfs2(n):
    q = deque([(1, [1])])
    visited = [False for _ in range(n + 1)]
    visited[1] = True
    
    while q:
        now, arr = q.popleft()
        if now == n:    # n에 처음 도달하는 것이 최단 루트
            print(len(arr)-1)
            for i in arr[::-1]:
                print(i, end=" ")
            break
        for nx in [now*3, now*2, now+1]:
            if nx <= n and not visited[nx]:
                q.append((nx, arr + [nx]))
                visited[nx] = True
            
bfs2(n2)           