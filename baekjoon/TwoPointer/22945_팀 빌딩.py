n = int(input())
ability = list(map(int, input().split()))

start, end = 0, n-1
ans = 0
while start < end:
    if ability[start] < ability[end]:
        ans = max(ans, (end-start-1) * ability[start])
        start += 1
    else:
        ans = max(ans, (end-start-1) * ability[end])
        end -= 1
print(ans)