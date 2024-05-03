import sys
input = sys.stdin.readline

n = int(input())
v = list(map(int, input().split()))

ans = v[-1]
for i in range(n-2, -1, -1):
    if ans % v[i] != 0:
        ans = (ans//v[i]+1)*v[i]
print(ans)
