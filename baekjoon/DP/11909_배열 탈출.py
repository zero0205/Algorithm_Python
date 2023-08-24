import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

cost = [[int(1e9)]*n for _ in range(n)]
cost[0][0] = 0
for i in range(n):
    for j in range(n):
        for a, b in [(0, 1), (1, 0)]:
            nr, nc = i+a, j+b
            if nr >= n or nc >= n:
                continue
            next_cost = cost[i][j]+(0 if arr[i][j] >
                                    arr[nr][nc] else arr[nr][nc]-arr[i][j]+1)
            if next_cost < cost[nr][nc]:
                cost[nr][nc] = next_cost
print(cost[n-1][n-1])
