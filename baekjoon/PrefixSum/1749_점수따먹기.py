import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ps = [[0]*(m+1) for _ in range(n+1)]    # 누적합 저장 행렬
for i in range(1, n+1):
    arr = list(map(int, input().split()))
    for j in range(1, m+1):
        ps[i][j] = ps[i-1][j] + ps[i][j-1] + arr[j-1] - ps[i-1][j-1]

ans = -int(1e9)
for x2 in range(1, n+1):
    for y2 in range(1, m+1):
        for x1 in range(1, x2+1):
            for y1 in range(1, y2+1):
                s = ps[x2][y2] - ps[x1-1][y2] - ps[x2][y1-1] + ps[x1-1][y1-1]
                if s > ans:
                    ans = s
print(ans)