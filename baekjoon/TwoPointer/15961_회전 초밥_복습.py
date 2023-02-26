import sys
input = sys.stdin.readline
from collections import defaultdict

n, d, k, c = map(int, input().split())
sushi = []
for _ in range(n):
    sushi.append(int(input()))
    
sushi = sushi * 2
kind = defaultdict(int)
kind[c] += 1    # 쿠폰으로 먹은 음식
for i in range(k):
    kind[sushi[i]] += 1

ans = len(kind)
for i in range(k, n + k):
    kind[sushi[i]] += 1
    kind[sushi[i-k]] -= 1
    if kind[sushi[i-k]] == 0:  # 빠진 종류
        del kind[sushi[i-k]]
    ans = max(ans, len(kind))
    
print(ans)