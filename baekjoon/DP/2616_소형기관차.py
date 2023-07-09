import sys
input = sys.stdin.readline

train_num = int(input())
customer = list(map(int, input().split()))
max_train = int(input())

acc = [0]   # 누적합
for i in range(train_num):
    acc.append(acc[i]+customer[i])

dp = [[0] * (train_num+1) for _ in range(4)]  # j번째 객차까지 최대 i대의 소형기관차가 운송할 수 있는 최대 고객의 수

for i in range(1, 4):
    for j in range(max_train, train_num+1):
        dp[i][j] = max(dp[i-1][j-max_train] + acc[j] - acc[j-max_train], dp[i][j-1])

print(dp[3][train_num])