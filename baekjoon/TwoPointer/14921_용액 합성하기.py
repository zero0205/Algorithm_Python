n = int(input())
liquid = list(map(int, input().split()))

start, end = 0, n-1
ans = int(1e9)
while start < end:
    mix = liquid[start] + liquid[end]
    if mix < 0:
        start += 1
    else:
        end -= 1
    if abs(ans) > abs(mix):
        ans = mix
print(ans)
