n, t, p = map(int, input().split())
time = []
for _ in range(t):
    s, e = map(int, input().split())
    s = s//100*60+s % 100
    e = e//100*60+e % 100
    time.append((s, e))
time.sort()
ans = 60*12


def find_seat(arr):  # 앉을 자리 선택
    if not arr:  # 아무도 없는 경우
        return 1
    candidate = []  # 앉을 자리 후보
    if arr[0][0] != 1:  # 1번 좌석
        candidate.append((arr[0][0]-1, 1))
    if arr[-1][0] != n:  # N번 좌석
        candidate.append((n-arr[-1][0], n))
    for i in range(1, len(arr)):    # 지금 앉아있는 사람들의 사이 좌석
        candidate.append(((arr[i][0]-arr[i-1][0])//2,
                         (arr[i][0]+arr[i-1][0])//2))
    # 조건에 맞는 자리 1자리만 리턴
    return sorted(candidate, key=lambda x: (-x[0], x[1]))[0][1]


used = []
for s, e in time:
    new_used = []   # 현재(시간: s) 사용중인 좌석
    for u in used:  # 퇴실한 좌석 걸러내기
        if u[1] > s:
            new_used.append(u)
    res = find_seat(new_used)   # 좌석 선택
    if res == p:    # 민규가 좋아하는 자리에 누가 앉음
        ans -= (e-s)
    new_used.append((res, e))
    used = sorted(new_used)
print(ans)
