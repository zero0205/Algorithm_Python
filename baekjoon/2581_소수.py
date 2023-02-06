m = int(input())
n = int(input())

prime = [True] * (n+1)
prime[1] = False 

# 에라토스테네스의 체
for i in range(2, int(n ** 0.5) + 1):
    if not prime:   # 이미 지워진 수
        continue
    for j in range(i * 2, n + 1, i):
        prime[j] = False    # 자기자신을 제외한 배수들 지우기

ans = 0
min_prime = -1
for num in range(m , n+1):
    if prime[num]:
        if min_prime == -1:
            min_prime = num
        ans += num
        
if min_prime == -1: # 범위에 소수가 없는 경우
    print(-1)
else:
    print(ans) 
    print(min_prime)