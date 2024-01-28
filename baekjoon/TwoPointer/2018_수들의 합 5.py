n = int(input())
left, right = 0, 1
ans = 0
total = 1   # left~right 구간의 수들의 합
while left <= n:
    if total == n:
        ans += 1
        left += 1
        right += 1
        total = (total-(left-1)+right)
    elif total < n:
        right += 1
        total += right
    else:
        total -= left
        left += 1
print(ans)
