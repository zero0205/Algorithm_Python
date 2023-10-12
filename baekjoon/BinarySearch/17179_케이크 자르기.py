n, m, l = map(int, input().split())
cut_loc = [int(input()) for _ in range(m)]+[l]
cut_num = [int(input()) for _ in range(n)]


def chk(min_l):
    s, cnt = 0, 0
    for loc in cut_loc:
        if loc - s >= min_l:
            cnt += 1
            s = loc
    return cnt  # 잘라진 조각 개수


for num in cut_num:
    start, end = 1, l
    ans = 0
    while start <= end:
        mid = (start+end) // 2
        if chk(mid) > num:  # 원하는 횟수 이상으로 자르기 가능
            start = mid + 1
            ans = max(ans, mid)
        else:
            end = mid - 1
    print(ans)
