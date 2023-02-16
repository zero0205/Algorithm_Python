import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin = []
for _ in range(n):
    coin.append(int(input()))

ans = 0
for i in range(n-1, -1, -1):
    ans += k // coin[i]
    k = k % coin[i]

print(ans)