from heapq import heappop, heappush
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
beers = []
for _ in range(k):
    v, c = map(int, input().split())    # 선호도, 도수 레벨
    beers.append([v, c])

beers.sort(key=lambda x: x[1])  # 도수 레벨 오름차순 정렬


def solution():
    picked = []  # 고른 맥주들
    preference = 0  # 고른 맥주들의 선호도 합

    for b in beers:
        heappush(picked, b)
        preference += b[0]
        if len(picked) >= n:    # 맥주를 n개 골랐다면?
            if preference >= m:
                return b[1]  # 이번에 preference에 들어간 맥주
            else:
                preference -= heappop(picked)[0]

    return -1


print(solution())
