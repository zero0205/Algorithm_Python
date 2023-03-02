import sys
input = sys.stdin.readline
from math import factorial

n, m = map(int, input().split())
total = factorial(n) // (factorial(n-3) * factorial(3))
bad_comb = set()
for _ in range(m):
    a, b = map(int, input().split())
    for i in range(1, n+1):
        if i == a or i == b:
            continue
        bad_comb.add(tuple(sorted([a,b,i])))
    
print(total-len(bad_comb))