INF = int(1e9)

n = int(input())
distances = [[INF]*26 for _ in range(26)]
for i in range(n):
    a, _, b = input().split()
    a = ord(a)-97
    b = ord(b)-97
    distances[a][b] = 1

# 플로이드-워셜
for k in range(26):
    for i in range(26):
        for j in range(26):
            distances[i][j] = min(
                distances[i][j], distances[i][k]+distances[k][j])

m = int(input())
for _ in range(m):
    a, _, b = input().split()
    a = ord(a)-97
    b = ord(b)-97
    print("T" if distances[a][b] < INF else "F")
