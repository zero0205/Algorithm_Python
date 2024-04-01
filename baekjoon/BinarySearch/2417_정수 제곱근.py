n = int(input())

s, e = 0, n
ans = 0
while s <= e:
    mid = (s+e)//2
    if mid ** 2 < n:
        s = mid+1
    else:
        ans = mid
        e = mid-1
print(ans)
