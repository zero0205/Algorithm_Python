m = int(input())


def count_zero(n):  # 왼쪽 끝 0 개수 구하기
    res = 0
    while n >= 5:
        res += n//5
        n //= 5
    return res


s, e = 0, int(1e9)
ans = -1
while s <= e:
    mid = (s+e)//2
    zero = count_zero(mid)
    if zero == m:
        ans = mid
        e = mid-1
    elif zero < m:
        s = mid+1
    else:
        e = mid-1
print(ans)
