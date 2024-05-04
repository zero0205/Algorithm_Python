import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    input_data = list(map(int, input().split()))
    arr.append(input_data[1:])

dp = [[[]for _ in range(10)] for _ in range(n)]
for a in arr[0]:    # 첫째날
    dp[0][a] = [a]
for i in range(1, n):
    for a in arr[i]:
        for j in range(1, 10):
            if a != j and dp[i-1][j] != []:
                dp[i][a] = dp[i-1][j]+[a]
                break

for i in range(1, 10):
    if dp[n-1][i] != []:
        for j in range(n):
            print(dp[n-1][i][j])
        exit()
print(-1)
