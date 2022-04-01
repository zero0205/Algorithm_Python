# https://www.acmicpc.net/problem/14500

import sys 
input = sys.stdin.readline

def dfs(r, c, idx, total):
    global ans
    # 백트래킹 : 이제까지 구해진 최대값(ans)보다 작음이 명확하면 더이상 dfs를 진행하지 않음
    if ans >= total + max_val * (3 - idx): 
        return
    # 테트로미노 완성
    if idx == 3:
        ans = max(ans, total)
        return
    else:
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            # 범위를 벗어나지 않고 아직 방문하지 않은 칸이라면 진행
            if (0 <= nr < n) and (0 <= nc < m) and not visited[nr][nc]:
                # ㅗ 만들기 : + 모양에서 한 방향만 방문 처리를 해서 안 가게 함
                if idx == 1:    
                    visited[nr][nc] = True
                    dfs(r, c, idx + 1, total + arr[nr][nc])
                    visited[nr][nc] = False
                visited[nr][nc] = True
                dfs(nr, nc, idx + 1, total + arr[nr][nc])
                visited[nr][nc] = False

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
    
visited = [([False] * m) for _ in range(n)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
ans = 0
max_val = max(map(max, arr))    # 백트래킹하려고

for r in range(n):
    for c in range(m):
        visited[r][c] = True
        dfs(r, c, 0, arr[r][c])
        visited[r][c] = False

print(ans)