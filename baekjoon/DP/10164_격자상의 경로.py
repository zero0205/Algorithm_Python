n, m, k = map(int, input().split())


def find_path(r, c):    # 세로 길이가 r, 가로 길이가 c인 격자에서 경로의 개수 구하기
    dp = [[0]*(c) for _ in range(r)]
    dp[0][0] = 1
    for i in range(r):
        for j in range(c):
            if i+1 < r:
                dp[i+1][j] += dp[i][j]
            if j+1 < c:
                dp[i][j+1] += dp[i][j]
    return dp[r-1][c-1]


if k == 0:
    print(find_path(n, m))
else:
    r = (k-1)//m
    c = (k-1) % m
    # k에 도달할 때까지의 경우의 수
    prev = find_path(r+1, c+1)
    # k부터 N X M까지의 경우의 수
    next = find_path(n-r, m-c)
    print(prev*next)
