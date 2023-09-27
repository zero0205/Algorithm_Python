n, m = map(int, input().split())
ans = 0
for i in range(n, n*m+1, n):
    if i % m != 0:
        ans += 1
print(ans)
