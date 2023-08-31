from itertools import permutations
from math import sqrt

# 에라토스테네스의 체
prime = [True] * 98765
prime[0] = False
prime[1] = False
for i in range(2, int(sqrt(98765))+1):
    if prime[i]:
        for j in range(i*i, 98765, i):
            prime[j] = False


def chk(num, m):
    flag = False
    # 서로 다른 두 개의 소수의 합인 경우
    for i in range(2, num//2+1):
        if i != (num-i) and prime[i] and prime[num-i]:
            flag = True
            break
    if not flag:
        return False
    # M으로 나누어 떨어지지 않을 때까지 나눈 수가 두 개의 소수의 곱인 경우
    while num % m == 0:
        num //= m
    for i in range(2, int(sqrt(num))+1):
        if num % i == 0 and prime[i] and prime[num//i]:
            return True
    return False


k, m = map(int, input().split())
ans = 0
for p in permutations(range(0, 10), k):
    p = list(map(str, p))
    if p[0] == '0':
        continue
    num = int(''.join(p))
    if chk(num, m):
        ans += 1
print(ans)
