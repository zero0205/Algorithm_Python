from math import sqrt

n = int(input())


def prime_number(n):
    is_prime = [True]*(n+1)
    is_prime[0] = False
    is_prime[1] = False

    for i in range(2, int(sqrt(n))+1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False

    prime = []
    for i in range(2, n+1):
        if is_prime[i]:
            prime.append(i)
    return prime


prime = prime_number(n)
dp = [0]*(n+1)
dp[0] = 1
for p in prime:
    for j in range(p, n+1):
        dp[j] = (dp[j] + dp[j-p]) % 123_456_789

print(dp[n])
