import sys
input = sys.stdin.readline

n = int(input()) 
m = int(input())
comp = [[False] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())    # a > b
    comp[a][b] = True
    
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            if comp[a][b]:
                continue
            if (comp[a][k] and comp[k][b]):
                comp[a][b] = True

for i in range(1, n+1):
    cnt = 0
    for j in range(1, n+1):
        if not comp[i][j] and not comp[j][i] and i != j:
            cnt += 1
    print(cnt)