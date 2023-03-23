n, m = map(int, input().split())
arr = [[0] * (m+1) for _ in range(n+1)]
for i in range(1, n+1):
    lst = list(map(int, input().split()))
    # 누적합 구해서 arr에 저장
    for j in range(1, m+1):
        arr[i][j] = arr[i][j-1] + lst[j-1]
# 합 구하기
for _ in range(int(input())):
    i, j, x, y = map(int, input().split())
    res = 0
    for r in range(i, x+1):
        res += arr[r][y] - arr[r][j-1]
    print(res)