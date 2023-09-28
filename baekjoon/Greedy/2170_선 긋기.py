import sys
input = sys.stdin.readline

n = int(input())
line = []
for _ in range(n):
    a, b = map(int, input().split())
    line.append([a, b])
line.sort()
ans = 0
s, e = line[0]
for i in range(1, n):
    if line[i][0] > e:
        ans += (e-s)
        s = line[i][0]
        e = line[i][1]
    else:
        e = max(e, line[i][1])
ans += (e-s)
print(ans)
