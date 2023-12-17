n, m = map(int, input().split())
lectures = list(map(int, input().split()))


def divide(l):    # 블루레이 1개의 크기를 l분으로 할 때 블루레이의 총 개수 구하기
    res = 0
    tmp = 0
    for i in range(n):
        if lectures[i] > l:  # 강의 1개의 길이가 l보다 긴 경우
            return 1_000_000_000
        if tmp+lectures[i] > l:
            res += 1
            tmp = lectures[i]
        else:
            tmp += lectures[i]
    if tmp > 0:
        res += 1
    return res


s, e = 1, 1_000_000_000
ans = 1_000_000_000
while s <= e:
    mid = (s+e)//2
    # 블루레이 크기를 mid로 할 때 블루레이의 개수
    b = divide(mid)
    if b <= m:
        ans = mid
        e = mid-1
    elif b > m:
        s = mid+1
print(ans)
