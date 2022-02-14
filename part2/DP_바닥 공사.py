# n 입력받기
n = int(input())

# DP 테이블
d = [0] * 1001

d[1] = 1
d[2] = 3

for i in range(3, n + 1):
    d[i] = d[i-1] + d[i-2] * 2

# 796,796으로 나눈 나머지 출력
print(d[n] % 796796)