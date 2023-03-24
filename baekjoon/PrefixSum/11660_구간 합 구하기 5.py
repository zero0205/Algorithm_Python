import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [[0] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    lst = list(map(int, input().split()))
    # (1, 1)부터 (i, j)까지 누적합 구해서 arr에 저장
    for j in range(1, n+1):
        arr[i][j] = arr[i-1][j] + arr[i][j-1] - arr[i-1][j-1] + lst[j-1]

# 합 구하기
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    res = arr[x2][y2] - arr[x2][y1-1] - arr[x1-1][y2] + arr[x1-1][y1-1]
    print(res)