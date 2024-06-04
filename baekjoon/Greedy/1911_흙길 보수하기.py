from math import ceil
import sys
input = sys.stdin.readline

n, l = map(int, input().split())
woongs = []
for _ in range(n):
    s, e = map(int, input().split())
    woongs.append((s, e))

woongs.sort()

ans = 0
prev = -1_000_000
for i in range(n):
    if prev <= woongs[i][0]:
        prev = woongs[i][0]
    num = ceil((woongs[i][1]-prev)/l)
    ans += num
    prev = prev + num*l
print(ans)
