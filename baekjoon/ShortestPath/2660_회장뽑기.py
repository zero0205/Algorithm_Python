n = int(input())
dist = [[50]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    dist[i][i] = 0
while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    dist[a][b] = 1
    dist[b][a] = 1

# Floyd-Warshall
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if dist[i][j] > dist[i][k]+dist[k][j]:
                dist[i][j] = dist[i][k]+dist[k][j]

cm, cm_score = [], 50
for i in range(1, n+1):
    score = 0
    for j in range(1, n+1):
        score = max(score, dist[i][j])
    if score < cm_score:
        cm = [i]
        cm_score = score
    elif score == cm_score:
        cm.append(i)

print(cm_score, len(cm))
print(*cm)
