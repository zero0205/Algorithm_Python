n, t = map(int, input().split())
alcohol = [list(map(int, input().split())) for _ in range(n)]

s, e = 1, int(1e9)
ans = int(1e9)
while s <= e:
    mid = (s+e)//2
    # 나눠주는 술의 총량 계산
    low, high = 0, 0
    for i in range(n):
        if alcohol[i][0] > mid:
            low = -1
            break
        low += alcohol[i][0]
        high += min(mid, alcohol[i][1])
    if low == -1 or high < t:
        s = mid+1
    else:
        if low <= t <= high:
            ans = min(ans, mid)
        e = mid-1
print(ans if ans != int(1e9) else -1)
