import sys
input = sys.stdin.readline

n, k, m = map(int, input().split())
gimbabs = []
for _ in range(n):
    length = int(input())
    if length <= k:
        continue
    if length < (k*2):
        length -= k
    else:
        length -= (k*2)
    if length == 0:
        continue
    gimbabs.append(length)

if not gimbabs:
    print(-1)
else:
    start, end = 1, max(gimbabs)
    ans = -1
    while start <= end:
        p = (start + end) // 2
        res = 0
        for gb in gimbabs:
            res += (gb//p)
        if res < m:
            end = p-1
        else:
            start = p+1
            ans = p
    print(ans)