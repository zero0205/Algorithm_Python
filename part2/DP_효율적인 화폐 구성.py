# n, m 입력받기
n, m = map(int, input().split())

# 화폐 종류 입력 받기
coin = []
for i in range(n):
    coin.append(int(input()))

# DP 테이블 만들기
d = [10001] * 10001
d[0] = 0

# 코인 1개로만 만들 수 있는 금액들
for c in coin:
    d[c] = 1

for i in range(m + 1):
    for c in coin:
        if (i - c) < 0: # 인덱스 범위를 벗어나면 안되니까
            continue
        d[i] = min(d[i - c] + 1, d[i])
            
if d[m] == 10001:
    print(-1)
else:
    print(d[m])