n = int(input())
color = [[] for _ in range(n+1)]
for _ in range(n):
    x, y = map(int, input().split())
    color[y].append(x)

ans = 0

for i in range(1, n+1):
    color[i].sort()
    for j in range(len(color[i])):
        if j == 0:
            ans += color[i][j+1]-color[i][j]
        elif j == len(color[i])-1:
            ans += color[i][j]-color[i][j-1]
        else:
            ans += min(color[i][j]-color[i][j-1], color[i][j+1]-color[i][j])

print(ans)
