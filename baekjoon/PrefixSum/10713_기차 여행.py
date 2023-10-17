import sys
input = sys.stdin.readline

n, m = map(int, input().split())
path = list(map(int, input().split()))
fee = [[] for _ in range(n)]
for i in range(1, n):
    fee[i] = list(map(int, input().split()))
# 철도 이용횟수 누적합
accum = [0] * (n+1)
for i in range(m-1):
    if path[i] < path[i+1]:
        accum[path[i]] += 1
        accum[path[i+1]] -= 1
    else:
        accum[path[i+1]] += 1
        accum[path[i]] -= 1
ans = 0
a = 0
for i in range(1, n):
    a += accum[i]
    ticket = fee[i][0] * a
    card = fee[i][2] + fee[i][1] * a
    ans += min(ticket, card)
print(ans)
