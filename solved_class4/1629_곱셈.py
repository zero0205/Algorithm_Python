# https://www.acmicpc.net/problem/1629

a, b, c = map(int, input().split())

for _ in range(b - 1):
    a %= c
    a *= a

print(a % c)