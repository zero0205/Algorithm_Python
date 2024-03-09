from itertools import combinations

n, m = map(int, input().split())
h = list(map(int, input().split()))

prime = [True]*10000
for i in range(2, 10000):
    if prime[i]:
        for j in range(i*2, 10000, i):
            prime[j] = False
ans = set()
for comb in combinations(range(n), m):
    total = 0
    for c in comb:
        total += h[c]
    if prime[total]:
        ans.add(total)
if ans:
    print(*sorted(list(ans)))
else:
    print(-1)
