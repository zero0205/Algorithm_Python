from itertools import combinations

n, l, r, x = map(int, input().split())
difficulty = list(map(int, input().split()))

ans = 0
for i in range(2, n+1):
    for diff in combinations(difficulty, i):
        if (l <= sum(diff) <= r) and (max(diff)-min(diff) >= x):
            ans += 1
print(ans)