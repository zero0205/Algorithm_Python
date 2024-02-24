n = int(input())
rgb = [list(map(int, input().split())) for _ in range(n)]
gom_r, gom_g, gom_b = map(int, input().split())

ans = int(1e9)


def bt(idx, r, g, b, k):
    global ans
    if idx >= n:
        return
    # 이번 색 넣음
    mun_r = r+rgb[idx][0]
    mun_g = g+rgb[idx][1]
    mun_b = b+rgb[idx][2]
    diff = abs(mun_r//(k+1)-gom_r)+abs(mun_g//(k+1)-gom_g)+abs(mun_b//(k+1)-gom_b)
    if k+1 >= 2 and ans > diff:
        ans = diff
    if k+1 < 7:
        bt(idx+1, mun_r, mun_g, mun_b, k+1)
    # 이번색 안 넣음
    bt(idx+1, r, g, b, k)
    
    
bt(0, 0, 0, 0, 0)
print(ans)
