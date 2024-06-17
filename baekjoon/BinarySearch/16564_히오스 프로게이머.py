n, k = map(int, input().split())
x = [int(input()) for _ in range(n)]

s, e = 1, int(1e9)+1
ans = 0
while s <= e:
    mid = (s+e)//2
    # 목표레벨 mid로 잡으면 달성 가능한지?
    need_level = 0
    for i in range(n):
        if x[i] < mid:
            need_level += mid-x[i]
    if need_level <= k:
        s = mid+1
        ans = mid
    else:
        e = mid-1
print(ans)
