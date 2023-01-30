import sys

n, m = map(int, sys.stdin.readline().split())
s = set()
for _ in range(n):
    s.add(sys.stdin.readline())

ans = 0    
for _ in range(m):
    if sys.stdin.readline() in s:
        ans += 1
        
print(ans)