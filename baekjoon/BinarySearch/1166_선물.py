n, l, w, h = map(int, input().split())

s, e = 0, max(l, w, h)
ans = 0
for _ in range(100):
    mid = (s+e)/2
    boxes = (l//mid)*(w//mid)*(h//mid)
    if boxes < n:
        e = mid
    else:
        ans = mid
        s = mid
print(ans)
