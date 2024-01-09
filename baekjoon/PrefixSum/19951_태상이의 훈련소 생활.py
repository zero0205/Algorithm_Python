import sys
input = sys.stdin.readline

n, m = map(int, input().split())
h = list(map(int, input().split()))
cmd = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, k = map(int, input().split())
    cmd[a].append((k, True))
    cmd[b].append((k, False))

tmp = 0
for i in range(1, n+1):
    plus = 0
    minus = 0
    for c in cmd[i]:
        if c[1]:
            plus += c[0]
        else:
            minus += c[0]
    tmp += plus
    h[i-1] += tmp
    tmp -= minus

print(*h)
