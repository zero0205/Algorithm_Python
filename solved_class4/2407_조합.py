# https://www.acmicpc.net/problem/2407

# from math import factorial

# n, m = map(int, input().split())
# print(factorial(n) // (factorial(n - m) * factorial(m)))

############################
f = [0] * 101
def fact(n):
    if n == 0 or n == 1:
        return 1
    if f[n] == 0:
        f[n] = fact(n - 1) * n
    return f[n]

n, m = map(int, input().split())
print(fact(n) // (fact(n - m) * fact(m)))