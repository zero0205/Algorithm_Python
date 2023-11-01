import sys
input = sys.stdin.readline

n, m = map(int, input().split())
times = list(map(int, input().split()))
if n < m:
    print(n)
else:
    s, e = 0, sys.maxsize
    minute = 0  # 원하는 명수를 태운 시점
    while s <= e:
        mid = (s+e)//2
        total = m
        for t in times:
            total += (mid//t)
        if total >= n:
            e = mid-1
            minute = mid
        else:
            s = mid+1
    cnt = m
    # 원하는 명수를 태우기 1분 전 탄 사람들의 수 총합
    for t in times:
        cnt += (minute-1)//t
    # 원하는 명수를 태운 시점에 탈 수 있었던 놀이기구 파악
    for i in range(len(times)):
        if (minute % times[i]) == 0:
            cnt += 1
        if cnt == n:
            print(i+1)
            break
