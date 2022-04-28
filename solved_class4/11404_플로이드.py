# https://www.acmicpc.net/problem/11404

INF = int(1e9)

n = int(input())
m = int(input())
bus = [[INF] * (n + 1) for _ in range(n + 1)]
# 자기자신으로 가는 값은 0으로 초기화
for i in range(n + 1):
    bus[i][i] = 0
    
for _ in range(m):
    a, b, c = map(int, input().split())
    bus[a][b] = min(bus[a][b], c)
    
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            bus[i][j] = min(bus[i][j], bus[i][k] + bus[k][j])
            
for r in range(1, n + 1):
    for c in range(1, n + 1):
        if bus[r][c] == INF:
            print(0, end=" ")
        else:
            print(bus[r][c], end=" ")
    print()