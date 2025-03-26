import sys
input = sys.stdin.readline

n, m = map(int, input().split())
boss = [0]+list(map(int, input().split()))

compliments = [0]*(n+1)
for _ in range(m):
    i, w = map(int, input().split())
    compliments[i] += w

for i in range(2, n+1):
    compliments[i] += compliments[boss[i]]

print(*compliments[1:])
