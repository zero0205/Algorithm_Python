# n 입력받기
n = int(input())
# 상담 스케줄 입력
data = []
for i in range(n):
    t, p = map(int, input().split())
    data.append((i + 1, t, p))   # 날짜, 상담소요기간, 금액

dp_table = [0] * (n + 1)
dp_table[1] = data[0][2]

for i, t, p in data:
    idx = i
    # n일 이후까지 상담을 해야해서 불가능한 경우
    if i + data[i-1][1] > (n + 1):
        continue
    dp_table[idx] = max(dp_table[idx], data[idx-1][2])
    while idx < len(data):
        n_idx = idx + data[idx-1][1]
        if n_idx > n:   # 범위를 벗어남
            break
        # n_idx에 있는 상담은 N일 이후까지 해야돼서 못하는 경우
        if n_idx + data[n_idx - 1][1] > (n + 1):
            break
        dp_table[n_idx] = max(dp_table[n_idx], dp_table[idx] + data[n_idx-1][2])
        idx = n_idx

# print(data)
# print(dp_table)
print(max(dp_table))

####################################
### 답지 ###
n = int(input())    # 전체 상담 개수
t = []  # 각 상담을 완료하는 데 걸리는 시간
p = []  # 각 상담을 완료했을 때 받을 수 있는 금액
dp = [0] * (n + 1)  # 다이나믹 프로그래밍을 위한 1차원 dp 테이블 초기화
max_value = 0

for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

# 리스트를 뒤에서부터 거꾸로 확인
for i in range(n - 1, -1, -1):
    time = t[i] + i
    # 상담이 기간 안에 끝나는 경우
    if time <= n:
        # 점화식에 맞게, 현재까지의 최고 이익 계산
        dp[i] = max(p[i] + dp[time], max_value)
        max_value = dp[i]
    # 상담이 기간을 벗어나는 경우
    else:
        dp[i] = max_value

print(max_value)
