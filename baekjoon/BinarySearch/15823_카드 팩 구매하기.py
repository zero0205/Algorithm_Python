import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))


def chk(num):   # Two Pointer
    pack = set()
    l, r = 0, 0
    cnt = 0
    while r < n:
        if arr[r] not in pack:
            pack.add(arr[r])
            r += 1
        else:
            while arr[l] != arr[r]:
                l += 1
            l += 1
            r = l
            pack = set()
        if len(pack) == num:
            cnt += 1
            if cnt == m:
                return True
            pack = set()
    return False


def bs():   # Parametric Search
    s, e = 1, n
    ans = 0
    while s <= e:
        mid = (s+e)//2
        if chk(mid):
            s = mid+1
            ans = mid
        else:
            e = mid-1
    return ans


print(bs())
