from math import sqrt

a, b = map(int, input().split())
# 에라토스테네스의 체
is_prime = [True]*(int(sqrt(b))+1)
is_prime[1] = False
for i in range(2, int(sqrt(b))+1):
    if is_prime[i]:
        for j in range(i*2, int(sqrt(b))+1, i):
            is_prime[j] = False

# 2~int(sqrt(b)) 사이의 소수들의 제곱수 중 a~b 사이에 존재하는 수의 개수 구하기
ans = 0
for i in range(2, int(sqrt(b))+1):
    if is_prime[i]:
        # 소수의 N제곱수들 (N>=2)
        tmp = i**2
        while tmp <= b:
            if a <= tmp <= b:
                ans += 1
            tmp *= i
print(ans)
