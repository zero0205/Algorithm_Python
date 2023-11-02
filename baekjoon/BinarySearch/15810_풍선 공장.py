import sys
input = sys.stdin.readline

n, m = map(int, input().split())
times = list(map(int, input().split()))

s, e = 0, max(times)*m
ans = 0
while s <= e:
    mid = (s+e)//2
    total = 0
    for t in times:
        total += mid//t
    if total >= m:
        ans = mid
        e = mid - 1
    else:
        s = mid + 1
print(ans)
