n, m = map(int, input().split())
arr = list(map(int, input().split()))

s, e = 0, 0
partial_sum = arr[0]
ans = 0
while e < n:
    if partial_sum < m:
        e += 1
        if e >= n:
            break
        partial_sum += arr[e]
    else:
        if partial_sum == m:
            ans += 1
        partial_sum -= arr[s]
        s += 1
print(ans)
