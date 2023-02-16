n = int(input())
arr = map(int, input().split())

prime = [True] * 1001
prime[1] = False 

# 에라토스테네스의 체
for i in range(2, int(1000 ** 0.5) + 1):
    if not prime:   # 이미 지워진 수
        continue
    for j in range(i * 2, 1001, i):
        prime[j] = False    # 자기자신을 제외한 배수들 지우기

ans = 0
for num in arr:
    if prime[num]:
       ans += 1
       
print(ans) 