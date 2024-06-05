m, n = map(int, input().split())
l = list(map(int, input().split()))

s, e = 1, max(l)
ans = 0
while s <= e:
    mid = (s+e)//2  # 과자 길이
    # 길이 mid로 잘랐을 때 만들 수 있는 과자 개수 구하기
    total = 0
    for i in range(n):
        total += l[i]//mid
    if total >= m:
        s = mid+1
        ans = mid
    else:
        e = mid-1

print(ans)
