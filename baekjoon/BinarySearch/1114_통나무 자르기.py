l, k, c = map(int, input().split())
points = [0]+sorted(list(map(int, input().split())))+[l]
pieces = [points[i+1]-points[i] for i in range(k+1)]
longest = max(pieces)


def chk(length):  # 최대 길이
    if longest > length:  # 가능한 최대 길이보다 더 긴 통나무가 있는 경우
        return [10001, -1]
    tmp = 0  # 통나무 조각 길이 합
    cutting = 0  # 자른 횟수
    for p in pieces[::-1]:
        tmp += p
        if tmp > length:    # 이번 조각을 더하면 l보다 길어지게 되는 경우
            cutting += 1
            tmp = p  # 새로운 조각 시작
    return [cutting, tmp if cutting == c else pieces[0]]


# 매개 변수 탐색
s, e = 0, int(1e9)
ans = []
while s <= e:
    mid = (s+e)//2
    cutting, first = chk(mid)
    if cutting <= c:
        ans = [mid, first]
        e = mid-1
    else:
        s = mid+1
print(*ans)
