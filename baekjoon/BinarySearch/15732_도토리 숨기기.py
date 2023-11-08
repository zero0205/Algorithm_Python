import sys
input = sys.stdin.readline

n, k, d = map(int, input().split())
rules = []
for _ in range(k):
    a, b, c = map(int, input().split())
    rules.append((a, b, c))

s, e = 1, 1_000_000
ans = 0
while s <= e:
    mid = (s+e)//2
    total = 0
    for r in rules:
        if r[0] > mid:
            continue
        total += ((min(r[1], mid)-r[0])//r[2] + 1)
    if total >= d:
        e = mid-1
        ans = mid
    else:
        s = mid+1

print(ans)
