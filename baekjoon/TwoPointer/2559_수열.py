n, k = map(int, input().split())
temp = list(map(int, input().split()))

total = sum(temp[:k])
ans = total
for i in range(n-k):
    total = total - temp[i] + temp[i+k]
    if ans < total:
        ans = total
print(ans)
