def chk(mid, berry, cnt):
    start = 0
    for c in cnt:
        gap = berry[start+c]-berry[start]+1
        if gap < mid:
            return False
    return True


def solution(n, berry, cnt):
    answer = 0
    berry = [1] + berry + [n-1]
    s, e = 1, n
    while s <= e:
        mid = (s+e)//2
        if chk(mid, berry, cnt):
            e = mid - 1
            answer = mid
        else:
            s = mid + 1
    return answer

# solution(16, [1, 3, 8, 9, 13, 16], [2, 2, 2])
# 5
