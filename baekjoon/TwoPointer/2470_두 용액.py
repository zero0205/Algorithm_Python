n = int(input())
liquid = sorted(list(map(int, input().split())))

start, end = 0, n - 1
min_mix = int(1e9) * 2
ans = []
while start < end:
    now_mix = liquid[start] + liquid[end]
    if abs(now_mix) < abs(min_mix):
        min_mix = now_mix
        ans = [liquid[start], liquid[end]]
    if now_mix < 0:
        start += 1
    else:
        end -= 1
print(*ans)